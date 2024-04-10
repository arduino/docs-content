---
title: lastIndexOf()
categories: "Variables"
subCategories: "Data Types"
leaf: true
---

**Description**

Locates a character or String within another String. By default,
searches from the end of the String, but can also work backwards from a
given index, allowing for the locating of all instances of the character
or String.

**Syntax**

`myString.lastIndexOf(val)`
`myString.lastIndexOf(val, from)`

**Parameters**

`myString`: a variable of type `String`.
`val`: the value to search for. Allowed data types: `char`, `String`.
`from`: the index to work backwards from.

**Returns**

The index of val within the String, or -1 if not found.

**See also**

-   EXAMPLE [String
    Tutorials^](https://www.arduino.cc/en/Tutorial/BuiltInExamples#strings)
