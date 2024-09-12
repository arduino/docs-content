---
beta: true
title: '01. Portenta X8 User Manual'
description: 'Get a general overview of Portenta X8 and its features.'
difficulty: intermediate
tags:
  - Embedded Linux
  - Containers
  - Firmware
  - Pins
  - Connections
author: 'Marta Barbero'
hardware:
  - hardware/04.pro/boards/portenta-x8
software:
  - ide-v1
  - ide-v2
  - iot-cloud
---

## Introduction

Portenta X8 is a powerful, industrial-grade System on a Module with Linux OS preloaded onboard that can run device-independent software thanks to its modular container architecture.

In this user manual, we will go through the foundations of the Portenta X8 to help you understand how the board works and how you can benefit from its advanced features.

## Required Hardware

* [Portenta X8](https://store.arduino.cc/products/portenta-x8) (x1)
* USB-C® cable (either USB-C® to USB-A or USB-C® to USB-C®) (x1)
* Wi-Fi® Access Point or Ethernet with Internet access (x1)

## Required Software

* For Linux programming, leverage the latest Linux image available, and check [this section](#portenta-x8-os-image-update) to verify if your Portenta X8 has already been updated.
* For Arduino programming, leverage [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2](https://www.arduino.cc/en/software), or [Arduino Web Editor](https://create.arduino.cc/editor), and the latest "Arduino Mbed OS Portenta Boards" Core > 3.0.1.

## Product Overview

The Portenta X8 combines the best of two approaches, offering the flexibility of Linux and the capability for real-time applications within the Arduino environment. Developers can execute real-time tasks while simultaneously handling high-performance processing on Linux cores.

So, let's have a look at its technical specifications.

### Board Architecture Overview

Portenta X8 is a powerful, industrial-grade System on a Module that combines a Yocto Linux distribution with the well-known Arduino environment.

![Portenta X8 Tech Specs](assets/portenta_x8_call_outs.png "Portenta X8 Tech Specs")

As reported in the image above, Portenta X8 features two powerful computing units:

* **NXP® i.MX 8M Mini** Cortex®-A53 quad-core up to 1.8GHz per core + 1x Cortex®-M4 up to 400 MHz. This microprocessor is the one where the Yocto Linux distribution is running together with Docker containers (check [this section](#linux-environment) of this user manual to learn more).

* **STMicroelectronics STM32H747XI** featuring 1x Arm® Cortex®-M7 core running up to 480 MHz and 1x Arm® Cortex®-M4 core running up to 240 MHz. This microcontroller hosts the ["Arduino Mbed OS Portenta Boards" Core](https://github.com/arduino/ArduinoCore-mbed). M4 core is accessible and programmable by the user, while M7 is dedicated to establishing and guaranteeing the communication between i.MX 8M Mini and M4, as well as to manage peripherals through RPC. For more details, refer to [this section](#arduino-environment) of the user manual.

The two computing units are responsible for different tasks, which are summarized in the table below.

| **NXP® i.MX 8M Mini**                                   | **STMicroelectronics STM32H747XI (M4)**                        |
|---------------------------------------------------------|----------------------------------------------------------------|
| Running Yocto Linux distribution with Docker containers | Running Arduino sketches with the Mbed OS Portenta Boards Core |
| Dedicated to high level tasks                           | Dedicated to real-time tasks                                   |
| Manage network connectivity                             | No direct connection to any network stack                      |
| Manage network-based buses (e.g., Modbus TCP, etc.)     | Manage field buses (e.g., Modbus RTU, CANbus, etc.)            |
| Access to peripherals without concurrent access control | Access to peripherals without concurrent access control        |

In addition to the above features, here is an overview of the board's main components:

* **External memory**: The board features an onboard 16 GB eMMC Flash memory and 2 GB Low Power DDR4 DRAM.

* **Wireless connectivity**: The board supports 2.4 GHz Wi-Fi® (802.11 b/g/n) and Bluetooth® 5.1, provided by the Murata® 1DX module. This high-performance Wi-Fi® and Bluetooth® module allows the Portenta X8 to communicate wirelessly with other devices and systems.

* **Ethernet connectivity**: The board features an onboard, high-performance 1 Gbps Ethernet transceiver accessible through its High-Density connectors.

* **Secure element**: The board includes a ready-to-use secure element, the SE050C2 from NXP®, tailored for IoT devices and offering advanced security features. This allows Portenta X8 to achieve PSA certification from ARM®. For more information, click [here](https://www.psacertified.org/products/portenta-x8/).

* **USB connectivity**: The board features a USB-C port for power and data, which is also accessible through the board's High-Density connectors. This port is linked to a MIPI to USB-C/DisplayPort converter, enabling video output through the USB-C connection.

* **Power management**: The Portenta X8 includes a power management integrated circuit (PMIC) to meet the demands of always-connected IoT devices.

### Pinout

![Portenta X8 Pinout](assets/ABX00049-pinout.jpg)

The full pinout is available and downloadable as PDF from the link below:
* [Portenta X8 Pinout](https://docs.arduino.cc/static/019dd9ac3b08f48192dcb1291d37aab9/ABX00049-full-pinout.pdf)

### Datasheet

The full datasheet is available and downloadable as PDF from the link below:
* [Portenta X8 Datasheet](https://docs.arduino.cc/resources/datasheets/ABX00049-datasheet.pdf)

### Schematics

The full schematics are available and downloadable as PDF from the link below:
* [Portenta X8 Schematics](https://docs.arduino.cc/resources/schematics/ABX00049-schematics.pdf)

### STEP Files

The full _STEP_ files are available and downloadable from the link below:
* [Portenta X8 STEP files](../../downloads/ABX00049-step.zip)

### Features Overview

Portenta X8 integrates two main programming experiences: the **Yocto Linux** and popular **Arduino** environments.

**DIAGRAM SHOWING MPU + LINUX, MCU (M4) + ARDUINO, COMPUTER, CLOUD + PORTENTA X8 MANAGER**

+-------------------------------------------+         +-------------------------------------------+
|               Yocto Linux (MPU)           |         |      MCU (M4) + Arduino Environment       |
|-------------------------------------------|         |-------------------------------------------|
|  - Embedded Linux OS (Yocto)              |         |  - STM32H7 M4 Core                        |
|  - Components:                            |         |  - Runs Arduino sketches                  |
|     * Bootloader                          |         |  - Real-time control and I/O operations   |
|     * Linux Kernel                        |         |  - Communicates with Linux via RPC        |
|     * Root Filesystem                     |         |                                           |
|  - Manages system resources (CPU, RAM)    |         |                                           |
|  - Handles networking and security        |         +-------------------------------------------+
|  - Executes Docker containers             |                             |
|     * Dockerfile setup                    |                             |
|     * Manages services (RPC, networking)  |                             |
|  - Provides APIs and system services      |                             |
+-------------------------------------------+                             |
           |                                                              |
           +--------------------------------------------------------------+
                                     |                                                       
                               +---------------------------------------+                   
                               |          Portenta X8 Board            |                   
                               |---------------------------------------|
                               |  - Integrates MPU (Linux) & MCU       |
                               |    (Arduino)                          |
                               |  - Dual-core integration (M4 & M7)    |
                               |  - M7 Core facilitates communication  |
                               |    between MPU and MCU                |
                               |  - Manages synchronization            |
                               |  - Hosts both Linux and Arduino       |
                               +---------------------------------------+
                                     |
                                     |
                                     +-----------------------------------+
                                     |                                   |
                        +---------------------------------+   +-------------------------------------------+
                        | Communication & Synchronization |   |          Computer Interface               |
                        |---------------------------------|   |-------------------------------------------|
                        |  - RPC (Remote Procedure Call)  |   |  - ADB/SSH connection to Linux            |
                        |  - Managed by M7 core           |   |  - Arduino IDE for M4 core                |
                        |  - Data exchange between MPU &  |   |  - CLI access to OS & Docker              |
                        |    MCU                          |   |  - Supports local DevOps                  |
                        |  - Involves network protocols   |   |  - Image flashing via `uuu` tool          |
                        |    (TCP/IP, SPI, Shared Memory) |   +-------------------------------------------+
                        +---------------------------------+                  |
                                     |                                       |
                                     +---------------------------------------+
                                                                             |
                                                                +-------------------------------------------+
                                                                |              Cloud Interface              |
                                                                |-------------------------------------------|
                                                                |  - Remote management via Arduino Cloud    |
                                                                |  - Firmware & OS updates                  |
                                                                |  - Secure container management            |
                                                                |  - IoT data and device control            |
                                                                +-------------------------------------------+


To explore specific sections in more detail, please click on the links below that interest you:

* [Linux Environment](#linux-environment)
* [Arduino Environment](#arduino-environment)
* [Arduino Cloud](#portenta-x8-with-arduino-cloud)

### Linux Environment

As you already know, Portenta X8 is based on a Yocto Linux distribution.

Before going into the details of Yocto distribution, it is important to understand how embedded Linux works.

The term **Embedded Linux** refers to embedded systems that use the Linux kernel and other open-source components. Linux has become a leading choice for operating systems on embedded devices due to its open-source nature and the fact that it is freely available.

An **Embedded Linux** system is composed of the following items:

* **Bootloader:** The first program executed right after powering the board. It has the task of initializing the hardware and the operating system, loading the **device tree** and its configuration file into the RAM.

  The **device tree** is a database containing information on the hardware components of the board, which is used to forward information from the bootloader to the Kernel at the hardware level.

* **Linux Kernel:** The core of the operating system. It deals with resource management, scheduling, hardware access and all the low-level operations the user does not want to worry about.

  In particular, the Linux Kernel manages all the hardware resources, like CPU, memory, and I/Os, and it provides a set of APIs that abstracts those resources, allowing the user applications and libraries to be easily deployed.

* **Root Filesystem:** It contains all system programs and utilities, configurations and user data (roughly speaking, the equivalent of the `C:\` drive on Windows). The Root Filesystem can be mounted from a USB stick, SD card or flash memory, being the case of the Portenta X8.

![Embedded Linux Start-Up](assets/Embedded_Linux_Start.png "Embedded Linux Start-Up")

#### Linux Yocto Distribution

To install a Linux operating system on a board, you need to decide which packages, applications, and libraries you want to use, so basically, you need to decide which Linux distribution better suits your needs.

As a matter of fact, a Linux distribution is an operating system consisting of the Linux Kernel, GNU tools, additional software, and a package manager. It may also include a display server and a desktop environment for using it as a regular desktop operating system. More than 300 Linux distributions are available on the market, including Ubuntu, Debian, Fedora, Red Hat, etc.

Portenta X8 is running a [Yocto Linux distribution](https://www.yoctoproject.org/). Yocto is built based on [OpenEmbedded (OE)](http://www.openembedded.org/wiki/Main_Page), which uses [BitBake](https://docs.yoctoproject.org/bitbake/) build to generate a full Linux image. BitBake and OE are combined to form the Yocto reference project, historically called [Poky](https://www.yoctoproject.org/software-item/poky/).

In addition, a full metadata selection is defined to select which tasks to perform. The following metadata is used in a Yocto project:

* **Recipes:** They deliver information regarding each package (i.e. author, homepage, license, etc.), recipe version, existing dependencies, source code location and how to retrieve it, configuration settings, and target path where the created package will be saved. Files with the `.bb` extension are recipe files.

* **Configuration file:** They contain metadata that define how to perform the build process. These files (with the `.conf` file extension) determine the configuration options for the machine, the compiler, the distribution, and general and user configurations. They allow you to set the target where you want to create the image and where you want to save the downloaded sources and other particular configurations.

* **Classes:** Class files with the extension `.bbclass` contain common functionalities that can be shared between various recipes within the distribution. When a recipe inherits a class, it also inherits its settings and functions.

* **File append:** With the extension `.bbappend`, File append extends or overwrites information for an existing recipe.

OpenEmbedded Core contains a recipe layer, classes, and associated files common to all OE-based systems, including Yocto. This metadata set is maintained by both the Yocto project and the OpenEmbedded project.

The Yocto distribution is a development environment that comprises various functional areas, as shown in the figure below.

![Yocto Distribution Architecture](assets/Yocto_Architecture.png "Yocto Distribution Architecture")

* **Layer:** The layers allow you to separate metadata by differentiating them according to software, hardware information, metadata concerning distribution, and adopted policies. Within each layer are the `conf` (with layer-specific configuration files) and `recipes-` directories. To illustrate how to use layers to maintain modularity, consider the example of recipes to support a specific target, which usually resides in a BSP layer.

  In this scenario, those recipes should be isolated from other recipes and supporting metadata, like a new Graphical User Interface (GUI). You would then have a couple of layers: one for the machine's configurations and one for the GUI environment. This would allow a specific machine to present special GUI features within the BSP layer without affecting the recipes inside the GUI layer itself. All of this is possible via an append file.

* **Source file:** To cross-compile any software module, be it a distribution or an application, we must have access to various source files. The latter can be sourced from three different upstream areas: Upstream Project Releases (archived at a specific location), Local Projects (available at a certain local path), and Source Control Managers (like GitHub).

* **Package feeds:** This area contains packages generated by the build system, which will be used later to generate operating system images or Software Development Kits (SDKs).

* **Build System:** The Build System macroblock is the heart of the Yocto distribution. It contains various processes controlled by BitBake, a tool written in Python language. The Build System parses the metadata, extracting the list of tasks to be performed. BitBake checks the software build process by using the recipes. It writes a *stamp* file in the Build Directory for each successfully completed task.

* **Images:** They are compressed forms of the Root Filesystem, ready to be installed on the target. BitBake releases multiple lists of images saved into the Build Directory, including *kernel-image*, *root-filesystem-image*, and *bootloaders*.

* **SDK:** From the SDK generation process you can get a standard SDK or an extensible SDK. In both cases, the output is an installation script of the SDK, which installs a cross-development toolchain, a set of libraries, and headers files, generating an environment setup script. The toolchain can be considered as part of the build system. In contrast, libraries and headers are target parts since they are generated for the target hardware.

***If you want to learn more about how to work with Yocto Distribution on your Portenta X8, please check the [dedicated section](#working-with-linux) of this user manual.***

#### Docker Containers

With Portenta X8, it is possible to deploy device-independent software thanks to its modular container architecture.

To explain how containers work, imagine the classic containers that transport goods worldwide by ship. These container "blocks" can be moved in multiple ways and locations: from a ship to a truck or from a truck to a warehouse. The same thing happens in computer science: you can consider an application, package it with everything needed to make it work, and take it out of the environment in which it runs. This is a container!

![Virtual Machine vs Containers](assets/Virtual_Machine_Containers.png "Virtual Machine vs Containers")

On one side, classic virtualization can virtualize an entire machine; on the other side, containers can virtualize even just a small subset of resources of the same machine.

Traditional virtual machines share hardware resources, but the operating system and applications are on the host. This translates into long start-up times (it takes minutes) and considerable use of resources (several Gigabytes). Containers, on the other hand, share the operating system as well as the infrastructure with the host. This means start-up times are short (a few seconds) and dimensions are significantly reduced (even a few KB).

Being able to "pack" applications and distribute them in any environment leads to various advantages: performance, time, costs, and integration. As a matter of fact, containers can be an interesting way to simplify infrastructure complexity, provide maximum performance and optimize costs by eliminating virtual machine licenses.

But let's see in detail some of the advantages of this technology:

* **Simple development, test and deployment:** The decoupling between applications and the environments in which they run allows you to deploy a container everywhere: on a public Cloud, in a private data center or on a PC. Whatever the chosen environment, the container will always remain the same. This means that even application updates can be released easily without involving the operating system hosting the container or all the other containers in use. In a nutshell, if you have to update an application, restarting the whole machine will not be necessary.

* **Control version:** If the deployment of an update was unsuccessful, thanks to the container architecture, it is easier to roll back and have the previous version working again a few times.

* **Isolation and security:** In containers, applications and resources are isolated. This means that if an application has to be deleted, it will be sufficient to remove its container and the operation will delete everything that concerns it, such as temporary or configuration files. At the same time, since containers are isolated, each of them "sees" only their own processes, while the others will remain unknown. Security first!

* **Granularity:** It is possible to containerize an entire application and a single component. This way, resources can be reduced into microservices, guaranteeing greater control and improved performance.

At this point, it is worth mentioning that Portenta X8 containers are based on [Docker](https://www.docker.com/). Docker is an open-source software platform developed by the company with the same name, which allows you to create, test, and distribute containerized applications. The goal of Docker is, therefore, to facilitate the creation and management of containers in order to distribute the resources required for an application in any environment, always keeping the executed code under control. Docker containers can run everywhere, in on-premises data centers or in public and private Clouds. Thanks to the virtualization at the operating system level, which is typical of this technology, Docker allows you to natively create containers in Linux environments.

It is sufficient to focus on the differences between Docker containers and the more generic Linux containers to understand the purpose of a platform like Docker. Docker mainly serves to simplify the construction and management of containers compared to the standard approach. Although it is based on the same technology, i.e. the **LXC (Linux Container)**, Docker guarantees a much more advanced experience than the standard implementation. LXC allows light virtualization, independent of the underlying hardware, but it is bulky and difficult to implement. In other words, basic LXC presents critical issues in terms of user experience.

Docker specifically simplifies the interface between the container and the end user through a series of automated procedures that guide the user step-by-step during container development, with correct versioning of all the generated images. Docker also simplifies the management of the applications to be run on the different containers, to make the overall orchestration more practical and faster, especially when dealing with applications made of many components.

Therefore, the reasons for using Docker are closely connected to the containers' usefulness, which are now indispensable tools for developing software based on a microservice architecture. In particular, this applies to the DevOps methodologies used for the development of native Cloud applications, which provide for continuous integration / continuous deployment cycles to guarantee the end user always and only the most up-to-date version.

The technology behind containers, and therefore of Docker itself, can be extremely summarized in three key terms:

* **Builder:** tools used to create containers. In the case of Docker, this tool corresponds to the **Dockerfile**.

* **Engine:** is the engine that allows you to run containers, as in the case of **Docker command** and **Docker Daemon**.

* **Orchestration:** technology used to manage containers, with full visibility of their execution status (tasks, servers / VMs, etc.), as in the case of **Docker Swarm** or the famous **Kubernetes**.

The fundamental advantage of a container is that it makes both the application and the execution environment configuration available. This allows you to manage the various images as instances, without having to install the application each time, as in traditional procedures.

As already mentioned, containers running with Docker are isolated and independent of each other. Therefore, it is possible to have complete control over their visibility and management without any constraints. The advantages in terms of IT security are obvious: if a container is corrupted, for example by exploiting a vulnerability of the application it is running, this event does not affect the functioning of the other running containers.

Isolation prevents, or at least makes it more difficult, the propagation of the threat within the host system, allowing Docker to terminate the corrupted instance, restart it in completely safe conditions, and have traces of what happened in the system logs.

Thus, Docker can ensure application security without sacrificing portability, guaranteeing full operation both on-premise and in the Cloud, using open and closed APIs to respond optimally to any business need.

As shown in the image below, Docker needs to be installed in the host operating system and it is composed of three main items:

* ***docker-daemon:*** It is a service that runs on the host operating system and leverages Linux Kernel features to work. It allows the user to create a container and run it, starting from an image developed by the user or downloaded from a registry.
* ***docker-cli:*** It is a command-line tool that allows the user to communicate with the *docker-daemon properly*. As a matter of fact, any operation on images or containers always starts via *docker-cli*. When Docker is installed, both the *docker-daemon* and the *docker-cli* are installed together, and any operation always takes place via *docker-cli*, even if managed via *docker-daemon*.

* ***docker-hub:*** It is a [Docker image repository](https://hub.docker.com/) from which it is possible to download all the images of interest and run them to create containers. Alternatively, a user can create the needed images through a *dockerfile*, using the repository only to download the required base images (like Linux-alpine).

![Docker host](assets/Docker_host.png "Docker host vs client")

Now, it is time to highlight better the difference between an image and a container. In programming languages, an image can be assimilated to a class, while a container to an object. It is possible to create a container starting from an image and then running it, stopping it, or pausing it. It can be deleted without removing the corresponding image when it is no longer needed.

As mentioned, images can be downloaded from a registry like Docker or defined through a *dockerfile*. A *dockerfile* is a text file with all the commands (*FROM, COPY, CMD, ENTRYPOINT, etc.*) a user can call from the command line to build various image layers. The *dockerfile* represents a definition of the image but not the final image, which can be built through the `docker build` command.

A Docker image comprises many layers and includes everything needed to configure a container. In particular, all the layers an image contains are read-only, and consequently, the image itself is also read-only. In this way, it is possible to launch the image several times always creating the same container.

When the container is created, a thin writable layer will be placed on top of the existing image layers and will be prepared to execute the main process command. This last writable layer will contain any changes made when the container is running, but will not affect the original underlying image. When the container is deleted, this thin, writable layer is removed.

An important thing to keep in mind is that, even if Docker shares the Linux Kernel with the underlying host, it is always necessary to add a full operating system or a Linux distribution as the first layer.

![Images and containers](assets/images_containers.png "Images vs containers")

On the other hand, a container represents a process, which runs starting from an image. The important thing to understand is that a container has a lifecycle. For this reason, it can reach different states depending on whether it is running or not. The lifecycle of a Container consists of the following states:

* **Created:** This is the first state of the container lifecycle after creating an image with the command `docker create`. A writable thin layer is created on the specified image and prepared to execute the main process commands. Consider that in this state the container is created but not started.

* **Running:** This is the state where the container runs. A container created through `docker create` or interrupted can be restarted through the command `docker start`.

* **Paused:** A running container can be paused through the `docker pause` command. As a consequence, all the processes of the specified container are suspended or blocked. When a container is paused, the file system and the RAM are unaffected.

* **Stopped:** A stopped container does not have any running process. When a container is stopped through the command `docker stop`, the file system is not affected, but the RAM gets deleted. This is the main difference between stopped and paused states.

* **Deleted:** A container can be removed through the `docker rm` command. This implies the complete cancellation of all the data associated with the container, including file system, volume, and network mapping.

Let's now have a look at the main Docker commands. The complete list can be found [here](https://docs.docker.com/engine/reference/commandline/docker/).
The command `docker image ls` makes it possible to check all the images installed on your Portenta. These images may have been downloaded from a repository using the command `docker pull XXX` or created from scratch with the command `docker build XXX` starting from a *dockerfile*.

Through the command `docker run XXX`, it is possible to run the image downloaded from the repository. But, if a user tries to launch a container through the command, `docker runs XXX` for a container whose image has not been downloaded yet.

First, the image will be downloaded, and then the container will start running.

To verify whether a container is running as expected, it is possible to launch the command `docker ps`.

To summarize, Docker is a powerful technology that prevents users from installing an undefined number of servers and services on a machine. Furthermore, since it runs in an isolated environment, it is possible to move the container or the image to another machine or a production server without friction.

***If you want to learn more about working with Docker containers on your Portenta X8, please check this user manual's [dedicated section](#working-with-linux).***

### Arduino Environment

In addition to what has been addressed, the user can upload sketches on the **M4 core** of **STM32H7** through the **Arduino IDE 1.8.10 or above**.

To do that, it is sufficient to open the Arduino IDE, make sure you have selected the Portenta X8 in the board selector, and start writing your sketch.

***Have a look at [this section](#portenta-x8-with-arduino-ide) of this user manual if you would like to start uploading your sketch on Portenta X8.***

From a user perspective, the process may appear the same as for other Arduino boards, but there are significant differences in what happens behind the scenes: the Portenta X8 includes a service that waits for a sketch to be uploaded to a folder. This service is called `monitor-m4-elf-file.service`: it monitors the directory `/tmp/arduino/` looking for an updated version of the `m4-user-sketch.elf`. Each time it detects a new file, it proceeds to flash the M4 with the new sketch using `openOCD` (check [openOCD website](https://openocd.org/doc/html/About.html) if you want to learn more).

### Communication Between Linux And Arduino

The two processors inside Portenta X8 need a communication mechanism to exchange data. The communication mechanism is called **RPC (Remote Procedure Call)**.

The expression RPC refers to activating a "procedure" or "function" by a program on a computer other than the one on which the program is executed. In other words, RPC allows a program to execute procedures "remotely" on "remote" computers (but accessible through a network).

The idea of transparency is also essential to the concept of RPC. The remote procedure call must be performed in a way similar to that of the traditional "local" procedure call; the details of the network communication must, therefore, be "hidden" (i.e., made transparent) for the user.

The RPC paradigm is particularly suitable for distributed computing based on the client-server model: the "call procedure" corresponds to the "request" sent by the "client," and the "return value" of the procedure corresponds to the "response" sent by the "server." Distributed computing uses the resources of several computers connected to a network (usually via the Internet) to solve large-scale computational problems.

Although the ultimate goal of the RPC paradigm is to provide a remote procedure call mechanism whose semantics are essentially equivalent to that of the local procedure call (hence the aforementioned transparency of the mechanism), this equivalence is never fully achieved due to difficulties that can arise in network communication (always subjected to failure).

Since there is no single obviously "right" way to handle these complications, RPC mechanisms can differ subtly in the exact semantics of the remote call. Some mechanisms, for example, have "at most once" semantics: in other words, a remote procedure call can fail (i.e., not be executed), but it is guaranteed not to result in multiple activations.

The opposite approach is represented by the "at least once" semantics, which guarantees that the procedure is called at least once (it could therefore happen that it is activated several times).

As a consequence, there are multiple types of RPC implementations. In the case of Portenta X8, **MessagePack-RPC** is used (check the [library repository](https://github.com/msgpack-rpc/msgpack-rpc) to get more details). It is an RPC implementation that uses MessagePack as a serialization protocol, i.e., data exchange is encoded in MsgPack format.

It is transported over different protocols:

* OpenAMP via Shared Memory
* SPI
* Linux Char Device
* TCP/IP

![Linux Arduino RPC](assets/linux_arduino_RPC.png "Linux Arduino RPC")

As you can see in the image above, the **M7 core** of **STM32H7** simplifies communication between the Linux and the Arduino environments. If an Arduino sketch runs on the **M4 core**, the **M7 core** will hand over any data/request between the M4 core and the Linux side. Due to this hardware design, traditional dual-core processing is not supported in the Portenta X8.

At the same time, on the Linux side, a service sends data between the two worlds, `m4-proxy`.

So, the communication between Arduino and Linux side will proceed as follows (check the image below):

* A program registers as the RPC server on port X for a list of procedures that the M4 may call
* `m4-proxy` will forward the calls from the M4 to the registered program/port

![RPC M4 proxy](assets/m4-proxy.png "RPC M4 proxy")

***If you want to learn more about working with RPC on your Portenta X8, please check this user manual's [dedicated section](#working-with-arduino-sketch).***

## Portenta X8 OS Image Update

It is recommended that you check every now and then to see if your Portenta X8 image version is up to date to have the latest security updates.

In the next sections, four major ways to update your Portenta X8 are described:

* Update for OS release V.399
* Update through Out-of-the-box experience (available for OS release XXXX or newer)
* Update through Portenta X8 Manager in your Arduino Cloud for Business account (available for all OS releases)
* Update using the `uuu` tool (compatible with custom images)

### Check Portenta X8 OS Release

To verify which OS release is flashed on your Portenta X8, you need to connect to your board through **ADB**, as explained in [this section](#working-with-linux) of this user manual.

You can type `cat /etc/os-release` in your command line window to get the OS release currently running on your device.

![Get OS release](assets/adb-shell-os-release.png "Get OS Release")

As shown in the image above, the OS release of this Portenta X8 corresponds to `IMAGE_VERSION=569`.

### Update For OS Release V.399

If your Portenta X8 is flashed with the OS release V.399 and you have a carrier compatible with Portenta X8 (like Portenta Breakout). In that case, we recommend you update it to the latest image release by following [this tutorial](https://docs.arduino.cc/tutorials/portenta-x8/image-flashing#flashing-mode-with-carrier).

Otherwise, you can also open a new Command Line window and connect to your Portenta X8, as explained [here](#working-with-linux). At this point, verify that your Portenta X8 is connected to the Internet and type the following commands:

```bash
wget https://downloads.arduino.cc/portentax8image/399-install-update
```

```bash
chmod +x 399-install-update
```

```bash
sudo ./399-install-update
```

Remember to set a new admin password at your first access.

***For image versions earlier than 844, the default password for admin access is `fio`.*** 

Now, you need to reboot the board by pressing its pushbutton for around 10 seconds. After that, connect again to your Portenta X8 through the Command Line and type the following commands:

```bash
wget https://downloads.arduino.cc/portentax8image/399-finalize-update
```

```bash
chmod +x 399-finalize-update
```

```bash
sudo ./399-finalize-update
```

These commands will make your V.399 compatible with the [aklite-offline](https://docs.foundries.io/latest/user-guide/offline-update/offline-update.html) tool. They will then allow you to update your Portenta X8 to the latest image version of Arduino released.

Arduino provides this tool for free for any Portenta X8 user to enable offline secure updates to all devices, even if those devices are not connected to any FoundriesFactory.

After the update process is finalized, your Portenta X8 will start running the latest OS release immediately.

### Update Through Out-Of-The-Box Experience

Leverage the integrated Out-of-the-box experience to update your Portenta X8 to the latest release.

***Warning: The Out-of-the-box update feature is not a complete Over-The-Air (OTA) update. It allows users to update only the Portenta X8 default image and containers. It will overwrite any custom container application. Thus, it is recommended to make a local copy of your containers before updating your Portenta X8.***

Open your Out-of-the-box as explained in [this section](#first-use-of-your-portenta-x8).

![Out-of-the-box homepage](assets/OOTB_homepage.png "Out-of-the-box homepage")

Click on **CHECK FOR UPDATES** in the lower right corner.

At this point, you have to select whether you would like to proceed with the update. If yes, click on **UPDATE**.

![Proceed with update](assets/OOTB_update_select.png "Proceed with update")

Please do not turn off your Portenta X8 or disconnect it from the network during the update. This process may take a few minutes.

![Successful update](assets/OOTB-succesful-OS-update.png "Successful update")

Once the update is finished, your Portenta X8 will automatically restart with the new Linux image in place.

At this point, if you want to continue using your Out-of-the-box, you can open a new command line window and launch the command `adb forward tcp:8080 tcp:80` again. Now open your browser, go to [http://localhost:8080](http://localhost:8080), and the same Out-of-the-box dashboard will appear.

#### Troubleshooting

If something goes wrong during the update, you can manually flash your Portenta X8 with the latest Linux image provided at [this link](https://github.com/arduino/lmp-manifest/releases).

You can follow [this section](#update-using-uuu-tool) to learn to use the `uuu` tool and update your device manually with the latest OS Image version. Follow [this dedicated tutorial](https://docs.arduino.cc/tutorials/portenta-x8/image-flashing) to learn how to flash your device manually.

### Update With Portenta X8 Board Manager

If you have an *Arduino Cloud for business* account with the Portenta X8 Manager, check if the target installed on your Portenta X8 is the latest one available in your FoundriesFactory.  

![FoundriesFactory device overview](assets/web_board_manager_factory_device-overview.png "FoundriesFactory device overview")

If this is not the case, you can update your device using FoundriesFactory **Waves** functionality. Check [this tutorial](https://docs.arduino.cc/tutorials/portenta-x8/waves-fleet-managment) to read the complete instructions.

More information about Waves can be found in the official Foundries documentation at [this link](https://docs.foundries.io/latest/reference-manual/factory/fioctl/fioctl_waves.html?highlight=wave).

### Update Using `uuu` Tool

An alternative method to updating the Portenta X8 with the latest OS image is to use the `uuu` command (`uuu_mac` command in case you use MAC OS).

This flash method is helpful if you have built a custom image or desire a more manual approach. Nonetheless, you will need to prepare the OS image files, and the board must be set to programming mode for this flashing process.

***To learn more about creating a custom image for Portenta X8, please check out [How To Build a Custom Image for Your Portenta X8](https://docs.arduino.cc/tutorials/portenta-x8/image-building) tutorial.***

You will need to download the latest OS image file via [Arduino Download repository](https://downloads.arduino.cc/portentax8image/image-latest.tar.gz) and extract the files in a desired directory.

The structure should be similar as follows after also extracting `mfgtool-files-portenta-x8.tar.gz` and `lmp-partner-arduino-image-portenta-x8.wic.gz` that came within the original compressed file:

```
Unzipped folder
├── mfgtool-files-portenta-x8/
├── imx-boot-portenta-x8
├── lmp-partner-arduino-image-portenta-x8.wic
├── lmp-partner-arduino-image-portenta-x8.wic.gz **(Compressed)**
├── mfgtool-files-portenta-x8.tar.gz **(Compressed)**
├── sit-portenta-x8.bin
└── u-boot-portenta-x8.itb
```

#### Set Flashing Mode with Carrier

The Portenta X8 can be set into programming mode using a carrier platform, such as Max Carrier, Breakout, or Hat Carrier, which provides DIP switches for convenient access, or a few more lines of command with barebone Portenta X8 via ADB.

If you plan to use a carrier, please check the carrier's configuration to be paired with Portenta X8.

For the **Portenta Max Carrier**, set the `BOOT SEL` and `BOOT` DIP switches to the ON position as depicted in the figure:

![Portenta Max Carrier DIP switches](assets/max-carrier-dip-switches.png)

Upon executing the `uuu` tool and ensuring the DIP switches are correctly configured, the Portenta Max Carrier will automatically start the flashing operation for the Portenta X8.

For the **Portenta Breakout**, the `BT_SEL` and `BOOT` DIP switches should be set to the ON position, as illustrated in the figure:

![Portenta Breakout DIP switches](assets/breakout-dip-switches.png)

After running the `uuu` tool, perform a long press on the `ON` button of the Portenta Breakout to begin the flashing process. This action enables the tool to identify and connect with the device, continuing with the flashing operation.

For the **Portenta Hat Carrier**, power cycle the Portenta X8, press and hold the `BOOT` button within the first 2 - 3 seconds after powering on, then press the Reset button, and release both buttons to start the flash process.

You can also turn the `BTSEL` DIP switch to the ON position and power cycle the Portenta X8 to start flash process, as depicted in the figure below:

![Portenta Hat Carrier DIP switches](assets/hatCarrier-dip-switches.png)

The `ETH CENTER TAP` DIP switch position does not affect the flashing mode state for the Portenta Hat Carrier.

For the **Portenta Mid Carrier**, the `BOOT SEL` DIP switch should be set to the ON position, as shown in the image below:

![Portenta Mid Carrier DIP switches](assets/midCarrier-dip-switches.png)

Like with the Portenta Max Carrier, the flashing process will commence once the `uuu` tool is run and starts searching for the device.

#### Set Flashing Mode without Carrier

If you decide to flash Portenta X8 without using the carrier, use the following command sequence inside the Portenta X8's terminal via ADB while you are in the root environment with root permission to reset Portenta X8's bootloader sector:

```bash
echo 0 > /sys/block/mmcblk2boot0/force_ro
```

```bash
dd if=/dev/zero of=/dev/mmcblk2boot0 bs=1024 count=4096 && sync
```

```bash
echo 0 > /sys/block/mmcblk2boot1/force_ro
```

```bash
dd if=/dev/zero of=/dev/mmcblk2boot1 bs=1024 count=4096 && sync
```

#### Flashing the Portenta X8 Using `uuu` Command

Now that we have the Portenta X8 in programming mode, we need to flash the OS image. Within the previously described OS image file structure, you need to navigate to the `mfgtool-files-portenta-x8` directory. You will find the `uuu` executable and its components inside the directory. Here, you will open a terminal and run the following command:

```bash
uuu full_image.uuu
```

If Portenta X8 is to be flashed without a carrier, you will want to execute the command **first** to let it search for the board. Subsequently, you will recycle the power source for Portenta X8 by unplugging and reconnecting the USB-C® cable.

It will let the board begin its boot sequence, allowing it to enter programming mode as set with the defaulted internal bootloader. When the active `uuu` instance detects board has entered programming mode, it will continue with its flashing process.

Once the flashing operation finishes, you will be greeted with a similar message in the terminal as the following figure:

![Successful uuu flashing operation](assets/uuu-flashing-success.png)

This applies to both flashing scenarios. If you have the carrier attached and decide to continue using docked with the platform, you must reset the DIP switch positions for either `BOOT SEL`, `BTSEL`, or `BT_SEL` and `BOOT` to OFF state. Reconnect the board and wait approximately 10 seconds until the Blue LED blinks, confirming the boot was successful.

In case the Portenta X8 was flashed barebone, you will need to recycle the power and should be ready with the latest OS image.

***For more in-depth tutorial for flashing Portenta X8, please check out [How To Flash Your Portenta X8](https://docs.arduino.cc/tutorials/portenta-x8/image-flashing) tutorial.***

## First Use Of Your Portenta X8

You can now start interacting with your Portenta X8. Portenta X8 has an embedded configuration console that will guide you step-by-step in configuring your board.  

### Power The Board

Connect the Portenta X8 to your PC via a USB-C® cable (either USB-C® to USB-A or USB-C® to USB-C®).

Once connected, you will see the Portenta X8 LEDs start blinking. Portenta X8 features two LEDs, a Power LED, and a Status LED, which can blink in parallel.

![Portenta X8 LEDs](assets/portenta_x8_leds.png "Portenta X8 LEDs")

The table below describes the meaning and functionalities of LEDs.

| **LED Type** | **Colour** | **Meaning**                                     |
|--------------|------------|-------------------------------------------------|
| Power LED    | Red        | Power ON                                        |
| Status LED   | White      | OS booting in progress                          |
| Status LED   | Blue       | Linux Kernel running                            |
| Status LED   | Green      | Board connected to the Internet                 |
| Status LED   | Red        | STM32H7 LED, blinking when triggered in the IDE |

### Setup with the Arduino Linux Wizard

***It is recommended that you have your Portenta X8 with the latest OS version. Check [this section](#portenta-x8-os-image-update) to learn how to have your Portenta X8 up-to-date.***

Once the Portenta X8 is correctly powered up, you can start interacting with it. 

Open your browser and navigate to [www.arduino.cc/start](www.arduino.cc/start). The following page will be displayed.

![First Setup](assets/registration-homepage.png "First Setup")

Click on **Linux boards** and sign in to your Arduino Cloud account. If you do not have an account, create a new one from the same webpage.

![Sign into Arduino Cloud](assets/registration-signin.png "Sign into Arduino Cloud")

When successfully logged in, you will be asked to download the Arduino Create Agent if you have not done so yet. Click on **DOWNLOAD**.

![Create Agent Installation](assets/agent-installation.png "Create Agent Installation")

The agent will be installed on your computer. This activity might take a few minutes. Once installed, your Portenta X8 will be automatically detected by your PC after a few seconds.

![Portenta X8 successfully detected](assets/board-detection.png "Portenta X8 successfully detected")

Now click on **START CONFIGURATION**. The tool will install all the required add-ons to make your Portenta X8 work efficiently with your PC via serial communication.

You can now proceed to the setup of the board connectivity by clicking **OK, GOT IT**. 

![Out-of-the-box Connectivity Configuration](assets/ootb-wifi-config.png "Out-of-the-box Connectivity Configuration")

***If you face any issue with this flow or prefer to interact directly with your Portenta X8 through the command line, please refer to [this section](#working-with-linux) to learn how to connect with the board leveraging ADB service.***

#### Wi-Fi® Configuration

Click **Wi-Fi® Connection** to start configuring your network connectivity. Otherwise, you can connect your Portenta X8 to the Internet through an Ethernet cable using a USB-C® hub with an RJ45 port or a Portenta Carrier. In this tutorial, Wi-Fi® connectivity will be used.

![Out-of-the-box Wi-Fi® Settings](assets/OOTB_homepage_Wifi.png "Out-of-the-box Wi-Fi® Settings")

Select your Wi-Fi® SSID. You can select a network from the available list or introduce your SSID manually.

![Out-of-the-box Wi-Fi® SSID set-up](assets/OOTB_wifi_selection.png "Out-of-the-box Wi-Fi® SSID set-up")

Type your Wi-Fi® password.

![Out-of-the-box Wi-Fi® password set-up](assets/OOTB_wifi_SSID.png "Out-of-the-box Wi-Fi® password set-up")

Once connected, you will get a notification confirming your Portenta X8 has connected to the selected network, and its LED will start blinking green.

Moreover, you can check the network you are connected to in the bottom left section of this dashboard.

![Out-of-the-box Wi-Fi® connection successful](assets/OOTB_wifi_connected.png "Out-of-the-box Wi-Fi® connection successful")

Now, you can click **OK** and be redirected to the Out-of-the-box homepage below.

![Out-of-the-box Homepage](assets/OOTB_homepage.png "Out-of-the-box Homepage")

***You can change your network by clicking on the Settings button and repeat the steps above.***

#### Arduino Linux Wizard Homepage

This web page is hosted on the Portenta X8 and allows a user to:

- Get board details
- [Configure Portenta X8 Wi-Fi®](#wi-fi-configuration)
- [Interact with the board through the embedded Python® Alpine Shell](#portenta-x8-with-python-alpine-shell)
- [Provision your device to Arduino Cloud](#portenta-x8-with-arduino-cloud)
- Manage the Linux distribution with the dedicated [Portenta X8 Board Manager](#portenta-x8-board-manager)

#### Portenta X8 with Python Alpine Shell

Click the **Shell** button to start using your Portenta X8 with Python-Alpine.

![Out-of-the-box Shell button](assets/OOTB_homepage_shell.png "Out-of-the-box Shell button")

This shell is running in a Python-Alpine container embedded in Portenta X8. You will find multiple examples under the directory `/root/examples` in this shell. Additionally, you can either add your own package through the command `apk add <packagename>` or start exploring the packages available online at [this link]( https://pkgs.alpinelinux.org/packages).

![Out-of-the-box Python-Alpine Shell](assets/OOTB_alpine_shell.png "Out-of-the-box Python-Alpine Shell")

#### Portenta X8 with Arduino Cloud

***Note: this is an optional step. The Portenta X8 can also be used with a local IDE without an internet connection.***

Making Portenta X8 compatible with Arduino Cloud means opening many new applications. This compatibility is guaranteed by a brand-new Python container, which includes a dedicated [Arduino IoT Cloud Python library](https://github.com/arduino/arduino-iot-cloud-py). Through Arduino Cloud APIs, the Python container ensures full interaction and simple porting of any Python developed application in the Arduino Cloud.

***Check all the available Arduino Cloud plans [here](https://cloud.arduino.cc/plans#business) and create your Arduino Cloud account in a couple of steps (see the dedicated documentation at [this link](https://docs.arduino.cc/arduino-cloud/)).***

With the Out-of-the-box experience, your Portenta X8 can be securely self-provisioned in Arduino Cloud; you need to create API keys, and the Python container running on X8 will do the rest. When provisioned, you can start directly interacting with an example Thing and Dashboard that will be automatically generated to guide you in this new journey.

Click the **Arduino Cloud** button to start provisioning your Portenta X8 in Arduino Cloud.

![Out-of-the-box Arduino Cloud](assets/OOTB_homepage_cloud.png "Out-of-the-box Arduino Cloud")

Start setting up the device name for your Portenta X8 (in this case, *portenta-x8-test*) and click on **CONTINUE**. The same device name will be used and visualized in your Arduino Cloud space, but you can freely change it in the future.

![Out-of-the-box Arduino Cloud Device Name](assets/OOTB_cloud_device_name.png "Out-of-the-box Arduino Cloud Device Name")

At this point, you will be asked to insert your API Key credentials and Organization ID. Organization ID is optional and should be filled in only if you use a Shared Space in Arduino Cloud for Business.

![Out-of-the-box Arduino Cloud API Keys](assets/OOTB_cloud_generate_API.png "Out-of-the-box Arduino Cloud API Keys")

To get API keys, log into your Arduino Cloud account and select the Space you would like your X8 to be provisioned into.

Thus, click on **GENERATE API KEY** in your Out-of-the-box dashboard. A new window in your web browser will allow you to log in to your Arduino Cloud space.

***If you want to learn more about what API keys are and how they work, please take a look at the dedicated documentation available at [this link](https://docs.arduino.cc/arduino-cloud/getting-started/arduino-iot-api).***

![Arduino Cloud Login](assets/web_Cloud_login.png "Arduino Cloud Login")

Click on **SIGN IN**. If you do not have an Arduino Cloud account, create a new one from the same webpage.

Sign in to your Arduino Cloud account by adding your credentials, i.e., Username/email and Password.

![Arduino Cloud Sign in](assets/web_cloud_signin.png "Arduino Cloud Sign in")

You are now logged into your Arduino Cloud space. Go on by clicking on **API keys** within the account banner in the top right corner.

![Arduino Cloud Homepage](assets/web_cloud_homepage.png "Arduino Cloud Homepage")

It is time to generate your API keys. Click on **CREATE API KEY** in the upper right-hand corner.

![Arduino Cloud New API Key](assets/web_cloud_new_api.png "Arduino Cloud New API Key")

Define a name for your API key, in this case, *portenta-x8-test-API*, and click on **CREATE**. These API keys are personal and visible only from your account.

![Arduino Cloud API Key name](assets/web_cloud_API_name.png "Arduino Cloud API Key name")

At this point, your API key has been created. Save the correspondent credentials in a safe storage space by clicking on **download the PDF**.

Keep this file safely stored; otherwise, your API credentials cannot be recovered. If you lose it, you will have to generate new API keys by repeating the above procedure.

![Arduino Cloud API Key](assets/web_cloud_API_key.png "Arduino Cloud API Key")

The PDF file will look like the image below and include the credentials you need to copy and paste into the Out-of-the-box page.

![Arduino Cloud API Key PDF](assets/web_cloud_API_key_PDF.png "Arduino Cloud API Key PDF")

Thus, copy the **Client ID** and the **Client Secret** credentials and paste them into your Out-of-the-box dashboard as shown below.

![Out-of-the-box with API Keys](assets/OOTB_cloud_API_copy.png "Out-of-the-box with API Keys")

If you are using an Arduino Cloud for Business account with Shared Spaces. In that case, you also need to add the Organization ID you would like your Portenta X8 to be provisioned into by clicking on **ADD ORGANIZATION**.

![Out-of-the-box successful Cloud provisioning](assets/OOTB_cloud_success.png "Out-of-the-box successful Cloud provisioning")

To recover the Organization ID, known as Space ID, of your Shared Space on Arduino Cloud for Business, open your Arduino Cloud homepage and navigate to **Space Settings > General** in the sidebar on the left.

![Space ID on Cloud Settings](assets/shared-space-settings.png "Space ID on Cloud Settings")

At this point, you can copy the **Space ID** of your Shared Space and paste it into your Out-of-the-box dashboard together with your API keys.

![API keys and Organization ID](assets/OOTB_cloud_organization_ID.png "API keys and Organization ID")

Click on **SETUP DEVICE**, and you are ready to go, your Portenta X8 is now provisioned into your Arduino Cloud space.

![Out-of-the-box successful Cloud provisioning](assets/OOTB_cloud_success.png "Out-of-the-box successful Cloud provisioning")

Once provisioned, the Portenta X8 will be automatically linked to an example [Thing](https://create.arduino.cc/iot/things) and [Dashboard](https://create.arduino.cc/iot/dashboards). You can freely check them by clicking on the corresponding links embedded in the Out-of-the-box.

![Portenta X8 example Thing](assets/cloud_thing_created.png "Portenta X8 example Thing")

As mentioned, Arduino provides an example dashboard that will automatically set up and be visible live after your Portenta X8 has been provisioned. To make this dashboard update its data automatically, you need to go back to your Out-of-the-box and launch the example.

To do so, copying the shown code `python3 examples/arduino_iot_cloud_example.py` and clicking on **Launch Example** is sufficient. An Alpine-Python shell will open, and you will have to paste the previous code here to launch the example.

![Launching dashboard example](assets/OOTB_example_dashboard_launch.png "Launching dashboard example")

Now, you can navigate to your dashboard [here](https://create.arduino.cc/iot/dashboards) to see your Portenta X8 LED blinking and the live temperature inside the microprocessor.

![Portenta X8 dashboard working](assets/cloud_dashboard_working.png "Portenta X8 dashboard working")

***If you face any issues during the provisioning of your Portenta X8, feel free to repeat the procedure above.***

***If you would like to customize your Portenta X8 Things/Dashboards with your custom data, check [this section](#working-with-arduino-cloud) of the user manual.***

#### Portenta X8 Board Manager

***Note: this is an optional step. Although the Portenta X8 Board manager opens a wide range of possibilities that are important for business applications, the Portenta X8 can be used for free without the need for any additional paid license***

Now, you can start connecting your Portenta X8 to the Portenta X8 Board Manager. You need an Arduino Cloud for your business account to leverage this feature.

Check the Arduino Cloud for business plan with Portenta X8 Manager [here](https://cloud.arduino.cc/plans#business) and create your Arduino Cloud account in a couple of steps (see the dedicated documentation at [this link](https://docs.arduino.cc/arduino-cloud/)).

When your Arduino Cloud for business account is correctly set up, log into it [here](https://cloud.arduino.cc/home/) and click on **Portenta X8 Board Manager**. The feature is located within the **Integrations** section of the Cloud.

![Arduino Cloud homepage with Portenta X8 Manager](assets/web_board_manager_cloud_integration.png "Arduino Cloud homepage with Portenta X8 Manager")

At this point, you will be asked to create a new account on [Foundries.io](https://foundries.io/) platform. It is recommended to register with the same email address you are currently using in your Arduino Cloud for business account.

![Foundries.io login](assets/web_board_manager_foundries_login.png "Foundries.io login")

Add all your credentials and click on **Sign up**.

![Foundries.io sign up](assets/web_board_manager_signup.png "Foundries.io sign up")

So, let's create your brand new FoundriesFactory. Select **Arduino Portenta X8**, define a **Factory name** for your Factory, and then click on **Create Factory**.

![FoundriesFactory name](assets/web_board_manager_factory_name.png "FoundriesFactory name")

Your FoundriesFactory is correctly set up. As you can see, the Factory does not have any device connected to it.

![FoundriesFactory homepage with no devices](assets/web_board_manager_factory_overview.png "FoundriesFactory homepage with no devices")

To provision your Portenta X8, go back to your Out-of-the-box webpage and click on the **Portenta X8 Manager** button.

![Out-of-the-box Portenta X8 Manager](assets/OOTB_homepage_portenta_x8_manager.png "Out-of-the-box Portenta X8 Manager")

Enter the Factory name you have just registered, in this case, *user-test*, and assign a Board Name to your Portenta X8. This Board Name will be used to correctly identify your Portenta X8 in your FoundriesFactory. You can now click on **REGISTER**.

![Out-of-the-box Factory and device registration](assets/OOTB_board_manager_factory_registration.png "Out-of-the-box Factory and device registration")

To complete the registration of the Board with the FoundriesFactory, copy the code that appeared in your Out-of-the-box.

![Out-of-the-box Factory code challenge](assets/OOTB_board_manager_factory_challenge.png "Out-of-the-box Factory code challenge")

Click on **COMPLETE REGISTRATION** to be re-directed to the Foundries.io activation page.

Paste your token in the text box and press **Next**.

***The token code is valid for 15 minutes; if you do not paste it in this time span, you will have to repeat all the above registration steps in your Out-of-the-box to generate a new code.***

![FoundriesFactory pasted token](assets/web_board_manager_factory_challenge.png "FoundriesFactory pasted token")

Confirm the addition of your Portenta X8 by pressing **Connect**.

![FoundriesFactory device confirmation](assets/web_board_manager_factory_challange_connect.png "FoundriesFactory device confirmation")

Go to your FoundriesFactory by clicking on **Factories Page**.

![FoundriesFactory device registration completed](assets/web_board_manager_factory_challenge_approved.png "FoundriesFactory device registration completed")

Now you will see the number of devices associated with your FoundriesFactory to be equal to 1.

![FoundriesFactory with 1 device](assets/web_board_manager_factory_device.png "FoundriesFactory with 1 device")

Your Portenta X8 is correctly provisioned into your FoundriesFactory.

To verify your device status, click on your FoundriesFactory, go to the **Devices** section, and check its target update and the installed containers Apps.

![FoundriesFactory device overview](assets/web_board_manager_factory_device-overview.png "FoundriesFactory device overview")

***If you want to learn more about Portenta X8 Manager features, check the dedicated section of this user manual called [Working with Portenta X8 Board Manager](#working-with-portenta-x8-board-manager).***

## Working with Linux

It is time to start interacting with the Linux OS embedded in your Portenta X8. To do that, you need to open your terminal window and look for [**ADB**](https://developer.android.com/studio/command-line/adb) inside the directory **Arduino15/packages/arduino/tools/adb/32.0.0**. The Arduino15 folder may have a different location depending on your Operating System. Check [this article](https://support.arduino.cc/hc/en-us/articles/360018448279-Open-the-Arduino15-folder) to learn where your Arduino15 folder is located.

Android Debug Bridge (ADB) is a tool included in the SDK software (Software Development Kit) and used, among other things, to make an Android device and a computer communicate. To check if ADB is working correctly, you can type `adb devices`. Your Portenta X8 will be listed there.

![Connection with ADB](assets/adb-connection.png "Connection with ADB")

***If you need to install ADB, you can also download the right tool for your Operating System directly from the [official Android website](https://developer.android.com/studio/releases/platform-tools).***

If you want to start the embedded Arduino Linux Wizard from the command line, you can continue typing in your terminal `adb forward tcp:8080 tcp:80`. With this command, ADB allows you to forward the requests of your computer's `8080 TCP-IP port` to the `80 TCP-IP port` of your device, which, in this case, is the device with the name *Portenta X8*.

![ADB forward command](assets/adb-tcp-port.png "ADB forward command")

Now you can open your browser, go to [http://localhost:8080](http://localhost:8080) and the same Arduino Linux Wizard dashboard will appear to allow you to configure your Portenta X8.

![Out-of-the-box Homepage](assets/OOTB_homepage.png "Out-of-the-box Homepage")

Now, you can type `adb shell` to start communicating with your Portenta X8.

![ADB shell command](assets/adb-shell-command.png "ADB shell command")

As it is a Linux device, you can create files, change directories, etc.

To gain admin (root) access, type `sudo su -` and set your own password. 

***For image versions earlier than 844, the default password for admin access is `fio`.*** 

After that, the terminal prefix should turn red.

![ADB shell with admin access](assets/adb-sudo-su.png "ADB shell with admin access")

You can now freely program your Portenta X8 Linux OS. In the sections below, you can check out some basic commands to get started.

### Change Default User Password

For image versions earlier than 844, our Portenta X8 comes with the default user `fio` with password `fio`.

For security reasons, we strongly suggest changing the default password. To do so, when logged in to your Portenta X8, launch this command to change the password of the `fio` account:

```bash
passwd fio
```

### Manage Your Network Via CLI

To connect to a Wi-Fi® Access Point via CLI, you can use the network manager tool **nmcli**. These are some of the most used commands:

* `nmcli device wifi connect <SSID> password <PASSWORD>` to connect to a specific SSID
* `nmcli de` to check the connection status
* `nmcli connection show` to visualize the active network interfaces (and their types) on your Portenta X8

### Accessing Over SSH Session

Establishing communication with the Portenta X8 via an SSH session is possible. To do so, a network connection is needed, either over Wi-Fi® or Ethernet. Using a device with DHCP server capabilities, such as a network router, is recommended for Ethernet connections. After setting up the network connection and DHCP, the Portenta X8 will be ready for SSH communication.

For Windows users, it is necessary to install a service tool to ease the following procedures. While Bonjour, Apple's implementation of zero-configuration networking, comes built into macOS, it is not natively included in Windows and must be installed separately.

***Before proceeding on __Windows__, please install [Bonjour Print Services for Windows](https://support.apple.com/kb/DL999?locale=en_US) before continuing the following steps.***

For macOS and Linux users, *Bonjour* is pre-installed on macOS, and *Avahi-Browse* is typically available on Linux by default. Thus, additional installation steps may be unnecessary for these operating systems.

In the subsequent sections, we will first walk you through the process on Windows, followed by details and instructions for Linux and macOS.

#### Using the Terminal

![SSH Services Availability Discovery](assets/ssh-x8-dns-sd-service.png "SSH Services Availability Discovery")

The command below is used to browse for SSH services on the local network that are advertised over a multicast Domain Name System (mDNS). This protocol resolves hostnames to IP addresses within small networks without a local name server.

```bash
dns-sd -B _sftp-ssh._tcp local
```

By executing this command, you can discover devices offering _SFTP services_ (file transfer over SSH) without prior knowledge of their IP addresses or hostnames.

The command lists these services, indicating where an SSH connection can be established for secure file transfers or shell access, helping to ease the identification and utilization of networked devices that support this protocol.

![Network Query for IPv4 and IPv6](assets/ssh-x8-dns-sd-v4v6.png "Network Query for IPv4 and IPv6")

```bash
dns-sd -G v4v6 portenta-x8-<UUID>.local
```

The command above queries the network for the _IPv4_ and _IPv6_ addresses associated with the hostname `portenta-x8-<UUID>.local`. The _UUID_ can be found within the instance name listed previously or if you have accessed the Portenta X8 via an ADB shell. An example command would look as follows:

```bash
dns-sd -G v4v6 portenta-x8-1822aa09dab6fad9.local
```

This command is handy for finding the IP addresses of devices such as the Portenta X8 that a DHCP server may assign dynamic IP addresses. It simplifies connecting to such devices over the network by providing their current IP addresses.

![Device Ping Test](assets/ssh-x8-dns-sd-ping.png "Device Ping Test")

The following command sends echo requests to the device with the hostname `portenta-x8-<UUID>.local` to check its network availability and measure round-trip time.

```bash
ping portenta-x8-<UUID>.local
```

This command helps verify that the Portenta X8 is online and reachable over the network and for diagnosing connectivity issues. The UUID can be ascertained by referring to the findings from an earlier SSH services scan with network query or the ADB shell.

![Portenta X8 Communication over SSH Session](assets/ssh-x8-session.png "Portenta X8 Communication over SSH Session")

After verifying that the Portenta X8 is accessible using a simple ping test, it is now possible to start an SSH session using the following command:

```bash
ssh fio@portenta-x8-1822aa09dab6fad9.local
```

The example command above starts an SSH (Secure Shell) connection to the Portenta X8 with the hostname `portenta-x8-1822aa09dab6fad9.local` using the username `fio`. The command format should be as follows:

```bash
ssh fio@portenta-x8-<UUID>.local
```

When executing the command, substitute the `<UUID>` placeholder with the actual UUID of the Portenta X8 you are attempting to connect to. You can confirm this UUID by checking the results of a prior SSH services scan with a network query or ADB shell.

If the device is configured correctly to accept SSH connections and the *`fio`* account exists with SSH access, this command will prompt for the password associated with the *`fio`* user.

Upon successful authentication, it will open a secure shell session to the device, allowing for command-line interface access and the execution of commands remotely on the Portenta X8.

The password and the rest of the configuration for using the Portenta X8 inside the shell remain the same.

The process is similar for *GNU/Linux* and *macOS*, with minor differences in the initial steps when browsing for SSH services on the local network.

- **For GNU/Linux**:

Use *Avahi-Browse* to search for SSH services on the local network:

```bash
avahi-browse -d local _sftp-ssh._tcp --resolve -t
```

- **macOS**:

On macOS, you can use the similar command:

```bash
dns-sd -B _sftp-ssh._tcp local
```

Alternatively, you can use a software called *Discovery*, which is available [here](https://apps.apple.com/it/app/discovery-dns-sd-browser/id1381004916?l=en&mt=12).

#### Using Software With GUI

The SSH session can be initialized using third-party software with a Graphical User Interface (GUI) for easy access. An example is a software called *Bonjour Browser*, which can be downloaded [here](https://hobbyistsoftware.com/bonjourbrowser).

![SSH Services Availability Discovery with GUI](assets/ssh-x8-bonjour.png "SSH Services Availability Discovery with GUI")

This software simplifies browsing SSH services on the local network advertised over mDNS using a GUI. The image above, for example, shows all available services on the network, including those for the Portenta X8. You can retrieve the IP address information by simply clicking on a service item.

Once the information is verified, you can use that data with software such as [*PuTTY*](https://www.putty.org/). *PuTTY* is a free and open-source terminal emulator, serial console, and network file transfer application. It supports several network protocols, including *SSH (Secure Shell)* and *SFTP (SSH File Transfer Protocol)*.

![Portenta X8 SSH Session with PuTTY - Setup](assets/ssh-x8-putty.png "Portenta X8 SSH Session with PuTTY - Setup")

In the PuTTY Configuration window, keeping the default values, you must specify the _Host Name (or IP address)_ field with `portenta-x8-<UUID>`. For instance, you would use:

```
portenta-x8-1822aa09dab6fad9
```

Click on `Open`, and it will prompt a security alert. It displays information about the connection, including fingerprint details. Depending on your connection profile preference, you can choose to `Accept` or `Connect Once`.

![Portenta X8 SSH Session with PuTTY - Authentication](assets/ssh-x8-putty-auth.png "Portenta X8 SSH Session with PuTTY - Authentication")

After verifying the security alert and proceeding, you have an SSH session that has begun communicating with the Portenta X8.

![Portenta X8 SSH Session with PuTTY](assets/ssh-x8-putty-session.png "Portenta X8 SSH Session with PuTTY")

### Inspect Real-Time Tasks And Logs Via CLI

Run `journalctl -f` to check the status of active services and possibly their errors, as well as various system event logs.

![ADB shell journalctl package](assets/adb-shell-real-time-tasks.png "ADB shell journalctl package")

By calling `journalctl`, it is possible to look at the log of all the running activities by specifying the type of log you are looking for. Some logs may be a warning that can be ignored, while some may be critical errors. Type `journalctl -p 0` to view emergency system messages; otherwise, change the number 0 with the error code you want to investigate according to the following error code numbers:

| **Error code** | **Meaning** |
|----------------|-------------|
| 0              | Emergency   |
| 1              | Alerts      |
| 2              | Critical    |
| 3              | Errors      |
| 4              | Warning     |
| 5              | Notice      |
| 6              | Info        |
| 7              | Debug       |

When you specify the error code, it shows all messages from that code and above. For example, if you specify error code 2, it shows all messages with priority 2, 1 and 0.

You can also view logs for a specific time and date duration. You can use the `-- since` switch with a combination of `"yesterday"`, `"now"`, or a specific date and time `"YYYY-MM-DD HH:MM:SS"`.

An example of how to use the command:

```bash
journalctl --since "2022-12-22 12:20:00" --until yesterday
```

### Create And Upload Docker Containers To Portenta X8

We created dedicated tutorials covering this topic. Go check them out:

* [Managing Containers with Docker on Portenta X8](https://docs.arduino.cc/tutorials/portenta-x8/docker-container)
* [Deploy a Custom Container with Portenta X8 Manager](https://docs.arduino.cc/tutorials/portenta-x8/custom-container)
* [Running Wordpress & Database Containers on Portenta X8](https://docs.arduino.cc/tutorials/portenta-x8/wordpress-webserver)

### Output Video Content On A Screen

The USB-C® port on your Portenta X8 supports video output. Consequently, you can connect a USB-C® monitor or a USB-C® to the HDMI hub to your Portenta X8 to start visualizing video or other visual renders.

Here you can find a list of validated compatible USB-C® to HDMI hubs:

* [TPX00145](https://store.arduino.cc/products/usb-c-to-hdmi-multiport-adapter-with-ethernet-and-usb-hub)
* [TPX00146](https://store.arduino.cc/products/usb-c-to-hdmi-multiport-adapter-4k-usb-hub-pd-pass-through)

***Learn more on how to output WebGL content on a screen with Portenta X8 by checking the [dedicated tutorial](https://docs.arduino.cc/tutorials/portenta-x8/display-output-webgl).***

### Build A Custom Image For Portenta X8

You may want to build a custom image for the Portenta X8 with the source code provided in the public [GitHub repository of lmp-manifest](https://github.com/arduino/lmp-manifest/). Building an image locally can help debug certain aspects of the system, such as the bootloader or kernel support.

***Have a look at [this dedicated tutorial](https://docs.arduino.cc/tutorials/portenta-x8/image-building) to understand how to build your own custom image.***

### Additional Tutorials

If you want to continue working with your Portenta X8, you can find tons of additional tutorials in the **Tutorials** section of our [Arduino Docs](https://docs.arduino.cc/hardware/portenta-x8). Please go check them out!

## Working With Arduino Sketch

In this section, you will learn how to upload a sketch to the M4 core on the STM32H747XI MCU.

Open the Arduino IDE and download the latest **Arduino Mbed OS Portenta Boards Core**. Learn how to do it by following [this tutorial](https://docs.arduino.cc/software/ide-v1/tutorials/getting-started/cores/arduino-mbed_portenta).

Select Portenta X8 in the board selector.

![IDE Board Selector](assets/x8-IDE.png "IDE Board Selector")

Create a custom sketch or open one of the example sketches, e.g., the blink sketch:

```arduino
void setup(){
 pinMode(LED_BUILTIN ,OUTPUT);
}

void loop(){
 digitalWrite(LED_BUILTIN , HIGH);
 delay(1000);
 digitalWrite(LED_BUILTIN , LOW);
 delay(1000);
}
```

At this point, select the port of your device in the port selector menu and then press the Compile and Upload button.

Behind the curtains, the sketch gets compiled into a binary. That binary file is then uploaded to the Linux side of the Portenta X8. The flashing is done on the board itself by the RPC service running on Linux (see [Communication between Linux and Arduino section](#communication-between-linux-and-arduino) of this user manual to learn more).

When the sketch has been uploaded successfully, the onboard LED of your Portenta X8 will start blinking at an interval of one second.

You can also upload the firmware manually if you like. To do so, you first need to compile the sketch by selecting **Export compiled binary** from the Sketch menu in the Arduino IDE. It will compile the sketch and save the binary file in the sketch folder. Alternatively, you can create a `elf` file using the [Arduino CLI](https://arduino.github.io/arduino-cli/0.29/).

You can use the ADB tool installed as part of the Portenta X8 core to upload the firmware. It can be found at `Arduino15\packages\arduino\tools\adb\32.0.0`.

From that directory, you can use the `adb` tool. To upload your compiled sketch, you need to type the following command into your terminal window:

```
adb push <sketchBinaryPath> /tmp/arduino/m4-user-sketch.elf
```

![ADB upload with a terminal](assets/x8-terminal-ADB-push.png)

You have just learned to use your Portenta X8 with the Arduino IDE. However, you can do much more with the Arduino environment, particularly leveraging the RPC communication between the Arduino and Linux layers.

You can have a look at this [GitHub repository](https://github.com/arduino/ArduinoCore-mbed/tree/master/libraries/RPC/examples) to have access to multiple IDE examples showing how to use RPC communication with Portenta X8.

***Check [Communication between Linux and Arduino](#communication-between-linux-and-arduino) section of this user manual to learn more about RPC.***

You can build an Arduino sketch to manage all the tasks requiring real-time, including sensor communication, Fieldbus management, etc., and then send those data to a Cloud or remote server via multiple connectivity options by leveraging the high-performance network management capabilities of Linux OS.

For instance, try [Data Exchange Between Python® on Linux and an Arduino Sketch](https://docs.arduino.cc/tutorials/portenta-x8/python-arduino-data-exchange) tutorial to learn how to exchange sensor data between the Python® container embedded on Portenta X8 and an Arduino sketch.

Additionally, if you are a more advanced user, you can check [Multi-Protocol Gateway With Portenta X8 & Max Carrier](https://docs.arduino.cc/tutorials/portenta-x8/multi-protocol-gateway) tutorial on developing your multi-protocol gateway: receive data from a sensor with the Arduino layer via MQTT protocol, take advantage of RPC to establish communication between Arduino and Linux, and then send the acquired data to The Things Network via LoRaWAN® managed by the Linux layer.

## Working With Arduino Cloud

To start using your Portenta X8 with Arduino Cloud, provision your device as described in [this section](#portenta-x8-with-arduino-cloud).

Once ready, you can customize Portenta X8, for example, Thing and Dashboard. This can be done by writing your own Python script leveraging the [Arduino IoT Cloud Python library](https://github.com/arduino/arduino-iot-cloud-py). Check the documentation and the examples inside the library to learn more about creating your own Python application.

When your Python script is ready, you have to create a dedicated Dockerfile to integrate your new script. The Dockerfile needs the Out-of-the-box Python container (i.e., `arduino-ootb-python-devel`) to interact with your Arduino Cloud account correctly.

So, open a terminal window and create a Dockerfile integrating the following code with your Python script:

```bash
FROM arduino/arduino-ootb-python-devel:latest
```

```bash
# Copy custom python cloud scripts
COPY ./custom-examples /root/custom-examples
```

```bash
RUN chmod -R 755 /root/custom-examples
```

### Build Your Container

You can create your custom containers and build them inside the Portenta X8. Since Portenta X8 is based on an arm64 architecture, you can use the command `build` only if you build the container directly on an arm64 architecture (e.g., Macbook based on M1/M2 processor or Portenta X8). Open a terminal window and type:

```bash
docker build . -t x8-custom-devel
```

Otherwise, if you are using a different architecture or building machine, use the `buildx` command to specify which architecture your build should compile for:

```bash
docker buildx build --platform linux/arm64 -t x8-custom-devel --load .
```

This way, your Docker image will be built and tagged with the name `x8-custom-devel`.

It is time for you to deploy the newly created Docker image. To do so, save it somewhere and deploy it on your Portenta X8.

### Deploy Your Container With Docker Hub

If you have a [Docker Hub account](https://hub.docker.com/), you can freely upload your Docker image to your registry (e.g., `yourhubusername`):

```bash
docker push yourhubusername/x8-custom-devel
```

Your image is now available in your Docker Hub registry `yourhubusername`.

At this point, you can directly pull the image to your Portenta X8. To do so, connect to your Portenta X8 through ADB. It can be found at `Arduino15\packages\arduino\tools\adb\32.0.0`.

You can pull the image from that directory to the preferred location.

```bash
adb shell
```

With the Portenta X8's terminal, the following command is used.

```bash
docker pull x8-custom-devel
```

Now, your image is correctly deployed on your Portenta X8.

### Deploy Your Container Without Docker Hub

If you do not have a Docker Hub account, you can also save the Docker container locally as a **.tar** file. Then, you can easily load that to an image.

You can use the 'docker save' command to save a Docker image after you have built it. For example, let's save a local copy of the `x8-custom-devel` docker image you made:

```bash
docker save x8-custom-devel:latest | gzip > x8-custom-devel_latest.tar.gz
```

At this point, you can directly pull the image to your Portenta X8. To do so, connect to your Portenta X8 through ADB. It can be found at `Arduino15\packages\arduino\tools\adb\32.0.0`.

```bash
docker import /home/fio/x8-custom-devel_latest.tar.gz x8-custom-devel:latest
```

Now, your image is correctly deployed on your Portenta X8.

### Launch Your Container

To launch your brand new image, you need to create a new `docker-compose.yml`. To do so, first, you must stop the current `docker-compose.yml`.

```bash
cd /var/sota/compose-apps/arduino-ootb && docker compose stop
```

You can now create the path for the new `docker-compose.yml`:

```bash
mkdir /var/sota/compose-apps/custom-devel && cd /var/sota/compose-apps/custom-devel && touch docker-compose.yml
```

Before uploading, open the `docker-compose.yml` and edit it as follows to make it use the Docker image you have just created:

```
services:
 custom:
  container_name: custom-devel
  hostname: "portenta-x8"
  image: x8-custom-devel:latest
      
  restart: unless-stopped
  tty: true
  read_only: false
  user: "0"
  volumes:
    #- '/dev:/dev'
    - '/run/arduino_hw_info.env:/run/arduino_hw_info.env:ro'
    - '/sys/devices:/sys/devices'
    - '/sys/class/pwm:/sys/class/pwm'
    - '/sys/bus/iio:/sys/bus/iio'
    - '/var/sota:/var/sota'
    - './keys:/tmp/keys:ro'
  devices:
    - '/dev/gpiochip5'
    - '/dev/tee0'
```

It is now time to upload the new `docker-compose.yml` to your Portenta X8:

```bash
docker-compose up --detach
```

And you are ready to go! Your Portenta X8 Dashboards and Things can be customized using the same process multiple times.

***If you are using the Portenta X8 Manager, go to [this documentation](https://docs.foundries.io/latest/tutorials/getting-started-with-docker/getting-started-with-docker.html) to learn how to upload the newly created container in your FoundriesFactory.***

## Working With Portenta X8 Board Manager

As mentioned, the Portenta X8 Board Manager allows you to keep your Portenta X8 Linux image and corresponding containers up to date easily, even remotely, through Over-The-Air (OTA) updates (via wireless connectivity).

Subscribe to an *Arduino Cloud for business* plan with Portenta X8 Board Manager to access all these features. Please have a look at [this section](#portenta-x8-board-manager) of the user manual to learn more.

### Device And Fleet Management With Portenta X8 Board Manager

Verify that your Portenta X8 is correctly added to your FoundriesFactory by checking if it is listed among the available devices under the **Devices** section.

![FoundriesFactory device overview](assets/web_board_manager_factory_device-overview.png "FoundriesFactory device overview")

If you want to check if your Portenta X8 is updated according to the latest available Target (i.e., update), you can check the bulb's color under the status column. There are three main color options:

| **Bulb color** | **Meaning**                    |
|----------------|--------------------------------|
| Green          | Device online and updated      |
| Yellow         | Device online and not updated  |
| Red            | Device offline and not updated |

In this case, the Portenta X8 is connected to the network (and to the FoundriesFactory) but has not been updated.

You can see the Target uploaded on your device under the Target column, i.e., *portenta-x8-lmp-569*, and get additional information about what is included in this specific Target by clicking on it.

![FoundriesFactory device target specs](assets/web_board_manager_factory_device_specs.png "FoundriesFactory device target specs")

The above window also shows you all the container apps you have installed on your device, and you can start using them.

If you scroll down in the same window, you can also look at the update history of that specific device.

![FoundriesFactory device update history](assets/web_board_manager_factory_update_history.png "FoundriesFactory update history")

You can now compare the Target uploaded on your Portenta X8 with the Target available in the **Targets** section and decide whether to update your device.

![FoundriesFactory target overview](assets/web_board_manager_factory_target.png "FoundriesFactory target overview")

***Learn how to update your Portenta X8 with your FoundriesFactory by checking the [dedicated section](#portenta-x8-os-image-update) of this user manual.***

This **Target** page contains the Linux images built each time something is committed in the repositories available under the **Source** section. In this section, you can find the four repositories that are used to customize the images:

* **ci-scripts.git:** Scripts that define the platform and container build jobs on the FoundriesFactory system.
* **containers.git:** This is where containers and docker-compose apps are defined. It allows you to define which containers to build/deploy and how to orchestrate them on the platform.
* **lmp-manifest.git:** The repo manifest for the platform build. It defines which layer versions are included in the platform image. This includes [**meta-partner-arduino**](https://github.com/arduino/meta-partner-arduino/), the layer containing Arduino-specific customizations (machine definition, device drivers, etc.).
* **meta-subscriber-overrides.git:** *OE* layer that defines what is included in your FoundriesFactory image. You can add board-specific customizations and overrides or add and remove packages provided in the default Linux microPlatform.

Committing to **lmp-manifest.git** or **meta-subscriber-overrides.git** repositories will create a platform Target, i.e. base Linux platform image. On the other hand, committing to **containers.git** will create a container Target, including all the containers and docker-compose apps you would like to upload on your Portenta X8.

Both these Targets will generate the artifacts specified in the **ci-scripts.git**, which includes all the required files to program the Target in case of platform build.  

### RBAC With Portenta X8 Board Manager

You do not have to be the only one in your organization with permission to update your Portenta X8 devices. The FoundriesFactory integrates a Role-Based-Access-Control functionality (RBAC) to allow users to add multiple teams with multiple members each.

You can start defining a new team by clicking the **Teams** section.

![FoundriesFactory Teams](assets/web_board_manager_team.png "FoundriesFactory Teams")

The level of access and specific permissions are defined by the team’s role in the FoundriesFactory. As you can notice from the image below, multiple roles and permissions are available.

![FoundriesFactory Team roles and permissions](assets/web_board_manager_factory_team_roles.png "FoundriesFactory Team roles and permissions")

Once you created the team, you can go to the **Members** section of your FoundriesFactory to invite new members to the team.

![FoundriesFactory new member](assets/web_board_manager_factory_member.png "FoundriesFactory new member")

You can type the email addresses of your teammates, and they will receive an automatic email with the invitation to join the corresponding team in your FoundriesFactory.

### FoundriesFactory FIOCTL

The FoundriesFactory includes a command line tool called [FIOCTL](https://docs.foundries.io/latest/getting-started/install-fioctl/index.html), which allows you to manage your Portenta X8 through your CLI.

With this tool, you can easily upload containers to a board linked to your FoundriesFactory just by stating the FoundriesFactory name, the board name, and the app you would like to upload.

***Learn how to use this tool by checking the dedicated tutorial at [this link](https://docs.arduino.cc/tutorials/portenta-x8/custom-container) or the corresponding [Foundries documentation](https://docs.foundries.io/latest/getting-started/install-fioctl/index.html).***

## Pins

In order to learn how to properly call GPIOs or other peripherals both in the Arduino environment or in Linux, with or without a carrier, you can check the following pinout diagrams:

* [Portenta X8 pinout](https://docs.arduino.cc/static/019dd9ac3b08f48192dcb1291d37aab9/ABX00049-full-pinout.pdf)
* [Portenta Breakout pinout](https://docs.arduino.cc/static/8d54d1a01d6174ed60fc9698e881ad4c/ASX00031-full-pinout.pdf)
* [Portenta Max Carrier pinout](https://docs.arduino.cc/static/d0bd73b17e97af0fe376b7d518b18660/ABX00043-full-pinout.pdf)
* [Portenta Hat Carrier pinout](https://docs.arduino.cc/resources/pinouts/ASX00049-full-pinout.pdf)
* [Portenta Mid Carrier pinout](https://docs.arduino.cc/resources/pinouts/ASX00055-full-pinout.pdf)

## Communication

In this section, you will learn how to make your Portenta X8 communicate with multiple types of sensors or other external devices, leveraging the wide variety of supported interfaces:

* [SPI](#spi)
* [I2C](#i2c)
* [UART](#uart)
* [Bluetooth®](#bluetooth)

### SPI

In this case, a Portenta X8 with a Portenta Breakout board is used to connect an external SPI device.

#### SPI With Linux

You need to enable SPI support before using SPI devices.

Open Portenta X8 Shell as explained [here](#working-with-linux).

```bash
sudo modprobe spi-dev
```

Insert the user password.

An upcoming image release for the X8 will load the `spi-dev` modules automatically at boot. In the current version, please create a `/etc/modules-load.d/spi-dev.conf` file with the following content:

```bash
spi-dev
```

and restart the board.

```bash
echo "spi-dev" | sudo tee > /etc/modules-load.d/spi-dev.conf
```

```bash
sudo systemctl reboot
```

Add the device you want to communicate within a container in a `docker-compose.yml` file: 

```
services:
 my_spi_service:
 devices:
 - /dev/spi-1
 - /dev/spi-2
 - /dev/spi-3
```

If the Linux user on which the container is running is not `root`, you need to set up the permissions for the user to access the SPI devices. You might add the required comments to an `entrypoint.sh` shell file (to be added to the `Dockerfile` or the `docker-compose.yml` file).

```bash
#!/usr/bin/env sh

# entrypoint.sh example

chgrp users /dev/spi-*
chmod g+rw /dev/spi-*
usermod -aG users <container user>

# Possible command to execute your application as a non-privileged user with gosu
# Check https://github.com/tianon/gosu for more information
gosu <container user> /usr/bin/python my_spi_service.py
```

#### SPI Port Mapping

| Linux | Arduino Portenta Breakout |
|-------|---------------------------|
| 134   | **`SPI1 CK`**             |
| 135   | **`SPI1 COPI`**           |
| 136   | **`SPI1 CIPO`**           |
| 137   | **`SPI1 CS`**             |

#### SPI With Arduino

The `SPI` object is [mapped](https://github.com/arduino/ArduinoCore-mbed/blob/23e4a5ff8e9c16bece4f0e810acc9760d3dd4462/variants/PORTENTA_X8/pins_arduino.h#L85) as follows on the Portenta Breakout Board and can be deployed as usual:

| **SPI Pin** | **Arduino Portenta Breakout** |
|-------------|-------------------------------|
| CIPO        | Pin 0 (Header GPIO0)          |
| COPI        | Pin A6 (Header Analog)        |
| SCK         | Pin A5 (Header Analog)        |
| CS          | Pin 1 (Header GPIO0)          |

### I2C

In this case, a Portenta X8 with a Portenta Breakout board is used to connect an external I2C device.

#### I2C With Linux

You need to enable I2C support before using I2C devices.

Open Portenta X8 Shell as explained [here](#working-with-linux).

Thus, execute the following command:

```bash
sudo modprobe i2c-dev
```

Insert the user password `fio`.

An upcoming image release for the X8 will load the `i2c-dev` modules automatically at boot. In the current version, please create a `/etc/modules-load.d/i2c-dev.conf` file with the following content:

```bash
i2c-dev
```

and restart the board.

```bash
echo "i2c-dev" | sudo tee > /etc/modules-load.d/i2c-dev.conf
```

```bash
sudo systemctl reboot
```

Add the device you want to communicate within a container in a `docker-compose.yml` file: 

```
services:
 my_i2c_service:
 devices:
 - /dev/i2c-1
 - /dev/i2c-2
 - /dev/i2c-3
```

If the Linux user on which the container is running is not `root`, you need to set up the permissions for the user to access the I2C devices. You might add the required comments to an `entrypoint.sh` shell file (to be added to the `Dockerfile` or the `docker-compose.yml` file).

```bash
#!/usr/bin/env sh

# entrypoint.sh example

chgrp users /dev/i2c-*
chmod g+rw /dev/i2c-*
usermod -aG users <container user>

# Possible command to execute your application as a non-privileged user with gosu
# Check https://github.com/tianon/gosu for more information
gosu <container user> /usr/bin/python my_i2c_service.py
```

#### I2C Port Mappings

| **Linux**    | **Arduino Portenta Breakout** | **Notes**   |
|--------------|-------------------------------|-------------|
| `/dev/i2c-1` | **`I2C1`**                    |             |
| `/dev/i2c-2` | **`I2C0`**                    | Recommended |
| `/dev/i2c-3` | **`I2C1`**                    |             |

#### Examples

Examples of using SMBus-compatible [libraries](https://github.com/kplindegaard/smbus2):

```python
from smbus2 import SMBus

# Connect to /dev/i2c-2
bus = SMBus(2)
b = bus.read_byte_data(80, 0)
print(b)
```

Example of using [python-periphery](https://python-periphery.readthedocs.io/en/latest/index.html):

```python
from periphery import I2C

# Open i2c-0 controller
i2c = I2C("/dev/i2c-2")

# Read byte at address 0x100 of EEPROM at 0x50
msgs = [I2C.Message([0x01, 0x00]), I2C.Message([0x00], read=True)]
i2c.transfer(0x50, msgs)
print("0x100: 0x{:02x}".format(msgs[1].data[0]))

i2c.close()
```

#### I2C With Arduino

The `Wire` object is [mapped](https://github.com/arduino/ArduinoCore-mbed/blob/23e4a5ff8e9c16bece4f0e810acc9760d3dd4462/variants/PORTENTA_X8/pins_arduino.h#L113) to pins `PWM6` (I2C `SCL`) and `PWM8` (I2C `SDA`) on the Portenta Breakout Board and can be deployed as usual.

Since one of the `I2C` pins is GPIO-multiplexed, you need to detach it from the other GPIO. Just add the following line to the `setup()` definition to make it fully functional for `I2C` operations.

 ```arduino
 void setup() {
  pinMode(PA_12, INPUT);
 }    
 ```
 
### UART

In this case, a Portenta X8 with a Portenta Breakout board is used to explore UART communication.

#### UART With Linux

A standard UART is available as `/dev/ttymxc1` in Linux and is mapped to the **`UART1`** port on the Portenta Breakout.

### Bluetooth®

Portenta X8 supports Bluetooth® connectivity just on the Linux side.

In order to communicate with Bluetooth® devices via the Portenta X8 Shell, you can use the Bluetooth® utility **bluetoothctl**. These are some of the most used commands:

* `bluetoothctl devices` to list all the available Bluetooth® devices
* `bluetoothctl pair [mac_address]` to pair with a specific device through its MAC address
* `bluetoothctl connect [mac_address]` to connect to a paired device
* `bluetoothctl disconnect [mac_address]` to disconnect from a paired device

***Do you want to send data from your Nicla to Portenta X8 via BLE? Check [this link](https://github.com/Zalmotek/arduino-environmental-monitoring-with-arduino-pro) to get started.***

## Support

If you encounter any issues or have questions while working with the Portenta X8, we provide various support resources to help you find answers and solutions.

### Help Center

Explore our [Help Center](https://support.arduino.cc/hc/en-us), which offers a comprehensive collection of articles and guides for the Portenta X8. The Arduino Help Center is designed to provide in-depth technical assistance and help you make the most of your device.

- [Portenta Family help center page](https://support.arduino.cc/hc/en-us/sections/360004767859-Portenta-Family)

### Forum

Join our community forum to connect with other Portenta X8 users, share your experiences, and ask questions. The forum is an excellent place to learn from others, discuss issues, and discover new ideas and projects related to the Portenta X8.

- [Portenta X8 category in the Arduino Forum](https://forum.arduino.cc/c/hardware/portenta/portenta-x8/172)

### Contact Us

Please get in touch with our support team if you need personalized assistance or have questions not covered by the help and support resources described before. We're happy to help you with any issues or inquiries about the Portenta X8.

- [Contact us page](https://www.arduino.cc/en/contact-us/)
