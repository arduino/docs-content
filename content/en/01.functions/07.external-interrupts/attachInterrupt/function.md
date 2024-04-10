---
title: attachInterrupt()
categories: "Functions"
subCategories: "External Interrupts"
---

**Description**

**Digital Pins With Interrupts**

The first parameter to `attachInterrupt()` is an interrupt number.
Normally you should use `digitalPinToInterrupt(pin)` to translate the
actual digital pin to the specific interrupt number. For example, if you
connect to pin 3, use `digitalPinToInterrupt(3)` as the first parameter
to `attachInterrupt()`.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Board</th>
<th style="text-align: left;">Digital Pins Usable For Interrupts</th>
<th style="text-align: left;">Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><p>Uno Rev3, Nano, Mini, other
328-based</p></td>
<td style="text-align: left;"><p>2, 3</p></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>UNO R4 Minima, UNO R4 WiFi</p></td>
<td style="text-align: left;"><p>2, 3</p></td>
<td style="text-align: left;"></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Uno WiFi Rev2, Nano Every</p></td>
<td style="text-align: left;"><p>All digital pins</p></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Mega, Mega2560, MegaADK</p></td>
<td style="text-align: left;"><p>2, 3, 18, 19, 20, 21</p></td>
<td style="text-align: left;"><p>(<strong>pins 20 &amp; 21</strong> are
not available to use for interrupts while they are used for I2C
communication; they also have external pull-ups that cannot be
disabled)</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Micro, Leonardo</p></td>
<td style="text-align: left;"><p>0, 1, 2, 3, 7</p></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Zero</p></td>
<td style="text-align: left;"><p>0-3, 5-13, A0-A5</p></td>
<td style="text-align: left;"><p>Pin 4 cannot be used as an
interrupt.</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>MKR Family boards</p></td>
<td style="text-align: left;"><p>0, 1, 4, 5, 6, 7, 8, 9, A1, A2</p></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Nano 33 IoT</p></td>
<td style="text-align: left;"><p>2, 3, 9, 10, 11, 13, A1, A5,
A7</p></td>
<td style="text-align: left;"></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Nano 33 BLE, Nano 33 BLE Sense (rev 1
&amp; 2)</p></td>
<td style="text-align: left;"><p>all pins</p></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Nano RP2040 Connect</p></td>
<td style="text-align: left;"><p>0-13, A0-A5</p></td>
<td style="text-align: left;"></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Nano ESP32</p></td>
<td style="text-align: left;"><p>all pins</p></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>GIGA R1 WiFi</p></td>
<td style="text-align: left;"><p>all pins</p></td>
<td style="text-align: left;"></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Due</p></td>
<td style="text-align: left;"><p>all digital pins</p></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>101</p></td>
<td style="text-align: left;"><p>all digital pins</p></td>
<td style="text-align: left;"><p>(Only pins 2, 5, 7, 8, 10, 11, 12, 13
work with <strong>CHANGE</strong>))</p></td>
</tr>
</tbody>
</table>

**Notes and Warnings**

**Note**
Inside the attached function, `delay()` won’t work and the value
returned by `millis()` will not increment. Serial data received while in
the function may be lost. You should declare as `volatile` any variables
that you modify within the attached function. See the section on ISRs
below for more information.

**Using Interrupts**

Interrupts are useful for making things happen automatically in
microcontroller programs and can help solve timing problems. Good tasks
for using an interrupt may include reading a rotary encoder, or
monitoring user input.

If you wanted to ensure that a program always caught the pulses from a
rotary encoder, so that it never misses a pulse, it would make it very
tricky to write a program to do anything else, because the program would
need to constantly poll the sensor lines for the encoder, in order to
catch pulses when they occurred. Other sensors have a similar interface
dynamic too, such as trying to read a sound sensor that is trying to
catch a click, or an infrared slot sensor (photo-interrupter) trying to
catch a coin drop. In all of these situations, using an interrupt can
free the microcontroller to get some other work done while not missing
the input.

**About Interrupt Service Routines**

ISRs are special kinds of functions that have some unique limitations
most other functions do not have. An ISR cannot have any parameters, and
they shouldn’t return anything.

Generally, an ISR should be as short and fast as possible. If your
sketch uses multiple ISRs, only one can run at a time, other interrupts
will be executed after the current one finishes in an order that depends
on the priority they have. `millis()` relies on interrupts to count, so
it will never increment inside an ISR. Since `delay()` requires
interrupts to work, it will not work if called inside an ISR. `micros()`
works initially but will start behaving erratically after 1-2 ms.
`delayMicroseconds()` does not use any counter, so it will work as
normal.

Typically global variables are used to pass data between an ISR and the
main program. To make sure variables shared between an ISR and the main
program are updated correctly, declare them as `volatile`.

For more information on interrupts, see [Nick Gammon’s
notes](http://gammon.com.au/interrupts).

**Syntax**

`attachInterrupt(digitalPinToInterrupt(pin), ISR, mode)` (recommended)
`attachInterrupt(interrupt, ISR, mode)` (not recommended)
`attachInterrupt(pin, ISR, mode)` (Not recommended. Additionally, this
syntax only works on Arduino SAMD Boards, Uno WiFi Rev2, Due, and 101.)

**Parameters**

`interrupt`: the number of the interrupt. Allowed data types: `int`.
`pin`: the Arduino pin number.
`ISR`: the ISR to call when the interrupt occurs; this function must
take no parameters and return nothing. This function is sometimes
referred to as an interrupt service routine.
`mode`: defines when the interrupt should be triggered. Four constants
are predefined as valid values:

-   **LOW** to trigger the interrupt whenever the pin is low,

-   **CHANGE** to trigger the interrupt whenever the pin changes value

-   **RISING** to trigger when the pin goes from low to high,

-   **FALLING** for when the pin goes from high to low.

The Due, Zero and MKR1000 boards allow also:

-   **HIGH** to trigger the interrupt whenever the pin is high.

**Returns**

Nothing

**Example Code**

    const byte ledPin = 13;
    const byte interruptPin = 2;
    volatile byte state = LOW;

    void setup() {
      pinMode(ledPin, OUTPUT);
      pinMode(interruptPin, INPUT_PULLUP);
      attachInterrupt(digitalPinToInterrupt(interruptPin), blink, CHANGE);
    }

    void loop() {
      digitalWrite(ledPin, state);
    }

    void blink() {
      state = !state;
    }

**Interrupt Numbers**

Normally you should use `digitalPinToInterrupt(pin)`, rather than place
an interrupt number directly into your sketch. The specific pins with
interrupts and their mapping to interrupt number varies for each type of
board. Direct use of interrupt numbers may seem simple, but it can cause
compatibility trouble when your sketch runs on a different board.

However, older sketches often have direct interrupt numbers. Often
number 0 (for digital pin 2) or number 1 (for digital pin 3) were used.
The table below shows the available interrupt pins on various boards.

Note that in the table below, the interrupt numbers refer to the number
to be passed to `attachInterrupt()`. For historical reasons, this
numbering does not always correspond directly to the interrupt numbering
on the ATmega chip (e.g. int.0 corresponds to INT4 on the ATmega2560
chip).

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Board</th>
<th style="text-align: left;">int.0</th>
<th style="text-align: left;">int.1</th>
<th style="text-align: left;">int.2</th>
<th style="text-align: left;">int.3</th>
<th style="text-align: left;">int.4</th>
<th style="text-align: left;">int.5</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><p>Uno, Ethernet</p></td>
<td style="text-align: left;"><p>2</p></td>
<td style="text-align: left;"><p>3</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Mega2560</p></td>
<td style="text-align: left;"><p>2</p></td>
<td style="text-align: left;"><p>3</p></td>
<td style="text-align: left;"><p>21</p></td>
<td style="text-align: left;"><p>20</p></td>
<td style="text-align: left;"><p>19</p></td>
<td style="text-align: left;"><p>18</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>32u4 based (e.g Leonardo,
Micro)</p></td>
<td style="text-align: left;"><p>3</p></td>
<td style="text-align: left;"><p>2</p></td>
<td style="text-align: left;"><p>0</p></td>
<td style="text-align: left;"><p>1</p></td>
<td style="text-align: left;"><p>7</p></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

For Uno WiFi Rev2, Due, Zero, MKR Family and 101 boards the **interrupt
number = pin number**.

**See also**

