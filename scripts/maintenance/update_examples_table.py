import os
import yaml
import re

# --- Configuration ---
EXAMPLES_DIR = "../app-bricks-examples/examples"
GITHUB_BASE_URL = "https://github.com/arduino/app-bricks-examples/tree/main/examples/"

# The HTML comments to look for in your Markdown files
START_MARKER = "<!-- app-bricks-examples table start -->"
END_MARKER = "<!-- app-bricks-examples table end -->"

def build_markdown_table():
    """Reads example directories and builds the Markdown table."""
    if not os.path.exists(EXAMPLES_DIR):
        print(f"Error: Directory '{EXAMPLES_DIR}' not found.")
        return None

    # Initialize table headers
    rows = [
        "| Example | Description | Source |",
        "|---|---|---|"
    ]
    
    examples_data = []
    
    # Get all subdirectories
    example_dirs = [
        d for d in os.listdir(EXAMPLES_DIR) 
        if os.path.isdir(os.path.join(EXAMPLES_DIR, d))
    ]
    
    for folder_name in example_dirs:
        yaml_path = os.path.join(EXAMPLES_DIR, folder_name, "app.yaml")
        
        if os.path.exists(yaml_path):
            try:
                with open(yaml_path, 'r', encoding='utf-8') as f:
                    app_data = yaml.safe_load(f)
                    
                # Extract fields with fallbacks
                name = app_data.get('name', folder_name)
                
                # Extract description and replace newlines with spaces
                description = app_data.get('description', 'No description provided.')
                if isinstance(description, str):
                    description = description.replace('\n', ' ').strip()
                
                # Construct GitHub link
                source_link = f"[GitHub]({GITHUB_BASE_URL}{folder_name})"
                
                examples_data.append({
                    "name": name,
                    "description": description,
                    "source_link": source_link
                })
                
            except Exception as e:
                print(f"Failed to process {yaml_path}: {e}")

    # Sort examples by name (case-insensitive)
    examples_data.sort(key=lambda x: x['name'].lower())

    for example in examples_data:
        rows.append(f"| {example['name']} | {example['description']} | {example['source_link']} |")

    return "\n".join(rows) + "\n"

def inject_table_into_markdown(table_content):
    """Finds Markdown files with the appropriate wrappers and updates them."""
    if not table_content:
        return
        
    # Regex to match the start marker, everything in between (non-greedy), and the end marker
    pattern = re.compile(rf"({START_MARKER}\n).*?(\n{END_MARKER})", re.DOTALL)
    
    # Recursively search for all .md files in the repository
    for root, _, files in os.walk("."):
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
