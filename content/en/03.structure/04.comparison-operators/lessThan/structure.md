---
title: "< (less than)"
categories: "Structure"
subCategories: "Comparison Operators"
---

**Description**

Compares the variable on the left with the value or variable on the
right of the operator. Returns true when the operand on the left is less
(smaller) than the operand on the right. Please note that you may
compare variables of different data types, but that could generate
unpredictable results, it is therefore recommended to compare variables
of the same data type including the signed/unsigned type.

**Syntax**

`x < y; // is true if x is smaller than y and it is false if x is equal or bigger than y`

**Parameters**

`x`: variable. Allowed data types: `int`, `float`, `double`, `byte`,
`short`, `long`.
`y`: variable or constant. Allowed data types: `int`, `float`, `double`,
`byte`, `short`, `long`.

**Example Code**

    if (x < y) {  // tests if x is less (smaller) than y
      // do something only if the comparison result is true
    }

**Notes and Warnings**

Negative numbers are less than positive numbers.

**See also**

