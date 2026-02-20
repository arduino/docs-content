---
title: 'Transition to Practical Implementation (4/4)'
description: 'This module introduces the hardware and software we will use in Part 2 of the course, guides the setup of the development environment, and presents a reference project.'
tags:
  - Edge AI
  - Fundamentals
  - Machine Learning
  - Workflow
  - Data collection
  - Preprocessing
  - Model training
  - Evaluation
  - Implementation
author: 'José Bagur'
hardware:
  - hardware/02.hero/boards/uno-r4-wifi
---

In the previous modules, we explored the theoretical foundations of Edge AI: what it is, how machine learning algorithms operate on resource-constrained devices, and the workflow for creating applications. Now it is time to prepare for practical implementation.

This module introduces the hardware and software we will use in Part 2 of the course, guides the setup of the development environment, and presents a reference project that demonstrates all the concepts learned so far.

## Introduction to Hardware and Software

### Arduino Boards for Edge AI

Arduino offers several boards compatible with Edge AI applications. In this course, we will work with two options from the R4 family, which share the same microcontroller and are compatible with the projects we will develop.

#### Arduino Nano R4

The Arduino Nano R4 is a compact board designed for projects where size matters. Its main features include a 32-bit Renesas RA4M1 microcontroller running at 48 MHz, 256 KB of Flash memory for storing programs and ML models, 32 KB of SRAM for inference, and a small form factor ideal for integration into prototypes and final products.

The board includes a Qwiic connector that allows connecting compatible sensors without soldering or loose wires, simplifying prototyping.

#### Arduino UNO R4 WiFi

The Arduino UNO R4 WiFi shares the same microcontroller as the Nano R4 but adds wireless connectivity and additional features. In addition to the Nano R4 specifications, it includes an integrated Wi-Fi and Bluetooth module (ESP32-S3), a 12×8 LED matrix for visualization, and a form factor compatible with traditional Arduino UNO shields.

Wi-Fi connectivity enables sending data to the cloud or receiving model updates remotely. However, for the Edge AI applications we will develop, inference runs entirely on the device without requiring an internet connection.

#### Which One to Choose?

Both boards are compatible with this course's projects. The choice depends on specific needs:

|     **Criterion**    |     **Nano R4**     |      **UNO R4 WiFi**     |
|:--------------------:|:-------------------:|:------------------------:|
|     Project size     | Compact, integrable | Prototyping with shields |
|     Connectivity     |       USB only      |  USB + Wi-Fi + Bluetooth |
|     Visualization    |      Status LED     |      12×8 LED matrix     |
| Shield compatibility |          No         |            Yes           |
|         Price        |        Lower        |          Higher          |

For detailed information about technical specifications, consult the official documentation:

- [Arduino Nano R4 Documentation](https://docs.arduino.cc/hardware/nano-r4/)
- [Arduino UNO R4 WiFi Documentation](https://docs.arduino.cc/hardware/uno-r4-wifi/)

### Sensors for Edge AI

Edge AI applications require sensors to capture data from the real world. The most common sensor types in Arduino projects include:

#### Motion Sensors (IMU)

Motion sensors combine accelerometers and gyroscopes to measure linear acceleration and angular velocity. They are fundamental for applications such as gesture recognition, activity detection, and vibration monitoring.

Options compatible with R4 boards:

- **[Modulino Movement](https://docs.arduino.cc/hardware/modulino-movement/)**: IMU sensor that connects via the Qwiic connector, offering simple integration without manual wiring. It includes a 6-axis accelerometer and gyroscope.
- **ADXL335**: 3-axis analog accelerometer that connects to the board’s analog pins. It is an economical option for vibration detection projects.

#### Audio Sensors

Microphones capture audio signals for applications such as voice command recognition and environmental sound classification.

- **MEMS Microphone**s: Options such as the SPH0645 or INMP441 offer good audio quality for voice recognition.

#### Image Sensors

Cameras enable the implementation of computer vision applications such as object classification and person detection.

- **OV7670**: Economical camera module compatible with Arduino, suitable for simple image classification applications.

#### Environmental Sensors

These measure variables such as temperature, humidity, and air quality for monitoring and prediction applications.

- **[Modulino Thermo](https://docs.arduino.cc/hardware/modulino-thermo/)**: Temperature sensor with Qwiic connection.
- **BME280**: Combined sensor for temperature, humidity, and atmospheric pressure.

### The Edge Impulse Platform

Edge Impulse is a development platform that simplifies creating machine learning applications for embedded devices. It will be our main tool in the practical part of the course [1].

#### Why Edge Impulse?

The platform offers several advantages for developers getting started with Edge AI:

- **Visual interface**: The entire workflow, from data collection to deployment, is managed through an intuitive web interface.
- **Arduino integration**: Arduino boards connect directly to the platform to collect data and download optimized models.
- **Automatic optimization**: The platform automatically quantizes and optimizes models for the selected hardware.
- **Free tier:** The free plan is sufficient for educational projects and prototypes.

#### Workflow in Edge Impulse

Project development in Edge Impulse follows these steps:

1. **Create a project**: Each project groups the data, model, and configuration for a specific application.
2. **Collect data**: Capture samples directly from the Arduino device or upload existing data.
3. **Design the impulse**: Configure the processing pipeline by selecting preprocessing blocks and the model type.
4. **Train the model**: The platform trains the model in the cloud and displays performance metrics.
5. **Test the model**: Evaluate it on test data before deployment.
6. **Deploy**: Download the model as an Arduino library ready to integrate into the project.

## Environment Setup

Before starting with practical projects, you need to set up the development environment. This section provides an overview of the process and links to official documentation for detailed steps.

### Step 1: Install Arduino IDE

The Arduino IDE is the development environment where we will write and upload code to Arduino boards.

1. Download the Arduino IDE 2.0 or higher from [arduino.cc/en/software](https://www.arduino.cc/en/software)
2. Install the software following the instructions for your operating system
3. Open the Arduino IDE and verify that it starts correctly

For detailed installation instructions, visit the [official Arduino IDE installation guide](https://docs.arduino.cc/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing/).

### Step 2: Install R4 Board Support

The Arduino UNO R4 WiFi board require the Arduino Renesas support package.

1. In Arduino IDE, go to **Tools > Board > Boards Manager**
2. Search for "Arduino UNO R4" or "Arduino Renesas"
3. Install the **Arduino UNO R4 Boards** package
4. Once installed, select your board in **Tools > Board > Arduino UNO R4 Boards**

For detailed instructions, visit:

- [Nano R4 Getting Started Guide](https://docs.arduino.cc/hardware/nano-r4/)
- [UNO R4 WiFi Getting Started Guide](https://docs.arduino.cc/hardware/uno-r4-wifi/)

### Step 3: Create an Edge Impulse Account

Edge Impulse requires an account to access the development platform.

1. Visit [studio.edgeimpulse.com](https://studio.edgeimpulse.com/)
2. Create a free account using your email or a Google/GitHub account
3. Verify your email if necessary
4. Log in and familiarize yourself with the dashboard

The official Edge Impulse documentation provides detailed guides for all aspects of the platform at [docs.edgeimpulse.com](https://docs.edgeimpulse.com/).

### Step 4: Install Edge Impulse CLI (Optional)

The Edge Impulse command-line interface (CLI) facilitates data collection directly from the device. Although optional, it is recommended for a smoother experience.

1. Install Node.js from [nodejs.org](https://nodejs.org/) (LTS version recommended)
2. Open a terminal and run: `npm install -g edge-impulse-cli`
3. Verify the installation by running: `edge-impulse-daemon --version`

For detailed instructions according to your operating system, visit the [Edge Impulse CLI installation guide](https://docs.edgeimpulse.com/docs/tools/edge-impulse-cli/cli-installation).

### Step 5: Connect the Board to Edge Impulse

Once the CLI is installed, you can connect your Arduino board to Edge Impulse to collect data.

1. Connect the Arduino board to your computer via the USB-C cable
2. Open a terminal and run: `edge-impulse-daemon`
3. Follow the on-screen instructions to log in and select your project
4. The board will appear as a connected device in the Edge Impulse dashboard

For specific instructions on connecting Arduino boards, visit the [Edge Impulse compatible devices documentation](https://docs.edgeimpulse.com/docs/edge-ai-hardware/mcu/arduino).

## Guided Activity: Reference Project

To illustrate how all the concepts learned in previous modules integrate, we will explore a complete Edge AI project: a motor anomaly detection system.

### Project Description

The "Motor Anomaly Detection" project demonstrates how to build a predictive maintenance system that monitors motor vibrations in real time to detect abnormal operating conditions [2].

The system uses:

- **Hardware:** Arduino UNO R4 WiFi with an accelerometer (ADXL335 or Modulino Movement)
- **Software:** Edge Impulse to train the anomaly detection model
- **ML Technique:** Anomaly detection using K-means clustering (unsupervised learning)

### Relationship with Course Concepts

This project demonstrates the concepts we have studied in practice:

|        **Course Concept**       |           **Implementation in the Project**          |
|:-------------------------------:|:----------------------------------------------------:|
|     Data types (Module 1.3)     |          Motion sensor data (accelerometer)          |
|    Preprocessing (Module 1.3)   |  Frequency feature extraction with Spectral Analysis |
|  Anomaly detection (Module 1.2) |     K-means model trained only with "normal" data    |
|    Optimization (Module 1.2)    | Automatic quantization for microcontroller execution |
| Evaluation metrics (Module 1.3) |            Configurable anomaly threshold            |
|     Deployment (Module 1.2)     |       Real-time inference with latency < 20 ms       |

### Project Workflow

The project development follows the Edge AI workflow we studied in Module 1.3:

1. **Problem definition:** Detect abnormal vibrations that could indicate mechanical failures
2. **Data collection:** Capture vibration data during normal motor operation
3. **Preprocessing:** Extract frequency features from accelerometer signals
4. **Training:** Train an anomaly detection model with normal data
5. **Evaluation:** Verify that the model detects simulated abnormal conditions
6. **Deployment:** Load the model onto the Arduino board for real-time monitoring

### Access to the Complete Project

The complete application note includes step-by-step instructions for:

- Setting up the hardware (accelerometer connections)
- Collecting vibration data with Edge Impulse
- Training the anomaly detection model
- Deploying the model to the Arduino board
- Interpreting results and configuring alerts

**Access the complete application note:** [Motor Anomaly Detection with the Arduino R4 WiFi](link-to-application-note)

In Part 2 of the course, we will work with this project and similar ones, applying step by step everything learned in Part 1.

## Concept Review and Preparation for Part 2

### Part 1 Summary

Throughout the four modules of Part 1, we have built a solid foundation of Edge AI knowledge:

**Module 1.1 - Edge AI Fundamentals:** We explored what Edge AI is, its differences from cloud processing, and the advantages of running machine learning models directly on embedded devices.

**Module 1.2 - ML Fundamentals for Edge Devices:** We studied algorithm types suitable for Edge AI, optimization techniques such as quantization and pruning, and tools in the TinyML ecosystem.

**Module 1.3 - Workflow for Creating Applications:** We delved into the four central development phases: data collection, preprocessing, training, and evaluation.

**Module 1.4 - Transition to Practical Implementation:** We introduced the hardware and software we will use, set up the development environment, and explored a reference project.

### What to Expect in Part 2

Part 2 of the course focuses on practical implementation. Throughout 10 hours of guided work, we will develop complete Edge AI projects:

- **Practical projects:** We will implement real applications such as gesture recognition, sound classification, and anomaly detection.
- **Step-by-step work:** Each project will be developed following the complete workflow, from data collection to deployment.
- **Troubleshooting:** We will learn to diagnose and solve common problems in Edge AI projects.
- **Customization:** We will explore how to adapt projects to specific needs.

### Preparation for Part 2

Before continuing with Part 2, make sure to:

1. **Have the hardware ready:** An Arduino UNO R4 WiFi board with a USB-C cable
2. **Set up the environment:** Arduino IDE installed with R4 board support
3. **Create your account:** An active Edge Impulse account
4. **Review the reference project:** Familiarize yourself with the structure of the anomaly detection application note

If you have questions about any of the theoretical concepts, this is a good time to review the previous modules before moving on to practical implementation.

## References

[1] Edge Impulse, "Edge Impulse Documentation," 2024. [Online]. Available: https://docs.edgeimpulse.com/

[2] Arduino, "Motor Anomaly Detection with the Arduino R4," Application Note, 2025. [Online]. Available: https://docs.arduino.cc/