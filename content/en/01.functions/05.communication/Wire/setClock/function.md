---
title: setClock()
categories: "Functions"
subCategories: "Communication"
leaf: true
---

**Description**

This function modifies the clock frequency for I2C communication. I2C
peripheral devices have no minimum working clock frequency, however
100KHz is usually the baseline.

**Syntax**

`Wire.setClock(clockFrequency)`

**Parameters**

-   *clockFrequency*: the value (in Hertz) of the desired communication
    clock. Accepted values are 100000 (standard mode) and 400000 (fast
    mode). Some processors also support 10000 (low speed mode), 1000000
    (fast mode plus) and 3400000 (high speed mode). Please refer to the
    specific processor documentation to make sure the desired mode is
    supported.

**Returns**

None.

