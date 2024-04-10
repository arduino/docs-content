---
title: sq()
categories: "Functions"
subCategories: "Math"
---

**Description**

Calculates the square of a number: the number multiplied by itself.

**Syntax**

`sq(x)`

**Parameters**

`x`: the number. Allowed data types: any data type.

**Returns**

The square of the number. Data type: `double`.

**Notes and Warnings**

Because of the way the `sq()` function is implemented, avoid using other
functions inside the brackets, it may lead to incorrect results.

This code will yield incorrect results:

    int inputSquared = sq(Serial.parseInt()); // avoid this

Use this instead:

    int input = Serial.parseInt();  // keep other operations outside the sq function
    int inputSquared = sq(input);

**See also**

-   LANGUAGE [abs()](../abs)

-   LANGUAGE [constrain()](../constrain)

-   LANGUAGE [map()](../map)

-   LANGUAGE [max()](../max)

-   LANGUAGE [min()](../min)

-   LANGUAGE [pow()](../pow)

-   LANGUAGE [sqrt()](../sqrt)

