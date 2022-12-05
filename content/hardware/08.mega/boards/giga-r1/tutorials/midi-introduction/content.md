---
title: 'Introduction to MIDI Control Systems'
tags:
  - GIGA R1
  - MIDI
description: 'This tutorial introduces MIDI control systems and how you can implement them using Arduino® hardware and software, mainly using the GIGA R1 board.'
author: 'José Bagur and Taddy Chung'
hardware:
  - hardware/08.mega/boards/giga-r1
software:
  - ide-v1
  - ide-v2
  - web-editor
  - iot-cloud
---

## Overview

When we talk about MIDI, we usually think about a sound machine, but in reality, MIDI is entirely different, although it is essential in sound production. In this tutorial, we will learn the basics of MIDI control systems and how to implement one using the Arduino ecosystem, particularly the GIGA R1.

## Goals

- Learn how MIDI can control audio devices
- Learn how to implement a MIDI control system using the Arduino ecosystem

### Required Hardware and Software

- Arduino GIGA R1 (x1)
- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2.0+](https://www.arduino.cc/en/software), or [Arduino Web Editor](https://www.arduino.cc/en/software)
- If you choose the offline Arduino IDE, you must install the following library: [`MIDIUSB`](https://github.com/arduino-libraries/MIDIUSB)

## MIDI Control Systems

The Musical Instrument Digital Interface (MIDI) is a widely used digital control system in music production; it combines a hardware interface with an asynchronous serial communication protocol. Since 1982 (40 years ago!), when the MIDI 1.0 specification was released for the first time, it has been a standard in the music production industry. One of the main characteristics of MIDI is its simplicity; because of this, it has been adapted to other digital interfaces, such as USB, Ethernet, and Bluetooth® for audio control. The original MIDI hardware interface used a 5-pin DIN connector; to avoid noise problems between connected MIDI devices, an optocoupler was placed between. A basic MIDI control system is shown in the image below:

![A basic MIDI control system.](assets/midi-introduction_001.png)

A MIDI controller, usually called a sequencer, controls an audio synthesizer. The sequencer sends MIDI data into the synthesizer that tells it what to do, precisely what notes to generate, and when to do it. Notice that the MIDI controller, the sequencer, does not generate any audio signal or produce any sound. The synthesizer is in charge of generating audio signals at the command of the MIDI controller data. 

> MIDI does not produce any sound; it just describes it.

### MIDI Control Messages

MIDI control messages are described in the image below:

![A common 3-byte MIDI message example.](assets/midi-introduction_002.png)

Common MIDI messages are 3-byte messages that consist of a control byte that defines the type of the message (`note ON` or `note OFF`) and the channel used (1-16), and one or more data bytes that provide specific information about a particular note (note number and note velocity). Notice that the status byte starts with a binary `1`, and the data bytes begin with a binary `0`. Notice that a single MIDI control system can be connected to up to 16 devices! 

Although MIDI use in the music production industry is still widespread, it has some limitations. MIDI 1.0 does not provide any feedback to the sequencer from the MIDI devices, for example, from a synthesizer; communication was proposed in the specification just in one direction. To address this issue, the MIDI Manufacturers Association (MMA) recently introduced a major MIDI 1.0 protocol revision: the MIDI 2.0 specification. In MIDI 2.0 specification, device profiling and bi-directional communication are the most significant changes. 

## MIDI and Arduino

There are two ways to implement a MIDI control system using the Arduino ecosystem. The first is to implement MIDI over Serial through a 5-pin DIN connector; the second is to implement MIDI over USB using the MIDIUSB library and a USB-native Arduino board. We will discuss both ways in the sections below. But before we discuss MIDI over Serial and MIDI over USB, let's talk about the standard MIDI out interface described in the image below:

![Standard MIDI out interface.](assets/midi-introduction_003.png)

The schematic above describes the standard MIDI out interface published by the MMA in 1985. The interface consists of a UART transmitter sending data at 31250 baud through two operational amplifiers and a 220-ohm current limiting resistor (defined by the MIDI specification) to pin 5 of a DIN connector. Pin 4 of the DIN connector is set to +5VDC (also using a 220-ohm current limiting resistor), while pin 2 of the DIN connector is set to GND. Pin 1 and 3 are not used in the standard MIDI out interface. This information is essential to design and implementing MIDI control systems from scratch.

Now let's talk about MIDI over Serial!

### MIDI Serial

### MIDI USB

## Conclusion

## References