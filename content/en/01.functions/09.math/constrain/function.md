---
title: constrain()
categories: "Functions"
subCategories: "Math"
---

**Description**

Constrains a number to be within a range.

**Syntax**

`constrain(x, a, b)`

**Parameters**

`x`: the number to constrain Allowed data types: all data types.
`a`: the lower end of the range. Allowed data types: all data types.
`b`: the upper end of the range. Allowed data types: all data types.

**Returns**

x: if x is between a and b.
a: if x is less than a.
b: if x is greater than b.

**Example Code**

The code limits the sensor values to between 10 to 150.

    sensVal = constrain(sensVal, 10, 150);  // limits range of sensor values to between 10 and 150

**Notes and Warnings**

Because of the way the `constrain()` function is implemented, avoid
using other functions inside the brackets, it may lead to incorrect
results.

This code will yield incorrect results:

    int constrainedInput = constrain(Serial.parseInt(), minimumValue, maximumValue);   // avoid this

Use this instead:

    int input = Serial.parseInt();  // keep other operations outside the constrain function
    int constrainedInput = constrain(input, minimumValue, maximumValue);

**See also**

-   LANGUAGE [abs()](../abs)

-   LANGUAGE [map()](../map)

-   LANGUAGE [max()](../max)

-   LANGUAGE [min()](../min)

-   LANGUAGE [pow()](../pow)

-   LANGUAGE [sq()](../sq)

-   LANGUAGE [sqrt()](../sqrt)

