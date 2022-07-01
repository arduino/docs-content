---
title: 'Output WebGL Content on a Screen'
description: 'This tutorial shows how to install and modify a container that outputs web browser and webGL content'
difficulty: easy
tags:
  - containers
  - Docker
  - WebGL
  - Vim
author: 'Pablo Marquínez'
software:
  - Terminal
  - Docker
hardware:
  - hardware/04.pro/boards/portenta-x8
---

## Overview

The Arduino Portenta X8's processor **NXP® i.MX 8M Mini Processor** can be used for 3D rendering, this will allow us to display 3D content on a screen or video output, the device is using OpenGL to process the 3D related calculations. In this tutorial we will render web content from the internet using WebGL and display it on a screen, using an USB Hub. We will go through the steps of how to setup, install and modify the video output.

## Goals

- Setup the Video Output
- Get the required container
- Run the container
- Change the video output

### Required Hardware and Software

- [Arduino Portenta X8](https://store.arduino.cc/products/portenta-x8)
- USB-C cable (either USB-C to USB-A or USB-C to USB-C)
- USB-C hub with HDMI
- External monitor 
- HDMI cable

## Instructions

### Install The Container

There are two ways to get the container, either through `foundriesFactories` or downloading the container from [portenta-containers repository](https://github.com/arduino/portenta-containers)

**With Foundries:** 

If you use [Foundries.io](https://www.foundries.io) you can switch the current `target` of your device to `x-kiosk-imx8-webgl` by switching the app from a terminal on your computer:

```
//Change the app to an existing one
fioctl devices config updates --apps "x-kiosk-imx8-webgl" <deviceName> -f <yourFactoryName>

//Make a clean installation with no containers
fioctl devices config updates --apps "," <deviceName> -f <yourFactoryName>

//If you are getting issues to do so, make sure you are logged correctly with your token
//You can logout:
fioctl logout

//Then login again and follow the instructions
fioctl login
```

You will now see the home-screen for some seconds and then it will fade-out and open the Aquarium 3D from [WebGL samples - Aquarium](https://webglsamples.org/aquarium/aquarium.html).

**With downloaded repository:** In case you downloaded the [portenta-containers repository](https://github.com/arduino/portenta-containers) you will need to connect your board directly to your computer and run the `adb shell`, then push the container to your Portenta X8.

### Connect to a Wi-Fi

Check the available Wi-Fi access points
```
nmcli de wifi

//Output
IN-USE  BSSID              SSID             MODE   CHAN  RATE        SIGNAL  BARS  SECURITY
        AA:BB:CC:DD:EE:FF  <yourAP-SSID>    Infra  X     130 Mbit/s  --      *     WPA2
```

You can save your Wi-Fi details with these commands:
```
nmcli c add type wifi con-name <customName> ifname wlan0 ssid <SSID>
nmcli con modify <customName> wifi-sec.key-mgmt wpa-psk
nmcli con modify <customName> wifi-sec.psk <PASSWORD>
nmcli con up <customName>

//To disconnect from a custom connection
nmcli con down <customName>

//To delete a saved connection
nmcli c delete <customName>
```

If the LED is on and green then we know that has been correctly connected. If you want to check it in your terminal, you can type:
```
nmcli de

//Output
DEVICE   TYPE      STATE                   CONNECTION
usb0     ethernet  connected               usbrndis
usb1     ethernet  connected               usbecm
wlan0    wifi      connected               <customName>
docker0  bridge    connected (externally)  docker0
```

### Get Your Board's IP
```
ifconfig wlan0

//Output
wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet <localIP>  netmask 255.255.255.0  broadcast <broadcastIP>
```

Test your IP connection by exiting the `adb shell`, you can use **CTRL+Z** or typing `exit`, then try to connect through **ssh** with:
```
ssh fio@<localIP>
```
***To connect through ssh it will request the user's password, which is "fio".***
***If you have troubles connecting with the ssh, please check the troubleshooting section at the end of this tutorial***

### Copy/push the Container
You can push the container from your computer, first open a terminal on the container's directory, then you can use this command to send the container to the Portenta X8:
```
scp <folderName> fio@<portentaX8-IP>:<desiredPath>
```

### Video Output Setup

Now we need a USB Hub that has a video output connector, like for an HDMI cable. Connect the Portenta X8 to the USB Hub as a Host, the video connector to a display, the power supply USB to your computer. We could also connect a USB mouse to the hub, this step is optional.

The setup should look like this:

![X8 usb hub setup](assets/portentaX8_hub_screen.svg)

By default if you connect the board to a display you will see the "home-screen" with the `Arduino PRO` background wallpaper, and a bottom bar with the real time.

***You can interact with the interface by plugging USB devices to your hub, like a mouse or a keyboard.***

![X8 home-screen](assets/portentaX8-home-screen.png)

### Running The Container
If you got the container from **Foundries.io** it will run automatically after few seconds.

In case you copied from the repository, you will need to initialize it with **docker** by accessing your Portenta X8 through ssh, going to the directory where you copied it and run it from there:

```
//Connect to your device
ssh fio@<portentaX8-IP>

//Change directory
cd <containerPath>

//Compose with docker
docker-compose up --detach

//Stop the docker-compose
docker-compose stop
```

### Edit The Output
You can change the URL of the web output, by going to the container's directory and editing the `docker-compose.yml` file:
```
//Connect to your device
ssh fio@<portentaX8-IP>

//Change directory
cd <containerPath>

//Edit the file with VIM
vim docker-compose.yml
```

Once you are inside the **VIM** editor, to edit the file you will need to press **insert** and replace the url as shown in the screenshot.

![VIM editing docker-compose.yml](assets/vim-edit-dockerCompose.png)

To save the changes press the **ESC** key and type `:wq` this will write and quit the **VIM** editor. After editing it you will need to compose the container again.

## Conclusion

In this tutorial we went through how to connect the board and display something on a screen. Using a container from foundriesFactories or by downloading it and uploading it to your Portenta X8. Lastly, we showed how to edit the video output by editing the container.

### Next Steps

- Make your own HTML content, push it to your device and output that content.
- You could make an app that shows information about the weather in a web and having that on a display.

## Troubleshooting
- If you tried to connect with `ssh` and you get a **fingerprint** issue you will need to remove the IP and fingerprint on your `.ssh` file, on windows the file is at `C:\Users\<yourUsername>\.ssh\known_hosts` and try again the **ssh** connection.

Example:
```
//<portentaX8-ip> <type> <fingerprint>
192.168.50.8 ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAasdaddgre<kopPOTYAAABBBM8EZPWPKdRRGHpSMosJM08R1d10G0h5g5rE4cNjXdJtYpmJNOR+X2FhNRpEdvyDGHfSomJepbaqBoRcCi0Y7M=
```
