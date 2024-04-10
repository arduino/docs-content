---
title: interrupts()
categories: "Functions"
subCategories: "Interrupts"
---

**Description**

Re-enables interrupts (after they’ve been disabled by
[noInterrupts()](../nointerrupts). Interrupts allow certain important
tasks to happen in the background and are enabled by default. Some
functions will not work while interrupts are disabled, and incoming
communication may be ignored. Interrupts can slightly disrupt the timing
of code, however, and may be disabled for particularly critical sections
of code.

**Syntax**

`interrupts()`

**Parameters**

None

**Returns**

Nothing

**Example Code**

The code enables Interrupts.

    void setup() {}

    void loop() {
      noInterrupts();
      // critical, time-sensitive code here
      interrupts();
      // other code here
    }

**See also**

-   LANGUAGE
    [attachInterrupts()](../../external-interrupts/attachinterrupt)

-   LANGUAGE
    [detachInterrupts()](../../external-interrupts/detachinterrupt)

