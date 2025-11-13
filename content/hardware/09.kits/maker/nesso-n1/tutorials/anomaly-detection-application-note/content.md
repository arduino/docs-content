---
title: 'Motor Anomaly Detection with the Nesso N1'
description: "This application note describes how to implement a motor anomaly detection system using the Nesso N1 development kit, its built-in IMU sensor, and Edge Impulse."
difficulty: intermediate
compatible-products: [nesso-n1]
tags:
  - Motor monitoring
  - Anomaly detection
  - Classification
  - Application note
  - Machine learning
  - Edge Impulse
  - IMU
  - Nesso N1
  - LoRaWAN
  - Wi-Fi
author: 'José Bagur'
hardware:
  - hardware/09.kits/maker/nesso-n1
software:
  - ide-v2
  - edge-impulse
---

## Introduction

Motor condition monitoring is crucial in industrial settings, where unexpected equipment failures can lead to significant downtime and high maintenance costs. This application note demonstrates how to construct a motor anomaly detection system utilizing the Nesso N1 development kit, its onboard 6-axis Inertial Measurement Unit (IMU), and Edge Impulse.

![ ](assets/hero-banner.png)

The developed system monitors vibration patterns in real-time to identify unusual operating conditions that may signal mechanical problems, wear, or potential failures. The system utilizes machine learning to identify vibration patterns that deviate from regular motor operation, enabling predictive maintenance. The Nesso N1's multiple connectivity options (Wi-Fi 6, LoRaWAN, Thread, and Bluetooth 5.3) enable flexible deployment in various industrial environments, ranging from local monitoring to long-range remote sensing applications.

## Goals

This application note will help you to:

- Build a motor anomaly detection system that monitors vibration patterns in real-time using the Nesso N1's built-in 6-axis IMU sensor.
- Collect and analyze vibration data from motors to create baseline patterns and detect changes.
- Train a machine learning model using Edge Impulse to detect anomalies based on vibration data.
- Deploy the trained model directly to the Nesso N1 development kit for real-time anomaly detection without needing cloud connectivity.
- Set up visual and audio feedback through the kit's built-in RGB LED, touch display, and buzzer to show detected anomalies and system status.
- Leverage the Nesso N1's multiple connectivity protocols (Wi-Fi 6, LoRaWAN, Thread, Bluetooth 5.3) to transmit alerts and data to remote monitoring systems.
- Create industrial predictive maintenance solutions using cost-effective embedded intelligence in a compact, pre-assembled enclosure.

## Hardware and Software Requirements

### Hardware Requirements

- [Arduino Nesso N1 development kit](https://store.arduino.cc/products/nesso-n1) (x1)
- [USB-C® cable](https://store.arduino.cc/products/usb-cable2in1-type-c) (x1)
- Motor or rotating equipment for testing (for example, a small DC motor or fan) (x1)
- Power supply for the motor (if needed) (x1)
- Mounting accessories or adhesive tape to secure the Nesso N1 to the motor (x1 set)

### Software Requirements

- [Arduino IDE 2.0+](https://www.arduino.cc/en/software) or [Arduino Web Editor](https://create.arduino.cc/editor)
- [ESP32 Arduino Core](https://github.com/espressif/arduino-esp32) (needed for the Nesso N1 ESP32-C6 processor)
- [Edge Impulse account](https://studio.edgeimpulse.com/) (free tier available)
- [Edge Impulse CLI tools](https://docs.edgeimpulse.com/docs/cli-installation) for data collection

***The Nesso N1 development kit features a powerful ESP32-C6 processor with a single-core 32-bit RISC-V CPU running at up to 160 MHz, 16 MB NOR Flash memory and 512 KB SRAM for machine learning tasks. The onboard 6-axis IMU (BMI270) eliminates the need for external accelerometer connections. For complete hardware specifications, see the [Nesso N1 documentation](https://docs.arduino.cc/hardware/nesso-n1/).***

## Hardware Setup Overview

The electrical connections for the motor anomaly detection system are simplified with the Nesso N1 development kit, as all its essential components are integrated into a single, compact device.

![The motor anomaly detection system hardware setup with the Nesso N1](assets/hardware-setup-nesso.png)

This diagram shows the system components using the Nesso N1 development kit. **The Nesso N1 acts as an all-in-one solution**, combining the kit's microcontroller (ESP32-C6), onboard IMU (BMI270), wireless connectivity, display, and battery in a single enclosed unit. **The onboard 6-axis IMU collects vibration data** from the motor through direct physical coupling when the device is mounted on the motor housing.

The Nesso N1 operates from its built-in rechargeable lithium-polymer battery or can be powered via the USB-C connector with a +5 VDC supply. The compact form factor (18 mm x 45 mm) and integrated enclosure make it ideal for direct mounting on motor equipment without the need for additional protective housing.

***__Important note__: This power setup is for testing and demonstration purposes only. In real industrial environments, proper power system design should include electrical isolation, noise filtering, surge protection, and compliance with industrial safety standards for your specific application.***

### Physical Mounting Considerations

Proper mounting of the Nesso N1 is essential for effective vibration monitoring. The development kit must be securely attached to the motor housing or equipment using appropriate mechanical fasteners or industrial-grade adhesive. A good mechanical connection between the mounting surface and the device ensures accurate vibration transmission from the motor to the onboard IMU.

The Nesso N1's enclosed design provides basic protection against dust and minor vibrations, making it suitable for many industrial environments. However, additional protective measures may be needed in extreme conditions.

***For this application note, we will use a computer cooling fan to simulate motor operation and demonstrate the anomaly detection system. The Nesso N1 can be mounted directly on top of the fan using double-sided adhesive tape or a custom 3D-printed mounting bracket, providing a stable and consistent mounting solution for testing.***

## Understanding Motor Vibration Analysis

Motor vibrations contain valuable information about the mechanical condition of the equipment. Regular motor operation produces characteristic vibration patterns that stay relatively consistent during healthy operation. Abnormal conditions manifest as changes in vibration amplitude, frequency content, or timing patterns.

### Common Motor Faults

Common motor faults that can be detected through vibration analysis include:

- **Bearing wear**: Creates higher frequency components and increased vibration levels across all axes
- **Misalignment**: Produces specific frequency patterns related to rotational speed, typically appearing in radial directions
- **Imbalance**: Results in increased vibration at the main rotational frequency, primarily in radial directions
- **Looseness**: Causes widespread increases in vibration across multiple frequencies and directions
- **Electrical issues**: May create vibrations at twice the line frequency due to magnetic field changes

### The Role of the IMU in Vibration Monitoring

The Nesso N1's onboard BMI270 6-axis IMU combines a 3-axis accelerometer and 3-axis gyroscope, providing complete motion sensing capabilities for vibration analysis. The accelerometer measures linear acceleration along the X, Y, and Z axes, capturing the intensity and direction of vibrations. The gyroscope complements this by detecting rotational movements, which can indicate wobbling or angular vibrations in the motor.

The BMI270 offers several advantages for industrial vibration monitoring:

- High sensitivity and low noise for detecting subtle vibration changes
- Programmable measurement ranges (±2g to ±16g for accelerometer)
- High sampling rates up to 1.6 kHz for capturing fast vibration events
- Built-in digital filters to reduce noise and improve signal quality
- Low power consumption, extending battery life in the Nesso N1

This integrated sensor approach eliminates the need for external accelerometer wiring, ensuring consistent and reliable measurements. The digital I²C interface between the BMI270 and the ESP32-C6 microcontroller enables noise-immune data transmission, which is important to have in electrically noisy industrial environments.

### Data Collection Strategy

The Nesso N1 collects vibration data at regular intervals to build a complete picture of the motor's behavior. The system samples the IMU at 100 Hz, providing sufficient resolution to capture vibration patterns up to 50 Hz, as per the Nyquist theorem. This sampling rate covers most mechanical vibration frequencies found in typical motor applications.

Each data collection window consists of 200 samples (2 seconds of data), providing enough information for the machine learning model to identify patterns while keeping computational requirements manageable. The Nesso N1's 512 KB SRAM provides ample buffer space for storing multiple windows of vibration data during processing.

## Simple Vibration Monitor Example Sketch

Now that we have covered the hardware components and vibration analysis basics, let's look at the software that enables vibration data collection. Before implementing intelligent anomaly detection, we need to collect training data representing normal motor operation for Edge Impulse, a platform that simplifies embedded AI development.

Edge Impulse needs training data in a specific format to build effective anomaly detection models. Our data collection sketch formats the IMU readings so Edge Impulse can analyze normal operation patterns and create a model that identifies when new data differs from these patterns.

This section breaks down the example sketch and guides you through its functionality. We will explore how the IMU is initialized, how vibration data is collected at consistent intervals, and how the results are formatted for Edge Impulse data collection and model training.

The complete example sketch is shown below.

```arduino
/**
  Motor Vibration Data Collection for Edge Impulse
  Name: motor_vibration_collector.ino
  Purpose: This sketch reads 6-axis IMU data from the onboard BMI270 sensor
  of the Nesso N1 development kit. The data is formatted for Edge Impulse
  data collection and training, with real-time display visualization.
  
  @version 1.0 01/11/25
  @author Arduino Product Experience Team
*/

#include <Arduino_BMI270_BMM150.h>
#include <M5GFX.h>

// Display instance
M5GFX display;

// Sampling parameters
const int sampleRate = 100;                             // 100 Hz
const unsigned long sampleTime = 1000 / sampleRate;     // 10ms between samples

// Data collection variables
unsigned long lastSample = 0;

void setup() {
  // Initialize USB serial communication at 115200 baud
  Serial.begin(115200);
  for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));
  
  // Initialize display
  display.begin();
  display.setRotation(1); // Landscape mode
  display.setTextColor(TFT_WHITE, TFT_BLACK);
  display.fillScreen(TFT_BLACK);
  display.setTextSize(1.5);
  display.setTextDatum(MC_DATUM);
  display.drawString("- Initializing IMU...", display.width() / 2, display.height() / 2);
  
  // Initialize IMU
  if (!IMU.begin()) {
    Serial.println("- Failed to initialize BMI270 IMU!");
    display.fillScreen(TFT_BLACK);
    display.setTextColor(TFT_RED, TFT_BLACK);
    display.drawString("- IMU Failed!", display.width() / 2, display.height() / 2);
    while (1);
  }
  
  Serial.println("- Motor Vibration Data Collector (BMI270)");
  Serial.println("- 6-axis sensor initialized!");
  
  // Display sensor information
  Serial.print("- Accelerometer sample rate: ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println(" Hz");
  
  // Wait for sensor stabilization
  delay(500);
  
  // Test initial reading
  float testX, testY, testZ;
  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(testX, testY, testZ);
    
    Serial.print("- Initial readings (g): X=");
    Serial.print(testX, 3);
    Serial.print(", Y=");
    Serial.print(testY, 3);
    Serial.print(", Z=");
    Serial.println(testZ, 3);

    Serial.println("- Sensor ready (values already in g units)");
  }
  
  Serial.println("- Streaming continuous data for Edge Impulse!");
  Serial.println("- Data format: X_accel,Y_accel,Z_accel");
  
  // Setup display for live data
  display.fillScreen(TFT_BLACK);
  display.setTextSize(1.5);
  display.setTextDatum(TL_DATUM);
  display.drawString("- Motor Vibration Data:", 5, 5);
  display.drawString("- X:", 5, 30);
  display.drawString("- Y:", 5, 45);
  display.drawString("- Z:", 5, 60);
  display.drawString("g", 100, 30);
  display.drawString("g", 100, 45);
  display.drawString("g", 100, 60);
  
  delay(1000);
}

void loop() {
  unsigned long currentTime = millis();
  
  if (currentTime - lastSample >= sampleTime) {
    float xAccel, yAccel, zAccel;
    bool dataValid = false;
    
    // Read new acceleration data from the IMU
    if (IMU.accelerationAvailable()) {
      IMU.readAcceleration(xAccel, yAccel, zAccel);
      dataValid = true;
    }
    
    // Output CSV format for Edge Impulse
    if (dataValid) {
      Serial.print(xAccel, 4);
      Serial.print(",");
      Serial.print(yAccel, 4);
      Serial.print(",");
      Serial.println(zAccel, 4);
      
      // Update display with current values
      display.fillRect(45, 30, 50, 45, TFT_BLACK);
      display.setTextColor(TFT_GREEN, TFT_BLACK);
      display.setTextSize(1.5);
      display.setCursor(40, 30);
      display.printf("%+.3f", xAccel);
      display.setCursor(40, 45);
      display.printf("%+.3f", yAccel);
      display.setCursor(40, 60);
      display.printf("%+.3f", zAccel);
    }
    
    lastSample = currentTime;
  }
}
```

The following sections will help you understand the main components of the example sketch, which can be divided into the following areas:

- Sensor selection and initialization
- Hardware configuration and calibration
- Data collection timing and control
- Signal processing and conversion
- Edge Impulse data formatting

### Sensor Selection and Initialization

The sketch begins by including the necessary libraries for the Nesso N1's integrated components:
```arduino
#include <Arduino_BMI270_BMM150.h>
#include <M5GFX.h>

// Display instance
M5GFX display;
```

In this code:

- The `Arduino_BMI270_BMM150` library provides access to the onboard 6-axis IMU of the Nesso N1
- The `M5GFX` library controls the 1.14" touch display

### Hardware Configuration and Calibration

Before we can collect vibration data, we need to configure the Nesso N1 development kit to interface with its onboard BMI270 IMU.

**BMI270 Configuration**

For the Nesso N1, the configuration is simplified as the BMI270 is factory-calibrated and internally connected:

```arduino
// Initialize IMU
if (!IMU.begin()) {
  Serial.println("- Failed to initialize BMI270 IMU!");
  while (1);
}

Serial.println("- Motor Vibration Data Collector (BMI270)");
Serial.println("- 6-axis sensor initialized!");

// Display sensor information
Serial.print("- Accelerometer sample rate: ");
Serial.print(IMU.accelerationSampleRate());
Serial.println(" Hz");
```

In this code:

- The IMU is initialized with its default settings
- No pin assignments are needed as the IMU is internally connected via I²C

### Data Collection Timing and Control

To ensure accurate vibration analysis and successful machine learning training, we need consistent data collection timing. These parameters control how data is gathered:

```arduino
// Sampling parameters
const int sampleRate = 100;                             // 100 Hz
const unsigned long sampleTime = 1000 / sampleRate;     // 10 ms between samples
```

In this code:

- Sample rate of 100 Hz captures enough frequency response for detecting most motor faults
- Sample time calculation determines the precise timing needed between measurements

### Signal Processing and Conversion

Once we have the sensor readings, the BMI270 IMU provides pre-processed digital values ready for use.

**BMI270 Signal Processing**

For the onboard BMI270 IMU, the data is already processed and calibrated:

```arduino
// Read new acceleration data from the IMU
if (IMU.accelerationAvailable()) {
  IMU.readAcceleration(xAccel, yAccel, zAccel);
  dataValid = true;
}
```

In this code:

- `IMU.accelerationAvailable()` checks if new data is ready from the IMU
- The acceleration values are returned directly in **g** units

### Edge Impulse Data Formatting

The final step formats our acceleration data so it can be used with Edge Impulse data collection tools:

```arduino
// Output CSV format for Edge Impulse
if (dataValid) {
  Serial.print(xAccel, 4);
  Serial.print(",");
  Serial.print(yAccel, 4);
  Serial.print(",");
  Serial.println(zAccel, 4);
}
```

In this code:

- CSV format with four decimal places gives us the precision needed for machine learning training
- Single-line output per sample makes it easy to integrate with the Edge Impulse data forwarder
- Comma separation follows standard CSV format that most data processing tools expect
- The display provides real-time visual feedback of the acceleration values

After uploading the example sketch to the Nesso N1 development kit, you should see the following output in the Arduino IDE's Serial Monitor:

![Example sketch output showing vibration data collection on the Arduino IDE Serial Monitor](assets/example-sketch-output-1.png)

### Optional: Display Visualization

The Nesso N1's built-in 1.14" touch display provides real-time visual feedback during data collection, which is particularly useful for verifying proper sensor mounting and monitoring vibration levels without needing a serial connection.

**Display Setup**

The display initialization configures the screen orientation and text properties:

```arduino
// Initialize display
display.begin();
display.setRotation(1);                    // Landscape mode for better data layout
display.setTextColor(TFT_WHITE, TFT_BLACK);
display.fillScreen(TFT_BLACK);
display.setTextSize(1.5);                  // Readable size for the small screen
```

**Real-time Data Visualization**

The display updates with each new sensor reading, showing the acceleration values for all three axes:

```arduino
// Update display with current values
display.fillRect(45, 30, 50, 45, TFT_BLACK);  // Clear previous values only
display.setTextColor(TFT_GREEN, TFT_BLACK);
display.setTextSize(1.5);
display.setCursor(40, 30);
display.printf("%+.3f", xAccel);              // Format with sign and 3 decimals
display.setCursor(40, 45);
display.printf("%+.3f", yAccel);
display.setCursor(40, 60);
display.printf("%+.3f", zAccel);
```

In this code:

- The `fillRect()` function clears only the area where values are displayed, preserving the labels
- Green text color provides good contrast against the black background
- The `printf()` format ensures consistent display with sign (+/-) and three decimal places
- Values update at 100 Hz

This visual feedback helps during setup by:

- Confirming the IMU is responding to vibrations
- Verifying proper mounting (values should change when motor runs)
- Monitoring data quality without a computer connection
- Providing immediate indication of sensor saturation or disconnection

After uploading the example sketch to the Nesso N1 development kit, you should see the following output in the Nesso N1's built-in 1.14" touch display:

![Example sketch output showing vibration data collection on the Nesso N1's built-in touch display](assets/example-sketch-output-display-1.png)

### Complete Example Sketch

Download the complete data collection example sketch [here](assets/motor_vibration_collector.zip).

[![ ](assets/download-button.png)](assets/motor_vibration_collector.zip)

## Connecting the Vibration Monitor to Edge Impulse

As vibration-based condition monitoring becomes more important for predictive maintenance, connecting our data collection system to Edge Impulse enables the development of intelligent anomaly detection models. Edge Impulse provides a complete platform for embedded machine learning, allowing us to transform raw vibration data into useful insights about motor health.

In this section, we will connect the vibration monitor to Edge Impulse platform to collect training data, develop machine learning models and deploy intelligent anomaly detection directly to the Nesso N1 development kit. This connection transforms our simple vibration monitor into an intelligent system that can detect motor anomalies without needing cloud connectivity.

***If you are new to Edge Impulse, please check out [this tutorial](https://docs.edgeimpulse.com/docs/tutorials/end-to-end-tutorials/time-series/continuous-motion-recognition/) for an introduction to the platform.***

### Setting up Edge Impulse Account and Project

The first step involves creating an Edge Impulse account and setting up a new project for motor anomaly detection. These steps establish the foundation for machine learning model development:

**Create Account**: Register for a free Edge Impulse account at [studio.edgeimpulse.com](https://studio.edgeimpulse.com/)

**New Project**: Create a new project with the following settings:

- Enter a project name (for example, "`nesso-n1-anomaly-detection`")
- Choose project type: Personal (free tier with 60 min job limit, 4 GB data limit)
- Choose project setting: Private (recommended for this application)

![Creating a new project on Edge Impulse](assets/new-project.png)

**Project Configuration**: Once created, the project will be ready for data collection. Sampling frequency and window settings will be configured later during impulse design.

### Data Collection with Edge Impulse CLI

The Edge Impulse CLI provides tools for streaming data directly from the Nesso N1 to the Edge Impulse platform. This eliminates manual file transfers and enables efficient data collection.

#### Installing Edge Impulse CLI

Before you can collect data from the Nesso N1, you need to install the Edge Impulse CLI tools on your computer. The installation process varies depending on your operating system.

Prerequisites:

- [Node.js](https://nodejs.org/en) 14 or higher
- [Python 3](https://www.python.org/downloads/)

For detailed installation instructions specific to your operating system, follow the [official Edge Impulse CLI installation guide](https://docs.edgeimpulse.com/docs/tools/edge-impulse-cli/cli-installation).

Verify the installation with the following command:

```bash
edge-impulse-daemon --version
```

![Edge Impulse Daemon version](assets/daemon-version.png)

#### Setting up Data Forwarding

Now that you have the CLI installed, you can set up data forwarding to stream vibration data directly from your Nesso N1 to Edge Impulse.

Connect your Nesso N1 to your computer via USB-C cable and upload the data collection sketch. Then open a terminal and run the following command:

```bash
edge-impulse-data-forwarder
```

The tool will guide you through the setup process:

1. **Login**: Enter your Edge Impulse username/email and password when prompted
2. **Select Device**: Choose the correct serial port for your Nesso N1 development kit (for example, `COM10`)
3. **Data Detection**: The tool will automatically detect the data frequency (100 Hz) and number of sensor axes (3)
4. **Name Axes**: When asked "What do you want to call them?", enter: `X`,`Y`,`Z`
5. **Device Name**: Give your device a name (for example, `nesso-n1`)
6. **Project Connection**: If you have multiple projects, the tool will ask which Edge Impulse project you want to connect the device to. Select your motor anomaly detection project.

![Setting up the data forwarder tool](assets/data-forwarder-configuration.png)

Once configured, the forwarder will stream data from your Nesso N1 board to Edge Impulse. You can verify the device connection by checking the "Devices" tab in Edge Impulse Studio. You can then start collecting training data for your machine learning model.

![Device connection verification to Edge Impulse Studio](assets/device-verification.png)

#### Data Collection Process

With the data forwarder running, you can now collect training data for your anomaly detection model. For effective anomaly detection, you need high-quality data representing normal motor operation in different states.

Start by mounting the accelerometer securely to the motor housing. You will collect two types of normal operation data:

1. **Idle data collection**: With the motor turned off, **collect 10 to 15 minutes of "idle" operation** data through multiple two second windows. This captures the baseline vibration environment without motor operation. Label all data as `idle` in Edge Impulse Studio.

2. **Nominal data collection**: With the motor running under normal operating conditions, **collect 10 to 15 minutes of "nominal" operation** data through multiple two second windows. Vary motor load conditions slightly to capture different normal operating scenarios. Label all data as `nominal` in Edge Impulse Studio.

Edge Impulse can automatically split your collected data into **training (80%) and testing (20%) sets**. The 20 to 30 minutes total of data ensures you have enough samples for both training the model and validating its performance on unseen data.

![Data collection on Edge Impulse Studio](assets/data-collection.png)

After data collection, review the collected samples in Edge Impulse Studio for consistency. Check for proper amplitude ranges and no clipping, verify sample rate consistency and timing accuracy and remove any corrupted or unusual samples from the training set.

***__Important note__: The anomaly detection model learns what "normal" looks like from both idle and nominal data. Any future vibration patterns that significantly differ from these learned patterns will be flagged as anomalies. This approach allows the system to detect unknown fault conditions without needing examples of actual motor failures.***