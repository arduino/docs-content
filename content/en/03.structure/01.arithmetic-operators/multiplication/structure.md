---
title: "* (multiplication)"
categories: "Structure"
subCategories: "Arithmetic Operators"
---

**Description**

**Multiplication** is one of the four primary arithmetic operations. The
operator `*` (asterisk) operates on two operands to produce the product.

**Syntax**

`product = operand1 * operand2;`

**Parameters**

`product`: variable. Allowed data types: `int`, `float`, `double`,
`byte`, `short`, `long`.
`operand1`: variable or constant. Allowed data types: `int`, `float`,
`double`, `byte`, `short`, `long`.
`operand2`: variable or constant. Allowed data types: `int`, `float`,
`double`, `byte`, `short`, `long`.

**Example Code**

    int a = 5;
    int b = 10;
    int c = 0;
    c = a * b;  // the variable 'c' gets a value of 50 after this statement is executed

**Notes and Warnings**

1.  The multiplication operation can overflow if the result is bigger
    than that which can be stored in the data type.

2.  If one of the numbers (operands) are of the type float or of type
    double, floating point math will be used for the calculation.

3.  If the operands are of float / double data type and the variable
    that stores the product is an integer, then only the integral part
    is stored and the fractional part of the number is lost.

<!-- -->

    float a = 5.5;
    float b = 6.6;
    int c = 0;
    c = a * b;  // the variable 'c' stores a value of 36 only as opposed to the expected product of 36.3

**See also**

