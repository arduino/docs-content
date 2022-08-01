---
author: Arduino
tags: [Yún]
title: 'Arduino Yún File Write Script'
description: 'Demonstrates how to write and execute a shell script with Process.'
---

This example writes to a file using the FileIO classes into the Yún device's filesystem. A shell script file is created in /tmp, and is executed afterwards.

## Hardware Required

- Yún board or shield

## Circuit

There is no circuit for this example.

![The circuit for this tutorial.](assets/Yun_Fritzing.png)

image developed using [Fritzing](http://www.fritzing.org). For more circuit examples, see the [Fritzing project page](http://fritzing.org/projects/)

## Code

Include the FileIO header, for communicating with the filesystem.
`#include <FileIO.h>`

In `setup()`, initialize Bridge, Serial communication, and FileSystem. Wait for an active serial connection, and call a custom function `uploadScript()` which will upload your file, before starting `loop()`.

```arduino
void setup() {

  Bridge.begin();

  Serial.begin(9600);

  while(!Serial);  // wait for Serial port to connect.

  Serial.println("File Write Script example\n\n");

  FileSystem.begin();

  uploadScript();
}
```

`loop()` will just execute your script every 5 seconds by calling another custom function, `runScript()`.

```arduino
void loop() {

  runScript();

  delay(5000);
}
```

Your `uploadScript()` function will create a shell script in the Linux file system that will check the network traffic of the Wi-Fi interface. Create the file and open it by creating an instance of the `File@ class, and calling`FileSystem.open()@@ indicating where you would like to create the script. You'll store the script in "/tmp", which resides in RAM, to preserve the limited number of FLASH memory read/write cycles.

```arduino
void uploadScript() {

  File script = FileSystem.open("/tmp/wlan-stats.sh", FILE_WRITE);
```

Write the contents of the script to the file with `File.print()`. begin by printing the header, "#!/bin/s", then the utility `ifconfig`.  @ifconfig@ is a command line utility for controlling network interfaces. you'll be looking at the Wi-Fi interface, which is referred to as "wlan0". The utility `grep` will search the output of `ifconfig`. You're looking for the number of bytes received , so search for the keywords "RX bytes" and close the file.

```arduino
script.print("#!/bin/sh\n");

  script.print("ifconfig wlan0 | grep 'RX bytes'\n");

  script.close();  // close the file
```

Instantiate a Process to make the script executable. `chmod@ is a command that will change the modes of files. By sending the`chmod@@ command and filepath, you can make your shell script run like an application.

```arduino
Process chmod;

  chmod.begin("chmod");      // chmod: change mode

  chmod.addParameter("+x");  // x stays for executable

  chmod.addParameter("/tmp/wlan-stats.sh");

  chmod.run();
}
```

The `runScript()` function will create a Process that runs the script and prints the results to the Serial Monitor.  Create a named Process, and start your script by calling `Process.begin(filepath)` and `Process.run()`.

```arduino
void runScript() {

  Process myscript;

  myscript.begin("/tmp/wlan-stats.sh");

  myscript.run();
```

Create a string to hold the output, and read the output into it

```arduino
String output = "";

  while (myscript.available()) {

    output += (char)myscript.read();

  }
```

Remove the blank spaces at the beginning and end of the string and print it to the serial monitor :

```arduino
output.trim();

  Serial.println(output);

  Serial.flush();
}
```

The complete sketch is below :

```arduino

/*

  Write to file using FileIO classes.

 This sketch demonstrate how to write file into the YunShield/Yún filesystem.

 A shell script file is created in /tmp, and it is executed afterwards.

 created 7 June 2010

 by Cristian Maglie

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/FileWriteScript

 */

#include <FileIO.h>

void setup() {

  // Setup Bridge (needed every time we communicate with the Arduino Yún)

  Bridge.begin();

  // Initialize the Serial

  SerialUSB.begin(9600);

  while (!SerialUSB); // wait for Serial port to connect.

  SerialUSB.println("File Write Script example\n\n");

  // Setup File IO

  FileSystem.begin();

  // Upload script used to gain network statistics

  uploadScript();
}

void loop() {

  // Run stats script every 5 secs.

  runScript();

  delay(5000);
}

// this function creates a file into the linux processor that contains a shell script
// to check the network traffic of the Wi-Fi interface
void uploadScript() {

  // Write our shell script in /tmp

  // Using /tmp stores the script in RAM this way we can preserve

  // the limited amount of FLASH erase/write cycles

  File script = FileSystem.open("/tmp/wlan-stats.sh", FILE_WRITE);

  // Shell script header

  script.print("#!/bin/sh\n");

  // shell commands:

  // ifconfig: is a command line utility for controlling the network interfaces.

  //           wlan0 is the interface we want to query

  // grep: search inside the output of the ifconfig command the "RX bytes" keyword

  //       and extract the line that contains it

  script.print("ifconfig wlan0 | grep 'RX bytes'\n");

  script.close();  // close the file

  // Make the script executable

  Process chmod;

  chmod.begin("chmod");      // chmod: change mode

  chmod.addParameter("+x");  // x stays for executable

  chmod.addParameter("/tmp/wlan-stats.sh");  // path to the file to make it executable

  chmod.run();
}

// this function run the script and read the output data
void runScript() {

  // Run the script and show results on the Serial

  Process myscript;

  myscript.begin("/tmp/wlan-stats.sh");

  myscript.run();

  String output = "";

  // read the output of the script

  while (myscript.available()) {

    output += (char)myscript.read();

  }

  // remove the blank spaces at the beginning and the ending of the string

  output.trim();

  SerialUSB.println(output);

  SerialUSB.flush();
}
```

**Last revision 2016/05/25 by SM**
