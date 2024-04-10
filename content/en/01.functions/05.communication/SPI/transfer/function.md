---
title: SPI.transfer()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

SPI transfer is based on a simultaneous send and receive: the received
data is returned in receivedVal (or receivedVal16). In case of buffer
transfers the received data is stored in the buffer in-place (the old
data is replaced with the data received).

**Syntax**

`receivedVal = SPI.transfer(val)`

`receivedVal16 = SPI.transfer16(val16)`

`SPI.transfer(buffer, size)`

**Parameters**

-   val: the byte to send out over the bus

-   val16: the two bytes variable to send out over the bus

-   buffer: the array of data to be transferred

**Returns**

The received data.

