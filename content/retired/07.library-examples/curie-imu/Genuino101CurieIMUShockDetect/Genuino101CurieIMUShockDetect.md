---
author: 'Arduino'
description: 'With this tutorial you learn to set up one of the features of the IMU and manage the interrupt generated when the feature sensing conditions are met.'
tags: [Arduino 101]
title: 'Arduino 101 CurieIMU Shock Detect'
---

With this tutorial you learn to set up one of the features of the IMU and manage the interrupt generated when the feature's sensing conditions are met.. Each feature can be fine tuned setting up trigger and duration values. Once set up, the IMU monitors the relevand accelerometer and gyroscope values looking for the data pattern that corresponds to the expected event. In this case we expect a shock.

## Hardware Required

- [Arduino 101](https://www.arduino.cc/en/Main/ArduinoBoard101)

## The Circuit

![](assets/genuino101fzz.jpg)

image developed using [Fritzing](http://www.fritzing.org).
No additional hardware is needed to use this tutorial.

## Software Essentials

### Libraries

CurieIMU.h is the library that gives access to all the parameters, features and readings of the IMU chip of the 101 board. This unit contains a three axes accelerometer and a three axes gyroscope. This library is part of the 101 board core and it is loaded together with the core files for Arduino 101. In this tutorial we set up the Shock detection feature and we enable its interrupt.

### Functions

none

## Code

A shock is when the sensor reads a significative acceleration for a very short time. The thdeshold defines how big the acceleration should be to be considered relevant, while the duration that is either 50 or 75 ms. These two fixed values have been defined to spot the shock pattern in high g events. Once set up threshold and duration, the interrupt is armed  and the callback function is set to  `eventCallback`, When the interrupt is asserted, the execution goes to the callback function where the [getInterruptStatus](https://docs.arduino.cc/retired/archived-libraries/CurieIMU) lets you check for the various axis and orientation combinations, finding exactly on which axis and which direction the shock happened.

```arduino
/*

 * Copyright (c) 2016 Intel Corporation.  All rights reserved.

 * See the bottom of this file for the license terms.

 */

/*

   This sketch example demonstrates how the BMI160 accelerometer on the

   Intel(R) Curie(TM) module can be used to detect shocks or sudden movements

*/

#include "CurieIMU.h"

bool blinkState = false;          // state of the LED

void setup() {

  Serial.begin(9600); // initialize Serial communication

  while(!Serial) ;    // wait for serial port to connect..

  /* Initialise the IMU */

  CurieIMU.begin();

  CurieIMU.attachInterrupt(eventCallback);

  /* Enable Shock Detection */

  CurieIMU.setDetectionThreshold(CURIE_IMU_SHOCK, 1500); // 1.5g = 1500 mg

  CurieIMU.setDetectionDuration(CURIE_IMU_SHOCK, 50);   // 50ms

  CurieIMU.interrupts(CURIE_IMU_SHOCK);

  Serial.println("IMU initialisation complete, waiting for events...");
}

void loop() {

  // blink the LED in the main loop:

  digitalWrite(13, blinkState);

  blinkState = !blinkState;

  delay(1000);
}

static void eventCallback(void)
{

  if (CurieIMU.getInterruptStatus(CURIE_IMU_SHOCK)) {

    if (CurieIMU.shockDetected(X_AXIS, POSITIVE))

      Serial.println("Negative shock detected on X-axis");

    if (CurieIMU.shockDetected(X_AXIS, NEGATIVE))

      Serial.println("Positive shock detected on X-axis");

    if (CurieIMU.shockDetected(Y_AXIS, POSITIVE))

      Serial.println("Negative shock detected on Y-axis");

    if (CurieIMU.shockDetected(Y_AXIS, NEGATIVE))

      Serial.println("Positive shock detected on Y-axis");

    if (CurieIMU.shockDetected(Z_AXIS, POSITIVE))

      Serial.println("Negative shock detected on Z-axis");

    if (CurieIMU.shockDetected(Z_AXIS, NEGATIVE))

      Serial.println("Positive shock detected on Z-axis");

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
