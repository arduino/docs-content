---
title: Serial.begin()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

Sets the data rate in bits per second (baud) for serial data
transmission. For communicating with Serial Monitor, make sure to use
one of the baud rates listed in the menu at the bottom right corner of
its screen. You can, however, specify other rates - for example, to
communicate over pins 0 and 1 with a component that requires a
particular baud rate.

An optional second argument configures the data, parity, and stop bits.
The default is 8 data bits, no parity, one stop bit.

**Syntax**

`_Serial_.begin(speed)`
`_Serial_.begin(speed, config)`

**Parameters**

`_Serial_`: serial port object. See the list of available serial ports
for each board on the [Serial main page](../../serial).
`speed`: in bits per second (baud). Allowed data types: `long`.
`config`: sets data, parity, and stop bits. Valid values are:
`SERIAL_5N1`
`SERIAL_6N1`
`SERIAL_7N1`
`SERIAL_8N1` (the default)
`SERIAL_5N2`
`SERIAL_6N2`
`SERIAL_7N2`
`SERIAL_8N2`
`SERIAL_5E1`: even parity
`SERIAL_6E1`
`SERIAL_7E1`
`SERIAL_8E1`
`SERIAL_5E2`
`SERIAL_6E2`
`SERIAL_7E2`
`SERIAL_8E2`
`SERIAL_5O1`: odd parity
`SERIAL_6O1`
`SERIAL_7O1`
`SERIAL_8O1`
`SERIAL_5O2`
`SERIAL_6O2`
`SERIAL_7O2`
`SERIAL_8O2`

**Returns**

Nothing

**Example Code**

    void setup() {
        Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
    }

    void loop() {}

**Arduino Mega example:**

    // Arduino Mega using all four of its Serial ports
    // (Serial, Serial1, Serial2, Serial3),
    // with different baud rates:

    void setup() {
      Serial.begin(9600);
      Serial1.begin(38400);
      Serial2.begin(19200);
      Serial3.begin(4800);

      Serial.println("Hello Computer");
      Serial1.println("Hello Serial 1");
      Serial2.println("Hello Serial 2");
      Serial3.println("Hello Serial 3");
    }
    void loop() {}

Thanks to Jeff Gray for the mega example

**Notes and Warnings**

For USB CDC serial ports (e.g. `Serial` on the Leonardo),
`Serial.begin()` is irrelevant. You can use any baud rate and
configuration for serial communication with these ports. See the list of
available serial ports for each board on the [Serial main
page](../../serial).

The only `config` value supported for `Serial1` on the Arduino Nano 33
BLE and Nano 33 BLE Sense boards is `SERIAL_8N1`.

