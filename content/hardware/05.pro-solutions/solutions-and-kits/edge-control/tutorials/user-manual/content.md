---
title: 'Edge Control User Manual'
difficulty: beginner
compatible-products: [edge-control]
description: 'Learn about the hardware and software features of the Arduino® Edge Control.'
tags: 
  - Cheat sheet
  - User manual
  - Agriculture
  - Sensors
  - Smart Farming
author: 'Christopher Mendez'
hardware:
  - hardware/05.pro-solutions/solutions-and-kits/edge-control
software:
  - ide-v1
  - ide-v2
  - web-editor
  - iot-cloud
---

## Overview

This user manual will guide you through a practical journey covering the most interesting features of the Arduino Edge Control. With this user manual, you will learn how to set up, configure and use this Arduino board.

## Hardware and Software Requirements
### Hardware Requirements

- [Arduino Edge Control](https://store.arduino.cc/products/arduino-edge-control) (x1)
- Micro USB cable (x1)
- External power source: a 12V SLA battery or 12V power supply (x1)

### Software Requirements

- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2.0+](https://www.arduino.cc/en/software), or [Arduino Web Editor](https://create.arduino.cc/editor)

## Product Overview

The Edge Control board is a versatile tool that allows agriculturalists to develop creative and innovative solutions for agriculture by harnessing modern technology. This board is designed to address the needs of precision farming. It provides a low power control system, suitable for irrigation with modular connectivity. Equipped with latching outputs and solid state relays, it becomes an ideal choice for controlling motorized or solenoid valves, among many other devices. As inputs, it manages 0-5V analog sensors, 4-20mA sensors, and Watermark soil moisture sensors, a variety that handles most of the agricultural needs. All this and more makes the Edge Control the perfect option for your 4.0 Agriculture industry. 

### Board Architecture Overview

The Edge Control features a robust and efficient architecture that integrates a wide range of sensors inputs and ready-to-use control outputs for industrial farming field devices.

![Edge Control main components](assets/top-view.png)

Here is an overview of the board's architecture's main components shown in the image above:

- **Microcontroller**: at the heart of the Edge Control is the nRF52840, a powerful and versatile System-on-Chip (SoC) from Nordic® Semiconductor. The nRF52840 is built around a 32-bit Arm® Cortex®-M4 processor running at 64 MHz.
- **MKR slots**: the on-board MKR slots 1 & 2 can be used to connect Arduino MKR boards to extend the capabilities such as connectivity through LoRa, Wi-Fi, 2G/3G/CatM1/NBIoT, and Sigfox.
- **Storage**: the board includes both a microSD card socket and an additional 2MB Flash memory for data storage. Both are directly connected to the main processor via a SPI interface.
- **Power management**: the Edge Control is designed for ultra-low power operation, with efficient power management features that ensure minimal energy consumption. It can operate for up to 34 months on a 12V/5Ah battery. Equipped with several buck and boost converters supplying a variety of output voltages from 19V DC to 3.3V DC. The LT3652 solar panel battery charger features a Maximum Power Point Tracker (MPPT) taking the best performance out of the solar panels.
- **Interfaces**: through the different terminal blocks, the board give access to several standardized sensors inputs like 0-5V, 4-20mA and watermark sensors. Also, it is equipped with drivered latching outputs, and relay contacts ready to manage high power external devices.

### Board Core and Libraries

To install the core for the Edge Control, navigate to **Tools > Board > Boards Manager** or click the Boards Manager icon in the left tab of the IDE. In the Boards Manager tab, search for `Edge Control` and install the latest `Arduino Mbed OS Edge Boards` version.

![Installing the Arduino Mbed OS Edge Boards core in the Arduino IDE bootloader](assets/bsp-install.png)

The **Arduino_EdgeControl** library contains the examples you need to work with the board's components, such as the different sensors, outputs and adds on like the LCD included with the [Enclosure Kit](https://store-usa.arduino.cc/products/edge-control-enclosure-kit?selectedStore=us).

![Installing the Arduino Edge Control library](assets/library-install.png)

### Pinout

![Edge Control pinout](assets/simple-pinout.png)

The full pinout is available and downloadable as PDF from the link below:

- [Edge Control pinout](https://docs.arduino.cc/resources/pinouts/AKX00034-full-pinout.pdf)

### Datasheet

The complete datasheet is available and downloadable as PDF from the link below:

- [Edge Control datasheet](https://docs.arduino.cc/resources/datasheets/AKX00034-datasheet.pdf)

### Schematics

The complete schematics are available and downloadable as PDF from the link below:

- [Edge Control schematics](https://docs.arduino.cc/resources/schematics/AKX00044-schematics.pdf)

### STEP Files

The complete STEP files are available and downloadable from the link below:

- [Edge Control STEP files](https://docs.arduino.cc/static/38d409dd238978baf03b79eac9bb752f/AKX00044-step.zip)

## First Use
### Powering the Board

The Edge Control can be powered by:

- Using a Micro USB cable (not included). 
- Using an external **12V power supply** connected to `BATT+` pin and `GND`.(please, refer to the [board pinout section](#pinout) of the user manual).
- Using a **12V lead-acid battery** connected to `BATT+` pin and `GND`. **It can be powered for up to 34 months on a 12V/5Ah battery**.
- Using a whole **off grid** power system including an **18V Solar Panel** and a **12V lead-acid battery**.

![Edge Control powered by external power supply](assets/ext-power-v2.png)
![Edge Control solar and battery powered](assets/green-power-v2.png)

### Hello World Example

Let's program the Edge Control with the classic `hello world` example used in the Arduino ecosystem: the `Blink` sketch. We will use this example to verify the board's connection to the Arduino IDE and that the Edge control core and the board itself are working as expected. 

There are two ways to program this example in the board:

- Navigate to **File > Examples > Arduino_EdgeControl > Basic > Blink.**
- Copy and paste the code below into a new sketch in the Arduino IDE.

```arduino
#include <Arduino_EdgeControl.h>

void setup() {
  Serial.begin(9600);

  auto startNow = millis() + 2500;
  while (!Serial && millis() < startNow)
    ;

  delay(1000);
  Serial.println("Hello, Challenge!");

  Power.on(PWR_3V3);
  Power.on(PWR_VBAT);

  Wire.begin();

  delay(500);

  Serial.print("IO Expander initializazion ");
  if (!Expander.begin()) {
    Serial.println("failed.");
    Serial.println("Please, be sure to enable gated 3V3 and 5V power rails");
    Serial.println("via Power.on(PWR_3V3) and Power.on(PWR_VBAT).");
  }
  Serial.println("succeeded.");

  Expander.pinMode(EXP_LED1, OUTPUT);
}

void loop() {
  Serial.println("Blink");
  Expander.digitalWrite(EXP_LED1, LOW);
  delay(500);
  Expander.digitalWrite(EXP_LED1, HIGH);
  delay(500);
}
```

For the Edge Control, the `EXP_LED1` macro represents the **Green LED** of the of the board.

The custom power management of the Edge Control lets you turn on just the board peripherals and power rails you need, as the LED is connected to the IO Expander is needed to enable the 3.3v and battery source, also the expander using these functions:

```arduino
Power.on(PWR_3V3);
Power.on(PWR_VBAT);
.
.
.
Expander.begin();
```

To upload the code to the Edge Control, click the **Verify** button to compile the sketch and check for errors; then click the **Upload** button to program the board with the sketch.

![Uploading a sketch to the Edge Control in the Arduino IDE](assets/board-selection.png)

***The Edge Control should be powered by an external power source or a battery so the blink works.***

You should see now the onboard LED turn on for half a second, then off, repeatedly.

![Hello World example running in the Edge Control](assets/Blink.gif)

