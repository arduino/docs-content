---
title: bitClear()
categories: "Functions"
subCategories: "Bits and Bytes"
---

**Description**

Clears (writes a 0 to) a bit of a numeric variable.

**Syntax**

`bitClear(x, n)`

**Parameters**

`x`: the numeric variable whose bit to clear.
`n`: which bit to clear, starting at 0 for the least-significant
(rightmost) bit.

**Returns**

`x`: the value of the numeric variable after the bit at position `n` is
cleared.

**Example Code**

Prints the output of `bitClear(x,n)` on two given integers. The binary
representation of 6 is 0110, so when `n=1`, the second bit from the
right is set to 0. After this we are left with 0100 in binary, so 4 is
returned.

    void setup() {
      Serial.begin(9600);
      while (!Serial) {
        ; // wait for serial port to connect. Needed for native USB port only
      }

      int x = 6;
      int n = 1;
      Serial.print(bitClear(x, n)); // print the output of bitClear(x,n)
    }

    void loop() {
    }

**See also**

