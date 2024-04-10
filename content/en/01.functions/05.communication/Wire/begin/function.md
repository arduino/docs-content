---
title: begin()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

This function initializes the Wire library and join the I2C bus as a
controller or a peripheral. This function should normally be called only
once.

**Syntax**

`Wire.begin()`

`Wire.begin(address)`

**Parameters**

-   *address*: the 7-bit slave address (optional); if not specified,
    join the bus as a controller device.

**Returns**

None.
