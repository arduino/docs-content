---
title: SPI.usingInterrupt()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

If your program will perform SPI transactions within an interrupt, call
this function to register the interrupt number or name with the SPI
library. This allows `SPI.beginTransaction()` to prevent usage
conflicts. Note that the interrupt specified in the call to
usingInterrupt() will be disabled on a call to `beginTransaction()` and
re-enabled in `endTransaction().`

**Syntax**

`SPI.usingInterrupt(interruptNumber)`

**Parameters**

interruptNumber: the associated interrupt number.

**Returns**

None.

