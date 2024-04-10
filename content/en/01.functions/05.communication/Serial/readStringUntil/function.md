---
title: Serial.readStringUntil()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

`readStringUntil()` reads characters from the serial buffer into a
String. The function terminates if it times out (see
[setTimeout()](../settimeout)).

`Serial.readStringUntil()` inherits from the [Stream](../../stream)
utility class.

**Syntax**

`_Serial_.readStringUntil(terminator)`

**Parameters**

`_Serial_`: serial port object. See the list of available serial ports
for each board on the [Serial main page](../../serial).
`terminator`: the character to search for. Allowed data types: `char`.

**Returns**

The entire `String` read from the serial buffer, up to the terminator
character. If the terminator character can’t be found, or if there is no
data before the terminator character, it will return `NULL`.

**Notes and Warnings**

The terminator character is discarded from the serial buffer. If the
terminator character can’t be found, all read characters will be
discarded.

**See also**

-   LANGUAGE [Serial](../../serial)

-   LANGUAGE [begin()](../begin)

-   LANGUAGE [end()](../end)

-   LANGUAGE [available()](../available)

-   LANGUAGE [read()](../read)

-   LANGUAGE [peek()](../peek)

-   LANGUAGE [flush()](../flush)

-   LANGUAGE [print()](../print)

-   LANGUAGE [println()](../println)

-   LANGUAGE [write()](../write)

-   LANGUAGE [SerialEvent()](../serialevent)

-   LANGUAGE [stream.parseFloat()](../../stream/streamparsefloat)

