import os
import re
import sys
import argparse
import posixpath
import urllib.parse
import fnmatch
import string

# Regex for Markdown links: [text](link "title")
LINK_REGEX = re.compile(r'(\[(?P<text>[^\]]*)\])\((?P<link>[^"\'\)]+)(?P<title>\s+["\'][^"\']*["\'])?\)')

# Regex for Markdown headings: # Heading
HEADING_REGEX = re.compile(r'^#{1,6}\s+(.+)$', re.MULTILINE)

# Regex for HTML ids and names: id="anchor" or name="anchor"
HTML_ID_REGEX = re.compile(r'(?:id|name)=["\']([^"\']+)["\']')

IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')
ASSET_EXTENSIONS = IMAGE_EXTENSIONS + ('.pdf', '.zip')

def slugify(text):
    """Converts a heading string to a valid Markdown anchor slug."""
    text = text.lower().strip()
    # Replace spaces with hyphens
    text = re.sub(r'\s+', '-', text)
    # Remove punctuation
    text = re.sub(r'[^\w\-]', '', text)
    return text

def extract_anchors(file_path):
    """Extracts all valid anchors from a Markdown file."""
    anchors = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Extract from headings
            for match in HEADING_REGEX.finditer(content):
                heading_text = match.group(1)
                anchors.add(slugify(heading_text))
                
            # Extract from HTML ids/names
            for match in HTML_ID_REGEX.finditer(content):
                anchors.add(match.group(1))
    except Exception as e:
        print(f"Warning: Could not read {file_path} to extract anchors: {e}")
    return anchors

def process_link(path):
    """
    1. Removes number prefixes (e.g., '1.', '02.') from folder names.
    2. Removes the filename if it is a Markdown file (.md).
    3. Replaces spaces with %20.
    """
    if path.startswith(('http://', 'https://', 'mailto:', '#', 'data:')):
        return path.replace(' ', '%20')
    
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
        if is_last and comp.endswith('.md'):
            continue
            
        if comp:
            new_comp = re.sub(r'^\d+\.', '', comp)
            new_components.append(new_comp)
        else:
            new_components.append(comp)
            
    result = "/".join(new_components)
    
    if result == "" and not base_path.startswith('/') and components[last_idx].endswith('.md'):
        result = "./"
        
    final_path = result + suffix
    return final_path.replace(' ', '%20')

def map_file_to_url(file_path, content_dir):
    """Maps a local markdown file to its production URL."""
    rel_path = os.path.relpath(file_path, content_dir).replace('\\', '/')
    
    # Special Hardware Tutorials rule
    hardware_match = re.match(r'^hardware/(?:[^/]+/)+([^/]+)/tutorials/([^/]+)/[^/]+\.md$', rel_path)
    if hardware_match:
        board = hardware_match.group(1)
        tutorial = re.sub(r'^\d+\.', '', hardware_match.group(2))
        return f"/tutorials/{board}/{tutorial}/"
        
    # Special Hardware Product rule
    product_match = re.match(r'^hardware/(?:[^/]+/)+([^/]+)/product\.md$', rel_path)
    if product_match:
        board = product_match.group(1)
        return f"/hardware/{board}/"
        
    # Default rule
    components = rel_path.split('/')
    new_components = []
    last_idx = len(components) - 1
    
    for i, comp in enumerate(components):
        is_last = (i == last_idx)
        if is_last and comp.endswith('.md'):
            continue
            
        if comp:
            new_comp = re.sub(r'^\d+\.', '', comp)
            new_components.append(new_comp)
            
    url = "/" + "/".join(new_components)
    if not url.endswith('/'):
        url += '/'
    return url

def fix_file(file_path):
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

IGNORE_CACHE = {}

def get_ignore_patterns(dir_path):
    if dir_path in IGNORE_CACHE:
        return IGNORE_CACHE[dir_path]
    
    ignore_path = os.path.join(dir_path, '.linterignore')
    patterns = []
    if os.path.exists(ignore_path):
        with open(ignore_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    patterns.append(line)
    IGNORE_CACHE[dir_path] = patterns
    return patterns

def is_ignored(file_path, root_dir):
    current_dir = os.path.dirname(os.path.abspath(file_path))
    root_dir_abs = os.path.abspath(root_dir)
    
    while current_dir.startswith(root_dir_abs):
        patterns = get_ignore_patterns(current_dir)
        if patterns:
            rel_path = os.path.relpath(file_path, current_dir).replace('\\', '/')
            for pattern in patterns:
                if fnmatch.fnmatch(rel_path, pattern) or fnmatch.fnmatch(rel_path.split('/')[-1], pattern):
                    return True
                path_parts = rel_path.split('/')
                for i in range(len(path_parts)):
                    if fnmatch.fnmatch('/'.join(path_parts[:i+1]), pattern):
                        return True
        if current_dir == root_dir_abs:
            break
        parent = os.path.dirname(current_dir)
        if parent == current_dir:
            break
        current_dir = parent
    return False

def validate_file(file_path, valid_production_paths, content_dir, anchor_cache):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    source_url = map_file_to_url(file_path, content_dir)
    
    issues = []
    for match in LINK_REGEX.finditer(content):
        raw_link = match.group('link')
        
        fixed_link = process_link(raw_link)
        if raw_link != fixed_link:
            if raw_link.rstrip('/') != fixed_link.rstrip('/'):
                issues.append(f"Improper format: '{raw_link}' -> expected '{fixed_link}'")
            
        # Parse link components
        parsed_link = urllib.parse.urlparse(fixed_link)
        clean_link = urllib.parse.unquote(parsed_link.path)
        anchor = urllib.parse.unquote(parsed_link.fragment)
        
        # Skip external links and assets
        if parsed_link.scheme in ('http', 'https', 'mailto', 'data') or fixed_link.startswith('//'):
            continue
        if clean_link.lower().endswith(ASSET_EXTENSIONS):
            continue
            
        # Determine the resolved base URL
        if clean_link == '':
            resolved_url = source_url
        else:
            resolved_url = posixpath.normpath(posixpath.join(source_url, clean_link))
            if fixed_link.split('#')[0].split('?')[0].endswith('/') or clean_link == '.' or clean_link == '..':
                if not resolved_url.endswith('/'):
                    resolved_url += '/'
        
        # Validate base URL
        resolved_url_no_slash = resolved_url.rstrip('/')
        target_file_path = None
        
        # We need to find the matching file path in valid_production_paths (ignoring trailing slash)
        for url, path in valid_production_paths.items():
            if url.rstrip('/') == resolved_url_no_slash:
                target_file_path = path
                break
                
        if not target_file_path:
            # We don't report an error if it's purely an anchor link and the source file isn't indexed (e.g. ignored file)
            if clean_link != '' or source_url in valid_production_paths:
                issues.append(f"Broken link: '{raw_link}' resolves to '{resolved_url}' which does not map to any markdown file.")
            continue
            
        # Validate Anchor
        if anchor:
            if target_file_path not in anchor_cache:
                anchor_cache[target_file_path] = extract_anchors(target_file_path)
                
            if anchor not in anchor_cache[target_file_path]:
                issues.append(f"Broken anchor: '#{anchor}' does not exist in {os.path.relpath(target_file_path, content_dir)}")
            
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
        
    current_dir = os.path.abspath(args.path)
    content_dir = None
    
    test_dir = current_dir if os.path.isdir(current_dir) else os.path.dirname(current_dir)
    while test_dir and test_dir != '/':
        if os.path.isdir(os.path.join(test_dir, 'content')):
            content_dir = os.path.join(test_dir, 'content')
            break
        if os.path.basename(test_dir) == 'content':
            content_dir = test_dir
            break
        test_dir = os.path.dirname(test_dir)
        
    if not content_dir:
        print("Warning: Could not find 'content' directory. URL validation might fail.")
        content_dir = current_dir if os.path.isdir(current_dir) else os.path.dirname(current_dir)
        
    repo_root = os.path.dirname(content_dir) if os.path.basename(content_dir) == 'content' else content_dir
                    
    files_to_process = []
    if os.path.isfile(args.path):
        if args.path.endswith(".md"):
            if not is_ignored(os.path.abspath(args.path), repo_root):
                files_to_process.append(args.path)
    else:
        for root, _, files in os.walk(args.path):
            for file in files:
                if file.endswith(".md"):
                    f_path = os.path.join(root, file)
                    if not is_ignored(f_path, repo_root):
                        files_to_process.append(f_path)
                    
    if args.command == "fix":
        fixed_count = 0
        for file_path in files_to_process:
            if fix_file(file_path):
                print(f"Fixed: {file_path}")
                fixed_count += 1
        print(f"Processed {len(files_to_process)} files. Fixed {fixed_count} files.")
        
    elif args.command == "validate":
        valid_production_paths = {}
        for root, _, files in os.walk(content_dir):
            for file in files:
                if file.endswith('.md'):
                    f_path = os.path.join(root, file)
                    if not is_ignored(f_path, repo_root):
                        url = map_file_to_url(f_path, content_dir)
                        valid_production_paths[url] = f_path
                        
        anchor_cache = {}
        all_issues = {}
        for file_path in files_to_process:
            issues = validate_file(file_path, valid_production_paths, content_dir, anchor_cache)
            if issues:
                all_issues[file_path] = issues
        
        if all_issues:
            print("Validation failed. The following files contain non-compliant or broken links:")
            for file_path, issues in all_issues.items():
                print(f"\n{file_path}:")
                for issue in issues:
                    print(f"  - {issue}")
            sys.exit(1)
        else:
            print("Validation successful: All local Markdown links are compliant and resolve to existing pages.")

if __name__ == "__main__":
    main()
