---
title: Arduino App Lab Agent Mode
overwriteSidebar: Agent Mode
description: Connect Claude Code or OpenCode to Arduino App Lab and build Apps with an AI coding agent that can edit your code and operate your board.
tags:
  - App Lab
  - AI
  - Claude Code
  - OpenCode
  - Agent Mode
---

**Agent Mode** brings an AI coding agent into Arduino App Lab. Describe what you want to build, and the agent scaffolds Apps, edits Python and sketch code, adds Bricks and AI models, runs your App, and reads its logs, all without leaving App Lab. Every action that changes your board or your files waits for your approval.

Agent Mode supports **Claude Code™** (by Anthropic) and **OpenCode** as a **Preview**. Support for Codex is coming soon.

## Requirements

- **Claude Code:** A [Claude Pro or Max](https://claude.com/pricing) subscription, or an [Anthropic API key](https://platform.claude.com/settings/keys).
- **OpenCode:** Works out of the box with OpenCode's free models (no API key needed). You can also connect an API key or account from Google Gemini, OpenCode, Anthropic, OpenAI, OpenRouter, or GitHub Copilot.
- An internet connection. The agent runs where App Lab runs (normally your computer) and uses your own account or API key. Arduino does not host the model, and usage counts against your provider plan or API billing.

## Set Up the Agent

1. Select **Settings** (gear icon) in the left sidebar and scroll down to the **Agent** section.

   You can also select **Set up an agent** in the Agent panel, or select the **Agent mode** button in the status bar.
2. Select **Install** on the **Claude Code** or **OpenCode** card. App Lab downloads the agent runtime (Node.js and the agent packages) to the device running App Lab. In Connected Mode, that is your computer, and nothing is installed on the board.
3. Connect the agent:
   - **Claude Code**: Select **Manage** on the card, then sign in using one of the two tabs:
     - **Sign in**: Select **Sign in with Anthropic**. Your browser opens the Anthropic sign-in page. When the page shows a sign-in token, copy it, paste it in the **Paste token** field in App Lab, and confirm. If the browser does not open, select **Copy link** and open the link manually.
     - **API Key**: Paste your Anthropic API key and select **Verify**.
   - **OpenCode**: OpenCode connects automatically after installation and can use **OpenCode free models** right away (**No API key needed**). To add models from another provider, select **Add provider** and choose a **Provider** (Google Gemini, OpenCode, Anthropic, OpenAI, OpenRouter, or GitHub Copilot):
     - For an API key provider: paste your **API key** and select **Verify** (or **Cancel** to go back). App Lab checks the key with the provider before saving it.
     - For **GitHub Copilot**, your browser opens the GitHub device activation page and App Lab shows a **Device code** (**Copy sign-in page** and **Copy device code**). Enter the code on GitHub to authorize OpenCode.
     - Select **Start building** when you are ready. You can add or remove providers at any time under **AI model providers** in **Settings**.
4. When the card shows **Connected**, the agent is ready.

![Agent Mode connect screen](../../assets/playwright/agent/agent-mode-connect.png)

### Credential Storage

- **API keys**: App Lab stores your Claude Code and OpenCode API keys in your system keychain. Without a keychain on Linux, OpenCode keys go in a file only your user can read, and a Claude Code key lasts only until you close App Lab.
- **Claude Code sign-in**: Claude Code stores your sign-in in your system keychain. Without a keychain, it uses its own file.
- **GitHub Copilot sign-in**: OpenCode stores your sign-in in its own file. The **Device code** only authorizes the sign-in on GitHub, and App Lab doesn't keep it.

To sign out of Claude Code and remove its stored API key, select **Manage** on its card, and then **Disconnect**. To remove an OpenCode key or GitHub Copilot sign-in, select the **Remove** button (X icon) next to the provider, or **Remove all** to keep only the free models.

## Open the Agent

You can work with the agent in two views. Both use the same sessions, so you can switch between them at any time.

### Agent Panel in the Editor

To chat with the agent while keeping your code visible, open the Agent panel next to the editor:

- Press **⌘L** (macOS) or **Ctrl+L** (Windows and Linux). Press it again to close the panel.
- Or select the **Agent panel** button in the top-right corner of the editor tabs bar.

![The Agent panel button in the editor tabs bar](../../assets/playwright/editor/agent-panel-button.png)

The panel works on the App that is open in the editor. Its header shows the session title (**New session** for a new session) and the App name, and buttons to start a **New chat**, open the **Sessions history** for this App, and **Close** the panel.

When you send a prompt from the panel, the agent also receives the file that is open in the editor (including unsaved changes) and the lines you have selected. You can ask about "this function" or "the selected code" without pasting it.

![The Agent panel open next to the editor](../../assets/playwright/editor/agent-panel-open.png)

<Alert type="info">

**Note:** The Agent panel is not available in read-only Apps, such as built-in examples and installed [App releases](../../apps/manage-apps/#install-an-app-release). Select **Copy and edit App** to create an editable copy first.

</Alert>

### Full-Screen Agent Mode

Select the **Agent mode** button in the bottom-right corner of the status bar to switch the whole window to the agent view. This view shows all your sessions, grouped by App, in a sidebar on the left.

![The Agent mode button in the status bar of Arduino App Lab](../../assets/playwright/statusbar-agent-mode-hl.png)

To return to the editor, select **Editor mode** in the same place. The agent keeps working in the background while you switch views.

## What the Agent Can Do

The agent works through a set of tools that App Lab provides for your board. With these tools, the agent can:

- **Read, edit, rename, and delete App files**: The agent edits a local copy of your App, and App Lab syncs changes to the board at the end of each turn. It can also rename, move, and delete files and folders inside your App. `app.yaml` and `sketch/sketch.yaml` stay managed through the App Lab tools.
- **Manage Apps**: List, create, duplicate, rename, start, and stop Apps, and read their logs.
- **Manage Bricks, models, and libraries**: Add, configure, and remove Bricks, install AI models, and add or remove sketch libraries.
- **Check the board and carriers**: Read the board status, system resources, Wi-Fi status, and carrier configuration (such as camera and display slots on the UNO Media Carrier). To connect to a new Wi-Fi network, the agent opens the App Lab Wi-Fi dialog, and you type the password yourself.
- **Run shell commands on the board**: As a last resort, for example to install a package. Commands run on the board, never on your computer.

The agent cannot export or import Apps, see your passwords, or read the values of secret Brick variables.

While the agent is answering, you can type and press **Enter** to queue follow-up prompts. Queued prompts appear at the top of the input box and run in order after the current turn finishes. Select **Remove from queue** on a prompt or **Clear all** to cancel them before they run.

## Approve Agent Actions

Actions that only read information run without asking. Any action that changes your files, your Apps, or your board shows an **Allow the agent to do this?** card in the chat, with these options:

- **Allow once**: Run this action now.
- **Always allow**: Run this action now and allow the same action again in this App without asking.
- **Reject**: Skip this action. The agent receives your answer and can try a different approach.

The agent waits until you answer. If you stop the agent's turn, pending requests are cancelled. Shell commands always ask for approval, show the exact command and the agent's reason, and cannot be set to **Always allow**.

Actions that affect another App show an **Outside this app** badge naming the target App, and previous **Always allow** answers don't apply.

## Choose a Mode and a Model

Use the **Mode** and **Model** pickers in the prompt area of the chat to adjust the current session:

- **Mode** controls how much the agent asks before acting:
  - In **Claude Code**:
    - **Default**: Asks for approval before changing anything.
    - **Accept Edits**: Applies file edits without asking. Other actions still ask.
    - **Plan Mode**: Explores and proposes a plan without changing anything. When the plan is ready, review it and choose whether to proceed.
    - **Don't Ask**: Never asks. Actions that you have not already allowed are rejected.
    - **Bypass Permissions**: Skips all approval checks. Use with caution.
  - In **OpenCode**:
    - **Build**: The default mode. Runs tools and edits files based on your approval settings.
    - **Plan**: Read-only planning mode that disallows all edit tools.
- **Model** selects the AI model for the session:
  - In **Claude Code**, choose between Opus (more thorough) and Sonnet or Haiku (faster and fewer tokens).
  - In **OpenCode**, the menu groups models by your connected providers, with OpenCode's free models available directly or under **Other models**. New chats start on the model you last selected, or on your connected provider's model when one is configured. Select **Add provider** at the bottom of the menu to configure another provider in **Settings**.

Each agent provides its own modes and models, so they can change when you update the agent runtime. App Lab remembers the mode and model you picked for each session.

## Sessions

Each conversation with the agent is a **session**. A session belongs to one App, which is shown next to the session title. Sessions that are not tied to an App are listed under **Arduino Apps**.

- **Start a session**: Select **New session** (or **New chat** in the Agent panel). In full-screen Agent Mode, select the App to work on from the **New session in** picker.
- **Reopen a session**: Select it in the session list. The full history is restored.
- **Organize sessions**: Open the session actions menu to **Rename**, **Pin Session**, or **Delete** a session.

Sessions are stored on your computer, not on the board, and are kept per board. If you rename an App, its sessions move with it. If you delete an App, its sessions are deleted too.

## Manage the Agent

In the **Agent** section of **Settings**, you can:

- **Set as default**: When you have more than one agent installed and connected, choose which agent App Lab uses. Before switching agents, App Lab syncs any pending file edits to the board to keep your changes.
- **Manage** the connection: For Claude Code, see the sign-in method and account, or **Disconnect**. For OpenCode, add or remove keys and sign-ins under **AI model providers** (**Add provider**, **Remove**, or **Remove all**).
- **Runtime & Packages**: See the installed agent version, Node.js version (**Node**), and disk usage, or **Uninstall** the agent runtime.

## Tips for Successful Prompting

- **Start with the goal**: Describe what you want to build at a high level, such as "An App that reads the temperature from a Modulino Thermo and shows it on a web dashboard." For larger tasks, switch to **Plan Mode** first and review the plan before the agent writes code.
- **Split work into steps**: Ask the agent to work in small, testable steps. Run the App after each step and check the result.
- **Describe problems precisely**: If something doesn't work, describe what you expected and what happened, or ask the agent to read the App logs.
- **Select code for context**: In the Agent panel, select the lines you want to discuss before sending your prompt.
- **Keep one topic per session**: Start a new session for unrelated tasks, so the agent doesn't carry over context from earlier work.

<Alert type="success">

**Tip:** Prefer to run a coding agent directly on the board instead? See [Agentic AI Development on UNO Q](/tutorials/uno-q/ai-coding-agents/).

</Alert>
