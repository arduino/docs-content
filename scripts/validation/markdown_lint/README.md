# Markdown Lint Script

This script validates and formats Markdown files across the documentation using `markdownlint-cli` with automatic root configuration inheritance.

## Features

- **Markdown Standards Enforcement:** Enforces consistent Markdown formatting, heading conventions, list indentation, and code block styles.
- **Hierarchical Configuration Inheritance:** Baseline rules are defined in `content/.markdownlint.yaml`. Subdirectories can provide a local `.markdownlint.yaml` for domain-specific rule overrides while automatically inheriting all baseline rules.
- **Hierarchical Ignore Support:** Automatically honors `.lintignore`, `.markdownlintignore`, and legacy `.linterignore` files placed at any directory depth.
- **Auto-Fixing:** Automatically remediates fixable lint errors using the `--fix` flag.

## Requirements

- Python 3
- Node.js & `npx` (with `markdownlint-cli` installed in `scripts/validation/node_modules/` or executable via `npx`)

## Usage

Run the script from the repository root:

### Validate Markdown Files

Validate Markdown files across the entire `content` directory:

```bash
python3 scripts/validation/markdown_lint/markdown_lint.py content
```

Or validate a specific section:

```bash
python3 scripts/validation/markdown_lint/markdown_lint.py content/software/app-lab
```

### Auto-Fix Formatting Issues

Automatically fix formatting issues:

```bash
python3 scripts/validation/markdown_lint/markdown_lint.py content --fix
```

## Configuration & Ignores

- **Baseline Config:** `content/.markdownlint.yaml`
- **Subdirectory Overrides:** A `.markdownlint.yaml` in any subdirectory merges with and overrides specific rules from the baseline config.
- **Ignore Files:** `.lintignore` (universal), `.markdownlintignore` (tool-specific), and `.linterignore` (legacy compatibility).
