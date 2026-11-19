# Arduino Documentation (`docs-content`)

This repository contains the Markdown and MDX source content for [Arduino Docs](https://docs.arduino.cc), Arduino's primary technical documentation portal.

## Documentation Ecosystem

`docs.arduino.cc` aggregates content and code from several repositories:

| Repository | Role |
| --- | --- |
| **`arduino/docs-content`** (this repo) | Hardware pages, datasheets, software guides, Cloud guides, tutorials, and Learn articles |
| [`arduino/docs.arduino.cc`](https://github.com/arduino/docs.arduino.cc) | Gatsby 5 + React 18 site engine, UI components, and routing logic (published as `@arduino/docs-arduino-cc`) |
| [`arduino/reference-en`](https://github.com/arduino/reference-en) | Arduino Language Reference (`/language-reference`) |
| `arduino/docs-content-library` | Arduino Library Reference (`/libraries`) |
| [`arduino/arduino-cli`](https://github.com/arduino/arduino-cli) & `arduino/iot-client-docs` | Upstream sources for `/arduino-cli` and `/cloud-api` |

## Contributing

Before opening a pull request, read [CONTRIBUTING.md](CONTRIBUTING.md) for workflow and validation steps, along with the authoring references in [`docs/`](docs/content-structure.md):

* **[CONTRIBUTING.md](CONTRIBUTING.md)** — Scope, pull request workflow, local validation commands, and preview checklist
* **[docs/content-structure.md](docs/content-structure.md)** — Directory layout, `content/order.json` sidebar ordering, grouped tutorials, frontmatter schemas, routing, downloadable resources, localization, and symlinks
* **[docs/style-and-syntax.md](docs/style-and-syntax.md)** — Writing style, headings, formatting, code blocks, images, `<Alert>` callouts, and MDX compilation rules

## Repository Structure

| Path | Purpose |
| --- | --- |
| `content/hardware/` | Hardware families, product pages (`product.md` and companion files), `downloads/`, datasheets, and product tutorials |
| `content/software/` | Software documentation (`app-lab`, `ide-v1`, `ide-v2`, `plc-ide`, `web-editor`) |
| `content/arduino-cloud/` | Arduino Cloud guides, APIs, IoT Remote, Education, and application notes |
| `content/learn/` | Conceptual electronics, microcontroller, programming, and Edge AI articles |
| `content/tutorials/` | Shared hardware-agnostic and multi-board tutorials |
| `content/built-in-examples/` | Built-in Arduino IDE sketch tutorials |
| `content/micropython/` & `content/programming/` | MicroPython documentation and programming landing content |
| `content/retired/` | Legacy and retired hardware documentation |
| [`content/order.json`](content/order.json) | Declarative sidebar and listing order across migrated sections |
| [`docs/`](docs/content-structure.md) | Authoring, structure, routing, style, and MDX syntax references |
| [`contribution-templates/`](contribution-templates/README.md) | Starter Markdown templates for tutorials, how-to guides, and articles |
| `scripts/` | Validation suite, maintenance generators, datasheet PDF renderer, and Playwright automation |

## Build, Preview, and Deployment

* **CI Site Build:** In GitHub Actions, `npm install` pulls `@arduino/docs-arduino-cc` and runs its `postinstall` bootstrap (`commands.sh bootstrap`) to copy the Gatsby site engine into the workspace, render modified datasheets to PDF ([`_render-datasheets.yml`](.github/workflows/_render-datasheets.yml)), copy hardware downloads into `static/resources/`, and build static HTML (`fetch-depth: 0` with `filter: blob:none` preserves per-page Git update timestamps).
* **Production (<https://docs.arduino.cc>):** Deployed by [`deploy-production.yml`](.github/workflows/deploy-production.yml) on a daily schedule (`08:00 Europe/Rome`) whenever `main` has undeployed commits, or on demand via `workflow_dispatch`.
* **Staging (<https://docs.oniudra.cc>):** Deployed manually via [`deploy-staging.yml`](.github/workflows/deploy-staging.yml).
* **Pull Request Previews:** Adding the `preview` label to an in-repository pull request triggers [`preview.yml`](.github/workflows/preview.yml) and posts a Netlify preview link on the PR. Pushing new commits automatically removes the `preview` label so rebuilds only run when re-labeled.
* **Local Environment:** Contributors do **not** need to run `npm install` at the repository root—it requires an internal `REPO_ACCESS_TOKEN` for private `@bcmi-labs/*` theme packages and skips the Gatsby bootstrap outside CI. Run the standalone validation tools below instead. Maintainers who need a live local Gatsby server should clone `arduino/docs.arduino.cc`, symlink this repository's `content/` directory into it, and run `npm run dev` there.

## Tooling and Validation

| Suite | Documentation | Purpose |
| --- | --- | --- |
| **Content Validation Suite** | [`scripts/validation/README.md`](scripts/validation/README.md) | Markdownlint, MDX compiler check (`mdx-check.js`), `<Alert>` spacing, internal route/resource link validation, image/asset checks, and legacy hardware schema linting |
| **Maintenance Scripts** | [`scripts/maintenance/README.md`](scripts/maintenance/README.md) | Auto-generators for App Lab Bricks, Examples, AI Models tables, and CLI command reference |
| **Playwright Automation** | [`scripts/playwright/README.md`](scripts/playwright/README.md) | Automated UI screenshot capture, cropping, and callout overlays |
| **Datasheet Rendering** | [`scripts/datasheet-rendering/`](scripts/datasheet-rendering/) | Docker-based PDF rendering configs and styles for English and localized datasheets |

## License

Documentation in this repository is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/), and code examples are dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). See [LICENSE.md](LICENSE.md) for details.
