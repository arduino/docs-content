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

# docs.arduino.cc itself: with --absolute, links to it are checked like root-relative links (offline, never fetched)
DOCS_HOSTS = ('docs.arduino.cc',)

# Site sections served by other systems (one path prefix per line, '#' comments): no Markdown here maps to them, so
# links into them aren't checked, only counted.
EXTERNAL_SECTIONS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'external-sections.txt')

IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')
ASSET_EXTENSIONS = IMAGE_EXTENSIONS + ('.pdf', '.zip', '.stl', '.sh', '.eim', '.bin', '.gz', '.tar', '.ino', '.py', '.tflite', '.npy')

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
    hardware_match = re.match(r'^hardware/(?:[^/]+/)+([^/]+)/tutorials/(?:.+/)?([^/]+)/[^/]+\.md$', rel_path)
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

IGNORE_FILES = ['.lintignore', '.linterignore', '.linklintignore']
IGNORE_CACHE = {}

def get_ignore_patterns(dir_path):
    if dir_path in IGNORE_CACHE:
        return IGNORE_CACHE[dir_path]
    
    patterns = []
    for fname in IGNORE_FILES:
        ignore_path = os.path.join(dir_path, fname)
        if os.path.exists(ignore_path):
            with open(ignore_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        patterns.append(line)
    IGNORE_CACHE[dir_path] = patterns
    return patterns

def is_ignored(path, repo_root):
    abs_path = os.path.abspath(path)
    root_dir_abs = os.path.abspath(repo_root)
    
    test_dir = abs_path if os.path.isdir(abs_path) else os.path.dirname(abs_path)
    while test_dir.startswith(root_dir_abs):
        patterns = get_ignore_patterns(test_dir)
        if patterns:
            rel_path = os.path.relpath(abs_path, test_dir).replace('\\', '/')
            for pattern in patterns:
                clean_p = pattern.strip().replace('\\', '/').rstrip('/')
                if fnmatch.fnmatch(rel_path, clean_p) or fnmatch.fnmatch(rel_path, clean_p + '/*') or fnmatch.fnmatch(rel_path, clean_p + '/**'):
                    return True
                if rel_path == clean_p or rel_path.startswith(clean_p + '/'):
                    return True
                parts = rel_path.split('/')
                for i in range(len(parts)):
                    sub = '/'.join(parts[:i+1])
                    if sub == clean_p or fnmatch.fnmatch(sub, clean_p):
                        return True
        if test_dir == root_dir_abs:
            break
        parent = os.path.dirname(test_dir)
        if parent == test_dir:
            break
        test_dir = parent
    return False

def find_content_dir(path):
    current_dir = os.path.abspath(path)
    test_dir = current_dir if os.path.isdir(current_dir) else os.path.dirname(current_dir)
    while test_dir:
        if os.path.isdir(os.path.join(test_dir, 'content')):
            return os.path.join(test_dir, 'content')
        if os.path.basename(test_dir) == 'content':
            return test_dir
        parent = os.path.dirname(test_dir)
        if parent == test_dir:
            break
        test_dir = parent
    return None

def validate_file(file_path, valid_production_paths, content_dir, anchor_cache, scope=None, absolute=False, sections=()):
    """Issues for one file. `scope` (a dict) counts every link by what was done with it: relative and absolute links
    to the docs that were checked, absolute ones left unchecked (no --absolute), links to other hosts (never fetched),
    links into sections other systems serve, and assets."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    source_url = map_file_to_url(file_path, content_dir)
    scope = scope if scope is not None else {}
    count = lambda k: scope.__setitem__(k, scope.get(k, 0) + 1)
    
    issues = []
    for match in LINK_REGEX.finditer(content):
        raw_link = match.group('link').strip()
        
        # an absolute link to the docs site: with --absolute, checked as the root-relative path it names
        docs_url = urllib.parse.urlparse(raw_link)
        if docs_url.scheme in ('http', 'https') and docs_url.netloc in DOCS_HOSTS:
            if not absolute:
                count('absolute docs links (not checked; --absolute checks them)')
                continue
            path = docs_url.path or '/'
            if path.lower().endswith(ASSET_EXTENSIONS):
                count('assets')
                continue
            if is_external_section(path, sections):
                count('served by another system (not checked)')
                continue
            count('absolute docs links checked')
            target = path.rstrip('/') or '/'
            files = next((v for u, v in valid_production_paths.items() if u.rstrip('/') == target), None)
            if not files:
                issues.append(f"Broken link: '{raw_link}' resolves to '{path}' which does not map to any markdown file.")
            elif docs_url.fragment:
                anchor = urllib.parse.unquote(docs_url.fragment)
                if not any(anchor in anchor_cache.setdefault(f, extract_anchors(f)) for f in files):
                    issues.append(f"Broken anchor: '#{anchor}' does not exist in {os.path.relpath(files[0], content_dir)}")
            continue
        
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
            count('other hosts (never fetched)' if parsed_link.scheme in ('http', 'https') or fixed_link.startswith('//') else 'mailto and data links')
            continue
        if clean_link.lower().endswith(ASSET_EXTENSIONS):
            count('assets')
            continue
            
        # Determine the resolved base URL
        if clean_link == '':
            resolved_url = source_url
        else:
            resolved_url = posixpath.normpath(posixpath.join(source_url, clean_link))
            if fixed_link.split('#')[0].split('?')[0].endswith('/') or clean_link == '.' or clean_link == '..':
                if not resolved_url.endswith('/'):
                    resolved_url += '/'
        
        if is_external_section(resolved_url, sections):
            count('served by another system (not checked)')
            continue
        count('relative links checked')

        # Validate base URL
        resolved_url_no_slash = resolved_url.rstrip('/')
        target_file_paths = []
        
        if clean_link == '':
            target_file_paths = [file_path]
        else:
            # We need to find the matching file path in valid_production_paths (ignoring trailing slash)
            for url, path_entry in valid_production_paths.items():
                if url.rstrip('/') == resolved_url_no_slash:
                    if isinstance(path_entry, list):
                        target_file_paths = path_entry
                    else:
                        target_file_paths = [path_entry]
                    break
                
        if not target_file_paths:
            # We don't report an error if it's purely an anchor link and the source file isn't indexed (e.g. ignored file)
            if clean_link != '' or source_url in valid_production_paths:
                issues.append(f"Broken link: '{raw_link}' resolves to '{resolved_url}' which does not map to any markdown file.")
            continue
            
        # Validate Anchor
        if anchor:
            found = False
            for target_file in target_file_paths:
                if target_file not in anchor_cache:
                    anchor_cache[target_file] = extract_anchors(target_file)
                if anchor in anchor_cache[target_file]:
                    found = True
                    break
            if not found:
                target_desc = os.path.relpath(target_file_paths[0], content_dir) if len(target_file_paths) == 1 else resolved_url
                issues.append(f"Broken anchor: '#{anchor}' does not exist in {target_desc}")
            
    return issues

def load_external_sections(path=EXTERNAL_SECTIONS_FILE):
    """Path prefixes (no trailing slash) of site sections other systems serve."""
    if not os.path.exists(path):
        return ()
    with open(path, 'r', encoding='utf-8') as f:
        return tuple(l.split('#')[0].strip().rstrip('/') for l in f if l.split('#')[0].strip())

def is_external_section(url, sections):
    u = url.split('#')[0].split('?')[0].rstrip('/')
    return any(u == s or u.startswith(s + '/') for s in sections)

def build_route_map(content_dir):
    """
    Crawls content_dir to build a mapping of production URLs to lists of file paths.
    All Markdown files (including those in ignored folders) are indexed so active
    pages can link to them. Symlinked folders are followed: a tutorial shared between
    products (e.g. hardware/.../nano-33-ble/tutorials/getting-started-omv -> the Nano
    generic one) is published under each product's URL.
    """
    valid_production_paths = {}
    for root, dirs, files in os.walk(content_dir, followlinks=True):
        real = os.path.realpath(root)
        # never follow a symlink back into a folder we're already inside (a loop)
        dirs[:] = [d for d in dirs if not (real + os.sep).startswith(os.path.realpath(os.path.join(root, d)) + os.sep)]
        for file in files:
            if file.endswith('.md'):
                f_path = os.path.join(root, file)
                url = map_file_to_url(f_path, content_dir)
                if url not in valid_production_paths:
                    valid_production_paths[url] = []
                valid_production_paths[url].append(f_path)
    return valid_production_paths

def main(argv=None):
    parser = argparse.ArgumentParser(description="Manage relative links in Markdown files.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    fix_parser = subparsers.add_parser("fix")
    fix_parser.add_argument("path", help="Path to a file or directory")
    
    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("path", help="Path to a file or directory")
    validate_parser.add_argument("--absolute", action="store_true",
                                 help="Also check absolute links to docs.arduino.cc, against the same route map (offline)")
    
    args = parser.parse_args(argv)
    
    if not os.path.exists(args.path):
        print(f"Error: Path '{args.path}' does not exist.")
        sys.exit(1)
        
    current_dir = os.path.abspath(args.path)
    content_dir = find_content_dir(current_dir)
        
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
        valid_production_paths = build_route_map(content_dir)
                        
        anchor_cache = {}
        all_issues = {}
        scope = {}
        sections = load_external_sections()
        for file_path in files_to_process:
            issues = validate_file(file_path, valid_production_paths, content_dir, anchor_cache, scope, args.absolute, sections)
            if issues:
                all_issues[file_path] = issues
        print("Scope: " + "; ".join(f"{k}: {v}" for k, v in sorted(scope.items())))
        
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
