---
title: Portenta X8 Fundamentals
difficulty: easy
tags: [Linux, containers, factories, foundries]
description: This article contains information about the fundamental concepts of the Portenta X8
author: Benjamin Dannegård
hardware:
  - hardware/04.pro/board/portenta-x8
software:
  - fioctl

---

## Overview

The Portenta X8 is one of the more advanced boards available from Arduino. And with that comes some new concepts that are not standard for Arduino boards. In this article we will go through some of the foundations of the Portenta X8 and help you understand how the board works and how you can benefit from the advanced features of this board. You will learn about FoundriesFactory® and how containers on the Portenta X8 work.

## Goals

- Get in-depth information about how the Portenta X8 works
- Learn how containers work

### Required Hardware and Software

-   [Portenta X8](https://store.arduino.cc/portenta-x8)
-   [fioctl](https://docs.foundries.io/latest/getting-started/install-fioctl/index.html)

## Instructions

If you need help with setting up your board then please have a look at the "Getting Started" tutorial. That tutorial will show you how to set up your board with FoundriesFactory and install containers on it.

## Embedded Linux

To work in an embedded Linux environment there a few things to consider. When approaching linux-based embedded devices software solutions, you need to provide a base distribution, a mechanism to update it and some applications that can run on the board. The X8 uses a Linux distribution built with the Yocto Project® as the base platform, with applications that are installed and packaged as confined containers.

A ready-made Linux distribution that packages everything seems most attractive for end users but you need to find a distribution that implements the function that you need. If you need to tweak them you may end up in a mess of patches on the top of someone else's build system. On the other hand, a generic distribution has some problems since installing software over it may pollute the original system and cause issues when updating the base platform. For example you install a new application and the older one no longer works. In addition to that you have to implement a lot of things like cybersecurity functions and system updates. Finally, your solution may rely on a too "generic" distribution, with tons of software you don't need. So you may end up removing a lot of software on the target and also turning features on and off. Until you mess up things or you need to update the system and you restart with a new fresh image and restart everything from the beginning.

### Benefits of Foundries.io

Foundries.io™ basically created their generic-but-not-too-generic distribution based on Yocto with minimal software installed, by default implementing top level cybersecurity features like OP-TEE and OSTREE that makes their solution ideal for professional applications. A custom OTA system update mechanism which is based on a client running on target and a robust cloud server. And they married Docker-compose as a way to deploy a software solution to a target. This is like having an app store for a particular device with the difference that we're not installing an app but a container which may contain a whole distribution or a minimal distribution running only our app or our set of apps.

In addition to that they developed the cloud side as well. In a nutshell you can use what's called FoundriesFactory, a cloud DevSecOps subscription service to build, test, deploy, and maintain secure, updatable IoT and Edge products. It provides a unique id and automatic builds of the base system and containers for this system in one place. Let's now take a look at the Foundries.io Factory page.

### Foundries.io Factory

With the help of the Arduino Cloud integration with Foundries.io, you can easily create your Factory right from the Arduino Cloud page. You can set your Factory's platform and name. The platform here will be the Portenta X8.

![Factory page](assets/factory-page.png)

Your Factory page allows you to add members, so that you can easily keep track of the members of your team that should have access to the Portenta X8's that are linked to your Factory. You can also set up teams for better management. On the page you can also find a list of all devices linked to the Factory, along with their name and version of container that is currently uploaded to the board. On the containers page you can find all the different versions of containers uploaded to the Factory.

On the "source" page of your Factory, you can find the four repositories that are used to customize the images. These are:

- **ci-scripts.git**: CI scripts to build images for all the machines that need to be built.
- **lmp-manifest.git**: Index of the repositories to be downloaded by repository to create the source work tree.
- **meta-subscriber-overrides.git**: Yocto layer containing Arduino specific customizations (machine definition, device drivers, etc). 
- **containers.git**: Container recipes

While the "targets" page contains the images built by the Continuous integration system each time something is committed in the repositories. Committing to a repository will trigger building a target which can then be inspected in the "targets" page. Each target will compile for multiple platforms (as specified in the ci-scripts.git) and will generate all the required files to program the target.

## Containers

Containers allow for easy deployment of Linux based processes, uploaded through git, which can then be tracked on your Factory page. A Linux container are processes that are isolated from the rest of the system. A container is an image file that contains all the files that are necessary to run it. This makes the Linux containers portable and consistent throughout development, testing and production. Making them much quicker to use than development pipelines that rely on replicating traditional testing environments.

Foundries.io provides a service that builds images using the Yocto Project and specifically built around the Linux microPlatform (LmP) distribution they maintain. LmP contains an extensive set of software components needed for IoT applications. 

Using [fioctl](https://docs.foundries.io/82/getting-started/install-fioctl/index.html) allows you to manage your boards through CLI. This will make it possible for you to easily upload containers to a board that is linked to your Factory. When the board is online and connected to the Factory you can easily push new apps to the board. Using fioctl command lines you only need to state the Factory, board and app.

### Benefits of Containers

For example if you are developing an application on a laptop and your environment has a specific configuration. Other developers may have slightly different configurations. The application will rely on your configuration and is dependent on specific files, libraries and dependencies. While your business has development and production environments with their own configurations and supporting files. You would want to emulate that environment as much as possible locally.

With containers you can make your app work across environments, pass quality assurance and get it deployed as fast and easy as possible.

The contents of a container image can be compared to a an installation of a Linux distribution complete with RPM packages, configuration files, etc. However, a container image distribution is easier to install rather than a new copy of the operating system.

A Linux container is a good solution for solutions that require portability, configurability and isolation. The idea behind Linux containers is to be able to develop solutions faster to meet business needs as they arise. In certain scenarios, like when real-time data streaming is implemented, containers are the only way to provide the scalability that the application needs. Regardless of the infrastructure on site, in the cloud, or a mix of both.

## Conclusion

Now you should have a better understanding of how the Portenta X8 works with factories and containers. This article also gives a better picture of how to utilize the Portenta X8 to its full potential. Be sure to check out our other tutorials with the Portenta X8 to see how to practically use factories and containers.
