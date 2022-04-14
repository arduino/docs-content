---
title: 'Managing Containers with Docker on Portenta X8'
description: 'This tutorial shows how to install and manage your containers using Docker.'
difficulty: easy
tags:
  - containers
  - Docker
  - Hello-World
author: 'Pablo Marquínez'
software:
  - Terminal
  - Docker
hardware:
  - hardware/04.pro/boards/portenta-x8
---

## Overview

[Docker](http://docker.com) Is a platform full of applications, called containers. Containers are isolated solutions and thus they don't have to depend on your environment. Making them portable and consistent throughout development, testing and production.

You can download, install, use and share applications in the form of containers. You can find all the available containers on the [hub.docker.com](hub.docker.com) page.

In this tutorial we will go through the steps of how to install, run and remove the [Hello-World Container](https://hub.docker.com/_/hello-world)

## Goals

- List the installed and running containers
- Install a container
- Run a container manually
- Uninstall a container

### Required Hardware and Software

- [Arduino Portenta X8](https://store.arduino.cc/products/portenta-x8)
- USB-C cable (either USB-C to USB-A or USB-C to USB-C)
- Wi-Fi Access Point with Internet Access
- ADB or SSH. [Check how to connect to your Portenta X8](docs.arduino.cc/tutorials/portenta-x8/out-of-the-box#controlling-portenta-x8-through-the-terminal)

## Using Docker

The Docker CLI comes with your Portenta X8 by default, you can check if the tool is installed by typing:
```
docker -v
```

***To use this tool, first of all you will need to connect to your device, check [how to connect using adb/ssh](/tutorials/portenta-x8/out-of-the-box#controlling-portenta-x8-through-the-terminal).***

You can check the Docker reference documentation, which covers all the features of the tool in depth at [https://docs.docker.com/](docs.docker.com).

The following steps shows how to install, run and uninstall the "Hello World" container.

### Install A Container

You will need to find your Docker container, on its Docker hub page it will show you how to install the desired container.

https://hub.docker.com/_/hello-world

```
docker pull hello-world
```

![Docker CLI pulling a container](assets/docker-pull.png)

### Run The Installed Container

```
docker run hello-world
```

![Docker CLI running Hello World app](assets/docker-run.png)

***To be able to see your container with `docker ps -a` you will need to run it at least once with `docker run`***

### Listing The Installed Packages
List the installed containers with the following command: 
``` 
docker ps -a
```

![Docker CLI listing all the installed containers](assets/docker-ps.png)

Keep in mind that you will need to get the `CONTAINER ID` to uninstall the container afterwards.

If you didn't run your container you can also check if it's correctly installed by using:
```
docker images
```

![Docker CLI images](assets/docker-images.png)

### Uninstall A Container

First get the Container ID from the container list.

Then use the remove (`rm`) command 
```
docker container rm <CONTAINER ID>
```

In this case we run `docker ps -a` and I copied the `CONTAINER_ID` which is `c44ba77b65cb`.

***`CONTAINER_ID` changes its value every time you re-install them***

![Docker CLI container uninstall](assets/docker-container-rm.png)

If you run `docker images` again you will see that the container is not showing up anymore.

## Conclusion

In this tutorial you learned how to install a container onto your device, run it and manage it.

### Next Steps

- Now that you have the base of the workflow to use [Docker](https://docker.com), go to its docs page and make sure you understand all the features.
- Look for a container from [Docker hub](http://hub.docker.com), install it and make your own application out of it.
- Create a container to run your custom made application.