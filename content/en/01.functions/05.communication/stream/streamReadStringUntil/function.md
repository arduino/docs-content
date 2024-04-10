---
title: Stream.readStringUntil()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

`readStringUntil()` reads characters from a stream into a String. The
function terminates if the terminator character is detected or it times
out (see [setTimeout()](../streamsettimeout)).

This function is part of the Stream class, and can be called by any
class that inherits from it (Wire, Serial, etc). See the [Stream
class](../../stream) main page for more information.

**Syntax**

`stream.readStringUntil(terminator)`

**Parameters**

`stream`: an instance of a class that inherits from Stream.
`terminator`: the character to search for. Allowed data types: `char`.

**Returns**

The entire String read from a stream, up to the terminator character. If
the terminator character can’t be found, or if there is no data before
the terminator character, it will return `NULL`.

**Notes and Warnings**

The terminator character is discarded from the stream. If the terminator
character can’t be found, all read characters will be discarded.

