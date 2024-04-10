---
title: Serial.setTimeout()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

`Serial.setTimeout()` sets the maximum milliseconds to wait for serial
data. It defaults to 1000 milliseconds.

`Serial.setTimeout()` inherits from the [Stream](../../stream) utility
class.

**Syntax**

`_Serial_.setTimeout(time)`

**Parameters**

`_Serial_`: serial port object. See the list of available serial ports
for each board on the [Serial main page](../../serial).
`time`: timeout duration in milliseconds. Allowed data types: `long`.

**Returns**

Nothing

**Notes and Warnings**

Serial functions that use the timeout value set via
`_Serial_.setTimeout()`:

-   `_Serial_.find()`

-   `_Serial_.findUntil()`

-   `_Serial_.parseInt()`

-   `_Serial_.parseFloat()`

-   `_Serial_.readBytes()`

-   `_Serial_.readBytesUntil()`

-   `_Serial_.readString()`

-   `_Serial_.readStringUntil()`

**See also**

-   LANGUAGE [stream](../../stream)

-   LANGUAGE [stream.setTimeout()](../../stream/streamsettimeout)

