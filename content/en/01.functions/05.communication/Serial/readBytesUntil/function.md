---
title: Serial.readBytesUntil()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

Serial.readBytesUntil() reads characters from the serial buffer into an
array. The function terminates (checks being done in this order) if the
determined length has been read, if it times out (see
[Serial.setTimeout()](../settimeout)), or if the terminator character is
detected (in which case the function returns the characters up to the
last character before the supplied terminator). The terminator itself is
not returned in the buffer.

`Serial.readBytesUntil()` returns the number of characters read into the
buffer. A 0 means that the `length` parameter &lt;= 0, a time out
occurred before any other input, or a termination character was found
before any other input.

`Serial.readBytesUntil()` inherits from the [Stream](../../stream)
utility class.

**Syntax**

`_Serial_.readBytesUntil(character, buffer, length)`

**Parameters**

`_Serial_`: serial port object. See the list of available serial ports
for each board on the [Serial main page](../../serial).
`character`: the character to search for. Allowed data types: `char`.
`buffer`: the buffer to store the bytes in. Allowed data types: array of
`char` or `byte`.
`length`: the number of bytes to read. Allowed data types: `int`.

**Returns**

Data type: `size_t`.

**Notes and Warnings**

The terminator character is discarded from the serial buffer, unless the
number of characters read and copied into the buffer equals `length`.

**See also**

-   LANGUAGE [Stream](../../stream)

-   LANGUAGE
    [Stream.readBytesUntil()](../../stream/streamreadbytesuntil)

