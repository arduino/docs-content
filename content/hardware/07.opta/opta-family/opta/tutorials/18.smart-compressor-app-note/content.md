---
title: 'Compressor Remote Condition Monitoring with Opta'
difficulty: intermediate
description: "This application note describes how to transform your industrial compressor into smart using Opta micro PLC."
tags:
  - modbus
  - maintenance
  - industrial
  - machine learning
author: 'Christopher Méndez'
hardware:
  - hardware/07.opta/opta-family/opta
  - hardware/06.nicla/boards/nicla-sense-me
---

## Introduction

Transform your industrial compressor into smart and connect it to the Arduino Cloud for advanced condition monitoring capabilities using the Opta™ micro PLC.

![Project Thumbnail]()

This affordable solution provides real-time remote data access, behavioral diagnostics, predictive maintenance, and efficient device management. It helps you maximize uptime, reduce operational costs, and extend the lifespan of your equipment.

### Goals

The goal of this application note is to showcase the Opta PLC capabilities on letting you convert conventional industrial equipment into smart for monitoring and predictive maintenance purposes. The project's objectives are the following:

- Monitor key performance indicators like power consumption, temperature and pressure of the compressor.
- Integrate additional sensing points into your assets like vibration for motor and bearings status control. 
- Connect the compressor via Modbus TCP industry-standard protocol for optional integration to currently installed systems.
- Leverage Arduino Cloud's powerful analytics to gain actionable insights into the compressor performance.
- Create an Arduino Cloud dashboard that syncs in real time to inform and alert the user.

## Hardware and Software Requirements

![Hardware Image]()

### Hardware Requirements

- [Opta™ WiFi](https://store.arduino.cc/products/opta-wifi) (x1)
- [Nicla Sense ME](https://store.arduino.cc/products/nicla-sense-me) (x1)
- 24 VDC Power Supply (x1)
- AC Current Sensor 0-10 V (x1)
- PT100 2 Wires RTD (x1)
- RTD to 0-10 V converter (x1)
- Pressure transmitter 0-10 V (x1)
- Power Relay 24 V (x1)
- Wiring Cable 18AWG
- [USB Type-C® Cable](https://store.arduino.cc/products/usb-cable2in1-type-c) (x1)
- Micro-USB Cable (x1)

### Software Requirements

- [Arduino IDE 2](https://www.arduino.cc/en/software) or [Arduino Cloud Editor](https://create.arduino.cc/editor)
- The [Compressor Monitor sketches for Opta and Nicla Sense ME]()
- The [Arduino Create Agent](https://cloud.arduino.cc/download-agent/) to provision the Opta WiFi on the Arduino Cloud.
- The [Arduino Cloud](https://cloud.arduino.cc/)

## Compressor Monitoring System Setup

The electrical connections of the intended application are shown in the diagram below:

![Electrical connections of the monitoring system]()

The Opta PLC will be powered with an external 24 VDC power supply connected to it's screw terminals `+` and `-` respectively.

![Opta power supply connection]()

The current, temperature and pressure sensors will be connected to inputs `I1`, `I2` and `I3` respectively.

![Sensors connection]()

The power relay will be connected to the Opta relay output 1 as follows:

![Power relay connection]()

The compressor power source will be wired through the power relay and the current sensor.

![Compressor power wiring]()

## Compressor Monitoring System Overview
The monitoring system for the compressor integrates the sensor data gathering, power control and cloud communication using the Opta WiFi connection.

The Opta is responsible for reading the sensors and uploading their data to the Cloud, also for controlling the power state of the compressor and sharing through Modbus TCP all the sensor information.

The Nicla Sense ME leverage it's internal IMU for anomalous vibration detection on the compressor motor and connects through BLE with the Opta for vibration status sharing. 

![Compressor Monitoring System]()

### Sensors Deployment

- The **Current Sensor** alongside the grid voltage will help us measure the compressor power consumption for monitoring and overcurrent detection. It will be placed hooked in the compressor AC power line.
- The **Temperature Sensor** will measure the compressor electric motor temperature for monitoring and high temperature detection. It will be fixed to the compressor motor.
- The **Pressure Sensor** will measure the compressor air pressure for monitoring and high pressure detection. It will be screwed in the compressor tank pressure output.
- The **Nicla Sense ME** will detect anomalous vibrations. It will be fixed to the compressor motor and powered with a battery or external power source.

### Anomalies Detection

Every sensor will be used for anomalies detection, if any measured variable exceeds its nominal range an anomaly alert will show up in the Arduino Cloud dashboard.

The sensors nominal threshold are difined in the code as follows:

```arduino
#define CURRENT_LIMIT 12 // in Amps
#define PRESSURE_LIMIT 8 // in Bar
#define TEMP_LIMIT 85 // in Celsius
```

### Modbus TCP data output

The Opta will detect if an ethernet cable is connected to its included RJ45 terminal and will start sending the measured sensor data through Modbus TCP to a defined server address.

The variables will be sent to the registers in the following order:

| **Address** | **Sensor**  |
| :---------: | :---------: |
|    0x00     | Temperature |
|    0x01     |    Power    |
|    0x02     |  Pressure   |
|    0x03     |   Current   |

***As the Modbus Holding Registers are __uint16_t__ the data sent should be a positive integer between 0 and 65535, for this reason the data is sent multiplied by a 100 factor. This way a measured temperature of 42.5 C will be sent as 4250.***

### Opta Code

You can download the code for the Opta PLC [here]().

Let's go through some important code sections to make this application fully operative; starting with the required libraries:

- `ArduinoBLE.h` enables the support for Bluetooth® Low Energy (BLE) communication, install it by searching for it on the Library Manager.
- `Ethernet.h` enables the Ethernet support for the Modbus TCP communication.
- `ArduinoModbus.h` and `ArduinoRS485.h` manage the Modbus TCP protocol, install them by searching for them on the Library Manager.
- `ArduinoIoTCloud.h` enable the Arduino Cloud integration, install it by searching for it on the Library Manager.
- `Arduino_ConnectionHandler.h` manages the internet connectivity for the board, install it by searching for it on the Library Manager.

There is a header included in the project code for the Arduino Cloud configuration:

- `thingProperties.h` includes the WiFi credentials and Arduino Cloud configuration.

```arduino
#include "thingProperties.h"
#include <ArduinoBLE.h>

// For Modbus TCP
#include <Ethernet.h>
#include <ArduinoRS485.h>  // ArduinoModbus depends on the ArduinoRS485 library
#include <ArduinoModbus.h>

// Ethernet + Modbus objects
EthernetClient ethClient;
ModbusTCPClient modbusTCPClient(ethClient);

IPAddress server(10, 0, 0, 227);  // update with the IP Address of your Modbus server

#define DEBUG false

// Anomalies thresholds
#define CURRENT_LIMIT 12 // in Amps
#define PRESSURE_LIMIT 8 // in Bar
#define TEMP_LIMIT 85 // in Celsius

// Sensor inputs
#define C_SENSOR A0
#define T_SENSOR A1
#define P_SENSOR A2

#define GRID_V 120.0  // replace this value with the Grid AC voltage

float P_I3 = 0;  // variable to store pressure (Bar)
float T_I2 = 0;  // variable to store temperature (C)
float C_I1 = 0;  // variable to store current (A)

byte AlertValue = 0;  // last alert value received.

bool control_once = 1;  // flow control variable

unsigned long previousMillis = 0;  // will store last time readings were done
const long interval = 1000;  // interval at which to repeat readings
```

In the `setup()` function the different board peripherals are initiated including:

- Serial communication
- LEDs and relay outputs
- ADC configuration
- Arduino Cloud properties
### Nicla Sense ME Code

### Arduino Cloud Dashboard



## Full Compressor Monitoring System Example

## Conclusion

### Next Steps