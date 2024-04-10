---
title: char
categories: "Variables"
subCategories: "Data Types"
---

**Description**

A data type used to store a character value. Character literals are
written in single quotes, like this: *A* (for multiple characters -
strings - use double quotes: "ABC").

Characters are stored as numbers however. You can see the specific
encoding in the [ASCII
chart](https://www.arduino.cc/en/Reference/ASCIIchart). This means that
it is possible to do arithmetic on characters, in which the ASCII value
of the character is used (e.g. *A* + 1 has the value 66, since the ASCII
value of the capital letter A is 65). See
`link:../../../functions/communication/serial/println[Serial.println]`
reference for more on how characters are translated to numbers.

The size of the `char` datatype is at least 8 bits. It’s recommended to
only use `char` for storing characters. For an unsigned, one-byte (8
bit) data type, use the `link:../byte[byte]` data type.

**Syntax**

`char var = val;`

**Parameters**

`var`: variable name.
`val`: the value to assign to that variable.

**Example Code**

    char myChar = 'A';
    char myChar = 65; // both are equivalent

**See also**

-   LANGUAGE
    [Serial.println](../../../functions/communication/serial/println)

