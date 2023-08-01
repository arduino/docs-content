---
title: 'Motion Detection with the Nicla Voice and Edge Impulse®'
description: "Learn how to create a simple motion detection application with the Arduino® Nicla Voice and the Edge Impulse® platform."
difficulty: intermediate 
tags:
  - Nicla
  - Machine Learning
  - IMU
author: 'José Bagur, Christopher Mendez, and Benjamin Dannegård'
software:
  - ide-v2
  - web-editor
  - iot-cloud
hardware:
  - hardware/06.nicla/boards/nicla-voice
---

## Overview

The Nicla Voice is a versatile board that can be used for various projects and applications. With its onboard Inertial Measurement Unit (IMU) and Tiny Machine Learning (TinyML), the Nicla Voice board provides an ideal device for the application described in this tutorial: **a simple motion detection application**.

The simple motion detection application will be based on a Tiny Machine Learning (TinyML) model developed with Edge Impulse®, a leading platform in developing intelligent devices and a powerful facilitator for TinyML applications. With Edge Impulse®, we will capture data from your Nicla's Voice onboard IMU, create and train a TinyML model specifically designed for motion detection, and deploy it into the board for testing and validation. By the end of this tutorial, you will have a fully functional motion detection application running on your Nicla Voice board and a solid foundation in applying TinyML to real-world applications.

## Goals

- Understand the key features and capabilities of the Nicla Voice board.
- Set up a Nicla Voice board and prepare it for developing of a motion detection application.
- Become familiar with the Edge Impulse® platform, its interface, and its key features.
- Collect motion data from the Nicla Voice board's onboard IMU using Edge Impulse®.
- Develop, train, and validate a TinyML model designed for motion detection using Edge Impulse®.
- Deploy the trained TinyML model onto the Nicla Voice board and test its real-time motion detection capabilities.
- Gain practical experience and foundational knowledge in developing TinyML applications for real-world scenarios.

## Hardware and Software Requirements

### Hardware Requirements

- Nicla Voice (x1)
- Micro USB cable (x1)

### Software Requirements

- Arduino IDE 2.0+, or Arduino Web Editor
- To create custom Machine Learning models, the integrated [Machine Learning Tools](https://cloud.arduino.cc/machine-learning-tools/) of the [Arduino Cloud](https://cloud.arduino.cc/) are needed. In case you do not have an Arduino Cloud account, you will need to create one first.

## Motion Detection and TinyML