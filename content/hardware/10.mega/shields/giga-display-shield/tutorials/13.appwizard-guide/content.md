---
title: GIGA Display Shield app wizard Guide
description: 'Learn how to use Seggers App Wizard with the GIGA Display Shield.'
author: Benjamin Dannegård
tags: [Display, appwizard, segger, GUI]
---

## Introduction

Segger's app wizard is a graphical framework for building powerful UIs, and is fully compatible with the GIGA Display Shield. It allows you to build UIs, using pre-made widgets like buttons, images, loading bars, sliders, checkboxes, etc. It also allows you to fully customize the screenspace on the display. In this guide, we will go through some of the different components, so you can learn how to best implement it in your projects.

![Appwizard full demo running on the GIGA Display Shield](assets/)

## Hardware & Software Needed

- [Arduino GIGA R1 WiFi](https://store.arduino.cc/products/giga-r1-wifi)
- [Arduino GIGA Display Shield](https://store.arduino.cc/products/giga-display-shield)
- [Arduino IDE](https://www.arduino.cc/en/software)
- [App Wizard](https://www.segger.com/products/user-interface/emwin/tools/appwizard/)
- [emWin Arduino Library](https://github.com/SEGGERMicro/emWin-Arduino-Library/)

## Downloading the Library and Core

The GIGA R1 core includes the [Arduino_H7_Video](https://github.com/arduino/ArduinoCore-mbed/tree/main/libraries/Arduino_H7_Video) library that handles the display.

In this guide, we will be using three different libraries:
- [Arduino_H7_Video](https://github.com/arduino/ArduinoCore-mbed/tree/main/libraries/Arduino_H7_Video), this one is bundled with the core, so make sure you have the latest version of the [Mbed core](https://github.com/arduino/ArduinoCore-mbed) installed.
- [Arduino_GigaDisplayTouch](https://www.arduino.cc/reference/en/libraries/arduino_gigadisplaytouch/), handles touch on the GIGA Display Shield
- [emWin Arduino Library](https://github.com/SEGGERMicro/emWin-Arduino-Library/)

To install this, open the library manager and install the latest version by searching for **"Arduino_GigaDisplayTouch"**.

## Creating an App Wizard project

First go to  **File -> New Project** to start your new project. Here we need to configure certain settings so it will work on the GIGA Display Shield. Set the  display size x to **480** and display size y to **800**. Then we need to disable the **Enable simulation** and **Generate loop in MainTask()** options. It should look like the image below.

![Create project settings]()

## Adding elements to the project

### Button

### Slider

### Gauge

## Exporting the project

## 

## Conclusion

This guide went through the building blocks of the different components that can be implemented with emWin. To see these examples in a full running example sketch go to **File > Examples > Arduino_H7_Video > emWinDemo**.

![Example in the IDE](assets/example-in-ide.png)

This demo sketch will show the different components using a screen manager in a 2x2 grid.

## Next Step
emWin is a comprehensive library and GUI framework that has a lot of customizability, if you are interested in playing around more with it, you can find many different examples and widgets on the official website for [Segger® emWin](https://wiki.segger.com/Main_Page). The code on the website can easily be adapted into a sketch for the GIGA Display Shield.
