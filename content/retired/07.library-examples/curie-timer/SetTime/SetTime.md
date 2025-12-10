---
author: 'Arduino'
description: 'This example demonstrate how to use the CurieTime library methods.'
tags: [Arduino 101]
title: 'CurieTime Read Test'

---

## Hardware Required

- Arduino 101 Board

## Code

```arduino

/*

 * Copyright (c) 2016 Intel Corporation.  All rights reserved.

 * See the bottom of this file for the license terms.

 */

#include <CurieTime.h>

void setup() {

  Serial.begin(9600); // initialize Serial communication

  while(!Serial) ;    // wait for serial port to connect.

  // set the current time to 14:27:00, December 14th, 2015

  setTime(14, 27, 00, 14, 12, 2015);
}

void loop() {

  Serial.print("Time now is: ");

  print2digits(hour());

  Serial.print(":");

  print2digits(minute());

  Serial.print(":");

  print2digits(second());

  Serial.print(" ");

  Serial.print(day());

  Serial.print("/");

  Serial.print(month());

  Serial.print("/");

  Serial.print(year());

  Serial.println();

  delay(1000);
}

void print2digits(int number) {

  if (number >= 0 && number < 10) {

    Serial.print('0');

  }

  Serial.print(number);
}

/*

 * Copyright (c) 2016 Intel Corporation.  All rights reserved.

 *

 * This library is free software; you can redistribute it and/or

 * modify it under the terms of the GNU Lesser General Public

 * License as published by the Free Software Foundation; either

 * version 2.1 of the License, or (at your option) any later version.

 *

 * This library is distributed in the hope that it will be useful,

 * but WITHOUT ANY WARRANTY; without even the implied warranty of

 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU

 * Lesser General Public License for more details.

 *

 * You should have received a copy of the GNU Lesser General Public

 * License along with this library; if not, write to the Free Software

 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

 */
```