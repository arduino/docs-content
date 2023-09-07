---
title: Microphone Tutorial
description: "Learn how to use the GIGA Display Shield's microphone."
author: Benjamin Dannegård
tags: [Display, microphone, LVGL]
---



## Hardware & Software Needed

- [Arduino GIGA R1 WiFi](/hardware/giga-r1)
- [Arduino GIGA Display Shield]()
- [Arduino IDE](https://www.arduino.cc/en/software)
- [LVGL library](https://reference.arduino.cc/reference/en/libraries/lvgl/)

## Downloading the Library and Core

Make sure the latest GIGA Core is installed in the Arduino IDE. **Tools > Board > Board Manager...**. Here you need to look for the **Arduino Mbed OS Giga Boards** and install it, the [Arduino_H7_Video library](https://github.com/arduino/ArduinoCore-mbed/tree/main/libraries/Arduino_H7_Video) is included in the core. Now you have to install the library needed for handling the image. Go to **Tools > Manage libraries..**, search for **LVGL**, and install it. This library will be used for the visual elements.

## Getting Microphone Readings

### Microphone Test Sketch

To test the microphone we can use the **PDMSerialPlotter** example sketch. This sketch can be found in **File > Examples > PDM** in the Arduino IDE. This sketch will print readings in the serial monitor. Upload the sketch and check so that readings are appearing in the serial monitor.

![]()


## Using the Microphone Readings

Now we can combine these readings with LVGL elements to visualize the readings. Lets start by creating the screen elements that will hold the bar that will react to the microphone readings.

```arduino
```

Then we can create the bar:

```arduino
```

Now we have to include the microphone readings in the sketch:

```arduino
```

And lastly make the visual elements react to the readings:

```arduino
```


## Conclusion
