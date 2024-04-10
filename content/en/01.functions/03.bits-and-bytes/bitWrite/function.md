---
title: bitWrite()
categories: "Functions"
subCategories: "Bits and Bytes"
---

**Description**

Writes to a bit of a variable, e.g. `bool`, `int`, `long`. Note that
`float` & `double` are not supported. You can write to a bit of
variables up to an `unsigned long` (32 bits / 4 bytes).

**Syntax**

`bitWrite(x, n, b)`

**Parameters**

`x`: the numeric variable to which to write.
`n`: which bit of the number to write, starting at 0 for the
least-significant (rightmost) bit.
`b`: the value to write to the bit (0 or 1).

**Returns**

Nothing

**Example Code**

Demonstrates the use of bitWrite by printing the value of a variable to
the Serial Monitor before and after the use of `bitWrite()`.

    void setup() {
      Serial.begin(9600);
      while (!Serial) {}  // wait for serial port to connect. Needed for native USB port only
      byte x = 0b10000000;  // the 0b prefix indicates a binary constant
      Serial.println(x, BIN); // 10000000
      bitWrite(x, 0, 1);  // write 1 to the least significant bit of x
      Serial.println(x, BIN); // 10000001
    }

    void loop() {}

**See also**

