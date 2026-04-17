---
title: Setup Arduino App Lab on Linux
overwriteSidebar: Linux
description: Learn how to install Arduino App Lab and configure your Linux system for the UNO Q.
author: Arduino Team
tags:
  - Linux
  - Setup
  - Arduino App Lab
  - UNO Q
---

This guide details how to prepare your Linux computer for developing with Arduino App Lab, including installing dependencies, configuring `udev` rules, and setting user permissions.

## Setup on Linux

1. [Prepare Your System](#prepare-your-system)
1. [Install Arduino App Lab](#install-arduino-app-lab)
1. [Connect Your Board](#connect-your-board)
1. [Get Started with Arduino App Lab](../../2.getting-started/1.quickstart/content.md)

## Prepare Your System

### Step 1: Install libwebkit2gtk

Arduino App Lab requires the `libwebkit2gtk-4.1-0` library to render the user interface.

* **Debian/Ubuntu:**

  ```bash
  sudo apt update
  sudo apt install libwebkit2gtk-4.1-0
  ```

* **Arch Linux:**

  ```bash
  sudo pacman -S webkit2gtk-4.1
  ```

* **Fedora:**

  ```bash
  sudo dnf install webkit2gtk4.1
  ```

### Step 2: Configure udev Rules

You must create a `udev` rule to ensure your Linux system correctly identifies and grants permission to the UNO Q hardware.

1. Create a new rules file:

   ```bash
   sudo nano /etc/udev/rules.d/99-arduino-uno-q.rules
   ```

2. Paste the following configuration into the file:

   ```systemd
   SUBSYSTEM=="usb", ATTRS{idVendor}=="2341", MODE="0666", GROUP="dialout"
   SUBSYSTEM=="usb", ATTRS{idVendor}=="05c6", MODE="0666", GROUP="dialout"
   ```

3. Save and exit (Ctrl+O, Enter, Ctrl+X).
4. Reload the rules:

   ```bash
   sudo udevadm control --reload-rules
   sudo udevadm trigger
   ```

### Step 3: Set User Permissions

Add your user account to the `dialout` group to allow access to the serial and USB interfaces used by the board.

```bash
sudo usermod -a -G dialout $USER
```

<Alert type="note">**Important:** You must log out and log back in for these group permission changes to take effect.</Alert>

## Install Arduino App Lab

1. Visit the official [Arduino software page](https://www.arduino.cc/en/software/#app-lab-section).
1. Locate the **Arduino App Lab** section.
1. Download the Arduino App Lab archive for Linux (.tar.gz).
1. Create an Applications directory in your home folder:

   ```bash
   mkdir -p ~/Applications
   ```

1. Extract the archive into that folder:

   ```bash
   tar -xf ~/Downloads/ArduinoAppLab*.tar.gz -C ~/Applications
   ```

## Connect Your Board

1. Launch Arduino App Lab.
2. Connect your UNO Q to your PC using a USB-C® cable.
3. Select your board when it appears in the Arduino App Lab interface (this may take up to 60 seconds).

## Next steps

* [Getting Started with Arduino App Lab](/software/app-lab/2.getting-started/1.quickstart/content.md)
