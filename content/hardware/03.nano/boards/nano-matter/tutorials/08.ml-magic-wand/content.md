---
title: 'ML Magic Wand with the Arduino Nano Matter'
difficulty: beginner
compatible-products: [nano-matter]
description: 'Learn how to build a Gesture Recognition Magic Wand using the Arduino Nano Matter'
tags:
  - AI
  - ML
  - IMU
  - Modulino
  - Matter

author: 'Christopher Méndez'
hardware:
  - hardware/03.nano/boards/nano-matter
software:
  - ide-v1
  - ide-v2
  - web-editor
  - iot-cloud
---

## Overview

This tutorial describes how to build a gesture recognition system based on a machine learning model using TensorFlow and the Arduino Nano Matter.

![Thumbnail](assets/)

The Arduino Nano Matter acts as a digital magic wand 🪄, where sensor data from its movements is processed by a model to classify and detect specific gestures. The inference results will tur

## Hardware and Software Requirements
### Hardware Requirements

- [Arduino Nano Matter](https://store.arduino.cc/products/nano-matter) (x1)
- Nano Connector Carrier (x1)
- Modulino Movement (x1)
- Modulino Pixels (x1)
- Qwiic cables (x2)
- [USB-C® cable](https://store.arduino.cc/products/usb-cable2in1-type-c) (x1)
- Custom 3D printed parts

### Software Requirements

- [Arduino IDE 2.0+](https://www.arduino.cc/en/software) or [Arduino Cloud Editor](https://create.arduino.cc/editor)
- [Modulino library](https://github.com/arduino-libraries/Modulino). This library adds the support for the Modulinos, you can install it from the **Library Manager** in the Arduino IDE.
- [Silicon Labs core](https://github.com/SiliconLabs/arduino). This enables the Silicon Labs hardware including the Arduino Nano Matter support. You can install it from the **Boards Manager** in the Arduino IDE. 
