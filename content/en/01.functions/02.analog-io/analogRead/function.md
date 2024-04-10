---
title: analogRead()
categories: "Functions"
subCategories: "Analog I/O"
---

**Description**

Reads the value from the specified analog pin. Arduino boards contain a
multichannel, 10-bit analog to digital converter. This means that it
will map input voltages between 0 and the operating voltage(5V or 3.3V)
into integer values between 0 and 1023. On an Arduino UNO, for example,
this yields a resolution between readings of: 5 volts / 1024 units or,
0.0049 volts (4.9 mV) per unit. See the table below for the usable pins,
operating voltage and maximum resolution for some Arduino boards.

The input range can be changed using
[analogReference()](../analogreference), while the resolution can be
changed (only for Zero, Due and MKR boards) using
[analogReadResolution()](../../zero-due-mkr-family/analogreadresolution).

On ATmega based boards (UNO, Nano, Mini, Mega), it takes about 100
microseconds (0.0001 s) to read an analog input, so the maximum reading
rate is about 10,000 times a second.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Board</th>
<th style="text-align: left;">Operating voltage</th>
<th style="text-align: left;">Usable pins</th>
<th style="text-align: left;">Max resolution</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><p>UNO R3</p></td>
<td style="text-align: left;"><p>5 Volts</p></td>
<td style="text-align: left;"><p>A0 to A5</p></td>
<td style="text-align: left;"><p>10 bits</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>UNO R4 (Minima, WiFi)</p></td>
<td style="text-align: left;"><p>5 Volts</p></td>
<td style="text-align: left;"><p>A0 to A5</p></td>
<td style="text-align: left;"><p>14 bits**</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Mini</p></td>
<td style="text-align: left;"><p>5 Volts</p></td>
<td style="text-align: left;"><p>A0 to A7</p></td>
<td style="text-align: left;"><p>10 bits</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Nano, Nano Every</p></td>
<td style="text-align: left;"><p>5 Volts</p></td>
<td style="text-align: left;"><p>A0 to A7</p></td>
<td style="text-align: left;"><p>10 bits</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Nano 33 (IoT, BLE, RP2040,
ESP32)</p></td>
<td style="text-align: left;"><p>3.3 Volts</p></td>
<td style="text-align: left;"><p>A0 to A7</p></td>
<td style="text-align: left;"><p>12 bits**</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Mega, Mega2560, MegaADK</p></td>
<td style="text-align: left;"><p>5 Volts</p></td>
<td style="text-align: left;"><p>A0 to A14</p></td>
<td style="text-align: left;"><p>10 bits</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Micro</p></td>
<td style="text-align: left;"><p>5 Volts</p></td>
<td style="text-align: left;"><p>A0 to A11*</p></td>
<td style="text-align: left;"><p>10 bits</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Leonardo</p></td>
<td style="text-align: left;"><p>5 Volts</p></td>
<td style="text-align: left;"><p>A0 to A11*</p></td>
<td style="text-align: left;"><p>10 bits</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Zero</p></td>
<td style="text-align: left;"><p>3.3 Volts</p></td>
<td style="text-align: left;"><p>A0 to A5</p></td>
<td style="text-align: left;"><p>12 bits**</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Due</p></td>
<td style="text-align: left;"><p>3.3 Volts</p></td>
<td style="text-align: left;"><p>A0 to A11</p></td>
<td style="text-align: left;"><p>12 bits**</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>GIGA R1</p></td>
<td style="text-align: left;"><p>3.3 Volts</p></td>
<td style="text-align: left;"><p>A0 to A11</p></td>
<td style="text-align: left;"><p>16 bits**</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>MKR Family boards</p></td>
<td style="text-align: left;"><p>3.3 Volts</p></td>
<td style="text-align: left;"><p>A0 to A6</p></td>
<td style="text-align: left;"><p>12 bits**</p></td>
</tr>
</tbody>
</table>

\*A0 through A5 are labelled on the board, A6 through A11 are
respectively available on pins 4, 6, 8, 9, 10, and 12
\*\*The default `analogRead()` resolution for these boards is 10 bits,
for compatibility. You need to use
[analogReadResolution()](../../zero-due-mkr-family/analogreadresolution)
to change it to a higher resolution.

**Syntax**

`analogRead(pin)`

**Parameters**

`pin`: the name of the analog input pin to read from.

**Returns**

The analog reading on the pin. Although it is limited to the resolution
of the analog to digital converter (0-1023 for 10 bits or 0-4095 for 12
bits). Data type: `int`.

**Example Code**

The code reads the voltage on analogPin and displays it.

    int analogPin = A3; // potentiometer wiper (middle terminal) connected to analog pin 3
                        // outside leads to ground and +5V
    int val = 0;  // variable to store the value read

    void setup() {
      Serial.begin(9600);           //  setup serial
    }

    void loop() {
      val = analogRead(analogPin);  // read the input pin
      Serial.println(val);          // debug value
    }

**Notes and Warnings**

If the analog input pin is not connected to anything, the value returned
by `analogRead()` will fluctuate based on a number of factors (e.g. the
values of the other analog inputs, how close your hand is to the board,
etc.).

**See also**

-   LANGUAGE
    [analogReadResolution()](../../zero-due-mkr-family/analogreadresolution)

-   EXAMPLE [Description of the analog input
    pins^](http://arduino.cc/en/Tutorial/AnalogInputPins)

