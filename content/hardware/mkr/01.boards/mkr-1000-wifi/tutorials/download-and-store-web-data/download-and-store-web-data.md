---
title: "Download and Store Web Data © GPL3+"
description: "How to use the Arduino HTTP Client library to download a raw text page and store its content on an SD card."
coverImage: "assets/mkr1000_-_mkr_sd_proto_shield_pWAhuqrpzk.jpg"
tags: [http, mkr1000, wifi]
difficulty: beginner
author: "Arduino_Genuino"
source: "https://create.arduino.cc/projecthub/Arduino_Genuino/download-and-store-web-data-37ef55"
---

## Components and Supplies

- [Arduino MKR1000](https://store.arduino.cc/arduino-mkr1000)
- [Arduino MKR SD Proto Shield](https://store.arduino.cc/mkr-sd-proto-shield)

## Apps and Online Services

- [Arduino Cloud Editor](https://create.arduino.cc/editor)
- [Arduino IDE](https://www.arduino.cc/en/main/software)

## About This Project

### Format Your SD Card the Right Way

The Arduino SD library is able to read and write only FAT16 or FAT32 cards, so first you need to format your SD card in one of these formats.

### Put Things Together

This project is very easy to assemble. You simply have to put your SD card in the Arduino MKR SD Proto Shield and place the shield on top of your MKR1000 board.

### HTTP Client Library

The [Arduino HTTP client library ](https://github.com/arduino-libraries/ArduinoHttpClient)allows you to easily parse a HTTP GET request separating the header and the body for you. This means that your code is very light and understandable. You can even change your sketch behavior depending on the status code response.

## Code

<iframe src='https://create.arduino.cc/editor/Arduino_Genuino/43b03333-b080-492f-85eb-ca6146a2dab7/preview?embed&snippet' style='height:510px;width:100%;margin:10px 0' frameborder='0'></iframe>


### Run the Code

To run the code, upload it onto your board and then open your Serial monitor. The board will print out the various steps in the code, and if the ASCII logo is correctly downloaded, it will be printed on the Serial monitor reading it from the SD card.