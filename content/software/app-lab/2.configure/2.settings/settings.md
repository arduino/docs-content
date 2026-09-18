---
title: 'Arduino App Lab Settings'
description: 'Learn about configuration options, system information, and device management tools available in the Arduino App Lab Settings page.'
overwriteSidebar: Settings
tags: [Arduino App Lab, Settings, Reference, UNO Q]
---

Manage your board's configuration, view system information, and access device management tools through the **Settings** page.

## Access Settings in Arduino App Lab

Follow these steps to open the Settings menu:

1. Open Arduino App Lab.
2. Connect to your board.
3. Select **Settings** (gear icon) from the left sidebar.

You can only access the Settings menu when connected to a board.

## Settings Overview

The settings page is divided into five sections that allow you to manage the Arduino App Lab software, view hardware details, and configure the board's system and network settings.

### Arduino App Lab

This section provides information about the local application environment.

- **App Lab Version**: Displays the current version of the Arduino App Lab application and indicates whether the software is up to date.
- **Documentation**: Click the link to view the official Arduino App Lab documentation.

### Device Details

This section identifies the properties of the connected board.

- **Board Name**: The custom name assigned to the board (e.g., `devan`). Select the **Edit** icon to modify the name.
- **Board Model**: Identifies the connected hardware model, such as `ARDUINO UNO Q`.
- **FQBN**: The Fully Qualified Board Name used by the compilation tools, such as `arduino:zephyr:unoq`.
- **Serial Number**: The unique hardware serial number of the board.
- **Disk Storage**: Used capacity versus the total available storage capacity.

### System Info

This section manages the software and security configuration of the board.

- **System version**: Indicates the current software status. Select the **Update** button to download and install available updates.
- **Release notes**: Click the link to view release notes for Arduino App Lab.
- **Keyboard language**: Configure the regional keyboard layout for the Linux environment.
- **OS password**: Select the **Change password** button to update the login credentials for the Linux operating system.
- **Remote access (SSH)**: A toggle switch to enable or disable Secure Shell (SSH) access to the board. Enabled by default.

### Operating system

This section details the low-level firmware and OS image currently running on the microprocessor.

- **Build Version**: The specific build identifier of the installed OS image.
- **Linux Distribution**: The active Linux distribution and version.
- **Kernel Version**: The active Linux kernel version.
- **Release date**: The release date of the installed OS image.
- **Install another OS version (Flash)**: Select the **Flash Board** button to initiate the flashing process and install a different operating system image. See [Flash a New Linux Image](../flash/) to learn more.

### Network Connections

This section manages the active network interfaces.

- **SSID**: The name of the currently connected Wi-Fi network. Select the **Change network** button to connect the board to a different wireless network.
- **IP**: The local IP address currently assigned to the board.
