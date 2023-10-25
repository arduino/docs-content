---
title: Things
description: Learn how to configure a Thing, a virtual twin of your hardware device.
tags: [Arduino Cloud, Things]
author: Karl Söderby
---

The communication between IoT devices and the Arduino Cloud is handled through something called **Things**. Things are a virtual twin of your hardware/setup, where you perform a lot of the configurations for your projects. 

In the Thing interface you can:
- Create cloud variables that can be synced across devices,
- select the main device you want to associate with,
- enter network credentials (such as Wi-Fi network/password),
- edit & upload sketches to your board,
- set webhooks that trigger whenever data changes.
- edit the timezone.

## Thing Interface

The Thing interface is designed for ease-of-use, and only has a few sections, which we will now go through.

![Thing Interface]()

### Device

In the device section you can select either a previously configured device, or configure a new one. Associating a device means your device and Thing are now linked indefinitely, until you decide to detach them.

The status of your device is also displayed in this section (online/offline).

***For more details on how to configure a device, check out the [Devices]() section. The available types and links to individual guides are found there.***

### Variables

The variables section is where you create **"Cloud Variables"**, a variable that exist in the Arduino Cloud as well as on your board/setup, and are synchronised continuously. You can configure a variable to be:
- **Read/Write** - you can interact with the variable from a dashboard,
- **Read Only** - you can only read data from the board.

When you create a variable, it is automatically\* added to your `thingProperties.h` file, which is included in your Arduino Cloud sketch. This means that you do not need to declare them again. Read more in the [Automatic Sketch Generation]() section further down.

For example, if you want to send temperature values to the cloud from a sensor, all you need to do is:

```arduino
temperature = sensor.readTemperature();
```

***\*This does not apply to Things that are associated with a manual device (JavaScript, Python) as they have no sketch associated. Read more at [Manual Devices]().***

There are a large number of variables available, including basic types such as `int`, `boolean` & `String`, but also complex types that hold multiple values, such as the `ColoredLight` variable. 

Variables of the same type can also be synchronised across all devices. This is done when creating a new variable, where you check the variables you want to sync with. 

***All variables are listed out in the [Variables]() section. See [Variable Synchronization]() for linking together your devices' variables.***

### Network

In the network section, you configure the credentials for your network, such as your Wi-Fi® network, secret key (for ESP32 boards) and other credentials for e.g. LoRaWAN® & cellular. The network details are securely stored.

![Network configuration.]()

The credentials entered are automatically included in your sketch (see automatic sketch generation just below). 

## Automatic Sketch Generation

Things based on Arduino / C++ (the default way) benefits from **automatic sketch generation**. Whenever any configuration is done in your Thing, the changes are reflected in your sketch files.

For example:
- Associating a Wi-Fi board will automatically update the connection method,
- creating a variable will add it to your `thingProperties.h` file,
- creating a variable with **read/write** permission will also add a callback function at the bottom of your sketch. This will trigger anytime the value changes.
- changing your network credentials will update the `arduino_secrets.h` file.

This is implemented so that the connection and synchronisation between the board and cloud is handled automatically, meaning you do not need to do any networking code when using the Arduino / C++ language.

***Please note that if you are using an offline environment, [Arduino IDE](), changes will only be made in the cloud environment and will manually need to be adjusted. If you plan on using the offline IDE, you make use of the [sketch synchronisation]() feature that allows you to push/pull your cloud sketches from the offline IDE.***

## Metadata

In the metadata tab you will find your **Thing ID**, **Timezone** configuration, timestamp data (creation/last modified). Here you can also create tags 

### Thing ID

Your Thing ID can be obtained from your metadata tab, and looks like this:

```
cd628fe4-31d1-42a8-bf33-a627997ce602
```

This ID is used when connecting with the [REST API]() or with the [Arduino CLI](). Using either of these clients provides information about your Thing, such as device associated and cloud variables.

### Timezone

You can choose your timezone through a dropdown menu in the metadata tab, which includes many cities from the Americas, Europe, Asia, Africa, Oceania, Atlantic, Pacific and even Antarctica.

This is particularly important when using the [scheduler]() feature to trigger events at specific times.

### Tags

Tags are used to organize and filter your Things. In a setup with many devices across different locations, this can be particularly useful. When creating a tag, you have two fields:
- **Key** - 