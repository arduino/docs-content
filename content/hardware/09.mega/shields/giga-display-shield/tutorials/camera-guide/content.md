---
title: Guide for the Camera Connector on the Giga Display Shield
description: 'Learn how to use the camera connector with the GIGA display shield'
author: Benjamin Dannegård
tags: [Display, Camera]
---


## Introduction

The Giga Display shield comes with an arducam camera connector. In this tutorial we will go through what cameras are compatible with the Display shield, how to connect the camera and how to run a sketch that will take a picture and display it on the screen.

## Hardware & Software Needed

- [GIGA R1 WiFi](/hardware/giga-r1).
- [GIGA Display Shield]()
- [Arduino IDE](https://www.arduino.cc/en/software)
- GC2145, HM01B0 or HM0360

## Downloading the Library and Core

The Arduino Mbed OS Giga Boards core contains the libraries and example you need to work with the shields camera connector. To install the core for Giga boards, navigate to **Tools > Board > Boards Manager** or click the Boards Manager icon in the left tab of the IDE. In the Boards Manager tab, search for giga and install the latest Arduino Mbed OS Giga Boards version.

## Compatible Cameras

The Giga Display shield is compatible with the following cameras:

- [GC2145](https://www.arducam.com/product/2mp-gc2145-color-dvp-camera-module-for-arduino-giga-r1-wifi-board/)
- [HM01B0](https://www.arducam.com/product/hm01b0-qvga-monochrome-dvp-camera-module-for-arduino-giga-r1-wifi-board/)
- [HM0360](https://www.arducam.com/product/hm0360-vga-monochrome-dvp-camera-module-for-arduino-giga-r1-wifi-board/)

Connect the camera to the connector on the front of the display shield as shown in the image below.

![Camera connected to the Giga display shield]()


## Example Code

Open the example sketch by going to **File->Examples->Camera->GigaCameraDisplay** in the Arduino IDE. Whichever of the compatible cameras you are using the sketch will include libraries and defenitions for them all, meaning no modification to the sketch is necessary to get it working. The sketch will capture frames into the framebuffer and then print the captured frame onto the display. The LED will then blink 20 times and re-do the process. 

## Conclusion

This tutorial went through how to connect a compatible camera to the shield and also how to test it out quickly with the example sketch included in the core.

