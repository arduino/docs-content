---
title: Stream.findUntil()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

`findUntil()` reads data from the stream until the target string of
given length or terminator string is found, or it times out (see
[Stream.setTimeout()](../streamsettimeout)).

The function returns `true` if target string is found, `false` if timed
out.

This function is part of the Stream class, and can be called by any
class that inherits from it (Wire, Serial, etc). See the [Stream
class](../../stream) main page for more information.

**Syntax**

`stream.findUntil(target, terminal)`

**Parameters**

`stream`: an instance of a class that inherits from Stream.
`target`: the string to search for. Allowed data types: `char`.
`terminal`: the terminal string in the search. Allowed data types:
`char`.

**Returns**

Data type: `bool`.
