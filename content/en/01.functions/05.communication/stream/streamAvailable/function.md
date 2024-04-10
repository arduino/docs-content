---
title: Stream.available()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

`available()` gets the number of bytes available in the stream. This is
only for bytes that have already arrived.

This function is part of the Stream class, and can be called by any
class that inherits from it (Wire, Serial, etc). See the [Stream
class](../../stream) main page for more information.

**Syntax**

`stream.available()`

**Parameters**

`stream`: an instance of a class that inherits from Stream.

**Returns**

The number of bytes available to read. Data type: `int`.

