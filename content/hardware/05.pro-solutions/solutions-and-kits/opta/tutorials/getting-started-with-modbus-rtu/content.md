---
title: 'Getting Started with Modbus RTU on the Arduino Opta®'
description: "Learn how to use the Modbus RTU serial protocol on the Arduino Opta®."
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

Modbus is an open serial protocol derived from the client/server architecture initially developed and published by Modicon (now Schneider Electric) in 1979 for use with programmable logic controllers (PLCs); since 1979, Modbus has become a standard communications protocol in industrial electronic devices. The Opta™, with its industrial hardware and software capabilities and the Arduino ecosystem tools such as the Arduino IDE and its libraries, can implement this communications protocol. In this tutorial, we will learn how to implement this communications protocol over RS-485 between two Opta™ devices.

## Goals

- Learn how to use the Modbus RTU communications protocol over RS-485 between two Opta™ devices

### Required Hardware and Software

### Hardware Requirements

- [Arduino Opta®](https://store.arduino.cc/pages/opta) (x2)
- 12VDC/1A DIN rail power supply (x1)
- USB-C® cable (x1)

### Software Requirements

- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2.0+](https://www.arduino.cc/en/software), or [Arduino Web Editor](https://create.arduino.cc/editor)

## Modbus 101

Modbus is a widely used open and royalty-free serial communications protocol in industrial electronic devices, especially in Building Management Systems (BMS) and Industrial Automation Systems (IAS). It has become a _de facto_ standard communications protocol among industrial electronic devices since it was published in 1979 (more than 40 years ago).

***Modbus communications protocol is often used to connect a supervisory device with a Remote Terminal Unit (RTU) in Supervisory Control and Data Acquisition (SCADA) Systems.***

Using messages with a simple 16-bit structure with a Cyclic-Redundant Checksum (CRC), reliability in communications between electronic devices is ensured with Modbus.

***If you want a more in-depth article explaining the entirety of Modbus communications protocol, look at our [Modbus article](https://docs.arduino.cc/learn/communication/modbus).***

## Instructions

### Setting Up the Arduino IDE

First, let's ensure we have the latest Arduino IDE version installed on our computers; you can download the latest Arduino IDE version [here](https://www.arduino.cc/en/software). If you are using Opta™ for the first time, please look at our [getting started tutorial](/tutorials/opta/getting-started) and install the device drivers on your computer. Modbus RTU communications protocol will be implemented using the [`ArduinoModbus`](https://www.arduino.cc/reference/en/libraries/arduinomodbus/) library, be sure to install the latest version of the library.

***`ArduinoModbus` library requires the `ArduinoRS485` library as the Modbus library is dependent on it; remember to install both libraries.***

### Connecting the Optas Over RS-485

Now that we have the Arduino IDE configured and the libraries installed, let's connect both Opta™ devices via RS-485, as shown in the image below:

![Connecting two Opta™ devices via RS-485.](assets/opta-modbus-connection.png)

### Code Overview

The objective of the example described below is to configure and use Modbus RTU communications protocol over RS-485 between two Opta™ devices, one acting as a Client and the other acting as a Server. The Client is responsible for writing and reading `Coil`, `Holding`, `Discrete Input`, and `Input` register values. The Server will poll for Modbus RTU requests and return values accordingly to each request. To help you understand better how the example works, we will briefly explain the essential parts of the code used in this tutorial.

#### Modbus RTU Client

The Opta™ Client will require the following setup:

```arduino
#include <ArduinoModbus.h>
#include <ArduinoRS485.h>

constexpr auto baudrate { 9600 };

// Calculate preDelay and postDelay in microseconds as per Modbus RTU specification
constexpr auto bitduration { 1.f / baudrate };
constexpr auto preDelayBR { bitduration * 9.6f * 3.5f * 1e6 };
constexpr auto postDelayBR { bitduration * 9.6f * 3.5f * 1e6 };

#define pause_trigger 15
int counter = 0;
int oper_pause = 0;

void setup() {
    Serial.begin(9600);
    while (!Serial);

    Serial.println("Modbus RTU Client");
    RS485.setDelays(preDelayBR, postDelayBR);

    // Start the Modbus RTU Client
    if (!ModbusRTUClient.begin(baudrate, SERIAL_8E1)) {
        Serial.println("Failed to start Modbus RTU Client!");
        while (1);
    }
}
```

Given Modbus RTU specification, `preDelay` and `postDelay` must be configured for correct operation. The baud rate can be configured as `4800`, `9600`, and `19200`; in the current example, we are using a baud rate of `9600`, but it can be changed depending on the system requirements. The `SERIAL_8E1` defines the serial port parameters setting (8 data bits, even parity, and one stop bit).

In this example, an Opta™ device is defined as a Modbus Server from which information will be retrieved. The Server can be a module or a sensor with registers that can be accessed using specified addresses to obtain desired information about what's being measured or monitored. Inside the loop function of the example code of the Client, we will have several tasks in charge of reading and writing specific values to test Modbus RTU communication with the Server.

```arduino
void loop(){
    writeCoilValues();
    readCoilValues();
    readDiscreteInputValues();
    writeHoldingRegisterValues();
    readHoldingRegisterValues();
    readInputRegisterValues();

    counter++;
    oper_pause++;

    if (oper_pause >= pause_trigger) {
      oper_pause = 0;
      delay(5000);
    }
    Serial.println();
}
```

As we are interested in obtaining specific values, we will define a simple operation pause counter that will be flagged if conditions are met with the defined pause trigger. This will keep the communication busy to keep data flowing and create a headroom for the devices to process if required.

The complete code for the Client is shown below:

```arduino
#include <ArduinoModbus.h>
#include <ArduinoRS485.h>

constexpr auto baudrate { 9600 };

// Calculate preDelay and postDelay in microseconds as per Modbus RTU Specification
constexpr auto bitduration { 1.f / baudrate };
constexpr auto preDelayBR { bitduration * 9.6f * 3.5f * 1e6 };
constexpr auto postDelayBR { bitduration * 9.6f * 3.5f * 1e6 };

#define pause_trigger 15
int counter = 0;
int oper_pause = 0;

void setup() {
    Serial.begin(9600);
    while (!Serial);

    Serial.println("Modbus RTU Client");
    RS485.setDelays(preDelayBR, postDelayBR);

    // Start the Modbus RTU Client
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
    oper_pause++;

    if (oper_pause >= pause_trigger){
      oper_pause = 0;
      delay(5000);
    }
    Serial.println();
}

void writeCoilValues() {
    // Set the coils to 1 when counter is odd
    byte coilValue = ((counter % 2) == 0) ? 0x00 : 0x01;
    Serial.print("Writing Coil register values... ");

    // Write 10 Coil register values to ID 42, address 0x00
    ModbusRTUClient.beginTransmission(42, COILS, 0x00, 10);
    for (int i = 0; i < 10; i++) {
        ModbusRTUClient.write(coilValue);
    }
    if (!ModbusRTUClient.endTransmission()) {
        Serial.print("Failed! ");
        Serial.println(ModbusRTUClient.lastError());
    } else {
        Serial.println("Success!");
    }
}

void readCoilValues() {
    Serial.print("Reading Coil register values... ");

    // Read 10 Coil values from ID 42, address 0x00
    if (!ModbusRTUClient.requestFrom(42, COILS, 0x00, 10)) {
        Serial.print("Failed! ");
        Serial.println(ModbusRTUClient.lastError());
    } else {
        Serial.println("Success!");

        while (ModbusRTUClient.available()) {
            Serial.print(ModbusRTUClient.read());
            Serial.print(' ');
        }
        Serial.println();
    }
}

void readDiscreteInputValues() {
    Serial.print("Reading Discrete Input register values... ");

    // Read 10 Discrete Input values from ID 42, address 0x00
    if (!ModbusRTUClient.requestFrom(42, DISCRETE_INPUTS, 0x00, 10)) {
        Serial.print("Failed! ");
        Serial.println(ModbusRTUClient.lastError());
    } else {
        Serial.println("success");

        while (ModbusRTUClient.available()) {
            Serial.print(ModbusRTUClient.read());
            Serial.print(' ');
        }
        Serial.println();
    }
}

void writeHoldingRegisterValues() {
    // Set the Holding register values to counter value
    Serial.print("Writing Holding registers values... ");

    // write 10 coil values to (slave) id 42, address 0x00
    ModbusRTUClient.beginTransmission(42, HOLDING_REGISTERS, 0x00, 10);
    for (int i = 0; i < 10; i++) {
        ModbusRTUClient.write(counter);
    }
    if (!ModbusRTUClient.endTransmission()) {
        Serial.print("failed! ");
        Serial.println(ModbusRTUClient.lastError());
    } else {
        Serial.println("Success");
    }
}

void readHoldingRegisterValues() {
    Serial.print("Reading Holding Register values ... ");

    // Read 10 Input Register values from ID 42, address 0x00
    if (!ModbusRTUClient.requestFrom(42, HOLDING_REGISTERS, 0x00, 10)) {
        Serial.print("Failed! ");
        Serial.println(ModbusRTUClient.lastError());
    } else {
        Serial.println("Success!");

        while (ModbusRTUClient.available()) {
            Serial.print(ModbusRTUClient.read());
            Serial.print(' ');
        }
        Serial.println();
    }
}

void readInputRegisterValues() {
    Serial.print("Reading Input register values ... ");

    // Read 10 discrete input values from ID 42,
    if (!ModbusRTUClient.requestFrom(42, INPUT_REGISTERS, 0x00, 10)) {
        Serial.print("Failed! ");
        Serial.println(ModbusRTUClient.lastError());
    } else {
        Serial.println("Success!");

        while (ModbusRTUClient.available()) {
            Serial.print(ModbusRTUClient.read());
            Serial.print(' ');
        }
        Serial.println();
    }
}
```

#### Modbus RTU Server

In the Opta™ Server, the main task will be to poll for Modbus RTU requests and return configured values when requested. It requires following the same initial configuration as the Opta™ Client. The main difference between the Client and the Server devices is found in the `setup()` function:

```arduino
// Start the Modbus RTU Server
void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("Modbus RTU Server");
  RS485.setDelays(preDelayBR, postDelayBR);

  if (!ModbusRTUServer.begin(42, baudrate, SERIAL_8E1)) {
      Serial.println("Failed to start Modbus RTU Client!");
      while (1);
  }

  // Configure Coils registers at address 0x00
  ModbusRTUServer.configureCoils(0x00, numCoils);

  // Configure Discrete Inputs registers at address 0x00
  ModbusRTUServer.configureDiscreteInputs(0x00, numDiscreteInputs);

  // Configure Holding registers at address 0x00
  ModbusRTUServer.configureHoldingRegisters(0x00, numHoldingRegisters);

  // Configure Input registers at address 0x00
  ModbusRTUServer.configureInputRegisters(0x00, numInputRegisters);
}
```

In the Server `setup()` function, we assign the Server address; the given Server address will be an identifier to be recognized by the Client. Also, we will configure the initial values of the `Coils`, `Discrete Input`, `Holding`, and `Input` registers. These will be the data that the Client will locate and retrieve. In the Server `loop()` function, the following line will be necessary:

```arduino
ModbusRTUServer.poll();
```

This is the line that will poll for Modbus RTU requests. The complete code for the Server is shown below:

```arduino
#include <ArduinoRS485.h>
#include <ArduinoModbus.h>

constexpr auto baudrate { 9600 };

// Calculate preDelay and postDelay in microseconds as per Modbus RTU Specification
constexpr auto bitduration { 1.f / baudrate };
constexpr auto preDelayBR { bitduration * 9.6f * 3.5f * 1e6 };
constexpr auto postDelayBR { bitduration * 9.6f * 3.5f * 1e6 };

const int numCoils = 10;
const int numDiscreteInputs = 10;
const int numHoldingRegisters = 10;
const int numInputRegisters = 10;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("Modbus RTU Server");
  RS485.setDelays(preDelayBR, postDelayBR);

  // Start the Modbus RTU client
  if (!ModbusRTUServer.begin(42, baudrate, SERIAL_8E1)) {
      Serial.println("Failed to start Modbus RTU Client!");
      while (1);
  }

  // Configure Coils registers at address 0x00
  ModbusRTUServer.configureCoils(0x00, numCoils);

  // Configure Discrete Inputs registers at address 0x00
  ModbusRTUServer.configureDiscreteInputs(0x00, numDiscreteInputs);

  // Configure Holding registers at address 0x00
  ModbusRTUServer.configureHoldingRegisters(0x00, numHoldingRegisters);

  // Configure Input registers at address 0x00
  ModbusRTUServer.configureInputRegisters(0x00, numInputRegisters);
}

void loop() {
  // Poll for Modbus RTU requests
  ModbusRTUServer.poll();

  // Map the Coil registers values to the discrete input values
  for (int i = 0; i < numCoils; i++) {
    int coilValue = ModbusRTUServer.coilRead(i);
    ModbusRTUServer.discreteInputWrite(i, coilValue);
  }

  // Map the Holding registers values to the Input registers values
  for (int i = 0; i < numHoldingRegisters; i++) {
    long holdingRegisterValue = ModbusRTUServer.holdingRegisterRead(i);
    ModbusRTUServer.inputRegisterWrite(i, holdingRegisterValue);
  }
}
```

### Testing the Modbus RTU Client and Server

Once you have uploaded the Modbus RTU Client and Server code for each Opta™ device, we can open the Serial Monitor on the Client side to debug the communication status between the devices. If everything is working correctly, you will be able to see `Success!` messages after each read-and-write tasks as shown in the image below:

![Modbus RTU Client and Server communication status.](assets/opta-modbus-client.png)

## Conclusion

In this tutorial, we established a Modbus RTU connection between two Opta™ devices using the Arduino ecosystem tools, such as the Arduino IDE and Arduino libraries. The `ArduinoRS485` and `ArduinoModbus` libraries are essential components that enable communication with compatible Modbus RTU devices. With the demonstrative example described in this tutorial, we have established communication between a Modbus RTU Server and a Client; we can now configure and set a secondary Arduino Opta® or use a Modbus RTU-compatible module for your project developments.