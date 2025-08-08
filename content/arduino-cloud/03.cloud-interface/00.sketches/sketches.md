---
title: Sketches
description: Learn about sketches (programs) in the Arduino Cloud.
tags: [Arduino Cloud, Sketches, IoT Sketches]
author: Karl Söderby
---

A sketch is a file where we write programs to run on our Arduino boards. Sketches have a `.ino` extension, which supports the Arduino programming language (a variant of C++).

The Arduino Cloud has two categories of sketches:
- **Sketch** - a single `.ino` file where you write a program. These sketches can be used for **any** Arduino board. 
- **Sketch with attached Thing** - a set of files that are automatically generated when creating a [Thing](/arduino-cloud/cloud-interface/things). This includes an `.ino` file and two header (`.h`) files that contain your Thing configuration + credentials. Only available for boards with Arduino Cloud support.

In this document, we will take a look at how to use sketches in the Arduino Cloud environment.

***If you need help getting started with programming your Arduino in the online environment, check out the [Cloud Editor](/arduino-cloud/guides/cloud-editor) tutorial.***

## Access Your Sketches

You can access all your sketches at [app.arduino.cc/sketches](https://app.arduino.cc/sketches). Here you can easily see if your sketch has a Thing connected to it by checking if it has a light blue text box next to it.

![Sketches in the Arduino Cloud](./assets/sketch.png)

Clicking on each sketch will direct you to the [Cloud Editor](https://create.arduino.cc/editor/), which is an online version of the Arduino IDE. Here you can write a program, compile it and upload it to your board. 

***To get started with the Cloud Editor, check out the [Cloud Editor](/arduino-cloud/guides/cloud-editor) tutorial.***

### How to Create and Organize Folders

You can easily organize your sketches by creating folders. Here’s how you can do it:

**Create a New Folder**: Click on **Create**, then select **New Folder**.

**Move Sketches into a Folder**:

- **Drag and Drop**: Simply drag the sketch you want to move and drop it into the desired folder.

- **Right-Click and Move**: Alternatively, click the three dots on the right, choose the option "Move to folder", and then select the folder you want to move it to.

## Regular Sketches

A regular sketch in the Arduino Cloud is exactly like a sketch used in the [Arduino IDE](/software/ide-v2), with no difference whatsoever. You can take a sketch from the online IDE and compile it in the offline IDE. 

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

## Sketches with an attached Thing

Sketches with an attached Thing are more complex and are generated automatically when you create a Thing and variables.

***Read more about [Things](/arduino-cloud/cloud-interface/things/).***

### Sketch File

The sketch file is generated with a set of additional Cloud-specific methods included, the essentials being:
- `initProperties()` - initializes properties/variables from your Thing.
- `ArduinoCloud.begin()` starts the library with the preferred connection (e.g. Wi-Fi® or LoRa®-based networks).
- `ArduinoCloud.update()` - synchronizes all data between the board and the Arduino Cloud.

In addition, any variable created with a read/write permission will also generate a callback function that executes whenever the variable's value changes.
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
  //sync with Cloud  
  ArduinoCloud.update();
}

void onTestChange(){
  /*
  callback function, runs each time
  the variable value changes
  */
}
```

There are a few different options available for synchronizing your sketch with the Arduino Cloud:
- `MOST_RECENT_WINS` - The latest update whether from the device or the cloud is used. Best for real-time applications where the latest data should always be used, regardless of source.
- `CLOUD_WINS` - The cloud value always overwrites the device value. Useful when the cloud holds critical configurations or settings that should always be enforced on the device.
- `DEVICE_WINS` - The device value always overwrites the cloud value. Used when the device generates important real-time data (sensor readings) that should always be preserved over cloud updates.

It can be set in your sketch with:

```arduino
setSyncPolicy(MOST_RECENT_WINS);  // or CLOUD_WINS, DEVICE_WINS
```

### Configuration Header File

The `thingProperties.h` file is a non-editable file that updates based on changes made in your Thing. For example:

- Creating a variable will add it to this file, along with parameters such as permission, update policy, variable type etc. 
- Changing from a Wi-Fi® device to a LoRa®-enabled device will update the **connection method** stored in this file,

The file cannot be edited in the Arduino Cloud as it is in sync with the platform and changes frequently.

### Secret File

The "Secret" File contains your secret credentials, such as Wi-Fi® network SSID/PASS or device secret key, if the board is using provisioning version 1.0. If the board is using version 2.0 the credentials are stored on the board. To find out more about this read [here](https://docs.arduino.cc/arduino-cloud/hardware/device-provisioning/).

This file will be visible as a "Secret" tab in the Cloud Editor and is named `arduino_secrets.h`, which is not visible on the Cloud platform.

Note that if you are using the offline IDE / Arduino CLI, you will need to manually create this file. More information is in the **Offline Sketches section** just below.

## Offline Sketches

The Arduino Cloud provides an all-inclusive service for programming, uploading and monitoring your boards. While it is necessary to use the Arduino Cloud for configurations, you do not need to use the Cloud Editor for programming.

It is possible to work in an offline environment (such as Arduino IDE), which for many might be more desirable. To set this up, there are a few requirements and setbacks:
- You need to manually install the [ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud) and [Arduino_ConnectionHandler](https://github.com/arduino-libraries/Arduino_ConnectionHandler) libraries,
- you need to either download your sketch files and move them to your local sketch folder (e.g. `~/Documents/Arduino`), **or**
- use the [Remote Sketchbook Feature](https://docs.arduino.cc/software/ide-v2/tutorials/ide-v2-cloud-sketch-sync) feature. 

The Remote Sketchbook feature is great as you can push/pull your sketches from the Arduino Cloud. So if your `thingProperties.h` file changes, you can pull those changes as well. 

***A very important note on Remote Sketchbook: when you push/pull a sketch, you will overwrite the existing sketch, similarly to how GitHub works, but without the option of retrieving your previous sketch.***


## Recommended Code Practices (Sketches with an attached Thing)

This section highlights some important aspects of writing code with regard to the implementations in the [ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud).

### Watchdog Timer (WDT)

Arduino Cloud sketches use a **Watchdog Timer (WDT)** by default, however, not all boards support this function. The WDT can be used to automatically recover from hardware faults or unrecoverable software errors.

A WDT is essentially a countdown timer, whereas it starts counting from a set value, and upon reaching zero, it resets the board. To prevent it from reaching zero, we continuously call it from the `loop()`, using the `ArduinoCloud.update()` function.

This is why, it is very important to not use any long blocking code in your sketch. For example, using a long `delay()` inside the `loop()` is **strongly discouraged**, as the WDT can reach zero and reset the board.

The WDT can however be disabled inside of the `setup()` function, by adding the `false` parameter:

```arduino
ArduinoCloud.begin(ArduinoIoTPreferredConnection, false).
```

***You can view the source code of this implementation [here](https://github.com/arduino-libraries/ArduinoIoTCloud/tree/master/src/utility/watchdog) and you can check if your board supports this feature [here](https://github.com/arduino-libraries/ArduinoIoTCloud?tab=readme-ov-file#what).***

### Alternatives to Delays

The `loop()` function includes the `ArduinoCloud.update();` call, which sends data to the Cloud and receives updates. To get the best responsiveness in your Cloud-connected projects, the `loop()` function should run as fast as possible. This means that no blocking commands should be used inside, and you should prefer a non-blocking programming approach whenever possible.

A common **blocking pattern** is the use of the `delay()` function which stops the execution of the function for the given time. We strongly advise to **get rid of this function** and achieve the same behavior in a non-blocking way with the `millis()` function as described below.

Let's see how to blink an LED. The traditional way involves the `delay()` function:

```arduino
void loop() {
  ArduinoCloud.update();

  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

This works, but it will cause a delay of at least two seconds between one execution of `ArduinoCloud.update()` and the next one, thus causing bad performance of the Cloud communication.

This can be rewritten in a non-blocking way as follows:

```arduino
void loop() {
  ArduinoCloud.update();

  digitalWrite(LED_PIN, (millis() % 2000) < 1000);
}
```

How does this work? It gets the current execution time provided by `millis()` and divides it by 2 seconds. If the remainder is smaller than one second it will turn the LED on, and if it's greater it will turn the LED off.

For a more complex and commented example, you can have a look at the [BlinkWithoutDelay example](/built-in-examples/digital/BlinkWithoutDelay).

### I2C Usage

Components connected via I²C (including the sensors onboard the [MKR IoT Carrier](https://store.arduino.cc/products/arduino-mkr-iot-carrier)) uses the same bus as the **ECCX08** crypto chip. As the crypto chip is an essential part of establishing a connection to the Arduino Cloud (it contains the credentials), it is important that other I²C peripherals are initialized after the connection has been made.

For example, if you are initializing a library such as [Arduino_MKRENV](https://www.arduino.cc/reference/en/libraries/arduino_mkrenv), your `setup()` should be implemented as:

```arduino
void setup() {
  Serial.begin(9600);
  delay(1500);

  initProperties();

  ArduinoCloud.begin(ArduinoIoTPreferredConnection);
  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();

  //initializing the Arduino_MKRENV library
  if (!ENV.begin()) {
    Serial.println("Failed to initialize MKR ENV shield!");
    while (1);
  }
}
```


### Avoid Blocking Serial Communication

`while(!Serial) {}` loops endlessly until the Serial Monitor is opened. This is a useful practice in cases where you want to see all debug output from the start of the sketch execution. However, when building IoT systems using **`while(!Serial){}` can hinder our project from running autonomously**, stopping the board from connecting to the network and Arduino Cloud before manually opening the Serial Monitor. Therefore, it is recommended to consider removing the `while(!Serial){}` loop if it's not necessary.

A common trick is to add a **`delay(1500);` command after `Serial.begin(9600);`**. This will slightly slow down the initialization of your device but will give you some time to open the serial monitor when you're interested in seeing its output without losing the very first lines.

## Create Agent

The [Arduino Create Agent](https://github.com/arduino/arduino-create-agent) is a single binary that will appear on the menu bar and work in the background. It allows you to use the Arduino Cloud and the Arduino Cloud Editor to seamlessly upload code to any board directly from the browser.

Downloading and installing the Arduino Create Agent plugin can be done following [this quick and easy process](https://create.arduino.cc/getting-started/plugin/welcome).

The full documentation of the [Arduino Create Agent is available here](https://github.com/arduino/arduino-create-agent#readme) for more advanced usage.

## Trademark Acknowledgments

- **LoRa®** is a registered trademark of Semtech Corporation.