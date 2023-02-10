---
title: "Voice Recognition With Cyberon SDK"
difficulty: beginner
tags: [Camera, Bitmap, SD Card]
description: Control your device with voice commands with the Cyberon SDK.
author: Pablo Marquínez
libraries:
  - name: Cyberon_DSpotterSDK_Maker_PortentaH7
    url: https://github.com/CyberonEBU/Cyberon_DSpotterSDK_Maker_PortentaH7
  - name: Cyberon_DSpotterSDK_Maker_33BLE
    url: https://github.com/CyberonEBU/Cyberon_DSpotterSDK_Maker_33BLE
  - name: Cyberon_DSpotterSDK_Maker_RP2040
    url: https://github.com/CyberonEBU/Cyberon_DSpotterSDK_Maker_RP2040
hardware:
  - hardware/04.pro/boards/portenta-h7
  - hardware/04.pro/shields/portenta-vision-shield
  - hardware/03.nano/boards/nano-33-ble
  - hardware/03.nano/boards/nano-rp2040-connect
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
- Get the license and use the demo sketch
- Create a new project (custom voice commands)
- Unlock limitations of the project (license needed)
<!-- - Create an Arduino sketch to control the LED's color -->

### Required Hardware and Software

- [Portenta H7](https://store.arduino.cc/portenta-h7)
- Portenta Vision Shield ([LoRa](https://store.arduino.cc/portenta-vision-shield-lora) or [Ethernet](https://store.arduino.cc/portenta-vision-shield))
- 1x USB-C® cable (either USB-A to USB-C® or USB-C® to USB-C®)
- Arduino IDE or Arduino-cli

## Instructions

* Get the Serial Number of your Arduino device
* Get the library
* Test the free demo
In case you have a license (paid):
* Fill some information on Cyberon's website
* Once you get the files, you need to activate your license

### Setup

#### Setup the Library

There are 3 libraries, depending on which board you are using:
* Cyberon_DSpotterSDK_Maker_RP2040 (Nano RP2040)
* Cyberon_DSpotterSDK_Maker_PortentaH7 (Portenta H7)
* Cyberon_DSpotterSDK_Maker_33BLE (Nano 33 BLE)

***Inside the downloaded library, you will have access to some documentation from Cyberon, inside the "extra" folder, check them out for more information.***

Go to the Library Manager, search the library that you need for your board and install it.

More instructions on how to install libraries, https://docs.arduino.cc/hacking/software/Libraries.

***From now on we will refer to the DSpotter SDK library as Cyberon_DSpotterSDK library, to skip the specific board***

#### Get The Serial Number

In order to get your board's serial number, once you have the library downloaded: navigate to **File > Examples > Cyberon_DSpotterSDK > GetSerialNumber**

Upload the sketch, and after it's done open the **Serial Monitor** to see your device's Serial Number.

You will need this to activate the license on your board.

##### Arduino IDE V1

There is another way only available through the previous version of the Arduino IDE.

To get the Serial Number of your board you will need to open the **Arduino IDE v1**, select the board's serial port and click on **tools > Get Board Info**, you will see the "SN" number, save it.

#### Get the Demo License

Once you have the Serial number.

Depending on the board that you are using, open https://tool.cyberon.com.tw/GetLicense/GetLicensePage.php

Select the board you are using.

Secondly fill the "Board serial number" field and click the **Submit** button.

Once everything is ready, click on the **submit** button to get your license.

Save that array of characters.

### Test the Free Demo Sketch

Open the sketch **File > Example > Cyberon_DSpotterSDK > VoiceRecognition**

Navigate to the `CybLicense.h` tab.

Paste your license between the brackets, like:
```cpp
const uint32_t g_lpdwLicense[]{
  AAAABBBBCCCCDDDD.....ZZZZ
};
```

Now switch back to the `VoiceRecognition` tab and upload the sketch.

You can now open the Serial Monitor, you will see the available commands that the CyberonSDK will recognice.

Feel free to say the commands and see how it recognice your voice!

Please note that the files you have are a "demo" version have limitations which:
  * Maximum of 50 recognitions per start.
  * 20 seconds delay before each trigger recognition.

#### Customized Commands

***This steps are compatible for the trial license (the one that we are showing) and the paid license***

Go to [Cyberon's Model Configuration](https://tool.cyberon.com.tw/ArduinoDSpotterAuth/CTMain.php)

Fill the required fields:
* e-mail address
* Board
* Serial Number of your board
* EULA Agreement (Please read it carefully)

Now you will see a new page to:
* Create a new project, or
* Import an existing project

##### Create a New Project

First, you need to select the desired language of the voice recognition, once is set, click **create**.

* Create the **Input Trigger word**, for example "Hey Arduino".
  The **Input Trigger word** will trigger the device, to let the board know that you are going to say a command after that.
* Add the **Command** list.
  This commands will be used to do tasks on your sketch, for example if you have a command which is "Play", afterwards you will be able to get that command and proceed with some job inside the sketch easily.

Once you finish your table of words, you can click **Next** to finish.
At the end you will see all the configuration that you have set, check it out and see if there is something wrong, you are on time to go back and fix it.

Once everything is checked, click **Confirm** and you will get the model header file (model.h), you will need to copy it onto your sketch folder in order to access it.

You will now get some files on your e-mail address, download them.

On the IDE, open the example **File > Examples > Cyberon_DSpotterSDK > VoiceRecognition** and click **File > Save As...** and type a name for your sketch.

Once it's saved, open your File Explorer, and navigate to your sketch path.

On your sketch directory, paste the files you have got on your e-mail before:
* `CybLicense_<id>.h`
* `Model_<id>.h`

Now to implement the **Input Trigger Command** and the **Command List** open the sketch and change the following `#include`

```cpp
...

#include "CybLicense.h" -> #include "CybLicense_<id>.h"

...

#include "Model_L1.h" -> #include "Model_<id>.h"

...

#include "Model_L0.h" -> #include "CybLicense_<id>.h"

```

Now you are all set to use your new project!

Upload the sketch, and open the Serial Monitor.

Test your new **Input Trigger Word** and the **Command** list that you have created.

You will see the recognised words on the **Serial Monitor**


The IDs of the words on the table are collected on the info.txt so you will have them already saved, these are used to know which command has been said by the user on the application.


#### Unlock Limitations (License)

***For this section you need to have bought the corresponding license, available at https://store.arduino.cc/speech-recognition-engine***
***Depending on the license you can configure more than one trigger words.***

Note that you need to have an already existing project, check the [previous section](#create-a-new-project).

Browse to [Cyberon's Licensed Project Configuration](https://tool.cyberon.com.tw/ArduinoDSpotterAuth/CFMain.php)


Fill the required fields:
* e-mail address
* Board
* Serial Number of your board
* Voucher code
* Import project: the `.dsproj` file that you have received on your e-mail.
* EULA Agreement (Please read it carefully)

Click next, review your project options and press continue.

You will get a new e-mail with the new License and Model headers.

Open the sketch you have duplicated on the [Create New Project](#create-a-new-project) section.

Repeat the replacement of `#include` files, with the latest ones (they have a different ID):
```cpp
...

#include "CybLicense_<id>.h" -> #include "CybLicense_<newId>.h"

...

#include "Model_<id>.h" -> #include "Model_<newId>.h"

...

#include "CybLicense_<id>.h" -> #include "CybLicense_<newId>.h"

```
<!--
### Create The Sketch

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
-->

## Conclusion

## Next Steps
