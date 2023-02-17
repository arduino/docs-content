---

title: 'Particle Detector with the Portenta Vision Shield'
description: 'Make your very own particle detector with the Portenta Vision Shield and a Portenta H7'
tags: 
  - tutorial
author: 'Ali Jahangiri & Francesca Cenna'
hardware:
  - hardware/04.pro/shields/portenta-vision-shield
  - hardware/04.pro/boards/portenta-h7
  - hardware/04.pro/boards/portenta-h7-lite
  - hardware/04.pro/boards/portenta-h7-connected
software:
  - openmv
difficulty: intermediate
tags: [OpenMV, Blob Detection, Physics]

---

## Introduction 

We live in a world, full of particles. In particular, we are showered by cosmic particles everyday which are refered to as, convinently, cosmic showers. While there are many ways to detect these, here we will use the CMOS sensor in the Portenta Vision Shield to detect them, with some help from OpenMV. 

## Goals

- Understand how CMOS detectors work
- Use the OpenMV environment to identify particles
- Measure muons with the Portenta Vision Shield

## Hardware & Software Needed

List the hardware and software needed. This could be the IDEs, libraries but also the hardware such as the board for example. Make sure to link to whatever you are listing. 

- 
- [Portenta H7](https://store.arduino.cc/portenta-h7).
- [Portenta Vision Shield](https://store.arduino.cc/portenta-vision-shield).
- [OpenMV IDE 2.9.0+](https://openmv.io/pages/download)


## Cosmic Rays

Cosmic showers happen when a high-speed particle from space, called a cosmic ray, hits the earth's atmosphere. This creates a chain reaction of secondary particles. These particles spread out and create a shower that can cover a big area. Studying these particles can help us learn a lot about outer space as well as the earth's atmosphere.

Cosmic showers are a natural source of particles so they are accessible anywhere in the world! 

## Portenta Vision Shield as a Particle Detector

The Arduino Portenta Vision Shield includes a Himax HM-01B0 camera module at a resolution of 320x320. The CMOS detector is a type of solid state detector. In addition to detecting light (photons), the detector can also detect muons. The Portenta Vision Shield is well suited to detecting muons, since there is not cover/filter on top of the camera that could absorb the incoming particles.

## OpenMV and Blob Detection

In this application note, we use a modified version of the Blob Detection tutorial. This code disables the LED from blinking, that is required to ensure that all photons are related to muon activity. Change area_threshold=255 to pixel_threshold=1 and merge blobs. [[Explain Why we do this and what the code does]]

## Set up 

**1.** Connect Portenta Vision Shield to Portenta H7. Use a USB-C cable to connect to a PC. 

**2.** Place the camera to face upwards in a dark box.

**3.** Program the Portenta H7 with the modified blob detection code in OpenMV. [[Lead shielding?]] [[Why not inside house?]]

**4.**  Data is saved to SD card. Repeat measurements with a vertical orientation.

## Data Analysis

**1.** Import data into Google Sheets for both orientations.

**2.** Do the analysis???

### Troubleshoot

If the code is not working, there are some common issues we can troubleshoot:

- Increase the duration of data collection. A time of at least 24 hours is recommended. A longer time, results in more accurate results.
- Make sure that the Blob example is alterated as instructed
- Ensure that no stray light impacts the CMOS sensor of the Portenta Vision Shield

## Conclusion

In this tutorial you learnt how to measure muons with the Portenta Vision Shield. You can take this a step further, and explore how muon showers change over time. Or, set up multiple devices which connect to the Arduino IoT Cloud and see how particle counts vary over time and position. 

