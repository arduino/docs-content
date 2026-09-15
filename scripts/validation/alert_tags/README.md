# Alert Tags Validator & Formatter

This script validates and formats MDX `<Alert>` blocks across the documentation.

## Why Alert Formatting Matters in MDX

In MDX (MDX v1 / Gatsby), content inside JSX components like `<Alert>` requires blank lines around the inner text to be processed as Markdown blocks:

- **Without blank lines (`<Alert>...`):** MDX treats the body as raw JSX children. Markdown syntax (bold `**`, code spans `` ` ``, links) is **not** rendered, and unescaped angle brackets (e.g. `<model>`, `<ip-address>`) cause JSX compilation errors.
- **With blank lines (`<Alert>\n\n...\n\n</Alert>`):** MDX processes the body as Markdown, correctly compiling bold, code spans, links, and code fences.

This tool guarantees that all Alert blocks follow this standard, while strictly preserving indentation for Alerts nested inside lists.

---

## Features

- **Deterministic Formatting:** Guarantees an empty line after the opening tag and before the closing tag.
- **List Indentation Preservation:** Correctly maintains indentation (e.g. 3 or 4 spaces) for Alert blocks inside numbered or bulleted list items.
- **Hierarchical Ignore Support:** Honors `.lintignore`, `.linterignore`, and `.alertlintignore` files across directory hierarchies.
- **Auto-Fixing:** Automatically formats invalid Alert blocks with the `fix` command or `--fix` flag.

---

## Usage

Run from the repository root:

### Validate Alert Blocks

Validate all Markdown files in `content`:

```bash
python3 scripts/validation/alert_tags/alert_tags.py validate content
```

Or validate a specific subdirectory:

```bash
python3 scripts/validation/alert_tags/alert_tags.py validate content/software/app-lab
```

### Auto-Fix Alert Blocks

Automatically format and fix all Alert blocks:

```bash
python3 scripts/validation/alert_tags/alert_tags.py fix content
```
