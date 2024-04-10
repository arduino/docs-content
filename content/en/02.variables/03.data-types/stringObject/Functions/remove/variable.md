---
title: remove()
categories: "Variables"
subCategories: "Data Types"
leaf: true
---

**Description**

Modify in place a String removing chars from the provided index to the
end of the String or from the provided index to index plus count.

**Syntax**

`myString.remove(index)`
`myString.remove(index, count)`

**Parameters**

`myString`: a variable of type `String`.
`index`: The position at which to start the remove process (zero
indexed). Allowed data types: `unsigned int`.
`count`: The number of characters to remove. Allowed data types:
`unsigned int`.

**Returns**

Nothing

**Example Code**

    String greeting = "hello";
    greeting.remove(2, 2);  // greeting now contains "heo"

**See also**

-   EXAMPLE [String
    Tutorials^](https://www.arduino.cc/en/Tutorial/BuiltInExamples#strings)
