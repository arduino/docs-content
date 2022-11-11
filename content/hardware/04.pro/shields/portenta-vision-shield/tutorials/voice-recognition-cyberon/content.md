---
title: "Voice Recognition With Cyberon"
difficulty: beginner
tags: [Camera, Bitmap, SD Card]
description: Control your device with voice commands thanks to the Cyberon SDK.
author: Pablo Marquínez
libraries:
  - name: CyberonSDK.com
    url: TBD
hardware:
  - hardware/04.pro/boards/portenta-h7
  - hardware/04.pro/shields/portenta-vision-shield
software:
  - ide-v1
  - ide-v2
  - web-editor
  - cli
---

## Overview
This tutorial shows you how to receive voice commands and perform custom tasks after receiving the order.

## Goals

- Setting the command triggers
- Getting the needed files and set up the library
- Get the license and use it on the sketch
- Create an Arduino sketch to control the LED's color

### Required Hardware and Software

- [Portenta H7](https://store.arduino.cc/portenta-h7)
- Portenta Vision Shield ([LoRa](https://store.arduino.cc/portenta-vision-shield-lora) or [Ethernet](https://store.arduino.cc/portenta-vision-shield))
- 1x USB-C® cable (either USB-A to USB-C® or USB-C® to USB-C®)
- Arduino IDE or Arduino-cli

## Instructions

In order to get the library, the dataset model and the license to use the library it is needed to:
* Get the Serial Number of your Arduino device
* Fill some information on Cyberon's website
* Once you get the files, you need to activate your license (only required if you have a license)

### Get The Files

#### Get The Serial Number

To get the Serial Number of your board you will need to open the **Arduino IDE**, select the board's serial port and click on **tools > Get Board Info**, you will see the "SN" number, save it.

#### Request the Files

Once you have the Serial number.

Depending on the board that you are using, navigate to:
* [Portenta H7 activation page](https://tool.cyberon.com.tw/GetLicense/GetLicensePage_portenta-h7.php)
* [Nano RP2040 activation page](https://tool.cyberon.com.tw/GetLicense/GetLicensePage_rp2040.php)
* [Nano 33 Sense BLE activation page](https://tool.cyberon.com.tw/GetLicense/GetLicensePage_33ble.php)

Now fill the "Board serial number" field and click the **Submit** button.

Now that you have submitted the activation, you should have received an e-mail with the file `Model_{board}.dsproj` this will be later on used to activate your license.

Please note that the files you have are a "demo" version. The limitations are:
  * 50 recognitions per start.
  * There will be a 20 seconds delay before each trigger recognition.

#### Activate The License and Customize the Model

Go to [Cyberon's Model Configuration](https://tool.cyberon.com.tw/ArduinoDSpotterAuth/CFMain.php)

Fill the required fields and make sure you upload the ".dsproj" file you have gotten on the previous step.

Now you will see a new page to configure the trigger word, this word will be the one used to let the board now that you are going to say a command after it.

Depending on the license you can configure more than one trigger words.

You are also able to add "command words", these are the ones to do work, for example "play music".

Once you finish your table of words, you can finish and you will get the model header file (model.h), you will need to copy it onto your sketch folder in order to access it.

The IDs of the words on the table are collected on the info.txt so you will have them already saved, these are used to know which command has been said by the user on the application.

#### Setup the Library

As any custom Arduino Library, you need to download the library and save it on the **Arduino/libraries** directory.

More instructions on how to install libraries, https://docs.arduino.cc/hacking/software/Libraries.

***From now on, if you want to use your license, you will need to copy the header file (.h) within the sketch folder.***

### Create the sketch

-EXPLANATION OF THE SKETCH PENDING HERE (TODO)-

#### Full Sketch

```cpp
#include "CDSpotterHL.h"
#include "LED_Control.h"

// The DSpotter License Data.
#include "CybLicense.h"
#define DSPOTTER_LICENSE g_lpdwLicense

#include "Model.h"
#define DSPOTTER_MODEL g_lpdwModel

// define the different words IDs
#define COMMAND_RED 1002
#define COMMAND_BLUE 1003

// define colors for the LED Color Function
#define COLOR_OFF 0b1
#define COLOR_ON 0b10
#define COLOR_RED 0b100
#define COLOR_GREEN 0b1000
#define COLOR_BLUE 0b10000

// The VR engine object. Only can exist one, otherwise not worked.
static CDSpotterHL g_oCDSpotterHL;

void ledColor(int color)
{
  digitalWrite(LEDR, (color & COLOR_RED) >> 2);
  digitalWrite(LEDG, (color & COLOR_GREEN) >> 3);
  digitalWrite(LEDB, (color & COLOR_BLUE) >> 4);

  nicla::leds.setColor(!(color & COLOR_OFF));
}

// Callback function for VR engine
void VRCallback(int nFlag, int nID)
{
  if (nFlag == CDSpotterHL::InitSuccess)
  {
    // ToDo
  }
  else if (nFlag == CDSpotterHL::GetResult)
  {
    // ToDo
    Serial.print("Got ID: ");
    Serial.println(nID);
    switch (nID)
    {
    case COMMAND_RED:
      ledColor(COLOR_RED);
      break;
    case COMMAND_BLUE:
      ledColor(COLOR_BLUE);
      break;

    default:
      break;
    }
  }
  else if (nFlag == CDSpotterHL::ChangeStage)
  {
    switch (nID)
    {
    case CDSpotterHL::TriggerStage:
      ledColor(COLOR_OFF);
      break;
    case CDSpotterHL::CommandStage:
      ledColor(COLOR_GREEN);
      break;
    default:
      break;
    }
  }
  else if (nFlag == CDSpotterHL::GetError)
  {
    g_oCDSpotterHL.Release();
    while (1)
      ; // hang loop
  }
  else if (nFlag == CDSpotterHL::LostRecordFrame)
  {
    // ToDo
  }
}

void setup()
{
  // Init Serial output
  Serial.begin(9600);
  while (!Serial)
    ;

  // Init LED
  LED_Init_All();

  // Init VR engine & Audio
  if (g_oCDSpotterHL.Init(DSPOTTER_LICENSE, sizeof(DSPOTTER_LICENSE), DSPOTTER_MODEL, VRCallback) != CDSpotterHL::Success)
    return;
}

void loop()
{
  // Do VR
  g_oCDSpotterHL.DoVR();
}
```

## Conclusion

## Next Steps
