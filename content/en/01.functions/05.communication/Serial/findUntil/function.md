---
title: Serial.findUntil()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

`Serial.findUntil()` reads data from the serial buffer until a target
string of given length or terminator string is found.

The function returns true if the target string is found, false if it
times out.

`Serial.findUntil()` inherits from the [Stream](../../stream) utility
class.

**Syntax**

`_Serial_.findUntil(target, terminal)`

**Parameters**

`_Serial_`: serial port object. See the list of available serial ports
for each board on the [Serial main page](../../serial).
`target`: the string to search for. Allowed data types: `char`.
`terminal`: the terminal string in the search. Allowed data types:
`char`.

**Returns**

Data type: `bool`.

**See also**

-   LANGUAGE [stream](../../stream)

-   LANGUAGE [stream.findUntil()](../../stream/streamfinduntil)

