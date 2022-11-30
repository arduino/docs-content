---
title: 'Connecting an Audio Amplifier to the GIGA R1'
tags:
  - GIGA R1
  - Digital-to-analog converter
  - Audio amplifier
description: 'This tutorial shows how to connect an audio amplifier to one of the digital-to-analog-converters of the Arduino® GIGA R1.'
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

When we talk about audio, you probably imagine a speaker playing some sounds or music. The GIGA R1 is a powerful Arduino® board with advanced audio capabilities that we can use to play sounds and develop interesting audio applications. In this tutorial, we will learn how to use one of the digital-to-analog converters (DAC) of the GIGA R1 to play sounds through an audio amplifier. Specifically, we will use DAC0 of the GIGA R1 and the almighty LM386 integrated circuit (IC) to build an audio amplifier from scratch; we will also show in the tutorial how to use a ready-available audio amplifier also with DAC0 of the GIGA R1.

## Goals

- Use one of the digital-to-analog converters (DAC) of the GIGA R1 to generate sound, specifically DAC0
- Build an audio amplifier from scratch using the LM386 IC
- Connect an audio amplifier to DAC0 of the GIGA R1

### Required Hardware and Software

- Arduino GIGA R1
- LM386 (x1)
- 470pF capacitor (x1)
- 0.1μF capacitor (x3)
- 10μF capacitor (x2)
- 100μF capacitor (x1)
- 1000μF capacitor (x1) 
- 10Ω resistor(x1)
- 10KΩ resistor (x1)
- 10KΩ potentiometer (x2)
- TRRS 3.5mm jack connector breakout board (x1)
- 8Ω speaker (x1)
- Audio cable (x1)

## Digital-to-Analog Converters

A digital-to-analog converter, commonly referred to as DAC, is a device that converts digital values (binary values that can be 0 or 1) to analog voltages. DACs can be found as peripherals of microcontrollers, but only some have one inside. If a microcontroller does not have an integrated DAC, you can build one using different techniques and approaches or buy one already available. 

The GIGA R1 has two internal DACs (`DAC0` and `DAC1`) that we can use for generating analog voltage from digital input. `DAC0` and `DAC1` in the GIGA R1 are connected to its 3.5mm stereo jack connector (`J15`). `DAC0` is connected to the right channel, while `DAC1` is connected to the left channel. In this tutorial, we will use just one DAC of the GIGA R1 to generate a sound and then play it via an audio amplifier and a speaker. Let's build an audio amplifier and connect it to the GIGA!

## A Simple Audio Amplifier Using the LM386 IC