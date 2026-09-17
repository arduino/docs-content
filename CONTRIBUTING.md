# Contributing to Arduino Documentation

This is the authoring reference for content published at <https://docs.arduino.cc>. Use it when creating, editing, reviewing, or moving documentation in this repository.

## Scope

Contributions should help readers understand or use Arduino products and features.

* Discuss substantial new topics in an [issue](https://github.com/arduino/docs-content/issues) before writing them.
* General project showcases belong on [Project Hub](https://projecthub.arduino.cc/).
* Avoid duplicate articles and third-party promotion.
* Explain third-party tools when they are necessary to the documented Arduino workflow, including their prerequisites and limitations.

## Using This Reference

This file defines shared authoring conventions.

* The [contribution templates](contribution-templates/README.md) provide starting structures, not a separate style standard.
* Section-specific maintenance instructions, such as the [App Lab guide](content/software/app-lab/README.md), supplement this reference.
* Do not apply a product-specific compatibility statement or asset layout to unrelated sections.
* Follow these conventions for new and substantially revised content.
* Keep small corrections focused: do not rename directories, convert unrelated legacy pages, or reformat whole articles as a side effect of fixing a typo.
* Report conflicts between this reference and tooling instead of weakening validation or inventing an exception.

## Contribution Workflow

### Small Corrections

Use GitHub's file editor for a small correction, or edit a local branch.

* Locate the source by title, description, or a distinctive sentence; the published URL is not always a filesystem path.
* Check the rendered website before treating a GitHub rendering difference as a content bug.

### Branches and Pull Requests

Fork and clone the repository, or create a branch if you have write access.

* Start from current `main`.
* Give the branch a descriptive, focused name, such as `username/fix-blink-instructions`.
* Keep each change about one topic.
* Review the diff, run relevant checks, and describe the change and verification in the [pull request template](pull_request_template.md).

## Content Types

### Tutorials

* A tutorial teaches a concrete outcome through an ordered sequence.
* Use the [tutorial template](contribution-templates/tutorial-template/tutorial-template.md).
* State the goal, prerequisites, circuit when relevant, programming steps, expected result, troubleshooting, and conclusion.
* Explain unfamiliar concepts before asking readers to use them.

### How-To Guides

* A how-to solves a narrower task for a reader with the necessary background.
* Use the [how-to template](contribution-templates/how-to-template/how-to-template.md).
* Provide prerequisites, the procedure, working code when needed, and related reading.
* Do not pad a short procedure with unrelated theory.

### Conceptual Articles

* An article explains a concept rather than requiring a sequence of actions.
* Use the [article template](contribution-templates/article-template/article-template.md).
* Organize it around the reader's questions, define terminology, and link to practical applications.

### Hardware Product Pages and Datasheets

* Product pages describe a specific product and connect its documentation, specifications, and store information.
* Datasheets are technical references with a different metadata schema and rendering workflow.
* Use verified product information; never invent a SKU, electrical rating, pin assignment, certification, release date, or compatibility claim to complete a template.
* See [datasheet tooling](scripts/datasheet-rendering/) before changing a datasheet's structure.

### Navigation Overviews and Fragments

* Family, category, and software overview files carry navigation metadata and, where applicable, introductory copy.
* Fragments such as `features.md` are included in a larger page and may have no frontmatter.
* Do not turn every Markdown file into a standalone article.

## Repository Structure

### Finding an Existing Article

* Search frontmatter `title` and `description` as well as filenames.
* An article called "Multimeter Basics" lives below a numbered category; hardware tutorials often use the generic filename `content.md`.
* Confirm the product and article content before editing a search match.

For example, from the repository root:

```bash
rg -n --glob '*.md' 'Multimeter Basics|multimeter features' content
```

### Directory and File Names

* Use descriptive lowercase names with hyphens between words for new paths.
* Preserve exact case in references to existing files.
* Avoid spaces and underscores in new article directory names.

Hardware commonly follows this layout:

```text
content/hardware/<family>/<product-type>/<product>/
  product.md
  features.md
  tech-specs.yml
  datasheet/datasheet.md
  tutorials/<tutorial>/content.md
```

* An article may instead use a matching filename, such as `blink/blink.md`.
* Follow its content type and neighboring maintained pages; a matching filename is not a universal requirement.
* Do not rename existing files merely to match an example in this reference.

### Ordering Prefixes

* Navigation trees that use ordered directories have prefixes such as `01.` or `1.`.
* Continue the surrounding convention.
* For a new ordered group of ten or more entries, use leading zeros consistently so lexical sorting preserves the intended order.
* Numbering is not required on every directory.
* Structural directories such as `boards`, `tutorials`, and `assets`, and product slugs such as `uno-q`, remain unnumbered.
* Changing a prefix can affect navigation even when the published slug stays the same.

### Overview Files

* Overview filenames and metadata depend on the content type: examples include `family.md`, `category.md`, `software.md`, and named category files such as `setup.md` in App Lab.
* Inspect the relevant section before adding one.
* `product.md` is a product page, not a generic replacement for every category overview.

## Frontmatter

Standalone content generally starts with YAML frontmatter between `---` delimiters.

```yaml
---
title: Setup Arduino App Lab
overwriteSidebar: Overview
description: Learn about different setup options for Arduino App Lab.
tags:
  - Getting Started
  - Arduino App Lab
  - UNO Q
---
```

### Article Metadata

The [tutorial schema](scripts/validation/rules/tutorial-metadata-schema.json) defines the following fields. Its current CI application is to selected hardware tutorials, not every Markdown file. Use the common article fields for new prose articles unless their content type specifies otherwise; do not assume unvalidated metadata has a supported rendering effect.

| Field | Type | Required | Purpose |
| --- | --- | --- | --- |
| `title` | String | Yes | Maximum 60 characters under this schema; page title in Title Case |
| `description` | String | Yes | Concise description of what the reader learns or accomplishes |
| `author` | String | Yes | Actual author or approved attribution |
| `tags` | Array of strings | Yes | Relevant topic tags, following existing terminology |
| `difficulty` | String | No | `beginner`, `intermediate`, or `advanced` |
| `hardware` | Array of strings | No | Hardware identifiers; use established values |
| `software` | Array of strings | No | Software identifiers; use established values |
| `compatible-products` | Array of strings | No | Verified compatible-product identifiers |
| `libraries` | Array of objects | No | Library objects with `name` and `url` strings |
| `coverImage` | String | No | Cover-image reference |
| `featuredImage` | String | No | Featured-image reference |
| `hero_position` | Integer | No | Hero positioning value; preserve section usage |
| `overwriteSidebar` | String | No | Sidebar override; confirm the section's expected value |
| `beta` | Boolean | No | Beta metadata; also explain limitations in the article |
| `source` | String | No | Source reference |
| `primary_button_title` | String | No | Maximum 15 characters |
| `secondary_button_title` | String | No | Maximum 20 characters |

The schema rejects additional fields. It does not establish all identifier vocabularies or image-path semantics: check maintained examples and the site preview rather than guessing.

### Datasheet Metadata

The [datasheet schema](scripts/validation/rules/datasheet-metadata-schema.json) is separate from the article schema and also rejects additional fields.

| Field | Type | Required | Purpose |
| --- | --- | --- | --- |
| `title` | String | Yes | Maximum 60 characters |
| `identifier` | String | Yes | Approved datasheet identifier |
| `type` | String | Yes | `maker`, `edu`, `pro`, or `limited-edition` |
| `author` | String | No | Author attribution |
| `hardwareRevision` | String | No | Hardware revision |
| `revision` | String | No | Document revision |
| `variant` | String | No | Product variant |
| `isPreviousRevision` | Boolean | No | Previous-revision status |
| `isDraft` | Boolean | No | Draft status |

Preserve identifiers and revision information unless the change explicitly updates them. Localized datasheets have additional language-specific workflow considerations.

### Product Metadata

Product metadata is not validated by the two schemas above. These are established fields illustrated by [VENTUNO Q's product page](content/hardware/14.ventuno/boards/ventuno-q/product.md), not a declaration that every product requires every field.

| Field | Observed Type | Required | Purpose |
| --- | --- | --- | --- |
| `title` | String | Yes | Official product name |
| `url_shop` | String | No | Product store URL |
| `primary_button_url`, `secondary_button_url` | String | No | Destination for the respective button |
| `primary_button_title`, `secondary_button_title` | String | No | Visible button label |
| `forumCategorySlug` | String | No | Product forum category path |
| `sku` | Array of strings | No | Approved product SKU identifiers |
| `useCases` | Array of strings | No | Existing use-case taxonomy values |
| `relevance` | Number | No | Product relevance metadata |
| `releaseDate` | Date (`YYYY-MM-DD`) | No | Verified release date |
| `isNew` | Boolean | No | New-product metadata |

Confirm new taxonomy values and button behavior with the content maintainer. Do not copy another board's identifiers or infer undocumented field requirements from a single example.

### Overview Metadata and Fragments

Hardware categories, software sections, and family overview files (e.g. `software.md`, `category.md`, `family.md`, `setup.md`) have their own frontmatter requirements. Copy the structure of the matching type, not the article schema.

Repository READMEs, this reference, and included fragments (like `features.md`) do not need article frontmatter.

## Writing Style

### Audience and Assumptions

* Write for the reader who needs to complete the documented task.
* State required hardware, software versions, prior setup, and background knowledge.
* Define unfamiliar concepts or link to an explanation.
* A tutorial should teach one outcome well.

### Voice and Point of View

* Use active voice and address the reader as "you" in instructions.
* Prefer direct imperatives.
* Explain what a component does in present tense.
* Use future tense only for a genuinely future event, not to narrate every step.

| Use | Avoid |
| --- | --- |
| Connect the board to your computer. | The board should be connected to the computer. |
| Select **Upload**. | Now we are going to select Upload. |
| The LED turns on when the input is high. | You will see that the LED will turn on. |

### Concise and Inclusive Language

* Use short sentences and concrete verbs.
* Omit filler such as "simply," "just," "obviously," "easy," and "leverage."
* Explain the action instead of evaluating its difficulty.
* Avoid idioms, unexplained jargon, and assumptions about the reader's experience or abilities.

### English Spelling

* Use American English in new prose: "color," "initialize," and "behavior."
* Preserve exact spelling in UI labels, quotations, filenames, and identifiers.
* Do not translate or normalize localized datasheets into English as part of a spelling correction.

### Terminology and Product Names

* Define technical terms on first use and expand unfamiliar acronyms.
* Use the same name for the same concept throughout a page.
* Preserve official spellings such as Arduino, MicroPython, OpenMV, and Wi-Fi, and the exact capitalization of APIs and products.
* Use "your board" when the instructions apply to every supported board in the article.
* Name the exact board when pinouts, voltage limits, setup, or compatibility differ.
* Board-agnostic wording must not imply unsupported compatibility.

### Versions and Technical Claims

* Prefer a specific version or date to "recently," "new," or "the latest."
* Identify preview features and restrictions in the prose.
* Verify technical specifications and code behavior against authoritative sources.
* Mark unresolved information for review rather than inventing it.

For example-code pedagogy, also consult the [Arduino writing guide](content/learn/08.contributions/00.arduino-writing-style-guide/arduino-writing-style-guide.md).

## Titles and Headings

### Capitalization

* Use Title Case for page titles and headings.
* Capitalize the first and last words and principal words; keep short articles, conjunctions, and prepositions lowercase unless first or last.
* For example: "Connect to a Wireless Network" and "Read Data from the Sensor."
* Preserve product names, code identifiers, and literal UI labels even when their case differs.

### Hierarchy

* Use descriptive headings, not bold paragraphs that imitate headings. Published article titles come from frontmatter; follow the page type's template rather than adding a duplicate H1. Repository reference files such as this one use an H1 title.
* Use H2 for major article sections, H3 for subsections, and H4 when another level is necessary.
* Do not use H5 or H6. Restructure an overly deep topic into shallower sections or an actual list or table rather than hiding headings in emphasis.

### Punctuation and Uniqueness

* Do not end headings with punctuation except a question mark.
* Keep headings distinct within their parent section.
* Repeated labels such as "Parameters" can occur under different parent sections, but avoid ambiguous anchors when linking to them.
* Changing a heading can break links.

## Text Formatting

### UI Labels and Menu Sequences

* Bold visible UI labels and preserve their displayed spelling: select **Run**, then **Stop**.
* Separate menu choices with `>`: **Tools** > **Board** > **Arduino UNO**.
* Do not use inline code for a button merely because it starts a program.

### Inline Code and Keyboard Shortcuts

* Use backticks for filenames, paths, commands, variables, parameters, and literal values: `sketch.ino`, `digitalRead()`, `HIGH`, and `--port`.
* Name keyboard keys consistently, such as **Ctrl+C** or **Command+C**, and specify platform differences when they matter.
* Keep keyboard shortcuts separate from commands entered in a terminal.

### Emphasis and Quotations

* Use bold sparingly for important text.
* Do not use italics or triple emphasis as a substitute for a heading.
* Use blockquotes for quoted material and attribute the source; use Alerts for callouts.

### Numbers, Units, and Symbols

* Use numerals for measurements and put a space between a number and its unit: `3.3 V`, `20 mA`, and `64 kB`.
* Preserve case: `MB` and `Mb` do not express the same quantity.
* Use consistent units within a comparison and distinguish limits from typical values.

### Trademarks

* Preserve official product and technology names.
* Follow the relevant owner's trademark guidelines, including [Arduino's policy](https://www.arduino.cc/en/trademark).
* Do not add trademark symbols to code identifiers or invent legal wording.

## Procedures and Lists

### Ordered Procedures

* Use Markdown ordered lists for steps, not manually bolded numbers.
* Put one principal action in each step, and explain prerequisites before the reader needs them.
* State the expected result after an action that changes device or application state.

```markdown
1. Connect the board with a USB data cable.
2. Select the board and port in the IDE.
3. Select **Upload**. Wait for the upload to finish.
```

### Unordered Lists and Nesting

* Use unordered lists for items without an execution order.
* Use parallel grammatical structures; punctuate complete sentences, but not short labels.
* Indent continuation paragraphs and blocks to belong to the intended list item.
* Keep nesting shallow and use subsections for distinct topics.

### Troubleshooting

* Describe the symptom, a way to check the cause, and a corrective action.
* Avoid telling readers to repeat a whole tutorial without identifying what to inspect.
* Warn before destructive steps and distinguish software problems from wiring, power, and hardware compatibility issues.

## Code and Commands

### Fenced Code Blocks

* Use fenced blocks with a language identifier such as `arduino`, `cpp`, `python`, `bash`, `json`, or `yaml`.
* Use `text` for plain output.
* Put blank lines around blocks and preserve indentation inside code.
* Use spaces rather than hard tabs, including in code blocks (MD010).

### Commands and Output

* State the working directory and required environment before a command.
* Keep commands and their output in separate blocks so readers can copy commands without a shell prompt or log text.
* Use the correct shell syntax for each supported platform.
* Explain commands that overwrite, erase, flash, or otherwise modify data before asking readers to run them.

### Placeholders and Escaping

* Explain every value the reader must replace.
* In prose, enclose placeholders such as `<port>` in backticks; bare angle-bracket placeholders can be parsed as HTML/JSX.
* Use representative non-secret values and never include real access tokens or credentials.

### Working Examples

* Make code do one thing clearly.
* Supply imports, setup, dependencies, and relevant wiring; label partial snippets as partial.
* Test examples on the documented hardware/software when possible and disclose what has not been tested.
* Do not alter indentation merely to satisfy a presentation preference when it changes program behavior.

### Externally Sourced Code

* Existing pages may use a custom `CodeBlock` component to fetch public GitHub code, as described in the root README.
* However, the base Markdownlint HTML allowlist does not include `CodeBlock`.
* Confirm the section's existing configuration and preview support before introducing it.
* Do not assume any JSX component is supported because it resembles Markdown.

## Tables

### Syntax and Cell Content

* Use a header row and separator row.
* Keep spaces inside separators, and escape a literal pipe inside a cell as `\|`.
* Prefer short cells to paragraphs embedded in tables.

```markdown
| Parameter | Description |
| --- | --- |
| `pin` | Digital pin to read |
| `mode` | Input configuration |
```

### Choosing a Table

* Use tables for comparisons, parameters, field definitions, and compact reference data.
* Use prose or procedures when readers need explanations or an ordered sequence.
* Do not edit generated table regions by hand; see [Generated Content](#generated-content).

## Links and Routing

### Published Routes Versus Source Paths

A site's URL is not a filesystem address. In particular, `/content/...` is not a general published link prefix, and `/hardware/...` does not mean "relative to the hardware folder." A leading `/` means relative to the website root.

The [link validator](scripts/validation/relative_links/relative_links.py) builds a route index from source paths. Its rules include the examples below; confirm unusual page types in the site preview because this index is not the website renderer itself.

| Source Path | Route Used by the Validator |
| --- | --- |
| `content/hardware/02.uno/boards/uno-q/product.md` | `/hardware/uno-q/` |
| `content/hardware/02.uno/boards/uno-q/tutorials/01.blink/content.md` | `/tutorials/uno-q/blink/` |
| `content/software/app-lab/1.setup/1.overview/overview.md` | `/software/app-lab/setup/overview/` |
| `content/learn/04.electronics/01.multimeter-basics/multimeter-basics.md` | `/learn/electronics/multimeter-basics/` |

Hardware tutorial routes use the product slug and final tutorial directory, collapsing any intermediate tutorial categories. The default rule strips numeric directory prefixes and drops the entire Markdown filename. Renaming only that filename can therefore leave the validator route unchanged. Do not put multiple independent pages in one article directory: they can collide in the route index.

### Root-Relative Article Links

Use the published path from the site root:

```markdown
[UNO Q](/hardware/uno-q/)
[Blink Tutorial](/tutorials/uno-q/blink/)
```

* This form is useful across sections and is independent of the source page's route depth.
* It does not require preserving the physical `hardware/<family>/boards/` hierarchy.

### URL-Relative Article Links

URL-relative links are also valid.

* Resolve them from the article's published route, not its source directory.

From `/software/app-lab/setup/overview/`, this links to its sibling:

```markdown
[Linux Setup](../linux/)
```

* From `/tutorials/uno-q/blink/`, `../serial/` targets `/tutorials/uno-q/serial/` regardless of the number of physical category directories.
* Recalculate these links when moving a page.
* Preserve a section's consistent linking style; neither form is universally required.

### Extensions, Prefixes, and Trailing Slashes

* For article routes, omit numeric ordering prefixes and source filenames such as `content.md`.
* Prefer a trailing slash for a page route, before a query or fragment: `/page/#section`.
* The current validator also accepts routes without that final slash; this is not a hard lint failure.
* Do not strip extensions from assets such as `.pdf`, `.zip`, or `.png`.

### Anchors and Link Text

* Use descriptive link text rather than "click here."
* Use `#section-heading` for a same-page heading or `/page/#section-heading` for another page.
* The checker lowercases headings, hyphenates whitespace, and removes punctuation to derive anchors.
* Duplicate and unusually formatted headings need preview verification; do not guess a numbered duplicate-anchor suffix.

### Absolute URLs and Downloads

* Use full `https://` URLs for external sites.
* Full `https://docs.arduino.cc/...` URLs also occur in content, but the internal link checker skips them, including their anchors.
* Prefer a site path for internal articles when you want route validation.
* Verify external destinations manually.
* Link downloads to the actual asset with its extension and indicate the file type in the link text.
* Image/asset validation is separate from article-route validation.

### Repository Documentation Links

* READMEs, contribution instructions, and tooling documentation are read on GitHub and use real relative filesystem links, including `.md`: `[Contributing](CONTRIBUTING.md)`.
* Do not convert these to published article routes or apply article frontmatter rules to them.

## Images and Captions

### Asset Locations and Names

* Usually place images in the article's `assets/` directory and reference them with a relative filesystem path.
* App Lab uses a shared section-level `assets/` directory; follow its local maintenance instructions.
* Use descriptive, hyphenated filenames and exact case in references.

### Captions and Alternative Text

* The text in Markdown image syntax becomes a visible caption on the documentation site.
* Write it to describe the image's relevant information; it is also alternative text, so do not use a filename, "image," or a direction such as "see above" as the entire description.

```markdown
![Serial Monitor showing the button state](assets/button-state.png)
```

* Explain important information in nearby prose as well.
* A screenshot alone must not be the only source of a required command, pin assignment, or warning.

### Screenshot Framing and Readability

* Crop screenshots to the relevant UI while retaining enough context to locate the control.
* Use a resolution at which labels remain readable; there is no blanket 1920×1080 requirement.
* Avoid unnecessary desktop areas and keep related screenshots visually consistent.
* State the platform or software version when its UI differs materially from the instructions.

### Annotations and Sensitive Information

* Keep annotations readable and do not rely on color alone to identify the target.
* Remove credentials, personal information, private project names, and unrelated notifications before capturing or exporting images.
* Do not obscure UI labels that the reader needs to recognize.

### Circuit Diagrams

* Use a wiring illustration when beginners need help identifying components, and a schematic when circuit behavior matters.
* Match pin names, component values, and voltages to the prose and code.
* Include necessary safety information rather than omitting it to simplify a drawing.

### File Sizes and Replacement

* The [image-size action](.github/actions/image-size-check/action.yml) limits changed PNG, JPG, JPEG, and SVG files to 2 MiB and GIFs to 10 MiB.
* Optimize without making text unreadable.
* These are byte-size checks, not screenshot-dimension requirements.
* When replacing an asset, check all references, especially in shared directories.
* Before removing an apparently unused asset, check dynamically loaded references and retention files.

## Callouts and Components

### Choosing an Alert

* Use MDX Alerts for new callouts.
* Choose a type appropriate to the message rather than using a warning merely for emphasis.
* Keep a callout focused; ordinary procedural content belongs in the main text.

| Type | Opening Label | Intended Use |
| --- | --- | --- |
| `info` | **Note:** | Helpful context |
| `success` | **Tip:** | Optional advice |
| `note` | **Important:** | Information necessary to complete the task |
| `warning` | **Warning:** | A risk or precaution |
| `danger` | **Danger:** | A serious hazard needing immediate attention |

### Required Spacing

* Put the opening and closing tags on their own lines.
* Include a blank line after the opening tag and before the closing tag.
* This is necessary for safe Markdown parsing and is checked by the [Alert validator](scripts/validation/alert_tags/README.md).

```markdown
<Alert type="info">

**Note:** Use a USB data cable, not a charge-only cable.

</Alert>
```

* The type/label convention is editorial guidance; the spacing checker does not establish technical truth or choose the correct severity for the author.

### Indentation and Escaping

* When an Alert belongs to a list item, indent its tags and body consistently with that item.
* Keep the blank lines.
* Put code and angle-bracket placeholders in backticks or a fenced block instead of leaving them to be interpreted as JSX.

### Legacy Notes

* Older articles use triple-asterisk callouts such as `***Note: Use a USB data cable.***`.
* Prefer MDX Alerts for new or substantially revised callouts.
* Existing legacy syntax is not an instruction to convert every note during an unrelated edit.
* When converting, preserve the meaning and severity, not just the visual emphasis.

### HTML and Other Components

* The base Markdownlint HTML allowlist contains `Alert`, `sup`, `sub`, and `br`.
* Check a section's local configuration before using other elements.
* An allowlist entry is not proof that a new component exists in the renderer.
* GitHub callouts such as `> [!NOTE]` and components copied from another documentation system are not substitutes for the site's supported MDX syntax.

## Moving and Maintaining Content

### Incoming and Outgoing Links

* Before moving an article, determine whether its published route changes.
* Search the entire content tree for the old route, filename, and related anchors, not only the source directory.
* Check metadata and navigation references as well as inline Markdown links.
* Update incoming links to the new route and recalculate outgoing URL-relative links from the new source route.
* Move article-local assets with the article and check their references.
* Do not assume moving a file updates links elsewhere automatically.

### Redirects and Public URLs

* Updating repository links does not preserve external bookmarks.
* Confirm the site's redirect mechanism and ownership with a maintainer before changing a published URL.
* The content link validator neither creates redirects nor proves that an old public URL still works.

### Shared Content and Symlinks

* Inspect whether an article is a symlink or is referenced through one before editing or moving it.
* Modify the shared source deliberately; do not replace a symlink with a duplicate article.
* Create links relative to the directory containing the symlink and verify that they resolve.

For a directory symlink on Unix, from the destination directory:

```bash
ln -s ../../../../../tutorials/generic/basic-servo-control basic-servo-control
```

* Adjust the target to the real directory depth.
* On Windows, a directory link uses `mklink /D` and may require administrator privileges or Developer Mode.
* Verify Git's symlink handling on that machine before committing.
* Python validators do not necessarily traverse directory symlinks, so check the rendered inclusion separately.

### Generated Content

* Do not hand-edit generated regions, including Bricks and Examples tables delimited by maintenance markers.
* Use the [maintenance scripts](scripts/maintenance/) and the relevant section's release workflow.
* Preserve frontmatter when replacing a generated article body.

### Maintenance Scope

* Check assets, metadata, navigation, anchors, and public URLs together.
* Keep unrelated legacy cleanup out of the move.
* A file deletion shown in a diff is not proof that its replacement was added; review new and untracked files as well.

## Validation and Preview

### Markdown Validation

From the repository root, run the wrapper rather than bare `npx markdownlint-cli`:

```bash
python3 scripts/validation/markdownlint/markdownlint.py CONTRIBUTING.md
python3 scripts/validation/markdownlint/markdownlint.py content/software/app-lab
```

* The wrapper discovers the base and nearest local configurations, loads custom rules, honors ignore files, and checks its own rules documentation for consistency.
* Bare Markdownlint can report a different rule set.
* The wrapper uses `npx`; have `markdownlint-cli` available locally or be prepared for its dependency resolution.
* Confirm the reported file count: zero checked files is not a successful inspection of your changes.

### Content Validation Commands

* The Python tools accept a file or directory.
* Replace `content` with the changed area for a focused check; after a move, include referring pages outside that area or check all content.

```bash
python3 scripts/validation/alert_tags/alert_tags.py validate content
python3 scripts/validation/relative_links/relative_links.py validate content
python3 scripts/validation/image_links/image_links.py validate content
```

| Tool | Checks and Important Boundaries |
| --- | --- |
| [Markdownlint](scripts/validation/markdownlint/README.md) | Markdown formatting with inherited configuration and custom heading-depth rule |
| [Alert validator](scripts/validation/alert_tags/README.md) | Blank-line spacing and indentation around Alerts |
| [Link validator](scripts/validation/relative_links/README.md) | Indexed article routes and heading anchors; skips external URLs and known asset extensions |
| [Image validator](scripts/validation/image_links/README.md) | Image/asset references; separate commands investigate unlinked assets |
| [Legacy content linter](scripts/validation/validate.js) | Selected hardware tutorial and datasheet metadata and content rules |

### Frontmatter Validation

The legacy content linter has its own configuration and exclusions. Run its wrapper from `scripts/validation`, with the hardware path relative to that directory:

```bash
./content-lint.sh -p '../../content/hardware/'
```

* The shell wrapper can install its local dependencies if missing.
* Review [its configuration](scripts/validation/config/) and schemas when diagnosing a metadata error.
* It does not provide a universal product/software frontmatter schema.
* `npm test` at the root is a placeholder, not a substitute for these checks.

### Spelling

* English content uses codespell in CI with a repository word list and exclusions.
* Localized datasheets use a separate cspell job for configured languages.
* Follow the exact commands and dependency versions in the [workflow](.github/workflows/workflow-validate.yaml).
* Do not run an English spell-check fix across all translations.
* Add a dictionary exception only for a real term, not to silence an ordinary typo.

### Ignore Files and Local Overrides

* The Python tools discover `.lintignore` and legacy `.linterignore` files up the directory tree.
* Tool-specific files include `.markdownlintignore`, `.alertlintignore`, `.linklintignore`, and `.imagelintignore`.
* Asset retention files include `.assetsignore` and `.keepassets`.
* The legacy content linter uses its own configuration rather than the same universal mechanism.
* CI targets `content`, but substantial legacy areas and some file types are excluded.
* The base Markdownlint configuration lives at [content/.markdownlint.yaml](content/.markdownlint.yaml).
* Local rules can override it.
* An excluded file can still need editorial correction; do not add ignore entries merely to obtain a green check.

### Link-Checker Limitations

* An ignored target may be missing from the route index even when its source exists.
* The index also has limitations around directory symlinks, colliding routes, and specialized page types.
* The checker uses inline-link matching, not a full renderer: metadata URLs, component attributes, and reference-style links require separate inspection.
* Verify unusual anchors in the preview.
* When a link fails, inspect the source route, target route, ignore rules, and actual public page before changing it.
* Do not replace a valid internal link with an absolute URL just to bypass a check.

### Automatic Fixes

* Use `--fix` for the Markdown wrapper and `fix` for the Alert or link tools only on the intended files.
* Review the diff afterward.
* Link normalization does not prove that the chosen destination is correct.
* Asset-removal commands are destructive: inspect unlinked-asset reports and shared references before deleting anything.

### Preview and Review Checklist

A pull request with the `preview` label receives a preview as described in [PR #1931](https://github.com/arduino/docs-content/pull/1931).

* GitHub's Markdown rendering is not the production renderer.
* Check headings, callouts, captions, code, tables, links, and narrow screens in the site preview.
* Theme installation and local rendering depend on the separate site package; do not assume this content repository supplies an `npm run serve` command.
* Before requesting review, verify the changed content, relevant referring pages, and newly added files.
* Report commands run, remaining warnings, and hardware/rendering checks you could not perform.
* A lint pass alone does not verify technical accuracy or hardware behavior.

## Licensing and Attribution

* Documentation contributions use [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
* Code examples use the [public-domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
* Attribute external material and verify its license before including text, code, diagrams, or screenshots.
* Preserve existing author credits unless the change intentionally corrects attribution.
