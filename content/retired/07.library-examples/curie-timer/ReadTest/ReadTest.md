---
author: 'Arduino'
description: 'This example demonstrate how to use the CurieTime library methods.'
tags: [Arduino 101]
title: 'CurieTime Read Test with Arduino 101'

---

##  Hardware Required

- Arduino 101 Board

##  Code

```arduino

/*

 * Copyright (c) 2016 Intel Corporation.  All rights reserved.

 * See the bottom of this file for the license terms.

 */

#include <CurieTime.h>

void setup() {

  Serial.begin(9600); // initialize Serial communication

  while (!Serial);    // wait for serial port to connect.

  Serial.println("CurieTime Read Test");

  Serial.println("-------------------");
}

void loop() {

  Serial.print("Ok, Time = ");

  print2digits(hour());

  Serial.write(':');

  print2digits(minute());

  Serial.write(':');

  print2digits(second());

  Serial.print(", Date (D/M/Y) = ");

  Serial.print(day());

  Serial.write('/');

  Serial.print(month());

  Serial.write('/');

  Serial.print(year());

  Serial.println();

  delay(1000);
}

void print2digits(int number) {

  if (number >= 0 && number < 10) {

    Serial.write('0');

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