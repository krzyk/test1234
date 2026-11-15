# Kursy — materiały dydaktyczne

This repository contains the actual **algorytm i techniki programowania** course imported from Moodle 2.6.5 into [Zensical](https://zensical.org/docs/). The maintained sources are Polish Markdown, with the original teaching text, examples, ordering and downloadable files. No Moodle installation is needed to read or build them.

Published course URL after deployment:
**https://krzyk.github.io/test1234/algorytmy-i-techniki-programowania/**

```text
courses/
  algorytmy-i-techniki-programowania/
    zensical.toml              # Explicit Polish navigation and Pages URL
    docs/
      index.md                # Course home
      00-...-s661/index.md     # Ordered section overview
      01-...-s662/*.md         # Lessons; Moodle IDs prevent name collisions
      ...
      assets/                 # Images and original downloads
    migration-report.md       # Complete ordered inventory and exclusions
    migration.json            # Provenance, attachment hashes, unresolved links
    .moodle-import.json       # Generated-file hashes protect subsequent edits
scripts/
  import_moodle.py            # Offline, reusable importer
  import-policy.json         # Reviewed exclusions for course 37 only
  build_sites.py             # Build all courses; assemble clean _site/
  validate_site.py            # Check links, navigation, assets and publication paths
  test_import_moodle.py       # Import regression tests
  requirements.txt           # Import-only dependencies
.github/workflows/deploy.yml
Dockerfile
requirements.txt             # Pinned Zensical release
MIGRATION_REPORT.md
```

The original `.mbz`, local environments, caches, and generated HTML are ignored by Git. Keep the backup outside public Git history: it contains user profiles, submissions and other private records. See [MIGRATION_REPORT.md](MIGRATION_REPORT.md) for publication concerns and exact limitations.

## Preview with Docker (no Python libraries installed on your system)

Install Docker Engine on Linux using your distribution's packages or [Docker's installation instructions](https://docs.docker.com/engine/install/). Run these commands from this checkout:

```sh
docker build -t moodle-zensical .
docker run --rm -it \
  --user "$(id -u):$(id -g)" -e HOME=/tmp \
  -p 127.0.0.1:8000:8000 \
  -v "$PWD:/workspace" -w /workspace \
  moodle-zensical \
  zensical serve -a 0.0.0.0:8000 \
  -f courses/algorytmy-i-techniki-programowania/zensical.toml
```

Open **http://localhost:8000/**. Stop with Ctrl+C. The image installs both Zensical and all migration dependencies. It excludes the backup and course files from its build context; those are available only through the explicit workspace mount. The UID/GID options keep generated files owned by you.

Build all courses and validate the deployment artifact:

```sh
docker run --rm --user "$(id -u):$(id -g)" -e HOME=/tmp \
  -v "$PWD:/workspace" -w /workspace moodle-zensical
```

The generated site is in `_site/`, with each course under its own directory and a course list at the root. Docker is optional for website editing/builds and provided specifically to isolate the Python migration tooling.

## Linux virtual environment alternative

Use Python 3.11 or newer (GitHub Actions and Docker use 3.13). On Debian/Ubuntu, install `python3`, `python3-venv` and `python3-pip` through apt if absent. Install packages only into the virtual environment:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
zensical serve -f courses/algorytmy-i-techniki-programowania/zensical.toml
```

Open http://localhost:8000/. For a single strict course build or a complete Pages build:

```sh
zensical build --clean --strict -f courses/algorytmy-i-techniki-programowania/zensical.toml
python scripts/build_sites.py
```

The latter command finds every `courses/*/zensical.toml`, builds it with Zensical, checks its generated HTML and assembles `_site/`. It clears generated `site/` and `_site/` directories to prevent stale content from being published. Never store source files there. It does **not** import Moodle or overwrite maintained Markdown.

## Import the original backup again

The initial import has already been performed. Normal editing does not require the backup or importer. To reproduce it in an independent directory for comparison:

```sh
docker run --rm --user "$(id -u):$(id -g)" -e HOME=/tmp \
  -v "$PWD:/workspace" -w /workspace moodle-zensical \
  python scripts/import_moodle.py \
  kopia_zapasowa-moodle2-course-37-alg-20261114-2248.mbz \
  --output .migration/reimport \
  --site-url https://krzyk.github.io/test1234/algorytmy-i-techniki-programowania/ \
  --policy scripts/import-policy.json
```

To update the original imported course, change `--output` to `courses/algorytmy-i-techniki-programowania`. An identical repeat is deterministic. The importer checks its manifest before writing anything and refuses to replace edited Markdown or unrelated files. Prefer importing into `.migration/reimport` and selectively merging updates after Markdown editing begins. `--overwrite-generated` deliberately replaces edited files previously owned by the importer; it still cannot overwrite unrelated files. Back up your edits first. `migration-report.md` and `migration.json` describe the latest import, not subsequent manual edits.

The equivalent Python command works inside the virtual environment after:

```sh
python -m pip install -r scripts/requirements.txt
```

The importer reads ZIP or tar backups directly, uses XML and HTML parsers, resolves file hashes and Moodle references, and exports only visible, unrestricted teaching content. It has support for Pages, Books with chapters/subchapters, Labels, Resources, Folders and URL activities. This actual course contains no Books or Folders; those paths have synthetic regression coverage. Interactive quizzes, assignments and forums are recorded in the report without placeholder lessons. The converter targets the inspected Moodle 2 layout; inspect other backup versions and the new report before accepting their output.

Run regression tests (Docker has all dependencies):

```sh
docker run --rm --user "$(id -u):$(id -g)" -e HOME=/tmp \
  -v "$PWD:/workspace" -w /workspace moodle-zensical \
  python -m unittest discover -s scripts -p 'test_*.py' -v
```

## Edit lessons and navigation in GitHub

Edit files under `courses/algorytmy-i-techniki-programowania/docs/` using GitHub's pencil button. Preserve the original text unless making an intentional editorial change. Use one `#` heading for the lesson title, `##` for subsections, fenced blocks such as ` ```cpp ` for programming examples, and normal Markdown tables. Code examples from Moodle may contain mistakes; the import intentionally retains them.

To add a lesson:

1. Add a UTF-8 file such as `06-tablice-statyczne-s667/nowa-lekcja.md`, starting with its Polish `#` title.
2. Add `{ "Nowa lekcja" = "06-tablice-statyczne-s667/nowa-lekcja.md" }` in the appropriate position of `nav` in `zensical.toml`.
3. Add a link to it in that section's `index.md` so the overview stays useful.
4. Upload images or downloads into `docs/assets/` and link relatively, e.g. `![Schemat](../assets/schemat.png)` or `[Pobierz](../assets/zadania.pdf)`.
5. Preview/build, then commit. Every Markdown page must appear exactly once in navigation; the validator enforces this.

For a new chapter, create a directory with an `index.md`, add its lessons, link it from the course home, and insert a navigation group in the intended position:

```toml
{ "Nowy rozdział" = [
  { "Przegląd" = "nowy-rozdzial/index.md" },
  { "Pierwsza lekcja" = "nowy-rozdzial/pierwsza-lekcja.md" },
] },
```

Use simple ASCII filenames and Polish display titles. Existing source IDs in names keep URLs stable and distinguish repeated titles. Rename only deliberately, updating navigation and incoming links together. Zensical supplies Polish search, per-page contents, breadcrumbs, previous/next lesson navigation, responsive layout and syntax highlighting using its default theme. System fonts avoid fetching Google Fonts.

## Add another independent course

Place its backup locally, inspect its privacy and visibility settings, and import to a new directory:

```sh
docker run --rm --user "$(id -u):$(id -g)" -e HOME=/tmp \
  -v "$PWD:/workspace" -w /workspace moodle-zensical \
  python scripts/import_moodle.py another-course.mbz \
  --output courses/another-course \
  --site-url https://krzyk.github.io/test1234/another-course/
```

Use a separate `--policy` JSON if that course needs reviewed file exclusions; the existing policy is bound to Moodle course 37. Review the new course's report, Markdown and attachments before committing. A folder's name must match its final URL segment. Keep `docs_dir = "docs"` and `site_dir = "site"`. The build automatically includes the additional course and updates the root course list. No workflow change is needed. Each course has its own navigation and search index.

## Enable GitHub Pages

In **krzyk/test1234 → Settings → Pages → Build and deployment → Source**, select **GitHub Actions**. Ensure Actions is enabled for the repository and that the `github-pages` environment permits deployment from `main`. No personal access token or additional hosting account is required.

Commit and push the reviewed files yourself. The workflow runs on pushes to the repository's verified default branch, `main`, or through **Actions → Publish courses to GitHub Pages → Run workflow**. The build job installs the pinned Zensical package, performs strict builds and local-link validation, then uploads only `_site/` with the official Pages artifact action. The deploy job uses the official Pages deployment action with `pages: write` and `id-token: write`. The build job has only repository and Pages read permissions.

The repository subpath is configured explicitly in each `site_url`; generated lesson, asset and search paths are relative. `_site/.nojekyll` is generated. Backup files, reports, importer scripts and temporary files are outside the uploaded artifact. If moving/forking the repository, update every `site_url` to the new owner/repository path. If changing the default branch, update `deploy.yml` and the Pages environment rule.

The migration does not rerun in CI: Markdown becomes the maintained source of truth. Local validations and import limitations are documented in [MIGRATION_REPORT.md](MIGRATION_REPORT.md). Official configuration references: [Zensical navigation](https://zensical.org/docs/setup/navigation/), [language](https://zensical.org/docs/setup/language/), [publishing](https://zensical.org/docs/publish-your-site/), and [GitHub Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).



## Troubleshoot GitHub Pages builds

If the log says `GitHub Pages: jekyll` or `Theme: jekyll-theme-primer` and renders files under `courses/.../docs/`, Pages is still using its legacy branch build. Open **Settings → Pages → Build and deployment → Source** and select **GitHub Actions**. Keep the existing `deploy.yml`; no Jekyll workflow template is needed. Then run **Actions → Publish courses to GitHub Pages → Run workflow** on `main` after committing and pushing your fixes. Re-running the old “pages build and deployment” job will repeat the legacy build.

If our workflow reports `Missing/changed attachment`, compare the source download with its hash in `migration.json`. Imported attachments retain the original bytes, including Windows CRLF line endings in some `.txt`/`.cpp` files. `.gitattributes` disables Git text normalization under every course's `docs/assets/` directory. Commit that file together with the affected original attachments; changing attributes alone does not restore bytes already normalized in a prior commit. The original bytes are still present in this working checkout. If working from a fresh checkout of the affected commit, recover those downloads from the original backup through an import to `.migration/reimport` and copy only the affected downloads back. Keep checksum validation enabled.
