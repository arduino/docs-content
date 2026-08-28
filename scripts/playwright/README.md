# Docs Automation Screenshots

This directory contains automated visual capture scripts for Arduino documentation. It uses [Playwright](https://playwright.dev/) to interact with local development builds and capture, highlight, and crop screenshots consistently.

## Prerequisites

1. **Physical Board Requirement**: A supported board (e.g. Arduino UNO Q) **must be powered on, running its software stack, and connected via USB or reachable over the local network** before starting.
2. **Environment**: Ensure you have Node.js, Yarn, and Direnv installed as per the repository setup instructions.
3. **Playwright Dependencies**: Run `npm install` inside this `scripts/playwright` directory, and ensure the Chromium binary is installed:
   ```bash
   npx playwright install chromium
   ```

## Setup & Execution

1. **Start the target app:**
   Navigate to the `arduino-app-lab` repository and start the local development server:
   ```bash
   yarn start-app-lab-desktop
   ```
2. **Run the automation script:**
   From the `docs-content/scripts/playwright` directory, execute:
   ```bash
   node runner.js --flow app-lab
   ```
   By default, screenshots are saved directly to `../../content/software/app-lab/assets/playwright`.

### Segmented / Step Execution
You can run specific steps of a flow using the `--step` flag:
- `node runner.js --flow app-lab --step navigation` (Sidebar and Status bar)
- `node runner.js --flow app-lab --step inspirations` (Inspirations card and detail views)
- `node runner.js --flow app-lab --step editor` (App creation and Editor panels)
- `node runner.js --flow app-lab --step run` (App compile, execution, stop, and console)
- `node runner.js --flow app-lab --step terminal` (Board shell button in the status bar)

## Modifying Locators and Adding Flows

- `core/capture.js`: Contains reusable visual capture logic, orthogonal connector drawing, label distribution, and toast suppression.
- `flows/app-lab.js`: Contains the sequence of interactions and locators for App Lab.
- `flows/arduino-cloud.js`: Template for adding automated visual captures for other Arduino services.
