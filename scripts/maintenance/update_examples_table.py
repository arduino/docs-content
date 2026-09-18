import os
import yaml
import re

# --- Configuration ---
# Possible locations for the app-bricks-examples repository
DEFAULT_REPO_PATHS = [
    os.environ.get("EXAMPLES_REPO_DIR"),
    os.environ.get("EXAMPLES_DIR"),
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../app-bricks-examples")),
    os.path.abspath("../app-bricks-examples"),
    os.path.expanduser("~/Documents/GitHub/app-bricks-examples"),
]

GITHUB_BASE_URL = "https://github.com/arduino/app-bricks-examples/tree/main/"

# The HTML comments to look for in your Markdown files
START_MARKER = "<!-- app-bricks-examples table start -->"
END_MARKER = "<!-- app-bricks-examples table end -->"

def find_repo_dir():
    """Finds the root directory of the app-bricks-examples repository."""
    for path in DEFAULT_REPO_PATHS:
        if path and os.path.exists(path) and os.path.isdir(path):
            return path
    return None

def build_markdown_table():
    """Reads inspirational example directories (common, platform_unoq, platform_ventunoq) and builds the Markdown tables."""
    repo_dir = find_repo_dir()
    if not repo_dir:
        print("Error: 'app-bricks-examples' repository directory not found.")
        return None

    inspirational_dir = os.path.join(repo_dir, "inspirational")
    if not os.path.exists(inspirational_dir):
        print(f"Error: Directory '{inspirational_dir}' not found.")
        return None

    sections = [
        ("Common Examples", os.path.join(inspirational_dir, "common")),
        ("Examples for UNO Q", os.path.join(inspirational_dir, "platform_unoq")),
        ("Examples for VENTUNO Q", os.path.join(inspirational_dir, "platform_ventunoq")),
    ]

    output_sections = []

    for section_title, section_dir in sections:
        if not os.path.exists(section_dir):
            continue

        examples_data = []
        for root, _, files in os.walk(section_dir):
            if "app.yaml" in files:
                yaml_path = os.path.join(root, "app.yaml")
                try:
                    with open(yaml_path, 'r', encoding='utf-8') as f:
                        app_data = yaml.safe_load(f) or {}

                    folder_name = os.path.basename(root)
                    # Extract fields with fallbacks
                    name = app_data.get('name', folder_name)

                    # Extract description and replace newlines with spaces
                    description = app_data.get('description', 'No description provided.')
                    if isinstance(description, str):
                        description = description.replace('\n', ' ').strip()

                    # Construct relative path from repository root for GitHub link
                    rel_path = os.path.relpath(root, repo_dir).replace('\\', '/')
                    source_link = f"[GitHub]({GITHUB_BASE_URL}{rel_path})"

                    examples_data.append({
                        "name": name,
                        "description": description,
                        "source_link": source_link,
                        "rel_path": rel_path
                    })

                except Exception as e:
                    print(f"Failed to process {yaml_path}: {e}")

        if examples_data:
            # Sort examples by name (case-insensitive), then by relative path
            examples_data.sort(key=lambda x: (x['name'].lower(), x['rel_path']))

            table_rows = [
                f"### {section_title}\n",
                "| Example | Description | Source |",
                "| --- | --- | --- |"
            ]
            for example in examples_data:
                table_rows.append(f"| {example['name']} | {example['description']} | {example['source_link']} |")

            output_sections.append("\n".join(table_rows))

    if not output_sections:
        print("No valid example configs found.")
        return None

    return "\n\n".join(output_sections) + "\n"

def inject_table_into_markdown(table_content):
    """Finds Markdown files with the appropriate wrappers and updates them."""
    if not table_content:
        return
        
    # Regex to match the start marker, everything in between (non-greedy), and the end marker
    pattern = re.compile(rf"({START_MARKER}\n).*?(\n{END_MARKER})", re.DOTALL)
    
    # Recursively search for all .md files in the repository
    search_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    for root, _, files in os.walk(search_root):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # Check if the markers exist in the file
                if START_MARKER in content and END_MARKER in content:
                    # Replace the content between the markers with the new table
                    updated_content = pattern.sub(rf"\1{table_content}\2", content)
                    
                    if content != updated_content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(updated_content)
                        print(f"✅ Successfully updated table in: {filepath}")
                    else:
                        print(f"⚡ No changes needed for: {filepath} (Table is up to date)")

if __name__ == "__main__":
    print("Generating Examples Markdown Table...")
    md_table = build_markdown_table()
    
    if md_table:
        print("Scanning Markdown files for injection markers...")
        inject_table_into_markdown(md_table)
        print("Done!")
