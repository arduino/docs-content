---
title: 'IoT Cloud Dashboards & Widgets'
description: 'Learn about dashboards and the different widgets that can be used to monitor & control your board.'
tags: [IoT Cloud, Widgets, Dashboards]
author: 'Karl Söderby'
difficulty: beginner
---

## Overview

An essential component of the [Arduino Cloud](https://create.arduino.cc/iot/) is a **cloud variable**. A cloud variable is the same as a regular variable that you use in an Arduino sketch, but with some additional functionality.

A cloud variable is synced between your Arduino board and the Arduino Cloud. So if a variable is updated on your board (like a sensor reading), the Arduino Cloud will also receive this value. Similarly, if you update a variable from the cloud, it also updates on your board. 

This means that at any given time, you are able to read and send data to and from your board, as long as your board is connected to the Arduino IoT Cloud.

**In this article, we will cover:**
- How to sync variables between your board and the Arduino IoT Cloud.
- What variables are available to use.
- How to structure a sketch for optimal variable synchronization.
- How to synchronize variables between devices.

`ArduinoCloud.update()`

## Create and Configure Variables

Creating and configuring variables are done inside **Thing**, starting with the **"Add Variable"** button.

![Click on "Add Variable"]()

### Variable Configuration

Inside a variable configuration, we have several options:

- **Name:** a friendly name for your variable. No spaces or special characters allowed.
- **(optional) Sync With Other Things:** sync a variable with a variable from another Thing. Whenever one variable updates, the other will follow.
- **Type:** type of variable. Choose between three categories.
  - [**Basic:**]() e.g. `float`, `int`, `String`.
  - [**Specialized:**]() e.g. `CloudAcceleration`, `CloudTemperature`, `CloudFrequency`.
  - [**Complex:**]() e.g. `CloudColor`, `CloudTelevision`.
- **Declaration:** the declaration of your variable. This is what you will use in a sketch.
- **Variable Permission:** 
  - **Read & Write:** variable can be updated from board and cloud.
  - **Read Only:** variable can only be updated from the board.
- **Variable Update Policy:**
  - **On Change:** variable synchronizes whenever value changes (threshold is `0` by default).
  - **Periodically:** variable synchronizes every `x` seconds. 

### Automatic Sketch Generation

Whenever you add, change or remove a variable, a file called `thingProperties.h` is updated automatically. This is a configuration file that should always be included in your main sketch (it is generated automatically).

Since it is defined in `thingProperties.h`, you do not need to declare it in your `.ino` file. 

Let's say we create a integer variable called `sensor_value`. To use this in a sketch, to for example read a sensor, we can use:

```arduino
sensor_value = analogRead(A0);
```

Note that we do not need to define the variable anywhere, as it has already been configured in `thingProperties.h`.

***Note that if you change a variable, you will need to upload the code to your board for the effects to come in change.***

## List of Variables

### Basic Types

| Type                  | Declaration            |
| --------------------- | ---------------------- |
| Boolean               | `bool variableName;`   |
| Character String      | `String variableName;` |
| Floating Point Number | `float variableName;`  |
| Integer Number        | `int variableName;`    |


### Specialized Types

For your convenience, IoT Cloud provides specialized types which are just wrappers around basic types but declare the variable semantics more explicitly. This enables smarter integrations with third-party services (such as Alexa) and better visualization of widgets in dashboards.

You can use them just like a normal variable of the wrapped type, since they support assignment and comparison operators.

| Type                 | Declaration                              | Wrapped data type |
| -------------------- | ---------------------------------------- | ----------------- |
| Acceleration         | `CloudAcceleration variableName;`        | `float`           |
| Angle                | `CloudAngle variableName;`               | `float`           |
| Area                 | `CloudArea variableName;`                | `float`           |
| Capacitance          | `CloudCapacitance variableName;`         | `float`           |
| Color                | `CloudColor variableName;`               | `float`           |
| Contact Sensor       | `CloudContactSensor variableName;`       | `bool`            |
| Counter              | `CloudCounter variableName;`             | `int`             |
| Data Rate            | `CloudDataRate variableName;`            | `float`           |
| Electric Current     | `CloudElectricCurrent variableName;`     | `float`           |
| Electric Potention   | `CloudElectricPotention variableName;`   | `float`           |
| Electric Resistance  | `CloudElectricResistance variableName;`  | `float`           |
| Energy               | `CloudEnergy variableName;`              | `float`           |
| Flow Rate            | `CloudFlowRate variableName;`            | `float`           |
| Force                | `CloudForce variableName;`               | `float`           |
| Frequency            | `CloudFrequency variableName;`           | `float`           |
| Heart Rate           | `CloudHeartRate variableName;`           | `float`           |
| Information Content  | `CloudInformationContent variableName;`  | `int`             |
| Length               | `CloudLength variableName;`              | `float`           |
| Light                | `CloudLight variableName;`               | `bool`            |
| Location             | `CloudLocation variableName;`            | `float`           |
| Logarithmic Quantity | `CloudLogarithmicQuantity variableName;` | `float`           |
| Luminance            | `CloudLuminance variableName;`           | `float`           |
| Luminous Flux        | `CloudLuminousFlux variableName;`        | `float`           |
| Luminous Intensity   | `CloudLuminousIntensity variableName;`   | `float`           |
| Mass                 | `CloudMass variableName;`                | `float`           |
| Motion Sensor        | `CloudMotionSensor variableName;`        | `bool`            |
| Percentage           | `CloudPercentage variableName;`          | `float`           |
| Power                | `CloudPower variableName;`               | `float`           |
| Pressure             | `CloudPressure variableName;`            | `float`           |
| Relative Humidity    | `CloudRelativeHumidity variableName;`    | `float`           |
| Smart Plug           | `CloudSmartPlug variableName;`           | `bool`            |
| Switch               | `CloudSwitch variableName;`              | `bool`            |
| CloudTemperature     | `CloudTemperature variableName;`         | `float`           |
| Temperature Sensor   | `CloudTemperatureSensor variableName;`   | `float`           |
| Time                 | `CloudTime variableName;`                | `float`           |
| Velocity             | `CloudVelocity variableName;`            | `float`           |
| Volume               | `CloudVolume variableName;`              | `float`           |


### Complex Types

The following variable types hold multiple values internally and are used to represent more complex data. In order to access such values, methods are provided.

#### DimmedLight

Declared as `CloudDimmedLight x;`

| Property   | Type            | Read value          | Set value           |
| ---------- | --------------- | ------------------- | ------------------- |
| Brightness | `float` (0-100) | `x.getBrightness()` | `x.setBrightness()` |
| Switch     | `bool`          | `x.getSwitch()`     | `x.setSwitch()`     |

#### ColoredLight

Declared as `CloudColoredLight x;`

| Property   | Type            | Read value          | Set value           |
| ---------- | --------------- | ------------------- | ------------------- |
| Switch     | `bool`          | `x.getSwitch()`     | `x.setSwitch()`     |
| Hue        | `float` (0-360) | `x.getHue()`        | `x.setHue()`        |
| Saturation | `float` (0-100) | `x.getSaturation()` | `x.setSaturation()` |
| Brightness | `float` (0-100) | `x.getBrightness()` | `x.setBrightness()` |

#### CloudColor

Declared as `CloudColor x;`.

To read the Color values, we can use the following method `Color colorValues = x.getValue();`. This will assign the hue, saturation, and brightness values to the `colorValues` variable.

| Property   | Type    | Read value        | Set value                              |
| ---------- | ------- | ----------------- | -------------------------------------- |
| Hue        | `float` | `colorValues.hue` | `x = Color(hue,saturation,brightness)` |
| Saturation | `float` | `colorValues.sat` | `x = Color(hue,saturation,brightness)` |
| Brightness | `float` | `colorValues.bri` | `x = Color(hue,saturation,brightness)` |

To set the color, we can assign the CloudColor variable directly to float variables `x = {hue,saturation,brightness}`, or using the method ` x = Color(hue,saturation,brightness)`.

#### CloudLocation

Declared as `CloudLocation x;`.

To read the location values, we can use the following method `Location coordinates = x.getValue();`. This will assign the longitude and latitude values to the coordinates variable. If we want too access the values individually we can use `Serial.println(coordinates.lat)` and `Serial.println(coordinates.lon)`.

| Property  | Type    | Read value        | Set value                   |
| --------- | ------- | ----------------- | --------------------------- |
| Latitude  | `float` | `coordinates.lat` | This variable is ready only |
| Longitude | `float` | `coordinates.lon` | This variable is ready only |

***The format of the `lat` and `lon` is in Decimal Degrees (DD), for example `41.40338`, `2.17403`.***

#### Television    
   
Declared as `CloudTelevision x;`

| Property         | Type                                                                                                                                                                                      | Read Value               | Set value                |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------ |
| Switch           | `bool`                                                                                                                                                                                    | `x.getSwitch()`          | `x.setSwitch()`          |
| Volume           | `int`(0-100)                                                                                                                                                                              | `x.getVolume()`          | `x.setVolume()`          |
| Mute             | `bool`                                                                                                                                                                                    | `x.getMute()`            | `x.setMute()`            |
| PlaybackCommands | `PlaybackCommands` (FastForward, Next, Pause, Play, Previous, Rewind, StartOver, Stop)                                                                                                    | `x.getPlaybackCommand()` | `x.setPlaybackCommand()` |
| Input            | `InputValue` ([Up to 60 values](https://github.com/arduino-libraries/ArduinoIoTCloud/blob/master/src/property/types/automation/CloudTelevision.h) such as HDMI1, HDMI2, DVD, GAME...etc.) | `x.getInput()`           | `x.setInput()`           |
| Channel          | `int`                                                                                                                                                                                     | `x.getChannel()`         | `x.setChannel()`         |

