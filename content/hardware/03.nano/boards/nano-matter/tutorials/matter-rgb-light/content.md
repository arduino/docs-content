---
title: 'Nano Matter RGB Ligthbulb'
difficulty: beginner
compatible-products: [nano-matter]
description: 'Learn how to build a Matter RGB ligthbulb.'
tags:
  - IoT
  - Matter
  - BLE
  - RGB
  - Lightbulb
author: 'Christopher Méndez'
hardware:
  - hardware/03.nano/boards/nano-matter
software:
  - ide-v1
  - ide-v2
  - web-editor
  - iot-cloud
---

## Overview

This tutorial will teach you how to create a Matter RGB Lightbulb to light up any room with colors. 

![RGB lightbulb overview](assets/thumbnail-v1.png)

Thanks to the seamless compatibility of the Nano Matter with almost any Matter network we can easily integrate our RGB light with Amazon Alexa, Google Assistant, Apple Home, Home Assistant and even custom assistants.

## Hardware and Software Requirements
### Hardware Requirements

- [Nano Matter](https://store.arduino.cc/products/nano-matter) (x1)
- Grove - 8x8 RGB LED Matrix (x1)
- Breadboard (x1)
- Jumper wires
- Eero 6+ WiFi Extender (Thread Border Router) (x1)
- [USB-C® cable](https://store.arduino.cc/products/usb-cable2in1-type-c) (x1)

### Software Requirements

- [Arduino IDE 2.0+](https://www.arduino.cc/en/software) or [Arduino Cloud Editor](https://create.arduino.cc/editor)
- [Amazon Alexa](https://www.amazon.com/Alexa-App/b?ie=UTF8&node=18354642011)
- [Seeed_RGB_LED_Matrix](https://github.com/Seeed-Studio/Seeed_RGB_LED_Matrix) library to control the RGB LED matrix. You can install it as .ZIP using the Arduino IDE.
- [DHT](https://github.com/mcmchris/DHT-sensor-library/tree/patch-1) library. Download from this [branch](https://github.com/mcmchris/DHT-sensor-library/tree/patch-1) so it support the Nano Matter. 

### Board Core and Libraries

The **Silicon Labs** core contains the libraries and examples you need to work with the board's components, such as its Matter, Bluetooth® Low Energy, and I/Os. To install the Nano Matter core, navigate to **File > Preferences** and in the **Additional boards manager URLs**, add the following:

`https://siliconlabs.github.io/arduino/package_arduinosilabs_index.json`

Now navigate to **Tools > Board > Boards Manager** or click the Boards Manager icon in the left tab of the IDE. In the Boards Manager tab, search for `Nano Matter` and install the latest `Silicon Labs` core version.

![Installing the Silicon Labs core in the Arduino IDE](assets/bsp-install-2.png)

## Project Setup

### Schematic Diagram

Use the following connection diagram for the project:

![Project wiring diagram](assets/diagram-v1.png)

### Programming

In the Arduino IDE upper menu, navigate to **Tools > Protocol stack** and select **Matter**.

![Matter Protocol stack selected](assets/matter-setup-2.png)

Copy and paste the following sketch:

```arduino

```

Once you uploaded the example code to the Nano Matter, open the Serial Monitor and reset the board.

![QR Code URL](assets/serial-monitor.png)

There you will find the URL that generates the QR for the Matter device commissioning.

### Commissioning 

Copy and paste the QR code URL on your favorite web browser and a unique QR code will be generated for your board.

Go to your **Google Home** app, navigate to **devices** and tap on **Add**, select the **Matter-enabled device** option and scan the QR code.

![Adding the device to Google Home app](assets/add-device.png)

![Your device is successfully added](assets/add-device-2.png)

## Final Results

Finally, you will be able to monitor your room temperature from your smartphone, hub or asking to your personal assistant.

![Temperature sensor final result](assets/temp-sensor.png)

You can also see the temperature value on the device OLED display.

## Conclusion

In this tutorial we have learned how to create a Matter enabled temperature sensor that can be monitored from our smartphone and personal assistant. The Nano Matter allows us to seamlessly integrate the sensor as a commercial product with our current smart home ecosystem.

### Next Steps

You can take this solution even further by adding the humidity measuring capability of the DHT11 sensor and integrate it as a 2nd sensor to your Matter network.