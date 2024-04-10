---
title: Serial.read()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

Reads incoming serial data.

`Serial.read()` inherits from the [Stream](../../stream) utility class.

**Syntax**

`_Serial_.read()`

**Parameters**

`_Serial_`: serial port object. See the list of available serial ports
for each board on the [Serial main page](../../serial).

**Returns**

The first byte of incoming serial data available (or -1 if no data is
available). Data type: `int`.

**Example Code**

    int incomingByte = 0; // for incoming serial data

    void setup() {
      Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
    }

    void loop() {
      // send data only when you receive data:
      if (Serial.available() > 0) {
        // read the incoming byte:
        incomingByte = Serial.read();

        // say what you got:
        Serial.print("I received: ");
        Serial.println(incomingByte, DEC);
      }
    }

