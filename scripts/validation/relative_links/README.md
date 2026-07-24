# Relative Links Validator

This script validates relative internal Markdown links and anchors across the documentation.

<Alert type="info">**Note:** Currently, this script and its mapping logic are specifically validated for the **App Lab** documentation structure (`content/software/app-lab`). While it attempts to map the entire repository, edge cases in hardware or cloud tutorials may exist.</Alert>

## Features

- **Link Validation:** Ensures relative links resolve to an actual production URL.
- **Anchor Validation:** Extracts valid heading slugs and explicit HTML IDs from the target file on-demand to ensure anchor links (e.g., `#my-heading`) are not broken.
- **Leniency:** Ignores trailing slashes and handles `.md` conversion gracefully.
- **Ignoring files:** Supports `.linterignore` files. These files follow standard `.gitignore` behavior and can be placed at any directory depth. Note that we always exclude external links and asset extensions (like `.png`, `.pdf`, etc.) which should be checked by the `image_links` script.

## Usage

You can validate a specific file:

```bash
python3 relative_links.py validate ../../content/software/app-lab/3.getting-started/1.quickstart/quickstart.md
```

Or validate an entire directory:

```bash
python3 relative_links.py validate ../../content/software/app-lab
```

You can also use the `fix` command to autocorrect improperly formatted links (like removing trailing `.md` extensions or numeric prefixes):

```bash
python3 relative_links.py fix <path>
```

## How it Works

1. The script crawls the `content` directory to build a map of valid production URLs to their respective local file paths.
2. It resolves any relative link inside a markdown file against that file's own production URL.
3. It verifies that the resolved URL exists in the global map.
4. If an anchor is present, it parses the target file for all `## Headings` and `<div id="...">` elements, caches them, and verifies that the anchor slug exists.
