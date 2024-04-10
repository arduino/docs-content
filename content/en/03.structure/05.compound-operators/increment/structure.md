---
title: "++ (increment)"
categories: "Structure"
subCategories: "Compound Operators"
---

**Description**

Increments the value of a variable by 1.

**Syntax**

`x{plus}{plus}; // increment x by one and returns the old value of x`
`{plus}{plus}x; // increment x by one and returns the new value of x`

**Parameters**

`x`: variable. Allowed data types: `int`, `long` (possibly unsigned).

**Returns**

The original or newly incremented value of the variable.

**Example Code**

    x = 2;
    y = ++x;  // x now contains 3, y contains 3
    y = x++;  // x contains 4, but y still contains 3

**See also**
