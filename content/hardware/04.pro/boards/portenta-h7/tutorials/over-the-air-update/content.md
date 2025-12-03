---
title: 'Over-The-Air (OTA) Updates with the Arduino Portenta H7'
description: 'Learn how to perform an OTA update of the firmware on the Arduino Portenta H7'
difficulty: intermediate
tags: 
  - OTA
  - Over-The-Air 
  - Wi-Fi
  - Cloud
author: 'Taddy Chung, José Bagur'
libraries:
  - name: Arduino IoT Cloud
    url: https://www.arduino.cc/reference/en/libraries/arduinoiotcloud/
  - name: Arduino_Portenta_OTA
    url: https://github.com/arduino-libraries/Arduino_Portenta_OTA
hardware:
  - hardware/04.pro/boards/portenta-h7
  - hardware/04.pro/boards/portenta-h7-lite-connected
software:
  - ide-v1
  - ide-v2
  - web-editor
  - cli
---

## Overview
In this tutorial, you will learn how to use and allow firmware updates via **OTA (Over-The-Air)** with the **Arduino Portenta H7**. With this tutorial, you will be able to create a binary file to be used with the OTA feature and use the internal **QSPI** or an external **SD card** to accomplish the OTA (Over-The-Air) process.

***To proceed with OTA using an SD Card, you will need to use a carrier or shield with an SD card slot, e.g., Portenta Breakout, Portenta Max Carrier, or Portenta Vision Shield.***

## Goals

The goals of this tutorial are:

- Create an OTA file required to use the OTA (Over-The-Air) feature
- Use QSPI or SD card storage to load the firmware downloaded using the OTA feature

## Hardware and Software Needed

- [Arduino Portenta H7](https://store.arduino.cc/portenta-h7)
- Operating System: Linux, macOS, or Windows (with Python 3 installed)
- Arduino IDE 1.8.10+ or Arduino IDE 2.0+
- USB-C® cable (either USB-A to USB-C® or USB-C® to USB-C®)
- [Arduino_Portenta_OTA library](https://github.com/arduino-libraries/Arduino_Portenta_OTA)
- SD card (optional, you can use QSPI instead)
- Carrier or shield compatible with the Portenta H7 with an SD card slot (if using SD card method)

## What OTA Means

**OTA** (Over-The-Air) is a method of distributing updates wirelessly to end devices to update their firmware, configuration, or security-related protocols. The purpose of this method is to change a device's behavior or its settings for better performance, for adding new features, or to change its targeted usage.

## Instructions 

We will explain briefly the steps required to be able to use the OTA (Over-The-Air) process with Arduino Portenta H7. It will consist of firmware OTA file creation and use of the preferred storage mode (QSPI or SD card).

### Firmware OTA File Creation

You will need to create the binary file required for the OTA (Over-The-Air) process to be able use it with either storage option stated previously. For the purpose of this tutorial, you will have to use the following script to create the binary file. 

```cpp
/*
 This sketch can be used to generate an example binary that can be uploaded to Portenta via OTA.
 It needs to be used together with
  - 'OTA_Qspi_Flash.ino' if you want to use the Qspi Flash as storage system
 OR
  - 'SD_Qspi_Flash.ino' if you want to use the SD card as storage system

 Steps to test OTA on Portenta:
 1) Upload this sketch or any other sketch (this one lights up the RGB LED with different colours).
 2) In the IDE select: Sketch -> Export compiled Binary
 3) Upload the exported binary to a server
 4) Choose a storage mechanism (SD or QSPI), open the related OTA_*_Portenta.ino sketch,
    eventually update the OTA_FILE_LOCATION
 5) Upload the sketch OTA_*_Portenta.ino to perform OTA via SD or QSPI Flash
*/

void setLed(int blue, int green, int red) {
  digitalWrite(LEDB, blue);
  digitalWrite(LEDG, green);
  digitalWrite(LEDR, red);
}


void setup()
{
  pinMode(LEDB, OUTPUT);
  pinMode(LEDG, OUTPUT);
  pinMode(LEDR, OUTPUT);
}

void loop()
{ //led BLUE ON
  setLed(1, 0, 0);
  delay(1000);
  //led GREEN ON
  setLed(0, 1, 0);
  delay(1000);
  //led RED ON
  setLed(0, 0, 1);
  delay(1000);
}
```

This script will light up the RGB LED with 3 different colors in sequence. This code will need to be uploaded to the Arduino Portenta H7 first. This is to verify whether the sketch compiles and works correctly. After verifying this, in the Arduino IDE, you will search for **Sketch > Export Compiled Binary**.

![Exporting Binary for the Sketch](assets/binary_export.png)

With the binary file ready, you can now create the OTA file needed to enable the Over-The-Air process.

### Creating the OTA File

To create the OTA file, you will need a macOS, Linux, or Windows environment with Python 3 installed.

Once you have a compatible environment, you will need the tools which can be found at the following link:

***[Arduino IoT Cloud Library - Over-The-Air Tools](https://github.com/arduino-libraries/ArduinoIoTCloud/tree/master/extras/tools)***

You will have to download the library and extract it to a preferred location to be able to use the tools. Then, you will need to run the following commands in sequence in your terminal to create the OTA file.

Copy the binary file into the library tool's folder 

```bash
// Exported binary format reference: sketch.bin
cp OTA_Usage_Portenta.ino.PORTENTA_H7_M7.bin ~/Arduino/libraries/ArduinoIoTCloud/extras/tools/
```

Navigate to the tools directory

```bash
cd ~/Arduino/libraries/ArduinoIoTCloud/extras/tools
```

Encode your binary file into `OTA_Usage_Portenta.ino.PORTENTA_H7_M7.lzss` (LZSS format)

```bash
// Argument format: ./lzss.py --encode sketch.bin sketch.lzss
./lzss.py --encode OTA_Usage_Portenta.ino.PORTENTA_H7_M7.bin OTA_Usage_Portenta.ino.PORTENTA_H7_M7.lzss
```

Convert your encoded file into `.ota` format

```bash
// Argument format: ./bin2ota.py PORTENTA_H7_M7 sketch.lzss sketch.ota
./bin2ota.py PORTENTA_H7_M7 OTA_Usage_Portenta.ino.PORTENTA_H7_M7.lzss OTA_Usage_Portenta.ino.PORTENTA_H7_M7.ota
```

You can use `OTA_Usage_Portenta.ino.PORTENTA_H7_M7` as a sketch name for easier identification of the file. After this, you will have the `.ota` file of the sketch that you will use with the OTA process.

### Installing Python 3 On Linux

If you are using Linux and cannot run the **`bin2ota.py`** script, you may need to install [Python 3](https://www.python.org/) and the necessary modules. To do this, execute the following command on your **Linux terminal**:

```bash 
sudo apt install python-is-python3
```

You will also need to install the **`crccheck`** module for Python by following these instructions:

Installing pip on python:

```bash
//Necessary to install python modules:
sudo apt install python3-pip 
```

Installing the `crccheck` necessary module on python:

```bash
//Necessary to run the script:
pip install crccheck
```

Once you have completed these steps, you should be able to run the `bin2ota.py` script successfully.

### Uploading OTA File to the Internet

Now you can upload your .ota file to an online reachable location. For example, `OTA_Usage_Portenta.ino.PORTENTA_H7_M7.ota` has been uploaded to: 

https://downloads.arduino.cc/ota/OTA_Usage_Portenta.ino.PORTENTA_H7_M7.ota

You can change the default file location in the code by modifying the following line in the **"OTA_Qspi_Flash"** sketch or in the **"OTA_SD_Portenta"** sketch, depending on which method you are going to follow:

```cpp
static char const OTA_FILE_LOCATION[] = "https://your-url-here/your-ota-file.ota";
```

***The latest library examples use HTTPS by default. Make sure your OTA file is hosted on an HTTPS server, or change the `is_https` parameter in the download function to `false` if using HTTP.***

For QSPI Flash example (line 97):

```cpp
int const ota_download = ota.download(OTA_FILE_LOCATION, true /* is_https */);
```

For SD Card example (line 88):

```cpp
int const ota_download = ota.download(OTA_FILE_LOCATION, false /* is_https */);
```

If you are going to use the example OTA file provided in this tutorial, you don't need to modify the file location.

***Now you have two options to choose: use QSPI or use an SD Card to store your OTA file. You can use the left-side index to jump to the option that you may need.***

### QSPI Storage Mode

#### Setting Up

To use the internal **QSPI** storage for downloading the binary file via OTA (Over-The-Air), you will only need the Arduino Portenta H7 board connected to the computer with the [Arduino IDE](https://www.arduino.cc/en/software). You will need to select the **Arduino Portenta H7 (M7 Core)** with the Flash split of **1 MB M7 + 1 MB M4** for the purpose of this tutorial and the corresponding port.

![Arduino Portenta H7 Board Connection](assets/portenta_h7_board_selection.png)

#### Writing the Script

To proceed with OTA using the QSPI flash, you can open the sketch from **Examples > Arduino_Portenta_OTA > OTA_Qspi_Flash**.

***Do not forget to fill in your Wi-Fi AP SSID and password in the `arduino_secrets.h` tab.***

This sketch will connect to your Wi-Fi, verify whether the OTA feature is available by checking the installed firmware on your Portenta.

Then prepare the OTA storage, download the .ota file from the internet, decompress it, reset the board so that after the reboot, it will apply the new firmware

### SD Card Storage Mode

#### Setting Up

To use the **SD card** as the preferred OTA (Over-The-Air) storage device, you can use the Arduino Portenta Vision Shield and Portenta H7 connected via **HD (High-Density)** Connectors.  

![Arduino Portenta H7 with Portenta Vision Shield - Ethernet](assets/portenta_h7_plus_vision_shield.svg)

You will need to select the **Arduino Portenta H7 (M7 Core)** with the Flash split of **1 MB M7 + 1 MB M4** for the purpose of this tutorial and the corresponding port.

#### Writing the Script

Similar to the QSPI storage mode, to proceed with OTA using the SD Card, you can open the sketch from **Examples > Arduino_Portenta_OTA > OTA_SD_Portenta**.

***Do not forget to fill in your Wi-Fi AP SSID and password in the `arduino_secrets.h` tab.***

This sketch will connect to your Wi-Fi, verify whether the OTA feature is available by checking the installed firmware on your Portenta.

Then prepare the OTA storage, download the .ota file from the internet, decompress it, reset the board so that after the reboot, it will apply the new firmware

## Testing the Code

After successfully uploading the code and completing the OTA process, you will be able to see the Arduino Portenta H7 blinking LED in Red, Blue, and Green in a cyclic manner. You will also be able to see the process log in the Serial Monitor provided by the Arduino IDE for more details.

![Arduino Portenta H7 OTA Completion with Cyclic RGB Blink](assets/portenta_h7_ota_blink_cycle.svg)

![Arduino Portenta H7 OTA QSPI Serial Monitor Log](assets/portenta_ota_qspi_result.png)

![Arduino Portenta H7 OTA SD Card Serial Monitor Log](assets/portenta_ota_sd_result.png)

## Conclusion

You have now learned how to use the OTA feature provided by the Arduino Portenta H7 by updating its firmware. You will now be able to create the OTA file with the sketch designed by yourself and use this to update the Arduino Portenta H7's firmware via OTA (Over-The-Air) feature with either QSPI or SD card storage mechanism.

### Next Steps

Now, with the OTA capability in place, you can design a future-proof system based on Arduino Portenta H7 or try different system applications using the OTA capability.

## Full Sketches

The complete script is as follows.

### QSPI Storage Mode

```cpp
/*
 * This example demonstrates how to update the firmware of the Arduino Portenta H7 using
 * a firmware image stored on the QSPI.
 *
 * Steps:
 *   1) Create a sketch for the Portenta H7 and verify
 *      that it both compiles and works on the board.
 *   2) In the IDE select: Sketch -> Export compiled Binary.
 *   3) Create an OTA update file using the tools 'lzss.py' and 'bin2ota.py' stored in
 *      https://github.com/arduino-libraries/ArduinoIoTCloud/tree/master/extras/tools .
 *      A) ./lzss.py --encode SKETCH.bin SKETCH.lzss
 *      B) ./bin2ota.py PORTENTA_H7_M7 SKETCH.lzss SKETCH.ota
 *   4) Upload the OTA file to a network-reachable location, e.g., OTA_Usage_Portenta.ino.PORTENTA_H7_M7.ota
 *      has been uploaded to: https://downloads.arduino.cc/ota/OTA_Usage_Portenta.ino.PORTENTA_H7_M7.ota
 *   5) Perform an OTA update via the steps outlined below.
 */

/******************************************************************************
 * INCLUDE
 ******************************************************************************/

#include <Arduino_Portenta_OTA.h>

#include <WiFi.h>

#include "arduino_secrets.h"

/******************************************************************************
 * CONSTANT
 ******************************************************************************/

/* Please enter your sensitive data in the Secret tab/arduino_secrets.h */
static char const SSID[] = SECRET_SSID;  /* your network SSID (name) */
static char const PASS[] = SECRET_PASS;  /* your network password (use for WPA, or use as key for WEP) */

#if defined(ARDUINO_NICLA_VISION)
static char const OTA_FILE_LOCATION[] = "https://downloads.arduino.cc/ota/OTA_Usage_Portenta.ino.NICLA_VISION.ota";
#elif defined(ARDUINO_PORTENTA_H7_M7)
static char const OTA_FILE_LOCATION[] = "https://downloads.arduino.cc/ota/OTA_Usage_Portenta.ino.PORTENTA_H7_M7.ota";
#elif defined(ARDUINO_OPTA)
static char const OTA_FILE_LOCATION[] = "https://downloads.arduino.cc/ota/OTA_Usage_Portenta.ino.OPTA.ota";
#elif defined(ARDUINO_GIGA)
static char const OTA_FILE_LOCATION[] = "https://downloads.arduino.cc/ota/OTA_Usage_Portenta.ino.GIGA.ota";
#else
#error "Board not supported"
#endif

/******************************************************************************
 * SETUP/LOOP
 ******************************************************************************/

void setup()
{
  Serial.begin(115200);
  while (!Serial) {}

  if (WiFi.status() == WL_NO_SHIELD)
  {
    Serial.println("Communication with WiFi module failed!");
    return;
  }

  int status = WL_IDLE_STATUS;
  while (status != WL_CONNECTED)
  {
    Serial.print  ("Attempting to connect to '");
    Serial.print  (SSID);
    Serial.println("'");
    status = WiFi.begin(SSID, PASS);
    delay(10000);
  }
  Serial.print  ("You're connected to '");
  Serial.print  (WiFi.SSID());
  Serial.println("'");

  Arduino_Portenta_OTA_QSPI ota(QSPI_FLASH_FATFS_MBR, 2);
  Arduino_Portenta_OTA::Error ota_err = Arduino_Portenta_OTA::Error::None;

  if (!ota.isOtaCapable())
  {
    Serial.println("Higher version bootloader required to perform OTA.");
    Serial.println("Please update the bootloader.");
    Serial.println("File -> Examples -> Portenta_System -> PortentaH7_updateBootloader");
    return;
  }

  Serial.println("Initializing OTA storage");
  if ((ota_err = ota.begin()) != Arduino_Portenta_OTA::Error::None)
  {
    Serial.print  ("Arduino_Portenta_OTA::begin() failed with error code ");
    Serial.println((int)ota_err);
    return;
  }


  Serial.println("Starting download to QSPI ...");
  int const ota_download = ota.download(OTA_FILE_LOCATION, true /* is_https */);
  if (ota_download <= 0)
  {
    Serial.print  ("Arduino_Portenta_OTA_QSPI::download failed with error code ");
    Serial.println(ota_download);
    return;
  }
  Serial.print  (ota_download);
  Serial.println(" bytes stored.");


  Serial.println("Decompressing LZSS compressed file ...");
  int const ota_decompress = ota.decompress();
  if (ota_decompress < 0)
  {
    Serial.print("Arduino_Portenta_OTA_QSPI::decompress() failed with error code");
    Serial.println(ota_decompress);
    return;
  }
  Serial.print(ota_decompress);
  Serial.println(" bytes decompressed.");


  Serial.println("Storing parameters for firmware update in bootloader accessible non-volatile memory ...");
  if ((ota_err = ota.update()) != Arduino_Portenta_OTA::Error::None)
  {
    Serial.print  ("ota.update() failed with error code ");
    Serial.println((int)ota_err);
    return;
  }

  Serial.println("Performing a reset after which the bootloader will update the firmware.");
  Serial.println("Hint: Portenta H7 LED will blink Red-Blue-Green.");
  delay(1000); /* Make sure the serial message gets out before the reset. */
  ota.reset();
}

void loop()
{

}
```

### SD Card Storage Mode

```cpp
/*
 * This example demonstrates how to update the firmware of the Arduino Portenta H7 using
 * a firmware image stored on the SD card.
 *
 * Steps:
 *   1) Create a sketch for the Portenta H7 and verify
 *      that it both compiles and works on the board.
 *   2) In the IDE select: Sketch -> Export compiled Binary.
 *   3) Create an OTA update file using the tools 'lzss.py' and 'bin2ota.py' stored in
 *      https://github.com/arduino-libraries/ArduinoIoTCloud/tree/master/extras/tools .
 *      A) ./lzss.py --encode SKETCH.bin SKETCH.lzss
 *      B) ./bin2ota.py PORTENTA_H7_M7 SKETCH.lzss SKETCH.ota
 *   4) Upload the OTA file to a network-reachable location, e.g., OTA_Usage_Portenta.ino.PORTENTA_H7_M7.ota
 *      has been uploaded to: http://downloads.arduino.cc/ota/OTA_Usage_Portenta.ino.PORTENTA_H7_M7.ota
 *   5) Perform an OTA update via the steps outlined below.
 */

/******************************************************************************
 * INCLUDE
 ******************************************************************************/

#include <Arduino_Portenta_OTA.h>

#include <WiFi.h>

#include "arduino_secrets.h"

/******************************************************************************
 * CONSTANT
 ******************************************************************************/

/* Please enter your sensitive data in the Secret tab/arduino_secrets.h */
static char const SSID[] = SECRET_SSID;  /* your network SSID (name) */
static char const PASS[] = SECRET_PASS;  /* your network password (use for WPA, or use as key for WEP) */

static char const OTA_FILE_LOCATION[] = "http://downloads.arduino.cc/ota/OTA_Usage_Portenta.ino.PORTENTA_H7_M7.ota";

/******************************************************************************
 * SETUP/LOOP
 ******************************************************************************/

void setup()
{
  Serial.begin(115200);
  while (!Serial) {}

  if (WiFi.status() == WL_NO_SHIELD)
  {
    Serial.println("Communication with WiFi module failed!");
    return;
  }

  int status = WL_IDLE_STATUS;
  while (status != WL_CONNECTED)
  {
    Serial.print  ("Attempting to connect to '");
    Serial.print  (SSID);
    Serial.println("'");
    status = WiFi.begin(SSID, PASS);
    delay(10000);
  }
  Serial.print  ("You're connected to '");
  Serial.print  (WiFi.SSID());
  Serial.println("'");

  //Arduino_Portenta_OTA_SD ota(SD_FATFS, 0);
  Arduino_Portenta_OTA_SD ota(SD_FATFS_MBR, 1);
  Arduino_Portenta_OTA::Error ota_err = Arduino_Portenta_OTA::Error::None;

  if (!ota.isOtaCapable())
  {
    Serial.println("Higher version bootloader required to perform OTA.");
    Serial.println("Please update the bootloader.");
    Serial.println("File -> Examples -> Portenta_System -> PortentaH7_updateBootloader");
    return;
  }

  Serial.println("Initializing OTA storage");
  if ((ota_err = ota.begin()) != Arduino_Portenta_OTA::Error::None)
  {
    Serial.print  ("Arduino_Portenta_OTA::begin() failed with error code ");
    Serial.println((int)ota_err);
    return;
  }


  Serial.println("Starting download to SD ...");
  int const ota_download = ota.download(OTA_FILE_LOCATION, false /* is_https */);
  if (ota_download <= 0)
  {
    Serial.print  ("Arduino_Portenta_OTA_SD::download failed with error code ");
    Serial.println(ota_download);
    return;
  }
  Serial.print  (ota_download);
  Serial.println(" bytes stored.");


  Serial.println("Decompressing LZSS compressed file ...");
  int const ota_decompress = ota.decompress();
  if (ota_decompress < 0)
  {
    Serial.print("Arduino_Portenta_OTA_SD::decompress() failed with error code");
    Serial.println(ota_decompress);
    return;
  }
  Serial.print(ota_decompress);
  Serial.println(" bytes decompressed.");


  Serial.println("Storing parameters for firmware update in bootloader accessible non-volatile memory");
  if ((ota_err = ota.update()) != Arduino_Portenta_OTA::Error::None)
  {
    Serial.print  ("Arduino_Portenta_OTA::update() failed with error code ");
    Serial.println((int)ota_err);
    return;
  }

  Serial.println("Performing a reset after which the bootloader will update the firmware.");
  Serial.println("Hint: Portenta H7 LED will blink Red-Blue-Green.");
  delay(1000);
  ota.reset();
}

void loop()
{

}
```

## Troubleshooting

For troubleshooting issues that might have arisen while following the tutorial, you can use the following tips to solve the issue.

- If there has been an issue with the Wi-Fi module, it means the device may have lost the Wi-Fi firmware partition. To solve this, you will have to use the **WiFiFirmwareUpdater** sketch found in the Arduino IDE examples to fix the issue.
- QSPI storage may throw error -3 while running the Portenta H7 OTA QSPI example. To fix this, you can use the guide on [Reading and Writing Flash Memory](https://docs.arduino.cc/tutorials/portenta-h7/reading-writing-flash-memory) in the section **Programming the QSPI Flash**. At this point, run the example again, and the error -3 (OTA Storage initialization error) should be resolved.
