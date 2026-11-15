#!/usr/bin/env python3
"""Offline, allowlisted Moodle 2 backup importer. No user content is exported."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import tarfile
import unicodedata
from urllib.parse import parse_qs, quote, unquote, urlsplit
import zipfile

from bs4 import BeautifulSoup, NavigableString, Tag
from defusedxml import ElementTree as ET
from markdownify import MarkdownConverter


def value(e, key, default=""):
    return e.findtext(key, default) or default


def slug(s):
    s = s.translate(str.maketrans("łŁ", "lL"))
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:100] or "material"


def digest(data):
    return hashlib.sha256(data).hexdigest()


class Archive:
    """Read members directly; never extract archive paths onto the filesystem."""
    def __init__(self, path):
        self.zip = zipfile.is_zipfile(path)
        self.handle = zipfile.ZipFile(path) if self.zip else tarfile.open(path, "r:*")
        self.names = set(self.handle.namelist() if self.zip else self.handle.getnames())
        if any(PurePosixPath(n).is_absolute() or ".." in PurePosixPath(n).parts for n in self.names):
            raise ValueError("Unsafe archive member path")
        if not self.zip and any(m.issym() or m.islnk() for m in self.handle.getmembers()):
            raise ValueError("Archive links are not accepted")

    def read(self, name):
        if self.zip:
            return self.handle.read(name)
        return self.handle.extractfile(name).read()

    def xml(self, name):
        return ET.fromstring(self.read(name))


class Converter(MarkdownConverter):
    # Keep these inline HTML elements: Markdown alone cannot express their meaning.
    def process_text(self, el, parent_tags=None):
        text = super().process_text(el, parent_tags)
        if not ({"pre", "code", "_noformat"} & set(parent_tags or [])):
            text = text.replace("<", "&lt;").replace(">", "&gt;")
        return text

    def convert_a(self, el, text, **kwargs):
        if el.get("id") and not text:
            return str(el)
        return super().convert_a(el, text, **kwargs)

    def convert_sup(self, el, text, **kwargs):
        return f"<sup>{text}</sup>"

    def convert_sub(self, el, text, **kwargs):
        return f"<sub>{text}</sub>"

    def convert_u(self, el, text, **kwargs):
        return f"<u>{text}</u>"

    def convert_ol(self, el, text, **kwargs):
        if el.get("type", "1") != "1" or el.select('[style*="list-style-type"], li[value]'):
            return "\n\n" + str(el) + "\n\n"
        return super().convert_ol(el, text, **kwargs)

    def convert_ul(self, el, text, **kwargs):
        if el.select('[style*="list-style-type"]'):
            return "\n\n" + str(el) + "\n\n"
        return super().convert_ul(el, text, **kwargs)

    def convert_table(self, el, text, **kwargs):
        # Spanned cells and multi-paragraph cells need HTML to retain their structure.
        if el.select('[rowspan], [colspan], td p, td ul, td ol, td pre'):
            return "\n\n" + str(el) + "\n\n"
        return super().convert_table(el, text, **kwargs)


def restricted(e):
    reasons = []
    if value(e, "visible", "1") != "1":
        reasons.append("hidden")
    # Conservative: even historical time windows need explicit review.
    for k in ("availablefrom", "availableuntil", "groupingid", "groupmembersonly", "groupmode", "defaultgroupingid"):
        if value(e, k) not in ("", "0", "$@NULL@$"):
            reasons.append(k)
    for k in ("availability", "availability_info", "availability_grade", "availability_completion"):
        c = e.find(k)
        if c is not None and (len(c) or (c.text or "").strip() not in ("", "0", "null", "$@NULL@$")):
            reasons.append(k)
    return reasons


class Importer:
    supported = {"page", "book", "label", "resource", "folder", "url"}

    def __init__(self, archive, site_url, policy=None):
        self.a = Archive(archive)
        self.meta = self.a.xml("moodle_backup.xml")
        self.course = self.a.xml("course/course.xml")
        self.site_url = site_url.rstrip("/") + "/"
        self.origin = value(self.meta, "information/original_wwwroot")
        self.title = value(self.course, "fullname")
        self.policy = policy or {}
        if self.policy and self.policy.get("course_id") != self.course.attrib["id"]:
            raise ValueError("Import policy is for a different course")
        self.excluded = self.policy.get("exclude_file_ids", {})
        self.files = [{**f.attrib, **{c.tag: c.text or "" for c in f}} for f in self.a.xml("files.xml") if value(f, "filename") != "."]
        self.sections = sorted((self.a.xml(n) for n in self.a.names if n.startswith("sections/") and n.endswith("/section.xml")), key=lambda s: int(value(s, "number")))
        self.activities = {}
        for n in sorted(self.a.names):
            if n.startswith("activities/") and n.endswith("/module.xml"):
                m = self.a.xml(n)
                kind = value(m, "modulename")
                a = self.a.xml(n.removesuffix("module.xml") + kind + ".xml")
                self.activities[m.attrib["id"]] = {"module": m, "root": a, "data": a.find(kind), "kind": kind, "id": m.attrib["id"], "context": a.attrib.get("contextid", ""), "title": value(a.find(kind), "name")}
        self.output = {}
        self.targets = {}
        self.chapters = {}
        self.asset_paths = {}
        self.unresolved = []
        self.external_images = []
        self.skipped = []
        self.inventory = []
        self.stats = Counter()
        self.exported_files = []

    def put(self, path, data):
        path = str(path)
        if path in self.output:
            raise ValueError(f"Output collision: {path}")
        self.output[path] = data.encode() if isinstance(data, str) else data

    def activity_files(self, a):
        areas = {"page": {"content", "intro"}, "book": {"chapter", "intro"}, "label": {"intro"}, "resource": {"content", "intro"}, "folder": {"content", "intro"}, "url": {"intro"}}
        files = [f for f in self.files if f["contextid"] == a["context"] and f["component"] == "mod_" + a["kind"] and f["filearea"] in areas.get(a["kind"], set())]
        if a["kind"] == "book" and "visible_chapter_ids" in a:
            files = [f for f in files if f["filearea"] == "intro" or f["itemid"] in a["visible_chapter_ids"]]
        return files

    def asset(self, f):
        if f["id"] in self.excluded:
            return None
        if f["id"] in self.asset_paths:
            return self.asset_paths[f["id"]]
        h = f["contenthash"]
        if not re.fullmatch(r"[a-f0-9]{40}", h):
            raise ValueError("Invalid Moodle content hash")
        source = f"files/{h[:2]}/{h}"
        if source not in self.a.names:
            self.unresolved.append({"page": "files.xml", "reference": f["id"], "reason": "Content-addressed file missing"})
            return None
        data = self.a.read(source)
        if hashlib.sha1(data).hexdigest() != h or len(data) != int(f["filesize"]):
            raise ValueError(f"Corrupt Moodle file {f['id']}")
        suffix = Path(f["filename"]).suffix.lower()
        if not re.fullmatch(r"\.[a-z0-9]+", suffix):
            suffix = ""
        name = slug(Path(f["filename"]).stem) + "-f" + f["id"] + suffix
        target = "assets/" + name
        self.put("docs/" + target, data)
        self.asset_paths[f["id"]] = target
        self.exported_files.append({"file_id": f["id"], "path": target, "mimetype": f["mimetype"], "license": f.get("license", ""), "sha256": digest(data)})
        return target

    @staticmethod
    def relative(target, page):
        return quote(os.path.relpath(target, str(PurePosixPath(page).parent)), safe="/-._~")

    def resolve(self, ref, a, page, item=None):
        ref = ref.strip()
        if not ref or ref.startswith("#"):
            return ref
        target = None
        reason = "Target absent from exported course (missing, hidden, restricted, or unsupported)"
        if "@@PLUGINFILE@@" in ref:
            rest = unquote(ref.split("@@PLUGINFILE@@", 1)[1].split("?", 1)[0])
            candidates = [f for f in self.activity_files(a) if f["filepath"] + f["filename"] == rest or "/" + f["itemid"] + f["filepath"] + f["filename"] == rest]
            if item is not None:
                candidates = [f for f in candidates if f["itemid"] == str(item)]
            if len(candidates) == 1:
                target = self.asset(candidates[0])
            reason = "PLUGINFILE metadata match missing or ambiguous" if not candidates else reason
        elif ref.startswith("$@"):
            match = re.fullmatch(r"\$@(\w+)VIEWBYID\*(\d+)@\$(?:#(.*))?", ref)
            if match:
                kind, mid, fragment = match.groups()
                target = self.targets.get(mid)
                if target and fragment:
                    return self.relative(target, page) + "#" + fragment
        else:
            u = urlsplit(ref)
            local = not u.netloc or u.netloc == urlsplit(self.origin).netloc
            q = parse_qs(u.query)
            if local and u.path.endswith("/view.php") and "/mod/" in u.path:
                mid = q.get("id", [None])[0]
                target = self.chapters.get(q.get("chapterid", [None])[0]) or self.targets.get(mid)
            elif local and u.path.endswith("/course/view.php"):
                if q.get("id", [None])[0] == self.course.attrib["id"]:
                    target = "index.md"
            elif local and "pluginfile.php/" in u.path:
                parts = unquote(u.path.split("pluginfile.php/", 1)[1]).split("/")
                if len(parts) >= 4:
                    ctx, comp, area, *tail = parts
                    candidates = [f for f in self.files if f["contextid"] == ctx and f["component"] == comp and f["filearea"] == area and (f["filepath"] + f["filename"]).lstrip("/") in ("/".join(tail), "/".join(tail[1:])) and f["id"] in self.allowed_files]
                    if len(candidates) == 1:
                        target = self.asset(candidates[0])
            elif u.scheme in ("http", "https", "mailto") and not local:
                return ref
            elif u.scheme == "data":
                reason = "Inline data URL requires manual review"
            elif u.scheme:
                reason = "Unsupported URL scheme"
        if target:
            frag = urlsplit(ref).fragment if not ref.startswith("$@") else ""
            return self.relative(target, page) + ("#" + frag if frag else "")
        self.unresolved.append({"page": page, "reference": ref, "reason": reason})
        return None

    def html(self, source, a, page, item=None):
        soup = BeautifulSoup(source or "", "html.parser")
        for node in soup.select("script, style, iframe, form, input"):
            self.unresolved.append({"page": page, "reference": node.name, "reason": "Active HTML omitted; manual review required"})
            node.decompose()
        for node in soup.find_all(True):
            for k in list(node.attrs):
                if k.lower().startswith("on"):
                    del node[k]
        for node in soup.find_all(True):
            for attr in ("href", "src", "data", "poster"):
                if not node.has_attr(attr):
                    continue
                original = node[attr]
                resolved = self.resolve(original, a, page, item)
                if resolved is None:
                    if node.name == "img":
                        node.replace_with(soup.new_string("[Brak obrazu w kopii kursu" + (": " + node.get("alt", "") if node.get("alt") else "") + "]"))
                    elif node.name == "a":
                        node.append(soup.new_string(" (odnośnik niedostępny w kopii kursu)"))
                        node.unwrap()
                    else:
                        del node[attr]
                    break
                node[attr] = resolved
                if node.name == "img" and urlsplit(resolved).netloc:
                    self.external_images.append({"page": page, "url": resolved})
        # Preserve explicit anchor targets through conversion.
        for node in list(soup.find_all(True)):
            anchor = node.get("id") or (node.get("name") if node.name == "a" else None)
            if anchor:
                mark = soup.new_tag("a", id=anchor)
                node.insert_before(mark)
                node.attrs.pop("id", None)
                node.attrs.pop("name", None)
        # Moodle's editor encodes most C++ samples as Courier spans and <br>.
        def mono(node):
            return isinstance(node, Tag) and any(x in node.get("style", "").lower() for x in ("monospace", "courier"))

        def code_text(node):
            clone = BeautifulSoup(str(node), "html.parser")
            for br in clone.find_all("br"):
                br.replace_with("\n")
            return clone.get_text().replace("\xa0", " ")

        for p in list(soup.find_all("p")):
            texts = [s for s in p.find_all(string=True) if s.strip()]
            if texts and all(any(mono(parent) for parent in s.parents if parent is not p) for s in texts) and not p.find(["img", "a", "table"]):
                pre = soup.new_tag("pre")
                code = soup.new_tag("code", attrs={"class": "language-cpp"})
                code.string = code_text(p)
                pre.append(code)
                p.replace_with(pre)
        for node in list(soup.find_all(["span", "font"])):
            if node.parent is None or node.find_parent(["pre", "code"]):
                continue
            style = node.get("style", "").lower()
            if mono(node) and not node.find(["p", "div", "ul", "ol"]):
                text = code_text(node)
                if "\n" not in text:
                    code = soup.new_tag("code")
                    code.string = text
                    node.replace_with(code)
            elif "underline" in style:
                node.name = "u"
                node.attrs = {}
        # Join adjacent code paragraphs without losing their line boundaries.
        for pre in list(soup.find_all("pre")):
            if pre.parent is None:
                continue
            while True:
                nxt = pre.next_sibling
                while isinstance(nxt, NavigableString) and not nxt.strip():
                    nxt = nxt.next_sibling
                if not isinstance(nxt, Tag) or nxt.name != "pre":
                    break
                if pre.code and nxt.code and pre.code.get("class") == nxt.code.get("class"):
                    pre.code.append("\n" + nxt.code.get_text())
                    nxt.decompose()
                else:
                    break
        # Normalize editor wrappers before Markdown emphasis delimiters are emitted.
        # Adjacent emphasis/code tags otherwise produce ambiguous **** or `` runs.
        for node in list(soup.find_all(["span", "font"])):
            if node.parent is not None and not node.find_parent(["pre", "code"]):
                node.unwrap()
        for node in soup.find_all(["b", "i"]):
            node.name = {"b": "strong", "i": "em"}[node.name]
        for node in list(soup.find_all(["em", "strong"])):
            if not node.get_text().strip():
                node.unwrap()
                continue
            while node.contents and isinstance(node.contents[-1], Tag) and node.contents[-1].name == "br":
                node.insert_after(node.contents[-1].extract())
        for node in list(soup.find_all(["em", "strong", "code"])):
            if node.parent is None or node.find_parent("pre"):
                continue
            while isinstance(node.next_sibling, Tag) and node.next_sibling.name == node.name:
                nxt = node.next_sibling
                for child in list(nxt.contents):
                    node.append(child.extract())
                nxt.decompose()
        for pre in soup.find_all("pre"):
            if pre.code:
                classes = pre.code.get("class", []) + pre.get("class", [])
                lang = next((c.removeprefix("language-") for c in classes if c.startswith("language-")), "text")
                pre["data-language"] = lang
        converter = Converter(heading_style="ATX", bullets="-", escape_underscores=True, code_language_callback=lambda el: el.get("data-language", "text"), keep_inline_images_in=["td", "th", "a"], table_infer_header=True)
        result = converter.convert_soup(soup).strip()
        # Remove editor-only empty paragraphs outside code, preserving code whitespace.
        lines, fenced, blank = [], False, False
        for line in result.splitlines():
            if line.lstrip().startswith("```"):
                fenced = not fenced
            if not fenced and not line.strip():
                if blank:
                    continue
                blank = True
            else:
                blank = False
            lines.append(line)
        result = "\n".join(lines).strip()
        return result + "\n" if result else ""

    def generate(self):
        self.allowed_files = set()
        active_sections = []
        for s in self.sections:
            sid = s.attrib["id"]
            folder = f"{int(value(s, 'number')):02d}-{slug(value(s, 'name') or 'Sekcja')}-s{sid}"
            section_title = value(s, "name") or f"Sekcja {value(s, 'number')}"
            section_path = folder + "/index.md"
            entries = []
            sr = restricted(self.course) + restricted(s)
            self.inventory.append(f"### {value(s, 'number')}. {section_title} (section {sid})" + (" — skipped: " + ", ".join(sr) if sr else ""))
            if not sr:
                active_sections.append((s, folder, section_title, entries))
            for mid in filter(None, value(s, "sequence").split(",")):
                if mid not in self.activities:
                    self.unresolved.append({"page": section_path, "reference": mid, "reason": "Activity in section sequence missing"})
                    continue
                a = self.activities[mid]
                reasons = list(dict.fromkeys(sr + restricted(a["module"])))
                af = self.activity_files(a)
                if any(f["id"] in self.excluded for f in af):
                    reasons.append("publication review: attachment withheld by import policy")
                status = "converted"
                if reasons:
                    status = "skipped: " + ", ".join(reasons)
                    self.skipped.append({"id": mid, "type": a["kind"], "title": a["title"], "reason": ", ".join(reasons)})
                elif a["kind"] not in self.supported:
                    status = "unsupported: interactive activity; no placeholder exported"
                    self.skipped.append({"id": mid, "type": a["kind"], "title": a["title"], "reason": status})
                self.inventory.append(f"- `{mid}` {a['kind']}: {a['title'].strip()} — {status}")
                if status != "converted":
                    continue
                a["path"] = folder + "/" + slug(a["title"]) + "-m" + mid + ".md"
                if a["kind"] == "label":
                    a["path"] = section_path
                self.targets[mid] = a["path"]
                if a["kind"] == "book":
                    chapters = sorted(a["data"].findall("chapters/chapter"), key=lambda c: int(value(c, "pagenum")))
                    a["chapters"] = chapters
                    a["visible_chapter_ids"] = {c.attrib["id"] for c in chapters if not restricted(c) and value(c, "hidden", "0") == "0"}
                    for c in chapters:
                        if not restricted(c) and value(c, "hidden", "0") == "0":
                            self.chapters[c.attrib["id"]] = folder + "/" + slug(a["title"]) + "-m" + mid + "/" + slug(value(c, "title")) + "-c" + c.attrib["id"] + ".md"
                        else:
                            self.skipped.append({"id": c.attrib["id"], "type": "book chapter", "title": value(c, "title"), "reason": "hidden or restricted"})
                self.allowed_files.update(f["id"] for f in self.activity_files(a))
                entries.append(a)
            self.inventory.append("")
        nav = [{"Początek": "index.md"}]
        home = "# " + self.title + "\n\n"
        course_context = {"kind": "course", "context": self.course.attrib.get("contextid", "")}
        home += self.html(value(self.course, "summary"), course_context, "index.md") + "\n"
        for s, folder, title, entries in active_sections:
            path = folder + "/index.md"
            section_a = {"kind": "course", "context": self.course.attrib.get("contextid", "")}
            self.targets["section-" + s.attrib["id"]] = path
            text = f"# {title}\n\n" + self.html(value(s, "summary"), section_a, path)
            section_nav = [{"Przegląd": path}]
            for a in entries:
                kind, page = a["kind"], a["path"]
                if kind == "label":
                    text += "\n" + self.html(value(a["data"], "intro"), a, path) + "\n"
                    self.stats["labels"] += 1
                    continue
                text += f"\n- [{a['title'].strip()}]({self.relative(page, path)})\n"
                body = f"# {a['title'].strip()}\n\n"
                if kind == "page":
                    body += self.html(value(a["data"], "content"), a, page)
                    self.stats["pages"] += 1
                else:
                    body += self.html(value(a["data"], "intro"), a, page)
                if kind in ("resource", "folder"):
                    downloads = sorted((f for f in self.activity_files(a) if f["filearea"] == "content"), key=lambda f: (int(f.get("sortorder", "0")), f["filepath"], f["filename"], int(f["id"])))
                    for f in downloads:
                        asset = self.asset(f)
                        if asset:
                            body += f"\n- [{f['filepath'].lstrip('/')}{f['filename']}]({self.relative(asset, page)})\n"
                    self.stats[kind + "s"] += 1
                if kind == "url":
                    url = self.resolve(value(a["data"], "externalurl"), a, page)
                    if url:
                        body += f"\n[{a['title']}]({url})\n"
                if kind == "book":
                    book_nav = [{"Wprowadzenie": page}]
                    parent_children = None
                    for c in a["chapters"]:
                        cp = self.chapters.get(c.attrib["id"])
                        if not cp:
                            continue
                        ct = value(c, "title")
                        self.put("docs/" + cp, f"# {ct}\n\n" + self.html(value(c, "content"), a, cp, c.attrib["id"]))
                        self.stats["book_chapters"] += 1
                        body += f"\n- [{ct}]({self.relative(cp, page)})\n"
                        if value(c, "subchapter") == "1" and parent_children is not None:
                            parent_children.append({ct: cp})
                        else:
                            parent_children = [{ct: cp}]
                            book_nav.append({ct: parent_children})
                    section_nav.append({a["title"].strip(): book_nav})
                else:
                    section_nav.append({a["title"].strip(): page})
                self.put("docs/" + page, body)
            self.put("docs/" + path, text)
            self.stats["exported_sections"] += 1
            nav.append({title: section_nav})
            home += f"- [{title}]({folder}/index.md)\n"
        self.put("docs/index.md", home)
        def toml(v):
            if isinstance(v, str):
                return json.dumps(v, ensure_ascii=False)
            if isinstance(v, list):
                return "[\n" + ",\n".join(toml(i) for i in v) + "\n]"
            return "{ " + ", ".join(toml(k) + " = " + toml(val) for k, val in v.items()) + " }"
        config = f'''# Explicit navigation follows Moodle section numbers and activity sequence.
[project]
site_name = {toml(self.title)}
site_url = {toml(self.site_url)}
docs_dir = "docs"
site_dir = "site"
nav = {toml(nav)}

[project.theme]
language = "pl"
font = false
features = ["navigation.path", "navigation.indexes", "navigation.footer", "navigation.top", "toc.follow", "content.code.copy"]

[project.markdown_extensions]
"tables" = {{}}
"sane_lists" = {{}}
"attr_list" = {{}}
"md_in_html" = {{}}
"pymdownx.superfences" = {{}}
"pymdownx.highlight" = {{}}
'''
        self.put("zensical.toml", config)
        self.stats["markdown_files"] = sum(p.endswith(".md") for p in self.output)
        self.stats["book_chapters"] += 0
        self.stats["attachments"] = len(self.exported_files)
        self.stats["hidden_activities"] = sum("hidden" in x["reason"] for x in self.skipped)
        self.stats["unsupported_visible_activities"] = sum(x["reason"].startswith("unsupported") for x in self.skipped)
        self.stats["withheld_for_review"] = sum("publication review" in x["reason"] for x in self.skipped)
        self.stats["source_sections"] = len(self.sections)
        self.stats["source_activities"] = len(self.activities)
        self.stats["unresolved_references"] = len(self.unresolved)
        self.put("migration-report.md", self.report())
        self.put("migration.json", json.dumps({"course": self.title, "stats": dict(self.stats), "targets": self.targets, "attachments": self.exported_files, "skipped": self.skipped, "unresolved": self.unresolved, "external_images": self.external_images}, ensure_ascii=False, indent=2) + "\n")
        return self.output

    def report(self):
        types = Counter(a["kind"] for a in self.activities.values())
        filetypes = Counter(f["mimetype"] for f in self.exported_files)
        lines = ["# Moodle migration report", "", f"Original course: **{self.title}** (ID {self.course.attrib['id']}).", "", f"Archive: {'ZIP' if self.a.zip else 'tar'}, Moodle {value(self.meta, 'information/moodle_release')}, backup {value(self.meta, 'information/backup_release')}.", "", "## Statistics", "", "| Metric | Count |", "| --- | ---: |"]
        lines += [f"| {k} | {v} |" for k, v in self.stats.items()]
        lines += ["", "Source activity types: " + ", ".join(f"{k}: {v}" for k, v in sorted(types.items())) + ". No Books or Folders occur in this backup." if not types.get("book") and not types.get("folder") else "", "", "Extracted file types:", ""]
        lines += [f"- {k}: {v}" for k, v in sorted(filetypes.items())]
        lines += ["", "## Publication and privacy", "", "The backup contains private user records and submission data. Only teaching fields from course/section metadata and allowlisted Page, Book, Label, Resource, Folder and URL modules are read for export. User profiles, enrolments, grades, quiz attempts/questions, forum discussions, submissions, completion data and logs are never copied. File components are allowlisted by exported activity context and content area; submission and question files are excluded. File metadata such as uploader IDs and author names is not exported.", "", "Hidden sections/modules and any non-empty availability/group restriction are excluded conservatively, including past date windows. No hidden material appears in docs or search. Report inventory lists titles and IDs only.", "", "Policy exclusions (file ID and review reason only; no original filename or content): " + ("; ".join(f"{fid}: {reason}" for fid, reason in self.excluded.items()) or "none") + ". Policies are course-specific and must not be reused blindly for another course.", "", "Several original attachments carry `allrightsreserved` metadata. Existing teacher attribution in lesson text is preserved. Confirm redistribution rights for teaching documents, examination extracts and third-party images before public distribution. Downloadable originals retain their internal document metadata; this is not a forensic guarantee that all embedded personal data has been removed. Review originals before broad public distribution.", "", "## Conversion details and limitations", "", "Section number and sequence fields control ordering. Duplicate titles use Moodle IDs in filenames. Labels remain inline in ordered section overviews (all Labels in this backup are separators). Page body content is preserved; Moodle's separate Page intro is a course-list description and is not prepended as duplicated lesson text. Resource intros and downloads are retained. Source code is never corrected. Courier paragraphs become fenced C++ blocks; mixed inline code is preserved as inline code. Superscript, subscript, underline, complex tables and lists with nonstandard marker rules retain useful HTML. Empty table headers may be inferred for Markdown tables. Books (when present) use pagenum/subchapter and chapter visibility. Unsupported interactive modules have no placeholder pages.", "", "Broken Moodle references are replaced by visible missing-reference notes, not invented targets. Exact originals are listed below. External URLs are preserved; they can change independently. Remote images remain external and are listed separately. No external assets are downloaded during import.", "", "## Skipped and unsupported activities", "", "| Moodle ID | Type | Title | Reason |", "| --- | --- | --- | --- |"]
        lines += [f"| {x['id']} | {x['type']} | {x['title'].strip().replace('|', '&#124;')} | {x['reason']} |" for x in self.skipped]
        lines += ["", "## Unresolved references", ""]
        lines += [f"- `{x['page']}`: `{x['reference']}` — {x['reason']}" for x in self.unresolved] or ["None."]
        lines += ["", "## External images", ""]
        lines += [f"- `{x['page']}`: {x['url']}" for x in self.external_images] or ["None."]
        lines += ["", "## Full ordered course inventory", ""] + self.inventory
        return "\n".join(lines) + "\n"


def write_output(output, files, overwrite=False):
    """Preflight ALL changes. Preserve unrelated files and protect edited Markdown."""
    output = output.resolve()
    manifest = output / ".moodle-import.json"
    old = json.loads(manifest.read_text()) if manifest.exists() else {}
    paths = set(old) | set(files)
    for rel in paths:
        p = output / rel
        if not p.resolve().is_relative_to(output) or p.is_symlink():
            raise ValueError(f"Unsafe output path: {rel}")
        if not p.exists():
            continue
        data = p.read_bytes()
        if rel in files and data == files[rel]:
            continue
        if rel not in old or (digest(data) != old[rel] and not overwrite):
            raise ValueError(f"Refusing to overwrite/delete edited or unrelated file: {p}. Import to a new directory and compare, or use --overwrite-generated for previously generated files.")
    output.mkdir(parents=True, exist_ok=True)
    for rel in sorted(set(old) - set(files)):
        (output / rel).unlink(missing_ok=True)
    for rel, data in sorted(files.items()):
        p = output / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
    manifest.write_text(json.dumps({k: digest(v) for k, v in sorted(files.items())}, indent=2) + "\n")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("archive", type=Path)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--site-url", required=True, help="Full Pages URL including repository and course subpaths")
    p.add_argument("--policy", type=Path, help="Course-specific reviewed exclusions JSON")
    p.add_argument("--overwrite-generated", action="store_true", help="Replace edited files from previous import manifest only")
    args = p.parse_args()
    importer = Importer(args.archive, args.site_url, json.loads(args.policy.read_text()) if args.policy else None)
    files = importer.generate()
    write_output(args.output, files, args.overwrite_generated)
    print(json.dumps(dict(importer.stats), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
