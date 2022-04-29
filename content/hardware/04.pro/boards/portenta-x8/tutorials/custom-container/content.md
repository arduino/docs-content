---
title: Create and Upload a Custom Container Portenta X8
difficulty: easy
tags: [Linux, containers]
description: This tutorial will show you how to create and upload your custom container to your Portenta X8
author: Benjamin Dannegård
hardware:
  - hardware/04.pro/board/portenta-x8
software:
  -

---

## Overview

In this tutorial we will create a simple container that we can then upload to the Portenta X8. A container consists of an image file and all it's dependencies if there are any. 

## Goals

- Learn how to create a container for use with the Portenta X8
- Learn how to upload a container to the Portenta X8

### Required Hardware and Software

-   [Portenta X8](https://store.arduino.cc/portenta-x8)

## Instructions

First we are going to write our Arduino Linux sketch. We will first create a file with the """" format. Open the file in the code editor of your choice, we can now start writng our Linux sketch. 


is a runnable instance of an image. You can create, start, stop, move, or delete a container using the DockerAPI or CLI.
can be run on local machines, virtual machines or deployed to the cloud.
is portable (can be run on any OS)
Containers are isolated from each other and run their own software, binaries, and configurations.

When running a container, it uses an isolated filesystem. This custom filesystem is provided by a container image. Since the image contains the container’s filesystem, it must contain everything needed to run an application - all dependencies, configuration, scripts, binaries, etc. The image also contains other configuration for the container, such as environment variables, a default command to run, and other metadata.

## 

### 

## Upload container

If you want to learn how to upload your newly created container to your Portenta X8, then please check out our [Uploading container tutorial](). It will show you how to add and remove containers from your Portenta X8 using SSH or ????.

### 

## Conclusion

Now you should have a better understanding of how the Portenta X8 works with factories and containers. This article also gives a better picture of how to utilize the Portenta X8 to its full potential. Be sure to check out our other tutorials with the Portenta X8 to see how to practically use factories and containers.
