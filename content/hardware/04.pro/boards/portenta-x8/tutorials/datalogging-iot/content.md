---
title: 'Data Logging with MQTT, Node-RED, InfluxDB and Grafana'
description: 'This tutorial will show you how to set up a local data logging application using an MQTT broker, Node-RED, InfluxDB, Grafana, and the Arduino® Portenta X8.'
difficulty: Intermediate
tags:
  - Docker
  - MQTT
  - Mosquitto
  - Node-RED
  - InfluxDB
  - Grafana
author: 'José Bagur, Taddy Chung'
software:
  - Terminal
  - Docker
hardware:
  - hardware/04.pro/boards/portenta-x8
---

## Overview

This tutorial will set up a typical Internet of Things (IoT) application: an MQTT data logger. For this application, we are going to use what we call in the Arduino team the "IoT-Quartet," four common building blocks that are popular and regularly used in these types of applications:

- Mosquitto (MQTT broker) 
- Node-RED
- InfluxDB
- Grafana

These four blocks will be running locally on the Portenta X8 board. We will use sensor data gathered using an Arduino MKR WiFi 1010 board to test the data logging application.

## Goals

- Install, configure and run Mosquitto (MQTT broker) locally in the X8
- Install, configure and run Node-RED locally in the X8
- Install, configure and run InfluxDB locally in the X8
- Install, configure and run Grafana locally in the X8
- Send sensor data from an Arduino® MKR WiFi 1010 board to the data logging application running locally in the X8

## Required Hardware and Software

- [Arduino® Portenta X8](https://store.arduino.cc/products/portenta-x8)
- [Arduino® MKR WiFi 1010](https://store.arduino.cc/products/arduino-mkr-wifi-1010)
- USB-C cable (either USB-C to USB-A or USB-C to USB-C)
- 10KΩ potentiometer (x1)
- Breadboard and jumper cables
- Wi-Fi Access Point (AP) with Internet access
- ADB or SSH
- Command-line interface
- [Arduino IDE 2.0](https://www.arduino.cc/en/software)
  
***If you are new to the Portenta X8 board, check out this [getting started tutorial](/tutorials/portenta-x8/out-of-the-box#controlling-portenta-x8-through-the-terminal) on how to control your board using a terminal or command-line interface.***

## IoT Architecture 101

IoT applications and devices are everywhere nowadays, even in places we don't think about there being a device or application connected to the Internet. Rather than a single technology, **IoT is a concept** that refers to the connection of everyday devices, just like your watch, to the Internet and how that Internet connection creates more and different ways to interact with your device and your environment. Interactions between humans and devices or applications create **data** (lots) that must be communicated and processed. 

How can we plan, build and deploy IoT solutions? To answer that question, we must think about **IoT architecture**. Due to the different IoT devices and applications that exist and can exist, there is not just one unique architecture for IoT devices and applications. But, we can talk about a base architecture that can be considered as a starting point for every IoT project. This base architecture consists of **three essential layers**: **perception** (or devices), **network**, and **application**. Let's talk more about these layers:

- **Perception layer**: this is the sensor's layer, where data comes from. In this layer, data is gathered with one or more sensor nodes; actuators, that answer to data collected from sensor nodes, are also in this layer.
- **Network layer**: this is the layer where data from sensor nodes is recollected and then transmitted to back-end services, such as databases. 
- **Application layer**: this layer is what the device or application user sees and interacts with, for example, a dashboard. 

The three-layer IoT architecture can be a starting point for designing and implementing an IoT device or application. In this tutorial, we are going to take this base architecture and set up a data logging application, as shown in the image below:

![IoT application high-level architecture.](assets/x8-data-logging-img_01.png)

In the high-level architecture described in the image above:

- The perception layer consists of an MKR WiFi 1010 board; this board will gather information from a sensor. 
- The network layer consists of the MQTT broker (Mosquitto), the data forwarder (Node-RED), and the database (InfluxDB). 
- The application layer consists of a dashboard (Grafana) where information from the sensor node is shown.

***For documentation purposes, we are going to explain, step by step, the installation process of each part of the application (Mosquitto, Node-RED, InfluxDB, and Grafana); this process can be done quickly using a unique Compose `YAML` file. If you are familiar with Containers in Docker, you can skip to this section of the tutorial.***

Let's start by configuring the MQTT broker!

## Installing Mosquitto

Let's start by creating a new directory in our Portenta X8 called `mqtt`; inside this directory, we are going to make a file named `docker-compose.yml`: 

```
# mkdir mqtt
# cd mqtt
# export TERM=xterm
# stty rows 36 cols 150
# sudo vi docker-compose.yml
```

***The `export TERM=xterm` and `stty rows 36 cols 150` commands enable VI editor full screen.*** 

Inside VI editor, copy and paste the following:

```
services:
        mqtt:
                container_name: mosquitto
                image: eclipse-mosquitto
                restart: always
                ports:
                        - "1883:1883"
                        - "9001:9001"
                volumes:
                        - /var/rootdirs/home/root/mqtt/config:/mosquitto/config
                        - /var/rootdirs/home/root/mqtt/data:/mosquitto/data
                        - /var/rootdirs/home/root/mqtt/log:/mosquitto/log
volumes:
        config:
        data:
        log:
```

***`1883` is a standard MQTT port; `8883` port is usually used for TLS secured MQTT connections.***

Save the file and exit VI editor. Save the file and exit VI editor. Return to the `mqtt` directory and run the following command:

```
mqtt# docker-compose up -d
```

You should see the following output, as shown in the image below:

**ADD IMAGE HERE**

Now, the Mosquitto broker should available on your Portenta X8 `IP address`. You can retrieve the `IP Address` of your board with the `ping <hostname>` command: 

```
# ping portenta-x8-a28ba09dab6fad9
PING portenta-x8-a28ba09dab6fad9 (192.168.1.111) 56 data bytes
```

We should see inside the `mqtt` directory three folders (`config`, `data`, and `log`) and the `docker-compose.yml` file we created before. Go to the `config` directory and make a file named `mosquitto.conf`:

```
mqtt# ls
config  data  docker-compose.yml  log
mqtt# cd config
/mqtt/config# sudo vi mosquitto.config
```

Inside VI editor, copy and paste the following:

```
persistence true
persistence_location /mosquitto/data/
log_dest file /mosquitto/log/mosquitto.log
```

Save the file and exit VI editor. Now, let's restart the Mosquitto container so the configuration file can start working. This can be done by using the `docker restart` command and the Mosquitto `CONTAINER ID`. To identify the Mosquitto `CONTAINER ID`, run the `docker ps` command and copy the ID, as shown in the image below:

**ADD IMAGE HERE**

Now, let's manage password files by adding a user to a new password file. For this, we need to run the `sh` command in the mosquitto container with the mosquitto `CONTAINER ID` found before as shown below:

```
/mqtt/config# docker exec -it CONTAINER ID sh
/ # 
```

Let's dissect that command. `docker exec` runs a command in a running container (in this case, the Mosquitto container), `-it CONTAINER ID sh` attaches a terminal session into the running container so we can see what is going with the container and interact with it. Now, in the terminal session with the Mosquitto container, run the following command:

```
/ # mosquitto_passwd -c /mosquitto/config/mosquitto.passwd guest
```

This command creates a new password file (`mosquitto.passwd`), if the file already exists, it will be overwritten; `guest` is the username. After entering the username, we would need to define a password for the username and then, exit the terminal session with the `exit` command: 

```
/ # mosquitto_passwd -c /mosquitto/config/mosquitto.passwd guest
Password:
Reenter password:
/ # exit
```

Now, let's return to the `config` directory, you should see now inside this directory the `mosquitto.passwd` file. Open the `mosquitto.config` file and add the following information to it:

```
password_file /mosquitto/config/mosquitto.passwd
allow_anonymous true

listener 1883
listener 9001
protocol websockets
```

The file should see now like this:

```
persistence true
persistence_location /mosquitto/data/
log_dest file /mosquitto/log/mosquitto.log

password_file /mosquitto/config/mosquitto.passwd
allow_anonymous true

listener 1883
listener 9001
protocol websockets
```

Save the file and exit VI editor; also, we need to restart the Mosquitto container so the configuration file can start working. This can be done by using the `docker restart` command and the Mosquitto `CONTAINER ID`. After restarting the container, the local Mosquitto broker should be ready. Let's test it!

### Testing Mosquitto

To test the Mosquitto broker, we need an MQTT client. We can use several ways to implement an MQTT client, one of the easiest ways is to install an MQTT client in our web browser and use it to test the connection between the local MQTT broker on the Portenta X8 board and the web-based MQTT client. In this tutorial, we will use MQTTBox, a Google Chrome extension that works as an MQTT client.

In MQTTBox, let's start by configuring the settings of the MQTT client. The information we are going to need is the following:

- **MQTT client name**: in this example, Portenta X8 MQTT Broker
- **Protocol**: mqtt/tcp
- **Username**: the one you define previously in the tutorial
- **Password**: the one for the user you define previously in the tutorial
- **Host**: This is your Portenta X8 board IP address

Leave everything else as default and save the settings of the client. If everything is ok, you should see now that the MQTT client connected with the local MQTT broker in our Portenta X8 board. Success! We can now start sending messages to the MQTT broker.

## Installing Node-RED

The simplest form to run Docker is by using the following command:

```
docker run -it -p 1880:1880 -v node_red_data:/data --name mynodered nodered/node-red    
```

With this command, we are going to run the Node-RED container locally in our Portenta X8 board. Let's dissect the command:

- `-it`: a terminal session is attached to the container so we can see what is happening with the container
- `-p 1880:1880`: Node-RED local port `1880` connects to the exposed internal port `1880` 
- `v node_red_data:/data`: a docker named volume called `node_red_data` in mounted to the container `/data` directory. This permits to any changes to the flow to persist
- `--name mynodered`: a friendly local name
- `nodered/node-red`: the image to base it on

After running the command, we should see a running instance of Node-RED in the terminal:

We can detach the terminal with `Ctrl-p` `Ctrl-q`. This doesn't stop the container, the container will be running in the background. The local instance of Node-RED should be ready. Let's test it!

### Testing Node-RED

Browse to `http://{your-portenta-ip}:1880`, this will open Node-RED desktop as show in the image below:

Node-RED desktop is a GUI that let us work with Node-RED flows graphically. Let's test Node-RED flows by connecting to the local MQTT broker we set up before. Go to the `Nodes` section in the left part of the browser, search for `network` and choose the `mqtt in` node. Drag the node and drop it in the workspace. Then, search for the `debug` node and drop it also in the workspace. Connect both nodes, it should look like in the image below:



## Installing InfluxDB

### Testing InfluxDB

## Installing Grafana

### Testing Grafana

## Sending Sensor Data Using the MKR WiFi 1010

## Conclusion

### Next Steps