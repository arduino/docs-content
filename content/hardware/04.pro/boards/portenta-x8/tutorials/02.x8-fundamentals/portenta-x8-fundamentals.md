---
title: '02. How to Use the Portenta X8 Manager'
difficulty: beginner
tags: [Linux, containers, factories, foundries]
description: 'This article contains information about how to use the Portenta X8 Manager.'
author: Benjamin Dannegård
hardware:
  - hardware/04.pro/board/portenta-x8
software:
  - fioctl

---

## Overview

The **Portenta** X8 is one of the most advanced boards available from Arduino. And with that comes some new concepts that are not standard for Arduino boards. In this article, we will go through some of the foundations of the Portenta X8 and help you understand how the board works and how you can benefit from its advanced features of this board. You will learn about FoundriesFactory® and how containers on the Portenta X8 work.

## Goals

- Get in-depth information about how the Portenta X8 works
- Learn how containers work

### Required Hardware and Software

- [Portenta X8](https://store.arduino.cc/portenta-x8)
- [fioctl](https://docs.foundries.io/latest/getting-started/install-fioctl/index.html)

## Instructions

If you need help setting up your board, please have a look at the [Portenta X8 User Manual](https://docs.arduino.cc/tutorials/portenta-x8/user-manual) where you will learn the basics and how to use your Portenta X8.

## Embedded Linux

There are a few things to consider to work in an embedded Linux environment. When approaching Linux-based embedded devices software solutions, you need to provide a base distribution, a mechanism to update it, and some applications that can run on the board. The X8 uses a Linux distribution built with the Yocto Project® as the base platform, with applications that are installed and packaged as confined containers.

A readily-available Linux distribution that packages everything seems most attractive for end users but you need to find a distribution that implements the function that you need. If you need to tweak them, you may end up in a mess of patches on the top of someone else's build system. On the other hand, a generic distribution has some problems since installing software over it may pollute the original system and cause issues when updating the base platform. For example, if you install a new application, the older one no longer works.

In addition, you have to implement lots of things like cybersecurity functions and system updates. Finally, your solution may rely on a too "generic" distribution, with tons of software you don't need. So you may end up removing a lot of software on the target and turning features on and off. Until you break the configuration or need to update the system and begin restarting with a new fresh image, consequently beginning everything from zero again.

### Benefits of Foundries.io

Foundries.io™ created their custom distribution based on Yocto with minimal software installed, by default implementing top-level cybersecurity features like OP-TEE and OSTREE that makes their solution ideal for professional applications.

A custom Over-The-Air (OTA) system update mechanism that is based on a client running on target and a robust Cloud server. And they married Docker-compose as a way to deploy a software solution to a target. This is like having an app store for a particular device with the difference that we're not installing an app but a container that may contain a whole distribution or a minimal distribution running only our app or our set of apps.

Additionally, they developed the Cloud side as well. You can use what's called FoundriesFactory, a Cloud DevSecOps subscription service to build, test, deploy, and maintain secure, updatable IoT and Edge products. It provides a unique id and automatic builds of the base system and containers for this system in one place. Let's now take a look at the Foundries.io Factory page.

### Foundries.io Factory

With the help of the Arduino Cloud integration with *Foundries.io*, you can easily create your Factory right from the Arduino Cloud page. You can set your Factory's platform and name. The Portenta X8 will be the platform in this case.

![Factory page](assets/factory-page.png)

Your Factory page allows you to add members so that you can easily keep track of the members of your team that should have access to the Portenta X8's that are linked to your Factory. You can also set up teams for better management. On the page, you can also find a list of all devices linked to the Factory, along with their name and version of the container currently uploaded to the board. On the containers page, you can find all the different versions of containers uploaded to the Factory.

On the "source" page of your Factory, you can find the four repositories that are used to customize the images. These are:

- **ci-scripts.git**: Scripts that define the platform and container build jobs to the FoundriesFactory continuous integration system.
- **lmp-manifest.git**: The repo manifest for the platform build. It defines which layer versions are included in the platform image. This includes **meta-partner-arduino**, the layer containing Arduino specific customizations (machine definition, device drivers, etc).
- **meta-subscriber-overrides.git**: OE layer that defines what is included in your Factory image. You can add board-specific customizations and overrides. Also, add and remove packages provided in the default Linux microPlatform base.
- **containers.git**: This is where containers and docker-compose apps are defined. It allows us to define what containers to build, and how to orchestrate them on the platform.

While the "targets" page contains the images built by the Continuous integration system each time something commits in the repositories. Committing to **lmp-manifest.git** or **meta-subscriber-overrides.git** repositories will create a platform target while committing to **containers.git** will create a container target. These targets will generate the artifacts for the platforms as specified in the **ci-scripts.git**, including all the required files to program the target in case of platform builds. You can inspect your FoundriesFactory targets on the "targets" page.

## Containers

Containers allow for easy deployment of Linux-based processes, uploaded through git, which can then be tracked on your Factory page. A Linux container is a process isolated from the rest of the system. A container is an image file conformed of the necessary files to run it. This makes the Linux containers portable and consistent throughout development, testing, and production. Making them much quicker to use than development pipelines that rely on replicating traditional testing environments.

*Foundries.io* provides a service that builds images using the Yocto Project and is specifically built around the Linux microPlatform (LmP) distribution they maintain. LmP contains an extensive set of software components needed for IoT applications.

Using [fioctl](https://docs.foundries.io/latest/getting-started/install-fioctl/index.html) allows you to manage your boards through CLI. It makes it easy to upload containers to a board linked to your Factory. When the board is online and connected to the Factory, you can easily push new apps to the board. Using the fioctl command lines, you only need to state the Factory, board, and app.

### Benefits of Containers

For example, if you are developing an application on a laptop and your environment has a specific configuration. Other developers may have slightly different configurations. The application will rely on your configuration and be dependent on specific files, libraries, and dependencies. On the other hand, your business has development and production environments with their configurations and supporting files. You would want to emulate that environment as much as possible locally.

With containers, you can make your app work across environments, pass quality assurance and deploy as fast as possible effortlessly.

The container image contents can be compared to an installation of a Linux distribution complete with RPM packages, configuration files, etc. However, a container image distribution is easier to install than setting a whole new copy of the operating system.

A Linux container is a good solution that requires portability, configurability, and isolation. The idea behind Linux containers is to help develop solutions faster to meet business needs as they arise. In certain scenarios, when real-time data streaming is implemented, containers are a dominant solution to provide the scalability that the application needs. Regardless of the infrastructure on-site, in the Cloud, or a mix of both.

## Conclusion

In this tutorial, we have expanded on how the Portenta X8 works with factories and containers. This article also gives a better picture of how to utilize the Portenta X8 to its full potential. Please check out our other tutorials with the Portenta X8 to see how factories and containers are applied in a real-world example.
