---
title: 'Portenta Machine Control Arduino Library Guide'
difficulty: beginner
compatible-products: [portenta-machine-control]
description: 'Learn about the library of the Arduino® Portenta Machine Control.'
tags:
  - Library
  - Portenta Machine Control
author: 'José Bagur'
hardware:
  - hardware/05.pro-solutions/solutions-and-kits/portenta-machine-control
software:
  - ide-v1
  - ide-v2
  - arduino-cli
  - web-editor 
---

## Overview

The Arduino Portenta Machine Control is a versatile industrial unit for driving machinery. It offers soft-PLC control, diverse I/O options, and flexible network connectivity. The Machine Control library enables efficient management of the features of the Portenta Machine Control board. This tutorial aims to highlight the recent changes in the library, focusing on its user-friendly approach and adherence to the Arduino style.

## Goals

- Introduce the library’s key features and capabilities.
- Show the library's main differences between its first and latest version. 

## Hardware and Software Requirements

### Hardware Requirements

- [Portenta Machine Control](https://store.arduino.cc/products/arduino-portenta-machine-control) (x1)
- [USB-A to Micro-USB cable](https://store.arduino.cc/products/usb-2-0-cable-type-a-micro) (x1)
- +24 VDC power supply (x1)

### Software Requirements

- [Arduino IDE 2.0+](https://www.arduino.cc/en/software) or [Arduino Web Editor](https://create.arduino.cc/editor)
- [Arduino_MachineControl library](https://github.com/leonardocavagnis/Arduino_MachineControl/tree/lib_refactoring)

## Portenta Machine Control Arduino Library

The Portenta Machine Control Library is a C++ library designed to efficiently manage the functionalities of the Portenta Machine Control board. It provides extensive support for inputs such as digital, analog, and encoder signals, while offering outputs including digital and analog signals. This library also manages communication through protocols like CAN-BUS and serial ports, and allows connectivity via Ethernet, USB, Wi-Fi, and Bluetooth Low Energy.

The library empowers users to easily initialize, control, and access the diverse functionalities of the Portenta Machine Control, enhancing its capability and adaptability for industrial applications.

### Library Features

The library manages input signals, including:

- 8 digital inputs at 24 VDC
- 2 channels for encoder readings
- 3 analog inputs for PT100/J/K temperature probes
- 3 analog inputs for 4-20mA/0-10V/NTC signals

The library manages output signals, including:

- 8 digital outputs at 24 VDC
- 4 analog outputs at 0-10 VDC

Provides control for other I/O:

- 12 programmable digital I/O at 24V

Supports various communication protocols:

- CAN-BUS
- Serial protocols (RS232/RS422/RS485)
- USB
- Handles RTC (Real-Time Clock) functionality

### Improvements Between Releases

#### Structural and Functional Enhancements

The library has undergone significant structural changes to improve its efficiency and user-friendliness. Key improvements include:

- Library Structure Revamping: Transition from a single header file to multiple .cpp and .h files organized by functionality.
- Naming Refactoring: Removal of the machinecontrol namespace, adopting a more descriptive prefix-based naming system.
- Function Optimization: Unused functions have been removed, streamlining the library.
- Direct Calls to mbed Core Removed: This change enhances the library's compatibility and ease of use.
- Example Reworking: Updated examples provide clearer demonstrations of the library's capabilities.
- Documentation Improvement: Enhanced documentation offers better support to users.

#### Practical Application Enhancements

- Input/Output Management: Enhanced handling of digital and analog signals for improved accuracy and reliability.
- Communication Protocol Integration: Improved support for CAN-BUS and serial protocols, facilitating smoother data exchange.
- Real-Time Clock (RTC) Functionality: More robust RTC management, ensuring precise timekeeping for time-sensitive applications.

These improvements make the Portenta Machine Control Library more adaptable and efficient for a wide range of industrial applications, from machinery control to sensor integration.

## Naming Conventions

One of the significant updates in the Portenta Machine Control Library is the change in naming conventions, which enhances clarity and consistency across the library.

Changes in Naming:

- Removal of machinecontrol Namespace: The previous version of the library used the machinecontrol namespace. This has been removed to simplify the code and make it more accessible.
- Introduction of MachineControl_ Prefix: In the updated library, a prefix MachineControl_ is used for each functionality's singleton object. This change ensures a clearer and more descriptive approach to accessing library functionalities.

Examples of Updated Naming:

Old Naming Convention:

```arduino
// Using the 'machinecontrol' namespace
using namespace machinecontrol;
void setup() {
    digital_inputs.init();
}
```

New Naming Convention:

```arduino
// Prefix 'MachineControl_' used for each functionality
void setup() {
    MachineControl_DigitalInputs.begin();
}
```

This new naming structure aligns with the Arduino standard of using clear and descriptive names, making the library more user-friendly, especially for those new to programming with Arduino.

## I/O Modules 

In the latest version of the Portenta Machine Control Library, interacting with input/output (I/O) modules has been streamlined for better usability and consistency with Arduino standards.

Initializing I/O Modules:

In the updated library, initializing an I/O module is more intuitive. The begin() function is now used to start a module, providing a clear starting point for module operations.

CamelCase Notation:

The library has adopted CamelCase notation for function names, aligning with the standard Arduino library style. This change makes the library more consistent with other Arduino libraries, enhancing readability and ease of use.

Examples of I/O Module Usage:

Old Approach:

```arduino
// Using the previous library version
#include <Arduino_MachineControl.h>
using namespace machinecontrol;
void setup() {
    analog_out.period_ms(0, 4);
}
```

New Approach:

```arduino
// Using the updated library
#include <Arduino_MachineControl.h>
void setup() {
    MachineControl_AnalogOut.begin();
    MachineControl_AnalogOut.setPeriod(0, 4);
}
```

In the new approach:

The begin() function is explicitly called to initialize the MachineControl_AnalogOut module. The setPeriod() method, following the CamelCase notation, replaces the older period_ms() function, making the function's purpose clearer and the code more consistent with Arduino standards. This update enhances the user experience by making the code more intuitive and aligned with the familiar Arduino programming style.

## Encoders

The handling of encoders has been updated in the latest version of the Portenta Machine Control Library for a more streamlined and intuitive approach.

Removing Array Object Access:

In the previous library version, encoder objects were accessed using array notation ([]). This approach has been simplified in the new version, enhancing code readability and reducing potential for errors.

Example of Encoder Usage:

Old Approach:

```arduino
// Using the previous library version
#include <Arduino_MachineControl.h>
using namespace machinecontrol;
int rev;
void setup() {
    rev = encoders[0].getRevolutions();
}
```

New Approach:

```arduino 
// Using the updated library
#include <Arduino_MachineControl.h>
int rev;
void setup() {
    rev = MachineControl_Encoders.getRevolutions(0);
}
```

In the new approach:

- The getRevolutions() function is called directly on the MachineControl_Encoders object, rather than accessing an encoder array.
- The encoder of interest is specified as a parameter in the function call, making the code more explicit and easier to understand.

This update to the encoder module in the Portenta Machine Control Library simplifies the interaction with encoders, making it more straightforward for users to implement in their projects.

## Communication

The latest update to the Portenta Machine Control Library has refined the way communication is managed, particularly in the context of RS485 communication and similar protocols.

Removal of Public Object Usage:

The updated library version moves away from using public objects for communication protocols. This change leads to a more encapsulated and modular approach, enhancing the robustness and clarity of the communication code.

Example of Communication Protocol Usage:

Old Approach:

```arduino
// Using the previous library version
#include "Arduino_MachineControl.h"
using namespace machinecontrol;
void setup() {
    comm_protocols.init();
    comm_protocols.rs485.begin(115200, 0, 500);
    comm_protocols.rs485.receive();
}
```

New Approach:

```arduino
// Using the updated library
#include "Arduino_MachineControl.h"
void setup() {
    MachineControl_RS485Comm.begin(115200, 0, 500);
    MachineControl_RS485Comm.receive();
}
```

In the new approach:

- Communication initialization and data reception are handled directly through the MachineControl_RS485Comm object.
- This design eliminates the need for initializing a separate communication protocol object (comm_protocols) and then accessing its members, making the code more straightforward and easier to maintain.

These improvements in the communication module of the Portenta Machine Control Library are part of the effort to make the library more user-friendly and aligned with best practices in software design.

## Temperature Sensors

The Portenta Machine Control Library's latest update has restructured the handling of temperature sensors, dividing the functionalities into two distinct classes for improved clarity and usability.

Separation into Two Classes:

The temperature sensing functionalities are now divided into two separate classes:

1. Temperature RTD: Specifically for Resistance Temperature Detectors (RTD).
2- Temperature TC: Dedicated to Thermocouple (TC) temperature sensors.

This separation ensures a more organized and intuitive approach to temperature sensing, allowing users to work more efficiently with the specific type of sensor they are using.

Example of Temperature Sensor Usage:

Old Approach:

```arduino
// Using the previous library version
#include <Arduino_MachineControl.h>
using namespace machinecontrol;
void setup() {
    temp_probes.tc.begin();
    temp_probes.enableTC();
}
```

New Approach:

```arduino
// Using the updated library
#include <Arduino_MachineControl.h>
void setup() {
    MachineControl_TCTempProbe.begin();
}
```

In the new approach:

- The initialization of the thermocouple temperature probe is done directly through the MachineControl_TCTempProbe object.
- This design removes the need for accessing a general temperature probe object (temp_probes) and then its specific member for thermocouples, streamlining the code and making it more straightforward.

These enhancements in managing temperature sensors within the Portenta Machine Control Library simplify the process of integrating and utilizing temperature sensors in industrial applications.