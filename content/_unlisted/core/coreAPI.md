---
title: Arduino Core API
description: Introduction to Arduino Core API
revision: Rev. 00
type: 
authors: Dario Pennisi
---

# Introduction
Arduino language has grown far beyond expectations and gathered a huge community around the simplicity of its API and breadth of supported hardware.
The original platform has born around a tiny 8 bit microcontroller while now Arduino is running on almost any microcontroller and its API have expanded rapidly and sometimes wildly.
For the above reasons a few years ago Project Chainsaw was started, drawing a clear separation line between hardware related code and high level API that form the core of the Arduino language.
More recently clever scripting allowed to base Arduino Core API on top of mbed OS, thus making it extremely easy to port Arduino Core on top of any mbed OS supported platform.
The next goal is to expand Arduino Core API to provide a unified API around more functions such as file systems, string manipulation, time management, etc. 
This effort aims to unify the calling conventions so that ideally every library that implements a platform specific variation of a functionality will expose the same base functions thus easing code portability and reusability.
In order to avoid locking in functionality and allow contributors to expand on APIs the programming model is centered around base classes which provide only general use function implementations, leaving specifics to library implementation.

# Inheritance
The key technical aspect of Arduino Core API is class inheritance: every API is wrapped in a container class where methods are mostly virtual. This means that Arduino Core API only defines the calling convention and leaves implementation to the library that will derive the base class.
Of course it's possible to extend Core API by adding functions in derived classes however if you feel the need for something that's missing Arduino strongly recommends to open a pull request to the Core API so that your proposal is standardized and the result of your contribution will be adopted also by other libraries.

# Contribution Guidelines
In general Core API have to be following Arduino coding guidelines that praise simplicity and tries to avoid complex constructs. It is also important to motivate API choices with use cases and code examples as this would make it clearer to the reviewers and to community how to use the API and what issues it's trying to solve.
In general the rules for the API are summarized in the [ API Style Guide ]( https://www.arduino.cc/en/Reference/APIStyleGuide ) while for examples they're in the [Coding Style Guide] (
https://www.arduino.cc/en/Reference/StyleGuide )

# API classes

## core
* [Time](API/time.md)
* [Strings](API/strings.md)
* [Low Power](API/lowpower.md)
* [Print](API/print.md)

## Buses
* [BusDevice](API/busdevice.md)

## storage
* [BlockDevice](API/blockdevice.md)
* [File](API/file.md)
* [FileSystem](API/filesystem.md)

## Communication
* [Networking](API/networking.md)
* [BLE](API/ble.md)

## Multimedia
* [Audio](API/audio.md)
* [Video](API/video.md)
