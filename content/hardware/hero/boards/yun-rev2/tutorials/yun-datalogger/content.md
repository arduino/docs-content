---
tags: [Yún]
author: Arduino
title: 'Arduino Yún Yún Datalogger'
description: 'Store sensor information on a SD card.'
---

This example shows how to log data from three analog sensors to an SD card or to a USB Flash memory stick using the Bridge library. The memory is not connected to the microcontroller, but the AR9331, which is why Bridge must be used.

Prepare your memory by creating an empty folder in the root directory named "arduino". When OpenWrt-Yun finds this folder on an attached storage device, it creates a link to the memory to the "/mnt/sd" path.

You can remove the Flash memory while Linux and the sketch are running but be careful not to remove it while data is writing to the card.

## Hardware Required

- Yún board or shield

- micro-SD card or USB Flash memory stick

- analog sensors attached to analog input pins 0, 1, and 2

## Circuit

There is no circuit for this example.

![The circuit for this tutorial.](assets/Yun_Fritzing.png)

image developed using [Fritzing](http://www.fritzing.org). For more circuit examples, see the [Fritzing project page](http://fritzing.org/projects/)

## Code

Include the FileIO header, for communicating with the SD card.
`#include <FileIO.h>`

in `setup()`, initialize Bridge, Serial communication, and FileSystem (for communicating with the OpenWrt-Yun file system). Wait for an active serial connection before starting the remainder of the sketch.

```arduino
void setup() {

  Bridge.begin();

  Serial.begin(9600);

  FileSystem.begin();

  while(!Serial);

  Serial.println("Filesystem datalogger\n");
}
```

In `loop()`, create a string that starts with a timestamp to organize the data to be logged. You'll create the `getTimeStamp()` function below.

```arduino
void loop () {

  String dataString;

  dataString += getTimeStamp();

  dataString += " = ";
```

Read the data from the sensors and append them to the string, separating the values with a comma :

```arduino
for (int analogPin = 0; analogPin < 3; analogPin++) {

    int sensor = analogRead(analogPin);

    dataString += String(sensor);

    if (analogPin < 2) {

      dataString += ",";

    }

  }
```

Open the file you'll be writing the data to using a `File` object and  `FileSystem.open()`. With the modifier `FILE_APPEND`, you can write information to the end of the file. If the file doesn't already exist, it will be created. In this case, you'll be creating and writing to a file at the root directory of the SD card named "datalog.txt".

```arduino
File dataFile = FileSystem.open("/mnt/sd/datalog.txt", FILE_APPEND);
```

If the file opens successfully, write the string to it, close the file, and print the information to the Serial monitor.

```arduino
if (dataFile) {

    dataFile.println(dataString);

    dataFile.close();

    Serial.println(dataString);

  }
```

If there is a problem opening the file, send an error to the Serial monitor  :

```arduino
else {

    Serial.println("error opening datalog.txt");

  }

  delay(15000);
}
```

Last, you'll write the function `getTimeStamp()` to retrieve the time the information was read. It will be returning a string. First, create a string to hold the current time. You'll also create an instance of Process called "time". start the process and call the "date" application. "date" is a command line utility that returns the current date and the time. Using `time.addParameter()`, you'll specify the parameters D and T, which will return the date (mm/dd/yy), and the current time (hh:mm:ss). Run the process and read the result into the string.

```arduino
String getTimeStamp() {

  String result;

  Process time;

  time.begin("date");

  time.addParameter("+%D-%T");

  time.run();

  while(time.available()>0) {

    char c = time.read();

    if(c != '\n')

      result += c;

  }

  return result;
}
```

The complete sketch is below :

```arduino

/*

  SD card datalogger

 This example shows how to log data from three analog sensors

 to an SD card mounted on the YunShield/Yún using the Bridge library.

 The circuit:

 * analog sensors on analog pins 0, 1 and 2

 * SD card attached to SD card slot of the YunShield/Yún

 Prepare your SD card creating an empty folder in the SD root

 named "arduino". This will ensure that the Yún will create a link

 to the SD to the "/mnt/sd" path.

 You can remove the SD card while the Linux and the

 sketch are running but be careful not to remove it while

 the system is writing to it.

 created  24 Nov 2010

 modified 9 Apr 2012

 by Tom Igoe

 adapted to the Yún Bridge library 20 Jun 2013

 by Federico Vanzati

 modified  21 Jun 2013

 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/YunDatalogger

 */

#include <FileIO.h>

void setup() {

  // Initialize the Bridge and the Serial

  Bridge.begin();

  Serial.begin(9600);

  FileSystem.begin();

  while (!SerialUSB); // wait for Serial port to connect.

  SerialUSB.println("Filesystem datalogger\n");
}

void loop() {

  // make a string that start with a timestamp for assembling the data to log:

  String dataString;

  dataString += getTimeStamp();

  dataString += " = ";

  // read three sensors and append to the string:

  for (int analogPin = 0; analogPin < 3; analogPin++) {

    int sensor = analogRead(analogPin);

    dataString += String(sensor);

    if (analogPin < 2) {

      dataString += ",";  // separate the values with a comma

    }

  }

  // open the file. note that only one file can be open at a time,

  // so you have to close this one before opening another.

  // The FileSystem card is mounted at the following "/mnt/FileSystema1"

  File dataFile = FileSystem.open("/mnt/sd/datalog.txt", FILE_APPEND);

  // if the file is available, write to it:

  if (dataFile) {

    dataFile.println(dataString);

    dataFile.close();

    // print to the serial port too:

    SerialUSB.println(dataString);

  }

  // if the file isn't open, pop up an error:

  else {

    SerialUSB.println("error opening datalog.txt");

  }

  delay(15000);

}

// This function return a string with the time stamp

String getTimeStamp() {

  String result;

  Process time;

  // date is a command line utility to get the date and the time

  // in different formats depending on the additional parameter

  time.begin("date");

  time.addParameter("+%D-%T");  // parameters: D for the complete date mm/dd/yy

  //             T for the time hh:mm:ss

  time.run();  // run the command

  // read the output of the command

  while (time.available() > 0) {

    char c = time.read();

    if (c != '\n') {

      result += c;

    }

  }

  return result;
}
```

**Last revision 2016/05/25 by SM**
