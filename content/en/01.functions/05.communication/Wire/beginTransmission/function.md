---
title: beginTransmission()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

This function begins a transmission to the I2C peripheral device with
the given address. Subsequently, queue bytes for transmission with the
`write()` function and transmit them by calling `endTransmission()`.

**Syntax**

`Wire.beginTransmission(address)`

**Parameters**

-   *address*: the 7-bit address of the device to transmit to.

**Returns**

None.
