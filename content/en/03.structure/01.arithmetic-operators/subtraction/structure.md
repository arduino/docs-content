---
title: "- (subtraction)"
categories: "Structure"
subCategories: "Arithmetic Operators"
---

**Description**

**Subtraction** is one of the four primary arithmetic operations. The
operator `-` (minus) operates on two operands to produce the difference
of the second from the first.

**Syntax**

`difference = operand1 - operand2;`

**Parameters**

`difference`: variable. Allowed data types: `int`, `float`, `double`,
`byte`, `short`, `long`.
`operand1`: variable or constant. Allowed data types: `int`, `float`,
`double`, `byte`, `short`, `long`.
`operand2`: variable or constant. Allowed data types: `int`, `float`,
`double`, `byte`, `short`, `long`.

**Example Code**

    int a = 5;
    int b = 10;
    int c = 0;
    c = a - b;  // the variable 'c' gets a value of -5 after this statement is executed

**Notes and Warnings**

1.  The subtraction operation can overflow if the result is smaller than
    that which can be stored in the data type (e.g. subtracting 1 from
    an integer with the value -32,768 gives 32,767).

2.  If one of the numbers (operands) are of the type float or of type
    double, floating point math will be used for the calculation.

3.  If the operands are of float / double data type and the variable
    that stores the difference is an integer, then only the integral
    part is stored and the fractional part of the number is lost.

<!-- -->

    float a = 5.5;
    float b = 6.6;
    int c = 0;
    c = a - b;  // the variable 'c' stores a value of -1 only as opposed to the expected difference of -1.1

**See also**

