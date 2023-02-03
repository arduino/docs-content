---
title: Guide to the Arduino® GIGA R1 and Tiny Machine Learning
description: 'This guide shows how, with the Arduino ecosystem, you can turn your GIGA R1 board into a versatile, powerful, and professional tiny machine learning solution.'
author: José Bagur and Taddy Chung
tags: [Machine Learning]
---

Tiny Machine Learning (also referred to as TinyML) is a fast-growing field of Machine Learning (ML) technologies and applications. TinyML involves hardware suitable for onboard data collection and inference; it also involves algorithms and software capable of performing on-device data analytics at extremely low power (typically in the range of mW) and with very low latency. The GIGA R1 is one of the most feature-packed boards from Arduino up to date. In the GIGA R1, you can find the powerful STM32H747XI, a dual-core (M4 and M7) 32-bit Arm® Cortex® microcontroller from STMicroelectronics; this is the same microcontroller found in the Arduino Portenta H7 family boards. This guide will show you how to use the Arduino ecosystem to turn a versatile and powerful board like the GIGA R1 into a versatile, powerful, and professional TinyML tool.

## TinyML Frameworks

Several ML frameworks that support TinyML applications. Some of the most popular and used nowadays are the following:

- [TensorFlow Lite](https://www.tensorflow.org/lite)
- [Fraunhofer AIfES for Arduino®](https://www.ims.fraunhofer.de/en/Business-Unit/Industry/Industrial-AI/Artificial-Intelligence-for-Embedded-Systems-AIfES.html)
- [Edge Impulse](https://www.edgeimpulse.com/) 

This guide will show you how to use the frameworks mentioned above with the GIGA R1. Let's start with TensorFlow Lite!

## TensorFlow Lite and the GIGA R1

TensorFlow is a free, open-source software library for ML and Artificial Intelligence (AI) developed by the Google Brain team; it was first published in 2015. TensorFlow Lite was developed from the work made by the Google team, that at that time, was running neural networks that were only 14 kilobytes (KB) in size; those neural networks needed to be so small because they were running on the Digital Signal Processors (DSPs) present in most Android-based phones, those DSPs had only tens of KB of RAM and Flash memory.    
