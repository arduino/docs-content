---
author: 'Arduino'
description: 'With this tutorial you learn to read the three axes of the accelerometer contained in the IMU (Inertial Measurement Unit) of the 101 board.'
tags: [Arduino 101]
title: 'Arduino 101 CurieIMU Accelerometer'

---

With this tutorial you learn to read the three axes of the accelerometer contained in the IMU (Inertial Measurement Unit) of the 101 board. Each axis measures the acceleration within a range defined by a specific function - [setAccelerometerRange](https://docs.arduino.cc/retired/archived-libraries/CurieIMU) - and returns a raw value that needs to be converted to get a value in mg. The result of the conversion is printed on the Serial monitor as triplets of acceleration values (X, Y and Z).

## Hardware Required

- [Arduino 101](https://www.arduino.cc/en/Main/ArduinoBoard101)

## The Circuit

![](assets/genuino101fzz.jpg)

image developed using [Fritzing](http://www.fritzing.org).
No additional hardware is needed to use this tutorial.

## Software Essentials

### Libraries

CurieIMU.h is the library that gives access to all the parameters, features and readings of the IMU chip of the 101 board. This unit contains a three axes accelerometer and a three axes gyroscope. This library is part of the 101 board core and it is loaded together with the core files for Arduino 101. In this tutorial we read the raw accelerometer values.

### Functions

*float convertRawAcceleration(int aRaw)* - transforms the raw data read from the accelerometer (aRaw) into a value expressed in mg (thousandths of g). The formula of the function must be adjusted to match the accelerometer range set with [setAccelerometerRange](https://docs.arduino.cc/retired/archived-libraries/CurieIMU).

## Code

This sketch is the simplest possible and doesn't include any calibration. The Accelerometer data is refreshed every 5 seconds.

```arduino
/*

 * Copyright (c) 2016 Intel Corporation.  All rights reserved.

 * See the bottom of this file for the license terms.

 */

/*

   This sketch example demonstrates how the BMI160 on the

   Intel(R) Curie(TM) module can be used to read accelerometer data

*/

#include "CurieIMU.h"

void setup() {

  Serial.begin(9600); // initialize Serial communication

  while (!Serial);    // wait for the serial port to open

  // initialize device

  Serial.println("Initializing IMU device...");

  CurieIMU.begin();

  // Set the accelerometer range to 2G

  CurieIMU.setAccelerometerRange(2);
}

void loop() {

  float ax, ay, az;   //scaled accelerometer values

  // read accelerometer measurements from device, scaled to the configured range

  CurieIMU.readAccelerometerScaled(ax, ay, az);

  // display tab-separated accelerometer x/y/z values

  Serial.print("a:\t");

  Serial.print(ax);

  Serial.print("\t");

  Serial.print(ay);

  Serial.print("\t");

  Serial.print(az);

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

