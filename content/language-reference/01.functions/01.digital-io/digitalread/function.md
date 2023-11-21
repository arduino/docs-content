---
title: digitalRead()
categories: "Functions"
subCategories: "Digital I/O"
---

//
:ext-relative: .html

= digitalRead()

// OVERVIEW SECTION STARTS
[#overview]
--

[float]
=== Description
Reads the value from a specified digital pin, either `HIGH` or `LOW`.
[%hardbreaks]

[float]
=== Syntax
`digitalRead(pin)`

[float]
=== Parameters
`pin`: the Arduino pin number you want to read

[float]
=== Returns
`HIGH` or `LOW`

--
// OVERVIEW SECTION ENDS

// HOW TO USE SECTION STARTS
[#howtouse]
--

[float]
=== Example Code
// Describe what the example code is all about and add relevant code ►►►►► THIS SECTION IS MANDATORY ◄◄◄◄◄
Sets pin 13 to the same value as pin 7, declared as an input.

## [source,arduino]

int ledPin = 13; // LED connected to digital pin 13
int inPin = 7; // pushbutton connected to digital pin 7
int val = 0; // variable to store the read value

void setup() {
pinMode(ledPin, OUTPUT); // sets the digital pin 13 as output
pinMode(inPin, INPUT); // sets the digital pin 7 as input
}

void loop() {
val = digitalRead(inPin); // read the input pin
digitalWrite(ledPin, val); // sets the LED to the button's value
}

---

[%hardbreaks]

[float]
=== Notes and Warnings
If the pin isn't connected to anything, `digitalRead()` can return either `HIGH` or `LOW` (and this can change randomly).

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
