---
title: 'Node-RED with Arduino IoT Cloud'
compatible-products: [mkr-1000-wifi, mkr-wifi-1010, nano-33-iot, nano-rp2040-connect]
difficulty: advanced
description: 'Learn how to use Node-RED together with the Arduino IoT Cloud to create advanced automation systems.'
tags:
  - Node-RED
  - IoT Cloud
  - Automation
  - IoT
author: 'Liam Aljundi'
---

## Introduction

Node-RED is a programming tool for connecting hardware devices such as Arduino with other hardware devices, APIs, and online services easily using a web-based flow editor. It allows you to connect those different devices and services by connecting a combination of nodes that create your desired flow.

In this tutorial, we will look into the applications of using Node-RED together with the Arduino IoT Cloud. The integration of the two platforms allows us to facilitate communications between the Arduino IoT Cloud and home automation devices, send and receive data from online services such as Email and SMS, and write JavaScript code to manipulate the data.

## Goals

## Hardware & Software Requirements

- The [Arduino Create Agent](https://github.com/arduino/arduino-create-agent)
- An [Arduino account](http://create.arduino.cc/iot).

You will also need a cloud compatible board:

- [MKR 1000 WiFi](https://store.arduino.cc/arduino-mkr1000-wifi)
- [MKR WiFi 1010](https://store.arduino.cc/arduino-mkr-wifi-1010)
- [MKR WAN 1300](https://store.arduino.cc/arduino-mkr-wan-1300-lora-connectivity-1414)
- [MKR WAN 1310](https://store.arduino.cc/mkr-wan-1310)
- [MKR GSM 1400](https://store.arduino.cc/arduino-mkr-gsm-1400)\*
- [MKR NB 1500](https://store.arduino.cc/arduino-mkr-nb-1500-1413)\*
- [Nano RP2040 Connect](https://store.arduino.cc/nano-rp2040-connect)
- [Nano 33 IoT](https://store.arduino.cc/arduino-nano-33-iot)
- [Portenta H7](https://store.arduino.cc/portenta-h7)

***Please note: The MKR GSM 1400 and MKR NB 1500 require a SIM card to connect to the cloud, as they communicate over mobile networks.***

## Node-RED Setup

Setting up Node-RED is simple, we will run it locally following the steps below:

**1.** [Install a supported version of Node.js](https://nodered.org/docs/faq/node-versions) if it's not already installed.

**2.** Install Node-RED from the command line using the command `sudo npm install -g --unsafe-perm node-red`, delete `sudo` if you are using a Windows device.

**3.** Start it by running the command `node-red` in the terminal, you should see a similar output to this:

    ```shell
    $ node-red

    Welcome to Node-RED
    ===================

    30 Jun 23:43:39 - [info] Node-RED version: v1.3.5
    30 Jun 23:43:39 - [info] Node.js  version: v14.7.2
    30 Jun 23:43:39 - [info] Darwin 19.6.0 x64 LE
    30 Jun 23:43:39 - [info] Loading palette nodes
    30 Jun 23:43:44 - [warn] rpi-gpio : Raspberry Pi specific node set inactive
    30 Jun 23:43:44 - [info] Settings file  : /Users/nol/.node-red/settings.js
    30 Jun 23:43:44 - [info] HTTP Static    : /Users/nol/node-red/web
    30 Jun 23:43:44 - [info] Context store  : 'default' [module=localfilesystem]
    30 Jun 23:43:44 - [info] User directory : /Users/nol/.node-red
    30 Jun 23:43:44 - [warn] Projects disabled : set editorTheme.projects.enabled=true to enable
    30 Jun 23:43:44 - [info] Creating new flows file : flows_noltop.json
    30 Jun 23:43:44 - [info] Starting flows
    30 Jun 23:43:44 - [info] Started flows
    30 Jun 23:43:44 - [info] Server now running at http://127.0.0.1:1880/red/

    ```
**4.**  Open the Node-RED editor by going to your browser and entering `http://localhost:1880`.

For a more detailed guide, you can check [Node-RED's installation page](https://nodered.org/docs/getting-started/local).

## The Node-RED Editor

The Node-RED editor consists of four main parts:

- a header on the top containing the deploy button, main menu, and the user menu (only visible if user authentication is enabled)
- the palette on the left side, containing the available nodes
- a workspace in the middle, where flows can be created
- the sidebar on the right, containing editing tools such as a node configuration tool and a debugger

![the node red editor](./assets/nodered-intro-01.png)

You can run the simple flow shown below using Node-RED's default nodes:

- drag the **"inject"** node from the palette on the left side into the workspace in the middle
- double-click on the node to edit it
- assign a name and topic to it
- click on the dropdown menu next to *msg.payload* and choose **"string"**, then enter a random message
- click **Done**
- drag the **"debug"** node into the workspace
- connect the two nodes by dragging a wire from the message node to the debug node
- click on the debug menu from the sidebar on the right
- press Depoly from the header on the top
- finally, press on the checkbox of the message node

![Creating a simple flow](./assets/nodered-intro-02.gif)

Your message should be printed to the console on the right side.

In addition to the default nodes installed in node-RED, you can use the palette manager to install additional nodes that can be useful to creating more advanced flows. Follow the steps below to install the Arduino IoT Cloud nodes using the palette manager:

**1.** click on the menu in the header bar in the top right corner

**2.** select **"Manage palette"**

**3.** go to the "install" tab

**4.** search for "Arduino"

**5.** from the shown results, install **"@arduino/node-red-contrib-arduino-iot-cloud"**

Now, you should be able to use the Arduino IoT Cloud nodes from the palette on the left side of the editor.

## Arduino IoT Cloud API Key

## Setting Up a Thing

## Communicating with Node-RED

## Further Applications

- Obtain Client ID and Client Secret from the things webpage by clicking on Add API
- Go to NodeRED web page
- Select one Arduino node from the pallete and drag to a flow
- Double click on the node
  - set a new connection
    - select 'Add new arduino-connection...' in the field 'Connection'
    - Click edit (Pencil button)
    - Insert a connection name, Client ID and Client Secret (collected at point 1)
    - Click Add
  - Select a thing
  - Select a Property
  - Set a name
- Connect Arduino property input node to other nodes to consume data coming from a thing property.
- end a payload to the Arduino property output node to change the value of a thing property.
