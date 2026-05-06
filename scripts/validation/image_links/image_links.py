import os
import re
import sys
import argparse
import urllib.parse

# Regex for Markdown images: ![alt](link "title")
# Handles one level of nested parentheses in the link (e.g., for file paths like "image_(1).png").
MD_IMAGE_REGEX = re.compile(r'!\[(?P<alt>[^\]]*)\]\((?P<inner>(?:[^)(]+|\([^)(]*\))+)\)')

# Regex for HTML images: <img src="link" ...>
HTML_IMAGE_REGEX = re.compile(r'<img\s+[^>]*src=["\'](?P<link>[^"\']+)["\'][^>]*>')

IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')

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

def validate_missing(root_path):
    """
    Scans the given directory for Markdown files and checks if the local images they reference exist.
    
    Args:
        root_path (str): The root directory to scan.
        
    Returns:
        tuple: (missing_images dict, referenced_images set)
            - missing_images: A dictionary mapping file paths to a list of broken image links.
            - referenced_images: A set of absolute paths to all existing referenced images.
    """
    missing_images = {}
    referenced_images = set()
    
    for root, _, files in os.walk(root_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
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

def get_all_assets(root_path):
    """
    Collects absolute paths for all image files located within any directory named 'assets'.
    
    Args:
        root_path (str): The root directory to scan.
        
    Returns:
        set: A set of absolute paths to all found asset files.
    """
    assets = set()
    for root, _, files in os.walk(root_path):
        # Restrict the search to directories explicitly named 'assets'
        if 'assets' in root.split(os.sep):
            for file in files:
                if file.lower().endswith(IMAGE_EXTENSIONS):
                    assets.add(os.path.normpath(os.path.join(root, file)))
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
        
    if args.command == "validate":
        missing, referenced = validate_missing(root_path)
        assets = get_all_assets(root_path)
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
        missing, _ = validate_missing(root_path)
        if missing:
            total_missing = sum(len(imgs) for imgs in missing.values())
            print(f"{total_missing} missing images found:")
            for file, imgs in missing.items():
                print(f"\n{os.path.relpath(file, root_path)}:")
                for img in imgs:
                    print(f"  - {img}")
            sys.exit(1)
        else:
            print("No missing images found.")
            
    elif args.command == "validate-unlinked":
        _, referenced = validate_missing(root_path)
        assets = get_all_assets(root_path)
        unlinked = assets - referenced
        
        if unlinked:
            print(f"{len(unlinked)} unlinked images found in assets folders:")
            for img in sorted(list(unlinked)):
                print(f"  - {os.path.relpath(img, root_path)}")
            sys.exit(1)
        else:
            print("No unlinked images found in assets folders.")
            
    elif args.command == "remove-unlinked":
        _, referenced = validate_missing(root_path)
        assets = get_all_assets(root_path)
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
