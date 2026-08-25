# Documentation Validation Suite

This directory contains the automated validation tools for `arduino/docs-content`. The suite ensures formatting quality, link integrity, asset tracking, and metadata compliance across all documentation pages.

---

## Tool Overview

| Tool | Script Location | CI Job Name | Description |
| :--- | :--- | :--- | :--- |
| **Markdown Lint** | `scripts/validation/markdown_lint/markdown_lint.py` | `Markdown Check` | Enforces Markdown formatting standards with hierarchical config inheritance. |
| **Alert Blocks** | `scripts/validation/alert_tags/alert_tags.py` | `Alert Check` | Enforces and formats empty-line spacing and indentation for MDX `<Alert>` blocks. |
| **Relative Links** | `scripts/validation/relative_links/relative_links.py` | `Link Check` | Validates all relative links and `#heading-slug` anchors against production route mappings. |
| **Image & Assets** | `scripts/validation/image_links/image_links.py` | `Image Check` | Flags broken image references and identifies orphaned files in `assets/` folders. |
| **Content Linter (Legacy)** | `scripts/validation/content-lint.sh` | `Content Linter (Hardware)` | Runs legacy YAML frontmatter schema checks for hardware tutorials during migration. |

---

## Quickstart (Running Checks Locally)

Run all checks from the repository root:

```bash
# 1. Validate Markdown formatting
python3 scripts/validation/markdown_lint/markdown_lint.py content

# 2. Validate Alert block formatting
python3 scripts/validation/alert_tags/alert_tags.py validate content

# 3. Validate internal links and heading anchors
python3 scripts/validation/relative_links/relative_links.py validate content

# 4. Validate image references and orphaned assets
python3 scripts/validation/image_links/image_links.py validate content

# 5. Spell check
codespell -I scripts/resources/spell-check-ignore-list.txt ./content/
```

---

## Ignore System Architecture

Validation tools traverse upwards from the target directory to the repository root to discover ignore files.

### 1. Universal Content Ignore (`.lintignore`)

Place a `.lintignore` file in `content/` or any subdirectory to exclude unmigrated directories across **all** validation tools:

```gitignore
# Exclude legacy hardware directories from all validation checks
hardware/01.mkr/
hardware/08.legacy/
```

### 2. Tool-Specific Ignores

When a directory needs a specific tool bypassed without disabling other checks:

- **`.markdownlintignore`**: Skips Markdown formatting checks (e.g. for auto-generated docs or complex MDX).
- **`.linklintignore`**: Skips relative link validation (e.g. for draft docs with pending route targets).
- **`.imagelintignore`**: Skips image asset validation.

---

## Further Documentation

Detailed documentation for each tool is available in its respective directory:

- [Markdown Lint Documentation](markdown_lint/README.md)
- [Alert Tags Validator Documentation](alert_tags/README.md)
- [Relative Links Validator Documentation](relative_links/README.md)
- [Image Links Validation Documentation](image_links/README.md)
