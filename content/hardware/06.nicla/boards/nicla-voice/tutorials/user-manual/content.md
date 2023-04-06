---
title: 'Nicla Voice User Manual'
difficulty: beginner
compatible-products: [nicla-vision]
description: 'Learn about the features of the Nicla Voice'
tags: 
  - IMU
  - Cheat sheet
  - RGB
  - Communication
author: 'Benjamin Dannegård'
hardware:
  - hardware/06.nicla/boards/nicla-voice
software:
  - ide-v1
  - ide-v2
  - web-editor
---

## Overview

Learn how to set up the Arduino Nicla Voice and get a quick overview of the components. Obtain information regarding pins and how to use the different sensors.

### Hardware & Software Needed

- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software)).
- [Arduino Nicla Voice](https://store.arduino.cc/nicla-voice) (x1)
- [Arduino Cloud](https://cloud.arduino.cc/)
- USB cable
- Machine Learning Tools

## Product overview

### 6-Axis IMU BMI270

The IMU module is a highly integrated, low power inertial measurement unit that combines precise acceleration and angular rate (gyroscopic) measurement with intelligent on-chip motion-triggered interrupt features.

[BMI270 datasheet](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmi270-ds000.pdf)

### High performance microphone IM69D130

The IM69D130 microphone is designed for applications where low self-noise (high SNR), wide dynamic range, low distortions
and a high acoustic overload point is required. Infineon's Dual Backplate MEMS technology is based on a miniaturized symmetrical microphone design, similar to what is utilized in studio condenser microphones, which results in high linearity of the output signal within a dynamic range of 105dB.

[IM69D130 datasheet](https://www.infineon.com/dgdl/Infineon-IM69D130-DS-v01_00-EN.pdf?fileId=5546d462602a9dc801607a0e46511a2e)

### Bluetooth® Low Energy ANNA-B112

The ANNA-B112 is an ultra-small, high-performing, standalone Bluetooth low energy module. The System-in-Package (SiP) module features Bluetooth 5, a powerful Arm® Cortex®-M4 microprocessor with FPU, with state-of-the-art power performance.

[ANNA-B112 datasheet](https://content.u-blox.com/sites/default/files/ANNA-B112_DataSheet_UBX-18011707.pdf)

### Most important libraries

The Mbed Nicla Core contains the most important libraries for the Nicla Voice. If you need assistant with installing the Mbed OS Nicla core, [visit this page.](https://docs.arduino.cc/software/ide-v1/tutorials/getting-started/cores/arduino-mbed_nicla)

### Datasheet

[View the full Nicla Voice datasheet here](assets/ABX00061-datasheet.pdf)

### Pinout

Here you can see the full pinout for the Nicla Voice:

![Pinout](assets/nicla-voice-pinout.png)

### Schematics

[Nicla Voice Schematics](assets/ABX00061-schematics.pdf)

### STEP files

[STEP files for the Nicla Voice](assets/ABX00061-step.zip)


## First use

### Power up the board:

The board can be powered up by connecting a Micro usb to the usb connector on the board. It can also be powered with batteries??

Micro USB
Battery

### Alexa demo

The board will come pre-flashed with an Alexa demo. To try this out simply power up the board by using a micro usb or a battery. When the board is powered try saying "Hey Alexa" close to the board. It should now blink when the phrase is recognized.

### Getting started with Voice recognition

To find out how to create a customizable Machine Learning model for voice recognition, please have a look at our [Getting Started with Nicla Voice tutorial.](https://docs.arduino.cc/tutorials/nicla-voice/getting-started-ml)

### Getting started with Motion recognition

To find out how to create a customizable Machine Learning model for motion recognition, please have a look at our []()

## Pins

Pinout image at the beginning

### Analog pins

The Nicla Voice has 2 analog pins (`ADC1` on pin 8 and `ADC2` on pin 7), that can be used through the `analogRead()` function.

```arduino
int value = analogRead(pin);
```

### Digital pins

To enable the digital pins we have to use `nicla::enable3V3LDO` or `nicla::enable1V8LDO` at the begining of our sketch.

```arduino

```


### PWM pins

Not sure what pins are PWM enabled??

```arduino
analogWrite(pin, value);
```

## Sensors

### Microphone (NDP120 Example)

You can test the Microphone using the NDP library built into the core. First select the Nicla Vision as a board in the Arduino IDE and select the correct port the board is connected to. Now navigate to **File->Examples->NDP->(FIND GOOD EXAMPLE???)**

### IMU (NDP120 Example)

You can test the IMU using the NDP library built into the core. First select the Nicla Vision as a board in the Arduino IDE and select the correct port the board is connected to. Now navigate to **File->Examples->NDP->IMUDemo** in the Arduino IDE. This will open a sketch that is ready to be uploaded to your board. This example will????

## Actuators

### RGB LED

The Nicla Voice features a built-in RGB that can be utilized as a feedback component for applications. The LED is connected through I2C, therefore specific functions need to be used to operate the LED colors.

The Nicla System header is required to use the RGB LED.

```arduino
#include "Nicla_System.h"
```

Since the functions are scoped under a specific Class name called "nicla", you need to explicitly write it before each statement. The LEDs need to be started along with the Nicla inside `void setup()`:

```arduino
nicla::begin();
nicla::leds.begin();
```

Now the complete sketch for blinking the LED can look like this:

```arduino
#include "Nicla_System.h"

void setup() {
  nicla::begin();
  nicla::leds.begin();
}

void loop() {
  nicla::leds.setColor(green);
  delay(1000);
  nicla::leds.setColor(off);
  delay(1000);
}
```

This will blink the green LED on the board. the color can easily be changed in the `nicla::leds.setColor()` statement by entering another color inside the parentheses. It can be set as green, blue or red.

## Communication 

### SPI

The pins used for SPI (Serial Peripheral Interface) on the Nicla Voice are the following:

- CS: Digital pin 6
- CIPO: Digtial pin 7
- COPI: Digital pin 8
- SCLK: Digital pin 9

You can refer to the pinout above to find them on the board.

To use SPI, you first need to include the [SPI](https://www.arduino.cc/en/reference/SPI) library.

```arduino
#include <SPI.h>
```

Inside `void setup()` you need to initialize the library.

```arduino
SPI.begin();
```

And to write to the device:

```arduino
digitalWrite(chipSelectPin, LOW); //pull down the CS pin
  
  SPI.transfer(address); // address for device, for example 0x00
  SPI.transfer(value); // value to write

  digitalWrite(chipSelectPin, HIGH); // pull up the CS pin
```

### I2C

The pins used for I2C (Inter-Integrated Circuit) on the Nicla Voice are the following:

- SDA: Digital pin 4
- SCL: Digital pin 3

You can refer to the pinout above to find the pins on the board.

To use I2C, you can use the [Wire](https://www.arduino.cc/en/Reference/wire) library, which you need to include at the top of your sketch.

```arduino
#include <Wire.h>
```

Inside `void setup()` you need to initialize the library.

```arduino
Wire.begin();
```

And to write something to a device connected via I2C, you can use the following commands:

```arduino
Wire.beginTransmission(1); //begin transmit to device 1
  Wire.write(byte(0x00)); //send instruction byte 
  Wire.write(val); //send a value
  Wire.endTransmission(); //stop transmit
```

### UART

The pins used for UART (Universal asynchronous receiver-transmitter) are the following:

- TX: LPIO2_EXT (Pin 4)
- RX: LPIO1_EXT (Pin 3)

You can refer to the pinout above to find the pins on the board.

To send and receive data through UART, you will first need to set the baud rate inside `void setup()`.

```arduino
Serial1.begin(9600);
```

To read incoming data, you can use a `while loop()` to read each individual character and add it to a string.

```arduino
while(Serial1.available()){
    delay(2);
    char c = Serial1.read();
    incoming += c;
  }
```

And to write something, you can use the following command:

```arduino
Serial1.write("Hello world!");
```

### BLE

### ESLOV

## Additional tutorials / Application notes
