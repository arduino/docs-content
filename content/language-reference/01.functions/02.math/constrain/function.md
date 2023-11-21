---
title: constrain()
categories: "Functions"
subCategories: "Math"
---

= constrain(x, a, b)

// OVERVIEW SECTION STARTS
[#overview]
--

[float]
=== Description
Constrains a number to be within a range.
[%hardbreaks]

[float]
=== Syntax
`constrain(x, a, b)`

[float]
=== Parameters
`x`: the number to constrain Allowed data types: all data types. +
`a`: the lower end of the range. Allowed data types: all data types. +
`b`: the upper end of the range. Allowed data types: all data types.

[float]
=== Returns
x: if x is between a and b. +
a: if x is less than a. +
b: if x is greater than b.

--
// OVERVIEW SECTION ENDS

// HOW TO USE SECTION STARTS
[#howtouse]
--

[float]
=== Example Code
// Describe what the example code is all about and add relevant code ►►►►► THIS SECTION IS MANDATORY ◄◄◄◄◄
The code limits the sensor values to between 10 to 150.

## [source,arduino]

## sensVal = constrain(sensVal, 10, 150); // limits range of sensor values to between 10 and 150

[float]
=== Notes and Warnings
Because of the way the `constrain()` function is implemented, avoid using other functions inside the brackets, it may lead to incorrect results.

This code will yield incorrect results:
[source,arduino]

---

## int constrainedInput = constrain(Serial.parseInt(), minimumValue, maximumValue); // avoid this

Use this instead:
[source,arduino]

---

int input = Serial.parseInt(); // keep other operations outside the constrain function
int constrainedInput = constrain(input, minimumValue, maximumValue);

---

[%hardbreaks]

--
// HOW TO USE SECTION ENDS

// SEE ALSO SECTION
[#see_also]
--

[float]
=== See also

[role="language"]

- #LANGUAGE# link:../abs[abs()]
- #LANGUAGE# link:../map[map()]
- #LANGUAGE# link:../max[max()]
- #LANGUAGE# link:../min[min()]
- #LANGUAGE# link:../pow[pow()]
- #LANGUAGE# link:../sq[sq()]
- #LANGUAGE# link:../sqrt[sqrt()]

--
// SEE ALSO SECTION ENDS
