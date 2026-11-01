# Relative Links Validator

This script validates relative internal Markdown links and heading anchors across the documentation.

## Features

- **Link Validation:** Ensures relative links resolve to a valid published route corresponding to an existing Markdown file.
- **Anchor Validation:** Extracts heading slugs and explicit HTML IDs from target files on-demand to ensure anchor links (e.g., `#my-heading`) are not broken.
- **Leniency:** Gracefully handles trailing slashes, index files, and relative navigation.
- **Auto-Fixing:** Automatically cleans up deprecated `.md` extensions and numeric ordering prefixes in links via the `fix` command.
- **Hierarchical Ignore Support:** Automatically honors `.lintignore`, `.linklintignore`, and legacy `.linterignore` files placed at any directory depth. External links (`http://`, `https://`, `mailto:`, etc.) and asset extensions (`.png`, `.pdf`, etc.) are skipped automatically.

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

Every run ends with a `Scope:` line that counts each link by what was done with it: relative and absolute docs links checked, absolute docs links not checked (no `--absolute`), links to other hosts (never fetched), links into sections other systems serve, and assets.

### Auto-Fix Improper Links

Autocorrect improperly formatted links (such as removing trailing `.md` extensions or fixing path formats):

```bash
python3 scripts/validation/relative_links/relative_links.py fix content/software/app-lab
```

## How It Works

1. The script crawls the `content` directory to build a route map of valid production URLs to their respective source file paths (including unmigrated or ignored folders).
2. It resolves any relative link inside a Markdown file against that file's mapped production URL.
3. It verifies that the resolved target URL exists in the global route map.
   Symlinked folders are followed: a tutorial shared between products (for example `hardware/.../nano-33-ble/tutorials/getting-started-omv`, a symlink to the generic Nano one) is published under each product's URL, so each of those URLs is a valid route.
4. Links into sections other systems serve (listed in `external-sections.txt`: the library and language references, `/resources`, `/certifications`) aren't checked; they're counted in the scope line.
5. Links are read as CommonMark reads them (https://spec.commonmark.org/0.31.2/#link-destination): spaces around the destination are ignored (`[text]( https://example.com )`), an angle-bracket destination is one link (`[text](<https://en.wikipedia.org/wiki/Servo_(radio_control)>)`), balanced parentheses belong to the path (`assets/wiring%20(1).jpg`), and there are no links in fenced code blocks or inline code. Something that looks like a link but isn't one (`[text]((https://...)`) is reported as an improper format: readers see it as plain text.
6. If an anchor (`#heading-slug`) is present, it parses the target file for Markdown headings and HTML ID tags, caches them, and verifies that the anchor slug exists.

## Ignore Configuration

The script automatically discovers ignore patterns by traversing from the target directory up to the repository root:

- `.lintignore` (universal ignore across all validation tools)
- `.linklintignore` (tool-specific ignore for relative link validation)
- `.linterignore` (legacy compatibility)

Files matching ignore patterns are excluded from having their own outbound links inspected, but they remain indexed in the production route map so other non-ignored documents can safely link to them.
