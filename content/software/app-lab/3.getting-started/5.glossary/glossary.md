---
title: Arduino App Lab Glossary
overwriteSidebar: Glossary
description: Definitions for common terms and concepts used in the Arduino App Lab ecosystem.
tags:
  - Glossary
  - Arduino App Lab
---

This glossary defines the terms used across the Arduino App Lab documentation and interface.

## ADB (Android Debug Bridge)

A command-line tool used to access the board's Linux shell over a USB connection. App Lab uses ADB to communicate with the board in USB mode, and you can use it for file transfers and terminal access without a network connection. See [Open the Board's Shell](../../cli/cli/#open-the-boards-shell).

## Agent Mode

The AI coding agent built into App Lab. The agent can edit App files, manage Bricks and AI models, run Apps, and read their logs, asking for your approval before any change. It runs on your computer with your own Claude account. **Agent mode** also refers to the full-screen view of the agent, opened from the status bar. See [Agent Mode](../../integrations/agent-mode/).

## Agent Panel

The panel that opens next to the editor (`⌘L` / `Ctrl+L`), where you can chat with the agent about the App you are editing. The agent receives the open file and your selected code as context.

## AI (Artificial Intelligence)

The simulation of human intelligence by machines. In App Lab, AI models typically run inside **Bricks** to perform tasks like object detection or speech recognition locally on the board.

## AI Model

The trained file that an AI Brick uses to make predictions, such as an object detector or a language model. Models are downloaded to the board and selected per Brick in the **AI Models** tab. See [AI Models](../../integrations/models/).

## API (Application Programming Interface)

A set of rules allowing software entities to communicate. Bricks expose high-level Python APIs that give your App access to complex features like machine learning or web interfaces.

## App

An Arduino App is a project that combines Python code running on the board's Linux system with optional **Bricks** and an optional Arduino **Sketch** running on the microcontroller. Every App is a folder containing an `app.yaml` manifest and a `python/main.py` entry point. See [About Apps](../../apps/about-apps/).

## App ID

A short name that identifies an App in the [Arduino App CLI](#arduino-app-cli), such as `user:my-app` for your Apps, `examples:inspirational/blink` for built-in examples, or `release:<name>` for installed releases. See [Refer to Apps](../../cli/cli/#refer-to-apps).

## App Release

A packaged, read-only version of an App, saved as an `.ard` file. It runs exactly as it did when it was created, on any board of the same type. See [Create an App Release](../../apps/manage-apps/#create-an-app-release).

## app.yaml

The mandatory manifest file of every App. It stores the App's name, description, icon, exposed ports, and the list of Bricks with their variables and selected AI models. App Lab manages it automatically.

## Arduino App CLI

The command-line tool (`arduino-app-cli`) pre-installed on compatible boards. It runs as a background service that App Lab talks to, and it manages the full lifecycle of Apps: creating, starting, and stopping them, managing Bricks and AI models, building releases, and updating the system. You can also use it directly from the board's terminal. See [Arduino App CLI](../../cli/cli/).

## Arduino App Lab

The development environment for creating, editing, and running Apps. It runs on your computer (Connected Mode) or directly on the board (SBC Mode).

## Arduino CLI

The command-line tool that compiles sketches and manages Arduino libraries. App Lab and the Arduino App CLI use it to build and upload the sketch part of an App.

## Arduino Flasher CLI

A standalone tool used to "flash" a board with a fresh Linux operating system image, for example to recover a board or to install a different OS version. App Lab includes a built-in version of the flasher. See [Flash a Linux Image](../../configure/flash/).

## Arduino Router

A background Linux service (`arduino-router`) that routes messages between the Linux system and the microcontroller, enabling the **Bridge** connection.

## Board Extensions

Hardware attached to the board that must be declared to the system, such as carriers and add-ons on the JHat header. Configure them in the **Board extensions** section of [Settings](../../configure/settings/#board-extensions).

## Brick

A reusable building block that an App can include to provide a specific feature, such as a web interface, a camera pipeline, an AI model, storage, or cloud connectivity. Bricks expose a high-level Python API, and some run additional services in containers. Each Brick has an ID, such as `arduino:web_ui`. See [About Bricks](../../bricks/about-bricks/).

## Bridge

The communication mechanism that enables the Linux processor (MPU) and the microcontroller (MCU) to exchange data. It allows Python and C++ code to call each other's functions through **Remote Procedure Calls (RPC)**. See [Getting Started with the Bridge](../../bridge/get-started-with-bridge/).

## Connected Mode

A setup where Arduino App Lab runs on your computer and connects to the board, either over USB or over the local network ([Network Mode](#network-mode)). Also called PC-hosted mode. See [Setup](../../setup/overview/).

## Console

The panel at the bottom of the editor that shows real-time logs of a running App, in separate tabs: **App launch** (startup progress), **Python** (Python output), **Serial Monitor** (sketch output), and one tab for each Brick container. See [Monitor an App](../../apps/run/#monitor-an-app).

## Container

An isolated environment, managed by Docker, in which a part of an App runs. Your App's Python code runs in a container, and some Bricks run additional services in their own containers.

## Custom Brick

A Brick you create inside an App, stored in the App's `bricks/` folder. Custom Bricks can package your own Python code and container services. See [Create Custom Bricks](../../bricks/custom-bricks/).

## EDL Mode (Emergency Download Mode)

A low-level boot mode used when flashing a new Linux image. You enter it by shorting the board's EDL pins with a jumper before connecting the board.

## Edge Impulse

A platform for training custom machine learning models. App Lab integrates with Edge Impulse Studio so you can train models for vision, audio, and sensor Bricks. See [Custom AI Models](../../integrations/ai-models/).

## Examples

Basic, single-topic starter Apps in App Lab, such as blinking an LED or using the Bridge, plus small examples for individual Bricks. Examples are read-only. See [Using Examples](../examples/).

## FQBN (Fully Qualified Board Name)

The identifier the Arduino tools use for a board, such as `arduino:zephyr:unoq`. It is shown in **Device details** in Settings.

## GGUF

A file format for language models used by llama.cpp. Models added to the LLM Brick from Hugging Face must be in GGUF format.

## GPIO (General Purpose Input/Output)

Digital pins on the board that can be programmed as inputs or outputs to interact with external electronic components.

## Hugging Face

An online hub of AI models. In App Lab, you can add language models from Hugging Face to the LLM Brick. See [Add Models from Hugging Face](../../integrations/models/#add-models-from-hugging-face).

## Inspirations

Rich, multi-component showcase Apps in App Lab that are ready to run and provide a complete experience. Inspirations are read-only; select **Copy and edit App** to modify one. See [Using Examples](../examples/).

## Linux Image

The operating system image that contains the Linux distribution and drivers required to run the board and App Lab. The UNO Q uses Debian, and the VENTUNO Q uses Ubuntu.

## LSP (Language Server Protocol)

A protocol that powers the code assistance in the App Lab editor, such as auto-completion, diagnostics, go to definition, and find all references, for Python, C++, and JavaScript/TypeScript. See [Language Server Protocol (LSP)](../../apps/develop-apps/#language-server-protocol-lsp).

## main.py

The mandatory entry point of an App, located in the `python/` folder. It contains the App's high-level logic and must call `App.run()` to start the App.

## MCP (Model Context Protocol)

An open protocol that lets AI models use external tools and data sources. The **MCP Client** Brick connects an App to MCP servers, and the App Lab agent uses MCP tools to operate your board.

## MCU (Microcontroller Unit)

The secondary processor on the board. It handles real-time tasks and hardware interaction, and runs the App's sketch on Zephyr OS.

## ML (Machine Learning)

A subset of AI focused on systems that learn from data. You can run ML models directly on the board using Bricks.

## Modulino

A system of plug-and-play hardware modules (sensors and actuators) that connect to the board via a standardized Qwiic (I2C) connector.

## Monitor

The object a sketch uses to print text to, and read text from, the **Serial Monitor** tab of the console. See [Monitor API](../../bridge/bridge-api/#monitor-api).

## MPU (Microprocessor Unit)

The primary processor on the board. It runs the Linux OS and handles high-level logic, networking, Bricks, and the App's Python code.

## MQTT (Message Queuing Telemetry Transport)

A lightweight messaging protocol used for IoT communication. Apps can use MQTT through Python libraries to report sensor data or receive remote commands.

## Network Mode

A way of connecting App Lab to the board over the local Wi-Fi network instead of USB. It requires the board to be connected to Wi-Fi, a Linux password, and **Remote access (SSH)** enabled in Settings.

## NPU (Neural Processing Unit)

A processor dedicated to running AI models efficiently. On boards with an NPU, such as the VENTUNO Q, App Lab provides models optimized for NPU acceleration.

## Project Hub

The Arduino community platform for sharing projects. You can upload an App to [Project Hub](https://projecthub.arduino.cc/) as a draft directly from App Lab. See [Publish on Project Hub](../../apps/manage-apps/#publish-on-project-hub).

## Qwiic

A standardized connection system for I2C peripherals. It allows users to connect compatible nodes and sensors to the board without soldering.

## Read-only App

An App that can be run but not edited, such as a built-in example, an Inspiration, or an installed App release. Select **Copy and edit App** to create an editable copy.

## README.md

An optional Markdown file in an App's root folder. It provides documentation and instructions that are displayed in the Arduino App Lab interface.

## RPC (Remote Procedure Call)

The mechanism underlying the **Bridge**, allowing a program on one processor (for example, the MPU) to execute a function on another (for example, the MCU) as if it were a local function.

## SBC Mode (Single-Board Computer)

A setup where the board works as a standalone computer, with a monitor, keyboard, and mouse connected, and App Lab runs directly on the board. See [Setup Arduino App Lab in SBC Mode](../../setup/standalone/).

## Session

A conversation with the App Lab agent. Each session belongs to an App and keeps its full message history, so you can reopen it later.

## Sketch

The Arduino C++ code (`sketch/sketch.ino`) that runs on the board's microcontroller (MCU). Its libraries are listed in `sketch/sketch.yaml`.

## SSH (Secure Shell)

A secure network protocol used to access the board's Linux terminal remotely. App Lab uses SSH in [Network Mode](#network-mode).

## Startup App

The App that the board starts automatically every time it is powered on. Only one App can run at startup. See [Run at Startup](../../apps/run/#run-at-startup).

## System Update

An update of the software running on the board, including the Arduino App CLI, Bricks, and other core packages. App Lab offers system updates when the board is connected to the internet. See [Manage Software Updates](../../configure/config/#manage-software-updates).

## Zephyr OS

The Real-Time Operating System (RTOS) that runs on the microcontroller (MCU) to handle low-level tasks and Bridge communication.
