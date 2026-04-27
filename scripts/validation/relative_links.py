import os
import re
import sys
import argparse

# Regex for Markdown links: [text](link "title")
# Updated to support spaces in the link part by stopping at the first quote or closing parenthesis.
LINK_REGEX = re.compile(r'(\[(?P<text>[^\]]*)\])\((?P<link>[^"\'\)]+)(?P<title>\s+["\'][^"\']*["\'])?\)')

def process_link(path):
    """
    1. Removes number prefixes (e.g., '1.', '02.') from folder names.
    2. Removes the filename if it is a Markdown file (.md).
    3. Ensures a trailing slash for directory-style links.
    4. Replaces spaces with %20.
    """
    if path.startswith(('http://', 'https://', 'mailto:', '#')):
        # Still encode spaces in these if they exist (though rare in mailto/anchors)
        return path.replace(' ', '%20')
    
    # Handle anchors and queries
    base_path = path
    suffix = ""
    if '#' in path:
        parts = path.split('#', 1)
        base_path = parts[0]
        suffix = '#' + parts[1]
    elif '?' in path:
        parts = path.split('?', 1)
        base_path = parts[0]
        suffix = '?' + parts[1]
        
    components = base_path.split('/')
    new_components = []
    
    last_idx = len(components) - 1
    
    for i, comp in enumerate(components):
        is_last = (i == last_idx)
        
        # If it's a Markdown filename, remove it entirely
        if is_last and comp.endswith('.md'):
            continue
            
        if comp:
            # Remove digits followed by a dot at the start (e.g., "1.setup" -> "setup")
            new_comp = re.sub(r'^\d+\.', '', comp)
            new_components.append(new_comp)
        else:
            # Preserve leading/empty components (e.g., absolute paths or trailing slashes)
            new_components.append(comp)
            
    result = "/".join(new_components)
    
    # Ensure trailing slash if it was a .md file or already a directory link
    if components[last_idx].endswith('.md') or components[last_idx] == "":
        if not result.endswith('/'):
            result += '/'
            
    # Edge case: if a relative link to a file in the same dir became empty (e.g., "file.md" -> "")
    if result == "" and not base_path.startswith('/') and components[last_idx].endswith('.md'):
        result = "./"
        
    final_path = result + suffix
    
    # 4. Replace spaces with %20
    return final_path.replace(' ', '%20')

def fix_file(file_path):
    """Processes a Markdown file and applies link fixes."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def replace_match(match):
        prefix = match.group(1)
        link = match.group('link')
        title = match.group('title') or ""
        return f"{prefix}({process_link(link)}{title})"

    new_content = LINK_REGEX.sub(replace_match, content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def validate_file(file_path):
    """Checks if a Markdown file contains links that don't match the required format."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    for match in LINK_REGEX.finditer(content):
        link = match.group('link')
        fixed_link = process_link(link)
        if link != fixed_link:
            issues.append(link)
    return issues

def main():
    parser = argparse.ArgumentParser(description="Manage relative links in Markdown files.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    fix_parser = subparsers.add_parser("fix")
    fix_parser.add_argument("path", help="Path to a file or directory")
    
    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("path", help="Path to a file or directory")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.path):
        print(f"Error: Path '{args.path}' does not exist.")
        sys.exit(1)
        
    files_to_process = []
    if os.path.isfile(args.path):
        if args.path.endswith(".md"):
            files_to_process.append(args.path)
    else:
        for root, _, files in os.walk(args.path):
            for file in files:
                if file.endswith(".md"):
                    files_to_process.append(os.path.join(root, file))
                    
    if args.command == "fix":
        fixed_count = 0
        for file_path in files_to_process:
            if fix_file(file_path):
                print(f"Fixed: {file_path}")
                fixed_count += 1
        print(f"Processed {len(files_to_process)} files. Fixed {fixed_count} files.")
        
    elif args.command == "validate":
        all_issues = {}
        for file_path in files_to_process:
            issues = validate_file(file_path)
            if issues:
                all_issues[file_path] = issues
        
        if all_issues:
            print("Validation failed. The following files contain non-compliant links:")
            for file_path, issues in all_issues.items():
                print(f"\n{file_path}:")
                for issue in issues:
                    print(f"  - {issue}")
            sys.exit(1)
        else:
            print("Validation successful: All local Markdown links are compliant.")

if __name__ == "__main__":
    main()
