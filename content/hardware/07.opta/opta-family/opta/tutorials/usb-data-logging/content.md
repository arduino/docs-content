---
title: 'Getting Started with USB Data Logging on Opta™'
description: "Learn how to interface an Opta™ device with a USB memory stick for data logging."
difficulty: intermediate
tags:
  - Opta
  - USB Memory Stick
  - Arduino IDE
author: 'José Bagur and Taddy Chung'
software:
  - ide-v1
  - ide-v2
hardware:
  - hardware/07.opta/opta-family/opta
---

## Overview

In this tutorial, we will learn how to interface an Opta™ device with a USB memory stick for data logging. We will take readings from four analog input ports from an Opta™ device and store those readings in a file on the USB memory stick. We will also use the onboard LEDs of the Opta™ device to indicate the status of the data logging process to the user. 

## Goals

- Interface an Opta™ device with a USB memory stick.
- Read data from analog input ports of an Opta™ device and write the data to a file on the USB memory stick.
- USE the onboard LEDs of an Opta™ device to indicate different states and errors to the user. 

## Hardware and Software Requirements

### Hardware Requirements

- [Opta™](https://store.arduino.cc/collections/pro-family) (x1)
- USB-C® cable (x1)
- Compatible USB-C® memory stick, such as this one from Kingston®

### Software Requirements

- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2](https://www.arduino.cc/en/software), or [Arduino Web Editor](https://create.arduino.cc/editor)
- [`Arduino_USBHostMbed5`](https://github.com/arduino-libraries/Arduino_USBHostMbed5) library

## USB Memory Sticks

A USB memory stick, also called a Flash drive, is a data storage device that includes Flash memory with an integrated USB interface. It is typically removable, rewritable, and much smaller than other available storage options. File systems can store and retrieve data on a USB memory stick. In this tutorial, we will use the File Allocation Table (FAT) file system, which is supported by most operating and embedded systems today.

To communicate the USB devices on Opta™ devices, we will use the `Arduino_USBHostMbed5` library, which allows an Opta™ device to function as a USB host. To work with the FAT file system, we will use the `FATFileSystem` library, which is included with the `Arduino_USBHostMbed5` library.

## Instructions 

### Setting Up the Arduino IDE

### Writing Data to a USB Memory Stick

## Conclusion