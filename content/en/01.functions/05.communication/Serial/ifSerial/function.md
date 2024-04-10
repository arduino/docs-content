---
title: if(Serial)
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

Indicates if the specified Serial port is ready.

On the boards with native USB, `if (Serial)` (or `if(SerialUSB)` on the
Due) indicates whether or not the USB CDC serial connection is open. For
all other boards, and the non-USB CDC ports, this will always return
true.

**Syntax**

`if (Serial)`

**Parameters**

None

**Returns**

Returns true if the specified serial port is available. This will only
return false if querying the Leonardo’s USB CDC serial connection before
it is ready. Data type: `bool`.

**Example Code**

    void setup() {
      //Initialize serial and wait for port to open:
      Serial.begin(9600);
      while (!Serial) {
        ; // wait for serial port to connect. Needed for native USB
      }
    }

    void loop() {
      //proceed normally
    }

**Notes and Warnings**

This function adds a delay of 10ms in an attempt to solve "open but not
quite" situations. Don’t use it in tight loops.

