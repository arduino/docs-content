import os
import re
import sys
import argparse

# Regex for Markdown images: ![alt](link "title")
MD_IMAGE_REGEX = re.compile(r'!\[(?P<alt>[^\]]*)\]\((?P<link>[^"\'\)]+)(?P<title>\s+["\'][^"\']*["\'])?\)')
# Regex for HTML images: <img src="link" ...>
HTML_IMAGE_REGEX = re.compile(r'<img\s+[^>]*src=["\'](?P<link>[^"\']+)["\'][^>]*>')

IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp')

def find_images_in_file(file_path):
    images = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Find MD images
            for match in MD_IMAGE_REGEX.finditer(content):
                images.append(match.group('link'))
            # Find HTML images
            for match in HTML_IMAGE_REGEX.finditer(content):
                images.append(match.group('link'))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return images

def is_remote(link):
    return link.startswith(('http://', 'https://', 'mailto:', '//'))

def validate_missing(root_path):
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
                    
                    # Clean up query/anchor
                    img_path_clean = img.split('#')[0].split('?')[0]
                    
                    # Resolve path relative to markdown file
                    # Handle both relative and absolute-ish (starting with /)
                    if img_path_clean.startswith('/'):
                        # If it starts with /, it might be relative to the repo root or content root.
                        # Usually in these docs, they are relative. 
                        # Let's assume relative for now as per the example observed.
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
    assets = set()
    for root, _, files in os.walk(root_path):
        # Only consider files inside a directory named 'assets'
        if 'assets' in root.split(os.sep):
            for file in files:
                if file.lower().endswith(IMAGE_EXTENSIONS):
                    assets.add(os.path.normpath(os.path.join(root, file)))
    return assets

def main():
    parser = argparse.ArgumentParser(description="Validate and manage image links in Markdown files.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    subparsers.add_parser("validate", help="Run both validate-missing and validate-unlinked")
    subparsers.add_parser("validate-missing", help="Check for missing images referenced in MD files")
    subparsers.add_parser("validate-unlinked", help="Check for unlinked images in assets folders")
    subparsers.add_parser("remove-unlinked", help="Remove unlinked images from assets folders")
    
    parser.add_argument("path", help="Path to the content directory (e.g., content/software/app-lab)")
    
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
            print("Missing images found:")
            for file, imgs in missing.items():
                print(f"\n{os.path.relpath(file, root_path)}:")
                for img in imgs:
                    print(f"  - {img}")
            has_errors = True
        
        if unlinked:
            print("\nUnlinked images found in assets folders:")
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
            print("Missing images found:")
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
            print("Unlinked images found in assets folders:")
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
