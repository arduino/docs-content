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

### Auto-Fix Improper Links

Autocorrect improperly formatted links (such as removing trailing `.md` extensions or fixing path formats):

```bash
python3 scripts/validation/relative_links/relative_links.py fix content/software/app-lab
```

## How It Works

1. The script crawls the `content` directory to build a route map of valid production URLs to their respective source file paths.
2. It resolves any relative link inside a Markdown file against that file's mapped production URL.
3. It verifies that the resolved target URL exists in the global route map.
4. If an anchor (`#heading-slug`) is present, it parses the target file for Markdown headings and HTML ID tags, caches them, and verifies that the anchor slug exists.

## Ignore Configuration

The script automatically discovers ignore patterns by traversing from the target directory up to the repository root:

- `.lintignore` (universal ignore across all validation tools)
- `.linklintignore` (tool-specific ignore for relative link validation)
- `.linterignore` (legacy compatibility)
