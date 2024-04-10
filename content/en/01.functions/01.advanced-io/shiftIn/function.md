---
title: shiftIn()
categories: "Functions"
subCategories: "Advanced I/O"
---

**Description**

Shifts in a byte of data one bit at a time. Starts from either the most
(i.e. the leftmost) or least (rightmost) significant bit. For each bit,
the clock pin is pulled high, the next bit is read from the data line,
and then the clock pin is taken low.

If you’re interfacing with a device that’s clocked by rising edges,
you’ll need to make sure that the clock pin is low before the first call
to `shiftIn()`, e.g. with a call to `digitalWrite(clockPin, LOW)`.

Note: this is a software implementation; Arduino also provides an [SPI
library](https://www.arduino.cc/en/Reference/SPI) that uses the hardware
implementation, which is faster but only works on specific pins.

**Syntax**

`byte incoming = shiftIn(dataPin, clockPin, bitOrder)`

**Parameters**

`dataPin`: the pin on which to input each bit. Allowed data types:
`int`.
`clockPin`: the pin to toggle to signal a read from **dataPin**.
`bitOrder`: which order to shift in the bits; either **MSBFIRST** or
**LSBFIRST**. (Most Significant Bit First, or, Least Significant Bit
First).

**Returns**

The value read. Data type: `byte`.

**See also**

