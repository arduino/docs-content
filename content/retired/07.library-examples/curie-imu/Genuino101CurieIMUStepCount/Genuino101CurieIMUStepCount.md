---
author: 'Arduino'
description: 'With this tutorial you learn to use the step counting feature of the IMU.'
tags: [Arduino 101]
title: 'Arduino 101 CurieIMU Step Count'

---

With this tutorial you learn to use the step counting feature of the IMU. You also learn to set the step detection mode and the interrupt based step counting. As an alternative, you can use a timed reading loop (polling) for a more relaxed output on the Serial monitor.

## Hardware Required

- [Arduino 101](https://www.arduino.cc/en/Main/ArduinoBoard101)

## The Circuit

![](assets/genuino101fzz.jpg)

image developed using [Fritzing](http://www.fritzing.org).
No additional hardware is needed to use this tutorial.

## Software Essentials

### Libraries

CurieIMU.h is the library that gives access to all the parameters, features and readings of the IMU chip of the 101 board. This unit contains a three axes accelerometer and a three axes gyroscope. This library is part of the 101 board core and it is loaded together with the core files for Arduino 101. In this tutorial we set up the Step detection feature and read the steps either with interrupt or polling.

### Functions

*updateStepCount()* - This function reads, when called, the number of steps counted since the initialisation of the IMU sensor. If the number is the same of the last reading, nothing happens, else the new value is printed on the Serial monitor and stored.

## Code

This sketch supports both interrupt driven and polling step counting. The Sketch is  set up for event driven (interrupt) reading, but you may go to 1s polling changing this line from `boolean stepEventsEnabeled = true;` to `boolean stepEventsEnabeled = false;`. The callback function that manages the interrupt, simply calls the updateStepCount() function at every step. This solution offers a more responsive reporting on the Serial monitor.

```arduino
/*

 * Copyright (c) 2016 Intel Corporation.  All rights reserved.

 * See the bottom of this file for the license terms.

 */

/*

   This sketch example demonstrates how the BMI160 accelerometer on the

   Intel(R) Curie(TM) module can be used as a Step Counter (pedometer)

*/

#include "CurieIMU.h"

/* To get an interrupt notification for every step detected,

    set stepEventsEnabeled to true. Otherwise, the main loop will

    poll for the current step count.

   By design, the step counter does not immediately update on every step detected.

   Please refer to Section 2.7 of the BMI160 IMU SensorData Sheet

   for more information on this feature.

*/

const int ledPin = 13;

bool stepEventsEnabeled = true;   // whether you're polling or using events
long lastStepCount = 0;              // step count on previous polling check

bool blinkState = false;          // state of the LED

void setup() {

  Serial.begin(9600); // initialize Serial communication

  while(!Serial) ;    // wait for serial port to connect.

  // pinMode(13, OUTPUT);

  // initialize the sensor:

  CurieIMU.begin();

  // turn on step detection mode:

  CurieIMU.setStepDetectionMode(CURIE_IMU_STEP_MODE_NORMAL);

  // enable step counting:

  CurieIMU.setStepCountEnabled(true);

  if (stepEventsEnabeled) {

    // attach the eventCallback function as the

    // step event handler:

    CurieIMU.attachInterrupt(eventCallback);

    CurieIMU.interrupts(CURIE_IMU_STEP);  // turn on step detection

    Serial.println("IMU initialisation complete, waiting for events...");

  }
}

void loop() {

  /* Instead of using step detection event notifications,

     we can check the step count periodically */

  if (!stepEventsEnabeled) {

    updateStepCount();

  }

  digitalWrite(13, blinkState);

  blinkState = !blinkState;

  delay(1000);
}

static void updateStepCount() {

  // get the step count:

  int stepCount = CurieIMU.getStepCount();

  // if the step count has changed, print it:

  if (stepCount != lastStepCount) {

    Serial.print("Step count: ");

    Serial.println(stepCount);

    // save the current count for comparison next check:

    lastStepCount = stepCount;

  }
}

static void eventCallback(void) {

  if (CurieIMU.stepsDetected())

    updateStepCount();
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

