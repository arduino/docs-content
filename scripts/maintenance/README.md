# Maintenance Scripts

This directory contains Python scripts for automatically generating and updating documentation tables and CLI references across the repository.

These scripts extract data from upstream repositories and inject the formatted Markdown between dedicated HTML comment markers in the documentation files.

## Prerequisites

- **Python 3**
- **PyYAML** (for YAML-based tables):
  ```bash
  pip install pyyaml
  ```
- **Go** (for CLI reference generation): required by `update_cli_reference.py` to inspect Cobra command definitions in `arduino-app-cli`.

### Repository Locations

The scripts look for upstream repositories in standard locations:
- Sibling directories next to `docs-content` (e.g. `../app-bricks-py`, `../app-bricks-examples`, `../arduino-app-cli`)
- `~/Documents/GitHub/<repo>`
- Custom paths specified via environment variables

---

## Available Scripts

### 1. Update Bricks Table (`update_bricks_table.py`)

Reads brick metadata (`brick_config.yaml`) from `app-bricks-py` and updates the Bricks table.

- **Source Repository:** [`arduino/app-bricks-py`](https://github.com/arduino/app-bricks-py)
- **Environment Variable Override:** `BRICKS_DIR`
- **Target Markers:** `<!-- app-bricks-py table start -->` and `<!-- app-bricks-py table end -->`
- **Usage:**
  ```bash
  python3 scripts/maintenance/update_bricks_table.py
  ```

### 2. Update Examples Table (`update_examples_table.py`)

Reads inspirational example applications (`app.yaml`) from `app-bricks-examples` and updates the Examples table.

- **Source Repository:** [`arduino/app-bricks-examples`](https://github.com/arduino/app-bricks-examples)
- **Environment Variable Override:** `EXAMPLES_REPO_DIR` or `EXAMPLES_DIR`
- **Target Markers:** `<!-- app-bricks-examples table start -->` and `<!-- app-bricks-examples table end -->`
- **Usage:**
  ```bash
  python3 scripts/maintenance/update_examples_table.py
  ```

### 3. Update Models Table (`update_models_table.py`)

Reads model definitions from `models-list.yaml` in `app-bricks-py` and updates the Models tables grouped by family (Vision, Audio & speech, Language, Sensor).

- **Source Repository:** [`arduino/app-bricks-py`](https://github.com/arduino/app-bricks-py) (`models/models-list.yaml`)
- **Target Markers:** `<!-- app-lab-models table start -->` and `<!-- app-lab-models table end -->`
- **Usage:**
  ```bash
  python3 scripts/maintenance/update_models_table.py
  ```

### 4. Update CLI Command Reference (`update_cli_reference.py`)

Generates the complete command-line reference from the `arduino-app-cli` Cobra command definitions. Preserves page frontmatter, intro prose, and linter directives.

- **Source Repository:** [`arduino/arduino-app-cli`](https://github.com/arduino/arduino-app-cli)
- **Environment Variable Override:** `ARDUINO_APP_CLI_DIR` or `APP_CLI_DIR`
- **Target Markers:** `<!-- arduino-app-cli commands start -->` and `<!-- arduino-app-cli commands end -->`
- **Usage:**
  ```bash
  # Ensure arduino-app-cli is on the desired release or tag (e.g. v0.13.0)
  python3 scripts/maintenance/update_cli_reference.py
  ```

---

## Run All Maintenance Scripts

To update all auto-generated content at once:

```bash
python3 scripts/maintenance/update_bricks_table.py
python3 scripts/maintenance/update_examples_table.py
python3 scripts/maintenance/update_models_table.py
python3 scripts/maintenance/update_cli_reference.py
```
