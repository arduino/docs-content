---
title: GIGA Display Shield 3D Engine Tutorial 
description: 'Get started using a 3D engine with the GIGA Display Shield'
author: Benjamin Dannegård
tags: [Display, 3D, TinyGL]
---

## Introduction

Using a 3D engine to construct and render objects can be a hardware heavy process. Now with the GIGA R1 WiFi, GIGA Display Shield and the [Arduino_TinyGL](https://github.com/arduino-libraries/Arduino_GigaDisplay_TinyGL) library this can be an easy process! The powerful GIGA R1 WiFi board can run the 3D engine while rendering it on the display shield, utilizing the touch interface of the display to move and interact with the rendered objects. 

In this tutorial, we will show you how to make use of these features!

<video width="100%" loop autoplay>
<source src="assets/3d-engine-example.mp4" type="video/mp4" />
</video>

***Please note that the development status of the [Arduino_TinyGL](https://github.com/arduino-libraries/Arduino_GigaDisplay_TinyGL) library is in an experimental phase.***

## Hardware & Software Needed

- [Arduino GIGA R1 WiFi](https://store.arduino.cc/products/giga-r1-wifi)
- [Arduino GIGA Display Shield](https://store.arduino.cc/products/giga-display-shield)
- [Arduino IDE](https://www.arduino.cc/en/software)

## Downloading the Library and Board Package

The Arduino Mbed OS Giga Boards Board Package contains most of the libraries you need to work with the shield's camera connector. To install the Board Package for GIGA boards, navigate to **Tools > Board > Boards Manager** or click the Boards Manager icon in the left tab of the IDE. In the Boards Manager tab, search for giga and install the latest Arduino Mbed OS Giga Boards version, the [Arduino_H7_Video library](https://github.com/arduino/ArduinoCore-mbed/tree/main/libraries/Arduino_H7_Video) library is included in the Board Package. 

To install the required libraries for this tutorail, search for **Arduino_TinyGL**, **LVGL** and **Arduino_GigaDisplayTouch**. Install these libraries as they are needed for the Arduino_TinyGL example to work.

## Arduino_TinyGL Library

The Arduino_TinyGL library will enable us to run an engine that can render 3D objects on the GIGA Display Shield. Arduino_TinyGL is based on OpenGL, meaning the objects that we want to be rendered are defined in a `.c` file. Let's take a closer look at these files!

- The source code for this library is available [here](https://github.com/arduino-libraries/Arduino_GigaDisplay_TinyGL)

## Rotating Gears Example
This example will render a set of rotating gears on your GIGA Display Shield's display, which you can move around and inspect using your fingers.
Open the example by going to **Files > Examples > Arduino_TinyGL > Gears** in the Arduino IDE, this will open both the required files in the IDE. You should see a `Gears.ino` and a `gears.c` file as tabs in the IDE. Let's first have a look at the `gears.c` file!

### Gears.c

The `gears.c` file will contain info about the objects you wish to render. This information can be quite technical and requires an understanding of 3D matrixes and viewport renderings. But in this example it has been made a bit easier by putting this information in functions that are easy to modify and use.

In this example gears will be rendered. If you wish to experiment with drawing different gears and seeing how the variables can change the final rendering. You can use the following function, that can be found at the top of the `gears.c` file:

```arduino
static void gear( GLfloat inner_radius, GLfloat outer_radius, GLfloat width, GLint teeth, GLfloat tooth_depth )
```

If you use the function, these will be parameters that are needed:

- **inner_radius**: Radius of hole in the center of the gear
- **outer_radius**: Radius at the center of the gears teeth
- **width**: Width of gear
- **teeth**: Number of teeth
- **tooth_depth**: Depth of tooth

Taking a look into this function you can see what is required for drawing and rendering an object with this library.

Inside the `Gears.ino` file is where we will call this and other functions from the `gears.c` file. So let's take a look at that file now!

### Gears.ino

The screen and view elements are handled by the LVGL framework. For more information on how this works and can be used, please head over to our [LVGL guide](/tutorials/giga-display-shield/lvgl-guide).

Now for the 3D-engine specific functions. If you take a look at the `setup()` function, this function is called inside:

```arduino
init_gears();
```

This is a function that you can find in the `gears.c` file. This function will build the three gears that you will see on the screen when you upload the sketch. If you wish to make simple changes at first, this function is good to take a further look into.

In the `static void anim(lv_timer_t * timer) {}` function you can see how the animation of the rendering is handled. It will need a function to handle the new drawings of the objects as the animation keeps running. The main function that handles this is:

```arduino
draw_gears();
```

This function can also be found inside `gears.c`. This function will handle animations and assign them to each of the gears. So for easy manipulation of the individual animations of the gears in the example have a look at this function.

In the sketch we will also need to define what will happen when the touch interface is triggered. The function used for this is:

```arduino
handleTouch(uint8_t contacts, GDTpoint_t *points)
```

For more information about how to use the touch functions on the display shield, please head over to our [touch tutorial](/tutorials/giga-display-shield/basic-touch).

## Running the Sketch

Since the sketch requires the `gears.c` file to compile correctly we recommend opening the example directly in the Arduino IDE from the **Arduino_TinyGL** library. After downloading the library the example can be found in **Files > Examples > Arduino_TinyGL > Gears**.

After uploading the sketch you should see the same result as shown in the gif below:

<video width="100%" loop autoplay>
<source src="assets/3d-engine-example.mp4" type="video/mp4" />
</video>