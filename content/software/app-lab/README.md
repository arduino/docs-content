# Arduino App Lab

This directory contains the documentation for **Arduino App Lab**.

## Structure & User Journey

The documentation is organized following the user journey and logical categorization of the platform:

1. **Setup**: Installation and initial configuration.
2. **Configure**: Detailed system and environment settings.
3. **Getting Started**: First steps and quickstart guides.
4. **Apps**: Creating and managing applications.
5. **Bricks**: Using and developing reusable components (Bricks).
6. **Bridge**: Connectivity and communication between components.
7. **CLI**: Command-line interface reference and usage.
8. **Integrations**: Connecting App Lab with external services.
9. **Release Notes**: Historical and current version changes.

### Board Agnosticism

When writing App Lab documentation, use generic terms like "your board" or "the board". Use "Arduino UNO Q" only for specific examples. Refer to "VENTUNO Q" *only* in the context of the list of compatible boards in the Setup Overview; avoid suggesting a broader set of compatible boards (do not use phrases like "For example, the UNO Q" or "UNO Q or other compatible board").

### Shared Asset Folder

Unlike other sections of the documentation, App Lab uses a **shared `assets/` folder** located at the root of the `app-lab` directory. All images and static files should be placed here to maintain a clean structure.

## Maintenance and Automation

> [!NOTE]
> These are manual tasks that must be performed for new releases.

### Bricks, Examples & Models Tables

The tables in the documentation that list available Bricks, Examples, and Models are **auto-generated**. Do not edit them manually, as they will be overwritten.

* **Setup**: These scripts expect the source repositories (`app-bricks-py` and `app-bricks-examples`) to be **cloned at the same directory level** as `docs-content`.
* **Update Bricks**: Run `python3 scripts/maintenance/update_bricks_table.py`. It looks for `<!-- app-bricks-py table start -->` markers.
* **Update Examples**: Run `python3 scripts/maintenance/update_examples_table.py`. It looks for `<!-- app-bricks-examples table start -->` markers.
* **Update Models**: Run `python3 scripts/maintenance/update_models_table.py`. It looks for `<!-- app-lab-models table start -->` markers.

### CLI Command Reference

The CLI reference page is generated from the `arduino-app-cli` source code.

* **Setup**: This script expects the `arduino-app-cli` repository to be cloned at the same directory level as `docs-content` (or configured via the `ARDUINO_APP_CLI_DIR` environment variable).
* **Update Commands Reference**: Run `python3 scripts/maintenance/update_cli_reference.py`. It looks for `<!-- arduino-app-cli commands start -->` markers.
