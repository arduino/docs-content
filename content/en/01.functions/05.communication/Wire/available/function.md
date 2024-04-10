---
title: available()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

This function returns the number of bytes available for retrieval with
`read()`. This function should be called on a controller device after a
call to `requestFrom()` or on a peripheral inside the `onReceive()`
handler. `available()` inherits from the Stream utility class.

**Syntax**

`Wire.available()`

**Parameters**

None.

**Returns**

The number of bytes available for reading.
