---
title: Stream.readBytes()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

`readBytes()` read characters from a stream into a buffer. The function
terminates if the determined length has been read, or it times out (see
[setTimeout()](../streamsettimeout)).

`readBytes()` returns the number of bytes placed in the buffer. A 0
means no valid data was found.

This function is part of the Stream class, and can be called by any
class that inherits from it (Wire, Serial, etc). See the [Stream
class](../../stream) main page for more information.

**Syntax**

`stream.readBytes(buffer, length)`

**Parameters**

`stream`: an instance of a class that inherits from Stream.
`buffer`: the buffer to store the bytes in. Allowed data types: array of
`char` or `byte`.
`length`: the number of bytes to read. Allowed data types: `int`.

**Returns**

The number of bytes placed in the buffer. Data type: `size_t`.
