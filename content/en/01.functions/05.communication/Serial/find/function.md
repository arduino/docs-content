---
title: Serial.find()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

`Serial.find()` reads data from the serial buffer until the target is
found. The function returns `true` if target is found, `false` if it
times out.

`Serial.find()` inherits from the [stream](../../stream) utility class.

**Syntax**

`_Serial_.find(target)`
`_Serial_.find(target, length)`

**Parameters**

`_Serial_`: serial port object. See the list of available serial ports
for each board on the [Serial main page](../../serial).
`target`: the string to search for. Allowed data types: `char`.
`length`: length of the target. Allowed data types: `size_t`.

**Returns**

Data type: `bool`.

**See also**

-   LANGUAGE [stream](../../stream)

-   LANGUAGE [stream.find()](../../stream/streamfind)

