---
title: 'Using Foundries.io Factory Waves fleet managment'
description: 'Learn how to use Foundries.io Factory fleet managment tool Waves to manage multiple Portenta X8 devices'
difficulty: easy
tags:
  - Embedded Linux
  - Flashing
  - Foundries.io
author: 'Benjamin Dannegård'
hardware:
  - hardware/04.pro/boards/portenta-x8
---

## Overview

Using Foundries factory with our Arduino Portenta X8 it is possible to use a fleet managing tool called "Waves". This is useful if you have multiple Portenta X8 devices that you need to push software to. (05:00)

## Goals

- Learn how to use Waves fleet manager

### Required Hardware and Software

- USB-C to USB-A or USB-C to USB-C
- Portenta X8
- Arduino Create account
- Arduino Pro Cloud Subscription. [Learn more about the Pro Cloud](https://www.arduino.cc/pro/hardware/product/portenta-x8#pro-cloud).
- Foundries.io account (linked with the Pro Cloud subscription)
- FoundriesFactory® ([Check the Getting Started tutorial](https://docs.arduino.cc/tutorials/portenta-x8/out-of-the-box))
- Devices already attached to your factory ([Check the Getting Started tutorial](https://docs.arduino.cc/tutorials/portenta-x8/out-of-the-box))
    
## Instructions

### Setting up the terminal

To use Waves fleet managment we need to have the X8 setup with FoundriesFactory and be able to access it through the adb terminal with fioctl. If you have not done this please take a look at some of our other tutorials [][].


### Commands

Rotate offline keys
```
fioctl keys rotate-root --initial /absolute/path/to/root.keys.tgz
```

Rotate target keys
```
fioctl keys rotate-targets /aboslute/path/to/root.keys.tgz
```

Copy target keys to root
```
fioctl keys copy-targets /absolute/path/to/root.keys.tgz /path/to/target.only.key.tgz
```

Initialize the Wave
```
fioctl wave init -k /absolute/path/to/targets.only.key.tgz <wave-name> <target number> <tag>
```

Finalize the Wave
```
fioctl wave complete <wave-name>
```

Configure device group
```
fioctl config device-group create canary "early adopters"
```

Configure device?
```
fioctl device config group deviceA canary
```

Initialize the Wave with wave name, target number and tag
```
fioctl wave init -k /absolute/path/to/targets.only.key.tgz v2.0-update 42 production
```

Rollout wave
```
fioctl waves rollout v2.0-update canary
```

Complete wave rollout or cancel it
```
fioctl waves complete v2.0-update
```
**or**
```
fioctl waves cancel v2.0-update
```


### Setting up Device Groups for Waves

Waves will let you push a target to a group of X8 devices, a group that you can define to suit your needs. 

### Pushing software to a Device Group

We will push our software with the help of "tags". This is where we will assign a certain target a tag so we can easily tell what target it is we want to use when pushing to our group. 


### Conclusion

In this tutorial we showed you how to create a group for your devices. Now you know how to manage a fleet of Portenta X8s using Foundies.io's Waves tool. 

## Troubleshooting
