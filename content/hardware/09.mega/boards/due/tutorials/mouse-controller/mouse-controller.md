---
title: 'Mouse Controller'
difficulty: intermediate
description: 'Use the Arduino Due as a USB host for a mouse.'
tags: 
  - USB Host
  - Computer Mice
libraries:
  - name: USBHost
    url: https://www.arduino.cc/reference/en/libraries/usbhost/
hardware:
  - hardware/02.hero/boards/due
software:
  - ide-v1
  - ide-v2
  - web-editor
author: "Arduino"
---

## Introduction

The Arduino Due has the ability to act as a USB host for peripherals such as mice connected to the SerialUSB port. This example demonstrates the use of the  MouseController library.


## Goals

- Learn how to use the Arduino Due as a USB host for a mouse.

### Hardware & Software Needed

- [Arduino Due](https://store.arduino.cc/arduino-due) Board

- USB mouse
- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software)).
- [USBHost library](https://www.arduino.cc/reference/en/libraries/usbhost/)

### The Circuit

There is no circuit for this tutorial. Simply connect your Arduino Due with the desired USB mouse.


## Programming the Board

**1.** First, let's make sure we have correct the drivers installed. If we are using the Web Editor, we do not need to install anything. If we are using an offline editor, we need to install it manually. This can be done by navigating to **Tools > Board > Board Manager...**. Here we need to look for the **Arduino SAM boards (32-bits ARM Cortex-M3)** and install it. 

**2.** Now, we need to install the libraries needed. Simply go to **Tools > Manage libraries...** and search for **USBHost** and install it.


The sketch can be found in the snippet below. Upload the sketch to the board.

## Code
Before we begin, let's take a look at some of the core functions in the program:

- `USBHost` - USBHost is the base class for all calls that rely on USB host communication. When invoked, it initializes a USB controller.

- `MouseController mouse(usb);` - MouseController is the class for all calls to the USBHost relating to an attached mouse.
  
- `mouseMoved()` - A function that is called whenever a connected USB mouse moves.

```arduino
/*

 Mouse Controller Example

 Shows the output of a USB Mouse connected to

 the Native USB port on an Arduino Due Board.

 created 8 Oct 2012

 by Cristian Maglie

 http://arduino.cc/en/Tutorial/MouseController

 This samlple code is part of the public domain.

 */

// Require mouse control library
#include <MouseController.h>

// Initialize USB Controller

USBHost usb;

// Attach mouse controller to USB

MouseController mouse(usb);

// variables for mouse button states
boolean leftButton = false;
boolean middleButton = false;
boolean rightButton = false;

// This function intercepts mouse movements
void mouseMoved() {

  Serial.print("Move: ");

  Serial.print(mouse.getXChange());

  Serial.print(", ");

  Serial.println(mouse.getYChange());
}

// This function intercepts mouse movements while a button is pressed
void mouseDragged() {

  Serial.print("DRAG: ");

  Serial.print(mouse.getXChange());

  Serial.print(", ");

  Serial.println(mouse.getYChange());
}

// This function intercepts mouse button press
void mousePressed() {

  Serial.print("Pressed: ");

  if (mouse.getButton(LEFT_BUTTON)){

    Serial.print("L");

    leftButton = true;

  }

  if (mouse.getButton(MIDDLE_BUTTON)){

    Serial.print("M");

    middleButton = true;

  }

  if (mouse.getButton(RIGHT_BUTTON)){

    Serial.print("R");

    Serial.println();

    rightButton = true;

  }
}

// This function intercepts mouse button release
void mouseReleased() {

  Serial.print("Released: ");

  if (!mouse.getButton(LEFT_BUTTON) && left==true) {

    Serial.print("L");

    leftButton = false;

  }

  if (!mouse.getButton(MIDDLE_BUTTON) && middle==true) {

    Serial.print("M");

    middleButton = false;

  }

  if (!mouse.getButton(RIGHT_BUTTON) && right==true) {

    Serial.print("R");

    rightButton = false;

  }

  Serial.println();
}

void setup()
{

  Serial.begin(9600);

  Serial.println("Program started");

  delay(200);
}

void loop()
{

  // Process USB tasks

  usb.Task();
}


```

## Testing It Out

After you have uploaded the code, plug your mouse into the Native USB port on the Due. It enables the Due to emulate a USB mouse or keyboard to an attached computer. In the **Arduino IDE**, open the serial monitor and start clicking and moving  your mouse to see the input!

![Arduino Due Ports](assets/DueUSBPorts.png)



### Troubleshoot

If the code is not working, there are some common issues we can troubleshoot:

- You are using the incorrect USB port
- You have not installed the correct drivers for the Arduino Due.
- You have not installed the [USBHost library](https://www.arduino.cc/reference/en/libraries/usbhost/).

## Conclusion

The Arduino Due has a number of facilities for communicating with a computer, another Arduino or other microcontrollers, and different devices like phones, tablets, cameras and so on. In this example, we have learned how to use the Arduino Due as a USB host for a mouse. 
