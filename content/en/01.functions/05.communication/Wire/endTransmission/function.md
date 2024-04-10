---
title: endTransmission()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

This function ends a transmission to a peripheral device that was begun
by `beginTransmission()` and transmits the bytes that were queued by
`write()`. The `endTransmission()` method accepts a boolean argument
changing its behavior for compatibility with certain I2C devices. If
true, `endTransmission()` sends a stop message after transmission,
releasing the I2C bus. If false, `endTransmission()` sends a restart
message after transmission. The bus will not be released, which prevents
another controller device from transmitting between messages. This
allows one controller device to send multiple transmissions while in
control. The default value is true.

**Syntax**

`Wire.endTransmission()` `Wire.endTransmission(stop)`

**Parameters**

-   *stop*: true or false. True will send a stop message, releasing the
    bus after transmission. False will send a restart, keeping the
    connection active.

**Returns**

-   *0*: success.

-   *1*: data too long to fit in transmit buffer.

-   *2*: received NACK on transmit of address.

-   *3*: received NACK on transmit of data.

-   *4*: other error.

-   *5*: timeout

