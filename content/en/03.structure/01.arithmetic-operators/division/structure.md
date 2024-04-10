---
title: / (division)
categories: "Structure"
subCategories: "Arithmetic Operators"
---

**Description**

**Division** is one of the four primary arithmetic operations. The
operator `/` (slash) operates on two operands to produce the result.

**Syntax**

`result = numerator / denominator;`

**Parameters**

`result`: variable. Allowed data types: `int`, `float`, `double`,
`byte`, `short`, `long`.
`numerator`: variable or constant. Allowed data types: `int`, `float`,
`double`, `byte`, `short`, `long`.
`denominator`: **non zero** variable or constant. Allowed data types:
`int`, `float`, `double`, `byte`, `short`, `long`.

**Example Code**

    int a = 50;
    int b = 10;
    int c = 0;
    c = a / b;  // the variable 'c' gets a value of 5 after this statement is executed

**Notes and Warnings**

1.  If one of the numbers (operands) are of the type float or of type
    double, floating point math will be used for the calculation.

2.  If the operands are of float / double data type and the variable
    that stores the result is an integer, then only the integral part is
    stored and the fractional part of the number is lost.

<!-- -->

    float a = 55.5;
    float b = 6.6;
    int c = 0;
    c = a / b;  // the variable 'c' stores a value of 8 only as opposed to the expected result of 8.409

**See also**

