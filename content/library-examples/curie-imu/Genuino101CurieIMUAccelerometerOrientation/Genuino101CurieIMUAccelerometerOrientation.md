---
author: 'Arduino'
description: 'With this tutorial you convert the accelerometer readings into an orientation on the 101 board.'
tags: [Arduino 101]
title: 'Arduino 101 CurieIMU Accelerometer Orientation'

---

With this tutorial you convert the accelerometer readings into an orientation. The orientation is then printed on the Serial monitor as text that tells you the position of the processor, the USB connector and the pins as reference.

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

None

## Code

The orientation of the board is calculated using the orientation of the three axes. The Z axis passes through the pcb: component side upwards is positive, while going below is negative. The X axis goes from USB connector to Bluetooth® antenna if positive, while Y axis goes from analog and power pins to digital pins when positive. Using the three axes signs the sketch calculates the orientation of the whole board.

```arduino
/*

 * Copyright (c) 2016 Intel Corporation.  All rights reserved.

 * See the bottom of this file for the license terms.

 */

/*

   This sketch example demonstrates how the BMI160 on the

   Intel(R) Curie(TM) module can be used to read accelerometer data

   and translate it to an orientation

*/

#include "CurieIMU.h"

int lastOrientation = - 1; // previous orientation (for comparison)

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
int orientation = - 1;   // the board's orientation

  String orientationString; // string for printing description of orientation

  /*

    The orientations of the board:

    0: flat, processor facing up

    1: flat, processor facing down

    2: landscape, analog pins down

    3: landscape, analog pins up

    4: portrait, USB connector up

    5: portrait, USB connector down

  */

  // read accelerometer:

  int x = CurieIMU.readAccelerometer(X_AXIS);

  int y = CurieIMU.readAccelerometer(Y_AXIS);

  int z = CurieIMU.readAccelerometer(Z_AXIS);

  // calculate the absolute values, to determine the largest

  int absX = abs(x);

  int absY = abs(y);

  int absZ = abs(z);

  if ( (absZ > absX) && (absZ > absY)) {

    // base orientation on Z

    if (z > 0) {

      orientationString = "up";

      orientation = 0;

    } else {

      orientationString = "down";

      orientation = 1;

    }

  } else if ( (absY > absX) && (absY > absZ)) {

    // base orientation on Y

    if (y > 0) {

      orientationString = "digital pins up";

      orientation = 2;

    } else {

      orientationString = "analog pins up";

      orientation = 3;

    }

  } else {

    // base orientation on X

    if (x < 0) {

      orientationString = "connector up";

      orientation = 4;

    } else {

      orientationString = "connector down";

      orientation = 5;

    }

  }

  // if the orientation has changed, print out a description:

  if (orientation != lastOrientation) {

    Serial.println(orientationString);

    lastOrientation = orientation;

  }
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

