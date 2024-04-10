---
title: + (addition)
categories: "Structure"
subCategories: "Arithmetic Operators"
---

**Description**

**Addition** is one of the four primary arithmetic operations. The
operator `+` (plus) operates on two operands to produce the sum.

**Syntax**

`sum = operand1 + operand2;`

**Parameters**

`sum`: variable. Allowed data types: `int`, `float`, `double`, `byte`,
`short`, `long`.
`operand1`: variable or constant. Allowed data types: `int`, `float`,
`double`, `byte`, `short`, `long`.
`operand2`: variable or constant. Allowed data types: `int`, `float`,
`double`, `byte`, `short`, `long`.

**Example Code**

    int a = 5;
    int b = 10;
    int c = 0;
    c = a + b;  // the variable 'c' gets a value of 15 after this statement is executed

**Notes and Warnings**

1.  The addition operation can overflow if the result is larger than
    that which can be stored in the data type (e.g. adding 1 to an
    integer with the value 32,767 gives -32,768).

2.  If one of the numbers (operands) are of the type float or of type
    double, floating point math will be used for the calculation.

3.  If the operands are of float / double data type and the variable
    that stores the sum is an integer, then only the integral part is
    stored and the fractional part of the number is lost.

<!-- -->

    float a = 5.5;
    float b = 6.6;
    int c = 0;
    c = a + b;  // the variable 'c' stores a value of 12 only as opposed to the expected sum of 12.1

**See also**

