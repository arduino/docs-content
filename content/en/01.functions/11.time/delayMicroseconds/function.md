---
title: delayMicroseconds()
categories: "Functions"
subCategories: "Time"
---

**Description**

Pauses the program for the amount of time (in microseconds) specified by
the parameter. There are a thousand microseconds in a millisecond and a
million microseconds in a second.

Currently, the largest value that will produce an accurate delay is
16383; larger values can produce an extremely short delay. This could
change in future Arduino releases. For delays longer than a few thousand
microseconds, you should use `delay()` instead.

**Syntax**

`delayMicroseconds(us)`

**Parameters**

`us`: the number of microseconds to pause. Allowed data types:
`unsigned int`.

**Returns**

Nothing

**Example Code**

The code configures pin number 8 to work as an output pin. It sends a
train of pulses of approximately 100 microseconds period. The
approximation is due to execution of the other instructions in the code.

    int outPin = 8;               // digital pin 8

    void setup() {
      pinMode(outPin, OUTPUT);    // sets the digital pin as output
    }

    void loop() {
      digitalWrite(outPin, HIGH); // sets the pin on
      delayMicroseconds(50);      // pauses for 50 microseconds
      digitalWrite(outPin, LOW);  // sets the pin off
      delayMicroseconds(50);      // pauses for 50 microseconds
    }

**Notes and Warnings**

This function works very accurately in the range 3 microseconds and up
to 16383. We cannot assure that delayMicroseconds will perform precisely
for smaller delay-times. Larger delay times may actually delay for an
extremely brief time.

**See also**

