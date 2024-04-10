---
title: "-- (decrement)"
categories: "Structure"
subCategories: "Compound Operators"
---

**Description**

Decrements the value of a variable by 1.

**Syntax**

`x--; // decrement x by one and returns the old value of x`
`--x; // decrement x by one and returns the new value of x`

**Parameters**

`x`: variable. Allowed data types: `int`, `long` (possibly unsigned).

**Returns**

The original or newly decremented value of the variable.

**Example Code**

    x = 2;
    y = --x;  // x now contains 1, y contains 1
    y = x--;  // x contains 0, but y still contains 1

**See also**

