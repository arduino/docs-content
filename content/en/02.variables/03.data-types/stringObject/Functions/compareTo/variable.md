---
title: compareTo()
categories: "Variables"
subCategories: "Data Types"
leaf: true
---

**Description**

Compares two Strings, testing whether one comes before or after the
other, or whether they’re equal. The strings are compared character by
character, using the ASCII values of the characters. That means, for
example, that *a* comes before *b* but after *A*. Numbers come before
letters.

**Syntax**

`myString.compareTo(myString2)`

**Parameters**

`myString`: a variable of type `String`.
`myString2`: another variable of type `String`.

**Returns**

`a negative number`: if myString comes before myString2.
`0`: if String equals myString2.
`a positive number`: if myString comes after myString2.

**See also**

-   EXAMPLE [String
    Tutorials^](https://www.arduino.cc/en/Tutorial/BuiltInExamples#strings)
