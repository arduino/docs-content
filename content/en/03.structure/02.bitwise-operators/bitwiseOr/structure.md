---
title: "| (bitwise or)"
categories: "Structure"
subCategories: "Bitwise Operators"
---

**Description**

The bitwise OR operator in C++ is the vertical bar symbol, |. Like the &
operator, | operates independently each bit in its two surrounding
integer expressions, but what it does is different (of course). The
bitwise OR of two bits is 1 if either or both of the input bits is 1,
otherwise it is 0.

In other words:

    0  0  1  1    operand1
    0  1  0  1    operand2
    ----------
    0  1  1  1    (operand1 | operand2) - returned result

**Example Code**

    int a =  92;    // in binary: 0000000001011100
    int b = 101;    // in binary: 0000000001100101
    int c = a | b;  // result:    0000000001111101, or 125 in decimal.

One of the most common uses of the Bitwise OR is to set multiple bits in
a bit-packed number.

    // Note: This code is AVR architecture specific
    // set direction bits for pins 2 to 7, leave PD0 and PD1 untouched (xx | 00 == xx)
    // same as pinMode(pin, OUTPUT) for pins 2 to 7 on Uno or Nano
    DDRD = DDRD | 0b11111100;

**See also**

-   LANGUAGE [|| Logical OR](../../boolean-operators/logicalor)

-   EXAMPLE [BitMath
    Tutorial^](https://www.arduino.cc/playground/Code/BitMath)

