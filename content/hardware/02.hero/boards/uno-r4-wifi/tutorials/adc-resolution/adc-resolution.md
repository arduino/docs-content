---
title: 'Arduino UNO R4 WiFi ADC Resolution'
description: 'Learn how to change the ADC resolution on the UNO R4 WiFi.'
tags:
  - ADC
  - 14-bit
author: 'Karl Söderby'
---

In this tutorial you will learn how to change the analog-to-digital converter (ADC) on an **Arduino UNO R4 WiFi** board. By default, the resolution is set to 10-bit, which can be updated to both 12-bit (0-4096) and 14-bit (0-65355) resolutions for improved accuracy on analog readings.

## Goals

The goals of this tutorials are:

- Update the ADC resolution to 12/14-bit.

## Hardware & Software Needed

- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software)).
- [Arduino R4 WiFi](/hardware/uno-r4-wifi).
- [Arduino Renesas Core](https://github.com/bcmi-labs/ArduinoCore-renesas)

## Analog-to-Digital Converter (ADC) 

An analog-to-digital converter (ADC) transforms an analog signal to a digital one. The standard resolution on Arduino boards is set to 10-bit (0-1023). The UNO R4 WiFi supports up to 14-bit resolutions, which can provide a more precise value from analog signals.

To update the resolution, you will only need to use the [analogReadResolution()](https://reference.arduino.cc/reference/en/language/functions/zero-due-mkr-family/analogreadresolution/) command.

To use it, simply include it in your `setup()`, and use `analogRead()` to retrieve a value from an analog pin.

```arduino
void setup(){
  analogReadResolution(14); //change to 14-bit resolution
}

void loop(){
  int reading = analogRead(A3); // returns a value between 0-65355
}
```

## Summary

This short tutorial show how to update the resolution for your ADC, a new feature available on the UNO R4 WiFi board.