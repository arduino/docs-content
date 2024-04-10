---
title: Serial.availableForWrite()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

Get the number of bytes (characters) available for writing in the serial
buffer without blocking the write operation.

**Syntax**

`_Serial_.availableForWrite()`

**Parameters**

`_Serial_`: serial port object. See the list of available serial ports
for each board on the [Serial main page](../../serial).

**Returns**

The number of bytes available to write.

**See also**

-   LANGUAGE [begin()](../begin)

-   LANGUAGE [end()](../end)

-   LANGUAGE [read()](../read)

-   LANGUAGE [peek()](../peek)

-   LANGUAGE [flush()](../flush)

-   LANGUAGE [print()](../print)

-   LANGUAGE [println()](../println)

-   LANGUAGE [write()](../write)

-   LANGUAGE [SerialEvent()](../serialevent)

-   LANGUAGE [Stream.available()](../../stream/streamavailable)

