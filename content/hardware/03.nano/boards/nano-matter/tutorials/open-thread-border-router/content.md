---
title: 'Open Thread Border Router with the Nano ESP32 and the Nano Matter'
difficulty: advanced
compatible-products: [nano-matter]
description: 'Learn how to create your own Thread Border Router using OpenThread and Arduino products.'
tags:
  - OTBR
  - Thread
  - Matter
  - Linux
author: 'Martino Facchin, Leonardo Cavagnis and Christopher Méndez'
hardware:
  - hardware/03.nano/boards/nano-matter
  - hardware/03.nano/boards/nano-esp32
---

## Introduction

Thread is a low-power, wireless mesh networking protocol designed for smart homes and IoT devices. A Thread Border Router serves as a bridge between the Thread network and the wider internet or local networks, allowing devices within the Thread network to communicate with external systems.

![Thumbnail Image]()

Matter devices can use Thread as their primary communication method, especially for low-power devices such as sensors, light bulbs, and door locks. These devices communicate using the Thread protocol and leverage Matter's application layer for interoperability.

### What is an OTBR?

An OpenThread Border Router (OTBR) consists of a **Matter Controller** and a **Radio Co-Processor** (RCP):

- The *Matter Controller* is essential for managing devices using the Matter protocol, which ensures interoperability between nodes. It handles: commissioning, communication and network management.
- The *Radio Co-Processor* (RCP) is dedicated to handling Thread network communications, improving efficiency by offloading radio communication tasks.

The **Arduino Nano Matter** serves as the **RCP**, connected to the **Arduino Nano ESP32** (the Matter Controller) via serial port.

## Goals

This tutorial main objective is to guide you through the build and configuration of an OpenThread Border Router that will allow you to deploy a Matter network over Thread to integrate Matter devices to your Smart Home system. 

- Create an OTBR using Arduino products.
- Leverage the Arduino Nano Matter as a Radio Co-Processor.
- Use the Arduino Nano ESP32 as a Matter Controller.
- Integrate a smart outlet based on the Nano Matter to your network.

## Hardware and Software Requirements

### Hardware Requirements

- [Nano Matter](https://store.arduino.cc/products/nano-matter) (x2)
- [Nano ESP32](https://store.arduino.cc/products/nano-esp32) (x1)
- Linux Computer (Laptop/PC) (x1)
- USB-C® cable (x1)

### Software Requirements

- [Arduino IDE 2.0+](https://www.arduino.cc/en/software)
- [Simplicity Studio](https://www.silabs.com/developers/simplicity-studio)
- [Visual Studio Code](https://code.visualstudio.com/)

## Setting up the OTBR

### The RCP: Arduino Nano Matter

This section outlines the steps to build the RCP firmware for the Arduino Nano Matter.

- Download Simplicity Studio: this is an IDE provided by Silicon Labs. It is designed to simplify the development process for Silicon Labs hardware platforms. Download latest version [here](https://www.silabs.com/developers/simplicity-studio).
- Open Simplicity Studio and create a new project by clicking on **File > New > Silicon Labs Project Wizard**.
  
![New project creation](assets/new-project.png)

- Set the following project configurations:
- 
|   **Field**   | **Setting** |
| :-----------: | :---------: |
| Target Boards |  BRD4318A   |

### The Matter Controller: Arduino Nano ESP32

### The CHIP Tool: Linux Computer

## Testing the OTBR

## Setup

## The Use Case: Smart Outlet