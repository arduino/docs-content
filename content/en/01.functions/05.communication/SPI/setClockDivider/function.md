---
title: SPI.setClockDivider()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

This function should not be used in new projects. Use
[SPISettings](../spisettings). with
[SPI.beginTransaction()](../begintransaction). to configure SPI
parameters.

Sets the SPI clock divider relative to the system clock. On AVR based
boards, the dividers available are 2, 4, 8, 16, 32, 64 or 128. The
default setting is SPI\_CLOCK\_DIV4, which sets the SPI clock to
one-quarter the frequency of the system clock (4 Mhz for the boards at
16 MHz).

**For Arduino Due:** On the Due, the system clock can be divided by
values from 1 to 255. The default value is 21, which sets the clock to 4
MHz like other Arduino boards.

**Syntax**

`SPI.setClockDivider(divider)`

**Parameters**

divider (only AVR boards):

-   SPI\_CLOCK\_DIV2

-   SPI\_CLOCK\_DIV4

-   SPI\_CLOCK\_DIV8

-   SPI\_CLOCK\_DIV16

-   SPI\_CLOCK\_DIV32

-   SPI\_CLOCK\_DIV64

-   SPI\_CLOCK\_DIV128

**chipSelectPin**: peripheral device CS pin (Arduino Due only)
**divider**: a number from 1 to 255 (Arduino Due only)

**Returns**

None.

