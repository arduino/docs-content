---
title: SPI
categories: "Functions"
subCategories: "Communication"
---

**Description**

This library allows you to communicate with SPI devices, with the
Arduino as the controller device. This library is bundled with every
Arduino platform (avr, megaavr, mbed, samd, sam, arc32), so **you do not
need to install** the library separately.

To use this library

`#include <SPI.h>`

To read more about Arduino and SPI, you can visit the [Arduino & Serial
Peripheral Interface
(SPI)](https://docs.arduino.cc/learn/communication/spi) guide.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td style="text-align: left;"><p>Boards</p></td>
<td style="text-align: left;"><p>Default SPI Pins</p></td>
<td style="text-align: left;"><p>Additonal SPI Pins</p></td>
<td style="text-align: left;"><p>Notes</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>UNO R3, UNO R3 SMD, UNO WiFi Rev2, UNO
Mini Ltd</p></td>
<td style="text-align: left;"><p>10(CS), 11(COPI), 12(CIPO),
13(SCK)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>SPI pins available on ICSP
header</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>UNO R4 Minima, UNO R4 WiFi</p></td>
<td style="text-align: left;"><p>10(CS), 11(COPI), 12(CIPO),
13(SCK)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>SPI pins available on ICSP
header</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Leonardo, Yún Rev2, Zero</p></td>
<td style="text-align: left;"><p>10(CS), 11(COPI), 12(CIPO),
13(SCK)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>SPI pins available on ICSP
header</p></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>Micro</p></td>
<td style="text-align: left;"><p>14(CIPO), 15(SCK), 16(COPI)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Nano boards</p></td>
<td style="text-align: left;"><p>11(COPI), 12(CIPO), 13(SCK)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>MKR boards</p></td>
<td style="text-align: left;"><p>8(COPI), 9(SCK), 10(CIPO)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Due</p></td>
<td style="text-align: left;"><p>74(CIPO), 75(MOSI), 76(SCK)</p></td>
<td style="text-align: left;"><p>SPI pins available on dedicated SPI
header</p></td>
<td style="text-align: left;"></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><p>GIGA R1 WiFi</p></td>
<td style="text-align: left;"><p>89(CIPO), 90(COPI), 91(SCK)</p></td>
<td style="text-align: left;"><p>12(CIPO), 11(COPI), 13(SCK),
10(CS)</p></td>
<td style="text-align: left;"><p>Note that pin 89,90,91 are located on
the SPI header</p></td>
</tr>
<tr class="even">
<td style="text-align: left;"><p>Mega 2560 Rev3</p></td>
<td style="text-align: left;"><p>50(CIPO), 51(COPI), 52(SCK),
53(CS)</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"><p>SPI pins available on ICSP
header</p></td>
</tr>
</tbody>
</table>

**Functions**

[SPISettings](../spi/spisettings)
[begin()](../spi/begin)
[beginTransaction()](../spi/begintransaction)
[endTransaction()](../spi/endtransaction)
[end()](../spi/end)
[setBitOrder()](../spi/setbitorder)
[setClockDivider()](../spi/setclockdivider)
[setDataMode()](../spi/setdatamode)
[transfer()](../spi/transfer)
[usingInterrupt()](../spi/usinginterrupt)

