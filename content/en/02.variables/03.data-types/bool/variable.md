---
title: bool
categories: "Variables"
subCategories: "Data Types"
---

**Description**

A `bool` holds one of two values, `link:../../constants/truefalse[true]`
or `link:../../constants/truefalse[false]`. (Each `bool` variable
occupies one byte of memory.)

**Syntax**

`bool var = val;`

**Parameters**

`var`: variable name.
`val`: the value to assign to that variable.

**Example Code**

This code shows how to use the `bool` datatype.

    int LEDpin = 5;     // LED on pin 5
    int switchPin = 13; // momentary switch on 13, other side connected to ground

    bool running = false;

    void setup() {
      pinMode(LEDpin, OUTPUT);
      pinMode(switchPin, INPUT);
      digitalWrite(switchPin, HIGH);  // turn on pullup resistor
    }

    void loop() {
      if (digitalRead(switchPin) == LOW) {
        // switch is pressed - pullup keeps pin high normally
        delay(100);                     // delay to debounce switch
        running = !running;             // toggle running variable
        digitalWrite(LEDpin, running);  // indicate via LED
      }
    }

**See also**

