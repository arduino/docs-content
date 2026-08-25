import os
import re
import sys
import argparse
import fnmatch

IGNORE_FILES = ['.lintignore', '.linterignore', '.alertlintignore']
IGNORE_CACHE = {}

ALERT_BLOCK_REGEX = re.compile(
    r"^(?P<indent>[ \t]*)<Alert(?P<attrs>[^>]*)>(?P<body>.*?)(?P<close_indent>[ \t]*)</Alert>",
    re.DOTALL | re.MULTILINE
)

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

def format_alert_block(indent, attrs, body, newline_char="\n"):
    """
    Formats an Alert block to guarantee empty lines after opening tag and before closing tag,
    while maintaining consistent indentation for nested list items.
    """
    body_lines = body.strip("\r\n").splitlines()
    non_empty = [l for l in body_lines if l.strip()]
    if not non_empty:
        return f"{indent}<Alert{attrs}>{newline_char}{newline_char}{indent}</Alert>"
    
    processed_lines = []
    for line in body_lines:
        line_str = line.rstrip()
        if not line_str.strip():
            processed_lines.append("")
        else:
            if indent and not line_str.startswith(indent):
                processed_lines.append(f"{indent}{line_str.lstrip()}")
            else:
                processed_lines.append(line_str)
                
    joined_body = newline_char.join(processed_lines)
    return f"{indent}<Alert{attrs}>{newline_char}{newline_char}{joined_body}{newline_char}{newline_char}{indent}</Alert>"

def process_file_content(content):
    """
    Scans content for Alert blocks and returns (new_content, is_modified, issues_list).
    """
    newline_char = "\r\n" if "\r\n" in content else "\n"
    issues = []
    
    def replacer(match):
        indent = match.group("indent")
        attrs = match.group("attrs")
        raw_body = match.group("body")
        close_indent = match.group("close_indent")
        
        formatted = format_alert_block(indent, attrs, raw_body, newline_char)
        original_block = match.group(0)
        
        if formatted != original_block:
            start_pos = match.start()
            line_no = content[:start_pos].count('\n') + 1
            issues.append({
                "line": line_no,
                "current": original_block.strip()[:80],
            })
            return formatted
        return original_block

    new_content = ALERT_BLOCK_REGEX.sub(replacer, content)
    return new_content, new_content != content, issues

def main():
    parser = argparse.ArgumentParser(
        description="Validate and format MDX <Alert> tags with required empty lines and consistent indentation."
    )
    parser.add_argument("command_or_path", nargs="?", default="validate", help="Command ('validate' or 'fix') or path to check.")
    parser.add_argument("path", nargs="?", default=None, help="Target file or directory path (default: content).")
    parser.add_argument("--fix", action="store_true", help="Automatically format and fix invalid Alert blocks.")

    args = parser.parse_args()

    # Normalize positional arguments
    if args.command_or_path in ["validate", "fix"]:
        command = args.command_or_path
        target_path_arg = args.path or "content"
    else:
        command = "fix" if args.fix else "validate"
        target_path_arg = args.command_or_path or "content"

    if args.fix:
        command = "fix"

    target_path = os.path.abspath(target_path_arg)
    if not os.path.exists(target_path):
        print(f"Error: Path '{target_path_arg}' does not exist.")
        sys.exit(1)

    current_dir = target_path
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

    files_to_check = []
    if os.path.isfile(target_path):
        if target_path.endswith(('.md', '.mdx')) and not is_ignored(target_path, repo_root):
            files_to_check.append(target_path)
    else:
        for root, _, files in os.walk(target_path):
            if is_ignored(root, repo_root):
                continue
            for file in files:
                if file.endswith(('.md', '.mdx')):
                    f_path = os.path.join(root, file)
                    if not is_ignored(f_path, repo_root):
                        files_to_check.append(f_path)

    if not files_to_check:
        print("No Markdown files found to check.")
        sys.exit(0)

    total_files_with_alerts = 0
    files_with_issues = {}
    fixed_files = 0

    for file_path in files_to_check:
        try:
            with open(file_path, 'r', encoding='utf-8', newline='') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue

        if "<Alert" in content:
            total_files_with_alerts += 1
            new_content, is_modified, issues = process_file_content(content)
            if is_modified:
                files_with_issues[file_path] = issues
                if command == "fix":
                    try:
                        with open(file_path, 'w', encoding='utf-8', newline='') as f:
                            f.write(new_content)
                        fixed_files += 1
                    except Exception as e:
                        print(f"Error writing {file_path}: {e}")

    rel_root = os.path.relpath(target_path, os.getcwd()) if os.path.isabs(target_path) else target_path

    if command == "fix":
        if fixed_files > 0:
            print(f"Successfully formatted Alert blocks in {fixed_files} file(s).")
        else:
            print(f"All Alert blocks in {len(files_to_check)} files are properly formatted.")
        sys.exit(0)
    else:
        if files_with_issues:
            total_issues = sum(len(iss) for iss in files_with_issues.values())
            print(f"❌ Found {total_issues} improperly formatted Alert block(s) in {len(files_with_issues)} file(s):\n")
            for f_path, issues in files_with_issues.items():
                rel_f = os.path.relpath(f_path, repo_root)
                print(f"{rel_f}:")
                for iss in issues:
                    print(f"  - Line {iss['line']}: Alert block missing empty lines or proper indentation: {iss['current']}...")
                print()
            print("Run `python3 scripts/validation/alert_tags/alert_tags.py fix` to format them automatically.")
            sys.exit(1)
        else:
            print(f"Validation successful: {total_files_with_alerts} files with Alert blocks checked, all comply with empty line and indentation requirements.")
            sys.exit(0)

if __name__ == "__main__":
    main()
