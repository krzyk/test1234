#!/usr/bin/env python3
"""Validate source/nav coverage and every built local HTML link and resource."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import tomllib
from urllib.parse import unquote, urljoin, urlsplit


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
        self.language = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.language = attrs.get("lang")
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        for key in ("href", "src", "poster", "data"):
            if key in attrs:
                self.links.append(attrs[key])


def nav_paths(nav):
    for entry in nav:
        if isinstance(entry, str):
            if entry.endswith(".md"):
                yield entry
        else:
            for value in entry.values():
                if isinstance(value, list):
                    yield from nav_paths(value)
                elif value.endswith(".md"):
                    yield value


def validate(course):
    config = tomllib.loads((course / "zensical.toml").read_text())["project"]
    docs = course / config.get("docs_dir", "docs")
    site = (course / config.get("site_dir", "site")).resolve()
    base = config["site_url"]
    origin = urlsplit(base)
    prefix = origin.path
    errors = []
    sources = {p.relative_to(docs).as_posix() for p in docs.rglob("*.md")}
    nav = list(nav_paths(config["nav"]))
    if set(nav) != sources or len(nav) != len(set(nav)):
        errors.append(f"Navigation mismatch: missing={sources - set(nav)}, nonexistent={set(nav) - sources}, duplicates={len(nav) - len(set(nav))}")
    for source in sources:
        path = Path(source)
        built = site / (path.parent / "index.html" if path.name == "index.md" else path.with_suffix("") / "index.html")
        if not built.is_file():
            errors.append(f"Markdown not built: {source}")
        text = (docs / source).read_text()
        if any(token in text for token in ("@@PLUGINFILE@@", "$@", "@@FILE@@")):
            errors.append(f"Moodle placeholder in {source}")
    documents = {}
    for p in site.rglob("*.html"):
        text = p.read_text()
        if "klzzwxh" in text or any(ord(c) < 32 and c not in "\t\n\r" for c in text):
            errors.append(f"Renderer placeholder/control character in {p.relative_to(site)}")
        documents[p.resolve()] = Document(text)
    checked = 0
    for path, doc in documents.items():
        if doc.language != "pl":
            errors.append(f"Non-Polish page: {path.relative_to(site)}")
        public = base + path.relative_to(site).as_posix()
        for ref in doc.links:
            u = urlsplit(urljoin(public, ref))
            if u.scheme not in ("http", "https") or u.netloc != origin.netloc:
                continue
            if not u.path.startswith(prefix):
                errors.append(f"Link escapes course subpath: {path.relative_to(site)} → {ref}")
                continue
            local = (site / unquote(u.path[len(prefix):])).resolve()
            if not local.is_relative_to(site):
                errors.append(f"Link escapes site: {ref}")
                continue
            if local.is_dir():
                local /= "index.html"
            if not local.is_file():
                errors.append(f"Missing local target: {path.relative_to(site)} → {ref}")
            elif u.fragment and local in documents and unquote(u.fragment) not in documents[local].ids:
                errors.append(f"Missing anchor: {path.relative_to(site)} → {ref}")
            checked += 1
    if not (site / "search.json").is_file():
        errors.append("Search index missing")
    for path in site.rglob("*"):
        if path.is_symlink() or path.suffix.lower() in {".mbz", ".py", ".toml"} or path.name in {"users.xml", "files.xml", "migration.json", "migration-report.md"}:
            errors.append(f"Unexpected published file: {path.relative_to(site)}")
    metadata_path = course / "migration.json"
    if metadata_path.exists():
        metadata = json.loads(metadata_path.read_text())
        for f in metadata["attachments"]:
            p = site / f["path"]
            if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != f["sha256"]:
                errors.append(f"Missing/changed attachment: {f['path']}")
        paths = set(metadata["targets"].values())
        for skipped in metadata["skipped"]:
            if skipped["type"] != "book chapter" and skipped["id"] in metadata["targets"]:
                errors.append(f"Skipped activity exported: {skipped['id']}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Validated {len(sources)} Markdown pages, {len(documents)} HTML documents and {checked} local links/resources; nav coverage, anchors, Polish language, search, attachment hashes and subpaths pass.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("course", type=Path)
    validate(parser.parse_args().course)
