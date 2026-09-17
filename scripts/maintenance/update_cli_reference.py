import os
import re
import shutil
import subprocess
import sys

# --- Configuration ---
# Possible locations for the arduino-app-cli repository
DEFAULT_REPO_PATHS = [
    os.environ.get("ARDUINO_APP_CLI_DIR"),
    os.environ.get("APP_CLI_DIR"),
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../arduino-app-cli")),
    os.path.abspath("../arduino-app-cli"),
    os.path.expanduser("~/Documents/GitHub/arduino-app-cli"),
]

# The HTML comments to look for in your Markdown files
START_MARKER = "<!-- arduino-app-cli commands start -->"
END_MARKER = "<!-- arduino-app-cli commands end -->"

GO_GEN_CODE = """package main

import (
	"fmt"
	"os"
	"strings"

	"github.com/arduino/arduino-app-cli/cmd/arduino-app-cli/app"
	"github.com/arduino/arduino-app-cli/cmd/arduino-app-cli/brick"
	"github.com/arduino/arduino-app-cli/cmd/arduino-app-cli/completion"
	"github.com/arduino/arduino-app-cli/cmd/arduino-app-cli/config"
	"github.com/arduino/arduino-app-cli/cmd/arduino-app-cli/daemon"
	"github.com/arduino/arduino-app-cli/cmd/arduino-app-cli/model"
	"github.com/arduino/arduino-app-cli/cmd/arduino-app-cli/monitor"
	"github.com/arduino/arduino-app-cli/cmd/arduino-app-cli/properties"
	"github.com/arduino/arduino-app-cli/cmd/arduino-app-cli/system"
	"github.com/arduino/arduino-app-cli/cmd/arduino-app-cli/version"
	cfg "github.com/arduino/arduino-app-cli/internal/orchestrator/config"
	"github.com/spf13/cobra"
	"github.com/spf13/pflag"
)

func main() {
	configuration := cfg.Configuration{}
	clientVersion := "0.0.0-dev"

	rootCmd := &cobra.Command{
		Use:   "arduino-app-cli [subcommand]",
		Short: "A CLI to manage Arduino Apps",
	}

	var formatStr, logLevelStr string
	rootCmd.PersistentFlags().StringVar(&formatStr, "format", "text", "Output format (text, json, json-lines)")
	rootCmd.PersistentFlags().StringVar(&logLevelStr, "log-level", "error", "Set the log level (debug, info, warn, error)")

	rootCmd.AddCommand(
		app.NewAppCmd(configuration),
		brick.NewBrickCmd(configuration),
		completion.NewCompletionCommand(),
		daemon.NewDaemonCmd(configuration, clientVersion),
		properties.NewPropertiesCmd(configuration),
		config.NewConfigCmd(configuration),
		system.NewSystemCmd(configuration),
		version.NewVersionCmd(clientVersion),
		monitor.NewMonitorCmd(),
		model.NewModelCmd(configuration),
	)

	normalizeCommands(rootCmd)

	var sb strings.Builder

	sb.WriteString("## arduino-app-cli\\n\\n")

	usage := rootCmd.UseLine()
	if !strings.Contains(usage, "[subcommand]") {
		usage += " [subcommand]"
	}
	sb.WriteString("**Usage:**\\n")
	sb.WriteString(fmt.Sprintf("`%s`\\n\\n", usage))

	var rootSubs []string
	for _, sub := range rootCmd.Commands() {
		if sub.IsAvailableCommand() && !sub.IsAdditionalHelpTopicCommand() {
			anchor := strings.ReplaceAll(strings.ToLower(sub.Name()), " ", "-")
			rootSubs = append(rootSubs, fmt.Sprintf("* [%s](#%s)", sub.Name(), anchor))
		}
	}
	if len(rootSubs) > 0 {
		sb.WriteString("**Subcommands:**\\n\\n")
		for _, s := range rootSubs {
			sb.WriteString(s + "\\n")
		}
		sb.WriteString("\\n")
	}

	sb.WriteString("### Global Options\\n\\n")
	rootCmd.PersistentFlags().VisitAll(func(flag *pflag.Flag) {
		defaultVal := ""
		if flag.DefValue != "" {
			defaultVal = fmt.Sprintf(" (default %q)", flag.DefValue)
		}
		sb.WriteString(fmt.Sprintf("* `--%s`: %s%s\\n", flag.Name, flag.Usage, defaultVal))
	})
	sb.WriteString("\\n---\\n\\n")

	if err := writeCompactCmds(rootCmd, &sb); err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v\\n", err)
		os.Exit(1)
	}

	fmt.Print(sb.String())
}

func normalizeCommands(cmd *cobra.Command) {
	path := cmd.CommandPath()
	switch path {
	case "arduino-app-cli brick details":
		if cmd.Use == "details" {
			cmd.Use = "details <brick_id>"
		}
	case "arduino-app-cli model delete":
		if cmd.Use == "delete" {
			cmd.Use = "delete <model_id>"
		}
	case "arduino-app-cli completion":
		if strings.Contains(cmd.Use, "[bash|zsh|fish|powershell]") {
			cmd.Use = "completion <shell>"
		}
		if !strings.Contains(cmd.Long, "(bash, zsh, fish, powershell)") {
			cmd.Long = "Generates completion scripts for various shells (bash, zsh, fish, powershell)"
		}
	case "arduino-app-cli system network-mode":
		if strings.Contains(cmd.Use, "<enable|disable|status>") {
			cmd.Use = "network-mode <command>"
			cmd.Long = "Manage the network mode of the system. Commands: enable, disable, status."
		}
	}

	// Normalize plain argument identifiers to '<...>' format (e.g. app_path -> <app_path>)
	parts := strings.Split(cmd.Use, " ")
	if len(parts) > 1 {
		for i := 1; i < len(parts); i++ {
			switch parts[i] {
			case "app_path", "zip_path", "name":
				parts[i] = "<" + parts[i] + ">"
			case "board_name":
				parts[i] = "<name>"
			}
		}
		cmd.Use = strings.Join(parts, " ")
	}

	for _, child := range cmd.Commands() {
		normalizeCommands(child)
	}
}

func writeCompactCmds(cmd *cobra.Command, sb *strings.Builder) error {
	if cmd.HasParent() {
		title := cmd.CommandPath()
		if strings.HasPrefix(title, "arduino-app-cli ") {
			title = strings.TrimPrefix(title, "arduino-app-cli ")
		}
		if title == "arduino-app-cli" {
			title = "arduino-app-cli (root)"
		}

		sb.WriteString(fmt.Sprintf("## %s\\n\\n", title))

		desc := cmd.Long
		if desc == "" {
			desc = cmd.Short
		}
		if desc != "" {
			sb.WriteString(desc + "\\n\\n")
		}

		usage := cmd.UseLine()
		if cmd.HasSubCommands() && !strings.Contains(usage, "[subcommand]") {
			usage += " [subcommand]"
		}
		sb.WriteString("**Usage:**\\n")
		sb.WriteString(fmt.Sprintf("`%s`\\n\\n", usage))

		if cmd.HasSubCommands() {
			var subs []string
			for _, sub := range cmd.Commands() {
				if sub.IsAvailableCommand() && !sub.IsAdditionalHelpTopicCommand() {
					subPath := sub.CommandPath()
					if strings.HasPrefix(subPath, "arduino-app-cli ") {
						subPath = strings.TrimPrefix(subPath, "arduino-app-cli ")
					}
					anchor := strings.ReplaceAll(strings.ToLower(subPath), " ", "-")
					subs = append(subs, fmt.Sprintf("* [%s](#%s)", sub.Name(), anchor))
				}
			}
			if len(subs) > 0 {
				sb.WriteString("**Subcommands:**\\n\\n")
				for _, s := range subs {
					sb.WriteString(s + "\\n")
				}
				sb.WriteString("\\n")
			}
		}

		var localFlags []string
		cmd.LocalFlags().VisitAll(func(flag *pflag.Flag) {
			if flag.Name == "help" {
				return
			}

			shorthand := ""
			if flag.Shorthand != "" {
				shorthand = fmt.Sprintf("-%s, ", flag.Shorthand)
			}

			defaultVal := ""
			if flag.DefValue != "" && flag.DefValue != "false" && flag.DefValue != "[]" && flag.DefValue != "0" {
				defaultVal = fmt.Sprintf(" (default %q)", flag.DefValue)
			}

			localFlags = append(localFlags, fmt.Sprintf("* `%s--%s`: %s%s", shorthand, flag.Name, flag.Usage, defaultVal))
		})

		if len(localFlags) > 0 {
			sb.WriteString("**Options:**\\n\\n")
			for _, lf := range localFlags {
				sb.WriteString(lf + "\\n")
			}
			sb.WriteString("\\n")
		}

		if cmd.Example != "" {
			// Clean up any temporary build paths in example output
			example := cmd.Example
			lines := strings.Split(example, "\\n")
			for i, line := range lines {
				trimmed := strings.TrimSpace(line)
				if strings.Contains(trimmed, "completion bash") {
					parts := strings.SplitN(line, "completion bash", 2)
					lines[i] = "  arduino-app-cli completion bash" + parts[1]
				}
			}
			cleanExample := strings.Join(lines, "\\n")
			sb.WriteString("**Example:**\\n```text\\n" + cleanExample + "\\n```\\n\\n")
		}
	}

	for _, child := range cmd.Commands() {
		if !child.IsAvailableCommand() || child.IsAdditionalHelpTopicCommand() {
			continue
		}
		if err := writeCompactCmds(child, sb); err != nil {
			return err
		}
	}

	return nil
}
"""

def find_repo_dir():
    """Finds the root directory of the arduino-app-cli repository."""
    for path in DEFAULT_REPO_PATHS:
        if path and os.path.exists(path) and os.path.isdir(path):
            return path
    return None

def get_repo_ref(repo_dir):
    """Returns the current git tag or branch name for logging."""
    try:
        res = subprocess.run(
            ["git", "describe", "--tags", "--exact-match"],
            cwd=repo_dir, capture_output=True, text=True
        )
        if res.returncode == 0:
            return res.stdout.strip()
        res = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=repo_dir, capture_output=True, text=True
        )
        if res.returncode == 0:
            return res.stdout.strip()
    except Exception:
        pass
    return "unknown"

def build_markdown_reference():
    """Executes the Go cobra generator inside arduino-app-cli and returns Markdown."""
    repo_dir = find_repo_dir()
    if not repo_dir:
        print("Error: 'arduino-app-cli' repository directory not found.")
        return None

    ref = get_repo_ref(repo_dir)
    print(f"Using arduino-app-cli at: {repo_dir} (ref: {ref})")

    docgen_dir = os.path.join(repo_dir, "cmd", "_docgen")
    docgen_file = os.path.join(docgen_dir, "main.go")

    try:
        os.makedirs(docgen_dir, exist_ok=True)
        with open(docgen_file, "w", encoding="utf-8") as f:
            f.write(GO_GEN_CODE)

        res = subprocess.run(
            ["go", "run", "./cmd/_docgen"],
            cwd=repo_dir,
            capture_output=True,
            text=True
        )

        if res.returncode != 0:
            print(f"Error running docgen in {repo_dir}: {res.stderr}")
            return None

        content = res.stdout
        # Strip trailing blank lines
        while content.endswith("\n\n"):
            content = content[:-1]

        return content

    finally:
        if os.path.exists(docgen_dir):
            shutil.rmtree(docgen_dir, ignore_errors=True)

def inject_reference_into_markdown(reference_content):
    """Finds Markdown files with the appropriate wrappers and updates them."""
    if not reference_content:
        return False

    pattern = re.compile(rf"({START_MARKER}\n).*?(\n{END_MARKER})", re.DOTALL)
    updated_any = False

    search_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    for root, _, files in os.walk(search_root):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)

                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                if pattern.search(content):
                    updated_content = pattern.sub(rf"\1{reference_content}\2", content)

                    if content != updated_content:
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(updated_content)
                        print(f"✅ Successfully updated CLI reference in: {filepath}")
                    else:
                        print(f"⚡ No changes needed for: {filepath} (Reference is up to date)")
                    updated_any = True

    if not updated_any:
        print(f"Warning: No Markdown files found with markers '{START_MARKER}' and '{END_MARKER}'.")
    return updated_any

if __name__ == "__main__":
    print("Generating Arduino App CLI Markdown Reference...")
    ref_markdown = build_markdown_reference()

    if ref_markdown:
        print("Scanning Markdown files for injection markers...")
        inject_reference_into_markdown(ref_markdown)
        print("Done!")
    else:
        print("Failed to generate CLI reference.")
        sys.exit(1)
