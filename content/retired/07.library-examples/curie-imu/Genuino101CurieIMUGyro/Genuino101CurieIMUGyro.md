---
author: 'Arduino'
description: 'With this tutorial you learn to read the gyroscope raw values and convert them into an angular velocity around each of the three axes.'
tags: [Arduino 101]
title: 'Arduino 101 CurieIMU Gyro'

---

With this tutorial you learn to read the gyroscope raw values and convert them into an angular velocity around each of the three axes. This information is useful to measure rotational movement around the three axes, something that acceleration can't measure if the movement is continuous.

## Hardware Required

- [Arduino 101](https://www.arduino.cc/en/Main/ArduinoBoard101)

## The Circuit

![](assets/genuino101fzz.jpg)

image developed using [Fritzing](http://www.fritzing.org).
No additional hardware is needed to use this tutorial.

## Software Essentials

### Libraries

CurieIMU.h is the library that gives access to all the parameters, features and readings of the IMU chip of the 101 board. This unit contains a three axes accelerometer and a three axes gyroscope. This library is part of the 101 board core and it is loaded together with the core files for Arduino 101. In this tutorial we read the raw gyro values.

### Functions

*float convertRawGyro(int gRaw)* - transforms the raw data read from the gyroscope (gRaw) into a value expressed in degrees per second (&#xB0;/s). The formula of the function must be adjusted to match the gyroscope range set with [setGyroRange](https://docs.arduino.cc/retired/archived-libraries/CurieIMU).

## Code

```arduino
/*

 * Copyright (c) 2016 Intel Corporation.  All rights reserved.

 * See the bottom of this file for the license terms.

 */

/*

   This sketch example demonstrates how the BMI160 on the

   Intel(R) Curie(TM) module can be used to read gyroscope data

*/

#include "CurieIMU.h"

void setup() {

  Serial.begin(9600); // initialize Serial communication

  while (!Serial);    // wait for the serial port to open

  // initialize device

  Serial.println("Initializing IMU device...");

  CurieIMU.begin();

  // Set the accelerometer range to 250 degrees/second

  CurieIMU.setGyroRange(250);
}

void loop() {

  float gx, gy, gz; //scaled Gyro values

  // read gyro measurements from device, scaled to the configured range

  CurieIMU.readGyroScaled(gx, gy, gz);

  // display tab-separated gyro x/y/z values

  Serial.print("g:\t");

  Serial.print(gx);

  Serial.print("\t");

  Serial.print(gy);

  Serial.print("\t");

  Serial.print(gz);

  Serial.println();
}

/*

   Copyright (c) 2016 Intel Corporation.  All rights reserved.

   This library is free software; you can redistribute it and/or

   modify it under the terms of the GNU Lesser General Public

   License as published by the Free Software Foundation; either

   version 2.1 of the License, or (at your option) any later version.

   This library is distributed in the hope that it will be useful,

   but WITHOUT ANY WARRANTY; without even the implied warranty of

   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU

   Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public

   License along with this library; if not, write to the Free Software

   Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

*/
```

