---
title: 'Draw Arduino Logo with MKR Vidor 4000'
description: 'Draw the Arduino Logo on an HDMI monitor, using the MKR Vidor 4000 board.'
tags: [HDMI]
difficulty: 'advanced'
author: Arduino
---

This example uses the drawing functions of the VidorGFX library to recreate on screen our beloved logo, in a stylized form. The functions available for the graphics generation are the same of the [Adafruit_GFX library](https://learn.adafruit.com/adafruit-gfx-graphics-library?view=all).

## Hardware Required

- [Arduino MKR Vidor 4000](https://store.arduino.cc/arduino-vidor-4000)
- microHDMI to HDMI cable or adaptor

- Monitor with HDMI input

## Circuit

There is no circuit for this example.

![The circuit for this tutorial.](assets/vidor-circuit.png)

## Code

Include the Vidor_GFX library, which is part of VidorGraphics.

- `#include "VidorGraphics.h"`
- `#include "Vidor_GFX.h"`

To manage graphics on screen you need to create an object with `Vidor_GFX vdgfx;` then all the functions will refer to that object. In our example we draw circles, rectangles and lines, with some added text. The screen resolution used for this example is 640 x 480 pixels and all the primitives are used with this coordinate system as reference.

The complete sketch is below and you find it in the examples from Libraries, under VidorGraphics :

```arduino

#include "VidorGraphics.h"
#include "Vidor_GFX.h"

Vidor_GFX  vdgfx;

void setup() {

  Serial.begin(9600);

  // wait for the serial monitor to open,

  // if you are powering the board from a USB charger remove the next line

  while (!Serial);

  // Initialize the FPGA

  if (!FPGA.begin()) {

    Serial.println("Initialization failed!");

    while (1) {}

  }

  delay(4000);
}

void loop()
{

  /**

  *  Draw an Arduino logo

  */

  // Fill the screen with a white background

  vdgfx.fillRect(0,0,640,480,vdgfx.White());

  /**

  *  The library allows drawing some basic elements to the view, like circles, rectangles, lines

  */

  vdgfx.fillCircle(225,225,100 ,vdgfx.lightBlue());

  vdgfx.fillCircle(415,225,100 ,vdgfx.lightBlue());

  vdgfx.fillCircle(225,225,90 ,vdgfx.White());

  vdgfx.fillCircle(415,225,90 ,vdgfx.White());

  vdgfx.fillRect(175,220,100,10 ,vdgfx.lightBlue());

  vdgfx.fillRect(365,220,100,10 ,vdgfx.lightBlue());

  vdgfx.fillRect(410,175,10,100 ,vdgfx.lightBlue());

  /**

  *  To draw a text we can use the classic functions like write() and print()

  *  Text size, color and position can be changed using the .text subclass

  */

  vdgfx.text.setCursor(150,375);

  vdgfx.text.setAlpha(255);

  vdgfx.text.setSize(3);

  vdgfx.text.setColor(vdgfx.lightBlue());

  vdgfx.println("ARDUINO");

  vdgfx.text.setCursor(480,145);

  vdgfx.text.setSize(1);

  vdgfx.println("TM");

  while (1) {

  }
}
```


**Last revision 2018/07/22 by SM**
