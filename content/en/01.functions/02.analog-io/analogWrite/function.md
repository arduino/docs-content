---
title: analogWrite()
categories: "Functions"
subCategories: "Analog I/O"
---

**Description**

Writes an analog value ([PWM wave](http://arduino.cc/en/Tutorial/PWM))
to a pin. Can be used to light a LED at varying brightnesses or drive a
motor at various speeds. After a call to `analogWrite()`, the pin will
generate a steady rectangular wave of the specified duty cycle until the
next call to `analogWrite()` (or a call to `digitalRead()` or
`digitalWrite()`) on the same pin.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Board</th>
<th style="text-align: left;">PWM Pins <code>*</code></th>
<th style="text-align: left;">PWM Frequency</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><p>UNO (R3 and earlier), Nano,
Mini</p></td>
<td style="text-align: left;"><p>3, 5, 6, 9, 10, 11</p></td>
<td style="text-align: left;"><p>490 Hz (pins 5 and 6: 980 Hz)</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>UNO R4 (Minima, WiFi)
<code>*</code></p></td>
<td style="text-align: left;"><p>3, 5, 6, 9, 10, 11</p></td>
<td style="text-align: left;"><p>490 Hz</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Mega</p></td>
<td style="text-align: left;"><p>2 - 13, 44 - 46</p></td>
<td style="text-align: left;"><p>490 Hz (pins 4 and 13: 980 Hz)</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>GIGA R1 <code>**</code></p></td>
<td style="text-align: left;"><p>2 - 13</p></td>
<td style="text-align: left;"><p>500 Hz</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Leonardo, Micro, Yún</p></td>
<td style="text-align: left;"><p>3, 5, 6, 9, 10, 11, 13</p></td>
<td style="text-align: left;"><p>490 Hz (pins 3 and 11: 980 Hz)</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>UNO WiFi Rev2, Nano Every</p></td>
<td style="text-align: left;"><p>3, 5, 6, 9, 10</p></td>
<td style="text-align: left;"><p>976 Hz</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>MKR boards <code>*</code></p></td>
<td style="text-align: left;"><p>0 - 8, 10, A3, A4</p></td>
<td style="text-align: left;"><p>732 Hz</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>MKR1000 WiFi <code>**</code></p></td>
<td style="text-align: left;"><p>0 - 8, 10, 11, A3, A4</p></td>
<td style="text-align: left;"><p>732 Hz</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Zero <code>**</code></p></td>
<td style="text-align: left;"><p>3 - 13, A0, A1</p></td>
<td style="text-align: left;"><p>732 Hz</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Nano 33 IoT <code>**</code></p></td>
<td style="text-align: left;"><p>2, 3, 5, 6, 9 - 12, A2, A3, A5</p></td>
<td style="text-align: left;"><p>732 Hz</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Nano 33 BLE/BLE Sense
<code>**</code></p></td>
<td style="text-align: left;"><p>1 - 13, A0 - A7</p></td>
<td style="text-align: left;"><p>500 Hz</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Due <code>*</code></p></td>
<td style="text-align: left;"><p>2-13</p></td>
<td style="text-align: left;"><p>1000 Hz</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>101</p></td>
<td style="text-align: left;"><p>3, 5, 6, 9</p></td>
<td style="text-align: left;"><p>pins 3 and 9: 490 Hz, pins 5 and 6: 980
Hz</p></td>
</tr>
</tbody>
</table>

`` These pins are officially supported PWM pins. While some boards have
additional pins capable of PWM, using them is recommended only for
advanced users that can account for timer availability and potential
conflicts with other uses of those pins.
`` In addition to PWM capabilities on the pins noted above, the MKR,
Nano 33 IoT, Zero and UNO R4 boards have true analog output when using
`analogWrite()` on the `DAC0` (`A0`) pin.
`` In addition to PWM capabilities on the pins noted above, the Due and
GIGA R1 boards have true analog output when using `analogWrite()` on
pins `DAC0` and `DAC1`.
`**` Only 4 different pins can be used at the same time. Enabling PWM on
more than 4 pins will abort the running sketch and require resetting the
board to upload a new sketch again.

You do not need to call `pinMode()` to set the pin as an output before
calling `analogWrite()`. The `analogWrite` function has nothing to do
with the analog pins or the `analogRead` function.

**Syntax**

`analogWrite(pin, value)`

**Parameters**

`pin`: the Arduino pin to write to. Allowed data types: `int`.
`value`: the duty cycle: between 0 (always off) and 255 (always on).
Allowed data types: `int`.

**Returns**

Nothing

**Example Code**

Sets the output to the LED proportional to the value read from the
potentiometer.

    int ledPin = 9;      // LED connected to digital pin 9
    int analogPin = 3;   // potentiometer connected to analog pin 3
    int val = 0;         // variable to store the read value

    void setup() {
      pinMode(ledPin, OUTPUT);  // sets the pin as output
    }

    void loop() {
      val = analogRead(analogPin);  // read the input pin
      analogWrite(ledPin, val / 4); // analogRead values go from 0 to 1023, analogWrite values from 0 to 255
    }

**Notes and Warnings**

The PWM outputs generated on pins 5 and 6 will have higher-than-expected
duty cycles. This is because of interactions with the `millis()` and
`delay()` functions, which share the same internal timer used to
generate those PWM outputs. This will be noticed mostly on low
duty-cycle settings (e.g. 0 - 10) and may result in a value of 0 not
fully turning off the output on pins 5 and 6.

**See also**

-   LANGUAGE
    [analogWriteResolution()](../../zero-due-mkr-family/analogwriteresolution)

-   DEFINITION [PWM^](http://arduino.cc/en/Tutorial/PWM)

-   EXAMPLE [Blink^](http://arduino.cc/en/Tutorial/Blink)

