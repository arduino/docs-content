---
title: c_str()
categories: "Variables"
subCategories: "Data Types"
leaf: true
---

**Description**

Converts the contents of a String as a C-style, null-terminated string.
Note that this gives direct access to the internal String buffer and
should be used with care. In particular, you should never modify the
string through the pointer returned. When you modify the String object,
or when it is destroyed, any pointer previously returned by c\_str()
becomes invalid and should not be used any longer.

**Syntax**

`myString.c_str()`

**Parameters**

`myString`: a variable of type `String`.

**Returns**

A pointer to the C-style version of the invoking String.

**See also**

-   EXAMPLE [String
    Tutorials^](https://www.arduino.cc/en/Tutorial/BuiltInExamples#strings)
