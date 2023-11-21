---
title: digitalWrite()
categories: "Functions"
subCategories: "Digital I/O"
---

//
:ext-relative: .html

= digitalWrite()

// OVERVIEW SECTION STARTS
[#overview]
--

[float]
=== Description
Write a `HIGH` or a `LOW` value to a digital pin.

If the pin has been configured as an `OUTPUT` with `pinMode()`, its voltage will be set to the corresponding value: 5V (or 3.3V on 3.3V boards) for `HIGH`, 0V (ground) for `LOW`.
[%hardbreaks]

If the pin is configured as an `INPUT`, `digitalWrite()` will enable (`HIGH`) or disable (`LOW`) the internal pullup on the input pin. It is recommended to set the `pinMode()` to `INPUT_PULLUP` to enable the internal pull-up resistor. See the http://arduino.cc/en/Tutorial/DigitalPins[Digital Pins^] tutorial for more information.
[%hardbreaks]

If you do not set the `pinMode()` to `OUTPUT`, and connect an LED to a pin, when calling `digitalWrite(HIGH)`, the LED may appear dim. Without explicitly setting `pinMode()`, `digitalWrite()` will have enabled the internal pull-up resistor, which acts like a large current-limiting resistor.
[%hardbreaks]

[float]
=== Syntax
`digitalWrite(pin, value)`

[float]
=== Parameters
`pin`: the Arduino pin number. +
`value`: `HIGH` or `LOW`.

[float]
=== Returns
Nothing

--
// OVERVIEW SECTION ENDS

// HOW TO USE SECTION STARTS
[#howtouse]
--

[float]
=== Example Code
// Describe what the example code is all about and add relevant code ►►►►► THIS SECTION IS MANDATORY ◄◄◄◄◄
The code makes the digital pin 13 an `OUTPUT` and toggles it by alternating between `HIGH` and `LOW` at one second pace.

## [source,arduino]

void setup() {
pinMode(13, OUTPUT); // sets the digital pin 13 as output
}

void loop() {
digitalWrite(13, HIGH); // sets the digital pin 13 on
delay(1000); // waits for a second
digitalWrite(13, LOW); // sets the digital pin 13 off
delay(1000); // waits for a second
}

---

[%hardbreaks]

[float]
=== Notes and Warnings
The analog input pins can be used as digital pins, referred to as A0, A1, etc. The exception is the Arduino Nano, Pro Mini, and Mini's A6 and A7 pins, which can only be used as analog inputs.

--
// HOW TO USE SECTION ENDS

// SEE ALSO SECTION
[#see_also]
--

[float]
=== See also

[role="example"]

- #EXAMPLE# http://arduino.cc/en/Tutorial/DigitalPins[Description of the digital pins^]

--
// SEE ALSO SECTION ENDS
