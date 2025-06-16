---
title: 'Over-The-Air (OTA)'
description: 'Learn how to utilize Over-The-Air (OTA), a feature that allows you to upload sketches remotely.'
tags:
  - OTA
  - Wireless upload
author: 'Jose Garcia'
---

The new Arduino Cloud brings a lot of new things, and one of them is the OTA (over-the-air) feature. This feature allows you to upload programs wirelessly to your Arduino boards. This way, as soon as you have a compatible board connected to a WiFi network and configured to work with OTA, you won’t need to physically connect the board to the computer in order to upload new sketches to it. Instead, everything will work over-the-air.


![Over-the-Air uploads.](assets/other_power_supplier.png)


Over-the-air update is now available through [Arduino Cloud](https://app.arduino.cc/) and the [Arduino Cloud Editor](https://create.arduino.cc/editor), which is an always up-to-date online IDE that stores sketches in the Cloud. It also allows you to wirelessly upload sketches from a browser, to any board that is connected to that computer. 

This tutorial will guide you through the necessary steps to configure your board to work with the OTA feature.

## Compatible Hardware

OTA is supported on several Arduino devices, as well as many ESP32 devices.

### Supported Arduino Boards

- [Arduino UNO R4 WiFi](https://store.arduino.cc/products/uno-r4-wifi)
- [Arduino MKR WiFi 1010](https://store.arduino.cc/mkr-wifi-1010)
- [Arduino Nano 33 IoT](https://store.arduino.cc/arduino-nano-33-iot)
- [Arduino Nano RP2040 Connect](https://store.arduino.cc/nano-rp2040-connect-with-headers)
- [Arduino Nano ESP32](https://store.arduino.cc/en-se/products/nano-esp32)
- [Portenta H7](https://store.arduino.cc/portenta-h7)
- [Portenta X8](https://store.arduino.cc/products/portenta-x8)
- [Portenta Machine Control](https://store.arduino.cc/products/arduino-portenta-machine-control)
- [Nicla Vision](https://store.arduino.cc/products/nicla-vision)
- [Nicla Sense ME](https://store.arduino.cc/products/nicla-sense-me)
- [Nicla Voice](https://store.arduino.cc/products/nicla-voice)
- [Portenta C33](https://store.arduino.cc/products/portenta-c33)
- [Arduino Opta WiFi](https://store.arduino.cc/products/opta)
- [Portenta H7 Lite Connected](https://store.arduino.cc/products/portenta-h7-lite-connected)
- [GIGA R1 WiFi](https://store.arduino.cc/products/giga-r1-wifi)


### Verified ESP32 Boards Supporting OTA 

The following ESP32 boards have been tested and verified to support OTA:

- ESP32-S2-DevKitC
- NODEMCU-32-S2
- WEMOS LOLIN D32
- ESP32-S3-DevKitC
- WEMOS LOLIN D32
- ESP32-CAM
- NodeMCU-32S
- Freenove ESP32 WROVER
- ESP32-DevKitC32E
- DOIT ESP32 DevKit v1

## How does it work

In order to configure the feature, we will need to create a project in the Arduino Cloud following the next steps.

**1.** Go to the [Arduino Cloud](https://app.arduino.cc/) by clicking the Cloud icon in the top right of the Arduino homepage.

![Navigating to the Cloud.](assets/iot_cloud_grid.png)

> **Note:** You will need to have an Arduino account to be able to use both the Cloud editor and Arduino Cloud features.


**2.** Once you are logged in the Arduino Cloud, you need to create a new thing and name it something, for this example let's call it “smart_led”.
    Inside the thing let’s include a boolean variable called `light`, set variable permission to **Read & Write** and select the **On Change** variable update policy. Once we have these characteristics set, click on **add variable**.


![Adding a variable.](assets/adding_variable.png)

> **Note:** If you want to know more about how to get started with the Arduino Cloud, visit the [getting started tutorial](/arduino-cloud/guides/overview).


**3.** Once you have added the variable, you’ll need to associate your device to this new thing and add your network credentials.

![Selecting a device to associate.](assets/select_device.png) 

**4.** Next step is to create a dashboard with a **Switch** widget, linked to the lights variable that you created before. Once it is set, click on the **use dashboard** button and go to **things > smart_led > Sketch**

![A switch widget.](assets/dashboard_widget.png)


**5.** It is time now to edit the sketch. Let’s create a program that turns ON/OFF the `LED_BUILTIN` embedded on your board. To do so, you will need to add just four lines of code to the auto generated sketch:
   1. Initialise as `false` the  boolean variable `led_status` at the beginning of the program.
   2. Set as `OUTPUT`  the `LED_BUILTIN` pin of the board in the `setup()` function.
   3. Modify the state of the `LED_BUILTIN` pin with the `led_status` variable in the `loop()` function. To do so, let’s use the `digitalWrite()` statement.
   4. Add the statement `led_status = !led_status` inside the `onLightChange()`auto generated function.


Check the highlighted lines in the following code to see what required changes are.

<iframe src="https://create.arduino.cc/editor/FT-CONTENT/865fd13a-03d3-484a-a7ef-8729b42716bd/preview?embed&snippet#L18,L21,L49,L53" style="height:510px;width:100%;margin:10px 0" frameborder="0"></iframe>



**6.** Once the sketch has uploaded to your board, let’s check that everything is working as it should. To do so, go back to the Arduino Cloud and once in there, go to the **smart_led** dashboard we created before. Now, when you turn the **light** widget in the dashboard ON or OFF, the LED in your board should also turn ON or OFF.

![Final dashboard.](assets/final_dashboard.png)


Now that we have checked that everything is working as it should, let’s go back to the **Things > smart_led >**  **Sketch** tab in the Arduino Cloud, and see what has happened there.

Once in the sketch tab, you'll see a toggle switch next to the board. The toggle switch lets us select a new option for connecting our board. Selecting the cloud icon instead of the USB icon means that when we upload to the board, it's done **Over the Air**.

![List of devices available.](assets/device_OtA.png)


If you select this option, you should be able to upload sketches to your board wirelessly. Let’s learn how to do it, by following the next steps.

**1.** Let’s modify the program in order to blink the LED each second when we click the button ON, and switch it Off when the button OFF is pressed.
   To do it, you will need to modify the `loop()` function by adding the highlighted lines shown in the following sketch.

<iframe src="https://create.arduino.cc/editor/FT-CONTENT/f6aa7be6-ae9c-40b9-a369-fc6e0d034514/preview?embed&snippet#L47-L54" style="height:510px;width:100%;margin:10px 0" frameborder="0"></iframe>

**2.** Power your board from a different power supplier than your computer's USB cable. Powering it through a phone charger's USB should be enough.

![img](assets/other_power_supplier.png)

**3.** Once you have powered the board from a power source other than your computer, you should only see the **Over-the-Air** option. Select it, and upload the program to the board.

![Over-the-Air board connection](assets/OtA_board_selection.png)

> **Note:** This option will take a bit longer than usual, since the process of compiling and uploading the program to the board over-the-air is a longer process.

**4.** Now, if you switch the widget on the Arduino Cloud dashboard ON and OFF, the LED will either blink every second or go off.


## But how does it work, inside?

An Arduino Cloud sketch is generated by the Arduino Cloud application, it leverages the Arduino Cloud and [Arduino Connection Handler](https://github.com/arduino-libraries/Arduino_ConnectionHandler) libraries to give your sketch IoT powers.


When uploading a sketch over-the-air:

- The sketch is compiled for the selected board type.
- The compiled file is stored in a [AWS S3](https://aws.amazon.com/s3/) bucket.
- OTA file url location is associated with the target device.
- OTA_REQ flag set to true to instruct the board to start the OTA file download.
- OTA file length/CRC is verified.
- Updated sketch is flashed on the board.


## Conclusion

In order to upload sketches Over-the-Air to your Arduino board you need:

- An [OTA Compatible board](#supported-arduino-boards).
- An **IoT Sketch** to be uploaded.


### Next steps

If you want to continue learning about amazing IoT features or projects you can check:

- [Oplà IoT Kit](https://opla.arduino.cc/)

---

### More tutorials

You can find more tutorials in the [Arduino Cloud documentation page](/arduino-cloud/).
