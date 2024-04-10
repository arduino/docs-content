---
title: onReceive()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

This function registers a function to be called when a peripheral device
receives a transmission from a controller device.

**Syntax**

`Wire.onReceive(handler)`

**Parameters**

-   *handler*: the function to be called when the peripheral device
    receives data; this should take a single int parameter (the number
    of bytes read from the controller device) and return nothing.

**Returns**

None.

