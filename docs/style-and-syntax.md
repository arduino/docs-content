# Style, Markdown, and MDX Syntax

This reference defines editorial voice, formatting conventions, media standards, and Markdown/MDX syntax rules for `arduino/docs-content`. For contribution workflow and validation commands, see [CONTRIBUTING.md](../CONTRIBUTING.md). For directory structure, `content/order.json`, frontmatter, routing, and localization, see [Content Structure, Metadata, and Routing](content-structure.md).

## Writing Style

### Audience and Assumptions

* Write for the reader who needs to complete the documented task.
* State required hardware, software versions, prior setup, and background knowledge up front.
* Define unfamiliar concepts on first use or link to an existing explanation.
* Focus each tutorial on teaching one outcome well.

### Voice and Point of View

* Use active voice and address the reader as "you" in instructions.
* Prefer direct imperatives for procedural steps.
* Describe what hardware or software does in present tense.
* Reserve future tense for genuinely future events rather than narrating every step.

| Use | Avoid |
| --- | --- |
| Connect the board to your computer. | The board should be connected to the computer. |
| Select **Upload**. | Now we are going to select Upload. |
| The LED turns on when the input is high. | You will see that the LED will turn on. |

### Concise and Inclusive Language

* Use short sentences and concrete verbs.
* Omit filler words such as "simply," "just," "obviously," "easy," and "leverage."
* Describe the action instead of judging how easy or hard it is.
* Avoid idioms, unexplained jargon, and assumptions about the reader's background or abilities.

### English Spelling

* Use American English in new English prose: "color," "initialize," and "behavior."
* Preserve exact spelling in UI labels, quotations, filenames, and code identifiers.
* Never normalize or overwrite localized datasheets or translated tutorials with English spelling corrections.

### Terminology and Product Names

* Expand unfamiliar acronyms on first use and apply the same term consistently throughout a page.
* Preserve official product and technology capitalization: Arduino, MicroPython, OpenMV, Wi-Fi, Bluetooth®, I2C, SPI.
* Use "your board" when instructions apply identically to every board covered by the article (check section-specific rules such as the [App Lab guide](../content/software/app-lab/README.md)).
* Name the exact board whenever pinouts, voltage limits, jumper positions, or compatibility differ.
* Do not imply broader board support than has been verified.

### Versions and Technical Claims

* Prefer explicit version numbers or dates over relative phrases such as "recently," "new," or "the latest."
* State preview or beta limitations directly in prose.
* Verify electrical ratings, pin assignments, CLI flags, and code behavior against authoritative sources.
* For sketch-commenting and beginner pedagogy conventions, also consult the [Arduino writing style guide](../content/learn/08.contributions/00.arduino-writing-style-guide/arduino-writing-style-guide.md).

## Titles and Headings

### Capitalization

* Use Title Case for page `title` frontmatter and Markdown headings.
* Capitalize the first and last words and all principal words; keep short articles, coordinating conjunctions, and short prepositions lowercase unless first or last (for example, `Connect to a Wireless Network` and `Read Data from the Sensor`).
* Preserve exact casing for product names, code identifiers, CLI commands, and literal UI labels.

### Hierarchy

* Published article titles come from `title` in YAML frontmatter; start article body sections at H2 (`##`) rather than adding a duplicate H1. Repository documentation files (such as `README.md`, `CONTRIBUTING.md`, and files in `docs/`) start with a single H1.
* Increment heading levels one step at a time (`##`, `###`, `####`).
* Do not use H5 (`#####`) or H6 (`######`); custom Markdownlint rule `no-h5` rejects them. Restructure deep topics into shallower sections, lists, or tables rather than using bold paragraphs as fake headings.

### Punctuation and Anchors

* Do not end headings with trailing punctuation (`.,;:!`), except question marks (`?`).
* Keep sibling headings unique under the same parent section (`MD024` with `siblings_only: true`).
* Renaming a heading changes its URL fragment (`#heading-slug`); search `content/` for incoming anchor links before renaming established headings.

## Text Formatting

### UI Labels and Menu Sequences

* Bold visible UI controls and preserve their exact displayed capitalization: select **Run**, then **Stop**.
* Separate menu paths with `>`: **Tools** > **Board** > **Arduino UNO R4 Boards**.
* Do not wrap GUI button labels in inline code backticks.

### Inline Code and Keyboard Shortcuts

* Wrap filenames, paths, CLI commands, functions, variables, pin constants, and literal parameter values in backticks: `sketch.ino`, `digitalRead()`, `LED_BUILTIN`, `--port`.
* Format keyboard shortcuts consistently, such as **Ctrl+C** or **Command+C**, noting OS differences when relevant.

### Emphasis and Quotations

* Use bold sparingly to highlight key terms, and never use bold or italic lines as a substitute for section headings.
* Use Markdown blockquotes (`>`) only for actual quotations with attribution; use `<Alert>` components for notes, tips, and warnings.

### Numbers, Units, and Trademarks

* Use numerals with a space before the unit symbol: `3.3 V`, `20 mA`, `115200 bps`, `64 kB`.
* Preserve unit case (`MB` vs `Mb`, `kHz` vs `MHz`) and distinguish absolute maximum ratings from nominal operating values.
* Follow [Arduino's trademark guidelines](https://www.arduino.cc/en/trademark) and third-party trademark rules; never add trademark symbols inside code identifiers.

## Procedures and Lists

### Ordered Procedures

* Use Markdown numbered lists (`1.`, `2.`, `3.`) for sequential steps rather than manually bolded numbers.
* Put one primary action in each step and state prerequisites before the step that needs them.
* Describe the expected visible or measurable outcome after steps that change hardware or application state:

```markdown
1. Connect the board to your computer with a USB-C data cable.
2. Select your board and serial port in the Arduino IDE toolbar.
3. Click **Upload** and wait for the **Done uploading** notification.
```

### Unordered Lists and Nesting

* Use unordered lists (`-` or `*`) when item order does not matter.
* Keep list items grammatically parallel; punctuate complete sentences with periods, and omit trailing periods on short fragments.
* Indent continuation paragraphs, code blocks, and nested lists consistently so they attach to the intended list item (2 spaces for nested unordered lists under `MD007`).
* Keep list nesting shallow; promote complex multi-paragraph items to subsections.

### Troubleshooting

* Structure troubleshooting entries around three parts: **symptom**, **how to check the cause**, and **corrective action**.
* Warn before steps that erase flash memory, reset configurations, or risk hardware damage.
* Distinguish software/driver issues from wiring, power-supply, and charge-only cable issues.

## Code, Commands, and Tables

### Fenced Code Blocks

* Always specify a language identifier on fenced code blocks (`MD040`), such as `arduino`, `cpp`, `c`, `python`, `bash`, `json`, `yaml`, `javascript`, `typescript`, `html`, `css`, or `diff`.
* Use `text` for plain console output, serial logs, or directory trees.
* Surround top-level fenced code blocks with blank lines and use spaces rather than hard tabs (`MD010` enforces `code_blocks: true`).

### Commands and Output

* State where a command runs (host terminal, board shell, container, working directory) before the snippet.
* Separate runnable commands from example output into distinct code blocks so readers can use the copy button cleanly.
* Explain destructive commands (flashing, partitioning, removing files) before asking readers to run them.

### Placeholders and Angle-Bracket Escaping

* Wrap user-replaceable placeholders such as `<port>`, `<board-ip>`, or `<sketch-name>` in backticks whenever they appear in prose or table cells. Bare `<placeholder>` text outside code spans is parsed as an HTML/JSX tag by MDX and fails compilation.
* Explain every placeholder right before or after the snippet, and never commit real API keys, tokens, Wi-Fi passwords, or personal identifiers.

### Working Examples

* Keep example sketches and scripts focused on the concept taught by the page.
* Include required `#include` / `import` statements, pin definitions, and library names; clearly label partial excerpts when omitting boilerplate.
* Test code on target hardware whenever possible and note any untested configurations in your PR description.

### Tables

* Include a header row and delimiter row with spaces around pipes (`| --- | --- |`).
* Escape literal pipe characters inside table cells as `\|`.
* Keep cell text concise; move multi-sentence procedures or explanations into prose or lists outside the table.
* Never hand-edit tables bounded by `<!-- ... table start -->` maintenance comments; see [Generated Content](content-structure.md#generated-content).

```markdown
| Parameter | Description |
| --- | --- |
| `pin` | GPIO pin number to read |
| `mode` | `INPUT`, `INPUT_PULLUP`, or `OUTPUT` |
```

## Images, Diagrams, and Assets

### Asset Locations and Filenames

* Store article images in an `assets/` folder inside the article directory and reference them with relative paths (`assets/serial-monitor.png`).
* Exception: App Lab uses a shared section-level `content/software/app-lab/assets/` folder; follow local section READMEs where present.
* Use lowercase, descriptive, hyphenated filenames (`uno-q-pinout-header.png`) and match filename case exactly in Markdown links (`image_links.py` checks case sensitivity).

### Captions and Alternative Text

On `docs.arduino.cc`, the alt text inside `![Alt text](assets/example.png)` is also rendered as a **visible figure caption** beneath the image:

```markdown
![Serial Monitor displaying temperature readings every second](assets/temperature-output.png)
```

* Write concise, descriptive text that works both as accessible alt text and as a figure caption. Do not use bare filenames (`image1.png`) or directional filler (`see above`).
* Never rely on an image alone to convey required commands, pin numbers, or safety warnings; state critical details in prose as well.

### Framing, Annotations, and Hygiene

* Crop screenshots to the relevant window or panel while preserving enough surrounding UI for orientation; readability matters rather than a fixed pixel resolution.
* Keep callout annotations legible in both light and dark page themes and do not rely on color alone to distinguish items.
* Strip personal usernames, internal URLs, private project names, tokens, and unrelated OS notifications before capturing screenshots.
* Use breadboard/wiring illustrations when helping readers identify physical connections, and schematic diagrams when circuit topology matters; verify that pin labels and voltages match the prose and code.

### File Size Limits and Asset Cleanup

* Changed image files in pull requests are checked by [`.github/actions/image-size-check`](../.github/actions/image-size-check/action.yml): **2 MiB** maximum for `.png`, `.jpg`, `.jpeg`, and `.svg`, and **10 MiB** maximum for `.gif`. Deployment builds also warn on `.pdf`, `.zip`, and `.mp4` files over **10 MiB**.
* Before replacing or deleting an existing asset, search `content/` for shared references and check `.assetsignore` / `.keepassets` retention rules via [`image_links.py`](../scripts/validation/image_links/README.md).

## Callouts, MDX, and HTML Rules

### MDX `<Alert>` Callouts

Use MDX `<Alert>` blocks for callouts in new and revised articles. Pick the severity that matches the message rather than using `warning` or `danger` for visual emphasis:

| `type` | Opening Label | Intended Use |
| --- | --- | --- |
| `info` | `**Note:**` | Helpful background context |
| `success` | `**Tip:**` | Optional shortcut or best practice |
| `note` | `**Important:**` | Prerequisite or detail required for success |
| `warning` | `**Warning:**` | Potential data loss, configuration pitfall, or equipment risk |
| `danger` | `**Danger:**` | Electrical, thermal, or physical hazard requiring immediate caution |

#### Required Spacing and Indentation

Put `<Alert>` and `</Alert>` on their own lines with a **blank line inside both tags** (enforced by [`alert_tags.py`](../scripts/validation/alert_tags/README.md)):

```markdown
<Alert type="info">

**Note:** Use a USB data cable, not a charge-only cable.

</Alert>
```

* When nesting an `<Alert>` inside a list item, indent `<Alert>`, its body lines, and `</Alert>` to match the list item's content column while keeping the inner blank lines.
* Legacy articles contain triple-asterisk callouts (`***Note: ...***`). Use `<Alert>` in new or substantially revised sections, but do not mass-convert legacy notes in unrelated typo fixes.
* GitHub-flavored blockquote alerts (`> [!NOTE]`) are not supported in `content/` articles; use `<Alert>` instead.

### MDX Compilation Rules (`mdx-check.js`)

Every Markdown page in `content/`—including legacy directories listed in `.lintignore`—is compiled by Gatsby using `@mdx-js/mdx` v1 and Babel. CI runs the identical compiler via [`scripts/validation/mdx/mdx-check.js`](../scripts/validation/mdx/README.md). Pages that violate JSX/MDX parsing rules break the site build and fail `MDX Check`:

* **Self-close all void HTML elements:** Write `<br/>`, `<hr/>`, and `<img .../>`—never unclosed `<br>` or `<img>`. In MDX, `<br>` opens an unclosed JSX tag and fails compilation with `Unterminated JSX contents`.
* **Close and nest HTML tags strictly in order:** Every non-void tag (`<sub>...</sub>`, `<sup>...</sup>`) must close in matching order on the same block level.
* **Escape `{ }` and `< >` in prose:** Outside backticks and fenced code blocks, `{expression}` is evaluated as JavaScript by MDX and `<word>` is parsed as a JSX tag. Wrap placeholders, C++/Python generics, and JSON snippets in backticks (`` `<port>` ``, `` `{key: value}` ``).
* **No HTML comments inside HTML blocks:** Use MDX comments or avoid placing `<!-- ... -->` inside raw HTML elements.

### Inline HTML Allowlist and Custom Components

* The baseline Markdownlint configuration ([`content/.markdownlint.yaml`](../content/.markdownlint.yaml), rule `MD033`) allows only `Alert`, `sup`, `sub`, and `br` (written as `<br/>` for MDX compatibility).
* The `docs.arduino.cc` MDX provider also registers `<CodeBlock url="https://github.com/..." className="language-..."/>` (for fetching public GitHub source files) and `<SketchIframe/>`, and product fragments such as `features.md` and `essentials.md` use product-specific components (excluded via `.markdownlintignore`).
* Before introducing `<CodeBlock>` or any other component in an article directory, verify both local `.markdownlint.yaml` `MD033` overrides and rendered behavior in a preview build.
