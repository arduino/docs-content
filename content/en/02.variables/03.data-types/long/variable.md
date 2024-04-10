---
title: long
categories: "Variables"
subCategories: "Data Types"
---

**Description**

Long variables are extended size variables for number storage, and store
32 bits (4 bytes), from -2,147,483,648 to 2,147,483,647.

If doing math with integers at least one of the values must be of type
long, either an integer constant followed by an L or a variable of type
long, forcing it to be a long. See the [Integer
Constants](../../constants/integerconstants) page for details.

**Syntax**

`long var = val;`

**Parameters**

`var`: variable name.
`val`: the value assigned to the variable.

**Example Code**

    long speedOfLight_km_s = 300000L;  // see the Integer Constants page for explanation of the 'L'

**See also**

-   LANGUAGE [Integer Constants](../../constants/integerconstants)
