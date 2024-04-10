---
title: Stream.find()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

`find()` reads data from the stream until the target is found. The
function returns true if target is found, false if timed out (see
[Stream.setTimeout()](../streamsettimeout)).

This function is part of the Stream class, and can be called by any
class that inherits from it (Wire, Serial, etc). See the [stream
class](../../stream) main page for more information.

**Syntax**

`stream.find(target)`
`stream.find(target, length)`

**Parameters**

`stream`: an instance of a class that inherits from Stream.
`target`: the string to search for. Allowed data types: `char`.
`length`: length of the target. Allowed data types: `size_t`.

**Returns**

Data type: `bool`.
