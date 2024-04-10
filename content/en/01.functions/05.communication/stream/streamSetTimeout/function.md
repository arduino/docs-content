---
title: Stream.setTimeout()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

`setTimeout()` sets the maximum milliseconds to wait for stream data, it
defaults to 1000 milliseconds. This function is part of the Stream
class, and can be called by any class that inherits from it (Wire,
Serial, etc). See the [Stream class](../../stream) main page for more
information.

**Syntax**

`stream.setTimeout(time)`

**Parameters**

`stream`: an instance of a class that inherits from Stream.
`time`: timeout duration in milliseconds. Allowed data types: `long`.

**Returns**

Nothing

**Notes and Warnings**

Stream functions that use the timeout value set via `setTimeout()`:

-   `find()`

-   `findUntil()`

-   `parseInt()`

-   `parseFloat()`

-   `readBytes()`

-   `readBytesUntil()`

-   `readString()`

-   `readStringUntil()`

