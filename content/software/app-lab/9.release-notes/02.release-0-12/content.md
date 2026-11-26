---
title: 'App Lab Release Notes 0.12.0'
overwriteSidebar: Release 0.12.0
tags: [app-lab, releases]
description: 'This article contains release notes for App Lab version 0.12.0.'
author: Arduino Team
---

## Overview

This page contains release notes for Arduino App Lab. Download the latest version from the [Arduino Software page](https://www.arduino.cc/en/software/#app-lab-section).

## Release 0.12.0 [2026.11.05]

This release adds **OpenCode** support and prompt queueing to Agent Mode. It also introduces agent tools for App files and carrier status, custom Brick image builds in Arduino App CLI, and improvements to Hugging Face downloads and App releases.

### What's New

* **OpenCode in Agent Mode:** Use **OpenCode** as an AI coding agent alongside Claude Code. OpenCode runs out of the box with its built-in free models (**No API key needed**). You can also connect an API key or account from Google Gemini, OpenCode, Anthropic, OpenAI, OpenRouter, or GitHub Copilot. Configure providers under **AI model providers** in **Settings** and switch between **Build** and **Plan** modes in the chat. New chats default to your last-used model or your connected provider's model. See [Agent Mode](../../integrations/agent-mode/).
* **Prompt Queue in Agent Mode:** Send follow-up prompts while the agent is still answering. App Lab queues them at the top of the chat input and runs them in order when the current turn finishes. Remove individual prompts or select **Clear all** to cancel them.
* **Agent File and Carrier Tools:** The agent can now rename, move, and delete files and folders inside your App while keeping open editor tabs in sync. It can also check how the board's carrier (such as the UNO Media Carrier's camera and display slots) is configured. App Lab protects `app.yaml` and `sketch/sketch.yaml` from direct agent edits so they stay managed by the App Lab tools.
* **Custom Brick Container Builds (Arduino App CLI 0.14.1):** Custom Bricks whose `brick_compose.yaml` defines a `build:` section now build their Docker container image on the board at every App start. See [Bricks Architecture and Configuration Reference](../../bricks/bricks-reference/#containerization-and-networking-constraints).
* **Hugging Face Download Diagnostics:** When a Hugging Face model download fails, App Lab now shows the specific cause. It reports non-GGUF links, missing or private repositories, gated or unavailable models, incompatible quantizations, and unreachable hosts.
* **Stop Individual Release Builds:** When building App releases, the progress banner lists a **Stop `<release name>`** action for each visible build.

### Fixes

* **Faster and More Reliable Updates:** Improved the speed of the board update and `system init` process by skipping redundant package installs, recent index downloads, and duplicate example sketch profiles. Also fixed a startup delay when initializing `arduino-cli`, and ensured the App Lab self-update runs only once per update flow.
* **Read-Only AI Models in Releases:** Installed App releases now lock AI model selection and use the read-only **Download the AI Model to run this App** dialog.
* **Project Hub VENTUNO Q Tagging:** Project Hub drafts published from a VENTUNO Q now use the VENTUNO Q board SKU (`ABX00181`) instead of an UNO Q SKU.
* **Folder Conflict Wording:** The folder conflict dialog now asks whether to overwrite the existing folder or keep both, matching its actual behavior.
* **Editor & Console:** Fixed copy, cut, and paste from the editor right-click menu, kept leading spaces in the Python console, prevented the rename shortcut overlay from clipping in split view, cleared dragged file nodes when a drag ends, and refreshed the Arduino library index before installing the core.
* **Dialogs & Setup:** Aligned input fields and dropdowns across App Lab with the design system, trimmed App, Brick, and board names before saving, prevented renaming an App while it is running or stopping, reset the sketch library search and the Train new model welcome step when reopening their dialogs, enabled the flasher **Exit** button after a failed flash, and requested Network Mode only once during initial setup.
* **Examples & Bricks 0.13.2:** Renamed the **Visualize Smartphone Sensors** Inspiration to **Smartphone Sensor Stream** and updated its QR pairing instructions. Also resolved ALSA audio cards by card index rather than list position.

### Release Information

App Lab updates automatically the next time you open it. All releases are available on [GitHub](https://github.com/arduino/arduino-app-lab/releases).
