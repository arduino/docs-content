---
title: Keyboard
categories: "Functions"
subCategories: "USB"
---

**Description**

The keyboard functions enable 32u4 or SAMD micro based boards to send
keystrokes to an attached computer through their micro’s native USB
port.

**Note: Not every possible ASCII character, particularly the
non-printing ones, can be sent with the Keyboard library.**
The library supports the use of modifier keys. Modifier keys change the
behavior of another key when pressed simultaneously. [See
here](../keyboard/keyboardmodifiers) for additional information on
supported keys and their use.

**Compatible Hardware**

HID is supported on the following boards:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Board</th>
<th style="text-align: left;">Supported Pins</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><p><a
href="https://docs.arduino.cc/hardware/leonardo">Leonardo</a></p></td>
<td style="text-align: left;"><p>All digital &amp; analog pins</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p><a
href="https://docs.arduino.cc/hardware/micro">Micro</a></p></td>
<td style="text-align: left;"><p>All digital &amp; analog pins</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p><a
href="https://docs.arduino.cc/hardware/due">Due</a></p></td>
<td style="text-align: left;"><p>All digital &amp; analog pins</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p><a
href="https://docs.arduino.cc/hardware/zero">Zero</a></p></td>
<td style="text-align: left;"><p>All digital &amp; analog pins</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p><a
href="https://docs.arduino.cc/hardware/uno-r4-minima">UNO R4
Minima</a></p></td>
<td style="text-align: left;"><p>All digital &amp; analog pins</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p><a
href="https://docs.arduino.cc/hardware/uno-r4-wifi">UNO R4
WiFi</a></p></td>
<td style="text-align: left;"><p>All digital &amp; analog pins</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p><a
href="https://docs.arduino.cc/hardware/giga-r1-wifi">Giga
R1</a></p></td>
<td style="text-align: left;"><p>All digital &amp; analog pins</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p><a
href="https://docs.arduino.cc/hardware/nano-esp32">Nano
ESP32</a></p></td>
<td style="text-align: left;"><p>All digital &amp; analog pins</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p><a
href="https://docs.arduino.cc/#mkr-family">MKR Family</a></p></td>
<td style="text-align: left;"><p>All digital &amp; analog pins</p></td>
</tr>
</tbody>
</table>

**Notes and Warnings**

These core libraries allow the 32u4 and SAMD based boards (Leonardo,
Esplora, Zero, Due and MKR Family) to appear as a native Mouse and/or
Keyboard to a connected computer.

**A word of caution on using the Mouse and Keyboard libraries**: if the
Mouse or Keyboard library is constantly running, it will be difficult to
program your board. Functions such as `Mouse.move()` and
`Keyboard.print()` will move your cursor or send keystrokes to a
connected computer and should only be called when you are ready to
handle them. It is recommended to use a control system to turn this
functionality on, like a physical switch or only responding to specific
input you can control. Refer to the Mouse and Keyboard examples for some
ways to handle this.

When using the Mouse or Keyboard library, it may be best to test your
output first using [Serial.print()](../../communication/serial/print).
This way, you can be sure you know what values are being reported.

**Functions**

[Keyboard.begin()](../keyboard/keyboardbegin)
[Keyboard.end()](../keyboard/keyboardend)
[Keyboard.press()](../keyboard/keyboardpress)
[Keyboard.print()](../keyboard/keyboardprint)
[Keyboard.println()](../keyboard/keyboardprintln)
[Keyboard.release()](../keyboard/keyboardrelease)
[Keyboard.releaseAll()](../keyboard/keyboardreleaseall)
[Keyboard.write()](../keyboard/keyboardwrite)

**See also**

-   EXAMPLE
    [KeyboardAndMouseControl^](http://www.arduino.cc/en/Tutorial/KeyboardAndMouseControl):
    Demonstrates the Mouse and Keyboard commands in one program.

-   EXAMPLE
    [KeyboardMessage^](http://www.arduino.cc/en/Tutorial/KeyboardMessage):
    Sends a text string when a button is pressed.

-   EXAMPLE
    [KeyboardLogout^](http://www.arduino.cc/en/Tutorial/KeyboardLogout):
    Logs out the current user with key commands

-   EXAMPLE
    [KeyboardSerial^](http://www.arduino.cc/en/Tutorial/KeyboardSerial):
    Reads a byte from the serial port, and sends back a keystroke.

-   EXAMPLE
    [KeyboardReprogram^](http://www.arduino.cc/en/Tutorial/KeyboardReprogram):
    opens a new window in the Arduino IDE and reprograms the board with
    a simple blink program

