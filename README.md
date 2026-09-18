# Arduino Documentation

## What Is this Repository?

This repository hosts the content for [Arduino Docs](https://docs.arduino.cc), Arduino's main documentation portal. The content is written in Markdown and converted to HTML automatically during the build process.

To find other Arduino projects, check the [repo page](https://github.com/arduino).

## Contributing

Before committing changes, please refer to our [CONTRIBUTING.md](CONTRIBUTING.md) guide.

## Prerequisites

- For local editing, use Git and a Markdown-capable editor like VS Code.
- Use Python 3 for the validation wrappers and Node.js/npm for Markdownlint and the legacy content linter.
- The versions in [package.json](package.json) and the [validation workflow](.github/workflows/workflow-validate.yaml) describe the repository's current toolchain.

The root dependency installation runs a theme bootstrap through `postinstall`.

Theme access may require credentials; running the focused validation tools does not require a complete site installation.

Do not copy credentials into articles, screenshots, or commits.

## Repository Structure

| Location | Purpose |
| --- | --- |
| `content/hardware/` | Hardware families, product types, products, tutorials, and datasheets |
| `content/software/` | Arduino software documentation and software-specific navigation |
| `content/learn/` | Conceptual and educational articles |
| `content/tutorials/` | Shared tutorials, including content reused by products |
| `content/built-in-examples/` | Built-in sketch examples |
| `contribution-templates/` | Article starting points |
| `scripts/` | Validation, rendering, automation, and maintenance tooling |

## Tooling & Validation

The repository employs several automated systems to ensure content quality. Refer to the specialized documentation for each:

| Tooling / Validation | Documentation Path | Description |
| --- | --- | --- |
| **Playwright Automation** | [`scripts/playwright/README.md`](scripts/playwright/README.md) | Guidelines for E2E tests and UI automation. |
| **Content Validation Suite** | [`scripts/validation/README.md`](scripts/validation/README.md) | Details on link checking and relative path validation. |
| **Maintenance Scripts** | [`scripts/maintenance/`](scripts/maintenance/) | Scripts for auto-generating tables and keeping documentation synced with source code. |

## License

Please note that your contribution to the Arduino Documentation is licensed under a [Creative Commons Attribution-Share Alike 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/).

![Creative Commons Attribution-ShareAlike](https://i.creativecommons.org/l/by-sa/3.0/88x31.png)
