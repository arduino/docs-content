---
title: 'GIGA Display Shield Touch Interface'
description: 'Learn how to use the touch interface on the GIGA Display Shield.'
author: Karl Söderby
tags: [Display, Touch Screen]
---

The [GIGA Display Shield](/hardware/giga-display-shield) has an advanced touch interface, supported via the [Arduino_GigaDisplayTouch](https://github.com/arduino-libraries/Arduino_GigaDisplayTouch) library.

This library is used to return the number of contact points, and the `x,y` coordinates for each of contacts, and in this guide you will learn about different methods to obtain the data.

## Hardware & Software Needed

- [GIGA R1 WiFi](/hardware/giga-r1-wifi).
- [GIGA Display Shield](/hardware/giga-display-shield)
- [Arduino IDE](https://www.arduino.cc/en/software)

## Overview

The **Arduino_GigaDisplayTouch** library can be used in combination with any of the available graphics libraries ([see available options](/tutorials/giga-display-shield/getting-started#overview)), but is independent from them and works standalalone.

The library has two methods of reading sensor data:
- **Polling** - continuously read the sensor data through the `getTouchPoint()` method.
- **IRQ** - only read data when the display is touched through an interrupt and a callback function, using the `onDetect()` method.

The number of contacts (fingers touching) can be retrieved and stored as an integer:

```arduino
contacts = touchDetector.getTouchPoints(points);
```

To read the `x` and `y` coordinates, we need to use a specific `struct` called `GDTpoint_t` which contains the values. The example belows simply iterates through the number of `contacts` and stores the coordinates of each contact.

```arduino
GDTpoint_t points[5];
uint8_t contacts;

for (uint8_t i = 0; i < contacts; i++) {
  x_coordinate = points[i].x;
  y_coordinate = points[i].y;
}
```

### Touch Interface

An option to consider 

### Gesture Detection

As you are able to retrieve multiple touch points at very fast rates, it is possible to create **gesture detections**. You could for example:
- change layout when swiping three fingers right,
- zoom in and out using two fingers,
- adjust the volume by swiping a finger from the bottom right corner and up,
- and many more scenarios.

This library can together with the supported graphics libraries create really interactions that we are using in modern day smartphones, tablets etc., with an easy interface and very fast response times.

## Polling Example

The polling example demonstrates how to continuously read the touch sensor using the `getTouchPoints()` method. Whenever the display screen is touched, the number of contacts + the coordinates of each contact is printed to the Serial Monitor.

<CodeBlock url="https://github.com/arduino-libraries/Arduino_GigaDisplayTouch/blob/main/examples/Touch_Polling/Touch_Polling.ino" className="arduino"/>

## IRQ Example

The IRQ example demonstrates how to set up an interrupt that triggers a function anytime the screen is touched. The interrupt is set up inside of the `setup()` function, using the `onDetect(function)` method. 

<CodeBlock url="https://github.com/arduino-libraries/Arduino_GigaDisplayTouch/blob/main/examples/Touch_IRQ/Touch_IRQ.ino" className="arduino"/>

## Delay Example

An important factor to consider is that the `loop()` on the GIGA R1 is executed at a very fast rate, meaning that you will register several touches each time you touch the screen.

This means that whenever you tap the screen, even quickly, you register somewhere between **5-20 touches**. So if you want a specific function to only execute once on a specific touch point, you will need to implement a delay in your code. 

Using the conventional, but blocking `delay(microseconds)` method is possible but not ideal. The best method to register only a single touch is through using the `millis()` method.

The example below is based on the **Polling Example**, and limits the if statement to only execute once every `250` milliseconds. This can be edited in the `threshold` variable.

```arduino
#include "Arduino_GigaDisplayTouch.h"

Arduino_GigaDisplayTouch touchDetector;
int lastTouch;
int threshold = 250; //time in milliseconds

void setup() {
  Serial.begin(115200);
  while(!Serial) {}

  if (touchDetector.begin()) {
    Serial.print("Touch controller init - OK");
  } else {
    Serial.print("Touch controller init - FAILED");
    while(1) ;
  }
}

void loop() {
  uint8_t contacts;
  GDTpoint_t points[5];
  
  contacts = touchDetector.getTouchPoints(points);

  // check if more time than the threshold defined has passed
  if (contacts > 0 && (millis() - lastTouch > threshold) ) {
    Serial.print("Contacts: ");
    Serial.println(contacts);

    for (uint8_t i = 0; i < contacts; i++) {
      Serial.print(points[i].x);
      Serial.print(" ");
      Serial.println(points[i].y);
    }
    lastTouch = millis(); // register last touch
  }

  delay(1);
}
```

## GFX Touch Example

The below example requires uses the [Arduino_GigaDisplay_GFX](https://github.com/arduino/Arduino_GigaDisplay_GFX) library, and demonstrates how to change a boolean whenever you touch the screen. It implements the `millis()` function to limit the number of executions. 

Anytime the screen is touched, the background and text color inverts (black and white). 

```arduino
#include "Arduino_GigaDisplay_GFX.h"
#include "Arduino_GigaDisplayTouch.h"

Arduino_GigaDisplayTouch touchDetector;
GigaDisplay_GFX display;

#define WHITE 0xffff
#define BLACK 0x0000

#define screen_size_x 480
#define screen_size_y 800

int touch_x;
int touch_y;

int lastTouch;
int threshold = 250;

bool switch_1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  display.begin();

  if (touchDetector.begin()) {
    Serial.print("Touch controller init - OK");
  } else {
    Serial.print("Touch controller init - FAILED");
    while (1)
      ;
  }
  changeSwitch();
}

void loop() {
  uint8_t contacts;
  GDTpoint_t points[5];
  contacts = touchDetector.getTouchPoints(points);
  
  if (contacts > 0 && (millis() - lastTouch > threshold)) {
    Serial.print("Contacts: ");
    Serial.println(contacts);

    //record the x,y coordinates 
    for (uint8_t i = 0; i < contacts; i++) {
      touch_x = points[i].x;
      touch_y = points[i].y;
    }

    //as the display is 480x800, anywhere you touch the screen it will trigger
    if (touch_x < screen_size_x && touch_y < screen_size_y) {
      switch_1 = !switch_1;
      Serial.println("switched");
      changeSwitch();
    }
    lastTouch = millis();
  }
}

void changeSwitch() {
  if (switch_1) {
    display.fillScreen(BLACK);
    display.setTextColor(WHITE);
  } else {
    display.fillScreen(WHITE);
    display.setTextColor(BLACK);
  }
  display.setCursor(50, screen_size_y/2);
  display.setTextSize(5);
  display.print("Switched");
}
```