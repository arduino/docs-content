---
title: 'Portenta X8 Getting Started (Beta)'
description: 'Learn how to set up the Portenta X8 (Beta)'
difficulty: medium
beta: true
tags:
  - Beta
  - Installation
  - OTA
  - Embedded Linux
author: 'Pablo Marquínez'
hardware:
  - hardware/04.pro/boards/portenta-x8
software:
  - ide-v1
  - ide-v2
  - web-editor
  - iot-cloud
---

## Connecting to the board

Once the Portenta X8 its plugged via USB, you can open your browser and go to http://192.168.7.1 and see a web which is hosted by the board, from this dashboard you will be able to:

![](assets/x8-oob-main.png)


* [Configure Wi-Fi](#connecting-to-your-wi-fi)
* [Register the factory (OTA)](#registering-a-factory)
* Board details
* Shell

## Connecting to your Wi-Fi

Click the Wi-Fi button to start configuring your network connection.

![](assets/x8-oob-  main-wifi.png)

Select your Wi-Fi SSID

![](assets/x8-oob-wifi-ssid.png)

Type the password
![](assets/x8-oob-wifi-pass.png)

Once its connected you should see the Wi-Fi status button on green.

![](assets/x8-oob-wifi-sucess.png)


***You can change your network by clicking again on the button and repeat the steps***

## Registering a Factory

Click the "Register with Factory" button, and set your new factory name.

![](assets/x8-oob-factory-name.png)

Click register, now you will get a code that you need to paste into your factory page by openning [Arduino Create Cloud](https://create.arduino.cc) in your browser and click inside the integrations section "Portenta X8 Board Manager

![](assets/cloud-main.png)

Once it succeed the factory button will turn to green.

![](assets/x8-oob-wifi-sucess.png)


## Controlling Portenta X8 through the terminal

You have plenty of ways to communicate with your board, we are going to show adb and ssh.

### ADB

First of all make sure you have the latest Mbed Portenta Core, which contains the adb program.
You can go to its directory inside the Arduino15/packages/arduino/tools/adb/32.0.0, to check the tool you can type on your terminal `adb` you should get feedback from the tool.

To know the list of devices that can be accessed type `adb devices`.

If you see only one you just can type `adb shell` if it succeed, you are now communicating to your Portenta X8.

### SSH

SSH is commonly used for remote control on a different kind of devices running different set ups through TCP-IP.

To communicate with your board, you will need to know the IP of it, and just type `ssh fio@<IP>`, then the terminal workaround should be the same as ADB.  

The password is `fio`.

![](assets/ssh-connection.png)
As it is a linux device, you can do normal stuff like creating files, changing directory, etc.

To gain admin (root) access, type `sudo su -` and the password is `fio`  after that the terminal prefix should turn red.

![](assets/ssh-connection-admin.png)

### Inspecting real time tasks

Run: `journalctl -f` to see what's going on on the device

![](assets/command-journalctl.png)

## Uploading an Arduino Sketch

Make sure you have the latest mbed Core and as every other board you can select the board inside the `mbed Portenta`.

![](assets/IDE-boards.png)

And click compile and upload.

***Make sure you don't share GPIOs on the linux side and the Arduino sketc, this will avoid possible errors***