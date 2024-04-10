---
title: map()
categories: "Functions"
subCategories: "Math"
---

**Description**

Re-maps a number from one range to another. That is, a value of
**fromLow** would get mapped to **toLow**, a value of **fromHigh** to
**toHigh**, values in-between to values in-between, etc.

Does not constrain values to within the range, because out-of-range
values are sometimes intended and useful. The `constrain()` function may
be used either before or after this function, if limits to the ranges
are desired.

Note that the "lower bounds" of either range may be larger or smaller
than the "upper bounds" so the `map()` function may be used to reverse a
range of numbers, for example

`y = map(x, 1, 50, 50, 1);`

The function also handles negative numbers well, so that this example

`y = map(x, 1, 50, 50, -100);`

is also valid and works well.

The `map()` function uses integer math so will not generate fractions,
when the math might indicate that it should do so. Fractional remainders
are truncated, and are not rounded or averaged.

**Syntax**

`map(value, fromLow, fromHigh, toLow, toHigh)`

**Parameters**

`value`: the number to map.
`fromLow`: the lower bound of the value’s current range.
`fromHigh`: the upper bound of the value’s current range.
`toLow`: the lower bound of the value’s target range.
`toHigh`: the upper bound of the value’s target range.

**Returns**

The mapped value. Data type: `long`.

**Example Code**

    /* Map an analog value to 8 bits (0 to 255) */
    void setup() {}

    void loop() {
      int val = analogRead(0);
      val = map(val, 0, 1023, 0, 255);
      analogWrite(9, val);
    }

**Appendix**

For the mathematically inclined, here’s the whole function

    long map(long x, long in_min, long in_max, long out_min, long out_max) {
      return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
    }

**Notes & Warnings**

As previously mentioned, the map() function uses integer math. So
fractions might get suppressed due to this. For example, fractions like
3/2, 4/3, 5/4 will all be returned as 1 from the map() function, despite
their different actual values. So if your project requires precise
calculations (e.g. voltage accurate to 3 decimal places), please
consider avoiding map() and implementing the calculations manually in
your code yourself.

**See also**

-   LANGUAGE [abs()](../abs)

-   LANGUAGE [constrain()](../constrain)

-   LANGUAGE [max()](../max)

-   LANGUAGE [min()](../min)

-   LANGUAGE [pow()](../pow)

-   LANGUAGE [sq()](../sq)

-   LANGUAGE [sqrt()](../sqrt)

