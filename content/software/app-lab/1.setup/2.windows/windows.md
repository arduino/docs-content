---
title: Setup Arduino App Lab on Windows
overwriteSidebar: Windows
description: Learn how to download and install Arduino App Lab on Windows.
author: Arduino Team
tags:
  - Windows
  - Setup
  - Arduino App Lab
  - UNO Q
---

This guide details how to prepare your Windows computer for use with Arduino App Lab, covering the installation of necessary tools and connecting your board.

## Setup on Windows

1. [Install Arduino App Lab](#install-arduino-app-lab)
1. [Connect Your Board](#connect-your-board)
1. [Get Started with Arduino App Lab](../../2.getting-started/1.quickstart/content.md)

## Install Arduino App Lab

1. Visit the official [Arduino software page](https://www.arduino.cc/en/software/#app-lab-section).

2. Locate the **Arduino App Lab** section.

3. Download the installer for Windows:

   * _Windows (10/11) NSIS Installer._ Recommended for most systems.

   * _Windows 11 (ARM) NSIS Installer._ Select this option if you are using a device with an ARM processor, like a Surface Pro.

4. Run the downloaded `.exe` file and follow the on-screen instructions to complete the installation.

## Connect Your Board

1. Launch Arduino App Lab.

1. If this is your first time launching Arduino App Lab, you may be asked to allow `mdns-discovery.exe`. You must **allow** if you want to remotely connect to boards on your network. See [About mdns-discovery.exe](#about-mdns-discoveryexe) for more information.

1. Connect your board to your PC using a USB-C cable.

1. Select your board when it appears in the Arduino App Lab interface (this may take up to 60 seconds).

## Next steps

* [Getting Started with Arduino App Lab](/software/app-lab/2.getting-started/1.quickstart/content.md)

## About mdns-discovery.exe

Network Mode relies on local network discovery (mDNS) to automatically find boards on the same network.

When installing and launching Arduino App Lab for the first time, you may receive a prompt from Windows Defender (or other security software) regarding `mdns-discovery.exe`. You must **allow** this access for the board to be discovered in Network Mode.

If you declined the prompt, you must [manually allow mdns-discovery through Windows Firewall](https://support.arduino.cc/hc/en-us/articles/4506515275548#allow-manually) for the board to appear in the App Lab interface.
