---
title: Portenta X8 Foundations
difficulty:
tags: []
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

The Portenta X8 is one of the more advanced boards available from Arduino. In this article we will go through some of the foundations of the Portenta X8 and help you understand how the board works. Especially how containers on the Portenta X8 works.

## Goals

- Learn more in depth information about how the Portenta X8 works
- Learn how containers work
- Learn why we decide to implement containers on the Portenta X8

### Required Hardware and Software

-   Portenta X8
-   Factories
-   Floctl

## Instructions

If you need help with setting up your board then please have a look at the [Getting started tutorial](). When you have your board set up and want to explore the different options available to you. 

### Factories

When you have your board connected to a factory you can then wirelessly change the container on the board.

FoundriesFactory is the start of your embedded OS, tailored specifically for your product. When you create a Factory, we immediately bootstrap the CI build process for a vanilla, unmodified Linux microPlatform OS Image, which is from this point onward, owned by you.

### Conatiners

The conatiners available on your factory page can be easily updated by pushing your changes to the git repository that is linked. This way you can get new releases of your code to your board in a quick and easy way. 

A Linux® container is a set of processes that are isolated from the rest of the system. All the files necessary to run them are provided from a distinct image, meaning Linux containers are portable and consistent as they move from development, to testing, and finally to production. This makes them much quicker to use than development pipelines that rely on replicating traditional testing environments.

### Benefits of container

Imagine you’re developing an application. You do your work on a laptop and your environment has a specific configuration. Other developers may have slightly different configurations. The application you’re developing relies on that configuration and is dependent on specific libraries, dependencies, and files. Meanwhile, your business has development and production environments that are standardized with their own configurations and their own sets of supporting files. You want to emulate those environments as much as possible locally, but without all the overhead of recreating the server environments.

So, how do you make your app work across these environments, pass quality assurance, and get your app deployed without massive headaches, rewriting, and break-fixing? The answer: containers.

The container that holds your application has the necessary libraries, dependencies, and files so you can move it through production without nasty side effects. In fact, the contents of a container image can be thought of as an installation of a Linux distribution because it comes complete with RPM packages, configuration files, etc. But, container image distribution is a lot easier than installing new copies of operating systems.

That’s a common example, but Linux containers can be applied to many different problems where portability, configurability, and isolation is needed. The point of Linux containers is to develop faster and meet business needs as they arise. In some cases, such as real-time data streaming with Apache Kafka, containers are essential because they're the only way to provide the scalability an application needs. No matter the infrastructure—on-premise, in the cloud, or a hybrid of the two—containers meet the demand. Of course, choosing the right container platform is just as important as the containers themselves.

## Conclusion

Now you should have a better understanding of how the Portenta X8 works. And have a better picture of how to utalize its full potential.