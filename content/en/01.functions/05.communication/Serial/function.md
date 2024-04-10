---
title: Serial
categories: "Functions"
subCategories: "Communication"
---

**Description**

Used for communication between the Arduino board and a computer or other
devices. All Arduino boards have at least one serial port (also known as
a UART or USART), and some have several.

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Board</th>
<th style="text-align: left;">Serial pins</th>
<th style="text-align: left;">Serial1 pins</th>
<th style="text-align: left;">Serial2 pins</th>
<th style="text-align: left;">Serial3 pins</th>
<th style="text-align: left;">Serial4 pins</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><p>UNO R3, UNO R3 SMD Mini</p></td>
<td style="text-align: left;"><p>0(RX), 1(TX)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Nano (classic)</p></td>
<td style="text-align: left;"><p>0(RX), 1(TX)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>UNO R4 Minima, UNO R4 WiFi</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>0(RX0), 1(TX0)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Leonardo, Micro, Yún Rev2</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>0(RX), 1(TX)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Uno WiFi Rev.2</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>0(RX), 1(TX)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>MKR boards</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>13(RX), 14(TX)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Zero</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>0(RX), 1(TX)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>GIGA R1 WiFi</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>0(RX), 1(TX)</p></td>
<td style="text-align: left;"><p>19(RX1), 18(TX1)</p></td>
<td style="text-align: left;"><p>17(RX2), 16(TX2)</p></td>
<td style="text-align: left;"><p>15(RX3), 14(TX3)</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Due</p></td>
<td style="text-align: left;"><p>0(RX), 1(TX)</p></td>
<td style="text-align: left;"><p>19(RX1), 18(TX1)</p></td>
<td style="text-align: left;"><p>17(RX2), 16(TX2)</p></td>
<td style="text-align: left;"><p>15(RX3), 14(TX3)</p></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Mega 2560 Rev3</p></td>
<td style="text-align: left;"><p>0(RX), 1(TX)</p></td>
<td style="text-align: left;"><p>19(RX1), 18(TX1)</p></td>
<td style="text-align: left;"><p>17(RX2), 16(TX2)</p></td>
<td style="text-align: left;"><p>15(RX3), 14(TX3)</p></td>
<td style="text-align: left;"></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Nano 33 IoT</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>0(RX0), 1(TX0)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Nano RP2040 Connect</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>0(RX0), 1(TX0)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Nano BLE / BLE Sense</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>0(RX0), 1(TX0)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

The Nano ESP32 board is an exception due to being based on the ESP32
core. Here, `Serial0` refers to `RX0` and `TX0`, while `Serial1` and
`Serial2` are additional ports that can be assigned to any free GPIO.

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr class="odd">
<td style="text-align: left;"><p>Board</p></td>
<td style="text-align: left;"><p>Serial0 pins</p></td>
<td style="text-align: left;"><p>Serial1 pins</p></td>
<td style="text-align: left;"><p>Serial2 pins</p></td>
<td style="text-align: left;"><p>Serial3 pins</p></td>
<td style="text-align: left;"><p>Serial4 pins</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Nano ESP32</p></td>
<td style="text-align: left;"><p>0(RX0), 1(TX0)</p></td>
<td style="text-align: left;"><p>Any free GPIO</p></td>
<td style="text-align: left;"><p>Any free GPIO</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

You can read more about configuring the Nano ESP32’s additional serial
ports in [this
article](https://docs.arduino.cc/tutorials/nano-esp32/cheat-sheet/#uart).

On older boards (Uno, Nano, Mini, and Mega), pins 0 and 1 are used for
communication with the computer. Connecting anything to these pins can
interfere with that communication, including causing failed uploads to
the board.

You can use the Arduino environment’s built-in serial monitor to
communicate with an Arduino board. Click the serial monitor button in
the toolbar and select the same baud rate used in the call to `begin()`.

Serial communication on pins TX/RX uses TTL logic levels (5V or 3.3V
depending on the board). Don’t connect these pins directly to an RS232
serial port; they operate at +/- 12V and can damage your Arduino board.

To use these extra serial ports to communicate with your personal
computer, you will need an additional USB-to-serial adaptor, as they are
not connected to the Mega’s USB-to-serial adaptor. To use them to
communicate with an external TTL serial device, connect the TX pin to
your device’s RX pin, the RX to your device’s TX pin, and the ground of
your Mega to your device’s ground.

**Functions**

[if(Serial)](../serial/ifserial)
[available()](../serial/available)
[availableForWrite()](../serial/availableforwrite)
[begin()](../serial/begin)
[end()](../serial/end)
[find()](../serial/find)
[findUntil()](../serial/finduntil)
[flush()](../serial/flush)
[parseFloat()](../serial/parsefloat)
[parseInt()](../serial/parseint)
[peek()](../serial/peek)
[print()](../serial/print)
[println()](../serial/println)
[read()](../serial/read)
[readBytes()](../serial/readbytes)
[readBytesUntil()](../serial/readbytesuntil)
[readString()](../serial/readstring)
[readStringUntil()](../serial/readstringuntil)
[setTimeout()](../serial/settimeout)
[write()](../serial/write)
[serialEvent()](../serial/serialevent)

**See also**

-   EXAMPLE
    [ReadASCIIString^](https://www.arduino.cc/en/Tutorial/ReadASCIIString)

-   EXAMPLE [ASCII
    TAble^](https://www.arduino.cc/en/Tutorial/ASCIITable)

-   EXAMPLE [Dimmer^](https://www.arduino.cc/en/Tutorial/Dimmer)

-   EXAMPLE [Graph^](https://www.arduino.cc/en/Tutorial/Graph)

-   EXAMPLE [Physical
    Pixel^](https://www.arduino.cc/en/Tutorial/PhysicalPixel)

-   EXAMPLE [Serial Call
    Response^](https://www.arduino.cc/en/Tutorial/SerialCallResponse)

-   EXAMPLE [Serial Call Response
    ASCII^](https://www.arduino.cc/en/Tutorial/SerialCallResponseASCII)

