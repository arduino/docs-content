# Relative Links Validator

This script validates relative internal Markdown links and heading anchors across the documentation.

## Features

- **Link Validation:** Ensures relative links resolve to a valid published route corresponding to an existing Markdown file.
- **Anchor Validation:** Extracts heading slugs and explicit HTML IDs from target files on-demand to ensure anchor links (e.g., `#my-heading`) are not broken.
- **Leniency:** Gracefully handles trailing slashes, index files, and relative navigation.
- **Auto-Fixing:** Automatically cleans up deprecated `.md` extensions and numeric ordering prefixes in links via the `fix` command.
- **Shared Pages:** A tutorial shared through a symlink is checked from every URL it's published at, and each problem is reported once, under the file to edit.
- **Hierarchical Ignore Support:** Automatically honors `.lintignore`, `.linklintignore`, and legacy `.linterignore` files placed at any directory depth. External links (`http://`, `https://`, `mailto:`, etc.) and asset extensions (`.png`, `.pdf`, etc.) are skipped automatically, except downloadable files under `/resources/` (see [How It Works](#how-it-works)).

## Usage

Run the script from the repository root:

### Validate All Content Links

Validate relative links across the entire `content` directory:

```bash
python3 scripts/validation/relative_links/relative_links.py validate content
```

Or validate a specific subdirectory or file:

```bash
python3 scripts/validation/relative_links/relative_links.py validate content/software/app-lab
```

### Also Check Absolute Links to the Docs

Absolute links to `https://docs.arduino.cc/...` are skipped by default. With `--absolute`, they're checked like root-relative links, against the same route map (offline: nothing is fetched):

```bash
python3 scripts/validation/relative_links/relative_links.py validate content --absolute
```

Every run prints a `Scope:` line that counts each link by what was done with it: relative and absolute docs links checked, absolute docs links not checked (no `--absolute`), links to other hosts (never fetched), mailto and data links, links into sections other systems serve, downloadable files checked or uploaded apart from this repo, and assets. A shared page's links are counted once; each further URL it's checked from counts as a copy of a shared page.

### Auto-Fix Improper Links

Autocorrect improperly formatted links (such as removing trailing `.md` extensions or fixing path formats):

```bash
python3 scripts/validation/relative_links/relative_links.py fix content/software/app-lab
```

`fix` doesn't follow symlinks: it only rewrites files kept under the path you give it.

## Reading the Output

Each file with problems is listed under its path, with one line per problem. A tutorial shared through a symlink is listed once, under the original file (the one to edit), and says how many URLs it's published at. A problem that's the same on every URL takes one line. A relative link that resolves differently on each URL lists each URL it's broken on, and the URLs where it works:

```text
content/software/plc-ide/tutorials/08.can-setup/content.md:
  Shared page, published at 2 URLs through symlinks: each link is checked from every one.
  - Broken link: '../../software/plc-ide' on all 2 URLs:
      /software/plc-ide/tutorials/can-setup/: resolves to '/software/plc-ide/software/plc-ide' which does not map to any markdown file.
      /tutorials/portenta-machine-control/can-setup/ (symlink content/hardware/pro-solutions/solutions-and-kits/portenta-machine-control/tutorials/can-setup): resolves to '/tutorials/software/plc-ide' which does not map to any markdown file.
```

Fix the link so it works from every URL listed: here, a root-relative link (`/software/plc-ide/`) works on both, while any `../` link would break on one of them.

The run ends with the number of link issues to fix and, when shared pages have problems, how many that is counting each URL they're published at.

## How It Works

1. The script crawls the `content` directory to build a route map of valid production URLs to their respective source file paths (including unmigrated or ignored folders).
2. It resolves any relative link inside a Markdown file against that file's mapped production URL.
3. It verifies that the resolved target URL exists in the global route map.
   Symlinked folders are followed: a tutorial shared between products (for example `hardware/.../nano-33-ble/tutorials/getting-started-omv`, a symlink to the generic Nano one) is published under each product's URL, so each of those URLs is a valid route. A relative link can work on one of those URLs and break on another, so the shared file's links are checked from each URL (see [Reading the Output](#reading-the-output)). A symlink back into a folder the crawl is already inside (a loop) isn't followed.
4. Links into sections and pages this repo's Markdown doesn't serve (listed in `external-sections.txt`: the library and language references, the Arduino CLI and Cloud API docs, and pages from the site's own code such as `/software/ide` and `/certifications`) aren't checked; they're counted in the scope line. An entry is a section prefix, or a single page with a trailing `$`.
   Downloadable files under `/resources/` follow the site's rules: a file in a product's `downloads/` folder is published as `/resources/pinouts/`, `/resources/schematics/` or `/resources/models/` plus its name (by its ending: `full-pinout.pdf`, `schematics.pdf`, `step.zip`), and datasheets as `/resources/datasheets/<identifier>[-<lang>]-datasheet.pdf` from their `[lang-]datasheet.md` pages. Links into those three folders are checked against the files here. Other files under `/resources/` (chip datasheets, CAD files, firmware) are uploaded to the site apart from this repo, so a link to one counts as fine when this repo publishes it and is otherwise not checked.
5. Links are read as CommonMark reads them (https://spec.commonmark.org/0.31.2/#link-destination): spaces around the destination are ignored (`[text]( https://example.com )`), an angle-bracket destination is one link (`[text](<https://en.wikipedia.org/wiki/Servo_(radio_control)>)`), balanced parentheses belong to the path (`assets/wiring%20(1).jpg`), and there are no links in fenced code blocks or inline code. Something that looks like a link but isn't one (`[text]((https://...)`) is reported as an improper format: readers see it as plain text.
6. If an anchor (`#heading-slug`) is present, it parses the target file for Markdown headings and HTML ID tags, caches them, and verifies that the anchor slug exists.

## Ignore Configuration

The script automatically discovers ignore patterns by traversing from the target directory up to the repository root:

- `.lintignore` (universal ignore across all validation tools)
- `.linklintignore` (tool-specific ignore for relative link validation)
- `.linterignore` (legacy compatibility)

Files matching ignore patterns are excluded from having their own outbound links inspected, but they remain indexed in the production route map so other non-ignored documents can safely link to them.

For a shared page, the path each URL is published from decides: a symlinked copy in an ignored folder isn't checked, and one outside ignored folders is checked even when the original is in an ignored folder. Problems are still reported under the original file. When you validate a single file or folder, the files in it are checked from every URL they're published at, including through symlinks elsewhere in `content`.
