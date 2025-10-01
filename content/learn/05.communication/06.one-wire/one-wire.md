---
title: "1-Wire Protocol"
description: "Learn about the communication between devices or sensors using the OneWire protocol."
source: "https://playground.arduino.cc/Learning/OneWire/"
author: "Arduino Community"
---

> This article was revised on 2022/09/28 by Hannes Siebeneicher.

***Controller/peripheral is formerly known as master/slave. Arduino no longer supports the use of this terminology. Devices formerly known as master are referred to as controller and devices formerly known as slaves are referred to as peripheral.***

1-Wire communication is a protocol operating through one wire between the controller device and the peripheral device. This article covers the basics of using the 1-Wire protocol with an Arduino with the help of the [OneWire](https://www.arduino.cc/reference/en/libraries/onewire/) library. The following sections provide information about the 1-Wire protocol, interface, power, addressing devices, reading devices and finally a short glimpse into the library's history.

## Latest version

The [latest version of the library](https://github.com/PaulStoffregen/OneWire) is on [Paul Stoffregen's](https://www.pjrc.com/teensy/td%5Flibs%5FOneWire.html) site.

OneWire is currently maintained by Paul Stoffregen. If you find a bug or have an improvement (to the library), email paul@pjrc.com. Please be sure you are using the latest version of OneWire.

[Bus](https://github.com/alexandrecuer/Bus) is a subclass of the OneWire library. Bus class scans the 1-Wire Bus connected to an analog pin and stores the ROMs in an array. Several methods are available in the Bus class to acquire data from different 1-Wire sensors (DS18B20, DS2438).

## The 1-Wire Protocol

Dallas Semiconductor (now Maxim) produces a family of devices that are controlled through a proprietary 1-Wire protocol. There are no fees for programmers using the Dallas 1-Wire (trademark) drivers.

On a 1-Wire network, which Dallas has dubbed a "MicroLan" (trademark), a single controller device communicates with one or more 1-Wire peripheral devices over a single data line, which can also be used to provide power to the peripheral devices. (Devices drawing power from the 1-wire bus are said to be operating in _parasitic power_ mode.) Tom Boyd's [guide to 1-Wire](https://sheepdogguides.com/arduino/asw1onew1.htm) may tell you more than you want to know, but it may also answer questions and inspire interest.

The 1-Wire temperature sensors have become particularly popular, because they're inexpensive and easy to use, providing calibrated digital temperature readings directly. They are more tolerant of long wires between sensor and Arduino. The sample code below demonstrates how to interface with a 1-Wire device using Jim Studt's [OneWire](https://www.arduino.cc/reference/en/libraries/onewire/) Arduino library, with the DS18S20 digital thermometer as an example. Many 1-Wire chips can operate in both [parasitic and normal power modes](http://sheepdogguides.com/dst9parasitic.htm).

## 1-Wire Interfaces

### Dedicated Bus Controller

Dallas/Maxim and a number of other companies manufacture dedicated bus controller for read/write and management of 1-Wire networks. Most of these are listed here:

[http://owfs.org/index.php?page=bus-masters](https://owfs.org/index.php?page=bus-masters)

These devices are specifically designed and optimized to read and write efficiently to 1-Wire devices and networks. Similar to UART/USART controller, they handle clocked operations natively with the use of a buffer, offloading the processing load from the host processor (e.g., sensor gateway or microcontroller) thereby increasing accuracy . External pull-up resistors are also often not required.

Many of the chips provide error-handling that specifically deals with loss of signal integrity, level variation, reflections, and other bus issues that may cause problems, particularly on large networks. Many of the devices have additional features, and are offered on a large variety of interfaces. They range in price from $1 to $30.

Another key advantage is support of , a read/write file system with vast device support for 1-Wire controller that exposes many native functions for a wide variety of 1-Wire device types.

### UART/USART controller

Most UART/USARTs are perfectly capable of sustained speeds well in excess of the 15.4kbps required of the 1-Wire bus in standard mode. More important, the clock and buffering is handled separately, again offloading it from the main process of the microcontroller or main processor. This implementation is discussed here: [http://www.maximintegrated.com/en/app-notes/index.mvp/id/214](https://www.maximintegrated.com/en/app-notes/index.mvp/id/214).

### Bitbanging approaches

Where native buffering/clock management is not available, 1-Wire may be implemented on a general purpose IO (GPIO) pin, where manual toggle of the pin state is used to emulate a UART/USART with reconstruction of the signal from the received data. These are typically much less processor-efficient, and directly impact and are directly impacted by other processes on the processor shared with other system processes.

On Arduino and other compatible chips, this may be done with the [OneWire](https://www.arduino.cc/reference/en/libraries/onewire/) library.

On single-board computers such as the Raspberry Pi, 1-Wire network read is often possible using kernel drivers that offer native support. The w1-gpio, w1-gpio-therm, and w1-gpio-custom kernel mods are included in the most recent distributions of Raspbian and are quite popular, as they allow interfacing with a subset of 1-Wire device with no additional hardware. Currently, however, they have limited device support, and have bus size limitations in software.

## Powering OneWire devices

The chip can be powered two ways. One way is the "parasitic" option,meaning that only two wires need go to the chip. The other may, in some cases, give a more reliable operation (parasitic often works well), as an extra wire carrying the power for the chip is involved. For getting started, especially if your chip is within 20 feet of your Arduino, the parasitic option is probably fine. The code below works for either option.

### Parasite power mode

When operating in parasite power mode, only two wires are required: one data wire, and one ground. In this mode, the power line must be connected to ground, per the datasheet. At the controller, a **4.7k pull-up resistor** must be connected to the 1-wire bus. When the line is in a "high" state, the device pulls current to charge an internal capacitor.

This current is usually very small, but may go as high as 1.5 mA when doing a temperature conversion or writing EEPROM. When a peripheral device is performing one of these operations, the bus controller must keep the bus pulled high to provide power until the operation is complete; a delay of 750ms is required for a DS18S20 temperature conversion. The controller can't do anything during this time, like issuing commands to other devices, or polling for the peripheral's operation to be completed. To support this, the [OneWire](https://www.arduino.cc/reference/en/libraries/onewire/) library makes it possible to have the bus held high after the data is written.

### Normal (external supply) mode

With an external supply, three wires are required: the bus wire, ground, and power. **The 4.7k pull-up resistor is still required** on the bus wire. As the bus is free for data transfer, the microcontroller can continually poll the state of a device doing a conversion. This way, a conversion request can finish as soon as the device reports being done, as opposed to having to wait for conversion time (dependent on device function and resolution) in "parasite" power mode.

### Note on resistors:

**For larger networks, you can try smaller resistors.**  
The ATmega328/168 datasheet indicates starting at 1k6 and a number of users have found smaller to work better on larger networks.

## Addressing a 1-Wire device

Each 1-Wire device contains a unique 64-bit 'ROM' address, consisting of an 8-bit family code, a 48-bit serial number, and an 8-bit CRC. The CRC is used to verify the integrity of the data. For example, the sample code, below, checks if the device being addressed is a DS18S20 temperature sensor by checking for its family code, 0x10\. To use the sample code with the newer DS18B20 sensor, you would check for a family code of 0x28, instead, and for the DS1822 you would check for 0x22.

### Single-device commands

Before sending a command to a single peripheral device, the controller must first select that device using its unique ROM. Subsequent commands will be responded to by the selected device, if found.

### Multiple-device commands

Alternatively, you can address a command to all peripheral devices by issuing a 'Skip ROM' command (0xCC), instead. It is important to consider the effects of issuing a command to multiple devices. Sometimes, this may be intended and beneficial. For example, issuing a Skip ROM followed by a convert T (0x44) would instruct all networked devices that have a Convert T command to perform a temperature conversion. This can be a time-saving and efficient way of performing the operations. On the other hand, issuing a Read Scratchpad (0xBE) command would cause all devices to report Scratchpad data simultaneously. Power consumption of all devices (for example, during a temperature conversion) is also important when using a Skip ROM command sequence.

## Reading a 1-Wire device

Reading a 1-Wire device requires multiple steps. The details are device-dependent, in that devices are capable of reporting different measurables. The popular DS18B20, for example, reads and reports temperature, while a DS2438 reads voltage, current, and temperature.

### Two Main Read Process Steps:

**Conversion**  
A command is issued to the device to perform an internal conversion operation. With a DS18B20, this is the Convert T (0x44) byte command. In the OneWire library, this is issued as ds.write(0x44), where ds is an instance of the OneWire class. After this command is issued, the device reads the internal ADC, and when this process is complete, it copies the data into the Scratchpad registers. The length of this conversion process varies depending on the resolution and is listed in the device datasheet. a DS18B20 takes from 94 (9-bit resolution) to 750ms (12-bit resolution) to convert temperature. While the conversion is taking place, the device may be polled, e.g. using in the ds.read() command in OneWire, to see if it has successfully performed a conversion.

**Read Scratchpad**  
Once the data has been converted, it is copied into the Scratchpad memory, where it may be read. Note that the Scratchpad may be read at any time without a conversion command to recall the most previous reading, as well as the resolution of the device and other device-dependent configuration options.

### Asynchronous vs. Synchronous read/write

The majority of existing code for 1-Wire devices, particularly that written for Arduino, uses a very basic "Convert, Wait, Read" algorithm, even for multiple devices. This creates several problems:

**Program timing for other functions**  
Arguably the biggest problem with using the above methodology is that unless threading measures are undertaken, the device must sit (hang) and wait for the conversion to take place if a hardcoded wait time is included. This presents a serious problem if other timed processes exist, and even if they don't -- many programs wait for user input, process data, and perform many other functions that cannot be put on hold for the time necessary for a temperature conversion process. As noted, a 12-bit conversion process for a DS18B20 can take as long as 750ms. There is no reason to use the wait method, unless it is desired that the controller does nothing (at all) until the measurement conversion is complete. It is far more efficient to issue a conversion command and return later to pick up the measurement with a Read Scratchpad command once the conversion is complete.

**Scaling for Poll Speed with multiple devices**  
Another major problem with the "Convert, Wait, Read" method is that it scales very poorly, and for no good reason. All conversion commands can be issued in series (or simultaneously) by issuing a Skip ROM and then converting the command so the result can then be read back in succession. See discussion here: [http://interfaceinnovations.org/onewireoptimization.html](https://interfaceinnovations.org/onewireoptimization.html).

**Adjustment of wait time to required conversion time**  
The most efficient and expeditious read of 1-Wire devices explicitly takes the conversion time of the device being read into account, which is typically a function of read resolution. In the example below, for example, 1000ms is given, while the datasheet lists 750ms as the maximum conversion time, and typical conversion takes place in 625ms or less. Most important, the value should be adjusted for the resolution that is currently being polled. A 9-bit conversion, for example, will take 94ms or less, and waiting for 1000ms simply does not make sense. As noted above, the most efficient way to poll is the use a read time slot to poll the device. This way one can know exactly when the result is ready and pick it up immediately.

## History

In 2007, Jim Studt created the original OneWire library that makes it easy to work with 1-Wire devices. Jim's original version only worked with arduino-007 and required a large (256-byte) lookup table to perform CRC calculations. This was later [updated](https://www.elsewhere.org/onewire/) to work with arduino-0008 and later releases. The most recent version eliminates the CRC lookup table and has been tested under arduino-0010.

The OneWire library had a bug causing an infinite loop when using the search function but [Version 2.0](https://www.pjrc.com/teensy/td%5Flibs%5FOneWire.html) merges Robin James's improved search function and includes Paul Stoffregen's improved I/O routines (fixes occasional communication errors), and also has several small optimizations.

Version 2.1 added compatibility with Arduino 1.0-beta and an improved temperature example (Paul Stoffregen), DS250x PROM example (Guillermo Lovato), chipKit compatibility (Jason Dangel), CRC16, convenience functions and DS2408 example (Glenn Trewitt).

Miles Burton derived its [Dallas Temperature Control Library](https://milesburton.com/index.php?title=Dallas%5FTemperature%5FControl%5FLibrary) from it as well.

## Example code

```
#include <OneWire.h>


// DS18S20 Temperature chip i/o

OneWire ds(10);  // on pin 10


void setup(void) {

  // initialize inputs/outputs

  // start serial port

  Serial.begin(9600);

}


void loop(void) {

  byte i;

  byte present = 0;

  byte data[12];

  byte addr[8];


  ds.reset_search();

  if ( !ds.search(addr)) {

    Serial.print("No more addresses.\n");

    ds.reset_search();

    return;

  }


  Serial.print("R=");

  for( i = 0; i < 8; i++) {

    Serial.print(addr[i], HEX);

    Serial.print(" ");

  }


  if ( OneWire::crc8( addr, 7) != addr[7]) {

      Serial.print("CRC is not valid!\n");

      return;

  }


  if ( addr[0] == 0x10) {

    Serial.print("Device is a DS18S20 family device.\n");

  }

  else if ( addr[0] == 0x28) {

    Serial.print("Device is a DS18B20 family device.\n");

  }

  else {

    Serial.print("Device family is not recognized: 0x");

    Serial.println(addr[0],HEX);

    return;

  }


  ds.reset();

  ds.select(addr);

  ds.write(0x44,1); // start conversion, with parasite power on at the end


  delay(1000);  // maybe 750ms is enough, maybe not

  // we might do a ds.depower() here, but the reset will take care of it.


  present = ds.reset();

  ds.select(addr);

  ds.write(0xBE); // Read Scratchpad


  Serial.print("P=");

  Serial.print(present,HEX);

  Serial.print(" ");

  for ( i = 0; i < 9; i++) {  // we need 9 bytes

    data[i] = ds.read();

    Serial.print(data[i], HEX);

    Serial.print(" ");

  }

  Serial.print(" CRC=");

  Serial.print( OneWire::crc8( data, 8), HEX);

  Serial.println();

}
```

### Converting HEX to something meaningful (Temperature)

In order to convert the HEX code to a temperature value, first you need to identify if you are using a DS18S20, or DS18B20 series sensor. The code to read the temperature needs to be slightly different for the DS18B20 (and DS1822), because it returns a 12-bit temperature value (0.0625 deg precision), while the DS18S20 and DS1820 return 9-bit values (0.5 deg precision).

First, you need to define some variables, (put right under loop() above)

```
int HighByte, LowByte, TReading, SignBit, Tc_100, Whole, Fract;
```

Then for a DS18B20 series you will need to add the following code below the **Serial.println();**

```
LowByte = data[0];

  HighByte = data[1];

  TReading = (HighByte << 8) + LowByte;

  SignBit = TReading & 0x8000;  // test most sig bit

  if (SignBit) // negative

  {

    TReading = (TReading ^ 0xffff) + 1; // 2's comp

  }

  Tc_100 = (6 * TReading) + TReading / 4; // multiply by (100 * 0.0625) or 6.25


  Whole = Tc_100 / 100; // separate off the whole and fractional portions

  Fract = Tc_100 % 100;


  if (SignBit) // If its negative

  {

    Serial.print("-");

  }

  Serial.print(Whole);

  Serial.print(".");

  if (Fract < 10)

  {

    Serial.print("0");

  }

  Serial.print(Fract);


  Serial.print("\n");
```

This block of code converts the temperature to deg C and prints it to the Serial output.

### A Code Snippet for the DS 1820 with 0.5 Degree Resolution

The example shown above works only for the B-type of the DS1820. Below is a code example that works with the lower resolution DS1820 and with multiple sensors displaying their values on a LCD. The example is working with Arduino pin 9\. Feel free to change that to an appropriate pin for your use. Pin 1 and 3 of the DS1820 have to be connected to ground! In the example a 5k resistor is connected from pin 2 of DS1820 to Vcc (+5V). See LiquidCrystal documentation for connecting the LCD to the Arduino.

```
#include <OneWire.h>

#include <LiquidCrystal.h>

// LCD=======================================================

//initialize the library with the numbers of the interface pins

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

#define LCD_WIDTH 20

#define LCD_HEIGHT 2


/* DS18S20 Temperature chip i/o */


OneWire ds(9);  // on pin 9

#define MAX_DS1820_SENSORS 2

byte addr[MAX_DS1820_SENSORS][8];

void setup(void)

{

  lcd.begin(LCD_WIDTH, LCD_HEIGHT,1);

  lcd.setCursor(0,0);

  lcd.print("DS1820 Test");

  if (!ds.search(addr[0]))

  {

    lcd.setCursor(0,0);

    lcd.print("No more addresses.");

    ds.reset_search();

    delay(250);

    return;

  }

  if ( !ds.search(addr[1]))

  {

    lcd.setCursor(0,0);

    lcd.print("No more addresses.");

    ds.reset_search();

    delay(250);

    return;

  }

}

int HighByte, LowByte, TReading, SignBit, Tc_100, Whole, Fract;

char buf[20];


void loop(void)

{

  byte i, sensor;

  byte present = 0;

  byte data[12];


  for (sensor=0;sensor<MAX_DS1820_SENSORS;sensor++)

  {

    if ( OneWire::crc8( addr[sensor], 7) != addr[sensor][7])

    {

      lcd.setCursor(0,0);

      lcd.print("CRC is not valid");

      return;

    }


    if ( addr[sensor][0] != 0x10)

    {

      lcd.setCursor(0,0);

      lcd.print("Device is not a DS18S20 family device.");

      return;

    }


    ds.reset();

    ds.select(addr[sensor]);

    ds.write(0x44,1); // start conversion, with parasite power on at the end


    delay(1000);  // maybe 750ms is enough, maybe not

    // we might do a ds.depower() here, but the reset will take care of it.


    present = ds.reset();

    ds.select(addr[sensor]);

    ds.write(0xBE); // Read Scratchpad


    for ( i = 0; i < 9; i++)

    { // we need 9 bytes

      data[i] = ds.read();

    }


    LowByte = data[0];

    HighByte = data[1];

    TReading = (HighByte << 8) + LowByte;

    SignBit = TReading & 0x8000;  // test most sig bit

    if (SignBit) // negative

    {

      TReading = (TReading ^ 0xffff) + 1; // 2's comp

    }

    Tc_100 = (TReading*100/2);


    Whole = Tc_100 / 100; // separate off the whole and fractional portions

    Fract = Tc_100 % 100;


    sprintf(buf, "%d:%c%d.%d\337C     ",sensor,SignBit ? '-' : '+', Whole, Fract < 10 ? 0 : Fract);


    lcd.setCursor(0,sensor%LCD_HEIGHT);

    lcd.print(buf);

  }

}
```
