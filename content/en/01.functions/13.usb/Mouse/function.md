---
title: Mouse
categories: "Functions"
subCategories: "USB"
---

**Description**

The mouse functions enable 32u4 or SAMD micro based boards to control
cursor movement on a connected computer through their micro’s native USB
port. When updating the cursor position, it is always relative to the
cursor’s previous location.

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

[Mouse.begin()](../mouse/mousebegin)
[Mouse.click()](../mouse/mouseclick)
[Mouse.end()](../mouse/mouseend)
[Mouse.move()](../mouse/mousemove)
[Mouse.press()](../mouse/mousepress)
[Mouse.release()](../mouse/mouserelease)
[Mouse.isPressed()](../mouse/mouseispressed)

**See also**

-   EXAMPLE
    [KeyboardAndMouseControl^](http://www.arduino.cc/en/Tutorial/KeyboardAndMouseControl):
    Demonstrates the Mouse and Keyboard commands in one program.

-   EXAMPLE
    [ButtonMouseControl^](http://www.arduino.cc/en/Tutorial/ButtonMouseControl):
    Control cursor movement with 5 pushbuttons.

-   EXAMPLE
    [JoystickMouseControl^](http://www.arduino.cc/en/Tutorial/JoystickMouseControl):
    Controls a computer’s cursor movement with a Joystick when a button
    is pressed.

