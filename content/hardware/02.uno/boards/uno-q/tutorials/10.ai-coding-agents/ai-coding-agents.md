---
title: 'Agentic AI Development on UNO Q'
difficulty: intermediate
compatible-products: [uno-q]
description: 'Learn how to use AI coding agents like OpenCode to develop, inspect, and run code directly on your Arduino UNO Q over SSH or ADB.'
author: 'Ernesto Voltaggio'
tags: [UNO Q, AI, SSH, Terminal, OpenCode, App CLI]
hardware:
  - hardware/02.uno/boards/uno-q
software:
  - app-cli
---

This tutorial shows how to run AI coding agents such as [OpenCode](https://github.com/anomalyco/opencode), Claude Code, or Codex in the [Arduino® UNO Q](https://store.arduino.cc/products/uno-q)'s Debian Linux environment. Running an agent on the board allows it to inspect files, run commands, read logs, and test applications directly. This guide focuses on OpenCode.

![AI Agentic development on Arduino UNO Q with OpenCode](assets/hero-banner.png)

## Required Hardware and Software

### Hardware Requirements

- [Arduino® UNO Q](https://store.arduino.cc/products/uno-q)
- A computer (macOS, Windows, or Linux)
- A USB-C® cable (only required for the ADB-over-USB workflow)
- A network connection (Ethernet or Wi-Fi®) for the SSH workflow

### Software Requirements

- **OpenCode**, or another terminal AI coding agent installed directly on your UNO Q.
- SSH or ADB access configured on your board.
- An account or API key for a model provider supported by your chosen agent.

***Note: For more details on setting up connections, refer to the [ADB tutorial](/tutorials/uno-q/adb/) or the [SSH tutorial](/tutorials/uno-q/ssh/).***

## Using OpenCode on the UNO Q

[OpenCode](https://github.com/anomalyco/opencode) is an open-source AI coding agent with terminal and web interfaces. The installation section also includes Claude Code and Codex as alternatives.

### 1. Connect to the Board

Before using the agent, ensure you can access the board's shell.

**Via Secure Shell (SSH):**
If the board is on your local network, access it using its hostname (e.g., `uno-q.local` or whatever hostname you configured):

```bash
ssh arduino@<hostname>.local
```

**Via ADB (Android Debug Bridge):**
If the board is connected directly via USB, use ADB:

```bash
adb shell
```

### 2. Install the Agent

Open an SSH or ADB session and install one of the following agents.

#### OpenCode

```bash
curl -fsSL https://opencode.ai/install | bash
```

Restart the SSH session or reload the shell, then verify the installation:

```bash
exec "$SHELL"
opencode --version
```

#### Claude Code

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

#### Codex CLI

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

### 3. Prepare Your Workspace

Run OpenCode from your home directory (`~`) for board-wide work, or from a dedicated application directory for a clearer project scope and simpler Git tracking. The directory is an organizational boundary, not a security sandbox: the agent has the same access as the `arduino` user. Avoid initializing a Git repository in `~` unless you intend to track the entire home directory.

For application-specific work, create a dedicated workspace:

```bash
mkdir -p ~/ArduinoApps/ai-agent-demo
cd ~/ArduinoApps/ai-agent-demo
git init
```

### 4. Provide Hardware Context to the Agent

The UNO Q includes [`arduino-app-cli`](/software/app-lab/tutorials/cli/) for creating, building, and running Arduino applications. Give the agent an initial prompt that defines its environment and boundaries. For example:

> *"You are running on an Arduino UNO Q Debian system. Explore `arduino-app-cli --help`, then use the CLI to create, build, and run applications. Do not change network, SSH, ADB, or security settings."*

Alternatively, create an `AGENTS.md` file in your workspace. This plain text Markdown file provides persistent instructions that OpenCode discovers when it starts in that directory. OpenCode also supports **Skills** — directories containing a `SKILL.md` file and optional scripts or references that are loaded on demand.

### 5. Start Developing

**Terminal UI (TUI):**  
Run `opencode` from your chosen directory. On the first launch, enter `/connect`, select a model provider, and follow the authentication instructions. Provider credentials are used by the OpenCode process on the UNO Q.

![OpenCode Terminal UI](assets/opencode-tui.png)

**Web UI:**  
Replace `your_password` and start the Web UI:

```bash
OPENCODE_SERVER_PASSWORD='your_password' opencode web --mdns
```

Open `http://opencode.local:4096`, the default address when that port is available, or use one of the addresses printed in the terminal. Log in as `opencode` with your password. Because the connection uses unencrypted HTTP, use it only on a trusted local network.

![OpenCode Web UI](assets/opencode-webui.png)

Try these example prompts to see what it can do:
- **System Inspection:** *"Inspect this board and summarize the Linux version, available memory, storage, and connected Arduino-related tools."*
- **App CLI Integration:** *"Use `arduino-app-cli` to scaffold an application with a Python component and an Arduino sketch. Make the sketch blink the user LED and let Python start and stop it through the Bridge."*
- **Debugging:** *"Check the logs for errors from my Python app and suggest the smallest fix."*

**Remote access from another device:**
- **OpenCode:** Use the Web UI described above, or connect OpenCode Desktop to an OpenCode server running on the UNO Q through a secure tunnel.
- **Claude Code:** From a trusted project directory, run `claude remote-control` for remote-only access, or `claude --remote-control` to keep an interactive local session. Continue from [claude.ai/code](https://claude.ai/code) or the Claude mobile app.
- **Codex:** Run `codex remote-control start`, followed by `codex remote-control pair`. When finished, run `codex remote-control stop`. This feature is experimental.

OpenCode connects directly to the server on the board, while Claude Code and Codex use account-linked remote-control services.

## Safety & Security

- **Permissions:** The agent has the same permissions as the `arduino` user. Tell it not to edit system, network, SSH, ADB, or security configuration unless required.
- **Git:** Commit a working version before asking the agent to make a large change.
- **Network Access:** The Web UI described above uses HTTP. Keep it on a trusted local network and do not forward its port from your router to the internet.
- **Credentials:** When the backend runs on the board, provider credentials are also on the board. Revoke them before sharing or transferring it.
- **Physical Access:** ADB is enabled over USB by default, so secure physical access to the board.

## Alternative: Remote Agent From Your Host Computer

If you prefer not to install the agent directly on the board—to save memory, keep your API keys strictly on your computer, or simply work from your preferred editor—you can run the agent on your host machine and control the UNO Q remotely.

***Tip: Working from the host has a key advantage: your code and configuration live on your computer, so you don't risk losing or having to transfer files when reflashing the board's Linux image.***

The agent runs in your computer's terminal but executes commands on the board. You can connect via **ADB** (over USB) or **SSH** (over the network). ADB is generally preferred when available since it requires no network configuration; fall back to SSH if USB is not accessible.

### 1. Host Setup

**Via ADB (USB):**
1. Connect the UNO Q to your computer via USB-C®.
2. Ensure the `adb` CLI tool is installed on your computer.
3. Run `adb devices` in your computer's terminal to confirm the board is recognized.

**Via SSH (Network):**
1. Ensure your UNO Q is on the same network as your computer. See the [SSH tutorial](/tutorials/uno-q/ssh/) for connection basics.
2. Set up **key-based authentication** so the agent can connect without being blocked by password prompts. From your computer:

   ```bash
   ssh-copy-id arduino@<hostname>.local
   ```

3. Optionally, add an alias to your `~/.ssh/config` so both you and the agent can connect with a short command:

   ```bash
   Host uno-q
       HostName <hostname>.local
       User arduino
   ```

***If key-based authentication is not possible, you can use `sshpass` with the password stored in an environment variable: `export UNO_Q_PASS="your_password"` then `sshpass -p "$UNO_Q_PASS" ssh arduino@<hostname>.local`.***

4. Install OpenCode on your computer (`curl -fsSL https://opencode.ai/install | bash`).

### 2. The Context File

Create a project folder **on your host computer** and add an `AGENTS.md` file. You must explicitly instruct the agent to route all its actions through the board. The instructions should prioritize ADB if available, and fall back to SSH otherwise:

```markdown
You are an AI assistant helping develop for an Arduino UNO Q board.
You are running on my host machine, but the target environment is connected via Android Debug Bridge (ADB) or SSH.

CRITICAL RULES:
1. DO NOT run standard bash commands (like `ls`, `mkdir`, `python`) directly on the host.
2. Prefer ADB when available. To run commands on the board via ADB, wrap them in `adb shell` (e.g., `adb shell "arduino-app-cli --help"`).
3. If ADB is not available, use SSH instead (e.g., `ssh uno-q "arduino-app-cli --help"`).
4. To read files from the board, use `adb shell "cat /path/to/file"` or `ssh uno-q "cat /path/to/file"`.
5. To write files to the board, write them to this local directory first, then use `adb push <local_file> <board_path>` or `scp <local_file> uno-q:<board_path>`.
6. To inspect logs or fetch files, use `adb pull <board_path> <local_file>` or `scp uno-q:<board_path> <local_file>`.
```

When you launch the agent from this local directory, it will automatically bridge the gap: drafting code safely on your computer and pushing it directly to the board.

> **Tested versions:** The on-board workflow was verified on an Arduino UNO Q 4 GB running Debian GNU/Linux 13 (trixie), OpenCode 1.17.15, Claude Code 2.1.216, Codex CLI 0.144.6, and Arduino App CLI 0.11.1. Commands may differ in later versions.
