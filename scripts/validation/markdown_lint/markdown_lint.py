import os
import sys
import subprocess
import argparse
import fnmatch
import tempfile

IGNORE_FILES = ['.lintignore', '.linterignore', '.markdownlintignore']
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

def get_base_config(repo_root):
    repo_root_abs = os.path.abspath(repo_root)
    # Check content/.markdownlint.yaml first, then repo root .markdownlint.yaml
    candidates = [
        os.path.join(repo_root_abs, 'content', '.markdownlint.yaml'),
        os.path.join(repo_root_abs, 'content', '.markdownlint.yml'),
        os.path.join(repo_root_abs, '.markdownlint.yaml'),
        os.path.join(repo_root_abs, '.markdownlint.yml'),
    ]
    for cand in candidates:
        if os.path.exists(cand):
            return cand
    return None

def find_closest_config(file_path, repo_root):
    curr = os.path.dirname(os.path.abspath(file_path))
    repo_root_abs = os.path.abspath(repo_root)
    while curr.startswith(repo_root_abs):
        for config_name in ['.markdownlint.yaml', '.markdownlint.yml', '.markdownlint.json', '.markdownlint.jsonc']:
            cand = os.path.join(curr, config_name)
            if os.path.exists(cand):
                return cand
        if curr == repo_root_abs:
            break
        parent = os.path.dirname(curr)
        if parent == curr:
            break
        curr = parent
    return get_base_config(repo_root)

def prepare_effective_config(cfg_path, repo_root):
    if not cfg_path:
        return None, False
    base_config = get_base_config(repo_root)
    
    # If the config is already the base config, or base config doesn't exist, use as-is
    if not base_config or os.path.abspath(cfg_path) == os.path.abspath(base_config):
        return cfg_path, False
        
    try:
        with open(cfg_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # If it already extends a config, leave it as-is
        if 'extends:' in content or '"extends"' in content:
            return cfg_path, False
            
        # Prepend extends from base config so local config acts as an incremental override
        with tempfile.NamedTemporaryFile('w', suffix='.yaml', delete=False) as tf:
            tf.write(f'extends: "{base_config}"\n\n{content}\n')
            return tf.name, True
    except Exception:
        return cfg_path, False

def main():
    parser = argparse.ArgumentParser(description="Validate Markdown files using markdownlint with .linterignore and hierarchical configs.")
    parser.add_argument("path", nargs="?", default="content", help="Path to a file or directory to lint (default: content)")
    parser.add_argument("--fix", action="store_true", help="Automatically fix fixable markdownlint issues.")
    
    args = parser.parse_args()
    target_path = os.path.abspath(args.path)
    
    if not os.path.exists(target_path):
        print(f"Error: Path '{args.path}' does not exist.")
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

    files_to_lint = []
    if os.path.isfile(target_path):
        if target_path.endswith('.md') and not is_ignored(target_path, repo_root):
            files_to_lint.append(target_path)
    else:
        for root, _, files in os.walk(target_path):
            if is_ignored(root, repo_root):
                continue
            for file in files:
                if file.endswith('.md'):
                    f_path = os.path.join(root, file)
                    if not is_ignored(f_path, repo_root):
                        files_to_lint.append(f_path)
                        
    if not files_to_lint:
        print("No Markdown files to lint.")
        sys.exit(0)
        
    configs_map = {}
    for f in files_to_lint:
        cfg = find_closest_config(f, repo_root)
        configs_map.setdefault(cfg, []).append(f)
        
    has_errors = False
    for cfg, f_list in configs_map.items():
        effective_cfg, is_temp = prepare_effective_config(cfg, repo_root)
        try:
            cmd = ['npx', 'markdownlint-cli'] + f_list
            if effective_cfg:
                cmd.extend(['--config', effective_cfg])
            if args.fix:
                cmd.append('--fix')
                
            result = subprocess.run(cmd, text=True)
            if result.returncode != 0:
                has_errors = True
        finally:
            if is_temp and effective_cfg and os.path.exists(effective_cfg):
                os.remove(effective_cfg)
            
    if has_errors:
        sys.exit(1)
    else:
        print(f"Validation successful: {len(files_to_lint)} Markdown files checked with 0 errors.")

if __name__ == "__main__":
    main()
