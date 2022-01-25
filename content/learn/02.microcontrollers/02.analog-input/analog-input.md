---
title: 'Analog Input Pins'
description: 'Find out how analog input pins work on an Arduino.'
tags: [Analog Inputs, Pin Setup]
---


A description of the analog input pins on an Arduino chip (ATmega8, ATmega168, ATmega328P, or ATmega1280).

## A/D converter

The ATmega controllers used for the Arduino contain an onboard 6 channel (8 channels on the Mini and Nano, 16 on the Mega) analog-to-digital (A/D) converter. The converter has 10 bit resolution, returning integers from 0 to 1023. While the main function of the analog pins for most Arduino users is to read analog sensors, the analog pins also have all the functionality of general purpose input/output (GPIO) pins (the same as digital pins 0 - 13).

Consequently, if a user needs more general purpose input output pins, and all the analog pins are not in use, the analog pins may be used for GPIO.

## Pin mapping

The analog pins can be used identically to the digital pins, using the aliases A0 (for analog input 0), A1, etc.  For example, the code would look like this to set analog pin 0 to an output, and to set it HIGH:

```arduino
pinMode(A0, OUTPUT);
digitalWrite(A0, HIGH);
```

## Pull-up resistors

The analog pins also have pull-up resistors, which work identically to pull-up resistors on the digital pins. They are enabled by issuing a command such as

```arduino
pinMode(A0, INPUT_PULLUP);  // set pull-up on analog pin 0
```

Be aware however that turning on a pull-up will affect the values reported by analogRead().

## Details and Caveats

The analogRead command will not work correctly if a pin has been previously set to an output, so if this is the case, set it back to an input before using analogRead. Similarly if the pin has been set to HIGH as an output, the pull-up resistor will be set, when switched back to an input.

The ATmega datasheet also cautions against switching analog pins in close temporal proximity to making A/D readings (analogRead) on other analog pins. This can cause electrical noise and introduce jitter in the analog system.
It may be desirable, after manipulating analog pins (in digital mode), to add a short delay before using analogRead() to read other analog pins.