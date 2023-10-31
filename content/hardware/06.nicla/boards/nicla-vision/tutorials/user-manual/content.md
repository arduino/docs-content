---
title: 'Nicla Vision User Manual'
difficulty: beginner
compatible-products: [nicla-vision]
description: 'Learn about the hardware and software features of the Arduino® Nicla Vision.'
tags: 
  - Camera
  - ToF
  - IMU
  - User manual
  - RGB
  - Sensors
  - Machine Learning
author: 'Christopher Mendez'
hardware:
  - hardware/06.nicla/boards/nicla-vision
software:
  - ide-v1
  - ide-v2
  - web-editor
  - iot-cloud
---

## Overview

This user manual will guide you through a practical journey covering the most interesting features of the Arduino Nicla Vision. With this user manual, you will learn how to set up, configure and use this Arduino board.

## Hardware and Software Requirements
### Hardware Requirements

- [Nicla Vision](https://store.arduino.cc/products/nicla-vision) (x1)
- Micro USB cable (x1)

### Software Requirements

- [OpenMV IDE](https://openmv.io/pages/download)
- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2.0+](https://www.arduino.cc/en/software), or [Arduino Web Editor](https://create.arduino.cc/editor)
- To create custom Machine Learning models, the integrated Machine Learning Tools of the [Arduino Cloud](https://create.arduino.cc/iot/) are needed. In case you do not have an Arduino Cloud account, you will need to create one first.

## Product Overview

The Arduino® Nicla Vision is a ready-to-use, standalone camera for analyzing and processing images on the edge. Thanks to its 2 MP color camera, smart 6-axis motion sensor, integrated microphone and distance sensor, it is suitable for asset tracking, object recognition and predictive maintenance. Quickly implement sensor nodes to send collected data to the Arduino® Cloud (or third-party vendor services) via integrated Wi-Fi®/Bluetooth® LE connectivity.

### Board Architecture Overview

The Nicla Vision features a robust and efficient architecture that integrates a range of sensors packed into a tiny footprint. Nicla Vision combines a powerful STM32H747AII6 Dual ARM® Cortex® M7/M4 IC processor with a 2MP color camera that supports TinyML, as well as a smart 6-axis motion sensor, integrated PDM microphone and a Time of Flight distance sensor.

![Nicla Vision main components (top view)](assets/arch-top.png)
![Nicla Vision main components (bottom view)](assets/arch-bot.png)

Here is an overview of the board's architecture's main components shown in the images above:

- **Camera**: the Nicla Vision features a camera based on GC2145 Color rolling shutter image sensor. The GC2145 incorporates a 1616V x 1232H active pixel
array, on-chip 10-bit ADC, and image signal processor.
The 2MP GC2145 CMOS camera module is equipped with a 80°(DFOV) stock lens, 1.75 μm pixel size and a focal length of 2.2 mm. It supports RGB output format.
- **Microcontroller**: at the heart of the Nicla Vision is the dual-core STM32H747 (U1) including a Cortex® M7 running at 480 MHz and a Cortex® M4 running at 240 MHz. The two cores communicate via a Remote Procedure Call mechanism that allows calling functions on the other processor seamlessly.
- **Onboard advanced motion sensor**: the board features the LSM6DSOX, a smart IMU that includes a 3-axis accelerometer and a 3-axis gyroscope. The LSM6DSOX has a full-scale acceleration range of ±2/±4/±8/±16 g and an angular rate range of ±125/±250/±500/±1000/±2000 dps.
- **Onboard distance sensor**: the VL53L1CBV0FY Time-of-Flight sensor (U4) adds accurate and low power ranging capabilities to the Arduino® Nicla Vision. The invisible near infrared VCSEL laser (including the analog driver) is encapsulated together with receiving optics in an all-in-one small module located below the camera.
- **Digital Microphone**: the MP34DT05 digital MEMS microphone is omnidirectional and operates via a capacitive sensing element with a high (64 dB) signal-to-noise ratio. The sensing element, capable of detecting acoustic waves, is manufactured using a specialized silicon micromachining process dedicated to producing audio sensors (U6).
- **Wireless connectivity**: the Murata® LBEE5KL1DX-883 wireless module (U9) simultaneously provides Wi-Fi® and Bluetooth® connectivity in an ultra-small package based on the Cypress CYW4343W. The IEEE802.11 b/g/n Wi-Fi® interface can be operated as an access point (AP), station (STA) or dual-mode simultaneous AP/STA. It supports a maximum transfer rate of 65 Mbps. Bluetooth® interface supports Bluetooth® Classic and BLE. An integrated antenna circuitry switch allows a single external antenna (J6) to be shared between Wi-Fi® and Bluetooth®.
- **Power management**: the Nicla Vision is designed for ultra-low power operation, with efficient power management features that ensure minimal energy consumption even when using always-on motion recognition and image processing. The Nicla Vision features the PF1550 from NXP®; a highly integrated battery charge management integrated circuit (IC) designed for wearables and Internet of Things (IoT) devices. 
- **Security Elements**: the Arduino® Nicla Vision enables IC level edge-to-cloud security capability through the NXP SE050C2 Crypto chip (U8). This provides Common Criteria EAL 6+ security certification up to OS level, as well as RSA/ECC cryptographic algorithm support and credential storage.

### Board Core and Libraries

#### With Arduino IDE

The **Arduino Mbed OS Nicla Boards** core contains the libraries and examples you need to work with the board's components, such as its camera and IMU. To install the core for Nicla boards, navigate to **Tools > Board > Boards Manager** or click the Boards Manager icon in the left tab of the IDE. In the Boards Manager tab, search for `Nicla Vision` and install the latest `Arduino Mbed OS Nicla Boards` version.

![Installing the Arduino Mbed OS Nicla Boards core in the Arduino IDE](assets/bsp-install.png)

To update the bootloader firmware of your Nicla Vision,  go to **File > Examples > STM32H747_System > STM32H747_manageBootloader** and upload this sketch to your board.

![Example sketch location for bootloader update](assets/example-bootloader.png)

After the sketch is uploaded, follow the instructions in the Serial Monitor.

  ![Serial Monitor instructions and current bootloader info](assets/firmware-update.png)

#### With OpenMV IDE
Before you can start programming OpenMV scripts for the Nicla Vision, you need to download and install the OpenMV IDE.

Open the [OpenMV](https://openmv.io/pages/download) download page in your browser, download the latest version available for your operating system, and follow the instructions of the installer.

![OpenMV Download Page](assets/openmv-down.png)

Open the OpenMV IDE and connect the Nicla Vision to your computer via the USB cable if you have not done so yet.

![The OpenMV IDE after starting it](assets/first-open.png)

Click on the "connect" symbol at the bottom of the left toolbar.

![Click the connect button to attach the Nicla Vision to the OpenMV IDE](assets/click-connect.png)

If your Nicla Vision has not the latest firmware, a pop-up will ask you to install it. Your board will enter in DFU mode and it's green LED will start fading. 

Select `Install the latest release firmware`. This will install the latest OpenMV firmware on the Nicla Vision. You can leave the option of erasing the internal file system unselected and click `OK`.

![Install the latest version of the OpenMV firmware](assets/first-connect.png)

Nicla Vision's green LED will start flashing while the OpenMV firmware is being uploaded to the board. A loading bar will start showing you the flashing progress.

Wait until the green LED stops flashing and fading. You will see a message saying `DFU firmware update complete!` when the process is done.

![Installing firmware on Nicla Vision board in OpenMV](assets/flashing.png)

The board will start flashing its blue LED when it is ready to be connected. After confirming the completion dialog, the Nicla Vision should already be connected to the OpenMV IDE, otherwise click the "connect" button (plug symbol) once again (the blue blinking should stop).

![When the Nicla Vision is successfully connected a green play button appears](assets/ready-connected.png)

### Pinout

![Nicla Vision pinout](assets/simple-pinout.png)

The full pinout is available and downloadable as PDF from the link below:

- [Nicla Vision full pinout](https://docs.arduino.cc/resources/pinouts/ABX00051-full-pinout.pdf)

### Datasheet

The complete datasheet is available and downloadable as PDF from the link below:

- [Nicla Vision datasheet](https://docs.arduino.cc/resources/datasheets/ABX00051-datasheet.pdf)

### Schematics

The complete schematics are available and downloadable as PDF from the link below:

- [Nicla Vision schematics](https://docs.arduino.cc/resources/schematics/ABX00051-schematics.pdf)

### STEP Files

The complete STEP files are available and downloadable from the link below:

- [Nicla Vision STEP files](https://docs.arduino.cc/static/24f56d94c6040c9c3a4a187375cf7601/ABX00051-step.zip)

## First Use
### Powering the Board

The Nicla Vision can be powered by:

- Using a Micro USB cable (not included). 
- Using an external **5V power supply** connected to `VIN` pin (please, refer to the [board pinout section](#pinout) of the user manual).
- Using a **3.7V Lithium Polymer (Li-Po) battery** connected to the board through the onboard battery connector; the manufacturer part number of the battery connector is BM03B-ACHSS and its matching receptacle manufacturer part number is ACHR-03V-S. The **recommended minimum battery capacity for the Nicla Vision is 200 mAh**. A Li-Po battery with an integrated NTC thermistor is also recommended for thermal protection. 
- Using the onboard **ESLOV connector**, which has a dedicated 5V power line.

![Nicla Vision battery powered](assets/battery-power.png)

### Hello World Example

Let's program the Nicla Sense ME with the classic `hello world` example used in the Arduino ecosystem: the `Blink` sketch. We will use this example to verify the board's connection to the Arduino IDE and that the Nicla Sense ME core and the board itself are working as expected. 

Copy and paste the code below into a new sketch in the Arduino IDE.

```arduino
#include "Nicla_System.h"
void setup() {
  // Initialize LED_BUILTIN as an output (this will turn on the LED)
  pinMode(LED_BUILTIN, OUTPUT);
}
void loop() {
  // Turn the built-in LED off
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  // Turn the built-in LED on
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

For the Nicla Sense ME, the `LED_BUILTIN` macro represents **all the LEDs** of the built-in RGB LED of the board, shining in **white**.

To upload the code to the Nicla Sense ME, click the **Verify** button to compile the sketch and check for errors; then click the **Upload** button to program the board with the sketch.

![Uploading a sketch to the Nicla Sense ME in the Arduino IDE](assets/BOARD.png)

You should see now all the LEDs of the built-in RGB LED turn on for one second, then off for one second, repeatedly.

![Hello World example running in the Nicla Sense ME](assets/White-blink.gif)