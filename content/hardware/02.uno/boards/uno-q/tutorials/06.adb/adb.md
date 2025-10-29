---
title:
description:
author: Karl Söderby
tags: [UNO Q, ADB, Linux]
---

## Requirements

The following hardware is required:
- [Arduino UNO Q](https://store.arduino.cc/products/uno-q)
- [USB-C® type cable](https://store.arduino.cc/products/usb-cable2in1-type-c)

You will also need to have the following software installed:
- [Android Debug Bridge](https://developer.android.com/tools/releases/platform-tools)

## Installing ADB (Host Computer)

***Note: if you are using the board as a Single Board Computer (SBC Mode (Preview) without a host computer), you do not need to install ADB. You can run `arduino-app-cli` directly from the terminal.***

The ADB command line tool is supported on MacOS, Windows & Linux. For more specific instructions for your OS, see the sections below. 

***You can find more information and download the latest version for the tool for all operating systems directly from the [Android SDK Platform Tools](https://developer.android.com/tools/releases/platform-tools#downloads) page.***

### MacOS

To install the ADB tools on **MacOS**, we can use `homebrew`. Open the terminal and run the following command:

```sh
brew install android-platform-tools
```

To verify the tool is installed, run `adb version`.

### Windows

To install the ADB tools on **Windows**, we can use `winget`, supported on Windows 11 and on some earlier Windows 10 versions. 

Open a terminal and run the following:

```sh
winget install Google.PlatformTools
```

To verify the tool is installed, run `adb version`.

### Linux

To install ADB tools on a **Debian/Ubuntu Linux distribution**, open a terminal and run the following command:

```sh
sudo apt-get install android-sdk-platform-tools
```

To verify the tool is installed, run `adb version`.

## Connect via ADB

1. Connect the UNO Q board to your computer via USB-C.
2. Run `adb devices` in the terminal. This should list the connected devices.

    ![Connected devices](assets/connected-devices.png)

>Note that it may take up to a minute for the device to appear after connecting it.

3. Run `adb shell`. If you have not set up your board prior to this via the Arduino App Lab, you may be required to provide a password, which is `arduino`.
4. You should now be inside your board's terminal.

    ![Terminal on the board.](assets/board-terminal.png)

5. You are now able to run commands via the terminal on your board! To exit from the terminal, simply type `exit`.