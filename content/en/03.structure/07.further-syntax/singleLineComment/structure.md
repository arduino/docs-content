---
title: "// (single line comment)"
categories: "Structure"
subCategories: "Further Syntax"
---

**Description**

**Comments** are lines in the program that are used to inform yourself
or others about the way the program works. They are ignored by the
compiler, and not exported to the processor, so they don’t take up any
space in the microcontroller’s flash memory. Comments' only purpose is
to help you understand (or remember), or to inform others about how your
program works.

A **single line comment** begins with `//` (two adjacent slashes). This
comment ends automatically at the end of a line. Whatever follows `//`
till the end of a line will be ignored by the compiler.

**Example Code**

There are two different ways of marking a line as a comment:

    // pin 13 has an LED connected on most Arduino boards.
    // give it a name:
    int led = 13;
    digitalWrite(led, HIGH);  // turn the LED on (HIGH is the voltage level)

**Notes and Warnings**

When experimenting with code, "commenting out" parts of your program is
a convenient way to remove lines that may be buggy. This leaves the
lines in the code, but turns them into comments, so the compiler just
ignores them. This can be especially useful when trying to locate a
problem, or when a program refuses to compile and the compiler error is
cryptic or unhelpful.

**See also**

