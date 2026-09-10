# Automated Screenshot Capture for Arduino App Lab

[Playwright](https://playwright.dev/) scripts that drive a local [`arduino-app-lab`](https://github.com/arduino/arduino-app-lab) dev build to regenerate documentation screenshots.

## Prerequisites

1. **An App Lab dev build running locally.** These scripts attach to `arduino-app-lab` in Wails dev mode at `http://localhost:34115`; they do not launch it. Check out the version you're documenting — the **latest release tag** for live docs, or `main` for unreleased changes — and start its dev server per that repo's own setup instructions before running a capture.
2. **A connected board.** A supported board (e.g. Arduino UNO Q) must be powered on and reachable, since the flow selects it on the welcome screen and runs a real app on it.
3. **Playwright installed** for this script folder:
   ```bash
   npm install
   npx playwright install chromium
   ```

## Running

From `scripts/playwright`, with the App Lab dev build up:

```bash
node runner.js --flow app-lab
```

Screenshots default to `../../content/software/app-lab/assets/playwright`.

| Flag | Values | Default | Description |
| --- | --- | --- | --- |
| `--flow <name>` | `app-lab`, `arduino-cloud`, … | `app-lab` | Which flow module in `flows/` to run. |
| `--step <name>` | `all`, `navigation`, `inspirations`, `editor`, `run`, `terminal` | `all` | Run only one segment of the flow. |
| `--outDir <path>` | any path | see above | Override the output directory (resolved from the current working dir). |
| `--debug`, `--verbose` | flag | `false` | Enable verbose logging during execution. |

A full run takes several minutes because it compiles and runs a real app on the board. While iterating on one screenshot, run just its step:

- `navigation` — sidebar and status bar
- `inspirations` — Inspirations card and detail views
- `editor` — app creation and editor panels
- `run` — app compile, execution, stop, and console (also runs the `editor` setup it depends on)
- `terminal` — board shell button in the status bar

## Post-run cleanup & committing

The automation script captures intermediate views and alternate crops that may not all be referenced in documentation. Additionally, dynamic indicators in the status bar (such as CPU load, memory utilization, or network state) vary across runs, causing otherwise byte-identical images to show file modifications in Git.

1. **Prune unreferenced captures**: Run the image linter to automatically delete unlinked images and keep repository checks green:
   ```bash
   python3 scripts/validation/image_links/image_links.py remove-unlinked content/software/app-lab
   ```
2. **Review image diffs selectively**: Many screenshots across various folders (such as bottom-anchored views in `editor/` or full-window captures) include the status bar. Because live system metrics (CPU load, memory utilization, network activity) constantly fluctuate, regenerated screenshots may show binary diffs in Git even when the underlying UI layout is unchanged.

   Inspect `git status` carefully and **only stage and commit images that reflect intentional UI or documentation updates**. Discard cosmetic diffs on unchanged views (e.g. using `git restore <file>`).

## Directory layout

```text
scripts/playwright/
├── runner.js            # Entry point: parses flags, launches Chromium, invokes the flow
├── core/capture.js      # Capture engine: CONFIG, capture(), highlights, callouts, overlay suppression
├── flows/app-lab.js     # The App Lab interaction sequence and locators
├── flows/arduino-cloud.js # Template/placeholder for a future flow
└── sketch.ino           # Sample sketch typed into the editor during the `editor` step
```

Each `capture()` call's `pathname` maps to an output path, e.g. `capture(page, 'editor/run-button.png', …)` → `…/playwright/editor/run-button.png`.

## Adding a screenshot or flow

Screenshots are produced by `capture(page, pathname, outDir, options)` in `core/capture.js`. Its `options` control framing (`crop`, `percentage`, `padding`) and annotation (`highlight` for orange outlines, labelled callouts with connector lines, `insetHighlight` for large panels). Rather than repeat the option list here, copy from the real call sites in `flows/app-lab.js` — e.g. the `statusbar-controls-hl.png` capture is a worked multi-label callout example.

To add a screenshot: inside the matching `if (step === …)` block in `flows/app-lab.js`, define a locator (prefer stable `id`/`aria-label`/`role` selectors), navigate to the state you need, and add a `capture()` call. Iterate with `node runner.js --flow app-lab --step <step>`.

Naming conventions:

- `-hl` — the image contains a highlight/outline; `-crop` — a cropped variant.
- Group related shots into subfolders (`navigation/`, `editor/`, `editor/console/`, `inspirations/`).

To add a flow, create `flows/<name>.js` exporting `async (page, outDir, options)` (see `flows/arduino-cloud.js`) and run it with `--flow <name>`.

## Debugging

On failure the runner writes a DOM snapshot and error details to `debug/` (git-ignored): `failure-dump.html` (page HTML at the point of failure) and `failure-details.log` (timestamp, URL, step, stack trace). Open the dump to find a stable attribute for a more robust selector.
