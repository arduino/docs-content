---
title: 'Extended SPI Library Usage with the Arduino Due'
difficulty: advanced
description: 'The SAM3X has advanced SPI capabilities. It is possible to use these extended methods, or the AVR-based ones.'
tags: 
  - SPI
hardware:
  - hardware/02.hero/boards/due
software:
  - ide-v1
  - ide-v2
  - web-editor
author: "Arduino"
---


> These APIs should not be used in new projects. Use [SPISettings](https://www.arduino.cc/en/Reference/SPISettings) with [SPI.beginTransaction()](https://www.arduino.cc/en/Tutorial/SPITransaction) to configure SPI parameters.

On the Arduino Due, the SAM3X has advanced SPI capabilities. It is possible to use these extended methods, or the AVR-based ones.

The extended API can use pins 4, 10, and 52 for CS.

## Use

You must specify each pin you wish to use as CS for the SPI devices.

It is possible for the Due to automatically handle the chip selection between multiple devices sharing the SPI bus. Each device may have also different attributes such as speed and datamode.

If using multiple devices with different CS pins, you'll need to declare those pins in setup(). In the following example, there are two devices that share the SPI MISO, MOSI, and SCK pins. One device CS is attached to pin 4, the other to pin 10.


```arduino
void setup(){
  // initialize the bus for a device on pin 4
  SPI.begin(4);
  // initialize the bus for a device on pin 10
  SPI.begin(10);
}
```

Once a pin has been declared as a CS pin, it's possible to change its default behaviors as well. For example, if the devices run at different clock speeds, the setup() may look like this:

```arduino
void setup(){
  // initialize the bus for the device on pin 4
  SPI.begin(4);
  // Set clock divider on pin 4 to 21
  SPI.setClockDivider(4, 21);
  // initialize the bus for the device on pin 10
  SPI.begin(10);
  // Set clock divider on pin 10 to 84
  SPI.setClockDivider(10, 84);
}
```

A single byte transfer to a device on pin 4 could look like this :

```arduino
void loop(){
  byte response = SPI.transfer(4, 0xFF);
}
```

In the above, “0xFF” is sent to the SPI device on pin 4 and the data coming from MISO is saved inside the variable response. The chip selection is handled automatically by the SPI controller, the transfer command implies the following:

- Select device by setting pin 4 to LOW
- Send 0xFF through the SPI bus and return the byte received
- Deselect device by setting pin 4 to HIGH

It's possible to send more than one byte in a transaction by telling the the transfer command to not deselect the SPI device after the transfer :

```arduino
void loop(){
//transfer 0x0F to the device on pin 10, keep the chip selected
SPI.transfer(10, 0xF0, SPI_CONTINUE);
//transfer 0x00 to the device on pin 10, keep the chip selected
SPI.transfer(10, 0×00, SPI_CONTINUE);
//transfer 0x00 to the device on pin 10, store byte received in response1, keep the chip selected
byte response1 = SPI.transfer(10, 0×00, SPI_CONTINUE);
//transfer 0x00 to the device on pin 10, store byte received in response2, deselect the chip
byte response2 = SPI.transfer(10, 0×00);
}
```

The parameter SPI_CONTINUE ensures that chip selection is keep active between transfers. On the last transfer SPI_CONTINUE is not specified as it's the last byte transferred.

See the individual reference pages for [setClockDivider()](https://www.arduino.cc/en/Reference/SPISetClockDivider), [setDataMode()](https://www.arduino.cc/en/Reference/SPISetDataMode), [transfer()](https://www.arduino.cc/en/Reference/SPITransfer), [setBitOrder()](https://www.arduino.cc/en/Reference/SPISetBitOrder) for proper syntax when using the extended methods.

>NB : once SPI.begin() is called, the declared pin will not be available as a general purpose I/O pin.