---
title: 'GIGA Display Shield Touch Interface'
description: 'Learn how to use the touch interface on the GIGA Display Shield.'
author: Karl Söderby
tags: [Display, Touch Screen]
---

The [GIGA Display Shield](/hardware/giga-display-shield) has an advanced touch interface, supported via the [Arduino_GigaDisplayTouch](https://github.com/arduino-libraries/Arduino_GigaDisplayTouch) library.

This library is used to return the number of contact points, and the `x,y` coordinates for each of these. For example, touching the screen with two fingers somewhere on the screen would generate the following:

- `x` - 0-480 (x-axis)
- `y` - 0-800 (y-axis)
- `contacts` - number of touchpoints (fingers on the screen).

***Please note that any example with the GIGA Display Shield requires a GIGA R1 WiFi board. To get started with the shield, visit the [Getting Started with GIGA Display Shield](/tutorials/giga-display-shield/getting-started).***

## Hardware & Software Needed

- [GIGA R1 WiFi](/hardware/giga-r1).
- [GIGA Display Shield](/hardware/giga-display-shield)
- [Arduino IDE](https://www.arduino.cc/en/software)

## Install Arduino_GigaDisplayTouch

The [Arduino_GigaDisplayTouch](https://www.arduino.cc/reference/en/libraries/arduino_gigadisplaytouch/) is used to read touchpoints across the screen, and returns the number of **contacts** and **coordinates**. 

![Install Arduino_GigaDisplayTouch](assets/install-touchlib.png)

***For source code and issues with the Arduino_GigaDisplayTouch library, please see the [GitHub repository](https://github.com/arduino-libraries/Arduino_GigaDisplayTouch).***

## LVGL

This library works with the [lvgl](https://github.com/lvgl/lvgl) framework, which provides a rich set of interactive widgets like buttons, dropdowns, radio buttons etc. This requires a touch interface, and the **Arduino_GigaDisplayTouch** provides just that.

***Learn more about how to use the lvgl framework with the GIGA Display Shield in [this tutorial](/tutorials/giga-display-shield/lvgl-guide).***

## Coordinates Example

To retrieve the coordinates when touching the display, we can use the **Touch_Polling** example from the library. You will find it at **Arduino_GigaDisplayTouch > Touch_Polling** in the IDE (library needs to be installed), or you will find it just below:

<CodeBlock url="https://github.com/arduino-libraries/Arduino_GigaDisplayTouch/tree/main/examples/Touch_Polling" className="arduino"/>

Upload the example to your GIGA R1 WiFi board, and open the **Serial Monitor** tool. If there any initialization issues, it will be printed here. Otherwise, you should see:

```
Touch controller init - OK
```

Seeing this, you can start touching the display area with one or more fingers. The serial monitor will print out how many "contacts" aka fingers you are using, and the coordinates for each point. Here's an example response:

```
Contacts: 2 <---- two fingers used
245 346 <---- x = 245, y = 346
178 473 <---- x = 178, y = 473
```

In this case, we have two touchpoints, and the coordinates for each of them printed below (`x`,`y`). And that's pretty much it to obtain a successful reading from the touch interface. 

You can use this to build customised gestures on the screen such as swiping two fingers left to trigger an animation, or three fingers up to change the background color.

## Summary

In this tutorial, we have explored the **Arduino_GigaDisplayTouch** library and tested out an example that allows us to read the coordinates of our touches. This library is essential for developing sophisticated touch displays using the lvgl framework.