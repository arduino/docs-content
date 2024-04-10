---
title: "> (greater than)"
categories: "Structure"
subCategories: "Comparison Operators"
---

**Description**

Compares the variable on the left with the value or variable on the
right of the operator. Returns true when the operand on the left is
greater (bigger) than the operand on the right. Please note that you may
compare variables of different data types, but that could generate
unpredictable results, it is therefore recommended to compare variables
of the same data type including the signed/unsigned type.

**Syntax**

`x > y; // is true if x is bigger than y and it is false if x is equal or smaller than y`

**Parameters**

`x`: variable. Allowed data types: `int`, `float`, `double`, `byte`,
`short`, `long`.
`y`: variable or constant. Allowed data types: `int`, `float`, `double`,
`byte`, `short`, `long`.

**Example Code**

    if (x > y) {  // tests if x is greater (bigger) than y
      // do something only if the comparison result is true
    }

**Notes and Warnings**

Positive numbers are greater than negative numbers.

**See also**
