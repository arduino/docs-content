---
title: 'Particle Detector with the Portenta Vision Shield'
description: 'Make your very own particle detector with the Portenta Vision Shield and a Portenta H7.'
tags: 
  - tutorial
author: 'Ali Jahangiri' 'Francesca Cenna'
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

- 

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

In this application note, we use a modified version of the Blob Detection tutorial. [[Explain Why we do this and what the code does]]

## Programming the Board

Example code for the reader to copy and paste into their own sketch. This section should explain the different sections in the code. 

## Testing It Out

After uploading the code, we should now start using it. Go through the flow with the reader. 

### Troubleshoot

Add a bullet list of the things that could be the potential issue for something not working. 

If the code is not working, there are some common issues we can troubleshoot:

- Troubleshoot point 1
- Troubleshoot point 2

## Conclusion

Add a conclusion to what this tutorial has gone through. Connect back to what you wrote in the "Goals" section. 

