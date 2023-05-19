---
title: "Arduino Xbee Shield"
source: "https://arduino.cc/en/Main/ArduinoXbeeShield"
---

***Note: This page refers to a product that is retired.***

## Arduino Xbee Shield

### Overview

The Xbee shield allows an Arduino board to communicate wirelessly using Zigbee. It is based on the [Xbee module from MaxStream](http://www.maxstream.net/products/xbee/xbee-oem-rf-module-zigbee.php). The module can communicate up to 100 feet indoors or 300 feet outdoors (with line-of-sight). It can be used as a serial/usb replacement or you can put it into a command mode and configure it for a variety of broadcast and mesh networking options. The shields breaks out each of the Xbee's pins to a through-hole solder pad. It also provides female pin headers for use of digital pins 2 to 7 and the analog inputs, which are covered by the shield (digital pins 8 to 13 are not obstructed by the shield, so you can use the headers on the board itself).

The Xbee shield was created in collaboration with [Libelium](http://www.libelium.com/), who developed it for use in their [SquidBee motes](http://www.libelium.com/index.php?option=com%5Fcontent&task=view&id=14&Itemid=60) (used for creating sensor networks).

### Schematic

[XbeeShieldSchematic.pdf](http://www.arduino.cc/en/uploads/Main/XbeeShieldSchematic.pdf) (Eagle schematics and board layouts available from the Libelium [SquidBee wiki download page](http://www.libelium.com/squidbee/index.php?title=Downloads).)

### Jumper Settings

The Xbee shield has two jumpers (the small removable plastic sleeves that each fit onto two of the three pins labelled Xbee/USB). These determine how the Xbee's serial communication connects to the serial communication between the microcontroller (ATmega8 or ATmega168) and FTDI USB-to-serial chip on the Arduino board. 

With the jumpers in the **Xbee** position (i.e. on the two pins towards the interior of the board), the DOUT pin of the Xbee module is connected to the RX pin of the microcontroller; and DIN is connected to TX. Note that the RX and TX pins of the microcontroller are still connected to the TX and RX pins (respectively) of the FTDI chip - data sent from the microcontroller will be transmitted to the computer via USB as well as being sent wirelessly by the Xbee module. The microcontroller, however, will only be able to receive data from the Xbee module, not over USB from the computer. 

With the jumpers in the **USB** position (i.e. on the two pins nearest the edge of the board), the DOUT pin the Xbee module is connected to the RX pin of the *FTDI chip*, and DIN on the Xbee module is connected to the TX pin of the FTDI chip. This means that the Xbee module can communicate directly with the computer - however, *this only works if the microcontroller has been removed from the Arduino board*. If the microcontroller is left in the Arduino board, it will be able to talk to the computer normally via USB, but neither the computer nor the microcontroller will be able to talk to the Xbee module.

### Networking

The Arduino XBee shield can be used with different XBee modules. The instructions below are for the **XBee 802.15.4 modules** (sometimes called "Series 1" to distinguish them from the Series 2 modules, although "Series 1" doesn't appear in the official name or product description).

#### Addressing

There are multiple parameters that need to be configured correctly for two modules to talk to each other (although with the default settings, all modules should be able to talk to each other). They need to be on the same network, as set by the **ID** parameter (see "Configuration" below for more details on the parameters). The modules need to be on the same channel, as set by the **CH** parameter. Finally, a module's destination address (**DH** and **DL** parameters) determine which modules on its network and channel will receive the data it transmits. This can happen in a few ways:

* If a module's **DH** is 0 and its **DL** is less than 0xFFFF (i.e. 16 bits), data transmitted by that module will be received by any module whose 16-bit address **MY** parameter equals **DL**.
* If **DH** is 0 and **DL** equals 0xFFFF, the module's transmissions will be received by all modules.
* If **DH** is non-zero or **DL** is greater than 0xFFFF, the transmission will only be received by the module whose serial number equals the transmitting module's destination address (i.e. whose **SH** equals the transmitting module's **DH** and whose **SL** equals its **DL**).

Again, this address matching will only happen between modules on the same network and channel. If two modules are on different networks or channels, they can't communicate regardless of their addresses.

#### Configuration

Here are some of the more useful parameters for configuring your Xbee module. For step-by-step instructions on reading and writing them, see the guide to the Xbee shield below. Make sure to prepend `AT` to the parameter name when sending a command to the module (e.g. to read the `ID` parameter, you should send the command `ATID`).

|||||
|-|-|-|-|
|*Command* |*Description* |*Valid Values* |*Default Value* |
|`ID`|The network ID of the Xbee module. |0 - 0xFFFF|3332|
|`CH` |The channel of the Xbee module. |0x0B - 0x1A|0X0C|
|`SH` and `SL` |The serial number of the Xbee module (`SH` gives the high 32 bits, `SL` the low 32 bits). Read-only.| 0 - 0xFFFFFFFF (for both `SH` and `SL`)|different for each module|
|`MY` | The 16-bit address of the module.| 0 - 0xFFFF| 0|
|`DH` and `DL` | The destination address for wireless communication (`DH` is the high 32 bits, `DL` the low 32). | 0 - 0xFFFFFFFF (for both `DH` and `DL`)| 0 (for both `DH` and `DL`)|
|`BD` |The baud rate used for serial communication with the Arduino board or computer. | 0 (1200 bps), 1 (2400 bps), 2 (4800 bps), 3 (9600 bps), 4 (19200 bps), 5 (38400 bps), 6 (57600 bps), 7 (115200 bps) | 3 (9600 baud)|

Note: although the valid and default values in the table above are written with a prefix of "0x" (to indicate that they are hexadecimal numbers), the module will not include the "0x" when reporting the value of a parameter, and you should omit it when setting values.

Here are a couple more useful commands for configuring the Xbee module (you'll need to prepend `AT` to these too).

|||
|-|-|
|*Command*|*Description*|
|`RE`| Restore factory default settings (note that like parameter changes, this is not permanent unless followed by the `WR` command).|
|`WR`| Write newly configured parameter values to non-volatile (long-term) storage. Otherwise, they will only last until the module loses power.|
|`CN`| Exit command mode now. (If you don't send any commands to the module for a few seconds, command mode will timeout and exit even without a `CN` command.)|

---

## Guide to Arduino Xbee Shield

The Arduino Xbee shield allows your Arduino board to communicate wirelessly using Zigbee. It was developed in collaboration with [Libelium](http://www.libelium.com/). This documentation describes the use of the shield with the XBee 802.15.4 module (sometimes called "Series 1" to distinguish them from the Series 2 modules, although "Series 1" doesn't appear in the official name or product description). For the XBee ZNet 2.5 ("Series 2") modules, see [this configuration guide](http://www.humboldt.edu/~cm19/XBee%20setup.pdf).

### A Simple Example

You should be able to get two Arduino boards with Xbee shields talking to each other without any configuration, using just the standard Arduino serial commands (described in the [reference](//www.arduino.cc/en/Reference/HomePage)). 

To upload a sketch to an Arduino board with a Xbee shield, you'll need to put both jumpers on the shield to the "USB" setting (i.e. place them on the two pins closest to the edge of the board) or remove them completely (but be sure not to lose them!). Then, you can upload a sketch normally from the Arduino environment. In this case, upload the **Communication | Physical Pixel** sketch to one of the boards. This sketch instructs the board to turn on the LED attached to pin 13 whenever it receives an 'H' over its serial connection, and turn the LED off when it gets an 'L'. You can test it by connecting to the board with the Arduino serial monitor (be sure it's set at 9600 baud), typing an H, and pressing enter (or clicking send). The LED should turn on. Send an L and the LED should turn off. If nothing happens, you may have an Arduino board that doesn't have a built-in LED on pin 13, in this case you'll need to supply your own.

Once you've uploaded the Physical Pixel sketch and made sure that it's working, unplug the first Arduino board from the computer. Switch the jumpers to the Xbee setting (i.e. place each on the center pin and the pin farthest from the edge of the board). Now, you need to upload a sketch to the other board. Make sure its jumpers are in the USB setting. Then upload the following sketch to the board:

```arduino
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  Serial.print('H');
  delay(1000);
  Serial.print('L');
  delay(1000);
}
```

When it's finished uploading, you can check that it's working with the Arduino serial monitor. You should see H's and L's arriving one a second. Turn off the serial monitor and unplug the board. Switch the jumpers to the Xbee setting. Now connect both boards to the computer. After a few seconds, you should see the LED on the first board turn on and off, once a second. (This is the LED on the Arduino board itself, not the one on the Xbee shield, which conveys information about the state of the Xbee module.) If so, congratulations, your Arduino boards are communicating wirelessly. This may not seem that exciting when both boards are connected to the same computer, but if you connect them to different computers (or power them with an external power supply - being sure to switch the power jumper on the Arduino board), they should still be able to communicate. 

### A Few Notes

You can use any of the standard Arduino serial commands with the Xbee shield. With the shield's jumpers in the Xbee position, the print and println commands will send data over the Xbee shield and the USB connection (i.e. to other Xbee shields and to the computer at the same time). In this configuration, however, the board will only receive data from the Xbee shield not from the USB connection (you'll need to switch the jumpers to allow the board to receive data from the computer). 

The Xbee module on the shield is set up to work at 9600 baud by default, so unless you reconfigure it, you'll need to make sure you're passing 9600 to the Serial.begin() command in your sketch.

To allow your computer to communicate directly with the Xbee shield, connect it to an Arduino board whose microcontroller has been removed and place its jumpers in the USB configuration. Then you can send data to and receive data from the Xbee module from any terminal program. This allows you, for example, to see the data that the module is receiving from other Xbee shields (e.g. to collect sensor data wirelessly from a number of locations).

### Configuring the Xbee Module

You can configure the Xbee module from code running on the Arduino board or from software on the computer. To configure it from the Arduino board, you'll need to have the jumpers in the Xbee position. To configure it from the computer, you'll need to have the jumpers in the USB configuration and have removed the microcontroller from your Arduino board. 

To get the module into configuration mode, you need to send it three plus signs: +++ and there needs to be at least one second before and after during which you send no other character to the module. Note that this includes newlines or carriage return characters. Thus, if you're trying to configure the module from the computer, you need to make sure your terminal software is configured to send characters as you type them, without waiting for you to press enter. Otherwise, it will send the plus signs immediately followed by a newline (i.e. you won't get the needed one second delay after the +++). If you successfully enter configuration mode, the module will send back the two characters 'OK', followed by a carriage return.

Send Command

`+++` 

Expected Response 

`OK` *CR* 

Once in configuration mode, you can send AT commands to the module. Command strings have the form ATxx (where xx is the name of a setting). To read the current value of the setting, send the command string followed by a carriage return. To write a new value to the setting, send the command string, immediately followed by the new setting (with no spaces or newlines in-between), followed by a carriage return. For example, to read the network ID of the module (which determines which other Xbee modules it will communicate with), use the *'ATID* command:

 Send Command

 Expected Response 

`ATID` *enter* 

`3332` *CR* 

To change the network ID of the module:

 Send Command

 Expected Response 

`ATID3331` *enter* 

`OK` *CR* 

Now, check that the setting has taken effect:

 Send Command

 Expected Response 

`ATID` *enter* 

`3331` *CR* 

Unless you tell the module to write the changes to non-volatile (long-term) memory, they will only be in effect until the module loses power. To save the changes permanently (until you explicitly modify them again), use the **ATWR** command:

 Send Command

 Expected Response 

`ATWR` *enter* 

`OK` *CR* 

To reset the module to the factory settings, use the **ATRE** command:

 Send Command

 Expected Response 

`ATRE` *enter* 

`OK` *CR* 

Note that like the other commands, the reset will not be permanent unless you follow it with the **ATWR** comamand.

### References

For more information, see: the [hardware page](//www.arduino.cc/en/Main/ArduinoXbeeShield) for the Xbee shield, the [Libelium SquidBee wiki](http://www.squidbee.org/), and the [MaxStream Xbee page](http://www.maxstream.net/products/xbee/xbee-oem-rf-module-zigbee.php). The text of the Arduino getting started guide is licensed under a[Creative Commons Attribution-ShareAlike 3.0 License](http://creativecommons.org/licenses/by-sa/3.0/). Code samples in the guide are released into the public domain.