---
title: GIGA Display Shield Draw Images Guide
description: 'Learn how to use basic draw functions to create and display images on the GIGA Display Shield.'
author: Benjamin Dannegård
hardware:
  - hardware/10.mega/boards/giga-r1-wifi
  - hardware/10.mega/shields/giga-display-shield
tags: [Display, Draw, Images]
---

The most basic use of the GIGA Display Shield is to draw an image on the screen using code. This is made easy by using the library `ArduinoGraphics`. In this tutorial we will go through how to draw the Arduino logo on the GIGA Display Shield with the commands provided by this library.

This is a great tutorial for getting started with your shield and exploring what possibilities the library gives us.

## Hardware & Software Needed

- [Arduino GIGA R1 WiFi](/hardware/giga-r1-wifi)
- [Arduino GIGA Display Shield](/hardware/giga-display-shield)
- [Arduino IDE](https://www.arduino.cc/en/software)
- [ArduinoGraphics library](https://www.arduino.cc/reference/en/libraries/arduinographics/)

## Downloading the Library and Core

Make sure the latest GIGA Core is installed in the Arduino IDE. **Tools > Board > Board Manager...**. Here you need to look for the **Arduino Mbed OS Giga Boards** and install it, the [Arduino_H7_Video library](https://github.com/arduino/ArduinoCore-mbed/tree/main/libraries/Arduino_H7_Video) is included in the core and is needed for the examples to work. Now you have to install the library needed for the graphical display features. To do this, go to **Tools > Manage libraries..**, search for **ArduinoGraphics**, and install it.

For more information about libraries and how to install them with the IDE, visit our [libraries tutorial](/software/ide-v2/tutorials/ide-v2-installing-a-library).

## Using Draw Feature in a Sketch

First, we need to include the library that we will be using and define the display screen:

```arduino
#include "Arduino_H7_Video.h"
#include "ArduinoGraphics.h"

Arduino_H7_Video Display(800, 480, GigaDisplayShield);
```

As we only want to draw something on the screen once, we can put all the drawing code in the `void setup()`. If we instead put this code in the `void loop()` function it will keep drawing the given image over and over.

Let's first draw the background of the image. Start by initializing the display class from the library with `Display.begin()`. Then to start drawing things on the screen we need to use `Display.beginDraw()`. Now the background color can be set with `Display.background(255, 255, 255)`, where RGB values are entered within the parentheses. `Display.clear()` will clear anything that has been drawn on the screen, but it will leave the background as it was set before.


```arduino
void setup() {
  Display.begin();
  
  Display.beginDraw();
  Display.background(255, 255, 255);
  Display.clear();
```

Next, let's draw the circle that will be the base of the logo. First, set the color of the circle with `Display.fill(0x008184);`. Then draw the circle with the command `Display.circle()`. Inside the parentheses enter the x position, y position, and diameter of the circle. We can make the positioning easy by using the display's total width and height as a base for our position measurements.

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

The complete code can be found as an example in the **Arduino_H7_video** library, it is called **ArduinoLogoDrawing**. The full sketch is also below. Now upload the entire sketch and you should see the Arduino logo being drawn on the display. 

### Full Sketch

```arduino
#include "Arduino_H7_Video.h"
#include "ArduinoGraphics.h"

Arduino_H7_Video Display(800, 480, GigaDisplayShield);
//Arduino_H7_Video Display(1024, 768, USBCVideo);

void setup() {
  Display.begin();
  
  Display.beginDraw();
  Display.background(255, 255, 255);
  Display.clear();
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
  Display.endDraw();
}

void loop() { }

```

### Testing It Out

Now that it is all uploaded your GIGA Display Shield should look like the image below:

![Sketch running on the GIGA Display Shield](assets/draw-on-shield.jpg)

## Displaying Images

Now let's have a look at how we can use the **ArduinoGraphics** library to display images on the GIGA Display Shield.

### Converting an Image

Using an online image converter you can pick any image you would like to be displayed on the display shield. However keep in mind the display is 480x800 in size. The format of the converted image needs to be Binary RGB565. Using an online image converter like the [LVGL image converter tool](https://lvgl.io/tools/imageconverter) will let you pick this as an option. Simply pick the "Binary RGB565" option under "Output format", your desired color format and hit "Convert". You will now have an image that is ready for use in an Arduino sketch.

### Displaying the Image on the Display

We will be using the example sketch "ArduinoLogo" as the basis for the sketch that let us display an image. The example sketch can be found under **File > Examples > Arduino_H7_Video > ArduinoLogo**.

Running the example sketch as is will display the Arduino logo on the screen, like in the image below:

[Arduino Logo on the GIGA Display Shield](assets/logo-img.svg)

Now to use the image that we converted in the last step. Use the macro inside the example sketch. This makes use of the `incbin.h` translation library. The necessary files are located in the folder for the example sketch.

At the start of the sketch you can see these lines commented out:
```arduino
/*
#define INCBIN_PREFIX
#include "incbin.h"
INCBIN(test, "/home/user/Downloads/test.bin");
*/
```

Uncomment these lines, and change the path to the image to the correct one. For Mac and Linux users the syntax of the path is correct as `"/home/user/Downloads/test.bin"`. For Windows users the path needs to be an absolute path, like this: `"C:\USERNAME\Downloads\test.bin"`. Now we need to change the `Image` variable to use our image.

By default the image we import will be called `test`. The line `Image img_arduinologo(ENCODING_RGB16, (uint8_t *) texture_raw, 300, 300);` needs to have one argument changed, `texture_raw` should now be `testData`. So the line should be `Image img_arduinologo(ENCODING_RGB16, (uint8_t *) testData, 300, 300);`.


### Full Sketch

```arduino
/*
  ArduinoLogo

  created 17 Apr 2023
  by Leonardo Cavagnis
*/

#include "Arduino_H7_Video.h"
#include "ArduinoGraphics.h"

#include "img_arduinologo.h"
// Alternatively, any raw RGB565 image can be included on demand using this macro
// Online image converter: https://lvgl.io/tools/imageconverter (Output format: Binary RGB565)
/*
#define INCBIN_PREFIX
#include "incbin.h"
INCBIN(test, "/home/user/Downloads/test.bin");
*/

Arduino_H7_Video Display(800, 480, GigaDisplayShield);
//Arduino_H7_Video Display(1024, 768, USBCVideo);

Image img_arduinologo(ENCODING_RGB16, (uint8_t *) texture_raw, 300, 300);

void setup() {
  Display.begin();

  Display.beginDraw();
  Display.image(img_arduinologo, (Display.width() - img_arduinologo.width())/2, (Display.height() - img_arduinologo.height())/2);
  Display.endDraw();
}

void loop() { }
```

## Conclusion

In this tutorial, we used basic drawing functions with the GIGA Display Shield. Using the `ArduinoGraphics` library we managed to draw the Arduino logo with just a few simple commands. Using these basic functions it is possible to create most images that you can think of. Now you can let your imagination run wild and draw to your heart's content!