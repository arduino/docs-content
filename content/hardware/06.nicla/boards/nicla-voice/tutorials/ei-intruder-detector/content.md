---
title: 'Door Intruder Detector using ML with the Nicla Voice'
description: "This application note describes how to identify normal door opening vs a forced attempt, looking for intruders by analyzing surroundings sounds using Machine Learning with Edge Impulse and the Nicla Voice to then be monitored with a Dashboard on the Arduino IoT Cloud."
difficulty: intermediate
tags:
  - Intruder detector
  - Nicla
  - Machine Learning
  - Edge Impulse
  - Sound recognition
  - Arduino IoT Cloud
  - Application Note
author: 'Christopher Mendez | MCMCHRIS'
libraries:
  - name: ArduinoBLE
    url: https://reference.arduino.cc/reference/en/libraries/arduinoble/
  - name: ArduinoIoTCloud
    url: https://github.com/arduino-libraries/ArduinoIoTCloud
  - name: Arduino_ConnectionsHandler
    url: https://github.com/arduino-libraries/Arduino_ConnectionHandler
  - name: NDP
    url: https://github.com/arduino-libraries/Arduino_ConnectionHandler
software:
  - ide-v1
  - ide-v2
  - arduino-cli
  - web-editor
  - iot-cloud
hardware:
  - hardware/06.nicla/boards/nicla-voice
---

## Introduction

Security has always been a very important factor for our well-being, from the personal to the material, keeping our assets safe is something we struggle with every day, in our cars, lockers, computers, our houses, we insure everything is locked up, but there are times when that is not enough. In such a connected world, where we have a lot of information in the palm of our hand, it would also be very useful to have the status of those things that we have insured in a more analogous way, such as the front door of our home. Using its integrated microphone the Nicla Voice is an ideal option to achieve this.

## Goals

The goal of this application note is to showcase an intruder detection and monitoring system for a house front door using the Nicla Voice + a Portenta H7 host and the Arduino IoT Cloud.

This project's characteristics are the following:

Analyzing the surrounding sounds with its integrated microphone and running artificial intelligence algorithms at the edge, the Nicla Voice is an ideal option to keep us aware if our door is opened or tried to be forced, reporting everything through BLE to a Host will allow us to monitor everything from the cloud.


## Hardware and Software Requirements

### Hardware Requirements

### Software Requirements

## The Machine Learning Model

## Intruder Detector System Setup

## Intruder Detector System Overview

### Nicla Voice Code

### Portenta H7 Code

### The Cloud Dashboard

## Full Intruder Detector Example

## Conclusion