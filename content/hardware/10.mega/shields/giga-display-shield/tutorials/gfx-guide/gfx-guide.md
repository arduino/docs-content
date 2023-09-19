---
title: 'Getting Started with the GIGA Display Shield'
description: 'Learn how to set up and use the GIGA Display Shield and get an overview of the features.'
author: 'Karl Söderby'
tags: [Displays, LVGL, GIGA, IMU]
---

The [GIGA Display Shield](/hardware/giga-display-shield) is compatible with the [Adafruit_GFX](https://github.com/adafruit/Adafruit-GFX-Library) graphics core library.

To access it, we have a library called [Arduino_GigaDisplay_GFX](https://github.com/arduino-libraries/Arduino_GigaDisplay_GFX) designed specifically for the shield. In this guide, we will get started with some of the essential methods of the library, that will allow us to e.g. print values, text, draw shapes.

## Goals

In this guide we will cover:
- Learn how to draw and print to the display,
- how to draw basic shapes (circles, rectangles etc)
- how to update values on the screen,

## Hardware & Software Needed

- [GIGA R1 WiFi](/hardware/giga-r1).
- [GIGA Display Shield](/hardware/giga-display-shield)
- [Arduino IDE](https://www.arduino.cc/en/software)

## Installation

To install the library, open the Arduino IDE and search for the **Arduino_GigaDisplay_GFX** library in the **Library Manager**.

![Install the library.]()

## Basic Example

The [Arduino_GigaDisplay_GFX](https://github.com/arduino-libraries/Arduino_GigaDisplay_GFX) is a layer library for the [Adafruit_GFX](https://github.com/adafruit/Adafruit-GFX-Library) library that's been around for some years now. The full documentation for this library can be found [here](https://learn.adafruit.com/adafruit-gfx-graphics-library).

The library provides graphic functions for drawing individual pixels, rectangles, circles, lines and other geometrical shapes. It also provides support for printing numeric values & strings directly on the display.

To use the library, we simply need to create a display object, initialize the library, change something and print it on the display. See this minimal example below:

```arduino
#include "Arduino_GigaDisplay_GFX.h"

GigaDisplay_GFX display; // create the object

void setup() {
  display.begin(); //init library
  
  display.setCursor(10,10); //x,y
  display.setTextSize(5); //adjust text size
  display.print("Hello World!"); //print
}
void loop(){}
```

The above example will simply print `Hello World!` at the `x` and `y` coordinates (10,10). Simple as that.

## Methods Overview

There are several methods available. In this section, we will list out a number of useful ones. To see the full list, check out Adafruit's documentation of this library in [this page](https://learn.adafruit.com/adafruit-gfx-graphics-library).

### Essentials

The most basic commands that you will need to know is how to change the coordinates, background color and updating screen:
- `fillScreen(color)` - sets the background color for the display.
- `setCursor(x, y)` - set the cursor on the display.
- `print(content)` - prints the content on the display.

### Color

To change color of text, pixels, background etc, you can first define the color using the RGB565 format:

- `#define YELLOW 0xFFE0`

Then use it anywhere in the code for coloring, such as:
- `drawPixel(x, y, YELLOW)` - color a single pixel.
- `setTextColor(YELLOW)` - color the text.
- `fillRect(x, y, width, height, YELLOW)` color a rectangle.

Read more about the color format and generate the colors your want at the following page:
- [RGB Color Picker](https://rgbcolorpicker.com/565) (external link)

### Pixels & Shapes

To draw pixels and shapes, use the following methods. This will draw the outl

- `drawPixel(x, y, color)` - draws a pixel at the coordinates specified.
- `drawRect(x, y, height, width, color)` - draws a rectangle at the coordinates with the height and width & color specified.
- `drawRoundRect(x, y, height, width, border-radius, color)` - rounded rectangle with the border-radius specified.
- `drawTriangle(x0, y0, x1, y1, x2, y2, color)` - draws a triangle at the coordinates specified. 
- `drawCircle(x, y, radius)` - draws a circle with specified radius.


### Text

- `setTextSize(size)` - set the size for the text. Any number between 1-80~ works on this display.
- `setTextColor(color,background_color)` - sets color and optionally background color. This is useful when overwriting an existing number (like printing sensor values continuously).



## Summary

In this guide we have covered the requirements & installation needs for using the GIGA Display Shield, as well as demonstrating how to access the RGB, IMU & Microphone peripherals. 

For more tutorials, visit the [documentation page for GIGA Display Shield](/hardware/giga-display-shield).