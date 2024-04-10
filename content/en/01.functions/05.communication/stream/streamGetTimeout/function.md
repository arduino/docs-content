---
title: Stream.getTimeout()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

`getTimeout()` returns the timeout value set by `setTimeout()`. This
function is part of the Stream class, and can be called by any class
that inherits from it (Wire, Serial, etc). See the [Stream
class](../../stream) main page for more information.

**Syntax**

`stream.getTimeout()`

**Parameters**

None

**Returns**

The timeout value set by `stream.setTimeout()`. Data type:
`unsigned long`.
