---
author: 'Arduino'
description: 'This example demonstrates the use of the KeyboardController library.'
title: 'Arduino Due Keyboard Controller'
tags: [USB]
---


## Keyboard Controller

The Arduino Due has the ability to act as a USB host for peripherals such as a keyboard connected to the SerialUSB port. This example demonstrates the use of the KeyboardController library.

## Hardware Required

- [Arduino Due](https://store.arduino.cc/arduino-due) Board
- USB keyboard (note that keyboards that connect through an internal USB hub, like Apple keyboards, will not work)
- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software)).
- [USBHost library](https://www.arduino.cc/reference/en/libraries/usbhost/)

## Code

```arduino
/*

 Keyboard Controller HID Example

 Shows the output of a USB Keyboard connected to the USB

 controller of an Arduino Due Board.

 created 8 Oct 2012

 by Cristian Maglie

 */

// Require keyboard control library
#include <KeyboardController.h>

// Initialize USB Controller

USBHost usb;

// Attach keyboard controller to USB

KeyboardController keyboard(usb);

// This function intercepts key press
void keyPressed() {

  Serial.print("Pressed:  ");

  printKey();
}

// This function intercepts key release
void keyReleased() {

  Serial.print("Released: ");

  printKey();
}

void printKey() {

  // getOemKey() returns the OEM-code associated with the key

  Serial.print(" key:");

  Serial.print(keyboard.getOemKey());

  // getModifiers() returns a bits field with the modifiers-keys

  int mod = keyboard.getModifiers();

  Serial.print(" mod:");

  Serial.print(mod);

  Serial.print(" => ");

  if (mod & LeftCtrl)

    Serial.print("L-Ctrl ");

  if (mod & LeftShift)

    Serial.print("L-Shift ");

  if (mod & Alt)

    Serial.print("Alt ");

  if (mod & LeftCmd)

    Serial.print("L-Cmd ");

  if (mod & RightCtrl)

    Serial.print("R-Ctrl ");

  if (mod & RightShift)

    Serial.print("R-Shift ");

  if (mod & AltGr)

    Serial.print("AltGr ");

  if (mod & RightCmd)

    Serial.print("R-Cmd ");

  // getKey() returns the ASCII translation of OEM key

  // combined with modifiers.

  Serial.write(keyboard.getKey());

  Serial.println();
}

void setup()
{

  Serial.begin(115200);

  Serial.println("Program started");

  delay(200);
}

void loop()
{

  // Process USB tasks

  usb.Task();
}
```
