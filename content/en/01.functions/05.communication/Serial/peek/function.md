---
title: Serial.peek()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

Returns the next byte (character) of incoming serial data without
removing it from the internal serial buffer. That is, successive calls
to `peek()` will return the same character, as will the next call to
`read()`.

`Serial.peek()` inherits from the [Stream](../../stream) utility class.

**Syntax**

`_Serial_.peek()`

**Parameters**

`_Serial_`: serial port object. See the list of available serial ports
for each board on the [Serial main page](../../serial).

**Returns**

The first byte of incoming serial data available (or -1 if no data is
available). Data type: `int`.

**See also**

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

-   LANGUAGE [Stream.peek()](../../stream/streampeek)

