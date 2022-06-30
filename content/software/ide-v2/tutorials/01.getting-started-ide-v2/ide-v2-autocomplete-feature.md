---
title: 'Getting Started with Arduino IDE 2.0'
difficulty: easy
description: 'An introductory guide to the Arduino IDE 2.0'
tags:
 - Arduino IDE 2
 - Software Tools
author: 'Karl Söderby'
---

Makers, students & professionals have been using the classic Arduino IDE (Integrated Development Environment) since the beginning of Arduino. 

The Arduino IDE 2.0 is an improvement of the classic IDE, with an increased performance, improved user interface and many new features, such as [autocompletion](/software/ide-v2/tutorials/ide-v2-autocomplete-feature), a [built-in debugger](/software/ide-v2/tutorials/ide-v2-debugger) and a [syncing sketches with Arduino Cloud](/software/ide-v2/tutorials/ide-v2-cloud-sketch-sync).

In this guide, we will cover the basics of the Arduino IDE 2.0, where you will find links to more detailed resources on how to use specific features!

***You can download the IDE 2.0 from the [Arduino Software page](https://www.arduino.cc/en/software#experimental-software).*** 

***You can also follow the [downloading and installing the Arduino IDE 2.0](/en/Tutorial/getting-started-with-ide-v2/ide-v2-downloading-and-installing) tutorial for more detailed guide on how to install the editor.***

## Requirements

- [Arduino IDE 2.0](https://www.arduino.cc/en/software#future-version-of-the-arduino-ide) installed. 

## Overview

The Arduino IDE 2.0 features a new sidebar, making the  most commonly used tools more accessible.

![Arduino IDE 2.0](assets/ide-2-overview.png)

- **Verify / Upload** - compile and upload your code to your Arduino Board.
- **Select Board & Port** - detected Arduino boards automatically show up here, along with the port number.
- **Sketchbook** - here you will find all of your sketches locally stored on your computer. Additionally, you can sync with the [Arduino Cloud](https://cloud.arduino.cc/), and also obtain your sketches from the online environment.
- **Board Manager** - browse through Arduino & third party packages that can be installed. For example, using a MKR WiFi 1010 board requires the `Arduino SAMD Boards` package installed.
- **Library Manager** - browse through thousands of Arduino libraries, made by Arduino & its community.
- **Debugger** - test and debug programs in real time.
- **Search** - search for keywords in your code.
- **Open Serial Monitor** - opens the Serial Monitor tool, as a new tab in the console.

## Features

The Arduino IDE 2.0 is a versatile editor with many features. You can install libraries directly, sync your sketches with Arduino Cloud. In this section, many of the core features are listed, along with a link to a more detailed article.

### Board Manager

![Board Manager.](assets/board-manager.png)

With the board manager, you can browse and install packages, or "cores" for your boards. A board package is required when compiling and uploading code for your board.

There are several Arduino board packages available, such as **avr, samd, megaavr, samd** and more.

***To learn more about the board manager, visit the [Installing new boards tutorial]().***

### Library Manager

![Library Manager.](assets/library-manager.png)

With the library manager you can browse and install thousands of libraries. Libraries are extensions of the Arduino API, and makes it easier to for example control motors, or use a Wi-Fi module.

***To learn more about the library manager, visit the [Installing new libraries tutorial]().***

### Serial Monitor

![Serial Monitor.]()

The Serial Monitor is a tool that allows you to view data streamed from your board, via for example the `Serial.print()` command. 

Historically, this tool has been located in a separate window, but is now integrated to the editor. This makes it easy to have multiple instances running at the same time on your computer.

***To learn more about the Serial Monitor, visit the [Serial Monitor tutorial]().***

### Serial Plotter

![Serial Plotter.](assets/potentiometer-plotter.gif)

The Serial Plotter tool is great for visualizing data using graphs, and to monitor e.g. peaks in voltage. 

You can monitor several variables simultaneously, with options to enable only certain types. 

***To learn more about the Serial Plotter, visit the [Serial Plotter tutorial]().***

### Debugging

![Debugger tool.](assets/playpause.gif)

The debugger tool is used to test and *debug* programs, hence the name. It can be used to navigate through a program's execution in a controlled manner. 

***To learn more about the debugger tool, visit the [Debugging tutorial]().***

### Autocompletion

![Autocompletion tool.](assets/autocomplete.png)

Autocompletion is a must-have for editors, and the 2.0 version now includes it. When writing code, this is useful to understand more about the elements of the Arduino API.

Note that you always need to select your board for autocompletion to work. 

***To learn more about the Autocompletion tool, visit the [Autocompletion tutorial]().***

### Remote Sketchbook

![Push and pull your sketches.](assets/remote-sketchbook.gif)

The Remote Sketchbook feature lets you sync sketches from your Arduino Cloud sketchbook with your local computer. To enable this feature, you will need to login to your Arduino Cloud account.

***To learn more about the Remote Sketchbook feature, visit the [Synchronizing Sketches tutorial]().***

### Firmware & Certificate Uploader

[Firmware & Certificate Uploader.](assets/fw-cert-upload.png)

## Contribute

The Arduino IDE 2.0 is an open-source project that is free for anyone to download. You can contribute to the project through [donations](https://www.arduino.cc/en/donate/), or by reporting issues at [our GitHub repository](https://github.com/arduino/arduino-ide).

## Conclusion