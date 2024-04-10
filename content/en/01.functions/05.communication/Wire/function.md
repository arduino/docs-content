---
title: Wire
categories: "Functions"
subCategories: "Communication"
---

**Description**

This library allows you to communicate with I2C devices, a feature that
is present on all Arduino boards. I2C is a very common protocol,
primarly used for reading/sending data to/from external I2C components.
To learn more, visit [this article for Arduino &
I2C](https://docs.arduino.cc/learn/communication/wire).

Due to the hardware design and various architectural differences, the
I2C pins are located in different places. The pin map just below
highlights the default pins, as well as additional ports available on
certain boards.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr class="odd">
<td style="text-align: left;"><p>Board</p></td>
<td style="text-align: left;"><p>I2C Default</p></td>
<td style="text-align: left;"><p>I2C1</p></td>
<td style="text-align: left;"><p>I2C2</p></td>
<td style="text-align: left;"><p>Notes</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>UNO R3, UNO R3 SMD, UNO Mini
Ltd</p></td>
<td style="text-align: left;"><p>A4(SDA), A5(SCL)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>I2C also available on the SDA / SCL
pins (digital header).</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>UNO R4 Minima, UNO R4 WiFi</p></td>
<td style="text-align: left;"><p>A4(SDA), A5(SCL)</p></td>
<td style="text-align: left;"><p>Qwiic: D27(SDA), D26(SCL)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>I2C also available on the SDA / SCL
pins (digital header).</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>UNO WiFi Rev2, Zero</p></td>
<td style="text-align: left;"><p>20(SDA), 21(SCL)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Leonardo, Micro, Yùn Rev2</p></td>
<td style="text-align: left;"><p>D2(SDA), D3(SCL)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Nano boards</p></td>
<td style="text-align: left;"><p>A4(SDA), A5(SCL)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>MKR boards</p></td>
<td style="text-align: left;"><p>D11(SDA), D12(SCL)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>GIGA R1 WiFi</p></td>
<td style="text-align: left;"><p>20(SDA), 21(SCL)</p></td>
<td style="text-align: left;"><p>D102(SDA1), D101 (SCL1)</p></td>
<td style="text-align: left;"><p>D9(SDA2), D8 (SCL2)</p></td>
<td style="text-align: left;"><p>Use <code>Wire1.begin()</code> for
I2C1, and <code>Wire2.begin()</code> for I2C2.</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Due</p></td>
<td style="text-align: left;"><p>20(SDA), 21(SCL)</p></td>
<td style="text-align: left;"><p>D70(SDA1), D71(SCL1)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>Use <code>Wire1.begin()</code> for
I2C1</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Mega 2560 Rev3</p></td>
<td style="text-align: left;"><p>D20(SDA), D21(SCL)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

This library inherits from the Stream functions, making it consistent
with other read/write libraries. Because of this, `send()` and
`receive()` have been replaced with `read()` and `write()`.

Recent versions of the Wire library can use timeouts to prevent a lockup
in the face of certain problems on the bus, but this is not enabled by
default (yet) in current versions. It is recommended to always enable
these timeouts when using the Wire library. See the Wire.setWireTimeout
function for more details.

**Note:** There are both 7 and 8-bit versions of I2C addresses. 7 bits
identify the device, and the eighth bit determines if it’s being written
to or read from. The Wire library uses 7 bit addresses throughout. If
you have a datasheet or sample code that uses 8-bit address, you’ll want
to drop the low bit (i.e. shift the value one bit to the right),
yielding an address between 0 and 127. However the addresses from 0 to 7
are not used because are reserved so the first address that can be used
is 8. Please note that a pull-up resistor is needed when connecting
SDA/SCL pins. Please refer to the examples for more information. MEGA
2560 board has pull-up resistors on pins 20 and 21 onboard.

**The Wire library implementation uses a 32 byte buffer, therefore any
communication should be within this limit. Exceeding bytes in a single
transmission will just be dropped.**

To use this library:

`#include <Wire.h>`

**Functions**

[begin()](../wire/begin)
[end()](../wire/end)
[requestFrom()](../wire/requestfrom)
[beginTransmission()](../wire/begintransmission)
[endTransmission()](../wire/endtransmission)
[write()](../wire/write)
[available()](../wire/available)
[read()](../wire/read)
[setClock()](../wire/setclock)
[onReceive()](../wire/onreceive)
[onRequest()](../wire/onrequest)
[setWireTimeout()](../wire/setwiretimeout)
[clearWireTimeoutFlag()](../wire/clearwiretimeoutflag)
[getWireTimeoutFlag()](../wire/getwiretimeoutflag)

