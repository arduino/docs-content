# Contributing to Arduino Documentation

Thank you for contributing to [Arduino Docs](https://docs.arduino.cc). Use this guide for contribution scope, pull request workflow, and local validation, together with the detailed authoring references in [`docs/`](docs/content-structure.md).

## Scope

Contributions should help readers understand or use Arduino hardware, software, and services.

* **Discuss major additions first:** Open an [issue](https://github.com/arduino/docs-content/issues) before writing a new tutorial, guide, or section restructuring.
* **Community project showcases:** End-to-end maker projects belong on [Arduino Project Hub](https://projecthub.arduino.cc/), not in product documentation.
* **Sibling documentation repos:** Fixes for the Language Reference (`/language-reference`), Library Reference (`/libraries`), or Arduino CLI pages (`/arduino-cli`) belong in their respective upstream repositories; see [Documentation Ecosystem](README.md#documentation-ecosystem).
* **Third-party tools:** Document external services or hardware only when required for a supported Arduino workflow, stating prerequisites and limitations neutrally without promotional copy.
* **Focused diffs:** When fixing a typo or broken link, keep the diff surgical—do not rename folders, reformat untouched sections, or mass-convert legacy callouts in the same pull request.

## Contribution Workflow

### Quick Corrections

For small text or link fixes, edit the file directly on GitHub or in a local branch:

* Search by frontmatter `title`, `description`, or a distinctive phrase inside `content/`—published URLs strip numeric folder prefixes and filenames such as `content.md`.
* Verify how the page renders on <https://docs.arduino.cc> before treating a GitHub Markdown preview difference as a bug.

### Branches and Pull Requests

1. Fork the repository (external contributors) or create a new branch in `arduino/docs-content` (maintainers), always branching from the latest `main`.
2. Name the branch descriptively for a single topic, such as `username/fix-uno-q-spi-pins`.
3. Follow the conventions in [Authoring Reference](#authoring-reference) and any section-specific guide (such as the [App Lab README](content/software/app-lab/README.md)).
4. Run the relevant checks in [Validation and Preview](#validation-and-preview) and complete the [pull request template](pull_request_template.md), noting what you verified and any hardware or rendering checks you could not run locally.

## Content Types

| Content Type | Purpose | Starting Point |
| --- | --- | --- |
| **Tutorial** | Teaches a complete, concrete outcome through ordered steps, code, testing, and troubleshooting | [Tutorial template](contribution-templates/tutorial-template/tutorial-template.md) |
| **How-To Guide** | Solves a narrow, practical task for readers who already know the basics | [How-To template](contribution-templates/how-to-template/how-to-template.md) |
| **Conceptual Article** | Explains an engineering or software concept, terminology, and practical links | [Article template](contribution-templates/article-template/article-template.md) |
| **Hardware Product Page & Datasheet** | Defines product overview, specs, downloads, and PDF datasheets from verified engineering data | [Product & Datasheet metadata](docs/content-structure.md#frontmatter-and-product-page-files) |
| **Navigation Overviews & Fragments** | Category/family/software index files (`family.md`, `category.md`, `software.md`) and included tabs (`features.md`) | [Overview files and fragments](docs/content-structure.md#overview-files-and-fragments) |

Template prose and sample metadata in [`contribution-templates/`](contribution-templates/README.md) are scaffolding—replace every placeholder before opening a pull request. Never invent SKUs, electrical limits, pin mappings, or compatibility claims.

## Authoring Reference

Detailed structural, routing, editorial, and syntax rules live in `docs/`:

| Topic | Reference |
| --- | --- |
| Directory naming, hardware folder layout, and finding source files | [Directory Layout and Naming](docs/content-structure.md#directory-layout-and-naming) |
| Sidebar ordering (`content/order.json`), numeric prefixes, and grouped tutorials (`category.md`) | [Sidebar Structure and Ordering](docs/content-structure.md#sidebar-structure-and-ordering) |
| Tutorial, datasheet, and product frontmatter (`overview.md`, `cardList.md`, `relevance.md`) | [Frontmatter and Product Page Files](docs/content-structure.md#frontmatter-and-product-page-files) |
| Published URL routes, relative links, `/resources/` downloads, and multi-file pinouts/schematics | [Links, Routing, and Downloadable Resources](docs/content-structure.md#links-routing-and-downloadable-resources) |
| Translated tutorials (`<name>-<lang>.md`) and localized datasheets (`<lang>-datasheet.md`) | [Localization](docs/content-structure.md#localization) |
| Shared symlinked tutorials, moving pages safely, and auto-generated tables | [Shared Content, Moving Pages, and Generated Regions](docs/content-structure.md#shared-content-moving-pages-and-generated-regions) |
| Voice, American English, terminology, and board-agnostic phrasing | [Writing Style](docs/style-and-syntax.md#writing-style) |
| Title Case, H2–H4 hierarchy, UI labels, units, lists, and troubleshooting | [Titles and Headings](docs/style-and-syntax.md#titles-and-headings) & [Text Formatting](docs/style-and-syntax.md#text-formatting) |
| Fenced code blocks, `<placeholder>` escaping, and Markdown tables | [Code, Commands, and Tables](docs/style-and-syntax.md#code-commands-and-tables) |
| Image captions, cropping, circuit diagrams, and PR file-size limits | [Images, Diagrams, and Assets](docs/style-and-syntax.md#images-diagrams-and-assets) |
| MDX `<Alert>` blocks, self-closed void tags (`<br/>`), and JSX/MDX compilation rules | [Callouts, MDX, and HTML Rules](docs/style-and-syntax.md#callouts-mdx-and-html-rules) |

## Validation and Preview

### Running Validation Locally

You need **Python 3** and **Node.js 22+** (`npm` / `npx`) to run the local checks; you do **not** need root `npm install`. Run checks from the repository root, substituting `content` with your changed path for fast iteration (or checking all `content` when moving/renaming pages):

```bash
# 1. Markdownlint (loads content/.markdownlint.yaml, local overrides, and custom rules)
python3 scripts/validation/markdownlint/markdownlint.py content/software/app-lab

# 2. MDX compiler check (catches unclosed <br>, mismatched HTML, and JSX syntax errors)
npm ci --prefix scripts/validation/mdx
node scripts/validation/mdx/mdx-check.js content/software/app-lab

# 3. MDX <Alert> spacing and indentation check
python3 scripts/validation/alert_tags/alert_tags.py validate content/software/app-lab

# 4. Internal route, heading anchor, symlink, and /resources/ download check
python3 scripts/validation/relative_links/relative_links.py validate content/software/app-lab

# 5. Image reference and case-sensitivity check
python3 scripts/validation/image_links/image_links.py validate content/software/app-lab
```

* Use the Python `markdownlint.py` wrapper rather than bare `npx markdownlint-cli` so hierarchical configs and custom rules (`no-h5`) apply accurately, and confirm the output reports a non-zero file count.
* Pass `--absolute` to `relative_links.py validate` to also verify full `https://docs.arduino.cc/...` links offline against the route map.
* Only run auto-fix modes (`markdownlint.py --fix`, `alert_tags.py fix`, `relative_links.py fix`) on your targeted directory, and inspect `git diff` afterward. Never run destructive asset-removal commands (`image_links.py remove-unlinked`) without checking shared references first.

### Frontmatter Validation

CI runs the legacy schema linter against `content/hardware/` to enforce [tutorial](scripts/validation/rules/tutorial-metadata-schema.json) and [datasheet](scripts/validation/rules/datasheet-metadata-schema.json) metadata schemas. Run it from `scripts/validation/`:

```bash
cd scripts/validation && ./content-lint.sh -p '../../content/hardware/'
```

### Spell Checking

CI checks English content with `codespell` (automatically skipping localized datasheets and translated `<name>-<lang>.md` tutorials) and checks localized datasheets with language-specific `cspell` dictionaries. Copy the exact commands from [`.github/workflows/workflow-validate.yaml`](.github/workflows/workflow-validate.yaml), and add terms to [`scripts/resources/spell-check-ignore-list.txt`](scripts/resources/spell-check-ignore-list.txt) only for genuine technical vocabulary.

### Ignore Files and Tool Boundaries

* `.lintignore` (and tool-specific `.markdownlintignore`, `.alertlintignore`, `.linklintignore`, `.imagelintignore`) excludes unmigrated legacy directories from outbound Python lint checks; see [`scripts/validation/README.md`](scripts/validation/README.md).
* **Two critical exceptions:**
  1. **`MDX Check` (`mdx-check.js`) intentionally ignores `.lintignore`**, because Gatsby compiles every Markdown file in `content/` during deployment.
  2. **`Link Check` (`relative_links.py`) still indexes ignored files in the route map**, so maintained pages can link to legacy pages without false broken-link errors.
* Never add paths to ignore files just to silence errors in new or edited content.

### Previewing Changes

* **PR Previews:** When a maintainer adds the `preview` label to an in-repository pull request, CI builds the site and posts a Netlify preview URL comment. Pushing additional commits removes the `preview` label automatically; re-apply it when you want a fresh preview build.
* **Local Preview (Maintainers):** Clone [`arduino/docs.arduino.cc`](https://github.com/arduino/docs.arduino.cc) (requires `REPO_ACCESS_TOKEN`), symlink this repo's `content/` directory to `docs.arduino.cc/content`, and run `npm run dev` there. Restart `npm run dev` after editing `content/order.json` or adding/renaming directories.
* **Visual Review:** GitHub's Markdown viewer does not match production MDX rendering. Always inspect headings, `<Alert>` callouts, captions, tables, links, and mobile widths in the preview build.

## Licensing and Attribution

* Prose, diagrams, and media contributions are licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
* Code examples are dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).
* Verify compatible licensing and include attribution before incorporating any external text, code, schematic, or image, and preserve existing author credits unless intentionally updating attribution. See [LICENSE.md](LICENSE.md).
