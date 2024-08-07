---
title: "Arduino MKR GSM 1400 and I2S "
description: "This tutorial aims to show you how to use the I2S bus to send audio over phone calls between the micro controller and the GSM module."
coverImage: "assets/img_0547_DjftN61d15.jpg"
tags: [audio, gsm, internet of things, iot]
difficulty: intermediate
author: "Arduino_Genuino"
source: "https://create.arduino.cc/projecthub/Arduino_Genuino/arduino-mkr-gsm-1400-and-i2s-2a48b6"
---

## Components and Supplies

- [Arduino MKR GSM 1400](https://www.newark.com/55AC1187?COM=ref_hackster)
- [Arduino MKR SD Proto Shield](https://store.arduino.cc/mkr-sd-proto-shield)
- [Digilent MicroSD Card with Adapter](http://store.digilentinc.com/)
- 3.7 V LiPo Battery
- [USB-A to Micro-USB Cable](https://www.newark.com/53W6089?COM=ref_hackster)

## Apps and Online Services

- [Arduino IDE](https://www.arduino.cc/en/main/software)
- [Arduino Cloud Editor](https://create.arduino.cc/editor)

## About This Project

### Introduction

The SAMD 21 (the microcontroller on your Arduino board) can communicate with the SARA U201 (the GSM module on your Arduino board) using the I2S bus. This means that you can send audio data from the micro controller to the module! In such a way you can reproduce for example a wav file over a phone call as we will show in this tutorial.

You have to consider that the I2S bus is the same that is present on the headers so if you use it to communicate with the module you can't use the same pins in your project. In particular you can't use:

* A6: I2S serial data;
* 2: I2S serial clock;
* 3: I2S frame select;

### How It Works

The operating principle of this tutorial is very simple: every time a phone call is received, the boards answers the call, plays the chosen .wav file and when it is finished it hangs the call.

### Setup

The setup to use this code is very simple. You just have to:

* format your SD card in FAT16 or FAT32 format;
* load the .wav [file](https://content.arduino.cc/assets/ADV.wav) on the SD card;
* plug your MKR SD Proto Shield on top of your board;
* plug the antenna into the board;
* plug a micro SIM card into your board;
* plug the battery into the board;
* plug the micro USB cable and connect it to your PC;
* load the code on the board using the Arduino Java or Web IDE;
* open the Serial Monitor;
* call the board and enjoy!
  
## Code
<iframe src='https://create.arduino.cc/editor/Arduino_Genuino/98e9e261-0626-4994-98d9-8efcd21ed5ec/preview?embed&snippet' style='height:510px;width:100%;margin:10px 0' frameborder='0'></iframe>


### See Also

This example is based on the [Arduino Sound](https://www.arduino.cc/en/Reference/ArduinoSound) library and the [Arduino GSM](https://www.arduino.cc/en/Reference/GSM) library. 