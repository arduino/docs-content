---
title: analogReference()
categories: "Functions"
subCategories: "Analog I/O"
---

**Description**

Configures the reference voltage used for analog input (i.e. the value
used as the top of the input range). The options are:

Arduino AVR Boards (Uno, Mega, Leonardo, etc.)

-   DEFAULT: the default analog reference of 5 volts (on 5V Arduino
    boards) or 3.3 volts (on 3.3V Arduino boards)

-   INTERNAL: a built-in reference, equal to 1.1 volts on the ATmega168
    or ATmega328P and 2.56 volts on the ATmega32U4 and ATmega8 (not
    available on the Arduino Mega)

-   INTERNAL1V1: a built-in 1.1V reference (Arduino Mega only)

-   INTERNAL2V56: a built-in 2.56V reference (Arduino Mega only)

-   EXTERNAL: the voltage applied to the AREF pin (0 to 5V only) is used
    as the reference.

Arduino Renesas Boards (UNO R4, Portenta C33)

-   AR\_DEFAULT: the default analog reference of 5 volts.

-   AR\_INTERNAL: A built-in reference, equal to 1.5 Volts on the RA4M1
    of the UNO R4

-   AR\_INTERNAL\_1\_5V: A built-in reference, equal to 1.5 V on the
    R7FA6M5 of the Portenta C33

-   AR\_INTERNAL\_2\_0V: A built-in reference, equal to 2.0 V on the
    R7FA6M5 of the Portenta C33

-   AR\_INTERNAL\_2\_5V: A built-in reference, equal to 2.5 V on the
    R7FA6M5 of the Portenta C33

-   AR\_EXTERNAL: the voltage applied to the AREF pin (0 to 5V only) is
    used as the reference.

Arduino SAMD Boards (Zero, etc.)

-   AR\_DEFAULT: the default analog reference of 3.3V

-   AR\_INTERNAL: a built-in 2.23V reference

-   AR\_INTERNAL1V0: a built-in 1.0V reference

-   AR\_INTERNAL1V65: a built-in 1.65V reference

-   AR\_INTERNAL2V23: a built-in 2.23V reference

-   AR\_EXTERNAL: the voltage applied to the AREF pin is used as the
    reference

Arduino megaAVR Boards (Uno WiFi Rev2)

-   DEFAULT: a built-in 0.55V reference

-   INTERNAL: a built-in 0.55V reference

-   VDD: Vdd of the ATmega4809. 5V on the Uno WiFi Rev2

-   INTERNAL0V55: a built-in 0.55V reference

-   INTERNAL1V1: a built-in 1.1V reference

-   INTERNAL1V5: a built-in 1.5V reference

-   INTERNAL2V5: a built-in 2.5V reference

-   INTERNAL4V3: a built-in 4.3V reference

-   EXTERNAL: the voltage applied to the AREF pin (0 to 5V only) is used
    as the reference

Arduino SAM Boards (Due)

-   AR\_DEFAULT: the default analog reference of 3.3V. This is the only
    supported option for the Due.

Arduino Mbed OS Nano Boards (Nano 33 BLE), Arduino Mbed OS Edge Boards
(Edge Control)

-   AR\_VDD: the default 3.3 V reference

-   AR\_INTERNAL: built-in 0.6 V reference

-   AR\_INTERNAL1V2: 1.2 V reference (internal 0.6 V reference with 2x
    gain)

-   AR\_INTERNAL2V4: 2.4 V reference (internal 0.6 V reference with 4x
    gain)

**Syntax**

`analogReference(type)`

**Parameters**

`type`: which type of reference to use (see list of options in the
description).

**Returns**

Nothing

**Notes and Warnings**

After changing the analog reference, the first few readings from
`analogRead()` may not be accurate.

**Don’t use anything less than 0V or more than 5V for external reference
voltage on the AREF pin! If you’re using an external reference on the
AREF pin, you must set the analog reference to EXTERNAL before calling
`analogRead()`.** Otherwise, you will short together the active
reference voltage (internally generated) and the AREF pin, possibly
damaging the microcontroller on your Arduino board.

Alternatively, you can connect the external reference voltage to the
AREF pin through a 5K resistor, allowing you to switch between external
and internal reference voltages. Note that the resistor will alter the
voltage that gets used as the reference because there is an internal 32K
resistor on the AREF pin. The two act as a voltage divider, so, for
example, 2.5V applied through the resistor will yield 2.5 \* 32 / (32 +
5) = ~2.2V at the AREF pin.

**See also**

-   EXAMPLE [Description of the analog input
    pins^](http://arduino.cc/en/Tutorial/AnalogInputPins)

