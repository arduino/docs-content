---
title: INPUT | INPUT_PULLUP | OUTPUT
categories: "Variables"
subCategories: "Constants"
---

**Defining Digital Pins modes: INPUT, INPUT\_PULLUP, and OUTPUT**

Digital pins can be used as `INPUT`, `INPUT_PULLUP`, or `OUTPUT`.
Changing a pin with [`pinMode()`](../../../functions/digital-io/pinmode)
changes the electrical behavior of the pin.

**INPUT**

Arduino (ATmega) pins configured as `INPUT` with
[`pinMode()`](../../../functions/digital-io/pinmode) are said to be in a
*high-impedance* state. Pins configured as `INPUT` make extremely small
demands on the circuit that they are sampling, equivalent to a series
resistor of 100 Megohms in front of the pin. This makes them useful for
reading a sensor.

If you have your pin configured as an `INPUT`, and are reading a switch,
when the switch is in the open state the input pin will be "floating",
resulting in unpredictable results. In order to assure a proper reading
when the switch is open, a pull-up or pull-down resistor must be used.
The purpose of this resistor is to pull the pin to a known state when
the switch is open. A 10 K ohm resistor is usually chosen, as it is a
low enough value to reliably prevent a floating input, and at the same
time a high enough value to not draw too much current when the switch is
closed. See the [Digital Read
Serial^](http://arduino.cc/en/Tutorial/DigitalReadSerial) tutorial for
more information.

If a pull-down resistor is used, the input pin will be `LOW` when the
switch is open and `HIGH` when the switch is closed.

If a pull-up resistor is used, the input pin will be `HIGH` when the
switch is open and `LOW` when the switch is closed.

**INPUT\_PULLUP**

The ATmega microcontroller on the Arduino has internal pull-up resistors
(resistors that connect to power internally) that you can access. If you
prefer to use these instead of external pull-up resistors, you can use
the `INPUT_PULLUP` argument in
[`pinMode()`](../../../functions/digital-io/pinmode).

See the [Input Pullup
Serial^](http://arduino.cc/en/Tutorial/InputPullupSerial) tutorial for
an example of this in use.

Pins configured as inputs with either `INPUT` or `INPUT_PULLUP` can be
damaged or destroyed if they are connected to voltages below ground
(negative voltages) or above the positive power rail (5V or 3V).

**OUTPUT**

Pins configured as `OUTPUT` with
[`pinMode()`](../../../functions/digital-io/pinmode) are said to be in a
*low-impedance* state. This means that they can provide a substantial
amount of current to other circuits. ATmega pins can source (provide
current) or sink (absorb current) up to 40 mA (milliamps) of current to
other devices/circuits. This makes them useful for powering LEDs because
LEDs typically use less than 40 mA. Loads greater than 40 mA (e.g.
motors) will require a transistor or other interface circuitry.

Pins configured as outputs can be damaged or destroyed if they are
connected to either the ground or positive power rails.

**See also**

