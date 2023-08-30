---
title: Screen Orientation With IMU Readings
description: 'Learn how to use the GIGA Display Shield's IMU to determine the shield's orientation.'
author: Benjamin Dannegård
tags: [Display, IMU, orientation, lvgl]
---

Any modern device with a screen uses sensors to determine the correct orientation in which an image should be displayed. Using the Arduino GIGA R1 WiFi with the GIGA Display Shield we can read values given by the onboard IMU to determine what orientation an image should be given. This tutorial will show you how to manipulate an image on the GIGA Display Shield using LVGL and readings from the IMU sensor.

## Hardware & Software Needed

- [GIGA R1 WiFi](/hardware/giga-r1)
- [GIGA Display Shield]()
- [Arduino IDE](https://www.arduino.cc/en/software)
- [Arduino_BMI270_BMM150 library](https://reference.arduino.cc/reference/en/libraries/arduino_bmi270_bmm150/)
- [Arduino_H7_Video library](https://github.com/arduino/ArduinoCore-mbed/tree/main/libraries/Arduino_H7_Video)
- [LVGL library](https://reference.arduino.cc/reference/en/libraries/lvgl/)

## Downloading the Library and Core

Make sure the latest GIGA Core is installed in the Arduino IDE. **Tools > Board > Board Manager...**. Here you need to look for the **Arduino Mbed OS Giga Boards** and install it. Now you have to install the library needed for the IMU and the library for handling the image. Go to **Tools > Manage libraries..**, search for **Arduino_BMI270_BMM150**, and install it. This library will help us with reading values from the IMU. Now search for **LVGL**, and install it. This library will be used for the image and rotating it.

## Using the IMU Readings With the Image

Now to first get the readings from the IMU we will use the `"Arduino_BMI270_BMM150.h"` library. The `"Arduino_H7_Video.h"` and 
`"lvgl.h"` libraries will help us handle the image. Set up the display dimensions with `Arduino_H7_Video Display(800, 480, GigaDisplayShield);`. To use the IMU set it up with `BoschSensorClass imu(Wire1);`. Next, we can give the image its attributes.

```arduino
#include "Arduino_BMI270_BMM150.h"
#include "Arduino_H7_Video.h"
#include "lvgl.h"

Arduino_H7_Video          Display(800, 480, GigaDisplayShield); /* Arduino_H7_Video Display(1024, 768, USBCVideo); */

BoschSensorClass imu(Wire1);
```

Start receiving IMU readings with `imu.begin();` and start the display with `Display.begin();`. Then we can assign attributes to the images such as its source, alignment and how the rotation should behave. For more information on image attributes with LVGL, check out our [LVGL tutorial](lvgl-guide#image).

```arduino
LV_IMG_DECLARE(img_arduinologo);
lv_obj_t * img;

void setup() {
  Serial.begin(115200);
  
  Display.begin();
  imu.begin();

  img = lv_img_create(lv_scr_act());
  lv_img_set_src(img, &img_arduinologo);
  lv_obj_align(img, LV_ALIGN_CENTER, 0, 0);
  lv_img_set_pivot(img, (img_arduinologo.header.w)/2, (img_arduinologo.header.h)/2); /* Rotate around the center of the image */
}
```

Now all that is left is to change the image depending on the IMU readings. First, declare the variables that will hold the values. Then to assign them the IMU reading values use `imu.readAcceleration(x, y, z);`. Next, we use `if ()` statements to change the rotation variable depending on the readings we are getting. And at the end, we render the image with the correct rotation. When the correct rotation has been calculated, we can apply it to the image using `lv_img_set_angle(img, rot_angle);`.

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
      int16_t rot_angle = 900 - atan(x / y) * 180.0 / M_PI * 10; //Calculation for the rotation angle
      lv_img_set_angle(img, rot_angle);
    }
  }
  lv_timer_handler();
}
```

### IMU Test Sketch

The easiest way to tell what values you are getting depending on the orientation of the device is to use a simple sketch, like the one below that will print the IMU values in the serial monitor. Take note of the values you are getting when you rotate the shield and you can use them in the full sketch.

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
}
```

### Full Sketch

Now to put it all together where the image will change depending on how we rotate the board and shield:

```arduino
#include "Arduino_BMI270_BMM150.h"
#include "Arduino_H7_Video.h"
#include "lvgl.h"

Arduino_H7_Video          Display(800, 480, GigaDisplayShield); /* Arduino_H7_Video Display(1024, 768, USBCVideo); */

BoschSensorClass imu(Wire1);

LV_IMG_DECLARE(img_arduinologo);
lv_obj_t * img;

void setup() {
  Serial.begin(115200);
  
  Display.begin();
  imu.begin();

  img = lv_img_create(lv_scr_act());
  lv_img_set_src(img, &img_arduinologo);
  lv_obj_align(img, LV_ALIGN_CENTER, 0, 0);
  lv_img_set_pivot(img, (img_arduinologo.header.w)/2, (img_arduinologo.header.h)/2); /* Rotate around the center of the image */
}

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
      int16_t rot_angle = 900 - atan(x / y) * 180.0 / M_PI * 10;
      lv_img_set_angle(img, rot_angle);
    }
  }
  lv_timer_handler();
}
```

### Using Another Image 

Any image could be the sketch. This tutorial and the example uses an image of the Arduino logo. Alternatively, any raw RGB565 image can be used. If you have an image you want to use, you can use this [online image converter](https://lvgl.io/tools/imageconverter), or any other software that lets you convert an image to a raw RGB565 image. This website will output in the Binary RGB565 format. For further instructions on how to display your own image, have a look at our [Text and Image tutorial](text-and-image).

## Testing it Out

Now try rotating your device to see if the image behaves correctly. If the image does not rotate correctly have another look at the values you entered into the previous sketch. It might help to try and run the simple IMU readings printer sketch to take a quick look at the IMU values in the serial monitor. This will help you figure out what values should be considered when the device is being moved. 

![Gif of the orientation sketch running on the screen]()

## Conclusion

Now you know how to use the GIGA Display Shield's IMU sensor to gather readings for device orientation, and how to use these readings to make an image on the GIGA Display Shield maintain the correct orientation depending on what way it is facing. 