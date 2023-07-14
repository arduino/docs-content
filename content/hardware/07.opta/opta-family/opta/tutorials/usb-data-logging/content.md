---
title: 'Getting Started with USB Data Logging on Opta™'
description: "Learn how to interface an Opta™ device with a USB memory stick for data logging."
difficulty: intermediate
tags:
  - Opta
  - USB Memory Stick
  - Arduino IDE
author: 'José Bagur'
software:
  - ide-v1
  - ide-v2
hardware:
  - hardware/07.opta/opta-family/opta
---

## Overview

In this tutorial, we will explore how to interface an Opta™ device with a USB memory stick to perform data logging. We will take readings from four analog input ports from an Opta™ device and store those readings in a `.txt` file on a USB memory stick. We will also use the onboard user button and user LEDs of the Opta™ device to start, finish and indicate the status of the data logging process to the user. 

## Goals

- Interface an Opta™ device with a USB memory stick.
- Read data from the analog input ports of an Opta™ device and write it to a `.txt` file on a USB memory stick.
- Use the onboard user button of an Opta™ device to start and finish the data logging process.
- Use the onboard user LEDs of an Opta™ device to indicate the different states and errors of the data logging process to the user.

## Hardware and Software Requirements

### Hardware Requirements

- [Opta™](https://store.arduino.cc/collections/pro-family/products/opta-wifi) (x1)
- [USB-C® cable](https://store.arduino.cc/products/usb-cable2in1-type-c) (x1)
- Compatible USB-C® memory stick (x1)

### Software Requirements

- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2.0+](https://www.arduino.cc/en/software), or [Arduino Web Editor](https://create.arduino.cc/editor)
- [`Arduino_USBHostMbed5`](https://github.com/arduino-libraries/Arduino_USBHostMbed5) library

## USB Memory Sticks

A USB memory stick, often referred to as a Flash drive, is a compact, removable, and rewritable data storage device that includes integrated Flash memory with a USB interface. Compared to other storage options, it's typically much smaller yet remarkably versatile. These devices employ file systems to manage data storage and retrieval; in this tutorial, we will use the [File Allocation Table (FAT) file system](https://en.wikipedia.org/wiki/File_Allocation_Table), which is supported by most contemporary operating and embedded systems.

To manage the communication between a USB memory stick and an Opta™ device, we will use the [`Arduino_USBHostMbed5` library](https://github.com/arduino-libraries/Arduino_USBHostMbed5), which allows an Opta™ device to function as a USB host. To work with the FAT file system, we will use the `FATFileSystem` library, which is included with the `Arduino_USBHostMbed5` library.

### Compatible USB Memory Sticks

Currently, the following USB memory sticks have been tested and are known to be fully compatible with Opta® devices:

- Kingston® DataTraveler® 80 M USB-C 256 GB Flash Drive
- SanDisk® Ultra® Dual Drive USB Type-C 64 GB Flash Drive
- SanDisk® Ultra® Dual Drive Go USB Type-C 64 GB Flash Drive

Before using with an Opta® device, all USB memory sticks were formatted with the `FAT32` file system.

**Note**:  It's recommended to use USB memory sticks with a storage capacity of 256 GB or less. If a memory stick has a storage capacity greater than 256 GB, it is advised to partition the memory stick to limit its accessible storage to 256 GB or less.

## Instructions 

### Setting Up the Arduino IDE 

This tutorial requires the latest version of the Arduino IDE; you can download it [here](https://www.arduino.cc/en/software). In the Arduino IDE, you need to install the core for Opta™ devices; this can be done by navigating to **Tools > Board > Boards Manager** or clicking the Boards Manager icon in the left tab of the IDE. In the Boards Manager tab, search for `opta` and install the latest release of the `Arduino Mbed OS Opta Boards`.

![Installing the Opta™ core in the Arduino IDE](assets/arduino-ide-1.png)

Now we are ready to start compiling and uploading Arduino sketches to an Opta™ device using the Arduino IDE. 

### Installing the Required Libraries 

This tutorial also requires the latest version of the `Arduino_USBHostMbed5` library installed on the Arduino IDE. This can be done by navigating to **Tools > Manage Libraries** or clicking the Library Manager icon in the left tab of the IDE. In the Library Manager tab, search for `Arduino_USBHostMbed5` and install the latest version.

![Installing libraries in the Arduino IDE](assets/arduino-ide-2.png)

### Writing Data to a USB Memory Stick

The example code shown below shows how to interface an Opta™ device with a USB memory stick, storing readings from four analog inputs into a file on the USB memory stick: 

```arduino
/**
  Opta USB data logging example sketch
  Name: usb_data_logging_opta.ino
  Purpose: This sketch logs data from four analog inputs of an Opta device 
  into a file on a USB memory stick. The data logging process starts when 
  the user button is pressed for 3 seconds and stops when the button is
  pressed again for 3 seconds. A Knight Rider LED pattern is used to indicate 
  the status of USB connection. Once the data logging is done, all the user 
  LEDs blink 10 times.

  @author Arduino PRO Content Team
  @version 1.0 07/06/23
*/

// Include necessary libraries for USB host and FAT file system functionality
#include <Arduino_USBHostMbed5.h>
#include <FATFileSystem.h>

// Create an instance of USBHostMSD to handle USB mass storage devices
USBHostMSD msd;

// Create an instance of the FATFileSystem class to handle the FAT file system on the USB mass storage device
mbed::FATFileSystem usb("KINGSTON");

// Define arrays for analog input pin numbers and built-in LEDs
const int analog_pins[] = { A0, A1, A2, A3 };
const int led_pins[] = { LED_D0, LED_D1, LED_D2, LED_D3 };

// Variables for time tracking without using delay() function (non-blocking)
unsigned long previousMillis = 0;
const long interval = 1000;

// File pointer for the data file
FILE *f;

// Knight Rider LED pattern variables
// 1 for left-to-right patterns, -1 for right-to-left pattern
int ledDirection = 1;
int currentLed = 0;

void setup() {
  // Set the Opta ADC resolution to 12-bits
  analogReadResolution(12);

  // Initialize and turn off the Opta user LEDs
  for (int i = 0; i < 4; i++) {
    pinMode(led_pins[i], OUTPUT);
    digitalWrite(led_pins[i], LOW);
  }

  // Initialize the Opta user button
  pinMode(BTN_USER, INPUT_PULLUP);
}

void loop() {
  // Flag indicating if the data logging process has started
  static bool dataLoggingStarted = false;

  // Check if the Opta user button is held down for 3 seconds to start data logging process
  if (!dataLoggingStarted) {
    if (digitalRead(BTN_USER) == LOW) {
      unsigned long buttonPressTime = millis();
      while (digitalRead(BTN_USER) == LOW) {}
      if (millis() - buttonPressTime >= 3000) {
        dataLoggingStarted = true;
      
        // Turn off all the Opta user LEDs
        for (int i = 0; i < 4; i++) {
          digitalWrite(led_pins[i], LOW);
        }
      }
    }
  }

  // Only execute the data logging process once dataLoggingStarted flag is TRUE
  if (dataLoggingStarted) {
    delay(1000);

    // Check if the Opta user button is held down for 3 seconds to stop data logging process
    if (digitalRead(BTN_USER) == LOW) {
      unsigned long buttonPressTime = millis();
      while (digitalRead(BTN_USER) == LOW) {}
      if (millis() - buttonPressTime >= 3000) {
        if (f != NULL) {
          fclose(f);
          dataLoggingStarted = false;
          // Blink all the Opta user LEDs 10 times to indicate that the data logging process has stopped
          for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 4; j++) {
              digitalWrite(led_pins[j], HIGH);
            }
            delay(500);
            for (int j = 0; j < 4; j++) {
              digitalWrite(led_pins[j], LOW);
            }
            delay(500);
          }
        }
      }
    }

    // Wait for USB mass storage device connection
    while (!msd.connect()) {
      // Knight Rider LED pattern indicating that Opta is waiting for a USB mass storage device connection
      for (int i = 0; i < 4; i++) {
        digitalWrite(led_pins[i], LOW);
      }

      digitalWrite(led_pins[currentLed], HIGH);
      delay(100);
      currentLed += ledDirection;

      if (currentLed == 3) {
        ledDirection = -1;
      } else if (currentLed == 0) {
        ledDirection = 1;
      }
    }

    // Turn off all the Opta user LEDs when changing state
    for (int i = 0; i < 4; i++) {
      digitalWrite(led_pins[i], LOW);
    }

    // Try to mount the file system on the USB mass storage device
    // If there's an error, blink an Opta user LED (LED_D1)
    int err = usb.mount(&msd);
    if (err) {
      while (1) {
        digitalWrite(led_pins[1], HIGH);
        delay(500);
        digitalWrite(led_pins[1], LOW);
        delay(500);
      }
    }

    // Open the data file on the USB device for writing
    // If there's an error, blink an Opta user LED (LED_D1)
    f = fopen("/KINGSTON/analog_inputs_data.txt", "w+");
    if (f == NULL) {
      while (1) {
        digitalWrite(led_pins[2], HIGH);
        delay(500);
        digitalWrite(led_pins[2], LOW);
        delay(500);
      }
    }

    // Take analog readings and write them to a .txt file every second
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
          error("- Error: %s (%d)\n", strerror(errno), -errno);
        }
      }

      // Flush and close the file output to ensure data is written to it
      fflush(f);
      fclose(f);
    }

    usb.unmount();
  }
}
```

Here is a step-by-step breakdown of the code shown above:

Import libraries:

- The necessary libraries are imported at the beginning of the code. `Arduino_USBHostMbed5` enables USB host functionality, while `FATFileSystem` allows us to interact with the FAT file system on the USB memory stick.

Define variables and instances:

- Instances for handling the USB mass storage device (`USBHostMSD msd`) and the file system (`mbed::FATFileSystem usb("KINGSTON")`) are created. Arrays are also created to store analog input pin numbers and the onboard LED numbers. Timing variables and a file pointer are also defined.

`setup()` function:

- The Opta™ device is initialized. The analog-to-digital converter's resolution is set, onboard LEDs are initialized, and a connection to the USB memory stick is established. If the USB memory stick is successfully connected and mounted, a file named "analog_inputs_data.txt" is opened in read/write mode.

Main `loop()` function:

- The connection between the Opta™ device and the USB memory stick is checked, and reconnection is made if both devices are disconnected. Then, readings are taken from the analog pins at an interval of one second, and those readings are written to a file on the USB memory stick. After a certain number of iterations, the file is closed, and one of the onboard LEDs is made to blink continuously.

## Conclusion

In this tutorial, you have learned how to interface an Opta™ device with a USB memory stick, read analog input data, and store it on the USB memory stick. You also learned how to use the onboard LEDs to display the status and error information to the user.