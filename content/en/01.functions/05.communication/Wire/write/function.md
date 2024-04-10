---
title: write()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

This function writes data from a peripheral device in response to a
request from a controller device, or queues bytes for transmission from
a controller to peripheral device (in-between calls to
`beginTransmission()` and `endTransmission()`).

**Syntax**

`Wire.write(value)` `Wire.write(string)` `Wire.write(data, length)`

**Parameters**

-   *value*: a value to send as a single byte.

-   *string*: a string to send as a series of bytes.

-   *data*: an array of data to send as bytes.

-   *length*: the number of bytes to transmit.

**Returns**

The number of bytes written (reading this number is optional).

**Example**

\`\`\` \#include &lt;Wire.h&gt;

byte val = 0;

void setup() { Wire.begin(); // Join I2C bus }

void loop() { Wire.beginTransmission(44); // Transmit to device number
44 (0x2C)

    Wire.write(val);             // Sends value byte
    Wire.endTransmission();      // Stop transmitting

    val++;                       // Increment value

    // if reached 64th position (max)
    if(val == 64) {
        val = 0;                   // Start over from lowest value
    }

        delay(500);
    }
    ```

