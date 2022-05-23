---
title: 'Nano RP2040 Datalogger with MicroPython'
difficulty: easy
compatible-products: [nano-rp2040-connect]
description: 'Learn how to save data in .csv format on the Nano RP2040 Connect, using MicroPython.'
tags: 
  - Datalogger
  - MicroPython
author: 'Karl Söderby'
hardware:
  - hardware/03.nano/boards/nano-rp2040-connect
software:
  - web-editor
---

## Introduction 

The [Nano RP2040 Connect](https://store.arduino.cc/nano-rp2040-connect) board has on-board storage that allows you to turn the device into a data logger without any extra components. 

In order to utilize this feature, we need to install the latest release of [OpenMV's flavor of MicroPython](https://github.com/openmv/openmv/). 

This tutorial can be completed with only the Nano RP2040 board and open-source software.

## Goals

The goals of this tutorial are:

- Install OpenMV MicroPython firmware on the board.
- Learn how to save data in a `.csv` format directly on the Nano RP2040 Connect.

## Hardware & Software Needed

- [Thonny IDE](https://thonny.org/).
- [Arduino Nano RP2040 Connect](https://store.arduino.cc/nano-rp2040-connect).

## Install MicroPython

**1.** The first step is to install the latest version of the OpenMV firmware (MicroPython) on the Nano RP2040 board. This version is available through the link below:

- [OpenMV firmware v4.3.1. (download)](https://github.com/openmv/openmv/releases/download/v4.3.1/firmware_v4.3.1.zip)

**2.** Unzip the contents, and locate the `firmware.uf2` file inside of the **ARDUINO_NANO_RP2040_CONNECT** folder.

**3.** Force the bootloader on the Nano RP2040 Connect, by connecting a jumper wire between `GND` and `REC` pins as shown in the image below. When the mass storage device opens, drag the `firmware.uf2` onto it, and the latest version will install.

**4.** Install and open the [Thonny IDE](). Navigate to **Run > Select Interpreter** and choose the **"MicroPython(generic)"** from the list. Your board should now appear in the other dropdown menu:

![Thonny board/port selection.]()

If your board appears, it has been successful. In this case, it is called `Board in FS mode (/dev/cu.usbmodem11201)`. 

## Data Logger Example

Now that the OpenMV MicroPython firmware is installed on your device, and it is detected using Thonny, we can create our datalogger.

The script for the datalogger is quite basic, and has the following functionality:

- Create a `.csv` file
- Read the value of an analog pin, and log it, using the `file.write()` function.
- Repeat 25 times and then finish script.
- Each time a reading is recorded, the built-in LED flashes.

### Code

The script can be found below:

```py
import machine
from machine import Pin
import time

adc_pin = machine.Pin(29) 
adc = machine.ADC(adc_pin)
led = Pin(6, Pin.OUT)
readings = 0

file=open("data.csv","w")
file.write("data"+"\n")

while True:
    
    led.value(1)
    reading = adc.read_u16()     
    print("ADC: ",reading)
    
    time.sleep_ms(100)
    
    file.write(str(reading)+"\n")
    
    led.value(0)
    time.sleep_ms(100)
    readings += 1
    if readings >= 25:
        file.close()
        break
```

Copy paste this code into the Thonny editor, and click on the **Green Play Button (F5)**. The values recorded are also printed in the Shell, so we can compare it later.

When you run the script, the board should now start blinking fast, every 100 milliseconds, and it will do so 25 times (as is specified in the code, the number can be changed).

### Accessing Data

Once done, navigate to Finder / Explorer, and locate a drive called **"NO NAME"**. This should now include a `data.csv` file. This contains the 25 readings we just made by running the script.

![The "NO NAME" drive with a data.csv file.]()

