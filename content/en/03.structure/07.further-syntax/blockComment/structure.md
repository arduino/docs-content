---
title: "/* */"
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

The beginning of a **block comment** or a **multi-line comment** is
marked by the symbol `/\*` and the symbol `*/` marks its end. This type
of comment is called so as this can extend over more than one line; once
the compiler reads the `/\*` it ignores whatever follows until it
encounters a `*/`.

**Example Code**

    /* This is a valid comment */

    /*
      Blink
      Turns on an LED on for one second, then off for one second, repeatedly.

      This example code is in the public domain.
      (Another valid comment)
    */

    /*
      if (gwb == 0) { // single line comment is OK inside a multi-line comment
        x = 3;          /* but not another multi-line comment - this is invalid */
      }
    // don't forget the "closing" comment - they have to be balanced!
    */

**Notes and Warnings**

When experimenting with code, "commenting out" parts of your program is
a convenient way to remove lines that may be buggy. This leaves the
lines in the code, but turns them into comments, so the compiler just
ignores them. This can be especially useful when trying to locate a
problem, or when a program refuses to compile and the compiler error is
cryptic or unhelpful.

**See also**

