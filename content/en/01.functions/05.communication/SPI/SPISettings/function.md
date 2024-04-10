---
title: SPISettings
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

The `SPISettings` object is used to configure the SPI port for your SPI
device. All 3 parameters are combined to a single `SPISettings` object,
which is given to `SPI.beginTransaction()`.

When all of your settings are constants, SPISettings should be used
directly in `SPI.beginTransaction()`. See the syntax section below. For
constants, this syntax results in smaller and faster code.

If any of your settings are variables, you may create a SPISettings
object to hold the 3 settings. Then you can give the object name to
SPI.beginTransaction(). Creating a named SPISettings object may be more
efficient when your settings are not constants, especially if the
maximum speed is a variable computed or configured, rather than a number
you type directly into your sketch.

**Syntax**

`SPI.beginTransaction(SPISettings(14000000, MSBFIRST, SPI_MODE0))` Note:
Best if all 3 settings are constants

‘SPISettings mySetting(speedMaximum, dataOrder, dataMode)\` Note: Best
when any setting is a variable’'

**Parameters**

`speedMaximum`: The maximum speed of communication. For a SPI chip rated
up to 20 MHz, use 20000000.
`dataOrder`: MSBFIRST or LSBFIRST
`dataMode`: SPI\_MODE0, SPI\_MODE1, SPI\_MODE2, or SPI\_MODE3

**Returns**

None.

