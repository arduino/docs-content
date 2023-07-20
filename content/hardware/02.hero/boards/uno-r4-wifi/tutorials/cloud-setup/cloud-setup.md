---
title: UNO R4 WiFi Cloud Setup
description: A step-by-step guide on how to set up the UNO R4 WiFi with the Arduino IoT Cloud
author: Hannes Siebeneicher
tags: [UNO R4 WiFi, IoT Cloud]
---

Thanks to the ESP32-S3 the UNO R4 WiFi comes with WiFi compatibilities which means you can use it with Arduino's IoT Cloud. This article shows you how to set up your board and connect it to the cloud allowing you to upload code through the air, create dashboards to monitor your data, or control your Arduino remotely.

## Software & Hardware Needed

- [Arduino UNO R4 WiFi](https://store.arduino.cc/uno-r4-wifi)
- [Arduino IoT Cloud](https://create.arduino.cc/iot/things)

## Setup and Process

***If you haven't used the Arduino IoT Cloud before check out [Getting Started With the Arduino IoT Cloud](/arduino-cloud/getting-started/iot-cloud-getting-started)***

To use the Arduino IoT Cloud you will need to register and set up a **free** account. 

### Configure Your Board

After you have set up your account you can connect your board to your pc. Inside the IoT Cloud Things overview click on **Create**.

![Create new Thing](.assets/thingsOverview.png)

This will take you to the setup menu for creating your Thing. Here you can set up your device, configure your network connection and add cloud variables. You will learn more about cloud variables in the following steps. First, under associate device, click on **Select Device**.

![Select Device](.assets/selectDevice.png)

Then click on **Set Up New Device**.

![Set Up New Device](.assets/setUpNewDevice.png)

You can now choose between three different options depending on what type of board you are using. In our case, using the UNo R4 WiFi continue by clicking on **Arduino board**.

![Select Arduino](.assets/selectArduino.png)

If this is your first time using the Arduino IoT Cloud you will be asked to download the **Arduino Create Agent** in the following step. The Create Agent is a piece of software that is necessary for your Arduino Board to communicate with the IoT Cloud. Download and install it by clicking on Download and following the installation process.

![Arduino Create Agent](.assets/createAgent.png)

When the installation is finished you will see a short loading screen and once your board has been found continue by pressing **configure**.

![Configure Device](.assets/configureDevice.png)

Now it's time to give your board a name. Name it whatever you want, as long as it doesn't contain any special characters. We advise you to choose a name that is related to your project making it easier when you have multiple boards set up. If you are out of ideas you can also press the arrow button which will give you a random name.

Once you have chosen a name that you are happy with press next and the next parts need a little bit more attention. Because the UNO R4 WiFi doesn't have a crypto chip it needs a **secret key** that works as an identifier, guaranteeing a safe connection. That secret key is shown to you in the next step and you can either download a pdf containing all the information you need to save or copy and paste the secret key and the device ID.

***Note: If you don't save the **secret key** you will not be able to continue with the next step so make sure you document and save it!***

![Secret Key](.assets/secretKey.png)

To use the UNO R4 with the IoT Cloud you will also need to update the firmware. Luckily we have simplified the normally somewhat tricky part of flashing new software to the microcontroller. Depending on what operating system you are using read the respective description but the basic steps are the same regardless of what you are using. 

![Update Board](.assets/updateDevice.png)

**Step 1**
[Download the latest firmware](https://github.com/arduino/uno-r4-wifi-usb-bridge/releases/download/0.2.0/unor4wifi-update-windows.zip) and unzip it

**Step 2**
Unplug all the USB devices except for your UNO R4.

**Step 3**
Open the update.bat file - if a warning dialog appears, click on "More info" and then "Run anyway"

**Step 4**
Follow the steps inside the terminal and select your board from the device list (if you still see more than one device after unplugging everything apart from the board, check under Windows Device Manager)

**Step 5**
Once done, unplug the board, connect it again and click "Done" to finish the setup.

If all the previous steps were done successfully you should be greeted by a prompt telling you that you can now use the board with the IoT Cloud.

![Finish set up](.assets/finishSetUp.png)

### Network Configuration

We are almost done with the setup and in the following step, you will need the **secret key** previously saved. Under Network click on **configure** and add your Wi-Fi® credentials as well as your secret key.

![Network Configuration](.assets/network.png)

## Summary

You have now successfully set up your UNO R4 WiFi to work with the IoT Cloud. If you want to learn how to create projects using the IoT Cloud check out [Getting Started With the Arduino IoT Cloud](arduino-cloud/getting-started/iot-cloud-getting-started)