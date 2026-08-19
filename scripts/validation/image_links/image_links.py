import os
import re
import sys
import argparse
import urllib.parse
import fnmatch

# Regex for Markdown images: ![alt](link "title")
# Handles one level of nested parentheses in the link (e.g., for file paths like "image_(1).png").
MD_IMAGE_REGEX = re.compile(r'!\[(?P<alt>[^\]]*)\]\((?P<inner>(?:[^)(]|\([^)(]*\))*)\)')

# Regex for HTML images: <img src="link" ...>
HTML_IMAGE_REGEX = re.compile(r'<img\s+[^>]*src=["\'](?P<link>[^"\']+)["\'][^>]*>')

IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')

IGNORE_FILES = ['.lintignore', '.linterignore', '.imagelintignore']
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

def find_images_in_file(file_path):
    """
    Extracts all image links (both Markdown and HTML) from a given file.
    
    Args:
        file_path (str): The path to the Markdown file.
        
    Returns:
        list: A list of image link strings extracted from the file.
    """
    images = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Find Markdown images
            for match in MD_IMAGE_REGEX.finditer(content):
                inner = match.group('inner').strip()
                # Separate the link from any optional title wrapped in quotes
                link_match = re.match(r'^(.*?)(?:\s+["\'].*["\'])?$', inner)
                if link_match:
                    images.append(link_match.group(1).strip())
                    
            # Find HTML images
            for match in HTML_IMAGE_REGEX.finditer(content):
                images.append(match.group('link').strip())
                
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return images

def is_remote(link):
    """
    Checks if an image link is a remote URL or non-file URI.
    """
    return link.startswith(('http://', 'https://', 'mailto:', '//', 'data:'))

def validate_missing(root_path, repo_root):
    """
    Scans the given directory for Markdown files and checks if the local images they reference exist.
    
    Args:
        root_path (str): The root directory to scan.
        repo_root (str): The repository root containing .linterignore.
        
    Returns:
        tuple: (missing_images dict, referenced_images set)
            - missing_images: A dictionary mapping file paths to a list of broken image links.
            - referenced_images: A set of absolute paths to all existing referenced images.
    """
    missing_images = {}
    referenced_images = set()
    
    for root, _, files in os.walk(root_path):
        if is_ignored(root, repo_root):
            continue
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if is_ignored(file_path, repo_root):
                    continue
                images = find_images_in_file(file_path)
                
                for img in images:
                    if is_remote(img):
                        continue
                    
                    # Clean up queries/anchors and decode URL encoding (like %20 to spaces)
                    img_path_clean = urllib.parse.unquote(img.split('#')[0].split('?')[0])
                    
                    # Resolve path relative to the specific markdown file
                    if img_path_clean.startswith('/'):
                        full_img_path = os.path.normpath(os.path.join(root_path, img_path_clean.lstrip('/')))
                    else:
                        full_img_path = os.path.normpath(os.path.join(root, img_path_clean))
                    
                    referenced_images.add(full_img_path)
                    
                    if not os.path.exists(full_img_path):
                        if file_path not in missing_images:
                            missing_images[file_path] = []
                        missing_images[file_path].append(img)
                        
    return missing_images, referenced_images

def get_all_assets(root_path, repo_root):
    """
    Collects absolute paths for all image files located within any directory named 'assets'.
    
    Args:
        root_path (str): The root directory to scan.
        repo_root (str): The repository root containing .linterignore.
        
    Returns:
        set: A set of absolute paths to all found asset files.
    """
    assets = set()
    for root, _, files in os.walk(root_path):
        if is_ignored(root, repo_root):
            continue
        # Restrict the search to directories explicitly named 'assets'
        if 'assets' in root.split(os.sep):
            for file in files:
                if file.lower().endswith(IMAGE_EXTENSIONS):
                    asset_path = os.path.normpath(os.path.join(root, file))
                    if not is_ignored(asset_path, repo_root):
                        assets.add(asset_path)
    return assets

def main():
    parser = argparse.ArgumentParser(description="Validate and manage local image links in Markdown files.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    subparsers.add_parser("validate", help="Run both missing link and unlinked asset checks.")
    subparsers.add_parser("validate-missing", help="Check for broken image links referenced in Markdown files.")
    subparsers.add_parser("validate-unlinked", help="Check for orphaned images in 'assets' folders that are not referenced anywhere.")
    subparsers.add_parser("remove-unlinked", help="Delete orphaned images from 'assets' folders.")
    
    parser.add_argument("path", help="Path to the content directory to process (e.g., content/software/app-lab)")
    
    args = parser.parse_args()
    root_path = os.path.abspath(args.path)
    
    if not os.path.exists(root_path):
        print(f"Error: Path '{args.path}' does not exist.")
        sys.exit(1)
        
    current_dir = root_path
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
        
    repo_root = os.path.dirname(content_dir) if content_dir and os.path.basename(content_dir) == 'content' else (content_dir or current_dir)

    if args.command == "validate":
        missing, referenced = validate_missing(root_path, repo_root)
        assets = get_all_assets(root_path, repo_root)
        unlinked = assets - referenced
        
        has_errors = False
        if missing:
            total_missing = sum(len(imgs) for imgs in missing.values())
            print(f"{total_missing} missing images found:")
            for file, imgs in missing.items():
                print(f"\n{os.path.relpath(file, root_path)}:")
                for img in imgs:
                    print(f"  - {img}")
            has_errors = True
        
        if unlinked:
            print(f"\n{len(unlinked)} unlinked images found in assets folders:")
            for img in sorted(list(unlinked)):
                print(f"  - {os.path.relpath(img, root_path)}")
            has_errors = True
            
        if has_errors:
            sys.exit(1)
        else:
            print("Validation successful: No missing or unlinked images found.")

    elif args.command == "validate-missing":
        missing, _ = validate_missing(root_path, repo_root)
        if missing:
            total_missing = sum(len(imgs) for imgs in missing.values())
            print(f"{total_missing} missing images found:")
            for file, imgs in missing.items():
                print(f"\n{os.path.relpath(file, root_path)}:")
                for img in imgs:
                    print(f"  - {img}")
            has_errors = True
        else:
            print("No missing images found.")
            
    elif args.command == "validate-unlinked":
        _, referenced = validate_missing(root_path, repo_root)
        assets = get_all_assets(root_path, repo_root)
        unlinked = assets - referenced
        
        if unlinked:
            print(f"{len(unlinked)} unlinked images found in assets folders:")
            for img in sorted(list(unlinked)):
                print(f"  - {os.path.relpath(img, root_path)}")
            has_errors = True
        else:
            print("No unlinked images found in assets folders.")
            
    elif args.command == "remove-unlinked":
        _, referenced = validate_missing(root_path, repo_root)
        assets = get_all_assets(root_path, repo_root)
        unlinked = assets - referenced
        
        if unlinked:
            print(f"Removing {len(unlinked)} unlinked images...")
            for img in unlinked:
                try:
                    os.remove(img)
                    print(f"  Deleted: {os.path.relpath(img, root_path)}")
                except Exception as e:
                    print(f"  Error deleting {img}: {e}")
        else:
            print("No unlinked images to remove.")

if __name__ == "__main__":
    main()
