---
title: Stream
categories: "Functions"
subCategories: "Communication"
---

**Description**

Stream is the base class for character and binary based streams. It is
not called directly, but invoked whenever you use a function that relies
on it.

Stream defines the reading functions in Arduino. When using any core
functionality that uses a `read()` or similar method, you can safely
assume it calls on the Stream class. For functions like `print()`,
Stream inherits from the Print class.

Some of the libraries that rely on Stream include :

-   [Serial](../serial)

-   [Wire](https://www.arduino.cc/en/Reference/Wire)

-   [Ethernet](https://www.arduino.cc/en/Reference/Ethernet)

-   [SD](https://www.arduino.cc/en/Reference/SD)

**Functions**

[available()](../stream/streamavailable)
[read()](../stream/streamread)
[flush()](../stream/streamflush)
[find()](../stream/streamfind)
[findUntil()](../stream/streamfinduntil)
[peek()](../stream/streampeek)
[readBytes()](../stream/streamreadbytes)
[readBytesUntil()](../stream/streamreadbytesuntil)
[readString()](../stream/streamreadstring)
[readStringUntil()](../stream/streamreadstringuntil)
[parseInt()](../stream/streamparseint)
[parseFloat()](../stream/streamparsefloat)
[setTimeout()](../stream/streamsettimeout)

**See also**

