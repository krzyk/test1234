#!/usr/bin/env python3
"""Build maintained Markdown only; assemble the Pages artifact, never import Moodle."""
import html
from pathlib import Path
import shutil
import subprocess
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]
# The container also exposes a copy in /opt; use the mounted checkout there.
if not (ROOT / "courses").exists():
    ROOT = Path.cwd()


def main():
    destination = ROOT / "_site"
    configs = sorted((ROOT / "courses").glob("*/zensical.toml"))
    if not configs:
        raise SystemExit("No course configurations found")
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir()
    links = []
    for config in configs:
        course = config.parent
        settings = tomllib.loads(config.read_text())["project"]
        # Enforce the known generated directory before removing it.
        if settings.get("site_dir", "site") != "site":
            raise SystemExit(f"{config}: site_dir must be 'site'")
        generated = course / "site"
        if generated.is_symlink():
            raise SystemExit(f"Refusing linked site directory: {generated}")
        if generated.exists():
            shutil.rmtree(generated)
        subprocess.run(["zensical", "build", "--clean", "--strict", "-f", str(config)], cwd=ROOT, check=True)
        subprocess.run([sys.executable, str(Path(__file__).with_name("validate_site.py")), str(course)], check=True)
        shutil.copytree(generated, destination / course.name)
        links.append(f'<li><a href="{html.escape(course.name)}/">{html.escape(settings["site_name"])}</a></li>')
    (destination / "index.html").write_text('<!doctype html>\n<html lang="pl"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Kursy</title><h1>Kursy</h1><ul>' + "".join(links) + '</ul></html>\n')
    (destination / ".nojekyll").touch()
    print(f"Pages artifact: {destination} ({len(configs)} courses)")


if __name__ == "__main__":
    main()
