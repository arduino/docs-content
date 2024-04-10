---
title: "% (remainder)"
categories: "Structure"
subCategories: "Arithmetic Operators"
---

**Description**

**Remainder** operation calculates the remainder when one integer is
divided by another. It is useful for keeping a variable within a
particular range (e.g. the size of an array). The `%` (percent) symbol
is used to carry out remainder operation.

**Syntax**

`remainder = dividend % divisor;`

**Parameters**

`remainder`: variable. Allowed data types: `int`, `float`, `double`.
`dividend`: variable or constant. Allowed data types: `int`.
`divisor`: **non zero** variable or constant. Allowed data types: `int`.

**Example Code**

    int x = 0;
    x = 7 % 5;  // x now contains 2
    x = 9 % 5;  // x now contains 4
    x = 5 % 5;  // x now contains 0
    x = 4 % 5;  // x now contains 4
    x = -4 % 5; // x now contains -4
    x = 4 % -5; // x now contains 4

    /* update one value in an array each time through a loop */

    int values[10];
    int i = 0;

    void setup() {}

    void loop() {
      values[i] = analogRead(0);
      i = (i + 1) % 10; // remainder operator rolls over variable
    }

**Notes and Warnings**

1.  The remainder operator does not work on floats.

2.  If the **first** operand is negative, the result is negative (or
    zero). Therefore, the result of `x % 10` will not always be between
    0 and 9 if `x` can be negative.

**See also**

