# Documentation Validation Suite

This directory contains the automated validation tools for `arduino/docs-content`. The suite checks formatting, links, assets, and selected metadata. Coverage varies by tool, content type, and ignore configuration; see [Validation and Preview](../../CONTRIBUTING.md#validation-and-preview).

---

## Tool Overview

| Tool | Script Location | CI Job Name | Description |
| :--- | :--- | :--- | :--- |
| **Markdown Lint** | `scripts/validation/markdownlint/markdownlint.py` | `Markdown Check` | Enforces Markdown formatting standards with hierarchical config inheritance. |
| **Alert Blocks** | `scripts/validation/alert_tags/alert_tags.py` | `Alert Check` | Enforces and formats empty-line spacing and indentation for MDX `<Alert>` blocks. |
| **Relative Links** | `scripts/validation/relative_links/relative_links.py` | `Link Check` | Checks inline root-relative and URL-relative article links and anchors against the route index. |
| **Image & Assets** | `scripts/validation/image_links/image_links.py` | `Image Check` | Flags broken image references and identifies orphaned files in `assets/` folders. |
| **Content Linter (Legacy)** | `scripts/validation/content-lint.sh` | `Content Linter` | Checks selected hardware tutorial and datasheet metadata and content using its own configuration. |

---

## Quickstart (Running Checks Locally)

Run these checks from the repository root:

```bash
# 1. Validate Markdown formatting
python3 scripts/validation/markdownlint/markdownlint.py content

# 2. Validate Alert block formatting
python3 scripts/validation/alert_tags/alert_tags.py validate content

# 3. Validate internal links and heading anchors
python3 scripts/validation/relative_links/relative_links.py validate content

# 4. Validate image references
python3 scripts/validation/image_links/image_links.py validate content
```

For spelling checks and their language-specific exclusions, follow the commands in the [validation workflow](../../.github/workflows/workflow-validate.yaml). The legacy content linter must run from `scripts/validation`; see [Frontmatter Validation](../../CONTRIBUTING.md#frontmatter-validation). Unlinked-asset reporting and removal use separate commands documented in the [image validator guide](image_links/README.md).

---

## Ignore System Architecture

The Python validation tools traverse upwards from the target directory to the repository root to discover ignore files. The legacy content linter uses [its own configuration](config/), and spelling checks use the exclusions in the workflow.

### 1. Shared Python-Tool Ignore (`.lintignore`)

Place a `.lintignore` file in `content/` or any subdirectory to exclude unmigrated directories from the Python Markdown, Alert, link, and image checks. It does not control the legacy content linter or spelling checks:

```gitignore
# Exclude legacy hardware directories from the Python checks
hardware/01.mkr/
hardware/08.legacy/
```

### 2. Tool-Specific Ignores & Retention

When a directory needs a specific tool bypassed or assets preserved:

- **`.markdownlintignore`**: Skips Markdown formatting checks (e.g. for auto-generated docs or complex MDX).
- **`.alertlintignore`**: Skips Alert formatting checks.
- **`.linklintignore`**: Skips relative link validation (e.g. for draft docs with pending route targets).
- **`.imagelintignore`**: Skips image asset validation.
- **`.assetsignore` / `.keepassets`**: Preserves unreferenced, standalone, or dynamically loaded image assets in `assets/` folders without triggering orphaned asset errors or removals during `validate-unlinked` / `remove-unlinked`.

---

## Further Documentation

Detailed documentation for each tool is available in its respective directory:

- [Markdown Lint Documentation](markdownlint/README.md)
- [Alert Tags Validator Documentation](alert_tags/README.md)
- [Relative Links Validator Documentation](relative_links/README.md)
- [Image Links Validation Documentation](image_links/README.md)
