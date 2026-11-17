# Contribution Templates

Use these templates to start an article. Read [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution workflow and validation, and the references in [`docs/`](../docs/content-structure.md) for structure, metadata, routing, style, and MDX syntax. Template instructions are scaffolding: replace them before submitting content.

## Choose a Template

| Template | Use | Suggested Structure |
| --- | --- | --- |
| [Tutorial](tutorial-template/tutorial-template.md) | Teach a concrete outcome step by step | Introduction, goals, prerequisites, circuit, feature explanation, programming, testing, troubleshooting, conclusion |
| [How-To](how-to-template/how-to-template.md) | Solve a focused task | Introduction, prerequisites, circuit or schematic when needed, code, related reading |
| [Article](article-template/article-template.md) | Explain a concept | Introduction, topic-specific sections, conclusion, references |

Generic project showcases belong on [Project Hub](https://projecthub.arduino.cc/), not here.

## Use a Template

1. Read the [content-type guidance](../CONTRIBUTING.md#content-types) and choose a destination.
2. Copy the template into the appropriate article directory.
3. Replace example metadata with verified information. Retain required fields, including `tags` for hardware tutorials; remove unused optional fields.
4. Replace instructional text, example links, and empty image destinations. Use meaningful headings suited to the article.
5. Run the [relevant validation](../CONTRIBUTING.md#validation-and-preview), inspect the site preview, and submit the change for review.

## Authoring Reference

| Topic | Reference |
| --- | --- |
| Source paths, `content/order.json`, and grouped tutorials | [Sidebar Structure and Ordering](../docs/content-structure.md#sidebar-structure-and-ordering) |
| Required fields, companion files, and content-type schemas | [Frontmatter and Product Page Files](../docs/content-structure.md#frontmatter-and-product-page-files) |
| Article URLs, `/resources/` downloads, and repository links | [Links, Routing, and Downloadable Resources](../docs/content-structure.md#links-routing-and-downloadable-resources) |
| Translated tutorials and localized datasheets | [Localization](../docs/content-structure.md#localization) |
| American English, voice, and terminology | [Writing Style](../docs/style-and-syntax.md#writing-style) |
| Title Case and H2–H4 heading depth | [Titles and Headings](../docs/style-and-syntax.md#titles-and-headings) |
| UI labels, units, and trademarks | [Text Formatting](../docs/style-and-syntax.md#text-formatting) |
| Real Markdown numbered lists and troubleshooting | [Procedures and Lists](../docs/style-and-syntax.md#procedures-and-lists) |
| Captions, readable cropped screenshots, and size limits | [Images, Diagrams, and Assets](../docs/style-and-syntax.md#images-diagrams-and-assets) |
| MDX `<Alert>` blocks, `<br/>` void tags, and compilation rules | [Callouts, MDX, and HTML Rules](../docs/style-and-syntax.md#callouts-mdx-and-html-rules) |

The `_assets/` directory retains illustrations from the older contribution guide. Screenshots
of old syntax or frontmatter are not authoritative examples of current rules.
