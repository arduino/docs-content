---
title: end()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

Disable the Wire library, reversing the effect of `Wire.begin()`. To use
the Wire library again after this, call `Wire.begin()` again.

**Note:** This function was not available in the original version of the
Wire library and might still not be available on all platforms. Code
that needs to be portable across platforms and versions can use the
`WIRE_HAS_END` macro, which is only defined when `Wire.end()` is
available.

**Syntax**

`Wire.end()`

**Parameters**

None.

**Returns**

None.

