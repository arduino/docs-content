---
title: Sketches
description: Learn about sketches (programs) in the Arduino Cloud.
tags: [Arduino Cloud, Sketches, IoT Sketches]
author: Karl Söderby
---

A sketch is a file where we write programs to run on our Arduino boards. Sketches have a `.ino` extension, which supports the Arduino programming language (a variant of C++).

The Arduino Cloud has two categories of sketches:
- **Regular sketch** - a single `.ino` file where you write a program. These sketches can be used for **any** Arduino board. 
- **IoT Sketch** - a set of files that are automatically generated when creating a [Thing](/arduino-cloud/cloud-interface/things). This includes a `.ino` file, and two header (`.h`) files that contains your Thing configuration + credentials. Only available for boards with IoT support.

In this document we will take a look at how to use sketches in the Arduino Cloud environment.

## Access Your Sketches

You can access all your sketches at [app.arduino.cc/sketches](app.arduino.cc/sketches), where you can easily select between your regular sketches, and IoT sketches.

![Sketches in the Arduino Cloud.](assets/sketch.png)

Clicking on each sketch will direct you to the [Cloud Editor](https://create.arduino.cc/editor/), which is an online version of the Arduino IDE. Here you can write a program, compile it and upload it to your board. 

***To get started with the Cloud Editor, check out the [Cloud Editor Guide](/arduino-cloud/cloud-editor/getting-started-cloud-editor).***

## Regular Sketches

A regular sketch in the Arduino Cloud are exactly like sketches used in the [Arduino IDE](/software/ide-v2), with no difference whatsoever. You can take a sketch from the online IDE and compile it in the offline IDE. 

A regular sketch only has two minimum requirements: the inclusion of the `void loop()` and `void setup()` functions, which are required for any Arduino sketch.

```arduino
void setup(){
    //code runs once
}

void loop(){
    //code loops infinitely
}
```

If you are new to the Arduino environment, you can check out the [Language Reference](https://www.arduino.cc/reference/en/), which contains all the functions that you can use for **all** Arduino boards. 

For specific features of a board, make sure to check out the [hardware documentation](/).

## IoT Sketches

IoT sketches are more complex, and are generated automatically when you create a Thing and variables.

***Read more about this in the [Automatic Sketch Generation](/arduino-cloud/cloud-interface/sketches) documentation.***

### Sketch File

This sketch file is generated with a set of additional cloud specific methods included, the essentials being:
- `initProperties()` - initializes properties/variables from your Thing.
- `ArduinoCloud.begin()` starts the library with the preferred connection (e.g. Wi-Fi® or LoRaWAN®).
- `ArduinoCloud.update()` - synchronizing all data between board and Arduino Cloud

In addition, any variables created with a read/write permission will also generate a callback function that executes whenever the variable's value changes.
- If you create a variable called `test`, the function will render as `void onTestChange(){}`

Below is an example of how a default sketch looks like:

```arduino
#include "thingProperties.h"

void setup(){
  Serial.begin(115200);
  delay(1500);

  //initialize the variables/properties  
  initProperties();

  //debug information  
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);
  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();
}
void loop() {
  //sync with cloud  
  ArduinoCloud.update();
}

void onTestChange(){
  /*
  callback function, runs each time
  the variable value changes
  */
}
```

### Configuration Header File

The `thingProperties.h` file is a non-editable file that updates based on changes made in your Thing. For example:

- Creating a variable will add it to this file, along with parameters such as permission, update policy, variable type etc. 
- Changing from a Wi-Fi® device to LoRa® device will update the **connection method** stored in this file,

The file cannot be edited in the Arduino Cloud as it is in sync with the platform and changes frequently.

### Secret File

The "Secret" File contains your secret credentials, such as Wi-Fi® network SSID/PASS or device secret key.

This file will be visible as a "Secret" tab in the Cloud Editor, and is named `arduino_secrets.h`, which is not visible in the cloud platform.

Note that if you are using the offline IDE / Arduino CLI instead, you will manually need to create this file. More information in the **Offline Sketches section** just below.

## Offline Sketches

The Arduino Cloud provides an all-inclusive service for programming, uploading and monitoring your boards. While it is necessary to use the Arduino Cloud for configurations, you do not need to use the Cloud Editor for programming.

It is possible to work in an offline environment (such as Arduino IDE), which for many might be more desirable. To set this up, there are a few requirements and setbacks:
- You need to manually install the [ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud) and [Arduino_ConnectionHandler](https://github.com/arduino-libraries/Arduino_ConnectionHandler) libraries,
- you need to either download your sketch files and move them to your local sketch folder (e.g. `~/Documents/Arduino`), **or**
- use the [Remote Sketchbook Feature](https://docs.arduino.cc/software/ide-v2/tutorials/ide-v2-cloud-sketch-sync) feature. 

The Remote Sketchbook feature is great as you can push/pull your sketches from the Arduino Cloud. So if your `thingProperties.h` file changes, you can pull those changes as well. 

***A very important note on Remote Sketchbook: when you push/pull a sketch, you will overwrite the existing sketch, similarly to how GitHub works, but without the option of retrieving your previous sketch.***