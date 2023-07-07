---
title: Using Basic Draw Functions with the Giga Display Shield
description: 'Learn how to use basic draw functions to create images on the GIGA display shield'
author: Benjamin Dannegård
tags: [Display, Draw]
---

The most basic use of the Giga display shield is to draw an image on the screen using code. This is made easy by using the library `ArduinoGraphics`. In this tutorial we will go through how to draw the Arduino logo on the Giga display shield with the commands provided by this library. This is a great tutorial for getting started with your shield and exploring what possibilities the library gives us.

## Hardware & Software Needed

- [GIGA R1 WiFi](/hardware/giga-r1).
- [GIGA Display Shield]()
- [Arduino IDE](https://www.arduino.cc/en/software)
- [ArduinoGraphics library]()
- [Library]() library.

## Downloading the Library and Core

Make sure the latest GIGA Core is installed in the Arduino IDE. **Tools > Board > Board Manager...**. Here you need to look for the **Arduino Mbed OS Giga Boards** and install it. Now you have to install the library needed for the graphical display features. To do this, go to **Tools > Manage libraries..**, search for **ArduinoGraphics**, and install it.

## Using Draw Feature in a Sketch

First, we need to include the library that we will be using and define the display screen:

```arduino
#include "Arduino_H7_Video.h"
#include "ArduinoGraphics.h"

Arduino_H7_Video Display(800, 480, GigaDisplayShield);
```

As we only want to draw something on the screen once, we can put all the drawing code in the `void setup()`. If we instead put this code in the `void loop()` function it will keep drawing the given image over and over.

Lets first draw the background of the image. Start by initializing the display class from the library with `Display.begin()`. Then to start drawing things on the screen we need to use `Display.beginDraw()`. Now the background color can be set with `Display.background(255, 255, 255)`, where RGB values are entered within the parentheses. `Display.clear()` will clear anything that has been drawn on the screen, but it will leave the background as it was set before.


```arduino
void setup() {
  Display.begin();
  
  Display.beginDraw();
  Display.background(255, 255, 255);
  Display.clear();
```

Next let's draw the circle that will be the base of the logo. First, set the color of the circle with `Display.fill(0x008184);`. Then draw the circle with the command `Display.circle()`. Inside the parentheses enter the x position, y position, and diameter of the circle. We can make the positioning easy by using the display's total width and height as a base for our position measurements.

```arduino
  Display.fill(0x008184);
  Display.circle(Display.width()/2, Display.height()/2, 300);
```

Next, we want to draw the two circles that are in the bigger circle of the Arduino logo. First, we will set the color of the circles we are drawing. To change the color of the lines we are drawing use `Display.stroke()`, where the color of the stroke will be the RGB value entered into the parentheses, in this case they will be white. Then we use `Display.noFill()` to indicate that we don't want to fill the circles we are drawing. Lastly, to get the thickness of the circles we can use a simple `for` loop that will draw circles in a slightly changed position 30 times, to give the appearance of the thick circles in the logo. 

```arduino
  Display.stroke(255, 255, 255);
  Display.noFill();
  for (int i=0; i<30; i++) {
    Display.circle((Display.width()/2)-55+5, Display.height()/2, 110-i);
    Display.circle((Display.width()/2)+55-5, Display.height()/2, 110-i);
  }
```

Lastly, let's draw the plus and minus symbols inside the two circles of the logo. The easiest way to draw these is to use the `Display.rect()` function, which will draw a rectangle with the parameters given. Let's first give the color with `Display.fill` as we have done before. When using `Display.rect()` we can make it easier and use the display's dimensions as the base of the sizes. After entering the width and height of the rectangle we can enter:

```arduino
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

## Testing It Out

Now that it is all uploaded your display shield should look like the image below:

![Sketch running on the Giga Display Shield](assets/draw-on-shield.jpg)


## Conclusion

In this tutorial we used basic drawing functions with the Giga display shield. Using the `ArduinoGraphics` library we managed to draw the Arduino logo with just a few simple commands. Using these basic functions it is possible to create most images that you can think of. Now you can let your imagination run wild and draw to your hearts content!