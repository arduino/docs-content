import os
import re
import yaml

# --- Configuration ---
# UI_DIR / CLOUD_EDITOR_MONO_DIR overrides the sibling cloud-editor-mono checkout.
# BRICKS_DIR overrides app-bricks-py (accepts either repo root or src/arduino/app_bricks).
UTILS_REL_PATH = os.path.join(
    "app", "core-ui", "src", "app-lab", "providers", "ai-models", "utils.ts"
)

DEFAULT_UI_PATHS = [
    os.environ.get("CLOUD_EDITOR_MONO_DIR"),
    os.environ.get("UI_DIR"),
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../cloud-editor-mono")),
    os.path.abspath("../cloud-editor-mono"),
    os.path.expanduser("~/Documents/GitHub/cloud-editor-mono"),
]

DEFAULT_BRICKS_PATHS = [
    os.environ.get("BRICKS_DIR"),
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../app-bricks-py/src/arduino/app_bricks")),
    os.path.abspath("../app-bricks-py/src/arduino/app_bricks"),
    os.path.expanduser("~/Documents/GitHub/app-bricks-py/src/arduino/app_bricks"),
]

# Human-readable labels for Edge Impulse project categories matched in isCompatibleEICategory.
CATEGORY_LABELS = {
    "object detection": "Object detection",
    "images": "Images (classification)",
    "images:keras-visual-anomaly": "Images (visual anomaly detection)",
    "audio": "Audio",
    "keyword spotting": "Keyword spotting",
    "accelerometer": "Accelerometer",
}

# The HTML comments to look for in Markdown files
START_MARKER = "<!-- app-lab-edge-impulse table start -->"
END_MARKER = "<!-- app-lab-edge-impulse table end -->"


def find_utils_file():
    """Finds cloud-editor-mono's ai-models/utils.ts."""
    for base in DEFAULT_UI_PATHS:
        if not base:
            continue
        candidate = base if base.endswith("utils.ts") else os.path.join(base, UTILS_REL_PATH)
        if os.path.isfile(candidate):
            return candidate
    return None


def find_bricks_dir():
    """Finds the app_bricks directory (accepts repo root or src/arduino/app_bricks)."""
    for path in DEFAULT_BRICKS_PATHS:
        if not path or not os.path.isdir(path):
            continue
        nested = os.path.join(path, "src", "arduino", "app_bricks")
        if os.path.isdir(nested):
            return nested
        return path
    return None


def load_brick_names(bricks_dir):
    """Returns {brick_id: display_name} from brick_config.yaml files."""
    names = {}
    for folder in os.listdir(bricks_dir):
        yaml_path = os.path.join(bricks_dir, folder, "brick_config.yaml")
        if not os.path.isfile(yaml_path):
            continue
        with open(yaml_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        if not config or config.get("disabled") is True:
            continue
        brick_id = config.get("id")
        if brick_id:
            names[brick_id] = config.get("name", folder)
    return names


def extract_brick_ids(block):
    """Extracts arduino:* brick IDs in order of appearance from a JS/TS snippet."""
    return list(dict.fromkeys(re.findall(r"['\"](arduino:[a-z0-9_]+)['\"]", block)))


def parse_compatible_categories(utils_path):
    """Parses isCompatibleEICategory() from cloud-editor-mono's utils.ts."""
    with open(utils_path, "r", encoding="utf-8") as f:
        src = f.read()

    fn_match = re.search(
        r"export\s+const\s+isCompatibleEICategory\s*=\s*\(.*?\n\};",
        src,
        re.DOTALL,
    )
    if not fn_match:
        raise ValueError(f"Could not locate isCompatibleEICategory in {utils_path}")

    fn_body = fn_match.group(0)
    case_matches = list(re.finditer(r"case\s+['\"]([^'\"]+)['\"]\s*:", fn_body))
    if not case_matches:
        raise ValueError(f"No switch cases found in isCompatibleEICategory ({utils_path})")

    entries = []
    for idx, m in enumerate(case_matches):
        cat = m.group(1).strip().lower()
        start = m.end()
        if idx + 1 < len(case_matches):
            end = case_matches[idx + 1].start()
        else:
            default_m = re.search(r"\bdefault\s*:", fn_body[start:])
            end = start + default_m.start() if default_m else len(fn_body)
        body = fn_body[start:end]

        if cat == "other":
            # Empty projects (no learning blocks) match every AI Brick; documented in prose.
            continue

        # Handle conditional sub-branches such as keras-visual-anomaly inside `case 'images'`.
        sub_if = re.search(
            r"lb\.type\s*===\s*['\"]([^'\"]+)['\"].*?if\s*\([^)]+\)\s*\{([^}]*)\}(.*)",
            body,
            re.DOTALL,
        )
        if sub_if:
            block_type = sub_if.group(1)
            then_ids = extract_brick_ids(sub_if.group(2))
            rest_ids = extract_brick_ids(sub_if.group(3))
            if rest_ids:
                entries.append((CATEGORY_LABELS.get(cat, cat.capitalize()), rest_ids))
            if then_ids:
                sub_key = f"{cat}:{block_type}"
                entries.append((CATEGORY_LABELS.get(sub_key, f"{cat.capitalize()} ({block_type})"), then_ids))
        else:
            brick_ids = extract_brick_ids(body)
            if brick_ids:
                entries.append((CATEGORY_LABELS.get(cat, cat.capitalize()), brick_ids))

    return entries


def build_markdown_table():
    """Builds the Edge Impulse project type to compatible Bricks Markdown table."""
    utils_path = find_utils_file()
    if not utils_path:
        print("Error: cloud-editor-mono ai-models/utils.ts not found.")
        return None

    bricks_dir = find_bricks_dir()
    if not bricks_dir:
        print("Error: 'app_bricks' directory not found.")
        return None

    brick_names = load_brick_names(bricks_dir)
    entries = parse_compatible_categories(utils_path)
    if not entries:
        print("No compatible Edge Impulse categories found.")
        return None

    rows = [
        "| Edge Impulse project type | Compatible Bricks |",
        "| :--- | :--- |",
    ]
    for label, brick_ids in entries:
        resolved = []
        for bid in brick_ids:
            if bid not in brick_names:
                raise ValueError(
                    f"Brick ID '{bid}' from {utils_path} not found in {bricks_dir}."
                )
            resolved.append(brick_names[bid])
        resolved.sort(key=lambda s: s.lower())
        rows.append(f"| {label} | {', '.join(resolved)} |")

    return "\n".join(rows)


def inject_table_into_markdown(table_content):
    """Finds Markdown files with the appropriate wrappers and updates them."""
    if not table_content:
        return

    pattern = re.compile(
        rf"(^{re.escape(START_MARKER)}\n).*?(^{re.escape(END_MARKER)}$)",
        re.DOTALL | re.MULTILINE,
    )
    search_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

    for root, _, files in os.walk(search_root):
        for file in files:
            if not file.endswith(".md"):
                continue
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            if pattern.search(content):
                updated_content = pattern.sub(rf"\1{table_content}\n\2", content)
                if content != updated_content:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(updated_content)
                    print(f"✅ Successfully updated table in: {filepath}")
                else:
                    print(f"⚡ No changes needed for: {filepath} (Table is up to date)")


if __name__ == "__main__":
    print("Generating Edge Impulse Compatibility Markdown Table...")
    md_table = build_markdown_table()
    if md_table:
        print("Scanning Markdown files for injection markers...")
        inject_table_into_markdown(md_table)
        print("Done!")
