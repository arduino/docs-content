---
title: Portenta X8 Foundations
difficulty: easy
tags: [Linux, containers, factories, foundries]
description: This article conatins information about the fundemental concepts of the Portenta X8
author: Benjamin Dannegård
libraries:
hardware:
  - hardware/04.pro/board/portenta-x8
software:

---

## Overview

The Portenta X8 is one of the more advanced boards available from Arduino. And with that comes some new concepts that are not standard for Arduino boards. In this article we will go through some of the foundations of the Portenta X8 and help you understand how the board works and how the new features of the board can be useful. Such as how factories and containers on the Portenta X8 works.

## Goals

- Learn more in depth information about how the Portenta X8 works
- Learn how containers work

### Required Hardware and Software

-   Portenta X8
-   fioctl

## Instructions

If you need help with setting up your board then please have a look at the [Getting started tutorial](). The getting started tutorial will show you how to set up your board with a factory and upload containers to it.

### Factories

With the help of the Arduino Cloud integration with foundries you can easily create your own factory right from the Arduino Cloud page. You can set your factory's platform and name. The platform here will be the Portenta X8.

Your factory page allows you to add members, so that you can easily keep track of the members of your team that should have access to the Portenta X8's that are linked to your factory. You can also set up teams for better management. On the page you can also find a list of all devices linked to the factory, along with their name and version of container that is currently uploaded to the board. On the containers page you can find all the different versions of containers uploaded to the factory.

![Factory page](assets/factory-page.png)

With the factory created and the board linked to it, you can start and develop Linux based containers that can then easily be uploaded to your factories Portenta X8.

## Containers

Containers allow for easy deployment of Linux based processes, uploaded through git, which can then be tracked on your factory page. A Linux container are processes that are isolated from the rest of the system. A container is an image file that contains all the files that are necessary to run it. This makes the Linux containers portable and consistent throughout development, testing and production. Making them much quicker to use than development pipelines that rely on replicating traditional testing environments.

Using [fioctl](https://docs.foundries.io/82/getting-started/install-fioctl/index.html) allows you to manage your boards through CLI. This will make it possible for you to easily upload containers to a board that is linked to your factory. When the board is online and connected to the factory you can easily push new apps to the board. Using fioctl command lines you only need to state the factory, board and app.

### Benefits of container

For example if you are developing an application on a laptop and your environment has a specific configuration. Other developers may have slightly different configurations. The application will rely on your configuration and is dependent on specific files, libraries and dependencies. While your business has development and production environments with their own configurations and supporting files. You would want to emulate that environment as much as possible locally.

With containers you can make your app work across environments, pass quality assurance and get it deployed as fast and easy as possible.

The contents of a container image can be compared to a an installation of a Linux distribution complete with RPM packages, configuration files, etc. However, a container image distribution is easier to install rather than a new copy of the operating system.

A Linux container is a good solution for solutions that require portability, configurability and isolation. The idea behind Linux containers is to be able to develop solutions faster to meet business needs as they arise. In certain scenarios, like when real-time data streaming is implemented, containers are the only way to provide the scalability that the application needs. Regardless of the infrastructure on site, in the cloud, or a mix of both.

## Conclusion

Now you should have a better understanding of how the Portenta X8 works with factories and containers. This article also gives a better picture of how to utilize the Portenta X8 to its full potential. Be sure to check out our other tutorials with the Portenta X8 to see how to practically use factories and containers.