---
title: digitalWrite()
categories: "Functions"
subCategories: "Digital I/O"
---

**Description**

Write a `HIGH` or a `LOW` value to a digital pin.

If the pin has been configured as an `OUTPUT` with `pinMode()`, its
voltage will be set to the corresponding value: 5V (or 3.3V on 3.3V
boards) for `HIGH`, 0V (ground) for `LOW`.

If the pin is configured as an `INPUT`, `digitalWrite()` will enable
(`HIGH`) or disable (`LOW`) the internal pullup on the input pin. It is
recommended to set the `pinMode()` to `INPUT_PULLUP` to enable the
internal pull-up resistor. See the [Digital
Pins^](http://arduino.cc/en/Tutorial/DigitalPins) tutorial for more
information.

If you do not set the `pinMode()` to `OUTPUT`, and connect an LED to a
pin, when calling `digitalWrite(HIGH)`, the LED may appear dim. Without
explicitly setting `pinMode()`, `digitalWrite()` will have enabled the
internal pull-up resistor, which acts like a large current-limiting
resistor.

**Syntax**

`digitalWrite(pin, value)`

**Parameters**

`pin`: the Arduino pin number.
`value`: `HIGH` or `LOW`.

**Returns**

Nothing

**Example Code**

The code makes the digital pin 13 an `OUTPUT` and toggles it by
alternating between `HIGH` and `LOW` at one second pace.

    void setup() {
      pinMode(13, OUTPUT);    // sets the digital pin 13 as output
    }

    void loop() {
      digitalWrite(13, HIGH); // sets the digital pin 13 on
      delay(1000);            // waits for a second
      digitalWrite(13, LOW);  // sets the digital pin 13 off
      delay(1000);            // waits for a second
    }

**Notes and Warnings**

The analog input pins can be used as digital pins, referred to as A0,
A1, etc. The exception is the Arduino Nano, Pro Mini, and Mini’s A6 and
A7 pins, which can only be used as analog inputs.

**See also**

-   EXAMPLE [Description of the digital
    pins^](http://arduino.cc/en/Tutorial/DigitalPins)
