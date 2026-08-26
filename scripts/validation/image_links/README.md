# Image Links Validation Script

This utility script manages and validates image links in Markdown files. It ensures that all referenced local images exist and helps keep your repository clean by identifying or removing orphaned files from your `assets` directories.

> [!WARNING]
> This script has currently only been officially validated for use within the `content/software/app-lab` folder structure. Exercise caution if running it against the entire `content` directory or other repositories.

## Assumptions & Limitations

*   **Asset Folders Only:** The script only searches for unlinked images inside directories specifically named `assets` (e.g., `some/path/assets/image.png`). It does not clean up images stored outside of an `assets` folder.
*   **Relative Paths:** The script assumes all local image links in your Markdown files are relative to the location of the `.md` file itself, *not* absolute to the project root. Absolute paths (starting with `/`) are currently interpreted as relative to the base directory provided in the command line argument.

## Requirements
*   Python 3

## Usage

Navigate to the root of the repository and run the script using Python.

### Validate All
Run both missing link and unlinked asset checks.

```bash
python3 scripts/validation/image_links/image_links.py validate content/software/app-lab
```

### Validate Missing
Check for broken image links referenced in Markdown files.

```bash
python3 scripts/validation/image_links/image_links.py validate-missing content/software/app-lab
```

### Validate Unlinked
Check for orphaned images in `assets` folders that are not referenced in any `.md` file.

```bash
python3 scripts/validation/image_links/image_links.py validate-unlinked content/software/app-lab
```

### Remove Unlinked
Surgically delete all orphaned images from `assets` folders.

```bash
python3 scripts/validation/image_links/image_links.py remove-unlinked content/software/app-lab
```
