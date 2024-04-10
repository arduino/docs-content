---
title: do...while
categories: "Structure"
subCategories: "Control Structure"
---

**Description**

The `do...while` loop works in the same manner as the
`link:../while[while]` loop, with the exception that the condition is
tested at the end of the loop, so the do loop will always run at least
once.

**Syntax**

    do {
      // statement block
    } while (condition);

**Parameters**

`condition`: a boolean expression that evaluates to
`link:../../../variables/constants/truefalse[true]` or
`link:../../../variables/constants/truefalse[false]`.

**Example Code**

    // initialize x and i with a value of 0
    int x = 0;
    int i = 0;

    do {
      delay(50);          // wait for sensors to stabilize
      x = readSensors();  // check the sensors
      i++;                // increase i by 1
    } while (i < 100);    // repeat 100 times

**See also**
