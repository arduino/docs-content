---
beta: true
title: 'Portenta X8 Getting Started (Beta)'
description: 'Learn how to set up the Portenta X8 (Beta)'
difficulty: medium
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

## Connecting to the Board

Once the Portenta X8 is plugged in via USB, you can open your browser and go to http://192.168.7.1 if you use Windows and Linux or http://192.168.8.1 on MacOS. This web page is hosted on the Portenta X8, from this dashboard you will be able to:

![Board set up page](assets/x8-oob-main.png)

* [Configure Wi-Fi](#connecting-to-your-wi-fi)
* [Add your device to a factory (OTA)](#add-a-new-device-to-your-factory)
* Board details
* Shell (alpine python)

## Connecting to Your Wi-Fi

Click the Wi-Fi button to start configuring your network connection.

![Select wifi on set up page](assets/x8-oob-main-wifi.png)

Select your Wi-Fi SSID.

![Wifi ssid set up](assets/x8-oob-wifi-ssid.png)

Type the password.

![Wifi password set up](assets/x8-oob-wifi-pass.png)

Once its connected you should see the Wi-Fi status dot in the bottom left turn green.

![Wifi connection done](assets/x8-oob-wifi-sucess.png)

***You can change your network by clicking on the button again and repeat the steps***

## Connect to a Factory

### Register the factory on foundries.io

Go to [https://create.arduino.cc](https://create.arduino.cc) and click on the portenta-X8 board manager, you will get prompted to set a new `Factory` name if you didn't have one before. The name will not be able to be changed later, so use one that you can remember and write easily.

![Arduino Cloud integration](assets/cloud-main.png)

It will redirect you to foundries factory registration page.

![Foundries Factory creation](assets/foundries-create-factory.png)

Then you can go to [https://app.foundries.io/factories](https://app.foundries.io/factories) and it will show the factory you just created.

![Foundries Factories](assets/foundries-factories.png)

After you have created your Foundries.io factory you need to go back to the Portenta-X8 web dashboard to add a new device into your new factory.

### Add a new device to your factory

Click the "Register Factory name" button.

![Register factory button](assets/x8-oob-main-factory.png)

![Factory connection](assets/x8-oob-factory-name.png)

The next panel gives you a code that you need to copy.

![Device factory token](assets/x8-oob-factory-register.png)

Click on the "Complete registration" button  from the Portenta X8 dashboard

The button will open the foundries activation page. Paste your token on the prompt and press continue.

![Foundries device link](assets/foundries-activation-token.png)

Confirm the addition of the new device by pressing "Connect"

![Foundries device confirmation](assets/foundries-activation-prompt.png)

Finally you will see a confirmation which means that your device now is attached to the new factory.

![](assets/foundries-activation-success.png)

Once it is completed the factory button on the Portenta X8 dashboard will turn green.

![Successful connection](assets/x8-oob-factory-success.png)

#### Check your factory

Have a look to your factories by going to [Foundries factories page](https://app.foundries.io/factories)

![](assets/foundries-factories.png)

Select the factory that you want to check and it will open its dashboard.

![](assets/foundries-factory-dashboard.png)

#### Check your device

You can check that your device is fully connected inside your factory by going to the "devices" tab

![](assets/foundries-factory-devices.png)

Then chose the device you want to check by clicking on its box and it will open its page.

![](assets/foundries-activation-device-page.png)

## Controlling Portenta X8 Through the Terminal

You have plenty of ways to communicate with your board, be it wirelessly or with a cable. Next we are going to show how to use adb and ssh.

### ADB

First of all make sure you have the latest **Mbed OS Portenta Core**, which contains the adb program.
You can go to its directory inside the **Arduino15/packages/arduino/tools/adb/32.0.0**. To check the tool you can use your teminal and type `adb`, you should get feedback from the tool when typing this.

To know the list of devices that can be accessed type `adb devices`.

If you only see one device you can try and type `adb shell`, you are now communicating with your Portenta X8.

![Terminal using ADB](assets/adb-connection.png)

### SSH

SSH is commonly used for remote control on different kinds of devices running different set ups through TCP-IP.

To communicate with your board, you will need to know the IP of it, and just type `ssh fio@<IP>`, then the terminal workaround should be the same as ADB. The password is `fio`.

![SSH connection](assets/ssh-connection.png)
As it is a linux device, you can do normal stuff like creating files, changing directory, etc.

To gain admin (root) access, type `sudo su -` and the password is `fio`  after that the terminal prefix should turn red.

![CLI configured](assets/ssh-connection-admin.png)

### Inspecting Real Time Tasks

Run: `journalctl -f` to see what's going on on the device

![Real time tasks on CLI](assets/command-journalctl.png)