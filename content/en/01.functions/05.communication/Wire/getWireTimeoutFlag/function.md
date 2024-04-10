---
title: getWireTimeoutFlag()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

Checks whether a timeout has occured since the last time the flag was
cleared.

This flag is set is set whenever a timeout occurs and cleared when
`Wire.clearWireTimeoutFlag()` is called, or when the timeout is changed
using `Wire.setWireTimeout()`.

**Syntax**

`Wire.getWireTimeoutFlag()`

**Parameters**

None.

**Returns**

-   bool: The current value of the flag

**Portability Notes**

This function was not available in the original version of the Wire
library and might still not be available on all platforms. Code that
needs to be portable across platforms and versions can use the
`WIRE_HAS_TIMEOUT` macro, which is only defined when
`Wire.setWireTimeout()`, `Wire.getWireTimeoutFlag()` and
`Wire.clearWireTimeout()` are all available.

