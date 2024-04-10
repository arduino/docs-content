---
title: digitalRead()
categories: "Functions"
subCategories: "Digital I/O"
---

**Description**

Reads the value from a specified digital pin, either `HIGH` or `LOW`.

**Syntax**

`digitalRead(pin)`

**Parameters**

`pin`: the Arduino pin number you want to read

**Returns**

`HIGH` or `LOW`

**Example Code**

Sets pin 13 to the same value as pin 7, declared as an input.

    int ledPin = 13;  // LED connected to digital pin 13
    int inPin = 7;    // pushbutton connected to digital pin 7
    int val = 0;      // variable to store the read value

    void setup() {
      pinMode(ledPin, OUTPUT);  // sets the digital pin 13 as output
      pinMode(inPin, INPUT);    // sets the digital pin 7 as input
    }

    void loop() {
      val = digitalRead(inPin);   // read the input pin
      digitalWrite(ledPin, val);  // sets the LED to the button's value
    }

**Notes and Warnings**

If the pin isn’t connected to anything, `digitalRead()` can return
either `HIGH` or `LOW` (and this can change randomly).

The analog input pins can be used as digital pins, referred to as A0,
A1, etc. The exception is the Arduino Nano, Pro Mini, and Mini’s A6 and
A7 pins, which can only be used as analog inputs.

**See also**

-   EXAMPLE [Description of the digital
    pins^](http://arduino.cc/en/Tutorial/DigitalPins)
