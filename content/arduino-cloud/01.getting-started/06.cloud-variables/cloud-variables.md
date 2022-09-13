---
title: 'IoT Cloud Dashboards & Widgets'
description: 'Learn about dashboards and the different widgets that can be used to monitor & control your board.'
tags: [IoT Cloud, Widgets, Dashboards]
author: 'Karl Söderby'
difficulty: beginner
---

## Overview

An essential component of the [Arduino Cloud](https://create.arduino.cc/iot/) is a **cloud variable**. A cloud variable is the same as a regular variable that you use in an Arduino sketch, but with some additional functionality.

A cloud variable is synced between your Arduino board and the Arduino Cloud. So if a variable is updated on your board (like a sensor reading), the Arduino Cloud will also receive this value. Similarly, if you update a variable from the cloud, it also updates on your board. 

This means that at any given time, you are able to read and send data to and from your board, as long as your board is connected to the Arduino IoT Cloud.

In this article, we will explore how to use variables in the Arduino IoT Cloud, 

`ArduinoCloud.update()`

