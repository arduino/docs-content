---
title: Portenta X8 Foundations
difficulty: easy
tags: [Linux, containers, factories]
description: This article conatins information about the fundemental concepts of the Portenta X8
author: Benjamin Dannegård
libraries:
hardware:
  - hardware/04.pro/board/portenta-x8
software:
  - ide-v1
  - ide-v2
  - web-editor
  - iot-cloud
---

## Overview

The Portenta X8 is one of the more advanced boards available from Arduino. And with that comes some new concepts that are not standard for Arduino boards. In this article we will go through some of the foundations of the Portenta X8 and help you understand how the board works and how the new features of the board can be usefull. Such as how factories and containers on the Portenta X8 works.

## Goals

- Learn more in depth information about how the Portenta X8 works
- Learn how containers work
- Learn why we decide to implement containers on the Portenta X8

### Required Hardware and Software

-   Portenta X8
-   Factories

## Instructions

If you need help with setting up your board then please have a look at the [Getting started tutorial](). The getting started tutorial will show you how to set up your board with a factory and upload containers to it.

## Factories

In your factory page you can with ease keep track of the devices, members, teams and containers associated with your factory. 

With the help of the Arduino Cloud integration with foundries you can easily create your own factory right from the Arduino Cloud page. You can set your factory's platform and name. The platform here will be the Portenta X8.

With the factory created and the board linked to it, you can start and develop Linux based containers that can then easily be uploaded to your factories Portenta X8.

## Conatiners

Containers allow for easy deployment of Linux based processes, uploaded through git to your factory page. A Linux container are processes that are isolated from the rest of the system. Creating an image that contains all the files that are necessary to run it. This makes the Linux containers portable and consistent throughout development, testing and production. Making them much quicker to use than development pipelines that rely on replicating traditional testing environments.

### Benefits of container

For example if you are developing an application on a laptop and your environment has a specific configuration. Then other developers may have slightly different configurations. The application will rely on your configuartion and is dependent on specific files, libraries and dependencies. While your business has development and production enviroments with their own configurations and supporting files. You would want to emulate that environment as much as possible locally.

With containers you can make your app work across environments, pass quality assurance and get it deployd as fast and easy as possible.

The contents of a container image can be compared to a an installation of a Linux distribution complete with RPM packages, configuration files, etc. However, a container image distribution is easier to install rather than a new copy of the operating system.

A linux container is a good solution for solutions that require portability, configurability and isolation. The idea behind Linux containers is to be able to develop solutions faster to meet business needs as they arise. In certain scenaris, like when real-time data streaming with Apache Kafka is implemented, containers are the only way to provide the scalability that the application needs. Regardles of the infrastructure on site, in the cloud, or a mix of both, containers are a great solution. 

## Conclusion

Now you should have a better understanding of how the Portenta X8 works. And have a better picture of how to utalize its full potential. Be sure to check out our other tutorials with the Portenta X8 to see how to use factories and containers.