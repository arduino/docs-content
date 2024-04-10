---
title: toFloat()
categories: "Variables"
subCategories: "Data Types"
leaf: true
---

**Description**

Converts a valid String to a float. The input String should start with a
digit. If the String contains non-digit characters, the function will
stop performing the conversion. For example, the Strings "123.45",
"123", and "123fish" are converted to 123.45, 123.00, and 123.00
respectively. Note that "123.456" is approximated with 123.46. Note too
that floats have only 6-7 decimal digits of precision and that longer
Strings might be truncated.

**Syntax**

`myString.toFloat()`

**Parameters**

`myString`: a variable of type `String`.

**Returns**

If no valid conversion could be performed because the String doesn’t
start with a digit, a zero is returned. Data type: `float`.

**See also**

-   EXAMPLE [String
    Tutorials^](https://www.arduino.cc/en/Tutorial/BuiltInExamples#strings)

