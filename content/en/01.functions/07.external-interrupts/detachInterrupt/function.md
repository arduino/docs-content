---
title: detachInterrupt()
categories: "Functions"
subCategories: "External Interrupts"
---

**Description**

Turns off the given interrupt.

**Syntax**

-   `detachInterrupt(digitalPinToInterrupt(pin))` (recommended)

-   `detachInterrupt(interrupt)` (not recommended)

-   `detachInterrupt(pin)` (Not recommended. Additionally, this only
    works on a specific set of boards.)

**Parameters**

`interrupt`: the number of the interrupt to disable (see
[attachInterrupt()](../attachinterrupt) for more details).
`pin`: the Arduino pin number of the interrupt to disable

**Returns**

Nothing

**See also**

