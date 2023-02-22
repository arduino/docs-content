---
title: 'Getting Started with Modbus RTU on Opta™'
description: "Learn how to use the Modbus RTU serial protocol on Opta™."
difficulty: intermediate
tags:
  - Getting started
  - Modbus RTU
  - RS-485
author: 'José Bagur and Taddy Chung'
libraries:
  - name: ArduinoRS485
    url: https://www.arduino.cc/reference/en/libraries/arduinors485/
  - name: ArduinoModbus
    url: https://www.arduino.cc/reference/en/libraries/arduinomodbus/
software:
  - ide-v1
  - ide-v2
  - arduino-cli
  - web-editor
hardware:
  - hardware/05.pro-solutions/solutions-and-kits/opta
---

## Overview

Modbus is an open serial protocol derived from the client/server architecture initially developed and published by Modicon (now Schneider Electric) to be used with programmable logic controllers (PLCs). Since 1979, Modbus has become a standard communications protocol in industrial electronic devices.

The **Opta™**, with its industrial hardware and software capabilities, and the Arduino ecosystem tools such as the Arduino IDE and its libraries, has been designed with the Modbus communication protocol in mind, being really easy to create a new Modbus communication line using Opta™. In this tutorial, we will learn how to implement Modbus RTU communications protocol over RS-485 between two Opta™ devices.

## Goals

- Learn how to create a RS-485 interface connection between two Opta™ devices
- Learn how to use the Modbus RTU communication protocol between two Opta™ devices

### Required Hardware and Software

### Hardware Requirements

- Opta™ PLC with RS-485 support (x2)
- 12VDC/1A DIN rail power supply (x1)
- USB-C® cable (x1)
- Wires similar to the following specs  (x3): 
- - STP/UTP 24-18AWG (Unterminated)/22-16AWG (Terminated)
- - 100-130Ω rated for RS-485 connection

### Software Requirements

- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2.0+](https://www.arduino.cc/en/software), or [Arduino Web Editor](https://create.arduino.cc/editor)
- If you choose an offline Arduino IDE, you must install the following libraries: `ArduinoRS485`, and `ArduinoModbus`. You can install these libraries via the Library Manager of the Arduino IDE.

## Modbus Protocol

Modbus is an open and royalty-free serial communication protocol widely used in industrial electronic devices, especially in Building Management Systems (BMS) and Industrial Automation Systems (IAS). It was published in 1979 (more than 40 years ago) and has become a _de facto_ standard communication protocol among industrial electronic devices.

***Modbus communication protocol is often used to connect a supervisory device with a Remote Terminal Unit (RTU) in Supervisory Control and Data Acquisition (SCADA) Systems.***

Reliability in communications between electronic devices is ensured with Modbus by using messages with a simple 16-bit structure with a Cyclic-Redundant Checksum (CRC).

***If you want more insights on the Modbus communication protocol, take a look at [Modbus article](https://docs.arduino.cc/learn/communication/modbus) complying as well with Opta™.***

## Instructions

### Setting Up the Arduino IDE

If you haven't already, head over [here](https://www.arduino.cc/en/software) and install the most recent version of the Arduino IDE along with the necessary device drivers for your computer. For additional details on Opta™, check our [getting started tutorial](/tutorials/opta/getting-started). Make sure you install the latest version of the [`ArduinoModbus`](https://www.arduino.cc/reference/en/libraries/arduinomodbus/) library because it will be used to implement the Modbus RTU communication protocol.

***`ArduinoModbus` library is dependent of the `ArduinoRS485` library; remember to install both libraries.***

### Connecting the Opta™ Over RS-485

Refer to the following diagram for connecting two Opta™ devices via RS-485 interface.

![Connecting two Opta™ devices via RS-485](assets/opta-modbus-connection.svg)

### Code Overview

The goal of the following example is to configure and use the Modbus RTU communication protocol over the RS-485 interface between two Opta™ devices.

In the Client-Server protocol known as Modbus, the requesting device is known as the Modbus Client, and the device that will provide the requested information is known as the Modbus Server. While several Modbus Servers are allowed, only one Modbus Client is authorized. In this example, an Opta™ Client is in charge of writing and reading `Coil`, `Holding`, `Discrete Input`, and `Input` register values, while an Opta™ Server will poll for Modbus RTU requests and return the appropriate values.

The crucial components of the code used in this tutorial are discussed in detail to make the example easier to read.

#### Modbus RTU Client

The Opta™ Client will require the following setup:

```arduino
#include <ArduinoModbus.h>
#include <ArduinoRS485.h> // ArduinoModbus depends on the ArduinoRS485 library

constexpr auto baudrate { 19200 };

// Calculate preDelay and postDelay in microseconds as per Modbus RTU Specification
//
// MODBUS over serial line specification and implementation guide V1.02
// Paragraph 2.5.1.1 MODBUS Message RTU Framing
// https://modbus.org/docs/Modbus_over_serial_line_V1_02.pdf
constexpr auto bitduration { 1.f / baudrate };
constexpr auto preDelayBR { bitduration * 9.6f * 3.5f * 1e6 };
constexpr auto postDelayBR { bitduration * 9.6f * 3.5f * 1e6 };
// constexpr auto preDelayBR { bitduration * 10.0f * 3.5f * 1e6 };

int counter = 0;

void setup() {
    Serial.begin(9600);
    while (!Serial);

    Serial.println("Modbus RTU Client");

    RS485.setDelays(preDelayBR, postDelayBR);

    // start the Modbus RTU client
    if (!ModbusRTUClient.begin(baudrate, SERIAL_8E1)) {
        Serial.println("Failed to start Modbus RTU Client!");
        while (1);
    }
}
```

The `preDelay` and `postDelay` parameters are configured for a proper operation per Modbus RTU specification. The method `RS485.setDelays(preDelayBR, postDelayBR)` is then called to correctly set and use Modbus RTU over RS-485 interface on Opta™. In this example, such parameters are applied based on the message RTU framing specifications explained in depth in this [guide](https://modbus.org/docs/Modbus_over_serial_line_V1_02.pdf).

The typical baud rate are usually `9600` and `19200`; in the current example, we are using a baud rate of `19200`, but it can be changed depending on the system requirements. For the serial port parameter, `SERIAL_8E1` is defined for setting 8 data bits, even parity, and one stop bit.

The Modbus Server can be a module or a sensor with registers that can be accessed using specified addresses to obtain the monitored information or measurements. Inside the loop function of the sketch for the Client device, there are several tasks in charge of reading and writing specific values to access these types of data. Such data are `Coil`, `Holding`, `Discrete Input`, and `Input` register values.

```arduino
void loop() {
    writeCoilValues();

    readCoilValues();

    readDiscreteInputValues();

    writeHoldingRegisterValues();

    readHoldingRegisterValues();

    readInputRegisterValues();

    counter++;

    delay(5000);
    Serial.println();
}
```

The complete code for the Client is shown below:

```arduino
/**
  Getting Started with Modbus RTU on Opta™
  Name: Opta_Client
  Purpose: Writes Coil and Holding Register values; Reads Coil, Discrete Input, Holding Registers, and Input Register values.

  @author Arduino
*/

#include <ArduinoModbus.h>
#include <ArduinoRS485.h> // ArduinoModbus depends on the ArduinoRS485 library

constexpr auto baudrate { 19200 };

// Calculate preDelay and postDelay in microseconds as per Modbus RTU Specification
//
// MODBUS over serial line specification and implementation guide V1.02
// Paragraph 2.5.1.1 MODBUS Message RTU Framing
// https://modbus.org/docs/Modbus_over_serial_line_V1_02.pdf
constexpr auto bitduration { 1.f / baudrate };
constexpr auto preDelayBR { bitduration * 9.6f * 3.5f * 1e6 };
constexpr auto postDelayBR { bitduration * 9.6f * 3.5f * 1e6 };
// constexpr auto preDelayBR { bitduration * 10.0f * 3.5f * 1e6 };

int counter = 0;

void setup() {
    Serial.begin(9600);
    while (!Serial);

    Serial.println("Modbus RTU Client");

    RS485.setDelays(preDelayBR, postDelayBR);

    // start the Modbus RTU client
    if (!ModbusRTUClient.begin(baudrate, SERIAL_8E1)) {
        Serial.println("Failed to start Modbus RTU Client!");
        while (1);
    }
}

void loop() {
    writeCoilValues();

    readCoilValues();

    readDiscreteInputValues();

    writeHoldingRegisterValues();

    readHoldingRegisterValues();

    readInputRegisterValues();

    counter++;

    delay(5000);
    Serial.println();
}

/**
  Writes Coil values to the server under specified address.
*/
void writeCoilValues() {
    // set the coils to 1 when counter is odd
    byte coilValue = ((counter % 2) == 0) ? 0x00 : 0x01;

    Serial.print("Writing Coil values ... ");

    // write 10 Coil values to (server) id 42, address 0x00

    ModbusRTUClient.beginTransmission(42, COILS, 0x00, 10);
    for (int i = 0; i < 10; i++) {
        ModbusRTUClient.write(coilValue);
    }
    if (!ModbusRTUClient.endTransmission()) {
        Serial.print("failed! ");
        Serial.println(ModbusRTUClient.lastError());
    } else {
        Serial.println("success");
    }

    // Alternatively, to write a single Coil value use:
    // ModbusRTUClient.coilWrite(...)
}

/**
  Reads Coil values from the server under specified address.
*/
void readCoilValues() {
    Serial.print("Reading Coil values ... ");

    // read 10 Coil values from (server) id 42, address 0x00

    if (!ModbusRTUClient.requestFrom(42, COILS, 0x00, 10)) {
        Serial.print("failed! ");
        Serial.println(ModbusRTUClient.lastError());
    } else {
        Serial.println("success");

        while (ModbusRTUClient.available()) {
            Serial.print(ModbusRTUClient.read());
            Serial.print(' ');
        }
        Serial.println();
    }

    // Alternatively, to read a single Coil value use:
    // ModbusRTUClient.coilRead(...)
}

/**
  Reads Discrete Input values from the server under specified address.
*/
void readDiscreteInputValues() {
    Serial.print("Reading Discrete Input values ... ");

    // read 10 Discrete Input values from (server) id 42, address 0x00

    if (!ModbusRTUClient.requestFrom(42, DISCRETE_INPUTS, 0x00, 10)) {
        Serial.print("failed! ");
        Serial.println(ModbusRTUClient.lastError());
    } else {
        Serial.println("success");

        while (ModbusRTUClient.available()) {
            Serial.print(ModbusRTUClient.read());
            Serial.print(' ');
        }
        Serial.println();
    }

    // Alternatively, to read a single Discrete Input value use:
    // ModbusRTUClient.discreteInputRead(...)
}

/**
  Writes Holding Register values to the server under specified address.
*/
void writeHoldingRegisterValues() {
    // set the Holding Register values to counter

    Serial.print("Writing Holding Registers values ... ");

    // write 10 coil values to (server) id 42, address 0x00

    ModbusRTUClient.beginTransmission(42, HOLDING_REGISTERS, 0x00, 10);
    for (int i = 0; i < 10; i++) {
        ModbusRTUClient.write(counter);
    }
    if (!ModbusRTUClient.endTransmission()) {
        Serial.print("failed! ");
        Serial.println(ModbusRTUClient.lastError());
    } else {
        Serial.println("success");
    }

    // Alternatively, to write a single Holding Register value use:
    // ModbusRTUClient.holdingRegisterWrite(...)
}

/**
  Reads Holding Register values from the server under specified address.
*/
void readHoldingRegisterValues() {
    Serial.print("Reading Holding Register values ... ");

    // read 10 Input Register values from (server) id 42, address 0x00

    if (!ModbusRTUClient.requestFrom(42, HOLDING_REGISTERS, 0x00, 10)) {
        Serial.print("failed! ");
        Serial.println(ModbusRTUClient.lastError());
    } else {
        Serial.println("success");

        while (ModbusRTUClient.available()) {
            Serial.print(ModbusRTUClient.read());
            Serial.print(' ');
        }
        Serial.println();
    }

    // Alternatively, to read a single Holding Register value use:
    // ModbusRTUClient.holdingRegisterRead(...)
}

/**
  Reads Input Register values from the server under specified address.
*/
void readInputRegisterValues() {
    Serial.print("Reading input register values ... ");

    // read 10 discrete input values from (server) id 42,

    if (!ModbusRTUClient.requestFrom(42, INPUT_REGISTERS, 0x00, 10)) {
        Serial.print("failed! ");
        Serial.println(ModbusRTUClient.lastError());
    } else {
        Serial.println("success");

        while (ModbusRTUClient.available()) {
            Serial.print(ModbusRTUClient.read());
            Serial.print(' ');
        }
        Serial.println();
    }

    // Alternatively, to read a single Input Register value use:
    // ModbusRTUClient.inputRegisterRead(...)
}
```

#### Modbus RTU Server

In the Opta™ Server, the main task will be to poll for Modbus RTU requests and return configured values when requested. It requires following the same initial configuration as the Opta™ Client. The main difference between the Client and the Server devices lies in the `setup()` function:

```arduino
#include <ArduinoRS485.h> // ArduinoModbus depends on the ArduinoRS485 library
#include <ArduinoModbus.h>

constexpr auto baudrate { 19200 };

// Calculate preDelay and postDelay in microseconds as per Modbus RTU Specification
//
// MODBUS over serial line specification and implementation guide V1.02
// Paragraph 2.5.1.1 MODBUS Message RTU Framing
// https://modbus.org/docs/Modbus_over_serial_line_V1_02.pdf
constexpr auto bitduration { 1.f / baudrate };
constexpr auto preDelayBR { bitduration * 9.6f * 3.5f * 1e6 };
constexpr auto postDelayBR { bitduration * 9.6f * 3.5f * 1e6 };
// constexpr auto preDelayBR { bitduration * 10.0f * 3.5f * 1e6 };

const int numCoils = 10;
const int numDiscreteInputs = 10;
const int numHoldingRegisters = 10;
const int numInputRegisters = 10;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("Modbus RTU Server");

  RS485.setDelays(preDelayBR, postDelayBR);

  // start the Modbus RTU client
  if (!ModbusRTUServer.begin(42, baudrate, SERIAL_8E1)) {
      Serial.println("Failed to start Modbus RTU Server!");

      while (1);
  }

  // configure coils at address 0x00
  ModbusRTUServer.configureCoils(0x00, numCoils);

  // configure discrete inputs at address 0x00
  ModbusRTUServer.configureDiscreteInputs(0x00, numDiscreteInputs);

  // configure holding registers at address 0x00
  ModbusRTUServer.configureHoldingRegisters(0x00, numHoldingRegisters);

  // configure input registers at address 0x00
  ModbusRTUServer.configureInputRegisters(0x00, numInputRegisters);
}
```

In the `setup()` function of the sketch dedicated to the Modbus server, the Server address is assigned as an identifier that will be recognized by the Client. Also, the initial values of the `Coils`, `Discrete Input`, `Holding`, and `Input` registers are configured. Those are the data that the Client will locate and retrieve. The following line is necessary in the Server `loop()` function:

```arduino
ModbusRTUServer.poll();
```

This is the line that polls for Modbus RTU requests. The complete code for the Server is shown below:

```arduino
/**
  Getting Started with Modbus RTU on Opta™
  Name: Opta_Server
  Purpose: Configures Coils, Discrete Inputs, Holding and Input Registers; Polls for Modbus RTU requests and maps the coil values to the Discrete Input values, and Holding Registers to the Input Register values.

  @author Arduino
*/

#include <ArduinoRS485.h> // ArduinoModbus depends on the ArduinoRS485 library
#include <ArduinoModbus.h>

constexpr auto baudrate { 19200 };

// Calculate preDelay and postDelay in microseconds as per Modbus RTU Specification
//
// MODBUS over serial line specification and implementation guide V1.02
// Paragraph 2.5.1.1 MODBUS Message RTU Framing
// https://modbus.org/docs/Modbus_over_serial_line_V1_02.pdf
constexpr auto bitduration { 1.f / baudrate };
constexpr auto preDelayBR { bitduration * 9.6f * 3.5f * 1e6 };
constexpr auto postDelayBR { bitduration * 9.6f * 3.5f * 1e6 };
// constexpr auto preDelayBR { bitduration * 10.0f * 3.5f * 1e6 };

const int numCoils = 10;
const int numDiscreteInputs = 10;
const int numHoldingRegisters = 10;
const int numInputRegisters = 10;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("Modbus RTU Server");

  RS485.setDelays(preDelayBR, postDelayBR);

  // start the Modbus RTU client
  if (!ModbusRTUServer.begin(42, baudrate, SERIAL_8E1)) {
      Serial.println("Failed to start Modbus RTU Client!");
      while (1);
  }

  // configure coils at address 0x00
  ModbusRTUServer.configureCoils(0x00, numCoils);

  // configure discrete inputs at address 0x00
  ModbusRTUServer.configureDiscreteInputs(0x00, numDiscreteInputs);

  // configure holding registers at address 0x00
  ModbusRTUServer.configureHoldingRegisters(0x00, numHoldingRegisters);

  // configure input registers at address 0x00
  ModbusRTUServer.configureInputRegisters(0x00, numInputRegisters);
}

void loop() {
  // poll for Modbus RTU requests
  ModbusRTUServer.poll();

  // map the coil values to the discrete input values
  for (int i = 0; i < numCoils; i++) {
    int coilValue = ModbusRTUServer.coilRead(i);

    ModbusRTUServer.discreteInputWrite(i, coilValue);
  }

  // map the holding register values to the input register values
  for (int i = 0; i < numHoldingRegisters; i++) {
    long holdingRegisterValue = ModbusRTUServer.holdingRegisterRead(i);

    ModbusRTUServer.inputRegisterWrite(i, holdingRegisterValue);
  }
}
```

### Testing the Modbus RTU Client and Server

Once the Modbus RTU Client and Server code for each Opta™ device has been uploaded, by opening the Serial Monitor on the Opta™ Client's side a `Success!` message will be displayed after each read-and-write task as shown in the image below:

![Modbus RTU Client and Server communication status](assets/opta-modbus-client.svg)

## Conclusion

This tutorial demonstrates how to use the Arduino ecosystem's `ArduinoRS485` and `ArduinoModbus` libraries, as well as the Arduino IDE, to implement the Modbus RTU protocol between two Opta™ devices. These are necessary elements to enable connection with Modbus RTU compliant devices.

With the help of these examples, it is easy to understand how to enable Modbus RTU communication between a Server and a Client. For further project developments, it offers a scalable architecture to link additional Modbus Server devices, such as secondary Opta™ or a Modbus RTU-compatible module.

### Next Steps

Now that you know how to establish and use Modbus RTU communication with Opta™, you can take a look at [Getting started with connectivity on the Opta™ tutorial](/tutorials/opta/getting-started-connectivity) to discover more about all the connectivity possibilities that Opta™ has to offer.