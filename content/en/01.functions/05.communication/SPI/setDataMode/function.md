---
title: SPI.setDataMode()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

This function should not be used in new projects. Use
[SPISettings](../spisettings). with
[SPI.beginTransaction()](../begintransaction). to configure SPI
parameters.

Sets the SPI data mode: that is, clock polarity and phase. See the
Wikipedia article on
[SPI](http://en.wikipedia.org/wiki/Serial_Peripheral_Interface_Bus:) for
details.

**Syntax**

`SPI.setDataMode(mode)`

**Parameters**

mode:

-   SPI\_MODE0

-   SPI\_MODE1

-   SPI\_MODE2

-   SPI\_MODE3

chipSelectPin - peripheral device CS pin (Arduino Due only)

**Returns**

None.

