---
title: HIGH | LOW
categories: "Variables"
subCategories: "Constants"
---

**Defining Pin Levels: HIGH and LOW**

When reading or writing to a digital pin there are only two possible
values a pin can take/be-set-to: `HIGH` and `LOW`. These are the same as
`true` and `false`, as well as `1` and `0`.

**HIGH**

The meaning of `HIGH` (in reference to a pin) is somewhat different
depending on whether a pin is set to an `INPUT` or `OUTPUT`. When a pin
is configured as an `INPUT` with
`link:../../../functions/digital-io/pinmode[pinMode()]`, and read with
`link:../../../functions/digital-io/digitalread[digitalRead()]`, the
Arduino (ATmega) will report `HIGH` if:

-   a voltage greater than 3.0V is present at the pin (5V boards)

-   a voltage greater than 2.0V is present at the pin (3.3V boards)

A pin may also be configured as an INPUT with
[`pinMode()`](../../../functions/digital-io/pinmode), and subsequently
made HIGH with
`link:../../../functions/digital-io/digitalwrite[digitalWrite()]`. This
will enable the internal 20K pullup resistors, which will *pull up* the
input pin to a `HIGH` reading unless it is pulled `LOW` by external
circuitry. This can be done alternatively by passing `INPUT_PULLUP` as
argument to the [`pinMode()`](../../../functions/digital-io/pinmode)
function, as explained in more detail in the section "Defining Digital
Pins modes: INPUT, INPUT\_PULLUP, and OUTPUT" further below.

When a pin is configured to OUTPUT with
[`pinMode()`](../../../functions/digital-io/pinmode), and set to `HIGH`
with [`digitalWrite()`](../../../functions/digital-io/digitalwrite), the
pin is at:

-   5 volts (5V boards)

-   3.3 volts (3.3V boards)

In this state it can source current, e.g. light an LED that is connected
through a series resistor to ground.

**LOW**

The meaning of LOW also has a different meaning depending on whether a
pin is set to INPUT or OUTPUT. When a pin is configured as an INPUT with
pinMode(), and read with digitalRead(), the Arduino (ATmega) will report
LOW if:

a voltage less than 1.5V is present at the pin (5V boards)

a voltage less than 1.0V (Approx) is present at the pin (3.3V boards)

When a pin is configured to OUTPUT with pinMode(), and set to LOW with
digitalWrite(), the pin is at 0 volts (both 5V and 3.3V boards). In this
state it can sink current, e.g. light an LED that is connected through a
series resistor to +5 volts (or +3.3 volts).

**See also**

