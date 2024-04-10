---
title: float
categories: "Variables"
subCategories: "Data Types"
---

**Description**

Datatype for floating-point numbers, a number that has a decimal point.
Floating-point numbers are often used to approximate analog and
continuous values because they have greater resolution than integers.
Floating-point numbers can be as large as 3.4028235E+38 and as low as
-3.4028235E+38. They are stored as 32 bits (4 bytes) of information.

**Syntax**

`float var = val;`

**Parameters**

`var`: variable name.
`val`: the value you assign to that variable.

**Example Code**

    float myfloat;
    float sensorCalbrate = 1.117;

    int x;
    int y;
    float z;

    x = 1;
    y = x / 2;          // y now contains 0, ints can't hold fractions
    z = (float)x / 2.0; // z now contains .5 (you have to use 2.0, not 2)

**Notes and Warnings**

If doing math with floats, you need to add a decimal point, otherwise it
will be treated as an int. See the [Floating
point](../../constants/floatingpointconstants) constants page for
details.

The float data type has only 6-7 decimal digits of precision. That means
the total number of digits, not the number to the right of the decimal
point. Unlike other platforms, where you can get more precision by using
a double (e.g. up to 15 digits), on the Arduino, double is the same size
as float.

Floating point numbers are not exact, and may yield strange results when
compared. For example 9.0 / 0.3 may not quite equal 30.0. You should
instead check that the absolute value of the difference between the
numbers is less than some small number.

Conversion from floating point to integer math results in truncation:

    float x = 2.9; // A float type variable
    int y = x;  // 2

If, instead, you want to round off during the conversion process, you
need to add `0.5`:

    float x = 2.9;
    int y = x + 0.5;  // 3

or use the `round()` function:

    float x = 2.9;
    int y = round(x);  // 3

Floating point math is also much slower than integer math in performing
calculations, so should be avoided if, for example, a loop has to run at
top speed for a critical timing function. Programmers often go to some
lengths to convert floating point calculations to integer math to
increase speed.

**See also**

