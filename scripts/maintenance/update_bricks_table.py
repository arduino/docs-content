import os
import yaml
import re

# --- Configuration ---
# Possible locations for the app_bricks directory
DEFAULT_BRICKS_PATHS = [
    os.environ.get("BRICKS_DIR"),
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../app-bricks-py/src/arduino/app_bricks")),
    os.path.abspath("../app-bricks-py/src/arduino/app_bricks"),
    os.path.expanduser("~/Documents/GitHub/app-bricks-py/src/arduino/app_bricks"),
]

GITHUB_BASE_URL = "https://github.com/arduino/app-bricks-py/tree/main/src/arduino/app_bricks/"

# The HTML comments to look for in your Markdown files
START_MARKER = "<!-- app-bricks-py table start -->"
END_MARKER = "<!-- app-bricks-py table end -->"

def find_bricks_dir():
    """Finds the app_bricks directory."""
    for path in DEFAULT_BRICKS_PATHS:
        if path and os.path.exists(path) and os.path.isdir(path):
            return path
    return None

def build_markdown_table():
    """Reads brick directories and builds the Markdown table."""
    bricks_dir = find_bricks_dir()
    if not bricks_dir:
        print("Error: 'app_bricks' directory not found.")
        return None

    bricks_data = []

    # Get all directories in the bricks folder
    brick_dirs = [
        d for d in os.listdir(bricks_dir) 
        if os.path.isdir(os.path.join(bricks_dir, d))
    ]
    
    for folder_name in brick_dirs:
        yaml_path = os.path.join(bricks_dir, folder_name, "brick_config.yaml")
        
        if os.path.exists(yaml_path):
            try:
                with open(yaml_path, 'r', encoding='utf-8') as f:
                    config = yaml.safe_load(f)
                    
                if not config:
                    continue
                    
                # Do not include disabled bricks
                if config.get('disabled') is True:
                    continue
                    
                # Extract fields with fallbacks
                name = config.get('name', folder_name)
                category = config.get('category', '')
                
                # Extract description and replace newlines with spaces so it doesn't break the Markdown table
                description = config.get('description')
                if description is None:
                    description = config.get('module_description', '')
                
                if isinstance(description, str):
                    description = description.replace('\n', ' ').strip()
                
                # Construct GitHub link
                source_link = f"[GitHub]({GITHUB_BASE_URL}{folder_name})"
                
                bricks_data.append({
                    'name': name,
                    'category': category,
                    'description': description,
                    'source': source_link
                })
                
            except Exception as e:
                print(f"Failed to process {yaml_path}: {e}")

    if not bricks_data:
        print("No valid brick configs found.")
        return None

    # Sort alphabetically by Brick Name for consistent table ordering
    bricks_data.sort(key=lambda x: x['name'].lower())

    # Initialize table headers
    rows = [
        "| Brick | Description | Source |",
        "| --- | --- | --- |"
    ]
    
    # Generate rows
    for brick in bricks_data:
        rows.append(f"| {brick['name']} | {brick['description']} | {brick['source']} |")

    return "\n".join(rows) + "\n"

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
    print("Generating Bricks Markdown Table...")
    md_table = build_markdown_table()
    
    if md_table:
        print("Scanning Markdown files for injection markers...")
        inject_table_into_markdown(md_table)
        print("Done!")
