---
title: 'GIGA Display Shield GFX Guide'
description: 'Learn how to draw shapes, print text and other useful methods with the GFX library.'
author: 'Karl Söderby'
tags: [Displays, GIGA, GFX]
---

The [GIGA Display Shield](/hardware/giga-display-shield) is compatible with the [Adafruit_GFX](https://github.com/adafruit/Adafruit-GFX-Library) graphics core library.

To access it, we can use a layer library called [Arduino_GigaDisplay_GFX](https://github.com/arduino-libraries/Arduino_GigaDisplay_GFX) designed specifically for the shield. In this guide, we will get started with some of the essential methods of the library, that will allow us to e.g. print values, text, draw shapes.

## Goals

In this guide we will cover:
- Learn how to draw and print to the display,
- How to draw basic shapes (circles, rectangles etc)
- How to update values on the screen,

## Hardware & Software Needed

- [GIGA R1 WiFi](/hardware/giga-r1-wifi).
- [GIGA Display Shield](/hardware/giga-display-shield)
- [Arduino IDE](https://www.arduino.cc/en/software)

## Installation

To install the library, open the Arduino IDE and search for the **Arduino_GigaDisplay_GFX** library in the **Library Manager**.

You can also manually download the library in the official GitHub repository. For any issues with the libraries, please report them here as well.
- [Arduino_GigaDisplay_GFX](https://github.com/arduino-libraries/Arduino_GigaDisplay_GFX)

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

### Coordinates

The coordinates in the GFX library are easy to work with. Most methods have the coordinates as parameters (x,y). To set the cursor (position) on the display, you can utilize the following method: 

- `setCursor(x, y)` - set the cursor on the display.

### Color

To change color of text, pixels, background etc, you can first define the color using the RGB565 format:

- `#define YELLOW 0xFFE0`

Then use it anywhere in the code for coloring, such as:
- `fillScreen(YELLOW)` - sets the background color for the display.
- `drawPixel(x, y, YELLOW)` - color a single pixel.
- `setTextColor(YELLOW)` - color the text.
- `fillRect(x, y, width, height, YELLOW)` color a rectangle.

Read more about the color format and generate the colors your want at the following page:
- [RGB Color Picker](https://rgbcolorpicker.com/565) (external link)

### Text

To display text on the screen, use the following methods:

- `setTextSize(size)` - set the size for the text. Any number between `1` (very small) to `80` (one digit covers the screen) works on this display.
- `setTextColor(color,background_color)` - sets color and optionally background color. This is useful when overwriting an existing number (like printing sensor values continuously).
- `print(content)` print something to the screen.

A minimal example for using text methods can be found below:

```arduino
#include "Arduino_GigaDisplay_GFX.h"

GigaDisplay_GFX display; // create the object

#define BLACK 0x0000

void setup() {
  display.begin();
  display.fillScreen(BLACK);
  display.setCursor(10,10); //x,y
  display.setTextSize(5); //adjust text size
  display.print("Hello World!"); //print
}
void loop(){}
```

### Pixels & Shapes

To draw pixels and shapes, use the following methods.

- `drawPixel(x, y, color)` - draws a pixel at the coordinates specified.
- `drawRect(x, y, height, width, color)` - draws a rectangle at the coordinates with the height and width & color specified.
- `drawRoundRect(x, y, height, width, border-radius, color)` - rounded rectangle with the border-radius specified.
- `drawTriangle(x0, y0, x1, y1, x2, y2, color)` - draws a triangle at the coordinates specified. 
- `drawCircle(x, y, radius, color)` - draws a circle with specified radius.

The above methods will draw the desired shape's outline, but it will not fill it. To do so, simply use `fillRect()`, `fillTriangle()` etc.

A minimal example for drawing geometrical shapes can be seen below:

```arduino
#include "Arduino_GigaDisplay_GFX.h"

GigaDisplay_GFX display;

#define WHITE 0xffff
#define BLACK 0x0000

void setup() {
  display.begin();
  display.fillScreen(WHITE);
  display.drawTriangle(100, 200, 300, 400, 300, 600, BLACK);
  display.drawCircle(100, 100, 50, BLACK);
  display.drawRect(10, 650, 300, 80, BLACK);
  display.drawRoundRect(300, 50, 100, 100, 30, BLACK);
}
void loop() {}
```

## GFX & Touch Example

The GFX library can be used together with the [Arduino_GigaDisplay_Touch](https://github.com/arduino-libraries/Arduino_GigaDisplayTouch) library. The below example demonstrates how to read a touch point and trigger a function, using a simple if statement.

The example below is very minimal, and it simply switches on and off a boolean whenever the screen is touched. But it is a good example to get started with if you plan to build your own UI with a touch interface.

```arduino
#include "Arduino_GigaDisplay_GFX.h"
#include "Arduino_GigaDisplayTouch.h"

Arduino_GigaDisplayTouch touchDetector;
GigaDisplay_GFX display;

#define WHITE 0xffff
#define BLACK 0x0000

#define screen_size_x 480
#define screen_size_y 800

int touch_x;
int touch_y;

//increase or decrease the sensitivity of the touch.
int trigger_sensitivity = 5;
bool switch_1;
int counter;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  display.begin();

  if (touchDetector.begin()) {
    Serial.print("Touch controller init - OK");
  } else {
    Serial.print("Touch controller init - FAILED");
    while (1)
      ;
  }
}

void loop() {
  uint8_t contacts;
  GDTpoint_t points[5];
  contacts = touchDetector.getTouchPoints(points);
  
  if (contacts > 0) {
    Serial.print("Contacts: ");
    Serial.println(contacts);

    counter++;

    //record the x,y coordinates 
    for (uint8_t i = 0; i < contacts; i++) {
      touch_x = points[i].x;
      touch_y = points[i].y;
    }

    //as the display is 480x800, any time you touch the screen it will trigger
    //the trigger sensitivity is set to "5". 
    if (touch_x < screen_size_x && touch_y < screen_size_y && counter > trigger_sensitivity) {
      switch_1 = !switch_1;
      Serial.println("switched");
      changeSwitch();
      delay(250);
    }
  }
}

void changeSwitch() {
  if (switch_1) {
    display.fillScreen(BLACK);
    display.setTextColor(WHITE);
  } else {
    display.fillScreen(WHITE);
    display.setTextColor(BLACK);
  }
  display.setCursor(50, screen_size_y/2);
  display.setTextSize(5);
  display.print("Switched");
  counter = 0;
}
```

***Learn more about the Giga Display's touch interface in the [Touch Interface Guide](/tutorials/giga-display-shield/basic-touch).***

## Summary

In this guide we have covered some basic methods of the GFX library, such as writing text, drawing rectangles and changing colors & text sizes. The GFX library is easy to get started with for beginners, but can also be used to build sophisticated and powerful UIs with advanced usage.

For more tutorials, visit the [documentation page for GIGA Display Shield](/hardware/giga-display-shield).