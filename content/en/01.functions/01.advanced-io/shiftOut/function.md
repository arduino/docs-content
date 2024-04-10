---
title: shiftOut()
categories: "Functions"
subCategories: "Advanced I/O"
---

**Description**

Shifts out a byte of data one bit at a time. Starts from either the most
(i.e. the leftmost) or least (rightmost) significant bit. Each bit is
written in turn to a data pin, after which a clock pin is pulsed (taken
high, then low) to indicate that the bit is available.

Note- if you’re interfacing with a device that’s clocked by rising
edges, you’ll need to make sure that the clock pin is low before the
call to `shiftOut()`, e.g. with a call to `digitalWrite(clockPin, LOW)`.

This is a software implementation; see also the [SPI
library](https://www.arduino.cc/en/Reference/SPI), which provides a
hardware implementation that is faster but works only on specific pins.

**Syntax**

`shiftOut(dataPin, clockPin, bitOrder, value)`

**Parameters**

`dataPin`: the pin on which to output each bit. Allowed data types:
`int`.
`clockPin`: the pin to toggle once the dataPin has been set to the
correct value. Allowed data types: `int`.
`bitOrder`: which order to shift out the bits; either MSBFIRST or
LSBFIRST. (Most Significant Bit First, or, Least Significant Bit
First).
`value`: the data to shift out. Allowed data types: `byte`.

**Returns**

Nothing

**Example Code**

For accompanying circuit, see the [tutorial on controlling a 74HC595
shift register](https://arduino.cc/en/Tutorial/ShiftOut).

    //**************************************************************//
    //  Name    : shiftOutCode, Hello World                         //
    //  Author  : Carlyn Maw,Tom Igoe                               //
    //  Date    : 25 Oct, 2006                                      //
    //  Version : 1.0                                               //
    //  Notes   : Code for using a 74HC595 Shift Register           //
    //          : to count from 0 to 255                            //
    //****************************************************************

    //Pin connected to ST_CP of 74HC595
    int latchPin = 8;
    //Pin connected to SH_CP of 74HC595
    int clockPin = 12;
    ////Pin connected to DS of 74HC595
    int dataPin = 11;

    void setup() {
      //set pins to output because they are addressed in the main loop
      pinMode(latchPin, OUTPUT);
      pinMode(clockPin, OUTPUT);
      pinMode(dataPin, OUTPUT);
    }

    void loop() {
      //count up routine
      for (int j = 0; j < 256; j++) {
        //ground latchPin and hold low for as long as you are transmitting
        digitalWrite(latchPin, LOW);
        shiftOut(dataPin, clockPin, LSBFIRST, j);
        //return the latch pin high to signal chip that it
        //no longer needs to listen for information
        digitalWrite(latchPin, HIGH);
        delay(1000);
      }
    }

**Notes and Warnings**

The dataPin and clockPin must already be configured as outputs by a call
to [pinMode()](../../digital-io/pinmode).

shiftOut is currently written to output 1 byte (8 bits) so it requires a
two step operation to output values larger than 255.

    // Do this for MSBFIRST serial
    int data = 500;
    // shift out highbyte
    shiftOut(dataPin, clock, MSBFIRST, (data >> 8));
    // shift out lowbyte
    shiftOut(dataPin, clock, MSBFIRST, data);

    // Or do this for LSBFIRST serial
    data = 500;
    // shift out lowbyte
    shiftOut(dataPin, clock, LSBFIRST, data);
    // shift out highbyte
    shiftOut(dataPin, clock, LSBFIRST, (data >> 8));

**See also**
