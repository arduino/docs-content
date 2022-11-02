---
title: Guide to Arduino GIGA USB Features
description: Learn how you can turn your USB device into a mouse or keyboard, how to read & write to a USB mass storage, and how to send MIDI signals.
author: Karl Söderby
---


## USB HID

It is possible to turn your GIGA board into Human Interface Device **(HID)**, using the [USBHID](https://github.com/arduino/ArduinoCore-mbed/tree/master/libraries/USBHID) library which is included in the GIGA core.

### Keyboard

***Important! When using the GIGA as a keyboard, make sure to include some sort of delay. Otherwise, you may end up printing things very fast, which can be very annoying. If this happens nontheless, double tap the reset button and upload a blank sketch to reset the board.*** 

To emulate a keyboard, we need to include `PluggableUSBHID.h` and `USBKeyboard.h`, and create an object using the `USBkeyboard` constructor. 

```arduino
#include "PluggableUSBHID.h"
#include "USBKeyboard.h"

USBKeyboard Keyboard;
```

To send a single character, we can use the `putc()` method.

```arduino
Keyboard.putc(97); //prints the letter 'a'
```

See the `DEC` column at [ascii-code.com](https://www.ascii-code.com/) to understand what number you need to print a specific character.

To print a whole string, use the `printf()` method.

```arduino
Keyboard.printf("Hello World!"); 
```

To use modifiers and function keys, use the `key_code()` method.

```
Keyboard.key_code(KEY_F1);
```

To use media keys, use the `media_control()` method.

```
Keyboard.media_control(KEY_NEXT_TRACK);
```

***All modifiers, function and media control keys can be found in [this header file](https://github.com/arduino/ArduinoCore-mbed/blob/master/libraries/USBHID/src/USBKeyboard.h).***

### Mouse

To emulate a mouse, we need to include `PluggableUSBHID.h` and `USBMouse.h`, and create an object using the `USBMouse` constructor. 

```arduino
#include "PluggableUSBHID.h"
#include "USBMouse.h"

USBMouse Mouse;
```

To move the cursor, we can write the **x** and **y** coordinates directly, using the `move()` method.

```arduino
Mouse.move(100,100);
```

For clicking the mouse, use the `click()` method.

```arduino
Mouse.click(MOUSE_LEFT);
Mouse.click(MOUSE_RIGHT);
Mouse.click(MOUSE_MIDDLE);
```

For double clicking the mouse, use the `double_click()` method.

```
Mouse.double_click(MOUSE_LEFT);
```

To press and release the buttons on the mouse, we can use the `press()` and `release()` methods. This way, we can define how long we want the button to be pressed for.

```arduino
Mouse.press(MOUSE_LEFT);
Mouse.press(MOUSE_RIGHT);
Mouse.press(MOUSE_MIDDLE);

delay(1000);

Mouse.release(); 
```



## USB Host



## USB Mass Storage

Through the USB-A connector onboard the Giga, it is possible to connect a USB mass storage device (like an USB stick). This makes it possible to both access and store large amount of data and files for more advanced projects.

This is particularly good for audio & display projects, but also for logging data.

### Reading From File



### Writing To File

##