# Content Structure, Metadata, and Routing

This reference defines how files, directories, navigation sidebars, frontmatter, published routes, downloadable resources, and translations work in `arduino/docs-content`. For contribution workflow and local validation commands, see [CONTRIBUTING.md](../CONTRIBUTING.md). For editorial voice, Markdown formatting, images, and MDX rules, see [Style and Syntax](style-and-syntax.md).

## Directory Layout and Naming

### Naming Rules

* Use descriptive lowercase names with hyphens between words for new directories and files.
* Preserve exact case in references to existing files.
* Avoid spaces and underscores in new article directory names.
* Do not rename existing files or directories merely to match an example in this reference.

### Finding an Existing Article

Published URLs do not map directly to filesystem paths. Search frontmatter `title` and `description` as well as filenames, because hardware tutorials and other pages frequently use generic filenames such as `content.md`:

```bash
grep -rn "Multimeter Basics\|multimeter features" content/
```

Confirm the product and section before editing a search match.

### Hardware Directory Layout

Hardware products sit under unnumbered family and product-type directories:

```text
content/hardware/<family>/<product-type>/<product>/
  product.md
  features.md
  tech-specs.yml
  tech-specs.md
  overview.md               # Optional Overview tab (video + quickstart cards)
  cardList.md               # Optional resource card strip
  communityProjects.md      # Optional Project Hub showcase cards
  essentials.md             # Optional Essentials tab items
  compatibility.yml         # Optional hardware/software compatibility data
  image.svg                 # Product illustration
  certifications/           # Optional regulatory/compliance files
  downloads/                # Pinouts, schematics, CAD, power tree, block diagram
  datasheet/
    datasheet.md            # Or en-datasheet.md + <lang>-datasheet.md
  tutorials/
    <tutorial>/content.md   # Uncategorized tutorial
    <category>/             # Optional grouped tutorial category
      category.md
      <tutorial>/content.md
```

* An article may use `content.md` or a filename matching its directory, such as `blink/blink.md`. Follow neighboring maintained pages in that section.
* `product.md` is a hardware product page, not a generic replacement for category or software overview files.

### Overview Files and Fragments

* Family, category, and software overview files carry navigation metadata and, where applicable, introductory prose. Examples include `family.md`, `category.md`, `software.md`, and named section overviews such as `setup.md` in App Lab.
* Inspect the target section before adding an overview file.
* Included fragments such as `features.md` and `tech-specs.md` render inside a parent product page rather than as standalone articles.

## Sidebar Structure and Ordering

Sidebar and listing order across the site is computed at build time from two coexisting mechanisms: [`content/order.json`](../content/order.json) and numeric directory prefixes.

### Declarative Ordering with `content/order.json`

New and migrated sections define directory order in [`content/order.json`](../content/order.json) instead of renaming folders with numeric prefixes:

```json
{
  "hardware": {
    "ventuno": {
      "boards/ventuno-q/tutorials": {
        "first-steps": [
          "user-manual",
          "first-setup",
          "sbc-mode-setup"
        ],
        "guides": [
          "arduino-ide",
          "bridge"
        ]
      }
    },
    "mkr": {
      "boards": [
        "mkr-wifi-1010",
        "mkr-zero"
      ]
    }
  },
  "learn": {
    "starting-guide": [
      "whats-arduino",
      "getting-started-arduino",
      "cores"
    ]
  }
}
```

`content/order.json` follows two rules:

* **Keys containing `/` only navigate.** Top-level section keys (`"hardware"`, `"learn"`, `"software"`) and multi-segment keys (`"boards/ventuno-q/tutorials"`) traverse intermediate folders without ordering them. You only write out the levels whose children need ordering.
* **Single-name keys and array items assign order.** Both single-segment object keys (such as `"first-steps"` before `"guides"`) and string entries in an array (such as `"user-manual"` before `"first-setup"`) place sibling folders in top-to-bottom order.

Keep these constraints in mind when editing `content/order.json`:

* **Never sort JSON keys alphabetically.** Key order in `content/order.json` defines the rendered order on the site.
* **Match folder names without numeric prefixes.** Entries match directory slugs with any `01.` prefix stripped.
* **Check build warnings.** Non-existent folder paths, duplicate placements, non-string array entries, or entries pointing to a folder that still has a numeric prefix emit `[content order]` build warnings and are ignored.
* **Restart local `gatsby develop` after changes.** The site build caches `content/order.json` and directory listings at startup; restart the dev server after editing `order.json` or adding, renaming, or removing content folders.

### Numeric Prefixes and Coexistence

Unmigrated sections still order directories with numeric prefixes such as `01.` or `1.`. When both conventions appear in the same parent directory, the build sorts siblings in three bands:

1. **Numbered folders first**, in numeric order (`1.`, `2.`, or `01.`, `02.`). Numeric prefixes always win over `content/order.json` for a folder that still carries a prefix.
2. **Unnumbered folders listed in `content/order.json`**, in the order written in the file.
3. **Remaining unnumbered folders**, sorted alphabetically.

When maintaining navigation order:

* To migrate an ordered directory to `content/order.json`, strip the numeric prefixes from its child directories and list them in `content/order.json`. Removing numeric folder prefixes does not change published URLs because slug generation strips them automatically.
* Navigating *through* a still-numbered parent folder via a `/` key in `content/order.json` is valid and requires no rename of that parent.
* If you add an entry inside an unmigrated numbered group without migrating the group, continue its existing numbering style (`01.` with leading zeros when a group has ten or more items).
* Structural directories (`boards`, `tutorials`, `assets`, `downloads`) and product slugs (`uno-q`, `ventuno-q`) remain unnumbered.

### Grouped Hardware Tutorials

By default, a product's `tutorials/` directory renders as a single collapsible **Tutorials** group. Products with larger documentation sets (such as `ventuno-q` and `uno-q`) can organize tutorials into named category subdirectories:

```text
content/hardware/uno/boards/uno-q/tutorials/
  first-steps/
    category.md
    user-manual/content.md
    power-specifications/content.md
  robotics/
    category.md
    ros2-setup/content.md
```

* **Explicit `category.md` marker required:** A subdirectory under `tutorials/` only becomes a sidebar and product-page category if it contains a `category.md` file. Without `category.md`, the build does not treat a nested folder as a category.
* **Category display title:** Set the category heading in `category.md` frontmatter so acronyms and capitalization render accurately:

  ```yaml
  ---
  title: AI Workflows
  ---
  ```

* **Ordering categories and tutorials:** Order both the category folders and each category's tutorials in `content/order.json` (using an object whose keys are category slugs and whose values are arrays of tutorial slugs).
* **Published URLs stay flat:** Intermediate category folders under `tutorials/` are collapsed in routes. `tutorials/first-steps/user-manual/content.md` publishes at `/tutorials/uno-q/user-manual/`, and `category.md` itself does not generate a standalone tutorial page.

## Frontmatter and Product Page Files

Standalone pages start with YAML frontmatter between `---` delimiters:

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

Repository READMEs, files in `docs/`, and included fragments (`features.md`, `tech-specs.md`) do not use article frontmatter.

### Article and Tutorial Metadata

The [tutorial schema](../scripts/validation/rules/tutorial-metadata-schema.json) defines the fields below. CI enforces it on hardware tutorials via the legacy content linter. Use the common fields (`title`, `description`, `author`, `tags`) for new prose articles unless the section's existing pages specify otherwise.

| Field | Type | Required | Purpose |
| --- | --- | --- | --- |
| `title` | String | Yes | Page title in Title Case (maximum 60 characters for layout and SEO) |
| `description` | String | Yes | Concise summary of what the reader learns or accomplishes |
| `author` | String | Yes | Author or approved team attribution |
| `tags` | Array of strings | Yes | Topic tags following established repository terminology |
| `difficulty` | String | No | `beginner`, `intermediate`, or `advanced` |
| `hardware` | Array of strings | No | Hardware identifiers (for example `hardware/nano/boards/nano-esp32` or legacy equivalents) |
| `software` | Array of strings | No | Software identifiers (`ide-v1`, `ide-v2`, `web-editor`, `iot-cloud`, `plc-ide`, `app-lab`) |
| `compatible-products` | Array of strings | No | Verified compatible product identifiers |
| `libraries` | Array of objects | No | Library entries with `name` and `url` strings |
| `coverImage` | String | No | Cover image reference |
| `featuredImage` | String | No | Featured image reference |
| `hero_position` | Integer | No | Hero positioning value; preserve section usage |
| `overwriteSidebar` | String | No | Shorter label displayed in the navigation sidebar instead of `title` |
| `beta` | Boolean | No | Marks beta content; also state beta limitations in prose |
| `source` | String | No | Upstream source reference |
| `primary_button_title` | String | No | Maximum 15 characters |
| `secondary_button_title` | String | No | Maximum 20 characters |

The tutorial schema rejects undeclared fields (`additionalProperties: false`). In software and overview sections not covered by this schema, frontmatter fields such as `hidden: true` or `hide_category: true` are also supported by the Gatsby schema; copy maintained pages in the same section rather than guessing.

### Datasheet Metadata

The [datasheet schema](../scripts/validation/rules/datasheet-metadata-schema.json) is separate from the tutorial schema and also rejects undeclared fields.

| Field | Type | Required | Purpose |
| --- | --- | --- | --- |
| `title` | String | Yes | Datasheet title in Title Case (maximum 60 characters) |
| `identifier` | String | Yes | Approved SKU/document identifier used for `/resources/datasheets/<identifier>-datasheet.pdf` |
| `type` | String | Yes | `maker`, `edu`, `pro`, or `limited-edition` |
| `author` | String | No | Author attribution |
| `hardwareRevision` | String | No | Hardware revision |
| `revision` | String | No | Document revision |
| `variant` | String | No | Product variant |
| `isPreviousRevision` | Boolean | No | Marks superseded hardware/datasheet revisions |
| `isDraft` | Boolean | No | Draft status |

Preserve `identifier` and revision fields unless your change intentionally updates them. Consult [datasheet rendering tooling](../scripts/datasheet-rendering/) before altering datasheet structure.

### Product Metadata and Companion Files

Hardware product pages combine [`product.md`](../content/hardware/ventuno/boards/ventuno-q/product.md) with optional companion files in the same product folder. Never invent SKUs, electrical ratings, certifications, release dates, or compatibility claims.

| Field in `product.md` | Type | Required | Purpose |
| --- | --- | --- | --- |
| `title` | String | Yes | Official product name |
| `url_shop` | String | No | Arduino Store URL |
| `primary_button_url`, `secondary_button_url` | String | No | Call-to-action button destination |
| `primary_button_title`, `secondary_button_title` | String | No | Visible button label |
| `forumCategorySlug` | String | No | Official Arduino Forum category path |
| `sku` | Array of strings | No | Approved product SKU codes |
| `useCases` | Array of strings | No | Hardware catalog filter values (`prototyping`, `industrial-automation`, `robotics`, `kits`, `edge-ai`, `iot-wireless`, `education`, `accessories`) |
| `releaseDate` | Date (`YYYY-MM-DD`) | No | Verified release date (drives **Recents** sorting on `/hardware`) |
| `isNew` | Boolean | No | Displays a new-product badge |
| `hidden` | Boolean | No | Excludes the product from catalog and sidebar listings |

#### Hardware Catalog Relevance (`content/hardware/relevance.md`)

Default **Relevance** ordering on `/hardware` is controlled centrally by [`content/hardware/relevance.md`](../content/hardware/relevance.md) via its `relevanceProducts` frontmatter list (matched case- and punctuation-insensitively against product folder slugs or titles). Products omitted from `relevanceProducts` follow in reverse chronological order by `releaseDate`.

#### Optional Product Companion Files

| File | Effect on Product Page |
| --- | --- |
| `overview.md` | Prepends an **Overview** tab with an embedded video (`url`) and quickstart cards (`info` array of `{ icon, title, description, link }`). |
| `cardList.md` | Renders a resource card section (`title` plus `cards` array of `{ icon, title, description, link, external }`). |
| `communityProjects.md` | Renders featured Project Hub cards under the **Tutorials** tab (`description` plus `communityProjects` array of `{ title, description, label, value, url, image }`). |
| `features.md` / `tech-specs.yml` / `tech-specs.md` / `essentials.md` / `compatibility.yml` | Populate the **Features**, **Tech Specs**, and **Essentials** tabs and compatibility badges. |

## Links, Routing, and Downloadable Resources

### Source Paths Versus Published Routes

A site URL is not a filesystem path: `/content/...` is never a published prefix, and a leading `/` resolves from the site root (`https://docs.arduino.cc/`).

| Source Path | Published Route |
| --- | --- |
| `content/hardware/uno/boards/uno-q/product.md` | `/hardware/uno-q/` |
| `content/hardware/uno/boards/uno-q/tutorials/first-steps/user-manual/content.md` | `/tutorials/uno-q/user-manual/` |
| `content/software/app-lab/1.setup/1.overview/overview.md` | `/software/app-lab/setup/overview/` |
| `content/learn/04.electronics/01.multimeter-basics/multimeter-basics.md` | `/learn/electronics/multimeter-basics/` |

* Slug generation strips numeric directory prefixes (`01.`) and drops the Markdown filename (`content.md`, `overview.md`).
* Hardware tutorial routes always use `/tutorials/<product-slug>/<tutorial-slug>/`, collapsing any intermediate category directory.
* Do not place multiple standalone English articles in the same leaf directory; their routes will collide (translated tutorials are the exception; see [Localization](#localization)).

### Internal Article Links

Both root-relative and URL-relative links are valid for internal pages:

* **Root-relative links** start from `/` and work identically regardless of where the linking page lives or whether it is symlinked into multiple products:

  ```markdown
  [UNO Q](/hardware/uno-q/)
  [UNO Q User Manual](/tutorials/uno-q/user-manual/)
  ```

* **URL-relative links** resolve against the **published URL** of the current page, not its filesystem folder. From `/software/app-lab/setup/overview/`, `[Linux Setup](../linux/)` resolves to `/software/app-lab/setup/linux/`. Preserve a section's established style, and prefer root-relative links in shared (symlinked) tutorials.

Formatting rules for internal links:

* Omit `.md` extensions and numeric directory prefixes (`01.`).
* Prefer a trailing slash before any query or `#anchor` fragment (`/hardware/uno-q/#features`), though the validator accepts routes with or without a trailing slash.
* Derive heading anchors by lowercasing heading text, replacing spaces with hyphens, and stripping punctuation (`#programming-the-board`). Verify duplicate or symbol-heavy headings in a preview build.
* Use descriptive link text rather than generic phrases like "click here."
* Prefer root-relative `/...` paths over full `https://docs.arduino.cc/...` URLs so the default CI link check validates them offline (or pass `--absolute` to [`relative_links.py`](../scripts/validation/relative_links/README.md) to check full `docs.arduino.cc` URLs as well).

### External Site Sections

Several routes on `docs.arduino.cc` are built from other repositories or React page templates rather than Markdown in `content/`. These prefixes and exact pages are listed in [`scripts/validation/relative_links/external-sections.txt`](../scripts/validation/relative_links/external-sections.txt) (`/libraries`, `/language-reference`, `/arduino-cli`, `/cloud-api`, `/software`, `/software/ide`, `/tutorials`, `/certifications`) and are skipped rather than flagged as broken by `relative_links.py`.

### Downloadable Product Resources

Files placed in a product's `downloads/` directory populate the **Downloadable resources** panel when their filenames end with a recognized suffix (`[SKU]-` prefix recommended):

| Filename Suffix in `downloads/` | Resource Label | Published `/resources/` Copy |
| --- | --- | --- |
| `full-pinout.pdf` | Pinout (PDF) | `/resources/pinouts/<filename>` |
| `pinout.png` | Interactive/Simplified Pinout | `/resources/pinouts/<filename>` |
| `schematics.pdf` | Schematics | `/resources/schematics/<filename>` |
| `step.zip` | STEP Files | `/resources/models/<filename>` |
| `cad-files.zip` (or `eagle-files.zip`) | CAD Files | Served via Gatsby static asset URL |
| `altium-files.zip` | Altium Files | Served via Gatsby static asset URL |
| `fritzing.fzpz` | Fritzing Files | Served via Gatsby static asset URL |
| `dfx.zip` / `stl.zip` | DFX / STL Files | Served via Gatsby static asset URL |
| `pinout-table.pdf` / `software-pinout-mapping.pdf` | Pinout Table / Software Mapping | Served via Gatsby static asset URL |
| `mechanical-drawing.pdf` | Mechanical Drawing | Served via Gatsby static asset URL |
| `power-tree.pdf` | Power Tree | Served via Gatsby static asset URL |
| `block-diagram.pdf` | Block Diagram | Served via Gatsby static asset URL |

Datasheet PDFs are rendered at build time from `datasheet/[<lang>-]datasheet.md` to `/resources/datasheets/<identifier>[-<lang>]-datasheet.pdf`. Keep file extensions intact whenever linking to assets or downloads, and state the file format in the link text (for example `[ABX00181 schematics (PDF)](/resources/schematics/ABX00181-schematics.pdf)`). `relative_links.py` strictly validates links into `/resources/pinouts/`, `/resources/schematics/`, and `/resources/models/` against `downloads/` in this repository; `/resources/datasheets/` also hosts external IC datasheets, so unmatched datasheet URLs are skipped rather than flagged as broken.

#### Multiple Schematics and Pinouts

When a product's `downloads/` directory contains two or more `*-schematics.pdf` or `*-full-pinout.pdf` files (for example across SKU variants or hardware revisions), **Downloadable resources** automatically groups them into a dropdown. Entry labels are derived from `[SKU]-[version]-schematics.pdf` / `[SKU]-[version]-full-pinout.pdf`, where versions match `v1`, `v1.2`, or `rev3`:

| Filename | Dropdown Label |
| --- | --- |
| `ABX00023-v1.2-schematics.pdf` | `ABX00023 - v1.2` |
| `ABX00023-schematics.pdf` | `ABX00023` |
| `v1.2-schematics.pdf` | `v1.2` |

### Repository Documentation Links

Repository documentation read on GitHub (`README.md`, `CONTRIBUTING.md`, `docs/*.md`, `contribution-templates/README.md`, and `scripts/**/README.md`) uses real filesystem-relative paths including the `.md` extension, such as `[CONTRIBUTING.md](../CONTRIBUTING.md)`.

## Localization

Supported non-English language codes (defined in `docs.arduino.cc` `src/utils/languages.json`) are `zh`, `pt`, `de`, `fr`, `hi`, `es`, `it`, `ja`, and `nl`.

### Translated Tutorials

* Place a translated tutorial in the same directory as its English source file using `<name>-<lang>.md` (for example `content-es.md` next to `content.md` or `content-en.md`).
* Never keep both `<name>.md` and `<name>-en.md` in the same directory; both represent the English page and collide at the same slug.
* Without a sibling English `<name>.md` or `<name>-en.md`, a file ending in `-it.md` (or another code) is treated as a standalone English page rather than a translation.
* Translated tutorials publish at `/<lang>/tutorials/...`, inherit the English page's sidebar and product context, expose a language selector on the page, and are automatically skipped by the English `codespell` check via [`scripts/validation/translations.js`](../scripts/validation/translations.js).

### Localized Datasheets

* Place localized datasheets in `<product>/datasheet/<lang>-datasheet.md` alongside `datasheet.md` or `en-datasheet.md`, preserving the exact same `identifier` in frontmatter.
* Rendering uses the per-language configuration in `scripts/datasheet-rendering/config.<lang>.json` to produce `/resources/datasheets/<identifier>-<lang>-datasheet.pdf`. When more than one language exists, the product page's **Datasheet** download button becomes a language dropdown.
* Localized datasheets are skipped by English `codespell` and checked by language-specific `cspell` dictionaries in CI (`de`, `es`, `fr`, `it`, `nl`, `pt`).
* Do not normalize or translate localized files during an English-only edit.

## Shared Content, Moving Pages, and Generated Regions

### Shared Tutorials and Symlinks

Tutorials applicable to multiple boards live once (commonly under `content/tutorials/` or `content/built-in-examples/` or a primary software/hardware directory) and are included under other products via directory symlinks.

On Unix, from the destination `tutorials/` directory:

```bash
ln -s ../../../../../tutorials/generic/basic-servo-control basic-servo-control
```

On Windows (requires Developer Mode or an elevated prompt):

```cmd
mklink /D basic-servo-control "..\..\..\..\..\tutorials\generic\basic-servo-control"
```

* Inspect whether a tutorial is a symlink or symlink target before editing or moving it; edits to the target affect every product sharing it.
* Do not replace a symlink with a copy-pasted duplicate article.
* [`relative_links.py`](../scripts/validation/relative_links/README.md) follows symlinked tutorial directories and validates every link from **each URL** where the shared tutorial is published, reporting issues once under the source file. Use root-relative links (`/software/plc-ide/`) rather than `../` links in shared tutorials whenever `../` would resolve differently across products.

### Moving or Renaming Content

* Before moving a directory, check whether its published route will change (reordering via `content/order.json` or stripping numeric prefixes preserves the route; renaming a slug or moving between sections changes it).
* Search the entire `content/` tree for incoming links, `overview.md` / `cardList.md` / `product.md` button URLs, symlinks, and `content/order.json` entries referencing the old path.
* Move article-local `assets/` alongside the article and recalculate any outgoing URL-relative links from the new route.
* Changing internal repository links does **not** create HTTP redirects for external bookmarks. Confirm redirect handling with a maintainer before changing an established public URL.

### Generated Content

Do not hand-edit regions bounded by HTML maintenance markers (`<!-- app-bricks-py table start -->`, `<!-- app-bricks-examples table start -->`, `<!-- app-lab-models table start -->`, `<!-- arduino-app-cli commands start -->`). Regenerate them with the Python scripts documented in [`scripts/maintenance/README.md`](../scripts/maintenance/README.md), preserving surrounding frontmatter and prose.
