---
title: Floating Point Constants
categories: "Variables"
subCategories: "Constants"
---

= Floating Point Constants

// OVERVIEW SECTION STARTS
[#overview]
--

[float]
=== Description
Similar to integer constants, floating point constants are used to make code more readable. Floating point constants are swapped at compile time for the value to which the expression evaluates.
[%hardbreaks]

--
// OVERVIEW SECTION ENDS

// HOW TO USE SECTION STARTS
[#howtouse]
--

[float]
=== Example Code

## [source,arduino]

## float n = 0.005; // 0.005 is a floating point constant

[%hardbreaks]

[float]
=== Notes and Warnings
Floating point constants can also be expressed in a variety of scientific notation. 'E' and 'e' are both accepted as valid exponent indicators.
[%hardbreaks]

|===
|floating-point constant |evaluates to: |also evaluates to:

|10.0
|10
|

|2.34E5
|2.34 \* 10^5
|234000

|67e-12
|67.0 \* 10^-12
|0.000000000067

|===
[%hardbreaks]

--
// HOW TO USE SECTION ENDS

// SEE ALSO SECTION BEGINS
[#see_also]
--

[float]
=== See also

[role="language"]

--
// SEE ALSO SECTION ENDS
