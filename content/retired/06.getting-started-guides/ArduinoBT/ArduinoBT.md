---
title: 'Getting Started with the Arduino BT'
description: 'The first steps to setting up your Arduino BT'
---

**This is a retired product.**

The Arduino BT is an Arduino board with built-in Bluetooth® module, allowing for wireless communication. To get started with the Arduino BT, follow the directions for the Arduino NG on your operating system ([Windows](https://arduino.cc/en/Guide/Windows), [MacOS](https://arduino.cc/en/Guide/macOS), [Linux](https://playground.arduino.cc/Learning/Linux)), with the following modifications:

- First, pair the Arduino BT with your computer and create a virtual serial port for it. Look for a Bluetooth® device called **ARDUINOBT** and the pass code is **12345**.

- Select **Arduino BT** from the **Tools | Board** menu of the Arduino environment.

When uploading to the Arduino BT, you may need to press the reset button on the board shortly before (or shortly after) clicking upload in the Arduino software.

### Information about the Arduino BT

In most respects, the Arduino BT is similar to the Arduino Diecimila. Here are the main differences of BT board (besides the fact that it communicates over Bluetooth® instead of USB):

- The Arduino BT is more fragile and easy to break than a regular Arduino board.

- **Don't power the board with more than 12 volts or reverse the polarity (power and ground pins) of your power supply, or you might kill the ATmega328P on the Arduino BT. Higher voltages or reversed polarity in the power supply can damage or destroy the board. The protection for reverse polarity connection is ONLY on the screw terminal.** The Arduino BT can, however, run with a minimum of 2.5 volts, making it easier to power with batteries.

- The microcontroller (an ATmega328P) on the Arduino BT is a physically smaller version of the chip on the USB Arduino boards. You can't remove it, so if you kill it, you need a new Arduino BT.

- There are two extra analog inputs on the Arduino BT (8 total). Two of these, however, are not connected to the pin headers on the board; you'll need to solder something to the pads next to the numbers "6" and "7".

- Pin 7 is connected to the reset pin of the Bluetooth® module; **don't use it for anything** (except resetting the module).

For more details, see the [Arduino BT hardware page](https://arduino.cc/en/Main/ArduinoBoardBluetooth).

### Using the Arduino BT

The on-board serial communication between the Bluetooth® module and the Arduino sketch (running on the ATmega328P) needs to be at 115200 baud (i.e. call Serial.begin(115200) in your setup() function). Communication between the Bluetooth® module and the computer can be at any baud rate.

Communication between the BT module and the computer can be temperamental. You might want to open the serial monitor a couple of seconds after resetting the board.

The text of the Arduino getting started guide is licensed under a
[Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/). Code samples in the guide are released into the public domain.
