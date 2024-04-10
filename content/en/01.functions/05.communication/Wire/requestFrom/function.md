---
title: requestFrom()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

This function is used by the controller device to request bytes from a
peripheral device. The bytes may then be retrieved with the
`available()` and `read()` functions. The `requestFrom()` method accepts
a boolean argument changing its behavior for compatibility with certain
I2C devices. If true, `requestFrom()` sends a stop message after the
request, releasing the I2C bus. If false, `requestFrom()` sends a
restart message after the request. The bus will not be released, which
prevents another master device from requesting between messages. This
allows one master device to send multiple requests while in control. The
default value is true.

**Syntax**

`Wire.requestFrom(address, quantity)`

`Wire.requestFrom(address, quantity, stop)`

**Parameters**

-   *address*: the 7-bit slave address of the device to request bytes
    from.

-   *quantity*: the number of bytes to request.

-   *stop*: true or false. true will send a stop message after the
    request, releasing the bus. False will continually send a restart
    after the request, keeping the connection active.

**Returns**

-   *byte* : the number of bytes returned from the peripheral device.

