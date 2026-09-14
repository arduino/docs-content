---
tags: [Yún]
author: Arduino
title: 'Arduino Yún Wi-Fi Status'
description: 'Runs a pre-configured script that reports back the strength of the current Wi-Fi network.'
---

This sketch runs a script called "pretty-wifi-info.lua" installed on your Yún device in the folder /usr/bin. It prints information about the status of your Wi-Fi connection.

It uses Serial to print, so you need to connect your Yún device to your computer using a USB cable and select the appropriate port from the Port menu before it will run.

## Hardware Required

- Yún board or shield

- wireless network

## Circuit

There is no circuit for this example.

![The circuit for this tutorial.](assets/Yun_Fritzing.png)

image developed using [Fritzing](http://www.fritzing.org). For more circuit examples, see the [Fritzing project page](http://fritzing.org/projects/)

## Code

You'll first need to include the Process class :
`#include <Process.h>`

In `setup()`, start serial communication, and the Bridge. The sketch won't run until a serial connection is made.

```arduino
void setup() {

  Serial.begin(9600);

  while(!Serial);

  Serial.println("Starting bridge...\n");

  pinMode(13,OUTPUT);

  digitalWrite(13, LOW);

  Bridge.begin();

  digitalWrite(13, HIGH);  // Led on pin 13 turns on when the bridge is ready

  delay(2000);
}
```

In `loop()`, initialize a new process that will run the Wi-Fi check script. you can run the script by calling `runShellCommand()` with the path to the script.

```arduino
void loop() {

  Process wifiCheck;

  wifiCheck.runShellCommand("/usr/bin/pretty-wifi-info.lua");
```

Print out any characters returned by the script to the serial monitor, and wair for a few seconds before running again.

```arduino
while (wifiCheck.available() > 0) {

    char c = wifiCheck.read();

    Serial.print(c);

  }

  Serial.println();

  delay(5000);
}
```

The complete code is below :

```arduino

/*

  WiFi Status

 This sketch runs a script called "pretty-wifi-info.lua"

 installed on your Yún in folder /usr/bin.

 It prints information about the status of your wifi connection.

 It uses Serial to print, so you need to connect your YunShield/Yún to your

 computer using a USB cable and select the appropriate port from

 the Port menu

 created  18 June 2013

 By Federico Fissore

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/YunWiFiStatus

 */

#include <Process.h>

void setup() {

  SerialUSB.begin(9600);  // initialize serial communication

  while (!SerialUSB);     // do nothing until the serial monitor is opened

  SerialUSB.println("Starting bridge...\n");

  pinMode(13, OUTPUT);

  digitalWrite(13, LOW);

  Bridge.begin();  // make contact with the linux processor

  digitalWrite(13, HIGH);  // Led on pin 13 turns on when the bridge is ready

  delay(2000);  // wait 2 seconds
}

void loop() {

  Process wifiCheck;  // initialize a new process

  wifiCheck.runShellCommand("/usr/bin/pretty-wifi-info.lua");  // command you want to run

  // while there's any characters coming back from the

  // process, print them to the serial monitor:

  while (wifiCheck.available() > 0) {

    char c = wifiCheck.read();

    SerialUSB.print(c);

  }

  SerialUSB.println();

  delay(5000);
}
```


**Last revision 2016/05/25 by SM**
