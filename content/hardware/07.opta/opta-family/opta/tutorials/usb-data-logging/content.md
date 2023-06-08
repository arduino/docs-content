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

This tutorial requires the latest version of the Arduino IDE; we can download it [here](https://www.arduino.cc/en/software). In the Arduino IDE, we need to install the core for Opta™ devices; this can be done by navigating to **Tools > Board > Boards Manager** or clicking the Boards Manager icon in the left tab of the IDE. In the Boards Manager tab, search for `opta` and install the latest `Arduino Mbed OS Opta Boards` version.

![Installing the Opta™ core in the Arduino IDE](assets/arduino-ide-1.png)

Now we are ready to start compiling and uploading Arduino sketches to an Opta™ device using the Arduino IDE. 

### Installing the Libraries 

This tutorial also requires the latest version of the `Arduino_USBHostMbed5` library installed on the Arduino IDE. This can be done by navigating to **Tools > Manage Libraries** or clicking the Library Manager icon in the left tab of the IDE. In the Library Manager tab, search for `Arduino_USBHostMbed5` and install the latest version.

![Installing libraries in the Arduino IDE](assets/arduino-ide-2.png)

### Writing Data to a USB Memory Stick

The example code shown below shows how to interface an Opta™ device with a USB memory stick, storing readings from four analog inputs into a file on the USB memory stick: 

```arduino
/**
  Opta USB data logging example sketch
  Name: usb_data_logging_opta.ino
  Purpose: Sketch stores readings from four analog inputs of an Opta device into a file on a USB memory stick 

  @author Arduino PRO Content Team
  @version 1.0 07/06/23
*/

// Include necessary libraries for USB host and FAT file system functionality
#include <Arduino_USBHostMbed5.h>
#include <FATFileSystem.h>

// Create an instance of USBHostMSD to handle USB mass storage devices
USBHostMSD msd;

// Create an instance of the FATFileSystem class to handle the file system on the device
mbed::FATFileSystem usb("KINGSTON");

// Define arrays for analog input pin numbers and built-in LEDs
const int analog_pins[] = { A0, A1, A2, A3 };
const int led_pins[] = { LED_D0, LED_D1, LED_D2, LED_D3 };

// Variables for time tracking without using delay() function
unsigned long previousMillis = 0;
const long interval = 1000;

// Variables to control the maximum number of write operations
const long maxIterations = 5;
long iterationCount = 0;

// File pointer for the data file
FILE *f;

void setup() {
  // Set the ADC resolution to 12 bits
  analogReadResolution(12);

  // Initialize LED pins
  for (int i = 0; i < 4; i++) {
    pinMode(led_pins[i], OUTPUT);
    digitalWrite(led_pins[i], LOW);
  }

  // Wait for USB mass storage device connection
  while (!msd.connect()) {
    digitalWrite(led_pins[0], HIGH);  // Blink LED to indicate waiting
    delay(500);
    digitalWrite(led_pins[0], LOW);
    delay(500);
  }

  // Try to mount the file system on the device
  int err = usb.mount(&msd);
  if (err) {  // If there's an error, blink a different LED
    while (1) {
      digitalWrite(led_pins[1], HIGH);
      delay(500);
      digitalWrite(led_pins[1], LOW);
      delay(500);
    }
  }

  // Open the data file on the USB device for writing
  f = fopen("/KINGSTON/analog_inputs_data.txt", "w+");
  if (f == NULL) {  // If there's an error, blink another LED
    while (1) {
      digitalWrite(led_pins[2], HIGH);
      delay(500);
      digitalWrite(led_pins[2], LOW);
      delay(500);
    }
  }
}

void loop() {
  delay(1000);

  // Check if the device is still connected and try to reconnect if not
  if (!msd.connected()) {
    msd.connect();
  }

  // Take analog readings and write to file every second
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

    // Loop over the analog pins, read values, and write to the data file
    for (int i = 0; i < 4; i++) {
      int value = analogRead(analog_pins[i]);

      // Write the analog reading to the file
      if (i < 3) {
        fprintf(f, "Pin A%d: %d, ", i, value);
      } else {
        fprintf(f, "Pin A%d: %d\n", i, value);
      }

      // Check if there was an error writing to the file
      if (ferror(f)) {
        error("error: %s (%d)\n", strerror(errno), -errno);
      }
    }

    // Flush the file output
    fflush(f);

    // If we have reached the maximum number of iterations, close the file
    iterationCount++;
    if (iterationCount >= maxIterations) {
      fclose(f);

      // Indicate completion by blinking another LED
      while (1) {
        digitalWrite(led_pins[3], HIGH);
        delay(500);
        digitalWrite(led_pins[3], LOW);
        delay(500);
      }
    }
  }
}
```

## Conclusion