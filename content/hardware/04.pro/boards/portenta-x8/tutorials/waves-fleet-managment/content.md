---
title: 'Using FoundriesFactory Waves Fleet Management'
description: 'Learn how to use Foundries.io Factory fleet management tool Waves to manage multiple Portenta X8 devices'
difficulty: intermediate
tags:
  - Embedded Linux
  - Flashing
  - Foundries.io
author: 'Benjamin Dannegård'
hardware:
  - hardware/04.pro/boards/portenta-x8
---

## Overview

In a production environment it is convenient to plan updates, and have control over when and which devices are updated. FoundriesFactory Waves is the feature for this. It allows you to easily define a group of Portenta X8s and then push updates to that specific group. This tutorial will show you how to define that group and how to construct a Wave that can then be pushed to a group.

## Goals

- Learn how to use Waves fleet manager
- Learn how to assign a target to a Wave
- Learn how to push a Wave to a group of devices

### Required Hardware and Software

- USB-C to USB-A or USB-C to USB-C
- Portenta X8
- Arduino Create account
- Arduino Pro Cloud Subscription. [Learn more about the Pro Cloud](https://www.arduino.cc/pro/hardware/product/portenta-x8#pro-cloud).
- Foundries.io account (linked with the Pro Cloud subscription)
- FoundriesFactory® ([Check the Getting Started tutorial](https://docs.arduino.cc/tutorials/portenta-x8/out-of-the-box))
- Devices already attached to your factory ([Check the Getting Started tutorial](https://docs.arduino.cc/tutorials/portenta-x8/out-of-the-box))
    
## Instructions

### Setting Up the Terminal

Waves fleet management requires us to have the X8 setup with a FoundriesFactory. If you have not done this please take a look our other tutorial [Getting Started tutorial](https://docs.arduino.cc/tutorials/portenta-x8/out-of-the-box), it will walk you through how to set up the X8 with your FoundriesFactory. To use Waves we also need to have fioctl installed and configured, you can follow this guide [here](https://docs.foundries.io/latest/getting-started/install-fioctl/index.html) for setting up fioctl. Creating waves and device groups will be done via the host, which is your factory, so the following commands will be in a terminal using fioctl connected to your FoundriesFactory.

### Rotating Our Keys

For security purposes we recommend that you rotate the keys of your FoundriesFactory. Rotation of the key will convert the root role's online-key, generated during the bootstrap of a Factory, to an offline key.

First we will rotate the root keys. These are the most important keys, they can be used to create new target keys. We will rotate them with this command:
```
fioctl keys rotate-root --initial /absolute/path/to/root.keys.tgz
```

Now we can rotate the target only keys. With this command:
```
fioctl keys rotate-targets /absolute/path/to/root.keys.tgz
```

And finally we copy the target keys to root using:
```
fioctl keys copy-targets /absolute/path/to/root.keys.tgz /path/to/target.only.key.tgz
```

Now we can move on to creating our Wave.

### Creating the Wave

The command below will create a wave that can then be pushed to our devices. To create a Wave we will have to sign it with a key, here we will use the targets only key. Then we can give the wave a name, target number and tag. The `target number` needs to correspond to the target that we want the wave to contain for our devices. The `tag` can be set as production or development. 
```
fioctl wave init -k /absolute/path/to/targets.only.key.tgz <wave-name> <target number> <tag>
```

And then we can complete the wave by calling this function with the waves name.
```
fioctl wave complete <wave-name>
```

Or we can cancel it if we wish with:
```
fioctl waves cancel <wave name>
```

When you create the wave you should be able to see it on your factory page. Here it should also be marked as complete once you call the wave complete command.

![The wave page on your FoundriesFactory](assets/foundriesfactory-waves-page.png)

### Create the Device Group

With this command we create our group. We give it a name and we can also give it a short description. 
```
fioctl config device-group create <group name> <"short description here">
```

Now to assign a device to our group we use:
```
fioctl device config group <device name> <group name>
```

On your FoundriesFactory page you can sort devices by group on the device page.

![Device group sorting on the FoundriesFactory page](assets/foundriesfactory-device-group.png)

And now to rollout our wave to our device group we use:
```
fioctl waves rollout <wave name> <device group name>
```

Now every device in the device group should have the target specified in the wave creation.

### Conclusion

In this tutorial we first looked at what is required to use the Wave tool. We then went through the process of creating a wave and device group. Then we pushed a target to the device group using the Wave tool. 

## Troubleshooting

- If you are having trouble with any fioctl commands you can use `fioctl wave --help` or `fioctl wave rollout --help` depending on the context.