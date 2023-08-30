---
title: 'Getting Started with the GIGA Display Shield'
description: 'Learn how to set up and use the GIGA Display Shield and get an overview of it's features.'
author: Karl Söderby
tags: [Displays, LVGL, GIGA]
---

The [GIGA Display Shield](/hardware/giga-display-shield) is an accessory shield designed for the [GIGA R1 WiFi](/hardware/giga-r1) board. With it, you can render fast & sophisticated user interfaces on a **800x480** display with **touch support**.

In this guide you will learn how to set your board up with the GIGA R1 WiFi board & how to get started with the supported frameworks.

## Hardware & Software Needed

- [GIGA R1 WiFi](/hardware/giga-r1).
- [GIGA Display Shield](/hardware/giga-display-shield)
- [Arduino IDE](https://www.arduino.cc/en/software)

## Overview

There are three official libraries available to use the display & touch interface:
- [Arduino_H7_Video](https://github.com/arduino/ArduinoCore-mbed/tree/main/libraries/Arduino_H7_Video) - manages the video output and integrates third party libraries such as [LVGL](https://lvgl.io/) and [emWin](https://www.segger.com/products/user-interface/emwin/). This library is used to configure and initialize the display and to perform basic draw functions.
- [ArduinoGraphics]() - a graphics primitive library that provides draw, text and animation functions.
- [Arduino_GigaDisplayTouch](https://github.com/arduino-libraries/Arduino_GigaDisplayTouch) - to handle the touch interface of the display.

The above libraries provides a basic set of functionalities. To build more sophisticated UI's, frameworks such as [LVGL](https://lvgl.io/) is required.

The LVGL framework allows you to build user interfaces using existing widgets such as buttons, gauges, text fields, drop down menus and much more.  

***To get started with LVGL and get access to some useful examples, visit the [Guide to LVGL with GIGA Display Shield]() tutorial.***

## Installation

To use the GIGA Display Shield, you will need to have a GIGA R1 WiFi board. To use the GIGA R1 WiFi, you will need to install the GIGA core, which can be done directly in the [Arduino IDE]().

***Learn more at [Getting Started with GIGA R1 WiFi](/tutorials/giga-r1-wifi/giga-getting-started).***


## Hardware Setup

To use the GIGA Display Shield, mount it on the **bottom** side of the GIGA R1 WiFi board. The GIGA R1 WiFi board will be flipped upside down when the display is used.

![Bottom View](assets/mounted.png)

### Camera Connector

Located on the top side of the shield is a camera connector that enables when you connect it to the GIGA R1 WiFi board. 

## Microphone 


## IMU 

This shield has a built-in IMU module, the **BMI270**. To use this module, you can follow the tutorial through the link below:
- []
