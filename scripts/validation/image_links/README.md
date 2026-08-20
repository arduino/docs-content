# Image Links Validation Script

This utility script manages and validates image links in Markdown files. It ensures that all referenced local images exist and helps keep the repository clean by identifying or removing orphaned files from `assets` directories.

## Features

- **Broken Image Link Detection:** Identifies referenced images in Markdown (`![alt](link)`) and HTML (`<img src="...">`) tags that do not exist on disk.
- **Orphaned Asset Detection:** Scans `assets/` folders to find images that are not referenced in any Markdown file.
- **Hierarchical Ignore Support:** Automatically honors `.lintignore`, `.imagelintignore`, and legacy `.linterignore` files placed at any directory depth.
- **Surgical Cleanup:** Provides a safe command to delete orphaned files automatically.

## Requirements

- Python 3

## Usage

Run the script from the repository root:

### Validate All

Run both missing image and unlinked asset checks:

```bash
python3 scripts/validation/image_links/image_links.py validate content
```

### Validate Missing Images Only

Check only for broken image references:

```bash
python3 scripts/validation/image_links/image_links.py validate-missing content
```

### Validate Unlinked Assets Only

Check only for unlinked images in `assets` folders:

```bash
python3 scripts/validation/image_links/image_links.py validate-unlinked content
```

### Remove Unlinked Assets

Delete orphaned images from `assets` folders:

```bash
python3 scripts/validation/image_links/image_links.py remove-unlinked content
```

## Ignore Configuration

The script automatically discovers ignore patterns by traversing from the target directory up to the repository root:

- `.lintignore` (universal ignore across all validation tools)
- `.imagelintignore` (tool-specific ignore for image validation)
- `.linterignore` (legacy compatibility)

Patterns follow standard `.gitignore` glob syntax relative to the location of the ignore file.
