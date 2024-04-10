---
title: Floating Point Constants
categories: "Variables"
subCategories: "Constants"
---

**Description**

Similar to integer constants, floating point constants are used to make
code more readable. Floating point constants are swapped at compile time
for the value to which the expression evaluates.

**Example Code**

    float n = 0.005;  // 0.005 is a floating point constant

**Notes and Warnings**

Floating point constants can also be expressed in a variety of
scientific notation. *E* and *e* are both accepted as valid exponent
indicators.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td style="text-align: left;"><p>floating-point constant</p></td>
<td style="text-align: left;"><p>evaluates to:</p></td>
<td style="text-align: left;"><p>also evaluates to:</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>10.0</p></td>
<td style="text-align: left;"><p>10</p></td>
<td style="text-align: left;"></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>2.34E5</p></td>
<td style="text-align: left;"><p>2.34 * 10^5</p></td>
<td style="text-align: left;"><p>234000</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>67e-12</p></td>
<td style="text-align: left;"><p>67.0 * 10^-12</p></td>
<td style="text-align: left;"><p>0.000000000067</p></td>
</tr>
</tbody>
</table>

**See also**

