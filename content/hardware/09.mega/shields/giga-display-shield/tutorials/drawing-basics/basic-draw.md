---
title: Using Basic Draw Functions with the Giga Display Shield
description: 'Learn how to use basic draw functions to create images on the GIGA display shield'
author: Benjamin Dannegård
tags: [Display, Draw]
---



## Hardware & Software Needed

- [GIGA R1 WiFi](/hardware/giga-r1).
- [GIGA Display Shield]()
- [Arduino IDE](https://www.arduino.cc/en/software)
- [ArduinoGraphics library]()
- [Library]() library.

## Downloading the Library and Core

Make sure the latest GIGA Core is installed in the Arduino IDE. **Tools > Board > Board Manager...**. Here you need to look for the **Arduino Mbed OS Giga Boards** and install it. Now you have to install the library needed for the IMU. Go to **Tools > Manage libraries..**, search for ** ** and install it.

## Using Draw Feature in a Sketch

First we need to include the library that we will be using and define the display screen that we are using:

```arduino
#include "Arduino_H7_Video.h"

Arduino_H7_Video Display(800, 480, GigaDisplayShield);
```

As we only want to draw something on the screen once, we can put all the drawing code in the `void setup()`. If we instead put this code in the `void loop()` function it will keep drawing the given image over and over.

Lets start by initializing the display class from the library with `Display.begin()`. Then to start drawing things on the screen we need to use `Display.beginDraw()`. Now the background color can be set with `Display.background(255, 255, 255)`, where RGB values are entered within the parentheses. `Display.clear()` will clear anything that has been drawn on the screen, but it will leave the background as it was set before.


```arduino
void setup() {
  Display.begin();
  
  Display.beginDraw();
  Display.background(255, 255, 255);
  Display.clear();
```



```arduino
  Display.fill(0x008184);
  Display.circle(Display.width()/2, Display.height()/2, 300);
  Display.stroke(255, 255, 255);
  Display.noFill();
  for (int i=0; i<30; i++) {
    Display.circle((Display.width()/2)-55+5, Display.height()/2, 110-i);
    Display.circle((Display.width()/2)+55-5, Display.height()/2, 110-i);
  }
  Display.fill(255, 255, 255);
  Display.rect((Display.width()/2)-55-16+5, (Display.height()/2)-5, 32, 10);
  Display.fill(255, 255, 255);
  Display.rect((Display.width()/2)+55-16-5, (Display.height()/2)-5, 32, 10);
  Display.fill(255, 255, 255);
  Display.rect((Display.width()/2)+55-5-5, (Display.height()/2)-16, 10, 32);
```

Now that the drawing is done the `Display.endDraw()` function can be called.

```arduino
  Display.endDraw();
}
```

The complete code can be found as an example in the **Arduino_H7_video** library, it is called **ArduinoLogoDrawing**. Now upload the entire sketch and you should see the Arduino logo being drawn on the display. 

## Testing it out



## Conclusion

This tutorial went through how to use the basic drawing functions with the Giga Display Shield. Using these basic functions it is possible to create most images that you can think of. Now you can let your imagination run wild and draw to your hearts content!