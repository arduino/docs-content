import os
import re
import sys
import argparse

MARKDOWNLINT_RULES_DOC = "https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md"
DAVID_ANSON_RULES_DOC = "https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md"

# Standard rule definitions for markdownlint
STANDARD_RULES = {
    "MD001": ("heading-increment", "Heading levels should only increment by one level at a time."),
    "MD002": ("first-heading-h1", "First heading should be a top-level heading."),
    "MD003": ("heading-style", "Consistent ATX heading style (`# Heading`)."),
    "MD004": ("ul-style", "Unordered list bullet style enforcement."),
    "MD005": ("list-indent", "Inconsistent indentation for list items at the same level."),
    "MD006": ("ul-start-left", "Bullet lists start at the beginning of the line."),
    "MD007": ("ul-indent", "Consistent unordered list indentation (2 spaces)."),
    "MD009": ("no-trailing-spaces", "Trailing spaces forbidden."),
    "MD010": ("no-hard-tabs", "Hard tabs forbidden; spaces enforced everywhere including code blocks."),
    "MD011": ("no-reversed-links", "Reversed link syntax `(text)[url]` forbidden."),
    "MD012": ("no-multiple-blanks", "Multiple consecutive blank lines forbidden."),
    "MD013": ("line-length", "Line length limit."),
    "MD014": ("commands-show-output", "Dollar signs before terminal commands without showing output."),
    "MD018": ("no-missing-space-atx", "Space required after `#` in ATX headings."),
    "MD019": ("no-multiple-space-atx", "Multiple spaces after `#` in ATX headings forbidden."),
    "MD020": ("no-missing-space-closed-atx", "Space required inside closed ATX headings."),
    "MD021": ("no-multiple-space-closed-atx", "Multiple spaces inside closed ATX headings forbidden."),
    "MD022": ("blanks-around-headings", "Headings must be surrounded by blank lines."),
    "MD023": ("heading-start-left", "Headings must start at the beginning of the line."),
    "MD024": ("no-duplicate-heading", "Multiple headings with the same content within the same section."),
    "MD025": ("single-title", "Single top-level heading (`# Title`) per document."),
    "MD026": ("no-trailing-punctuation", "Trailing punctuation in heading."),
    "MD027": ("no-multiple-space-blockquote", "Multiple spaces after blockquote `>` forbidden."),
    "MD028": ("no-blanks-blockquote", "Blank lines inside blockquotes forbidden."),
    "MD029": ("ol-prefix", "Ordered list item prefix."),
    "MD030": ("list-marker-space", "Consistent spacing after list markers."),
    "MD031": ("blanks-around-fences", "Fenced code blocks surrounded by blank lines."),
    "MD032": ("blanks-around-lists", "Lists must be surrounded by blank lines."),
    "MD033": ("no-inline-html", "Inline HTML restrictions."),
    "MD034": ("no-bare-urls", "Bare URLs must use link formatting `[text](url)` or `<url>`."),
    "MD035": ("hr-style", "Consistent horizontal rule style (`---`)."),
    "MD036": ("no-emphasis-as-heading", "Emphasis used instead of a heading."),
    "MD037": ("no-space-in-emphasis", "Spaces inside emphasis markers (`* text *`) forbidden."),
    "MD038": ("no-space-in-code", "Spaces inside code span elements (`` ` code ` ``) forbidden."),
    "MD039": ("no-space-in-links", "Spaces inside link text (`[ text ](url)`) forbidden."),
    "MD040": ("fenced-code-language", "Fenced code blocks must specify an explicit language identifier."),
    "MD041": ("first-line-heading", "First line of document must be a top-level heading."),
    "MD042": ("no-empty-links", "Empty link targets (`[]()`) forbidden."),
    "MD043": ("required-headings", "Required heading structure."),
    "MD044": ("proper-names", "Proper name capitalization consistency."),
    "MD045": ("no-alt-text", "Images must provide descriptive alternative text."),
    "MD046": ("code-block-style", "Consistent code block style (fenced)."),
    "MD047": ("single-trailing-newline", "Files must end with a single newline character."),
    "MD048": ("code-fence-style", "Consistent code fence style (backticks)."),
    "MD049": ("emphasis-style", "Consistent emphasis style (`*italic*`)."),
    "MD050": ("strong-style", "Consistent strong emphasis style (`**bold**`)."),
    "MD060": ("table-column-style", "Table column style and alignment enforcement."),
}

RULE_DOC_LINKS = {
    "MD001": f"{MARKDOWNLINT_RULES_DOC}#md001---header-levels-should-only-increment-by-one-level-at-a-time",
    "MD002": f"{MARKDOWNLINT_RULES_DOC}#md002---first-header-should-be-a-top-level-header",
    "MD003": f"{MARKDOWNLINT_RULES_DOC}#md003---header-style",
    "MD004": f"{MARKDOWNLINT_RULES_DOC}#md004---unordered-list-style",
    "MD005": f"{MARKDOWNLINT_RULES_DOC}#md005---inconsistent-indentation-for-list-items-at-the-same-level",
    "MD006": f"{MARKDOWNLINT_RULES_DOC}#md006---consider-starting-bulleted-lists-at-the-beginning-of-the-line",
    "MD007": f"{MARKDOWNLINT_RULES_DOC}#md007---unordered-list-indentation",
    "MD009": f"{MARKDOWNLINT_RULES_DOC}#md009---trailing-spaces",
    "MD010": f"{MARKDOWNLINT_RULES_DOC}#md010---hard-tabs",
    "MD011": f"{MARKDOWNLINT_RULES_DOC}#md011---reversed-link-syntax",
    "MD012": f"{MARKDOWNLINT_RULES_DOC}#md012---multiple-consecutive-blank-lines",
    "MD013": f"{MARKDOWNLINT_RULES_DOC}#md013---line-length",
    "MD014": f"{MARKDOWNLINT_RULES_DOC}#md014---dollar-signs-used-before-commands-without-showing-output",
    "MD018": f"{MARKDOWNLINT_RULES_DOC}#md018---no-space-after-hash-on-atx-style-header",
    "MD019": f"{MARKDOWNLINT_RULES_DOC}#md019---multiple-spaces-after-hash-on-atx-style-header",
    "MD020": f"{MARKDOWNLINT_RULES_DOC}#md020---no-space-inside-hashes-on-closed-atx-style-header",
    "MD021": f"{MARKDOWNLINT_RULES_DOC}#md021---multiple-spaces-inside-hashes-on-closed-atx-style-header",
    "MD022": f"{MARKDOWNLINT_RULES_DOC}#md022---headers-should-be-surrounded-by-blank-lines",
    "MD023": f"{MARKDOWNLINT_RULES_DOC}#md023---headers-must-start-at-the-beginning-of-the-line",
    "MD024": f"{MARKDOWNLINT_RULES_DOC}#md024---multiple-headers-with-the-same-content",
    "MD025": f"{MARKDOWNLINT_RULES_DOC}#md025---multiple-top-level-headers-in-the-same-document",
    "MD026": f"{MARKDOWNLINT_RULES_DOC}#md026---trailing-punctuation-in-header",
    "MD027": f"{MARKDOWNLINT_RULES_DOC}#md027---multiple-spaces-after-blockquote-symbol",
    "MD028": f"{MARKDOWNLINT_RULES_DOC}#md028---blank-line-inside-blockquote",
    "MD029": f"{MARKDOWNLINT_RULES_DOC}#md029---ordered-list-item-prefix",
    "MD030": f"{MARKDOWNLINT_RULES_DOC}#md030---spaces-after-list-markers",
    "MD031": f"{MARKDOWNLINT_RULES_DOC}#md031---fenced-code-blocks-should-be-surrounded-by-blank-lines",
    "MD032": f"{MARKDOWNLINT_RULES_DOC}#md032---lists-should-be-surrounded-by-blank-lines",
    "MD033": f"{MARKDOWNLINT_RULES_DOC}#md033---inline-html",
    "MD034": f"{MARKDOWNLINT_RULES_DOC}#md034---bare-url-used",
    "MD035": f"{MARKDOWNLINT_RULES_DOC}#md035---horizontal-rule-style",
    "MD036": f"{MARKDOWNLINT_RULES_DOC}#md036---emphasis-used-instead-of-a-header",
    "MD037": f"{MARKDOWNLINT_RULES_DOC}#md037---spaces-inside-emphasis-markers",
    "MD038": f"{MARKDOWNLINT_RULES_DOC}#md038---spaces-inside-code-span-elements",
    "MD039": f"{MARKDOWNLINT_RULES_DOC}#md039---spaces-inside-link-text",
    "MD040": f"{MARKDOWNLINT_RULES_DOC}#md040---fenced-code-blocks-should-have-a-language-specified",
    "MD041": f"{MARKDOWNLINT_RULES_DOC}#md041---first-line-in-file-should-be-a-top-level-header",
    "MD042": f"{DAVID_ANSON_RULES_DOC}#md042---no-empty-links",
    "MD043": f"{DAVID_ANSON_RULES_DOC}#md043---required-heading-structure",
    "MD044": f"{DAVID_ANSON_RULES_DOC}#md044---proper-names-should-have-the-correct-capitalization",
    "MD045": f"{DAVID_ANSON_RULES_DOC}#md045---images-should-have-alternate-text-alt-text",
    "MD046": f"{MARKDOWNLINT_RULES_DOC}#md046---code-block-style",
    "MD047": f"{MARKDOWNLINT_RULES_DOC}#md047---file-should-end-with-a-single-newline-character",
    "MD048": f"{DAVID_ANSON_RULES_DOC}#md048---code-fence-style",
    "MD049": f"{DAVID_ANSON_RULES_DOC}#md049---emphasis-style",
    "MD050": f"{DAVID_ANSON_RULES_DOC}#md050---strong-style",
    "MD060": f"{DAVID_ANSON_RULES_DOC}#md060---table-column-style",
}

DEFAULT_DESCRIPTIONS = {
    "MD004": "Unordered list bullet style enforcement disabled to permit both `-` and `*` bullet markers.",
    "MD010": "Hard tabs forbidden; spaces enforced everywhere including code blocks (`code_blocks: true`).",
    "MD013": "Line length limit disabled to prevent breaking long URLs, code samples, and technical prose.",
    "MD014": "Dollar signs before terminal commands permitted in tutorial code snippets.",
    "MD024": "Duplicate headings allowed across different parent sections (`siblings_only: true`).",
    "MD026": 'Trailing punctuation forbidden except question marks (`punctuation: ".,;:!。，；：！"`).',
    "MD029": 'Ordered lists accept either sequential (`1. 2. 3.`) or repeating (`1. 1. 1.`) prefixes (`style: "one_or_ordered"`).',
    "MD031": "Fenced code blocks immediately following list items permitted without extra blank lines (`list_items: false`).",
    "MD033": 'Inline HTML restricted; allowed elements: `<Alert>`, `<sup>`, `<sub>`, `<br>` (`allowed_elements`).',
    "MD036": "Standalone bold/italic emphasis lines permitted for custom layout styling.",
    "MD060": "Table column pipe alignment enforcement disabled to minimize diff churn on edits.",
}

def parse_yaml_fallback(content):
    """Simple fallback parser for .markdownlint.yaml if PyYAML is unavailable."""
    data = {}
    current_key = None
    current_dict = None
    
    for raw_line in content.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
            
        if raw_line.startswith("  ") and current_key and current_dict is not None:
            sub_line = line
            if ":" in sub_line:
                sk, sv = [x.strip() for x in sub_line.split(":", 1)]
                if sv.startswith("[") and sv.endswith("]"):
                    items = [x.strip().strip("'\"") for x in sv[1:-1].split(",") if x.strip()]
                    current_dict[sk] = items
                elif sv.lower() == "true":
                    current_dict[sk] = True
                elif sv.lower() == "false":
                    current_dict[sk] = False
                else:
                    current_dict[sk] = sv.strip("'\"")
            continue
            
        if ":" in line:
            k, v = [x.strip() for x in line.split(":", 1)]
            if not v:
                current_key = k
                current_dict = {}
                data[k] = current_dict
            else:
                current_key = None
                current_dict = None
                if v.lower() == "true":
                    data[k] = True
                elif v.lower() == "false":
                    data[k] = False
                elif v.startswith("[") and v.endswith("]"):
                    items = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
                    data[k] = items
                else:
                    data[k] = v.strip("'\"")
    return data

def load_rule_config(config_path):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")
        
    with open(config_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    try:
        import yaml
        return yaml.safe_load(content)
    except ImportError:
        return parse_yaml_fallback(content)

def get_custom_rules(rules_dir):
    rules = []
    if not os.path.isdir(rules_dir):
        return rules
        
    for fname in sorted(os.listdir(rules_dir)):
        if fname.endswith(".cjs") or fname.endswith(".js"):
            fpath = os.path.join(rules_dir, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                c = f.read()
            names_match = re.search(r'names:\s*\[(.*?)\]', c)
            desc_match = re.search(r'description:\s*["\'](.*?)["\']', c)
            if names_match:
                names = [n.strip().strip('"\'') for n in names_match.group(1).split(",") if n.strip()]
                primary_name = names[1] if len(names) > 1 and names[0].startswith("no-") and not names[1].startswith("MD") else names[0]
                alias = names[0] if primary_name != names[0] else (names[1] if len(names) > 1 else primary_name)
                desc = desc_match.group(1) if desc_match else "Custom validation rule"
                rules.append({
                    "id": primary_name,
                    "name": alias,
                    "description": desc,
                    "file": fname
                })
    return rules

def find_repo_root(start_path):
    curr = os.path.abspath(start_path)
    while curr and curr != os.path.dirname(curr):
        if os.path.exists(os.path.join(curr, "content", ".markdownlint.yaml")) or os.path.exists(os.path.join(curr, ".git")):
            return curr
        curr = os.path.dirname(curr)
    return os.path.abspath(start_path)

def format_rule_link(rule_id, custom_file=None):
    if custom_file:
        return f"[**{rule_id}**](rules/{custom_file})"
    link = RULE_DOC_LINKS.get(rule_id, f"{MARKDOWNLINT_RULES_DOC}#{rule_id.lower()}")
    return f"[**{rule_id}**]({link})"

def generate_rules_markdown(config, custom_rules):
    """Generates Markdown text for the active, disabled, and default rules tables."""
    lines = []
    lines.append("<!-- MARKDOWNLINT-RULES:START -->")
    lines.append("### Configured Active Rules & Customizations\n")
    lines.append("Rules with repository-specific configuration in `content/.markdownlint.yaml`:\n")
    lines.append("| Rule | Name | Status | Enforcement Details |")
    lines.append("| :--- | :--- | :--- | :--- |")

    # Configured rules
    configured = {k: v for k, v in config.items() if k.startswith("MD") and v is not False}
    for rule_id in sorted(configured.keys()):
        rule_name = STANDARD_RULES.get(rule_id, (rule_id, ""))[0]
        desc = DEFAULT_DESCRIPTIONS.get(rule_id, "")
        opts = configured[rule_id]
        if not desc:
            desc = f"Configured with options: `{opts}`"
        rule_link = format_rule_link(rule_id)
        lines.append(f"| {rule_link} | `{rule_name}` | Active | {desc} |")

    # Custom rules
    for cr in custom_rules:
        rule_link = format_rule_link(cr['id'], cr['file'])
        lines.append(f"| {rule_link} | `{cr['name']}` | Active (Custom) | {cr['description']}. Enforced via `rules/{cr['file']}`. |")

    lines.append("\n### Disabled Rules\n")
    lines.append("Rules explicitly disabled in `content/.markdownlint.yaml` (`false`):\n")
    lines.append("| Rule | Name | Status | Reason for Exemption |")
    lines.append("| :--- | :--- | :--- | :--- |")

    disabled = [k for k, v in config.items() if k.startswith("MD") and v is False]
    for rule_id in sorted(disabled):
        rule_name = STANDARD_RULES.get(rule_id, (rule_id, ""))[0]
        reason = DEFAULT_DESCRIPTIONS.get(rule_id, "Rule disabled for documentation content.")
        rule_link = format_rule_link(rule_id)
        lines.append(f"| {rule_link} | `{rule_name}` | Disabled (`false`) | {reason} |")

    lines.append("\n### Default Active Rules\n")
    lines.append("The baseline configuration enables all standard `markdownlint` rules by default (`default: true`), except those explicitly disabled above. Key enforced default rules include:\n")
    lines.append("| Rule | Name | Description |")
    lines.append("| :--- | :--- | :--- |")

    default_active = [k for k in sorted(STANDARD_RULES.keys()) if k not in disabled and k not in configured and k != "MD002"]
    for rule_id in default_active:
        rule_name, desc = STANDARD_RULES[rule_id]
        rule_link = format_rule_link(rule_id)
        lines.append(f"| {rule_link} | `{rule_name}` | {desc} |")

    lines.append("<!-- MARKDOWNLINT-RULES:END -->")
    return "\n".join(lines)

def parse_markdown_table_rows(lines):
    """Extracts table rows keyed by rule ID from a list of markdown lines."""
    rows = {}
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|") or stripped.startswith("| :") or stripped.startswith("| Rule"):
            continue
        cols = [c.strip() for c in stripped.split("|")[1:-1]]
        if cols:
            match = re.search(r'\[?\*\*?([a-zA-Z0-9_-]+)\*\*?\]?(?:\((.*?)\))?', cols[0])
            if match:
                rule_id = match.group(1)
                link = match.group(2) if match.lastindex >= 2 else None
                rows[rule_id] = {
                    "raw": stripped,
                    "columns": cols,
                    "link": link
                }
    return rows

def parse_readme_sections(readme_text):
    """Parses markdown text into sections by heading."""
    sections = {}
    current_sec = "header"
    for line in readme_text.splitlines():
        if line.startswith("### "):
            current_sec = line[4:].strip()
            sections[current_sec] = []
        elif line.startswith("## ") and current_sec != "header":
            current_sec = line[3:].strip()
            sections[current_sec] = []
        else:
            sections.setdefault(current_sec, []).append(line)
    return sections

def validate_readme_content(config_path, readme_path, rules_dir):
    """
    Validates that README.md accurately reflects the rule configuration.
    Returns (is_valid: bool, errors: list[str]).
    """
    errors = []
    
    if not os.path.exists(config_path):
        return False, [f"Rule configuration not found at '{config_path}'."]
    if not os.path.exists(readme_path):
        return False, [f"README.md not found at '{readme_path}'."]
        
    config = load_rule_config(config_path)
    custom_rules = get_custom_rules(rules_dir)
    
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_text = f.read()

    sections = parse_readme_sections(readme_text)

    # Locate the active, disabled, and default sections
    active_sec_lines = []
    disabled_sec_lines = []
    default_sec_lines = []
    for sec_name, lines in sections.items():
        if "configured active" in sec_name.lower() or "active rules" in sec_name.lower():
            active_sec_lines.extend(lines)
        elif "disabled" in sec_name.lower():
            disabled_sec_lines.extend(lines)
        elif "default active" in sec_name.lower():
            default_sec_lines.extend(lines)

    if not active_sec_lines:
        errors.append("README.md is missing an 'Active Rules' or 'Configured Active Rules' section.")
    if not disabled_sec_lines:
        errors.append("README.md is missing a 'Disabled Rules' section.")

    active_rows = parse_markdown_table_rows(active_sec_lines)
    disabled_rows = parse_markdown_table_rows(disabled_sec_lines)
    default_rows = parse_markdown_table_rows(default_sec_lines)

    disabled_rules_in_config = set(k for k, v in config.items() if k.startswith("MD") and v is False)
    configured_rules_in_config = set(k for k, v in config.items() if k.startswith("MD") and v is not False)
    custom_rule_ids = set(cr["id"] for cr in custom_rules)

    # Check 1: All disabled rules in config must appear in disabled table and NOT in active table
    for rule in disabled_rules_in_config:
        if rule not in disabled_rows:
            errors.append(f"Rule {rule} is disabled in .markdownlint.yaml (`false`) but missing from the Disabled Rules table in README.md.")
        if rule in active_rows:
            errors.append(f"Rule {rule} is disabled in .markdownlint.yaml (`false`) but appears in the Active Rules table in README.md.")
        if rule in default_rows:
            errors.append(f"Rule {rule} is disabled in .markdownlint.yaml (`false`) but appears in the Default Active Rules table in README.md.")

    # Check 2: All configured active rules in config must appear in active table and NOT in disabled table
    for rule in configured_rules_in_config:
        if rule not in active_rows:
            errors.append(f"Rule {rule} is configured in .markdownlint.yaml but missing from the Active Rules table in README.md.")
        if rule in disabled_rows:
            errors.append(f"Rule {rule} is active in .markdownlint.yaml but appears in the Disabled Rules table in README.md.")

    # Check 3: Every rule listed in disabled table must actually be disabled in .markdownlint.yaml
    for rule in disabled_rows:
        if rule not in disabled_rules_in_config:
            errors.append(f"Rule {rule} is listed as Disabled in README.md, but is NOT disabled in .markdownlint.yaml.")

    # Check 4: Check dynamic configuration options for configured rules
    for rule in configured_rules_in_config:
        if rule in active_rows:
            row_raw = active_rows[rule]["raw"]
            opts = config.get(rule)
            if isinstance(opts, dict):
                for opt_k, opt_v in opts.items():
                    if opt_k.lower() not in row_raw.lower():
                        errors.append(f"Rule {rule} documentation in README.md is missing expected configuration key: '{opt_k}'.")
                    if isinstance(opt_v, list):
                        for item in opt_v:
                            if str(item).lower() not in row_raw.lower():
                                errors.append(f"Rule {rule} documentation in README.md is missing expected element/option: '{item}'.")
                    elif isinstance(opt_v, str):
                        if opt_v.lower() not in row_raw.lower() and not any(part in row_raw for part in opt_v.split()):
                            errors.append(f"Rule {rule} documentation in README.md does not match configured option: '{opt_v}'.")

    # Check 5: Custom rules in rules/ must appear in active table
    for cr in custom_rules:
        cr_id = cr["id"]
        if cr_id not in active_rows:
            errors.append(f"Custom rule '{cr_id}' ({cr['file']}) is missing from the Active Rules table in README.md.")

    # Check 6: Check documentation link on all standard rules in tables
    all_table_rows = {**active_rows, **disabled_rows, **default_rows}
    for rule_id, rdata in all_table_rows.items():
        if rule_id.startswith("MD"):
            expected_link = RULE_DOC_LINKS.get(rule_id)
            actual_link = rdata.get("link")
            if not actual_link:
                errors.append(f"Rule {rule_id} in README.md is not linked. Expected link: '{expected_link}'.")
            elif expected_link and actual_link != expected_link:
                errors.append(f"Rule {rule_id} link in README.md is '{actual_link}', expected '{expected_link}'.")
        elif rule_id in custom_rule_ids:
            actual_link = rdata.get("link")
            if not actual_link or "rules/" not in actual_link:
                errors.append(f"Custom rule {rule_id} in README.md should link to its implementation file under rules/.")

    return (len(errors) == 0, errors)

def update_readme_rules(config_path, readme_path, rules_dir):
    config = load_rule_config(config_path)
    custom_rules = get_custom_rules(rules_dir)
    generated = generate_rules_markdown(config, custom_rules)
    
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "<!-- MARKDOWNLINT-RULES:START -->" in content and "<!-- MARKDOWNLINT-RULES:END -->" in content:
        pattern = re.compile(r"<!-- MARKDOWNLINT-RULES:START -->.*?<!-- MARKDOWNLINT-RULES:END -->", re.DOTALL)
        new_content = pattern.sub(generated, content)
    else:
        if "## Configuration & Ignores" in content:
            new_content = content.replace("## Configuration & Ignores", f"## Rules & Configuration\n\n{generated}\n\n## Configuration & Ignores")
        else:
            new_content = content + f"\n\n## Rules & Configuration\n\n{generated}\n"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"✓ Updated rule documentation in '{readme_path}' to match '{config_path}'.")

def main():
    parser = argparse.ArgumentParser(description="Validate that markdownlint README.md accurately reflects the rule configuration in .markdownlint.yaml.")
    parser.add_argument("--update", action="store_true", help="Automatically synchronize README.md rules table with .markdownlint.yaml")
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = find_repo_root(script_dir)
    
    config_path = os.path.join(repo_root, "content", ".markdownlint.yaml")
    readme_path = os.path.join(script_dir, "README.md")
    rules_dir = os.path.join(script_dir, "rules")

    if args.update:
        update_readme_rules(config_path, readme_path, rules_dir)
        sys.exit(0)

    is_valid, errors = validate_readme_content(config_path, readme_path, rules_dir)
    if not is_valid:
        print(f"❌ Markdownlint README validation failed ({len(errors)} errors found):")
        for err in errors:
            print(f"  - {err}")
        print("\nTip: Run 'python3 scripts/validation/markdownlint/validate_readme.py --update' to sync README.md automatically.")
        sys.exit(1)
    else:
        config = load_rule_config(config_path)
        configured_count = len([k for k, v in config.items() if k.startswith("MD") and v is not False])
        disabled_count = len([k for k, v in config.items() if k.startswith("MD") and v is False])
        custom_count = len(get_custom_rules(rules_dir))
        print(f"✓ Markdownlint README validation passed: rules documentation matches '{config_path}' ({configured_count} configured, {disabled_count} disabled, {custom_count} custom).")
        sys.exit(0)

if __name__ == "__main__":
    main()
