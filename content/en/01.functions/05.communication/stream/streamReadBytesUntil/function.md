---
title: Stream.readBytesUntil()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

`readBytesUntil()` reads characters from a stream into a buffer. The
function terminates if the terminator character is detected, the
determined length has been read, or it times out (see
[setTimeout()](../streamsettimeout)). The function returns the
characters up to the last character before the supplied terminator. The
terminator itself is not returned in the buffer.

`readBytesUntil()` returns the number of bytes placed in the buffer. A 0
means the terminator character can’t be found or there is no data before
it.

This function is part of the Stream class, and can be called by any
class that inherits from it (Wire, Serial, etc). See the [Stream
class](../../stream) main page for more information.

**Syntax**

`stream.readBytesUntil(character, buffer, length)`

**Parameters**

`stream`: an instance of a class that inherits from Stream.
`character`: the character to search for. Allowed data types: `char`.
`buffer`: the buffer to store the bytes in. Allowed data types: array of
`char` or `byte`.
`length`: the number of bytes to read. Allowed data types: `int`.

**Returns**

The number of bytes (excluding the terminator character) placed in the
buffer if the terminator character has been found.

**Notes and Warnings**

The terminator character is discarded from the stream.

