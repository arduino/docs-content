---
title: Stream.readString()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

`readString()` reads characters from a stream into a String. The
function terminates if it times out (see
[setTimeout()](../streamsettimeout)).

This function is part of the Stream class, and can be called by any
class that inherits from it (Wire, Serial, etc). See the [Stream
class](../../stream) main page for more information.

**Syntax**

`stream.readString()`

**Parameters**

`stream`: an instance of a class that inherits from Stream.

**Returns**

A String read from a stream.
