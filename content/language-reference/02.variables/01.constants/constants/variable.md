---
title: constants
categories: "Variables"
subCategories: "Constants"
---

= Constants

// OVERVIEW SECTION STARTS
[#overview]
--

[float]
== Description
Constants are predefined expressions in the Arduino language. They are used to make the programs easier to read. We classify constants in groups:

[float]
== Defining Logical Levels: true and false (Boolean Constants)
There are two constants used to represent truth and falsity in the Arduino language: `true`, and `false`.

[float]
=== false
`false` is the easier of the two to define. false is defined as 0 (zero).
[%hardbreaks]

[float]
=== true
`true` is often said to be defined as 1, which is correct, but true has a wider definition. Any integer which is non-zero is true, in a Boolean sense. So -1, 2 and -200 are all defined as true, too, in a Boolean sense.
[%hardbreaks]

Note that the `true` and `false` constants are typed in lowercase unlike `HIGH`, `LOW`, `INPUT`, and `OUTPUT`.
[%hardbreaks]

[float]
== Defining Pin Levels: HIGH and LOW
When reading or writing to a digital pin there are only two possible values a pin can take/be-set-to: `HIGH` and `LOW`.

[float]
=== HIGH
The meaning of `HIGH` (in reference to a pin) is somewhat different depending on whether a pin is set to an `INPUT` or `OUTPUT`. When a pin is configured as an `INPUT` with `link:../../../functions/digital-io/pinmode[pinMode()]`, and read with `link:../../../functions/digital-io/digitalread[digitalRead()]`, the Arduino (ATmega) will report `HIGH` if:

- a voltage greater than 3.0V is present at the pin (5V boards)
- a voltage greater than 2.0V is present at the pin (3.3V boards)
  [%hardbreaks]

A pin may also be configured as an INPUT with link:../../../functions/digital-io/pinmode[`pinMode()`], and subsequently made HIGH with `link:../../../functions/digital-io/digitalwrite[digitalWrite()]`. This will enable the internal 20K pullup resistors, which will _pull up_ the input pin to a `HIGH` reading unless it is pulled `LOW` by external circuitry. This can be done alternatively by passing `INPUT_PULLUP` as argument to the link:../../../functions/digital-io/pinmode[`pinMode()`] function, as explained in more detail in the section "Defining Digital Pins modes: INPUT, INPUT_PULLUP, and OUTPUT" further below.
[%hardbreaks]

When a pin is configured to OUTPUT with link:../../../functions/digital-io/pinmode[`pinMode()`], and set to `HIGH` with link:../../../functions/digital-io/digitalwrite[`digitalWrite()`], the pin is at:

- 5 volts (5V boards)
- 3.3 volts (3.3V boards)

In this state it can source current, e.g. light an LED that is connected through a series resistor to ground.
[%hardbreaks]

[float]
=== LOW
The meaning of `LOW` also has a different meaning depending on whether a pin is set to `INPUT` or `OUTPUT`. When a pin is configured as an `INPUT` with link:../../../functions/digital-io/pinmode[`pinMode()`], and read with link:../../../functions/digital-io/digitalread[`digitalRead()`], the Arduino (ATmega) will report LOW if:

- a voltage less than 1.5V is present at the pin (5V boards)
- a voltage less than 1.0V (Approx) is present at the pin (3.3V boards)

When a pin is configured to `OUTPUT` with link:../../../functions/digital-io/pinmode[`pinMode()`], and set to `LOW` with link:../../../functions/digital-io/digitalwrite[`digitalWrite()`], the pin is at 0 volts (both 5V and 3.3V boards). In this state it can sink current, e.g. light an LED that is connected through a series resistor to +5 volts (or +3.3 volts).
[%hardbreaks]

[float]
== Defining Digital Pins modes: INPUT, INPUT_PULLUP, and OUTPUT
Digital pins can be used as `INPUT`, `INPUT_PULLUP`, or `OUTPUT`. Changing a pin with link:../../../functions/digital-io/pinmode[`pinMode()`] changes the electrical behavior of the pin.

[float]
=== Pins Configured as INPUT
Arduino (ATmega) pins configured as `INPUT` with link:../../../functions/digital-io/pinmode[`pinMode()`] are said to be in a _high-impedance_ state. Pins configured as `INPUT` make extremely small demands on the circuit that they are sampling, equivalent to a series resistor of 100 Megohms in front of the pin. This makes them useful for reading a sensor.
[%hardbreaks]

If you have your pin configured as an `INPUT`, and are reading a switch, when the switch is in the open state the input pin will be "floating", resulting in unpredictable results. In order to assure a proper reading when the switch is open, a pull-up or pull-down resistor must be used. The purpose of this resistor is to pull the pin to a known state when the switch is open. A 10 K ohm resistor is usually chosen, as it is a low enough value to reliably prevent a floating input, and at the same time a high enough value to not draw too much current when the switch is closed. See the http://arduino.cc/en/Tutorial/DigitalReadSerial[Digital Read Serial^] tutorial for more information.
[%hardbreaks]

If a pull-down resistor is used, the input pin will be `LOW` when the switch is open and `HIGH` when the switch is closed.
[%hardbreaks]

If a pull-up resistor is used, the input pin will be `HIGH` when the switch is open and `LOW` when the switch is closed.
[%hardbreaks]

[float]
=== Pins Configured as INPUT_PULLUP
The ATmega microcontroller on the Arduino has internal pull-up resistors (resistors that connect to power internally) that you can access. If you prefer to use these instead of external pull-up resistors, you can use the `INPUT_PULLUP` argument in link:../../../functions/digital-io/pinmode[`pinMode()`].
[%hardbreaks]

See the http://arduino.cc/en/Tutorial/InputPullupSerial[Input Pullup Serial^] tutorial for an example of this in use.
[%hardbreaks]

Pins configured as inputs with either `INPUT` or `INPUT_PULLUP` can be damaged or destroyed if they are connected to voltages below ground (negative voltages) or above the positive power rail (5V or 3V).
[%hardbreaks]

[float]
=== Pins Configured as OUTPUT
Pins configured as `OUTPUT` with link:../../../functions/digital-io/pinmode[`pinMode()`] are said to be in a _low-impedance_ state. This means that they can provide a substantial amount of current to other circuits. ATmega pins can source (provide current) or sink (absorb current) up to 40 mA (milliamps) of current to other devices/circuits. This makes them useful for powering LEDs because LEDs typically use less than 40 mA. Loads greater than 40 mA (e.g. motors) will require a transistor or other interface circuitry.
[%hardbreaks]

Pins configured as outputs can be damaged or destroyed if they are connected to either the ground or positive power rails.
[%hardbreaks]

[float]
== Defining built-ins: LED_BUILTIN
Most Arduino boards have a pin connected to an on-board LED in series with a resistor. The constant `LED_BUILTIN` is the number of the pin to which the on-board LED is connected. Most boards have this LED connected to digital pin 13.

--
// OVERVIEW SECTION ENDS

// HOW TO USE SECTION STARTS
[#howtouse]
--

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
