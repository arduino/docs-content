---
title: 'MKR Zero Data Logger'
difficulty: intermediate
compatible-products: [mkr-zero]
description: 'Learn how to log data on an SD card.'
tags:
  - Micro SD
  - Storage
author: 'Karl Söderby'
libraries: 
  - name: SD
    url: https://www.arduino.cc/en/Reference/SD
hardware:
  - hardware/01.mkr/01.boards/mkr-zero
software:
  - ide-v1
  - ide-v2
  - web-editor
---

## Introduction 

In this tutorial, we will find out how we can log data on an SD card. The [Arduino MKR Zero](https://store.arduino.cc/arduino-mkr-zero-i2s-bus-sd-for-sound-music-digital-audio-data) comes equipped with a slot for a micro SD card, a great feature to use when there's a need to log data offline.

We will test this out by uploading a sketch that reads three of the analog pins.

## Goals

The goals of this project are:

- Read data from the analog pins.
- Store the data on the SD card.
- View the data using a text editor on a computer.

## Hardware & Software Needed

- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software)).
- [SD](https://www.arduino.cc/en/Reference/SD) library.
- Arduino MKR Zero ([link to store](https://store.arduino.cc/arduino-mkr-zero-i2s-bus-sd-for-sound-music-digital-audio-data)).
- A formatted micro SD card (with adapter).

## Secure Digital (SD) Card

You have most likely used, nevertheless heard, of the SD card. It is short for Secure Digital, and is a great option for storing large quantities of data. The SD card is tiny and weighs practically nothing, yet, some of them are capable of storing up to a **terabyte of data.** In comparison, it is quite standard for a laptop to have between 128 - 256 gigabytes of storage space. 

However, to log data from e.g. sensors, it would take quite some time to reach that limit. 

### Useful Scenarios

But let's take a look at when and where we might want to use an SD card. There are typically two main scenarios when they are quite useful for an Arduino project:

- Storing larger files, e.g. sound files or icons (useful for projects using a display).
- Logging data offline.

Let's imagine we have an Arduino board and a couple of environmental sensors, and we want to do a weather project. We do not have any way of transmitting real time data, but we would like to track the weather for the next month, to later be analysed. We do not have the possibility to connect the board to a computer, since it needs to be outdoor.

The solution: an SD card. A really simple way of logging data over a longer period of time, without any connection to Internet or a computer is to simply store it locally. Let's say we do a reading every 10 seconds of the temperature and wind speed, we can then also store that reading on the SD card.

![Storing different data types.](assets/MKRZERO_T1_IMG01.png)

When we have finished recording, we simply remove the SD card and plug it into a computer. The data has now nicely been logged, and these values can easily be converted into a graph. We can then for example see the pattern of temperature going up and down and the wind increasing.
 
![Graphing the data.](assets/MKRZERO_T1_IMG02.png)

### Circuit

The circuit for this tutorial is very easy. All we have to do is insert the SD card into the MKR Zero board. 

![Inserting the SD card.](assets/MKRZERO_T1_IMG03.png)


## Programming the Board

We will now get to the programming part of this tutorial. We will here create a program that will make readings on A0, A1 and A2, create a file on the SD card, and log the readings in that file. 

**1.** First, let's make sure we have the drivers installed. If we are using the Web Editor, we do not need to install anything. If we are using an offline editor, we need to install it manually. This can be done by navigating to **Tools > Board > Board Manager...**. Here we need to look for the **Arduino SAMD boards (32-bits Arm® Cortex®-M0+)** and install it. 

**2.** We can now take a look at some of the Board Package functions of this sketch:

- `while (!Serial)` 
- `SD.begin(chipSelect)` - initializes the SD card with selected pin.
- `File dataFile = SD.open("datalog.txt", FILE_WRITE)` - creates the `dataFile` object to access the library functionalities, and opens/create a file named `datalog.txt` on the SD card, and set it to write mode. 
- `dataFile.print()` - prints something to the `datalog.txt` file. 
- `dataFile.close()` - closes the file.

The sketch can be found in the snippet below. The sketch can also be accessed from the IDE, by navigating to **File > Examples > SD > Datalogger**. Upload the code to the board.

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

After uploading the code to the board, we need to open the Serial Monitor to initialize the program. This is due to the `while(!Serial)` command introduced in the setup, which prevents the program from running. 

When we open the Serial Monitor, we will see data from the three analog pins being printed, each separated by a comma. This is also how it should look inside the `.txt` file that we are printing the values to as well.

![Serial Monitor output of the data recorded from pin A0-A2.](assets/MKRZERO_T1_IMG04.png)

Now if we are seeing these values, and no error messages, we can assume the data logging on the SD card has gone well. To check this, let's follow a few simple steps:

**1.** Cut the power to the MKR Zero board.  
**2.** Remove the micro SD card from the board.  
**3.** Insert the micro SD card to an adapter that fits your computer.  
**4.** Insert the card into a computer, and open up the `datalog.txt` file.  

This file should now show the same values that we saw in the Serial Monitor.

![Inside the datalog.txt file.](assets/MKRZERO_T1_IMG05.png)

And that's how we can log data, using only the MKR Zero board, the SD library and a micro SD card. 

>**Bonus:** If you want to log data in a file that can be opened with **excel**, change the `.txt` to `.csv`. These files can then be opened with excel, where you can do more interesting thing with the data, such as creating graphs. 


### Troubleshoot

If the code is not working, there are some common issues we can troubleshoot:

- Check that the SD card is working.
- Check that you have installed the Board Package for the MKR Zero board (instructions are above the code).
- Make sure you open the Serial Monitor.

## Conclusion

In this tutorial, we have tested out one of the many great features that comes with the MKR Zero board: the possibility to store data directly to a micro SD card. As a very basic example, we read the values of three analog pins, stored them in a `.txt` file and later viewed the data on our computer. 

The analog pins are of course not generating any useful data, as we have not connected anything to them, but you can now go looking for some interesting sensors that could provide some more useful data.

Feel free to explore the [SD](https://www.arduino.cc/en/reference/SD) library further, and try out some of the many cool functions in this library. 
