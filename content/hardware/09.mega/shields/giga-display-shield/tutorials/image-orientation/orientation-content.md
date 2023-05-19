---
title: Using IMU to determine orientation of the Giga Display Shield
description: 'Learn how to use the shields IMU to determine the orientation of the Giga Display Shield'
author: Benjamin Dannegård
tags: [Display, IMU, orientation]
---

Any modern device uses sensors to determine the correct orientation that an image should be displayed with. Using the Arduino GIGA R1 WiFi with the GIGA Display Shield we can read values given by the on board IMU to determine what orientation an image should be given. This tutorial will show you how to manipulate an image on the GIGA Display Shield using readings from the IMU sensor. 

## Hardware & Software Needed

- [GIGA R1 WiFi](/hardware/giga-r1).
- [GIGA Display Shield]()
- [Arduino IDE](https://www.arduino.cc/en/software)
- [Arduino_BMI270_BMM150 library]()
- [ArduinoGraphics library]()
- [Library]() library.

## Downloading the Library and Core

Make sure the latest GIGA Core is installed in the Arduino IDE. **Tools > Board > Board Manager...**. Here you need to look for the **Arduino Mbed OS Giga Boards** and install it. Now you have to install the library needed for the IMU. Go to **Tools > Manage libraries..**, search for **Arduino_BMI270_BMM150** and install it, this library will help us with reading values from the IMU.

## Getting IMU Readings

The three axis that we will measure will be:

- x-axis: Measures horizontally
- y-axis: Measures vertically
- z-axis: Measures the rotational axis

This tutorial will assume that the screen is oriented as in the image below.

![Orientation of screen normally]()

## Creating an Image

Any image could be used here. This tutorial will use the following image of the Arduino logo. Alternatively, any raw RGB565 image can be used. If you have an image you want to use, you can use this [online image converter](https://lvgl.io/tools/imageconverter), or any other software that lets you convert an image to a raw RGB565 image. This website will output in the Binary RGB565 format.

[In sketch image]()

## Using the IMU Readings With the Image

Now to first get the readings from the IMU we will use the `"Arduino_BMI270_BMM150.h"` library. Then we need to set the image name variables with `extern const lv_img_dsc_t arduino_logo_1;`. To use the IMU set it up with `BoschSensorClass imu(Wire1);`.

```arduino

#include "Portenta_lvgl.h"
#include "lv_demo_widgets.h"
#include "Arduino_BMI270_BMM150.h"

extern const lv_img_dsc_t arduino_logo_1;

void LCD_ST7701_Init();

BoschSensorClass imu(Wire1);
```

initialize the display with `void LCD_ST7701_Init();`, start recieving IMU readings with `imu.begin();`. Next we can give the image its attributes.

```arduino
void setup() {
  Serial.begin(115200);
  giga_init_video();
  LCD_ST7701_Init();
  //lv_demo_widgets();
  imu.begin();

  LV_IMG_DECLARE(arduino_logo_1);
  lv_obj_t * obj;
  obj = lv_obj_create(lv_scr_act());
  lv_obj_set_size(obj, 350, 350);

  avatar = lv_img_create(obj);
  lv_img_set_src(avatar, &arduino_logo_1);
}

```

Now all that is left is to change the image depending on the IMU readings. First declare the variables that will hold the values. Then to assign them the IMU reading values use `imu.readAcceleration(x, y, z);`. Next we use `if ()` statements to change the rotation variable depending on the readings we are getting. And at the end we render the image with the correct rotation.

```arduino

uint8_t rotation = 0;

void loop() {
  float x, y, z;
  if (imu.accelerationAvailable()) {
    imu.readAcceleration(x, y, z);
    if ( z < 0.8 && z > -0.8) {
      if (x < -0.8) {
        rotation = 0;
      } else if (x > 0.8) {
        rotation = 2;
      } else if (y < -0.8) {
        rotation = 1;
      } else if (y > 0.8) {
        rotation = 3;
      }
      lv_img_set_angle(avatar,  900 - atan(x / y) * 180.0 / M_PI * 10);
    }
  }
}
```

The easiest way to tell what values you are getting depending on the orientation of the device you can use a simple sketch. Like the one below that will simply print the IMU values in the serial monitor. Take note of the values you are getting when you rotate the shield and you can use them in the previous sketch.

```arduino
#include "Arduino_BMI270_BMM150.h"

BoschSensorClass imu(Wire1);

void setup(){
  Serial.begin(115200);
  imu.begin();
}

void loop(){
  float x, y, z;
  if (imu.accelerationAvailable()) {
    imu.readAcceleration(x, y, z);
    Serial.print(x);
    Serial.print('\t');
    Serial.print(y);
    Serial.print('\t');
    Serial.println(z);
}
```

Now to put it all together where the image will change depending on how we rotate the board and shield:

```arduino

```

## Testing it Out

Now try and rotating your device to see if the image behaves correctly. If the image does not rotate correctly have another look at the values you entered into the previous sketch. It might help to try and run the simple IMU readings printer sketch to take a quick look at the IMU values in the serial monitor. This will help you figure out what values should be considered when the device is being moved. 

## Conclusion

Now you know how to use the GIGA Display Shields IMU sensor to gather readings for device orientation. And how to use these readings to make an image on the GIGA display shield maintain the correct orientation depending on what way it is facing. 