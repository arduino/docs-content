---
title: noInterrupts()
categories: "Functions"
subCategories: "Interrupts"
---

**Description**

Disables interrupts (you can re-enable them with
[`interrupts()`](../interrupts)). Interrupts allow certain important
tasks to happen in the background and are enabled by default. Some
functions will not work while interrupts are disabled, and incoming
communication may be ignored. Interrupts can slightly disrupt the timing
of code, however, and may be disabled for particularly critical sections
of code.

**Syntax**

`noInterrupts()`

**Parameters**

None

**Returns**

Nothing

**Example Code**

The code shows how to enable interrupts.

    void setup() {}

    void loop() {
      noInterrupts();
      // critical, time-sensitive code here
      interrupts();
      // other code here
    }

**Notes and Warnings**

Note that disabling interrupts on the Arduino boards with native USB
capabilities (e.g.,
[Leonardo^](https://docs.arduino.cc/hardware/leonardo)) will make the
board not appear in the Port menu, since this disables its USB
capability.

**See also**

