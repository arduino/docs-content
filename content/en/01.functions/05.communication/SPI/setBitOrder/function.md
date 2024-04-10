---
title: SPI.setBitOrder()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

This function should not be used in new projects. Use
[SPISettings](../spisettings). with
[SPI.beginTransaction()](../begintransaction). to configure SPI
parameters.

Sets the order of the bits shifted out of and into the SPI bus, either
LSBFIRST (least-significant bit first) or MSBFIRST (most-significant bit
first).

**Syntax**

`SPI.setBitOrder(order)`

**Parameters**

order: either LSBFIRST or MSBFIRST

**Returns**

None.
