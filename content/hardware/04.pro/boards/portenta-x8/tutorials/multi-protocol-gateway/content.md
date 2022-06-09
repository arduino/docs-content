---
title: 'Build Multi-Protocol Gateway With Portenta X8 & Max Carrier'
description: 'This tutorial shows on how to setup multi-protocol gateway environment on Portenta X8 using Max Carrier'
tags:
  - containers
  - Docker
  - LoRa
  - WiFi
  - Sensor
  - RPC
author: 'Taddy Ho Chung, José Bagur'
software:
  - Terminal
  - Docker
hardware:
  - hardware/04.pro/boards/portenta-x8
---

## Overview

Portenta X8 has the NXP® i.MX 8M Mini MPU (Linux) and STM32H747XI dual Cortex®-M7+M4 32bit low power ARM® MCU (Arduino) stacked together and can be used to design different work loads for these two different microprocessors. We will use the Portenta Max Carrier to lend its onboard the CMWX1ZZABZ-078 LoRaWAN® module from Murata®, and WiFi connectivity from Portenta X8 to build a Multi-Protocol Gateway.

In this tutorial we will go through the steps of how to setup both Linux and Arduino side. A device collecting sensor data will transfer the data via WiFi Connectivity, receive the data and exchange between Arduino and Linux layers to use the LoRaWAN to finally send the information to The Things Network. 

## Goals

- Establish Sensor readings from Arduino part on Portenta X8.
- Obtain data from sensor using WiFi connection from Arduino part on Portenta X8.
- Establish LoRa connection to send sensor data to The Things Network from Linux part on Portenta X8.

### Required Hardware and Software

- [Arduino Portenta X8](https://store.arduino.cc/products/portenta-x8)
- [Arduino Portenta Max Carrier](https://docs.arduino.cc/hardware/portenta-max-carrier)
- USB-C cable (either USB-C to USB-A or USB-C to USB-C)
- Wi-Fi Access Point with Internet Access
- 868-915 MHz antenna with SMA connector
- ADB or SSH. [Check how to connect to your Portenta X8](docs.arduino.cc/tutorials/portenta-x8/out-of-the-box#controlling-portenta-x8-through-the-terminal)

## Multi-Protocol Gateway 101

![Multi-Protocol Gateway Architecture Overview](assets/.png)

A gateway is a network node and a key-point for data exchange between different netoworks under certain given specification. Simply referred as a hardware that relies between two networks. On the other hand, a **multi-protocol gateway** goes one step further by implementing variety of protocols in a single gateway. 

The idea of **Multi-Protocol Gateway** is to build a device that will establish a information relay, that handles incoming and outgoing traffic of data using different connectivity protocols.

This means that the gateway can receive the data transmitted in certain protocol type and relay the data in a different protocol for a remote server. Such capability provides the ability to develop on distinctive types of protocols and relay the data with less complexity involving in one's end. 

The Portenta X8 paired to Portenta Max Carrier has the potential to create synergy, and you will have following tools at disposal:

- WiFi (MQTT Protocol)
- Bluetooth Low Energy
- LoRaWAN (The Things Network)
- NB-IoT & Cat-M1

![Multi-Protocol Gateway and Scalability Overview](assets/.png)

Bear in mind, that this present tutorial emphasizes on making a multi-protocol gateway using previous connectivity modules. Yet, this Portenta combination still has much to offer. To get the most out of this Portenta configuration, we will go step by step on establishing the multi-protocol gateway and add scalability to expand its capability. 

Foremost, you will get to know how the multi-protocol gateway will be implemented in Portenta X8 paired with Max Carrier. Few of the tutorials will be referenced to guide you through the present tutorial, as it involves mechanisms that are extensive to cover in this tutorial.

## Arduino Layer

The Arduino layer is extended within the M4 Core and the layer to go on development with if real time operations requires to be addressed. Thus, you can use the Arduino Layer to perform PID tasks and make the RPC calls to exchange the data with the Linux layer. 

***To learn about how to exchange data using RPC between Arduino and Linux layer, please read ["Data Exchange Between Python on Linux and an Arduino Sketch"](https://docs.arduino.cc/tutorials/portenta-x8/python-arduino-data-exchange)***

In this tutorial, you will learn how to involve the RPC to expose the data received at the Linux layer on Arduino layer if further development requirement requires to feed the data at devices interfaced communicating with M4 core. We will leave the tasks running and open to be interfaced for expanding the capability of the Portenta X8 and Max Carrier.

To showcase the ability of the Arduino layer extended by M4 Core, we will explore two scenarios as example. One scenario is where the Arduino layer will be the terminal to expose the received sensor data to a local end-device to be controlled. While other scenario has a local end-device that transfers data to Linux layer for further networking process, hence the multi-protocol architecture will help to handle the data for transmitting in a desired protocol.  

## Linux Layer

It is important to understand that **all networking process is made within the Linux layer**. All the network processes that are WiFi, Bluetooth low energy, LoRa, NB-IoT, and Cat-M1. In this tutorial we will focus on using WiFi with MQTT protocol, Bluetooth low energy, and LoRa connectivities to establish a gateway based on multiple protocols. 

![Multi-Protocol Handling Procedure in Linux Layer](assets/.png)

The Portenta X8 provides WiFi connectivity and the Portenta Max Carrier provides LoRaWAN module that can help us communicate with The Things Network. We will use the MQTT protocol to receive the sensor data transmitted by an end device. 

Thus, we will use a python script that will configure and handle the connectivity modules and its sensor data. The RPC calls will make to expose the received sensor data to Arduino layer to set up data exchange configuration to further expand the capability of the Portenta X8 and Max Carrier. The process can also be done vice-versa if the Arduino layer is to transmit the data to Linux layer fed from the local end-device. 

## Hardware Setup 

First things first, we will need to configure the hardware to be able to develop and work on Multi-Protocol gateway. We will attach the Portenta X8 to Portenta Max Carrier via High-Density Connectors, and we will make sure to attach an antenna for LoRa connectvity. The Portenta X8 should also need to have the WiFi antenna attached to it. 

![Multi-Protocol Gateway Hardware Setup](assets/.png)

***If you have not set up the Portenta X8, please have a look at [Portenta X8 Getting Started](https://docs.arduino.cc/tutorials/portenta-x8/out-of-the-box) tutorial.***

## Pre-Requisites

Before we begin diving deep into creating Multi-protocol gateway, and having understood we will frequently communicate between Arduino and Linux layer, we will have to know how to debug and observe the way these 2 layers interact. 

The `m4-proxy` is a service that manages data exchange between these layers. You can use the following command in the terminal to observe if the service is running correctly.

```
sudo journalctl -fu m4-proxy
```
We are going to implement RPC (Remote Procedure Call) to establish communication between Arduino and Linux layer. This is a communication mechanism implemented to exchange data between these two layers. 

A very important note to take it into account: **you will not be able to check messages via `Serial.println()` statements** to check if the Arduino sketch is running in a desired manner. You will have to use **`py-serialrpc`**, which is a service that will assist you in listening to those messages to print them on a console. To have the service active, please download [this compressed file](assets/py-serialrpc.zip) to build and run the container at Linux side of Portenta X8. Please execute following commands in order to have the service running.

```
// Copy the decompressed files in ../adb/32.0.0 
adb push py-serialrpc /home/fio
adb shell

// The password is: fio
sudo su -

// Head to directory and mount the container
cd /home/fio/py-serialrpc
#py-serialrpc sudo docker build. -t py-serialrpc 
#py-serialrpc sudo docker-compose up -d
```

To access the logs of `py-serialrpc` service, while maintaining at same directory, execute the following command.

```
sudo docker-compose logs -f --tail 20
```

***For more detail about how data exchange between Arduino and Linux layer works and to understand how to debug, please read [Data Exchange Between Python on Linux and an Arduino Sketch](https://docs.arduino.cc/tutorials/portenta-x8/python-arduino-data-exchange)***

## Coding Multi-Protocol Gateway

As everything sounds beautiful, now it is important to land all the requirements into a operational task that will orchestrate every protocols we are going to use. We will create the following files and the required codes for multi-protocol gateway. 

We will need the Docker files that will configure and let us build a working container.

***If you are unfamiliar handling with Docker and containers, please read the tutorial on [Create and Upload a Custom Container to the Portenta X8](https://docs.arduino.cc/tutorials/portenta-x8/custom-container)***

You can access the files [here](assets/multi-protocol-gateway.zip) to have the files ready. Meanwhile, let me help you understand some of the important details of the included files. 

### Docker Compose

Beginning with the `docker-compose.yml` file. Which is where we define permissions and settings for the container involved. 

```
...
extra_hosts:
  - "m4-proxy:host-gateway"
devices:
  - /dev/ttymxc3
tty: true
user: "0"
```

### Requirements

Here we will define which additional components are required to be able to run the script built inside the container. 

```
msgpack-rpc-python
pyserial==3.4
certifi
paho-mqtt
...
```

### Multi-Protocol

This is the main Python script that will handle overall networking process.

```
#M4 Proxy Server Configuration
# Fixed configuration parameters
port = 8884
publish_interval = 5

# The M4 Proxy address needs to be mapped via Docker's extra hosts
m4_proxy_address = 'm4-proxy'
m4_proxy_port = 5001
```

```
def get_data_from_m4():

    rpc_address = RpcAddress(m4_proxy_address, m4_proxy_port)

    data = ()

    try:
        rpc_client = RpcClient(rpc_address)
        temperature = rpc_client.call('temperature')

        rpc_client = RpcClient(rpc_address)
        humidity = rpc_client.call('humidity')

        data = temperature, humidity

    except RpcError.TimeoutError:
        print("Unable to retrieve data from the M4.")

    return data
```

```
# Obtained during first registration of the device
SECRET_DEV_EUI = 'XXXXXXXXXXXXXXXX'
SECRET_APP_EUI = 'XXXXXXXXXXXXXXXX'
SECRET_APP_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
```

<WIP>

## Mounting the Multi-Protocol Gateway Container

It is now time make the multi-protocol gateway run, we will need to build the Docker container that will help us operate in the background on the Linux layer. Using the terminal, we will use the following commands to get the multi-protocol gatewya container up and running. 

```
adb push multi-protocol-gateway /home/fio
adb shell
```

```
cd ../home/fio/multi-protocol-gateway
#multi-protocol-gateway sudo docker build . -t multi-protocol-gateway
```

```
#multi-protocol-gateway sudo docker-compose up
```

```
#multi-protocol-gateway sudo docker-compose down
```

```
docker ps -a
```

<WIP>

## Conclusion

In this tutorial you learned how to set up a Multi-Protocol Gateway composed of WiFi connectivity and LoRaWAN, by using the Portenta X8 and the Portenta Max Carrier. 

### Next Steps
- Now that you have established a multi-protocol gateway, using WiFi and LoRaWAN connectivity, expand the gateway's capability by adding other connectivity types or ground a proper gateway with extended functionalities for data processing. 