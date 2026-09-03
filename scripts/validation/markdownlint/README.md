# Markdown Lint Script

This script validates and formats Markdown files across the documentation using `markdownlint-cli` with automatic root configuration inheritance.

## Features

- **Markdown Standards Enforcement:** Enforces consistent Markdown formatting, heading conventions, list indentation, and code block styles.
- **Hierarchical Configuration Inheritance:** Baseline rules are defined in `content/.markdownlint.yaml`. Subdirectories can provide a local `.markdownlint.yaml` for domain-specific rule overrides while automatically inheriting all baseline rules.
- **Hierarchical Ignore Support:** Automatically honors `.lintignore`, `.markdownlintignore`, and legacy `.linterignore` files placed at any directory depth.
- **Auto-Fixing:** Automatically remediates fixable lint errors using the `--fix` flag.
- **Documentation Rule Validation:** Validates that active and disabled rules documented in this README stay strictly synchronized with `content/.markdownlint.yaml`.

## Requirements

- Python 3
- Node.js & `npx` (with `markdownlint-cli` installed in `scripts/validation/node_modules/` or executable via `npx`)

## Usage

Run the script from the repository root:

### Validate Markdown Files

Validate Markdown files across the entire `content` directory:

```bash
python3 scripts/validation/markdownlint/markdownlint.py content
```

Or validate a specific section:

```bash
python3 scripts/validation/markdownlint/markdownlint.py content/software/app-lab
```

### Auto-Fix Formatting Issues

Automatically fix formatting issues:

```bash
python3 scripts/validation/markdownlint/markdownlint.py content --fix
```

### Validate README Rule Documentation

Verify that this README accurately matches `content/.markdownlint.yaml`:

```bash
python3 scripts/validation/markdownlint/validate_readme.py
# or via markdownlint.py:
python3 scripts/validation/markdownlint/markdownlint.py --validate-readme
```

To automatically update and sync the rules tables in this README:

```bash
python3 scripts/validation/markdownlint/validate_readme.py --update
# or:
python3 scripts/validation/markdownlint/markdownlint.py --update-readme
```

## Rules & Configuration

The documentation suite enforces standard Markdown rules configured in [`content/.markdownlint.yaml`](../../../content/.markdownlint.yaml). All standard rules are active by default (`default: true`), with repository-specific customizations, exclusions, and custom rules detailed below.

<!-- MARKDOWNLINT-RULES:START -->
### Configured Active Rules & Customizations

Rules with repository-specific configuration in `content/.markdownlint.yaml`:

| Rule | Name | Status | Enforcement Details |
| :--- | :--- | :--- | :--- |
| [**MD010**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md010---hard-tabs) | `no-hard-tabs` | Active | Hard tabs forbidden; spaces enforced everywhere including code blocks (`code_blocks: true`). |
| [**MD024**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md024---multiple-headers-with-the-same-content) | `no-duplicate-heading` | Active | Duplicate headings allowed across different parent sections (`siblings_only: true`). |
| [**MD026**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md026---trailing-punctuation-in-header) | `no-trailing-punctuation` | Active | Trailing punctuation forbidden except question marks (`punctuation: ".,;:!。，；：！"`). |
| [**MD029**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md029---ordered-list-item-prefix) | `ol-prefix` | Active | Ordered lists accept either sequential (`1. 2. 3.`) or repeating (`1. 1. 1.`) prefixes (`style: "one_or_ordered"`). |
| [**MD031**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md031---fenced-code-blocks-should-be-surrounded-by-blank-lines) | `blanks-around-fences` | Active | Fenced code blocks immediately following list items permitted without extra blank lines (`list_items: false`). |
| [**MD033**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md033---inline-html) | `no-inline-html` | Active | Inline HTML restricted; allowed elements: `<Alert>`, `<sup>`, `<sub>`, `<br>` (`allowed_elements`). |
| [**no-h5**](rules/no-h5.cjs) | `no-h5-headings` | Active (Custom) | Heading levels deeper than H4 (H5, H6) are not supported. Enforced via `rules/no-h5.cjs`. |

### Disabled Rules

Rules explicitly disabled in `content/.markdownlint.yaml` (`false`):

| Rule | Name | Status | Reason for Exemption |
| :--- | :--- | :--- | :--- |
| [**MD004**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md004---unordered-list-style) | `ul-style` | Disabled (`false`) | Unordered list bullet style enforcement disabled to permit both `-` and `*` bullet markers. |
| [**MD013**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md013---line-length) | `line-length` | Disabled (`false`) | Line length limit disabled to prevent breaking long URLs, code samples, and technical prose. |
| [**MD014**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md014---dollar-signs-used-before-commands-without-showing-output) | `commands-show-output` | Disabled (`false`) | Dollar signs before terminal commands permitted in tutorial code snippets. |
| [**MD036**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md036---emphasis-used-instead-of-a-header) | `no-emphasis-as-heading` | Disabled (`false`) | Standalone bold/italic emphasis lines permitted for custom layout styling. |
| [**MD060**](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md060---table-column-style) | `table-column-style` | Disabled (`false`) | Table column pipe alignment enforcement disabled to minimize diff churn on edits. |

### Default Active Rules

The baseline configuration enables all standard `markdownlint` rules by default (`default: true`), except those explicitly disabled above. Key enforced default rules include:

| Rule | Name | Description |
| :--- | :--- | :--- |
| [**MD001**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md001---header-levels-should-only-increment-by-one-level-at-a-time) | `heading-increment` | Heading levels should only increment by one level at a time. |
| [**MD003**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md003---header-style) | `heading-style` | Consistent ATX heading style (`# Heading`). |
| [**MD005**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md005---inconsistent-indentation-for-list-items-at-the-same-level) | `list-indent` | Inconsistent indentation for list items at the same level. |
| [**MD006**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md006---consider-starting-bulleted-lists-at-the-beginning-of-the-line) | `ul-start-left` | Bullet lists start at the beginning of the line. |
| [**MD007**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md007---unordered-list-indentation) | `ul-indent` | Consistent unordered list indentation (2 spaces). |
| [**MD009**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md009---trailing-spaces) | `no-trailing-spaces` | Trailing spaces forbidden. |
| [**MD011**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md011---reversed-link-syntax) | `no-reversed-links` | Reversed link syntax `(text)[url]` forbidden. |
| [**MD012**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md012---multiple-consecutive-blank-lines) | `no-multiple-blanks` | Multiple consecutive blank lines forbidden. |
| [**MD018**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md018---no-space-after-hash-on-atx-style-header) | `no-missing-space-atx` | Space required after `#` in ATX headings. |
| [**MD019**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md019---multiple-spaces-after-hash-on-atx-style-header) | `no-multiple-space-atx` | Multiple spaces after `#` in ATX headings forbidden. |
| [**MD020**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md020---no-space-inside-hashes-on-closed-atx-style-header) | `no-missing-space-closed-atx` | Space required inside closed ATX headings. |
| [**MD021**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md021---multiple-spaces-inside-hashes-on-closed-atx-style-header) | `no-multiple-space-closed-atx` | Multiple spaces inside closed ATX headings forbidden. |
| [**MD022**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md022---headers-should-be-surrounded-by-blank-lines) | `blanks-around-headings` | Headings must be surrounded by blank lines. |
| [**MD023**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md023---headers-must-start-at-the-beginning-of-the-line) | `heading-start-left` | Headings must start at the beginning of the line. |
| [**MD025**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md025---multiple-top-level-headers-in-the-same-document) | `single-title` | Single top-level heading (`# Title`) per document. |
| [**MD027**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md027---multiple-spaces-after-blockquote-symbol) | `no-multiple-space-blockquote` | Multiple spaces after blockquote `>` forbidden. |
| [**MD028**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md028---blank-line-inside-blockquote) | `no-blanks-blockquote` | Blank lines inside blockquotes forbidden. |
| [**MD030**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md030---spaces-after-list-markers) | `list-marker-space` | Consistent spacing after list markers. |
| [**MD032**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md032---lists-should-be-surrounded-by-blank-lines) | `blanks-around-lists` | Lists must be surrounded by blank lines. |
| [**MD034**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md034---bare-url-used) | `no-bare-urls` | Bare URLs must use link formatting `[text](url)` or `<url>`. |
| [**MD035**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md035---horizontal-rule-style) | `hr-style` | Consistent horizontal rule style (`---`). |
| [**MD037**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md037---spaces-inside-emphasis-markers) | `no-space-in-emphasis` | Spaces inside emphasis markers (`* text *`) forbidden. |
| [**MD038**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md038---spaces-inside-code-span-elements) | `no-space-in-code` | Spaces inside code span elements (`` ` code ` ``) forbidden. |
| [**MD039**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md039---spaces-inside-link-text) | `no-space-in-links` | Spaces inside link text (`[ text ](url)`) forbidden. |
| [**MD040**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md040---fenced-code-blocks-should-have-a-language-specified) | `fenced-code-language` | Fenced code blocks must specify an explicit language identifier. |
| [**MD041**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md041---first-line-in-file-should-be-a-top-level-header) | `first-line-heading` | First line of document must be a top-level heading. |
| [**MD042**](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md042---no-empty-links) | `no-empty-links` | Empty link targets (`[]()`) forbidden. |
| [**MD043**](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md043---required-heading-structure) | `required-headings` | Required heading structure. |
| [**MD044**](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md044---proper-names-should-have-the-correct-capitalization) | `proper-names` | Proper name capitalization consistency. |
| [**MD045**](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md045---images-should-have-alternate-text-alt-text) | `no-alt-text` | Images must provide descriptive alternative text. |
| [**MD046**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md046---code-block-style) | `code-block-style` | Consistent code block style (fenced). |
| [**MD047**](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md#md047---file-should-end-with-a-single-newline-character) | `single-trailing-newline` | Files must end with a single newline character. |
| [**MD048**](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md048---code-fence-style) | `code-fence-style` | Consistent code fence style (backticks). |
| [**MD049**](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md049---emphasis-style) | `emphasis-style` | Consistent emphasis style (`*italic*`). |
| [**MD050**](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md050---strong-style) | `strong-style` | Consistent strong emphasis style (`**bold**`). |
<!-- MARKDOWNLINT-RULES:END -->

## Configuration & Ignores

- **Baseline Config:** `content/.markdownlint.yaml`
- **Subdirectory Overrides:** A `.markdownlint.yaml` in any subdirectory merges with and overrides specific rules from the baseline config.
- **Ignore Files:** `.lintignore` (universal), `.markdownlintignore` (tool-specific), and `.linterignore` (legacy compatibility).

## Rule Validation System

To prevent documentation rot and ensure contributors always have accurate guidance, the active and disabled rules in this README are automatically validated against `content/.markdownlint.yaml`:

- **Automatic Verification:** Running `python3 scripts/validation/markdownlint/markdownlint.py content` validates this README before linting files. If a rule is toggled or reconfigured in `.markdownlint.yaml` without updating this README, validation fails.
- **Manual Verification:** Run `python3 scripts/validation/markdownlint/validate_readme.py` (or `markdownlint.py --validate-readme`) to verify synchronization.
- **Automatic Synchronization:** Run `python3 scripts/validation/markdownlint/validate_readme.py --update` (or `markdownlint.py --update-readme`) to regenerate the rules tables directly from the YAML configuration.

