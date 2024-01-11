---
title: 'Data Logger with MKR SD Proto Shield'
difficulty: intermediate
compatible-products: [mkr-sd-proto-shield]
description: 'Learn how to log data on an SD card using the MKR SD Proto Shield.'
tags:
  - Micro SD
  - Storage
author: 'Karl Söderby'
libraries: 
  - name: SD
    url: https://www.arduino.cc/en/Reference/SD
hardware:
  - hardware/01.mkr/02.shields/mkr-sd-proto-shield
  - hardware/01.mkr/01.boards/mkr-wifi-1010
software:
  - ide-v1
  - ide-v2
  - web-editor
---

## Introduction 

In this tutorial, we will find out how we can log data on an SD card. The [MKR SD Proto Shield](https://store.arduino.cc/mkr-sd-proto-shield) is a MKR form factor shield, that has a slot for a micro SD card. A great add-on for any MKR board (except for [Arduino MKR Zero](https://store.arduino.cc/arduino-mkr-zero-i2s-bus-sd-for-sound-music-digital-audio-data) which already has a micro SD card slot), that can be used to log data offline, or to store larger amounts of data.

In this tutorial we will only focus on logging offline data, by uploading a sketch that reads three of the analog pins on a MKR family board.

>**Important:** The MKR SD Proto Shield does not come with pins soldered to the circuit board. These will have to be manually soldered to be able to fit on top of a MKR family board directly. If you do not have the option to solder, you can check out the [MKR MEM Shield](https://store.arduino.cc/arduino-mkr-mem-shield), a similar shield that also provides extra Flash memory, that comes with the pins pre-soldered. 

## Goals

The goals of this project are:

- Read data from the analog pins on a MKR family board.
- Store the data on the SD card.
- View the data using a text editor on a computer.

## Hardware & Software Needed

- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software)).
- [SD](https://www.arduino.cc/en/Reference/SD) library.
- Arduino MKR family board ([link to store](https://store.arduino.cc/arduino-genuino/arduino-genuino-mkr-family)).
- Arduino MKR SD Proto Shield ([link to store](https://store.arduino.cc/mkr-sd-proto-shield)).
- A formatted micro SD card (with adapter).

## Secure Digital (SD) Card

You have most likely used, or simply have heard of the SD card. It is short for Secure Digital, and is a great option for storing large quantities of data. The SD card is small in size and weighs practically nothing, yet, some of them are capable of storing up to a **terabyte of data**. In comparison, it is quite standard for a laptop to have between 128 - 256 Gigabytes of storage space. 

However, to log data from e.g. sensors, it would take quite some time to reach the storage limit. 

### Useful Scenarios

Let's take a look at when and where we might want to use an SD card. There are typically two main scenarios when they are quite useful for an Arduino project:

- Storing larger files, e.g. sound files or icons (useful for projects using a display).
- Logging data offline.

Let's imagine we have an Arduino board and a couple of environmental sensors and we want to do a weather project. We do not have any way of transmitting real time data, but we would like to track the weather for the next month, to later be analysed. We do not have the possibility to connect the board to a computer, since it needs to be outdoor.

The solution: an SD card. A really simple way of logging data over a longer period of time, without any connection to the Internet or a computer is to simply store it locally. Let's say we do a reading every 10 seconds of the temperature and wind speed, which we can then store on the SD card.

![Storing different data types.](assets/MKRSD_T1_IMG01.png)

When we have finished recording, we simply remove the SD card and plug it into a computer. The data have now been logged, and these values can easily be converted into a graph. For example, we can see the patterns of temperature going up and down as well as the wind increasing.
 
![Graphing the data.](assets/MKRSD_T1_IMG02.png)

### Circuit

The circuit for this tutorial is very easy. First, let's mount the MKR SD Proto Shield on top of a MKR family board of your choice.

![Mounting the shield.](assets/MKRSD_T1_IMG03.png)

Now, we need to insert a micro SD card into the slot on the shield. 

![Inserting the Micro SD card.](assets/MKRSD_T1_IMG04.png)


## Programming the Board

We will now get to the programming part of this tutorial. We are going to create a program that will make readings on A0, A1 and A2 pins, create a file on the SD card, and log the readings in that file. 

**1.** First, let's make sure we have the drivers installed. If we are using the Web Editor, we do not need to install anything. If we are using an offline editor, we need to install it manually. This can be done by navigating to **Tools > Board > Board Manager...**. Here we need to look for the **Arduino SAMD boards (32-bits Arm® Cortex®-M0+)** and install it. 

**2.** Here are some of the core functions of this sketch:

- `while (!Serial)` - prevents the program from running until we open the Serial Monitor.
- `SD.begin(chipSelect)` - initializes the SD card with selected pin.
- `File dataFile = SD.open("datalog.txt", FILE_WRITE)` - creates the `dataFile` object to access the library functionalities, and opens/create a file named `datalog.txt` on the SD card, and set it to write mode. 
- `dataFile.print()` - prints something to the `datalog.txt` file. 
- `dataFile.close()` - closes the file.

The sketch can be found in the snippet below, or it can also be accessed from the IDE, by navigating to **File > Examples > SD > Datalogger**. Continue by uploading the code to the board.

```cpp
#include <SPI.h>
#include <SD.h>

const int chipSelect = SDCARD_SS_PIN;

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }


  Serial.print("Initializing SD card...");

  // see if the card is present and can be initialized:
  if (!SD.begin(chipSelect)) {
    Serial.println("Card failed, or not present");
    // don't do anything more:
    while (1);
  }
  Serial.println("card initialized.");
}

void loop() {
  // make a string for assembling the data to log:
  String dataString = "";

  // read three sensors and append to the string:
  for (int analogPin = 0; analogPin < 3; analogPin++) {
    int sensor = analogRead(analogPin);
    dataString += String(sensor);
    if (analogPin < 2) {
      dataString += ",";
    }
  }

  // open the file. note that only one file can be open at a time,
  // so you have to close this one before opening another.
  File dataFile = SD.open("datalog.txt", FILE_WRITE);

  // if the file is available, write to it:
  if (dataFile) {
    dataFile.println(dataString);
    dataFile.close();
    // print to the serial port too:
    Serial.println(dataString);
  }
  // if the file isn't open, pop up an error:
  else {
    Serial.println("error opening datalog.txt");
  }
  delay(1000);
}
```

## Testing It Out

After uploading the code to the board, we need to open the Serial Monitor to initialize the program. This is due to the `while(!Serial)` command introduced in the setup, which prevents the program from running unless the Serial Monitor opens. 

On the Serial Monitor, we will see data from the three analog pins being printed, each separated by a comma. This is also how it should look inside the `.txt` file where we are printing the values as well.

![Serial Monitor output of the data recorded from pin A0-A2.](assets/MKRSD_T1_IMG05.png)

Now if we are seeing these values, and no error messages, we can assume that the data logged on the SD card went well. To check this, let's follow a few simple steps:

**1.** Cut the power to the MKR family board.  
**2.** Remove the micro SD card from the shield.  
**3.** Insert the micro SD card to an adapter that fits your computer.  
**4.** Insert the card into a computer, and open up the `datalog.txt` file.  

This file should now show the same values that we saw in the Serial Monitor.

![Inside the datalog.txt file.](assets/MKRSD_T1_IMG06.png)

And that's how we can log data using a MKR family board, a MKR SD Proto Shield, the SD library and a micro SD card. 

>**Bonus:** If you want to log data in a file that can be opened with **excel**, change the `.txt` to `.csv`. These files can then be opened with excel, where you can do more interesting thing with the data, such as creating graphs. 


### Troubleshoot

If the code is not working, there are some common issues we can troubleshoot:

- Check that the SD card is working.
- Check that you have installed the Board Package for the MKR family boards (instructions are above the code).
- Make sure you open the Serial Monitor.

## Conclusion

In this tutorial, we have tested the main functionality of the MKR SD Proto Shield: storing data on an SD Card.

As a very basic example, we read the values of three analog pins, stored them in a `.txt` file and later viewed the data on our computer. 

The analog pins are currently not generating any useful data, as we have not connected anything to them, but for further exploration you can connect some type of sensor, that would provide more useful data.

Feel free to explore the [SD](https://www.arduino.cc/en/reference/SD) library further, and try out some of the many cool functions in this library.