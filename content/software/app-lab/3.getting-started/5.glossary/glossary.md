---
title: Arduino App Lab Glossary
overwriteSidebar: Glossary
description: Definitions for common terms and concepts used in the Arduino App Lab ecosystem.
tags:
  - Glossary
  - Arduino App Lab
---

## ADB (Android Debug Bridge)
A command-line tool used to access the board's Linux shell over a USB connection. It allows for file management and terminal access without a network connection.

## AI (Artificial Intelligence)
The simulation of human intelligence by machines. In App Lab, AI models are typically deployed within **Bricks** to perform tasks like object detection or speech recognition locally on the board.

## API (Application Programming Interface)
A set of rules allowing software entities to communicate. Bricks expose high-level APIs that allow Python scripts to access complex features like machine learning or hardware drivers.

## App
An Arduino App is a modular software architecture that orchestrates multiple components into a single project. The core logic runs via high-level code (Python) on the board's Linux subsystem. Apps can also include an Arduino **Sketch** running on a microcontroller for precise hardware control, and **Bricks**—pre-built software components (like AI models or databases) running in isolated containers. Every App is defined by a project folder containing a mandatory `app.yaml` manifest and a `python/main.py` entry point. For more information, see [About Apps](../../apps/about-apps/).

## app.yaml
The mandatory manifest file for every App. It stores metadata and configuration, such as the App's name, icon, and the list of Bricks used in the project.

## Arduino CLI
The command-line tool that handles board detection and sketch compilation. It serves as the underlying engine for managing the C++ components of an App.

## Arduino App CLI
A specialized command-line tool pre-installed on compatible boards. It automates the lifecycle of an App, including building, starting, and stopping services directly from the Linux terminal.

## Arduino App Lab
The integrated development environment (IDE) designed for modular application development. It allows users to create, edit, and manage Apps through a graphical interface on a computer or directly on the board in **SBC Mode**.

## Arduino Flasher CLI
A standalone utility used to "flash" or reset a board with a fresh Linux operating system image, returning it to its factory state.

## Arduino Router
A background Linux service (`arduino-router`) that manages data traffic between the Linux processor and the microcontroller, enabling the **Bridge** connection.

## Brick
A reusable building block that an app can include to provide a specific feature, such as a web interface, a camera pipeline, an AI model, storage, or cloud connectivity. Bricks expose a high-level API so apps can use their functionality without implementing it from scratch. For more information, see [About Bricks](../../bricks/about-bricks/).

## Bridge
The communication mechanism that enables the Linux processor (MPU) and the microcontroller (MCU) to exchange data. It allows Python and C++ code to interact through **Remote Procedure Calls (RPC)**.

## Connected Mode
A mode where the board is connected to a computer via USB-C. The Arduino App Lab software runs on the computer and communicates with the board to deploy and monitor Apps.

## Console
The interface within App Lab used to view real-time logs. It displays deployment progress, Python output, and serial data from the microcontroller.

## EDL Mode (Emergency Download Mode)
A low-level boot mode used when flashing a new Linux image to the board. It is required for the **Arduino Flasher CLI** to communicate with the hardware.

## GPIO (General Purpose Input/Output)
Digital pins on the board that can be programmed as inputs or outputs to interact with external electronic components.

## Linux Image
The operating system file that contains the customized Linux distribution and drivers required to run the board and App Lab.

## main.py
The mandatory entry point for an Arduino App. It is a Python script running on the Linux subsystem that contains the high-level application logic and orchestrates any active Bricks or microcontroller sketches.

## MCU (Microcontroller Unit)
The secondary processor on the board. It handles real-time tasks and hardware interaction, running independently but in coordination with the primary processor.

## ML (Machine Learning)
A subset of AI focused on systems that learn from data. Developers can deploy ML models directly on the board using Bricks.

## MQTT (Message Queuing Telemetry Transport)
A lightweight messaging protocol used for IoT communication. Apps can use MQTT to report sensor data or receive remote commands.

## MPU (Microprocessor Unit)
The primary processor on the board. It runs the Linux OS and handles high-level logic, networking, and the App's Python scripts.

## Modulino
A system of plug-and-play hardware modules (sensors and actuators) that connect to the board via a standardized I2C connector.

## Network Mode
A wireless connection state where the board is accessed over a local Wi-Fi network. This allows for remote development and monitoring after an initial USB setup.

## QWIIC
A standardized connection system for I2C peripherals. It allows users to connect compatible nodes and sensors to the board without soldering.

## README.md
An optional Markdown file located in an App's root directory. It provides human-readable documentation and instructions that are displayed within the Arduino App Lab interface.

## RPC (Remote Procedure Call)
The protocol underlying the **Bridge**, allowing a program on one processor (e.g., MPU) to execute code on another (e.g., MCU) as if it were a local function.

## SBC Mode (Single-Board Computer)
A standalone mode where the board acts as a computer. This requires connecting a monitor, keyboard, and mouse directly to the board via a USB-C hub.

## Sketch
The Arduino/C++ code (`sketch.ino`) that runs on the board's microcontroller (MCU).

## SSH (Secure Shell)
A secure network protocol used to access the board's Linux terminal remotely.

## Zephyr OS
The Real-Time Operating System (RTOS) that runs on the microcontroller (MCU) to handle low-level tasks and bridge communication.
