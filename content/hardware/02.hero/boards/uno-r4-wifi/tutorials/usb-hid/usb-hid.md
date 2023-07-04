---
title: 'Arduino UNO R4 WiFi USB HID'
description: 'Learn how to use the UNO R4 WiFi as a mouse/keyboard.'
tags:
  - USB
  - HID
  - Keyboard
  - Mouse
author: 'Karl Söderby'
---

In this tutorial you will learn how to emulate a mouse/keyboard using an **Arduino UNO R4 WiFi** board with the [Keyboard](https://www.arduino.cc/reference/en/language/functions/usb/keyboard/) and [Mouse](https://www.arduino.cc/reference/en/language/functions/usb/mouse/) APIs.

This feature can be used to create game controllers, keyboard extensions or other HID devices.

## Goals

The goals of this tutorials are:

- Learn how to emulate a keyboard (keypresses),
- learn how to emulate a mouse (x,y coordinates).

## Hardware & Software Needed

- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software))
- [Arduino UNO R4 WiFi](https://store.arduino.cc/uno-r4-wifi)
- [Arduino Renesas Core](https://github.com/arduino/ArduinoCore-renesas)

## Human Interface Device (HID) 

Human interface devices (HID) are devices designed for humans (keyboards, mice, game controllers etc.), that frequently sends data over USB to a computer. When you press a key on a keyboard, you send data to a computer, which reads it and in turn activates the corresponding key.

The UNO R4 WiFi has built-in support for HID, a feature found on most modern day development boards, but not on previous UNO revisions. 

To turn your board into an HID, you can use the **keyboard/mouse** API that is built in to the core. You can visit the documentation for this API in the language reference at:
- [Keyboard](https://www.arduino.cc/reference/en/language/functions/usb/keyboard/)
- [Mouse](https://www.arduino.cc/reference/en/language/functions/usb/mouse/)

In the section below, you will a couple of useful examples to get you started!

## Keyboard

To use keyboard functionalities, we need to include the library at the top of our sketch. The Keyboard class contains several methods that are useful to emulate a keyboard.

```arduino
#include <Keyboard.h>

Keyboard.method()
```

### Keyboard Example

To emulate a keyboard, we can use the `press()` and `releaseAll()` methods. This will emulate a keypress, as well as releasing the keypress. The following example prints a **"w"** every second.

```arduino
#include <Keyboard.h>

void setup() {
  Keyboard.begin();
  delay(1000);
}

void loop() {
  Keyboard.press('w');
  delay(100);
  Keyboard.releaseAll();
  delay(1000); 
}
```

To see more examples, please refer to links below:

- [Keyboard and Mouse Control Tutorial](/built-in-examples/usb/KeyboardAndMouseControl)
- [Keyboard Reprogram Tutorial](/built-in-examples/usb/KeyboardReprogram)
- [Keyboard Serial Tutorial](/built-in-examples/usb/KeyboardSerial)
- [Keyboard Logout Tutorial](/built-in-examples/usb/KeyboardLogout)
- [Keyboard Message Tutorial](/built-in-examples/usb/KeyboardMessage)

## Mouse 

To use mouse functionalities, we need to include the library at the top of our sketch. The Mouse class contains several methods that are useful to emulate a mouse.

```arduino
#include <Mouse.h>

Mouse.method();
```

### Mouse Example

The following example moves both axis of mouse just slightly (10 points), back and forth.

```arduino
#include <Mouse.h>

void setup() {
  Mouse.begin();
  delay(1000);
}

void loop() {
  Mouse.move(10,10);
  delay(1000);
  Mouse.move(-10,-10);
  delay(1000); 
}
```

To see more examples, please refer to links below:

- [Keyboard and Mouse Control Tutorial](/built-in-examples/usb/KeyboardAndMouseControl)
- [Button Mouse Control Tutorial](/built-in-examples/usb/ButtonMouseControl)
- [Joystick Mouse Control Tutorial](/built-in-examples/usb/JoystickMouseControl)

## Summary

In this tutorial, we have demonstrated some basic HID usage with the UNO R4 WiFi. To view the full API, please refer to the following APIs:
- [Keyboard](https://www.arduino.cc/reference/en/language/functions/usb/keyboard/)
- [Mouse](https://www.arduino.cc/reference/en/language/functions/usb/mouse/)

In there, you will find a detailed reference along with some good examples to get you started with HID features.