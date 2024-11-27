---
title: 'Arduino GIGA R1 Cheat Sheet'
description: 'Learn how to set up the GIGA R1, get a quick overview of the components, information regarding pins and how to use different Serial (SPI, I2C, UART), and much, much more.'
tags:
  - Installation
  - I2C
  - SPI
  - UART
  - JTAG
  - CAN
  - DAC
  - MIPI
  - USBHost
  - Arducam
  - Audio Jack
author: 'Jacob Hylén'
hardware:
  - hardware/10.mega/boards/giga-r1-wifi
software:
  - ide-v1
  - ide-v2
  - web-editor
---

The **Arduino GIGA R1** is one of our most feature-packed Arduino boards to date, supported by the same powerful, ML-capable, dual-core microcontroller found in the Pro family's Portenta H7. It features support for display connectors, USB-host, an Audio Jack, an Arducam connector, a CAN bus, 4 UART Serial Ports, 2 I2C buses, dedicated DAC Pins, and much, much more. 

This article is a collection of resources and guides to make use of every great feature of this powerful hardware.

You can also visit the documentation platform for the [GIGA R1](/hardware/giga-r1-wifi).

## Datasheet

The full datasheet is available as a downloadable PDF from the link below:

- [Download the GIGA R1 datasheet](/resources/datasheets/ABX00063-datasheet.pdf)

## Arduino Cloud

The GIGA R1 WiFi is compatible with the [Arduino Cloud](https://create.arduino.cc/iot/things), a Cloud service that allows you to create IoT applications in just minutes.

***Visit the [Getting Started with Arduino Cloud](/arduino-cloud/getting-started/iot-cloud-getting-started) guide for more information.***

## Power Supply

To power the **GIGA R1** you may either use a USB-C cable, or the VIN pin. 

If you're using the USB-C connector you must power it with 5V.

Powering the board with the VIN pin gives you more options, as you can safely power the board with any voltage between 6-24V.

By connecting the OFF pin to GND you can cut the power supply to the board, turning it off completely. Read more about this feature in the [OFF-pin](#off-pin) section of this article

It should however be noted that the internal operating voltage of the microcontroller is 3.3V, and you should not apply voltages higher than that to the GPIO pins.

## Installation

***For detailed instructions on how to install the GIGA R1 Board Package, please refer to the [Getting Started with GIGA R1](/tutorials/giga-r1-wifi/giga-getting-started) guide.***

The **GIGA R1** can be programmed through:

- The **Classic Arduino IDE 1.8.X**, 
- the **Arduino IDE 2**, 
- and the Web-editor. 

## Board Package

The GIGA R1 is based on the [Arduino Mbed OS GIGA Board Package](/tutorials/giga-r1-wifi/giga-getting-started), which also provides a set of examples that works out of the box.

These examples are available in the Arduino IDE via **File > Examples > Examples for Arduino GIGA R1**.

### Mbed OS

As the [Arduino Mbed OS GIGA Board Package](/tutorials/giga-r1-wifi/giga-getting-started) is based on [MbedOS](https://os.mbed.com/), it is possible for the operating system to crash while running a sketch. 

On most Arduino boards, when a sketch fails due to e.g. memory shortage, the board resets.

On the GIGA R1, whenever the MbedOS fails, the board does **not reset automatically**. Instead, if it fails, the onboard red LED will start to blink in a looping pattern of 4 fast blinks and 4 slow blinks.

***Please note, the red LED does NOT mean your board is broken or bricked.***

![Red LED blinking due to MbedOS crashing.](assets/red_led_blink.gif)

In case you encounter the red LED, you can either:
- Press the reset button **once** (this resets the sketch).
- **Double-tap** the reset button to enter bootloader mode (allowing you to re-program the board).

## Boot0

Pressing and holding the button labelled `BOOT0` on the board while powering the board will boot it into DFU-mode (Device Firmware Update), letting you reflash the bootloader without the use of external hardware, if you were to ever need to. 

![BOOT0 button](assets/BOOT0.png)

The state of this button can also be read from a sketch while it is running, giving you a basic interactive component without needing to do any wiring.

To read the state of the Boot0 button in your sketch, you use this line of code:

```arduino
digitalRead(PC_13);
```

## STM32H747XI Microcontroller

The GIGA R1 features the powerful dual core **STM32H747XI** microcontroller found on the Arduino PRO family's Portenta H7 board, but in a form factor accessible to any maker who has tinkered with an Arduino board before. 

The **STM32H747XI** is a powerful dual core chip, capable of being programmed with a high-level language such as MicroPython on one core, while simultaneously running Arduino compiled code on the other, and having the two programs communicate with each other seamlessly.

![Microcontroller on the GIGA R1](assets/STM32H747XI.png)

The microcontroller operates on a voltage of 3.3V, applying a higher voltage than that, such as 5V, to a pin might damage the microcontroller.

## Memory

### RAM

The **GIGA R1** has 1 MB of SRAM that is internal to the processor, and 8MB of SDRAM which you can access and write to. 

To access the SDRAM you need to use the SDRAM library, include it in your sketch with:

```arduino
#include "SDRAM.h"
```

Before writing to the SDRAM, you need to allocate it, the following code will create an array that reserves 7MB of the SDRAM for you to write to.
```arduino
 uint8_t* myVeryBigArray = (uint8_t*)SDRAM.malloc(7 * 1024 * 1024);
```
If you now store any data in this array, it will be written to SDRAM.
```arduino
for (int i = 0; i<128; i++) {
        myVeryBigArray[i] = i;
    }
```

When you no longer need to use the SDRAM, you can free it, so it can be used for other things.

```arduino
SDRAM.free(myVeryBigArray);
```


### Flash

The **GIGA R1** has 2MB of internal, and 16MB of external Flash storage.
The external Flash storage on the **GIGA R1** is QSPI and can be accessed and used to store data. If you need to, you can configure the board to act as a USB flash drive, so you can store files such as images, audio, and more.

The GIGA firmware has full support for FATFS and littleFS.

To access the QSPI flash storage as a USB flash drive, you need to follow a few steps, first you need to update the WiFi modules firmware, then you need to create partitions on the flash storage, before finally exposing the partitions to be detected by a computer. These three steps are broken down into different built in example sketches that conveniently all come with the GIGA Board Package.

Firstly, navigate in the IDE menu to `File > Examples > STM32H747_System > WiFiFirmwareUpdater` and upload the sketch to your board. 

In the Serial monitor you will now be able to interface with the board. Follow the instructions by sending a "**y**" in the monitor. You will now see the progress of the firmware update, don't power off the board until you see a message telling you that it is safe.

After completing this, the next step is to partition the flash storage. Navigate to `File > Examples > STM32H747_System > QSPIFormat` and upload the sketch. From here, your interaction with the board will be very similar to when you updated the WiFi firmware. In the serial monitor, you will get the option to choose from two partition schemes. For this purpose, partition scheme 1 is good. Again, send "**y**" in the serial monitor and wait for confirmation before powering the board off. 

Lastly, navigate to `File > Examples > USB Mass Storage > AccessFlashAsUSBDisk` and upload the sketch. 

Once this is completed, you should now see a new storage device connected as a portable storage device in your computer.

This can be very useful, as this flash storage **does not get deleted when you upload a new sketch to the board.** Meaning that you can store files on the board, and then upload a new sketch that can access and use those files without the need for an SD card and card reader.

***Note: In this configuration, the USB serial port used for serial communication with the computer is occupied, so you won't be able to send or read information in the serial monitor. **This includes uploading new sketches. To upload a new sketch you need to put the GIGA R1 in DFU mode by double pressing the RST button.***

## Radio Module

![Murata LBEE5KL1DX-883 radio module + antenna connector.](assets/wifi.png)

The Wi-Fi® / Bluetooth® module onboard the GIGA R1 WiFi is the Murata LBEE5KL1DX-883. This module does not come with a built-in antenna, but an external antenna is included when purchasing the board.

The antenna connector (see image above) is located right next to the USB-C connector, and is of a **U.FL.** type.

### Wi-Fi®

Wi-Fi® on the GIGA R1 WiFi is supported via the `WiFi` library. This library is included in the core, so it is automatically installed when installing the Board Package.

To use the Wi-Fi® features on this board, please refer to the [GIGA R1 WiFi Network Examples](/tutorials/giga-r1-wifi/giga-wifi) guide.

***The easiest way to connect your board to the Internet is via the [Arduino Cloud](https://create.arduino.cc/iot/) platform. Here you can configure, program, monitor and synchronize your devices without having to write any networking code.*** 

### Bluetooth® Low Energy

To use the BLE features on this board, refer to the [ArduinoBLE library documentation](https://reference.arduino.cc/reference/en/libraries/arduinoble/).

## Ethernet

If you want to add Ethernet connectivity to your project, the [Arduino Ethernet Shield Rev2](/hardware/ethernet-shield-rev2) is compatible. In the shield's documentation, you will find a series of examples.

## Audio Jack

The **GIGA R1** features an audio jack, with 2x DAC channels, and 1x ADC channel, and is capable of reading input from a microphone, as well as outputting sound through a speaker. 

![Audio jack.](assets/audio-jack.png)

The audio jack is connected to the following pins:
- **A12 / DAC0**
- **A13 / DAC1**
- **A7**

Both of these come with caveats, though. As there is no amplifier circuit on the board itself, driving a high impedance speaker directly without an amplifier circuit could cause damage to the board, and microphone input without an amplifier circuit between the microphone and the board may sound dim.

In the coming sections we will provide resources and basic information on how to use the audio jack as both an input and an output. 

### DAC Output

In order to output audio from the DAC, you can use the `AdvancedAnalogRedux` library from Arduino. You will need to connect a speaker to your board either through the audio jack or the DAC pins.

Include the library and create the `AdvancedDAC` object, such as the `dac1(A12)`, with the following code in the beginning of your sketch, outside of the `void setup()` function:

```arduino
#include "AdvancedDAC.h"

AdvancedDAC dac1(A12);
```

To initialize the library, and check that everything went as expected with the following piece of code:

```arduino
 if (!dac1.begin(AN_RESOLUTION_12, 8000, 32, 64)) {
        Serial.println("Failed to start DAC!");
        while (1);
    }
```

Then lastly, add the following code to `void loop()` to start:
```arduino
if (dac1.available()) {

        // Get a free buffer for writing
        SampleBuffer buf = dac1.dequeue();

        // Write data to buffer
        for (int i=0; i<buf.size(); i++) {
            buf.data()[i] =  (i % 2 == 0) ? 0: 0xfff;
        }

        // Write the buffer data to DAC
        dac1.write(buf);
    }
```

***The options for audio playback and generation on your GIGA R1 are **much** more vast than this, however. To learn about audio playback in depth, check out the [GIGA R1 Audio Guide](/tutorials/giga-r1-wifi/giga-audio).***

### ADC Input

The audio jack on the GIGA R1 is also connected to pin A7, for microphone capabilities. 

To take advantage of this, you can use the `AdvancedAnalogRedux` library from Arduino, start off by including the library and setting up the pin as an `AdvancedADC` pin in the beginning of your sketch, outside of `void setup()`.

```arduino
#include "AdvancedADC.h"

AdvancedADC adc1(A7);
```

Now, initialize the library and run a check to make sure everything went as expected with the following code within `void setup()`:
```arduino

  Serial.begin(9600);

  // Resolution, sample rate, number of samples per channel, and queue depth of the ADC
   if (!adc1.begin(AN_RESOLUTION_16, 16000, 32, 64)) {
       Serial.println("Failed to start analog acquisition!");
       while (1);
   }
```
Finally, read the ADC, and store it in a way that you can use it, do this within `void loop()`:
```arduino
  if (adc1.available()) {
        SampleBuffer buf = adc1.read();

        // Print first sample
        Serial.println(buf[0]);

        // Release the buffer to return it to the pool
        buf.release();
```

***The options for audio input on your GIGA R1 are **much** more vast than this, however. To learn about audio recording in depth, check out the [GIGA R1 Audio Guide](/tutorials/giga-r1-wifi/giga-audio).***

## MIPI DSI®

Display Serial Interface (DSI), is a specification from the Mobile Industry Processor Interface (MIPI).

The **STM32H747XI** has an internal 2D graphics accelerator with support for resolutions up to 1024x768, it also has the ability to encode and decode JPEG codec. This is what allows the **GIGA R1** to boast a 2 lane MIPI display interface. 

The [GIGA Display Shield]() is designed to be mounted on the GIGA R1 through the MIPI/DSI connector located on the board, with support for popular frameworks such as [LVGL](https://docs.arduino.cc/tutorials/giga-display-shield/lvgl-guide) and [GFX](https://docs.arduino.cc/tutorials/giga-display-shield/gfx-guide).

The pinout for the display connector is shown in the image below:

![MIPI/DSI connector.](assets/mipi-dsi.png)

***When connecting a module or shield to the GIGA R1 WiFi board, be careful to not connect it at an angle or your board may be damaged.***

The following pins are directly connected to the STM32H747XI and cannot be used as GPIOs.
- D1N
- D1P
- CKN
- CKP
- D0N
- D0P

The following pins can also be used as GPIOs:
- D68
- D69
- D70
- D71
- D72
- D73
- D74
- D75

The connector also has a series of power connections, including:
- 3.3 V
- 5 V
- GND
- VIN

## USB Features

***To learn about all the USB features in more detail, visit the [Guide to GIGA R1 USB Features](/tutorials/giga-r1-wifi/giga-usb).***

### USB HID

The GIGA R1 comes with support for HID, and can be used as either a keyboard or mouse. For more information, visit the [USB HID section](/tutorials/giga-r1-wifi/giga-usb#usb-hid).

### USBHost

![USB-A connector.](assets/usb.png)

The USB-A port you find on the **GIGA R1** is configured as a host-only port, meaning that it cannot be used to program the board, instead it is used to connect peripherals to the board. 

The board can receive keyboard input, effectively enabling a few hundred more inputs without any wiring, or be used to read & write files on a USB flash drive, which makes it possible to for example, build a [datalogger](/tutorials/giga-r1-wifi/giga-usb#datalogger-example).

For more information, go to the following sections:
- [USBHost Keyboard](/tutorials/giga-r1-wifi/giga-usb#usb-host-keyboard).
- [USB mass storage](/tutorials/giga-r1-wifi/giga-usb#usb-mass-storage).

## RTC

### RTC Manual Example

The following sketch will continuously print the time in the Serial monitor.

```arduino
#include "mbed.h"
#include <mbed_mktime.h>

constexpr unsigned long printInterval { 1000 };
unsigned long printNow {};

void setup() {
  Serial.begin(9600);
  RTCset();
}

void loop() {
      if (millis() > printNow) {
        Serial.print("System Clock:          ");
        Serial.println(getLocaltime());
        printNow = millis() + printInterval;
    }
}

void RTCset()  // Set cpu RTC
{    
  tm t;
            t.tm_sec = (0);       // 0-59
            t.tm_min = (52);        // 0-59
            t.tm_hour = (14);         // 0-23
            t.tm_mday = (18);   // 1-31
            t.tm_mon = (11);       // 0-11  "0" = Jan, -1 
            t.tm_year = ((22)+100);   // year since 1900,  current year + 100 + 1900 = correct year
            set_time(mktime(&t));       // set RTC clock                                 
}

String getLocaltime()
{
    char buffer[32];
    tm t;
    _rtc_localtime(time(NULL), &t, RTC_4_YEAR_LEAP_YEAR_SUPPORT);
    strftime(buffer, 32, "%Y-%m-%d %k:%M:%S", &t);
    return String(buffer);
}
```

To get accurate time, you'll want to change the values in `void RTCset()` to whatever time it is when you're starting this clock. As long as the VRTC pin is connected to power, the clock will keep ticking and time will be kept accurately.

### RTC / UDP / NTP Example

With the following sketch, you can automatically set the time by requesting the time from a Network Time Protocol (NTP), using the UDP protocol.

```arduino
/*
 Udp NTP Client

 Get the time from a Network Time Protocol (NTP) time server
 Demonstrates use of UDP sendPacket and ReceivePacket
 For more on NTP time servers and the messages needed to communicate with them,
 see http://en.wikipedia.org/wiki/Network_Time_Protocol

 created 4 Sep 2010
 by Michael Margolis
 modified 9 Apr 2012
 by Tom Igoe
 modified 28 Dec 2022
 by Giampaolo Mancini

This code is in the public domain.
 */

#include <WiFi.h>
#include <WiFiUdp.h>
#include <mbed_mktime.h>

int status = WL_IDLE_STATUS;
#include "arduino_secrets.h"
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = ""; // your network SSID (name)
char pass[] = ""; // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0; // your network key index number (needed only for WEP)

unsigned int localPort = 2390; // local port to listen for UDP packets

// IPAddress timeServer(162, 159, 200, 123); // pool.ntp.org NTP server

constexpr auto timeServer { "pool.ntp.org" };

const int NTP_PACKET_SIZE = 48; // NTP timestamp is in the first 48 bytes of the message

byte packetBuffer[NTP_PACKET_SIZE]; // buffer to hold incoming and outgoing packets

// A UDP instance to let us send and receive packets over UDP
WiFiUDP Udp;

constexpr unsigned long printInterval { 1000 };
unsigned long printNow {};

void setup()
{
    // Open serial communications and wait for port to open:
    Serial.begin(9600);
    while (!Serial) {
        ; // wait for serial port to connect. Needed for native USB port only
    }

    // check for the WiFi module:
    if (WiFi.status() == WL_NO_SHIELD) {
        Serial.println("Communication with WiFi module failed!");
        // don't continue
        while (true)
            ;
    }

    // attempt to connect to WiFi network:
    while (status != WL_CONNECTED) {
        Serial.print("Attempting to connect to SSID: ");
        Serial.println(ssid);
        // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
        status = WiFi.begin(ssid, pass);

        // wait 10 seconds for connection:
        delay(10000);
    }

    Serial.println("Connected to WiFi");
    printWifiStatus();

    setNtpTime();

}

void loop()
{
    if (millis() > printNow) {
        Serial.print("System Clock:          ");
        Serial.println(getLocaltime());
        printNow = millis() + printInterval;
    }
}

void setNtpTime()
{
    Udp.begin(localPort);
    sendNTPpacket(timeServer);
    delay(1000);
    parseNtpPacket();
}

// send an NTP request to the time server at the given address
unsigned long sendNTPpacket(const char * address)
{
    memset(packetBuffer, 0, NTP_PACKET_SIZE);
    packetBuffer[0] = 0b11100011; // LI, Version, Mode
    packetBuffer[1] = 0; // Stratum, or type of clock
    packetBuffer[2] = 6; // Polling Interval
    packetBuffer[3] = 0xEC; // Peer Clock Precision
    // 8 bytes of zero for Root Delay & Root Dispersion
    packetBuffer[12] = 49;
    packetBuffer[13] = 0x4E;
    packetBuffer[14] = 49;
    packetBuffer[15] = 52;

    Udp.beginPacket(address, 123); // NTP requests are to port 123
    Udp.write(packetBuffer, NTP_PACKET_SIZE);
    Udp.endPacket();
}

unsigned long parseNtpPacket()
{
    if (!Udp.parsePacket())
        return 0;

    Udp.read(packetBuffer, NTP_PACKET_SIZE);
    const unsigned long highWord = word(packetBuffer[40], packetBuffer[41]);
    const unsigned long lowWord = word(packetBuffer[42], packetBuffer[43]);
    const unsigned long secsSince1900 = highWord << 16 | lowWord;
    constexpr unsigned long seventyYears = 2208988800UL;
    const unsigned long epoch = secsSince1900 - seventyYears;
    set_time(epoch);

#if defined(VERBOSE)
    Serial.print("Seconds since Jan 1 1900 = ");
    Serial.println(secsSince1900);

    // now convert NTP time into everyday time:
    Serial.print("Unix time = ");
    // print Unix time:
    Serial.println(epoch);

    // print the hour, minute and second:
    Serial.print("The UTC time is "); // UTC is the time at Greenwich Meridian (GMT)
    Serial.print((epoch % 86400L) / 3600); // print the hour (86400 equals secs per day)
    Serial.print(':');
    if (((epoch % 3600) / 60) < 10) {
        // In the first 10 minutes of each hour, we'll want a leading '0'
        Serial.print('0');
    }
    Serial.print((epoch % 3600) / 60); // print the minute (3600 equals secs per minute)
    Serial.print(':');
    if ((epoch % 60) < 10) {
        // In the first 10 seconds of each minute, we'll want a leading '0'
        Serial.print('0');
    }
    Serial.println(epoch % 60); // print the second
#endif

    return epoch;
}

String getLocaltime()
{
    char buffer[32];
    tm t;
    _rtc_localtime(time(NULL), &t, RTC_FULL_LEAP_YEAR_SUPPORT);
    strftime(buffer, 32, "%Y-%m-%d %k:%M:%S", &t);
    return String(buffer);
}

void printWifiStatus()
{
    // print the SSID of the network you're attached to:
    Serial.print("SSID: ");
    Serial.println(WiFi.SSID());

    // print your board's IP address:
    IPAddress ip = WiFi.localIP();
    Serial.print("IP Address: ");
    Serial.println(ip);

    // print the received signal strength:
    long rssi = WiFi.RSSI();
    Serial.print("signal strength (RSSI):");
    Serial.print(rssi);
    Serial.println(" dBm");
}
```
### RTC / UDP / NTP Example (Timezone)

This example provides an option to set the timezone. As the received epoch is based on GMT time, you can input e.g. `-1` or `5` which represents the hours. The `timezone` variable is changed at the top of the example.

```arduino
/*
 Udp NTP Client with Timezone Adjustment

 Get the time from a Network Time Protocol (NTP) time server
 Demonstrates use of UDP sendPacket and ReceivePacket
 For more on NTP time servers and the messages needed to communicate with them,
 see http://en.wikipedia.org/wiki/Network_Time_Protocol

 created 4 Sep 2010
 by Michael Margolis
 modified 9 Apr 2012
 by Tom Igoe
 modified 28 Dec 2022
 by Giampaolo Mancini
 modified 29 Jan 2024
 by Karl Söderby

This code is in the public domain.
 */

#include <WiFi.h>
#include <WiFiUdp.h>
#include <mbed_mktime.h>

int timezone = -1; //this is GMT -1. 

int status = WL_IDLE_STATUS;

char ssid[] = "Flen";        // your network SSID (name)
char pass[] = "";  // your network password (use for WPA, or use as key for WEP)

int keyIndex = 0;  // your network key index number (needed only for WEP)

unsigned int localPort = 2390;  // local port to listen for UDP packets

// IPAddress timeServer(162, 159, 200, 123); // pool.ntp.org NTP server

constexpr auto timeServer{ "pool.ntp.org" };

const int NTP_PACKET_SIZE = 48;  // NTP timestamp is in the first 48 bytes of the message

byte packetBuffer[NTP_PACKET_SIZE];  // buffer to hold incoming and outgoing packets

// A UDP instance to let us send and receive packets over UDP
WiFiUDP Udp;

constexpr unsigned long printInterval{ 1000 };
unsigned long printNow{};

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ;  // wait for serial port to connect. Needed for native USB port only
  }

  // check for the WiFi module:
  if (WiFi.status() == WL_NO_SHIELD) {
    Serial.println("Communication with WiFi module failed!");
    // don't continue
    while (true)
      ;
  }

  // attempt to connect to WiFi network:
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:
    delay(10000);
  }

  Serial.println("Connected to WiFi");
  printWifiStatus();

  setNtpTime();
}

void loop() {
  if (millis() > printNow) {
    Serial.print("System Clock:          ");
    Serial.println(getLocaltime());
    printNow = millis() + printInterval;
  }
}

void setNtpTime() {
  Udp.begin(localPort);
  sendNTPpacket(timeServer);
  delay(1000);
  parseNtpPacket();
}

// send an NTP request to the time server at the given address
unsigned long sendNTPpacket(const char* address) {
  memset(packetBuffer, 0, NTP_PACKET_SIZE);
  packetBuffer[0] = 0b11100011;  // LI, Version, Mode
  packetBuffer[1] = 0;           // Stratum, or type of clock
  packetBuffer[2] = 6;           // Polling Interval
  packetBuffer[3] = 0xEC;        // Peer Clock Precision
  // 8 bytes of zero for Root Delay & Root Dispersion
  packetBuffer[12] = 49;
  packetBuffer[13] = 0x4E;
  packetBuffer[14] = 49;
  packetBuffer[15] = 52;

  Udp.beginPacket(address, 123);  // NTP requests are to port 123
  Udp.write(packetBuffer, NTP_PACKET_SIZE);
  Udp.endPacket();
}

unsigned long parseNtpPacket() {
  if (!Udp.parsePacket())
    return 0;

  Udp.read(packetBuffer, NTP_PACKET_SIZE);
  const unsigned long highWord = word(packetBuffer[40], packetBuffer[41]);
  const unsigned long lowWord = word(packetBuffer[42], packetBuffer[43]);
  const unsigned long secsSince1900 = highWord << 16 | lowWord;
  constexpr unsigned long seventyYears = 2208988800UL;
  const unsigned long epoch = secsSince1900 - seventyYears;
  
  const unsigned long new_epoch = epoch + (3600 * timezone); //multiply the timezone with 3600 (1 hour)

  set_time(new_epoch);

#if defined(VERBOSE)
  Serial.print("Seconds since Jan 1 1900 = ");
  Serial.println(secsSince1900);

  // now convert NTP time into everyday time:
  Serial.print("Unix time = ");
  // print Unix time:
  Serial.println(epoch);

  // print the hour, minute and second:
  Serial.print("The UTC time is ");       // UTC is the time at Greenwich Meridian (GMT)
  Serial.print((epoch % 86400L) / 3600);  // print the hour (86400 equals secs per day)
  Serial.print(':');
  if (((epoch % 3600) / 60) < 10) {
    // In the first 10 minutes of each hour, we'll want a leading '0'
    Serial.print('0');
  }
  Serial.print((epoch % 3600) / 60);  // print the minute (3600 equals secs per minute)
  Serial.print(':');
  if ((epoch % 60) < 10) {
    // In the first 10 seconds of each minute, we'll want a leading '0'
    Serial.print('0');
  }
  Serial.println(epoch % 60);  // print the second
#endif

  return epoch;
}

String getLocaltime() {
  char buffer[32];
  tm t;
  _rtc_localtime(time(NULL), &t, RTC_FULL_LEAP_YEAR_SUPPORT);
  strftime(buffer, 32, "%Y-%m-%d %k:%M:%S", &t);
  return String(buffer);
}

void printWifiStatus() {
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your board's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}
```

### VRTC Pin

The GIGA R1 also features a `VRTC` pin, giving you the ability to power the RTC with a coin cell battery to keep the time even when your board is turned off, for low power timekeeping. 

![VRTC pin on the GIGA R1](./assets/rtc.png)

## Camera Interface

The Arduino GIGA features an onboard Arducam compatible connector.

To learn more about the camera capabilities of the GIGA R1, check out the [GIGA R1 Camera Guide](/tutorials/giga-r1-wifi/giga-camera)

## JTAG

The **GIGA R1** features a 2x5 pin JTAG (Joint Test Action Group) connector, giving advanced debug functionalities for more advanced users. 

![JTAG Connector](assets/jtag.png)

## CAN Bus

The **GIGA R1** features a dedicated CAN bus. 

![CAN Bus](assets/canpins.png)

***The CAN bus does not include a built in transceiver. If you need to use the CAN bus, you can add a transceiver as a breakout board.***

CAN, or **Controller Area Network**, is a communication standard that allows microcontroller-based devices to communicate with each other without the need for a host computer. This means that building a complex system with many different subsystems within becomes much easier. 

This makes the **GIGA R1** a powerful option for complex multilayered systems, as it can be integrated into existing systems or be used to build a new one from scratch. 

The CAN pins on the **GIGA R1** are labelled `CANRX` and `CANTX`. Typically, transceiver breakouts are labelled with a similar syntax, and to connect them to the board, use the following wiring scheme:

| GIGA R1 | Transceiver |
| ------- | ----------- |
| VCC     | 3.3V        |
| GND     | GND         |
| CANTX   | CANTX\*     |
| CANRX   | CANRX\*     |

***\*The name of CANTX/CANRX differs from product to product.***

Below is an example of how to send & receive data using a CAN bus.

```arduino
#include "CAN.h"

mbed::CAN can1(PB_5, PB_13);
uint8_t counter = 0;

void send() {
  Serial.println("send()");
  if (can1.write(mbed::CANMessage(1337, &counter, 1))) {
    Serial.println("wloop()");
    counter++;
    Serial.print("Message sent: ");
    Serial.println(counter);
  } else {
    Serial.println("Transmission error");
    Serial.println(can1.tderror());
    can1.reset();
  }
}

void receive() {
  mbed::CANMessage msg;
  if (can1.read(msg)) {
    Serial.print("Message received: ");
    Serial.println(msg.data[0]);
  }
}


void setup() {
  Serial.begin(115200);
  can1.frequency(1000000);
}

bool receiver = false;
void loop() {
  if (receiver) {
    receive();
  } else {
    send();
  }
  delay(1000);
}
```

## SPI 

![SPI Pins](assets/spipins.png)

The **GIGA R1** features two separate SPI (Serial Peripheral Interface) buses, one is configured on the 6 pin header (ICSP) labelled SPI, and the other is broken out into pin connections on the board.

The first bus which has a dedicated SPI header, `SPI1`, uses the following pins:

- (CIPO) - D89
- (COPI) - D90
- (SCK) - D91
- (CS) - unassigned, use any free GPIO for this.
  
***Please note that the SPI header provides a 5 V pin. Make sure that the SPI device you are connecting supports an input voltage of 5 V. If you have an SPI device that supports 3.3 V only, use the `SPI5` port (see below).***

The second bus (header), `SPI5`, uses the following pins: 

- (CIPO) - D12
- (COPI) - D11
- (SCK) - D13
- (CS) - D10

For using both SPI buses simultaneously, check out the following example:

```arduino
#include <SPI.h>

const int CS_1 = 10;
const int CS_2 = 5;

void setup() {
  pinMode(CS_1, OUTPUT);
  pinMode(CS_2, OUTPUT);

  SPI.begin();
  SPI1.begin();

  digitalWrite(CS_1, LOW);
  digitalWrite(CS_2, LOW);

  SPI.transfer(0x00);
  SPI1.transfer(0x00);
  
  digitalWrite(CS_1, HIGH);
  digitalWrite(CS_2, HIGH);
}

void loop() {
}
```

Please note that the in the GIGA R1 schematics and the code does not match exactly. In the schematics, you will notice that `SPI` is `SPI1` and `SPI1` is `SPI5`.

![SPI ports in the schematics.](assets/schematics-spi.png)


## I2C Pins

I2C lets you connect multiple I2C compatible devices in series using only two pins. The controller will send out information through the I2C bus to a 7 bit address, meaning that the technical limit of I2C devices on a single line is 128. Practically, you're never gonna reach 128 devices before other limitations kick in.

The **GIGA R1** has three separate I2C buses of which two are usable without external components, letting you control more devices.

The pins used for I2C on the **GIGA R1** are the following:
- SDA - D20
- SCL - D21
- SDA1 - also available on the camera connector.
- SCL1 - also available on the camera connector.
- SDA2 - D9
- SCL2 - D8

![I2C Pins](assets/i2cpins.png)

To connect I2C devices you will need to include the [Wire](https://www.arduino.cc/reference/en/language/functions/communication/wire/) library at the top of your sketch.

```arduino
#include <Wire.h>
```

Inside `void setup()` you need to initialize the library, and initialize the I2C port you want to use.

```arduino
Wire.begin() //SDA & SDL
Wire1.begin(); //SDA1 & SDL1
Wire2.begin(); //SDA2 & SDL2
```

And to write something to a device connected via I2C, we can use the following commands:

```arduino
Wire.beginTransmission(1); //begin transmit to device 1
Wire.write(byte(0x00)); //send instruction byte 
Wire.write(val); //send a value
Wire.endTransmission(); //stop transmit
```

If you pay close attention you may notice that there are three sets of I2C pins. The two first sets (SDA, SCL, SDA1, SCL1) have internal pullup resistors connected to them which are required to make them function as I2C pins. 

If you want to use the third set (SDA2, SCL2) as I2C pins you will need to use external pull-up resistors.

## Serial/UART Pins

The **GIGA R1** supports, like every other Arduino board, serial communication with UART (Universal Asynchronous, Receiver-Transmitter). However, the **GIGA R1** board features 5 separate serial ports, including the standard serial over USB port that is initialized using `Serial.begin()`. 

This not only means that you may print different values to different ports and monitor them separately, which is useful enough in and of itself, but that you may also communicate with **4 different serial enabled devices** simultaneously. 

The pins used for UART on the **GIGA R1** are the following:

- RX0 - D0
- TX0 - D1
- RX1 - D19
- TX1 - D18
- RX2 - 17
- TX2 - 16
- RX3 - 15
- TX3 - 14

Each Serial port works in the same way as the one you're used to, but you use different functions to target them:

```arduino
Serial.begin(9600); //initialize serial communication over USB
Serial1.begin(9600); //initialize serial communication on RX0/TX0
Serial2.begin(9600); //initialize serial communication on RX1/TX1
Serial3.begin(9600); //initialize serial communication on RX2/TX2
Serial4.begin(9600); //initialize serial communication on RX3/TX3
```

To send and receive data through UART, we will first need to set the baud rate inside `void setup()`. In this example, we use RX0/TX0.

```arduino
Serial1.begin(9600);
```

To read incoming data, we can use a while loop() to read each individual character and add it to a string.

```arduino
  while(Serial1.available()){
    delay(2);
    char c = Serial1.read();
    incoming += c;
  }
```

And to write something, we can use the following command:

```arduino
Serial1.write("Hello world!");
```

## Pins

The **GIGA R1** gives you access to more pins than any other Arduino board that is this accessible for makers. Many of them have special features that will be accounted for in the upcoming sections of this article. Keep reading to learn what you can do with them.

If you just need a quick overview of the pins functionality, this is a full table of all the IO pins on the **GIGA R1**

| Pin       | Function        | Notes                                   |
| --------- | --------------- | --------------------------------------- |
| D0        | TX              | Serial communication                    |
| D1        | RX              | Serial communication                    |
| D2        | PWM             | PWM, Digital IO pin                     |
| D3        | PWM             | PWM, Digital IO pin                     |
| D4        | PWM             | PWM, Digital IO pin                     |
| D5        | PWM             | PWM, Digital IO pin                     |
| D6        | PWM             | PWM, Digital IO pin                     |
| D7        | PWM             | PWM, Digital IO pin                     |
| D8        | PWM/SCL2        | PWM, Digital IO, I2C                    |
| D9        | PWM/SDA2        | PWM, Digital IO, I2C                    |
| D10       | PWM/CS          | PWM, Digital IO, SPI                    |
| D11       | PWM/COPI        | PWM, Digital IO, SPI                    |
| D12       | PWM/CIPO        | PWM, Digital IO, SPI                    |
| D13       | PWM/SCK         | PWM, Digital IO, SPI                    |
| D14       | TX3             | Serial communication                    |
| D15       | RX3             | Serial communication                    |
| D16       | TX2             | Serial communication                    |
| D17       | RX2             | Serial communication                    |
| D18       | TX1             | Serial communication                    |
| D19       | RX1             | Serial communication                    |
| D20       | SDA             | Digital IO, I2C                         |
| D21       | SCL             | Digital IO, I2C                         |
| D22       | GPIO            | Digital IO pin                          |
| D23       | GPIO            | Digital IO pin                          |
| D24       | GPIO            | Digital IO pin                          |
| D25       | GPIO            | Digital IO pin                          |
| D26       | GPIO            | Digital IO pin                          |
| D27       | GPIO            | Digital IO pin                          |
| D28       | GPIO            | Digital IO pin                          |
| D29       | GPIO            | Digital IO pin                          |
| D30       | GPIO            | Digital IO pin                          |
| D31       | GPIO            | Digital IO pin                          |
| D32       | GPIO            | Digital IO pin                          |
| D33       | GPIO            | Digital IO pin                          |
| D34       | GPIO            | Digital IO pin                          |
| D35       | GPIO            | Digital IO pin                          |
| D36       | GPIO            | Digital IO pin                          |
| D37       | GPIO            | Digital IO pin                          |
| D38       | GPIO            | Digital IO pin                          |
| D39       | GPIO            | Digital IO pin                          |
| D40       | GPIO            | Digital IO pin                          |
| D41       | GPIO            | Digital IO pin                          |
| D42       | GPIO            | Digital IO pin                          |
| D43       | GPIO            | Digital IO pin                          |
| D44       | GPIO            | Digital IO pin                          |
| D45       | GPIO            | Digital IO pin                          |
| D46       | GPIO            | Digital IO pin                          |
| D47       | GPIO            | Digital IO pin                          |
| D48       | GPIO            | Digital IO pin                          |
| D49       | GPIO            | Digital IO pin                          |
| D50       | GPIO            | Digital IO pin                          |
| D51       | GPIO            | Digital IO pin                          |
| D52       | GPIO            | Digital IO pin                          |
| D53       | GPIO            | Digital IO pin                          |
| D54       | GPIO            | Digital IO pin                          |
| D55       | GPIO            | Digital IO pin                          |
| D56       | GPIO            | Digital IO pin                          |
| D57       | GPIO            | Digital IO pin                          |
| D58       | GPIO            | Digital IO pin                          |
| D59       | GPIO            | Digital IO pin                          |
| D60       | GPIO            | Digital IO pin                          |
| D61       | GPIO            | Digital IO pin                          |
| D62       | GPIO            | Digital IO pin                          |
| D63       | GPIO            | Digital IO pin                          |
| D64       | GPIO            | Digital IO pin                          |
| D65       | GPIO            | Digital IO pin                          |
| D66       | GPIO            | Digital IO pin                          |
| D67       | GPIO            | Digital IO pin                          |
| D68       | GPIO            | Digital IO pin                          |
| D69       | GPIO            | Digital IO pin                          |
| D70       | GPIO            | Digital IO pin                          |
| D71       | GPIO            | Digital IO pin                          |
| D72       | GPIO            | Digital IO pin                          |
| D73       | GPIO            | Digital IO pin                          |
| D74       | GPIO            | Digital IO pin                          |
| D75       | GPIO            | Digital IO pin                          |
| A0 / D76  | Analog in       | Analog In                               |
| A1 / D77  | Analog in       | Analog In                               |
| A2 / D78  | Analog in       | Analog In                               |
| A3 / D79  | Analog in       | Analog In                               |
| A4 / D80  | Analog in       | Analog In                               |
| A5 / D81  | Analog in       | Analog In                               |
| A6 / D82  | Analog in       | Analog In                               |
| A7 / D83  | Analog in       | Analog In                               |
| A8        | Analog in       | Analog In                               |
| A9        | Analog in       | Analog In                               |
| A10       | Analog in       | Analog In                               |
| A11       | Analog in       | Analog In                               |
| A12 / D84 | DAC0            | Analog In, DAC                          |
| A13 / D85 | DAC1            | Analog In, DAC                          |
| D86       | RGB (red)       | Only RGB, not accessible as GPIO        |
| D87       | RGB (green)     | Only RGB, not accessible as GPIO        |
| D88       | RGB (blue)      | Only RGB, not accessible as GPIO        |
| D89       | SPI1 (CIPO)     | SPI connector                           |
| D90       | SPI1 (COPI)     | SPI connector                           |
| D91       | SPI1 (SCK)      | SPI connector                           |
| D92       | USB Host Enable | USB-A connector, not accessible as GPIO |
| D93       | CANRX           | Digital IO pin, CAN                     |
| D94       | CANTX           | Digital IO pin, CAN                     |

### Analog Pins

The **GIGA R1** has 12 analog input pins that can be read with a resolution of 16 Bits, by using the `analogRead()` function.

```arduino
value = analogRead(pin, value);
```

The reference voltage of these pins is 3.3V. 

Pins A8, A9, A10 and A11 can not be used as GPIOs, but are limited to use as analog input pins.

The **STM32H7** has an internal OPAMP and comparator that are exposed on the **GIGA R1** as follows:

| Pin | OPAMP              | Comparator |
| --- | ------------------ | ---------- |
| A0  | OPAMP1_VOUT        | COMP1_INM  |
| A1  | OPAMP1_VINM &VINM0 |            |
| A2  | OPAMP1_VINP        | COMP1_INP  |
| A3  |                    | COMP1_INM  |
| A6  |                    | COMP1_INM  |

***For more advanced analog readings, you can use the `AdvancedAnalogRedux` library. Read more about this in the [Advanced ADC section](/tutorials/giga-r1-wifi/giga-audio#analog-to-digital-converters).***


### PWM Pins

PWM (Pulse Width Modulation) capability allows a digital pin to emulate analog output by flickering on and off very fast letting you, among other things, dim LEDs connected to digital pins. 

The **GIGA R1** has 12 PWM capable pins, the PWM capable pins are 2-13. You may use them as analog output pins with the function: 

```arduino
analogWrite(pin, value);
```

### Digital Pins

The **GIGA R1** features more pins than any other Arduino board for makers, a full 76 digital pins. Though many of them serve another purpose and shouldn't be used for GPIO if you have other pins available.

- 0 - RX0
- 1 - TX0
- 8 - SCL2
- 9 - SDA2
- 10 - CS
- 11 - COPI
- 12 - CIPO
- 13 - SCK 
- 14 - TX3
- 15 - RX3
- 16 - TX2
- 17 - RX2
- 18 - TX1
- 19 - RX1
- 20 - SDA
- 21 - SCL

The reference voltage of all digital pins is 3.3V.

The logic for `LED_BUILTIN` is reversed if compared to the behavior of, for example, the **Arduino UNO** board. What this means is that if you write HIGH to `LED_BUILTIN`, the LED will turn off, and on respectively if you write LOW.

#### D7 Pin

By default, the digital pin 7 (D7) provides a voltage of ~1.65 V. 

To disable this pin, you need to configure it as an output and set it to a `LOW` state.

```arduino
pinMode(7, OUTPUT);
digitalWrite(7, LOW);
```

### DAC Pins

The **GIGA R1** also has two DAC pins, A12 & A13, that can act as genuine analog output pins which means they are even more capable than PWM pins.
```arduino
analogWrite(pin, value);
```

![DAC Pins](assets/audio-jack.png)

These DAC pins have a default write resolution of 8-bits. This means that values that are written to the pin should be between 0-255.

However you may change this write resolution if you need to, to up to 12-bits:

```arduino
analogWriteResolution(12);
```

***For advanced usage of the DAC, you can use the `AdvancedAnalogRedux` library. Read more about this in the [Advanced DAC section](/tutorials/giga-r1-wifi/giga-audio#digital-to-analog-converters).***

### OFF Pin

On the **GIGA R1** you will find a pin labelled **"OFF"**. If you connect this pin to ground, the board will power down even if power is supplied to the board.

You can install a flip-switch to the board to let you turn your device on and off easily, which can be a handy option for a more permanent fixture. 

## Interrupts 

If you're creating a project that relies heavily on accurate sensor data, and therefore need to ensure that you read the record any change in value, it can be difficult to write a program that does anything else well. This is because the microcontroller is busy trying to read the values constantly. To get around this you can use interrupts that can let you can be useful for reading input from for example a rotary encoder or a push button without putting any code in your loop function. 

This feature might be extra valuable to the maker with an **GIGA R1**, as their circuit gets more and more complex.

All GPIO pins on the **GIGA R1** can be used for interrupts. 

The syntax for creating an interrupt function should be included in `void setup()` and is as follows:
```arduino
attachInterrupt(digitalPinToInterrupt(pin), ISR, mode)
```

- `pin` represents the pin number of the pin your input sensor is connected to, 
- `ISR` is the function that is called whenever the interrupt is triggered, and should be defined bt you somewhere in your sketch.
- `mode` defines when the interrupt should be triggered, and can be one of four pre-defined modes.

The different modes that can be used are: 
- `LOW` triggers the interrupt when the pin is low.
- `CHANGE` triggers whenever the pin changes values.
- `RISING` triggers when the pin goes from low to high. 
- `FALLING` triggers when the pin goes from high to low.

This example sketch will turn on or off an LED connected to pin 13 whenever a pushbutton connected to pin 2 is pressed or released:

```arduino
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
```
