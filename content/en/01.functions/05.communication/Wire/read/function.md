---
title: read()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

This function reads a byte that was transmitted from a peripheral device
to a controller device after a call to `requestFrom()` or was
transmitted from a controller device to a peripheral device. `read()`
inherits from the Stream utility class.

**Syntax**

`Wire.read()`

**Parameters**

None.

**Returns**

The next byte received.

**Example**

\`\`\` \#include &lt;Wire.h&gt;

void setup() { Wire.begin(); // Join I2C bus (address is optional for
controller device) Serial.begin(9600); // Start serial for output }

void loop() { Wire.requestFrom(2, 6); // Request 6 bytes from slave
device number two

    // Slave may send less than requested
    while(Wire.available()) {
        char c = Wire.read();    // Receive a byte as character
        Serial.print(c);         // Print the character
    }

        delay(500);
    }
    ```

