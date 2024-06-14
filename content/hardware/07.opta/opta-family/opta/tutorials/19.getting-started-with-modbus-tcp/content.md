---
title: 'Getting Started with Modbus TCP on Opta™'
description: "Learn how to use the Modbus TCP protocol on Opta™."
author: 'Taddy Chung'
libraries:
  - name: 'ArduinoRS485'
    url: https://www.arduino.cc/reference/en/libraries/arduinors485
  - name: 'ArduinoModbus'
    url: https://www.arduino.cc/reference/en/libraries/arduinomodbus
difficulty: intermediate
tags:
  - Getting-started
  - ModbusTCP
  - RS-485
software:
  - ide-v1
  - ide-v2
  - arduino-cli
  - web-editor
hardware:
  - hardware/07.opta/opta-family/opta
---

## Overview

...

## Goals

- Learn how to use the Modbus TCP communication protocol between two Opta™ devices

## Required Hardware and Software

### Hardware Requirements

- [Opta™ Lite](https://store.arduino.cc/products/opta-lite), [Opta™ RS485](https://store.arduino.cc/products/opta-rs485), or [Opta™ WiFi](https://store.arduino.cc/products/opta-wifi) (x2)
- 12 VDC / 1 A DIN rail power supply (x1)
- [USB-C® cable](https://store.arduino.cc/products/usb-cable2in1-type-c) (x1)
- RJ-45 LAN cable (x1)
- Power cables for supply and load: Wires with a cross-sectional area ranging from 13.3 mm² to 21.2 mm², corresponding to AWG sizes 6 to 4

### Software Requirements

- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2](https://www.arduino.cc/en/software), or [Arduino Web Editor](https://create.arduino.cc/editor)
- If you choose an offline Arduino IDE, you must install the following libraries: `ArduinoRS485`, and `ArduinoModbus`. You can install these libraries via Library Manager of the Arduino IDE.
- [Modbus TCP example code](assets/Opta_Modbus_TCP_Example.zip)

## Modbus Protocol

Modbus is an open and royalty-free serial communication protocol derived from the client/server architecture. It is widely used in industrial electronic devices, especially in Building Management Systems (BMS) and Industrial Automation Systems (IAS).

It was published by Modicon (now Schneider Electric) in 1979 and has become a _de facto_ standard communication protocol among industrial electronic devices to be used with programmable logic controllers (PLCs).

Modbus communication protocol is often used to connect a supervisory device with a Remote Terminal Unit (TCP) in Supervisory Control and Data Acquisition (SCADA) systems. Reliability in communications between electronic devices is ensured with Modbus by using messages with a simple 16-bit structure with a Cyclic-Redundant Checksum (CRC).

If you want more insights on the Modbus communication protocol, take a look at [Modbus article](https://docs.arduino.cc/learn/communication/modbus) complying as well with Opta™.

## Modbus TCP

The Modbus protocol is a messaging service structure using Client/Server communication. It is an *application protocol*, with its data management being independent of the transmission method.

The **Modbus TCP/IP**, often simply referred to as **Modbus TCP**, is a variant of the Modbus RTU protocol that uses the TCP/IP interface over Ethernet to exchange data between compatible devices. Here are some key elements to understand about Modbus TCP:

* The 'Transmission Control Protocol (TCP)' is responsible for the exchange of packets.

* The 'Internet Protocol (IP)' defines the addresses for routing message destinations.

* A distinct feature of Modbus TCP concerns how it maintains data integrity. Since Modbus TCP encapsulates the basic data frame within the TCP frame, the usual checksum field of Modbus isn't utilized. Instead, the checksum method from the Ethernet TCP/IP layer ensures data integrity.

* Modbus TCP/IP adheres to TCP/IP networking standards on Ethernet, using the Modbus messaging service as its data handler. Typically, the connected devices are Modbus TCP/IP Client and Server devices. However, interconnections can also be established through routers, gateways, or bridges, forming a TCP/IP network.

***Controller/Peripheral was formerly known as Master/Slave. The Modbus Organization no longer supports the use of this terminology. Devices formerly known as Master are referred to as Controller/Client and devices formerly known as Slaves are referred to as Peripheral/Server.***

## Instructions

### Setting Up the Arduino IDE

If you haven't already, head over [here](https://www.arduino.cc/en/software) and install the most recent version of the Arduino IDE along with the necessary device drivers for your computer. For additional details on Opta™, check out the [User Manual](/tutorials/opta/user-manual). Make sure you install the latest version of the [ArduinoModbus](https://www.arduino.cc/reference/en/libraries/arduinomodbus/) and the [ArduinoRS485](https://www.arduino.cc/reference/en/libraries/arduinors485/) libraries, as they will be used to implement the Modbus TCP communication protocol.

### Connecting the Opta™ Over Ethernet LAN

Set up the connection by attaching the Ethernet LAN (RJ-45) cable to both devices using the `ETH RJ45` port. The following image provides a connection diagram for both devices:

![Connecting two Opta™ devices via RS-485](assets/opta-modbus-connection.svg)

The setup incorporates an Ethernet switch that monitors both Opta™ devices using the PLC IDE. This configuration not only links both Opta™ devices using the PLC IDE but also lets you employ a profile to observe information exchanges in real-time. We recommend using the setup with the Ethernet switch for this tutorial to ensure optimal communication between devices.

### Code Overview

...

#### Modbus TCP Client

The Opta™ Client will require the following setup:

```arduino
#include <SPI.h>
#include <Ethernet.h>

#include <ArduinoRS485.h> // ArduinoModbus depends on the ArduinoRS485 library
#include <ArduinoModbus.h>

// Enter a MAC address for your controller below.
// Newer Ethernet shields have a MAC address printed on a sticker on the shield
// The IP address will be dependent on your local network:
byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
};
IPAddress ip(192, 168, 1, 177);

EthernetClient ethClient;
ModbusTCPClient modbusTCPClient(ethClient);

IPAddress server(192, 168, 1, 10); // update with the IP Address of your Modbus server

void setup() {
  //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // start the Ethernet connection and the server:
  Ethernet.begin(mac, ip);

  // Check for Ethernet hardware present
  if (Ethernet.hardwareStatus() == EthernetNoHardware) {
    Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(");
    while (true) {
      delay(1); // do nothing, no point running without Ethernet hardware
    }
  }
  if (Ethernet.linkStatus() == LinkOFF) {
    Serial.println("Ethernet cable is not connected.");
  }
}

void loop() {
  if (!modbusTCPClient.connected()) {
    // client not connected, start the Modbus TCP client
    Serial.println("Attempting to connect to Modbus TCP server");
    
    if (!modbusTCPClient.begin(server, 502)) {
      Serial.println("Modbus TCP Client failed to connect!");
    } else {
      Serial.println("Modbus TCP Client connected");
    }
  } else {
    // client connected

    // write the value of 0x01, to the coil at address 0x00
    if (!modbusTCPClient.coilWrite(0x00, 0x01)) {
      Serial.print("Failed to write coil! ");
      Serial.println(modbusTCPClient.lastError());
    }

    // wait for 1 second
    delay(1000);

    // write the value of 0x00, to the coil at address 0x00
    if (!modbusTCPClient.coilWrite(0x00, 0x00)) {
      Serial.print("Failed to write coil! ");
      Serial.println(modbusTCPClient.lastError());
    }

    // wait for 1 second
    delay(1000);
  }
}
```

#### Modbus TCP Server

In the Opta™ Server, the main task will be to poll for Modbus TCP requests and return configured values when requested. It requires following the same initial configuration as the Opta™ Client. The main difference between the Client and the Server devices lies in the `setup()` function:

```arduino
/*
  Ethernet Modbus TCP Server LED

  This sketch creates a Modbus TCP Server with a simulated coil.
  The value of the simulated coil is set on the LED

  Circuit:
   - Any Arduino MKR Board
   - MKR ETH Shield

  created 16 July 2018
  by Sandeep Mistry
*/

#include <SPI.h>
#include <Ethernet.h>

#include <ArduinoRS485.h> // ArduinoModbus depends on the ArduinoRS485 library
#include <ArduinoModbus.h>

// Enter a MAC address for your controller below.
// Newer Ethernet shields have a MAC address printed on a sticker on the shield
// The IP address will be dependent on your local network:
byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
};
IPAddress ip(192, 168, 1, 177);

EthernetServer ethServer(502);

ModbusTCPServer modbusTCPServer;

const int ledPin = LED_BUILTIN;

void setup() {
  // You can use Ethernet.init(pin) to configure the CS pin
  //Ethernet.init(10);  // Most Arduino shields
  //Ethernet.init(5);   // MKR ETH shield
  //Ethernet.init(0);   // Teensy 2.0
  //Ethernet.init(20);  // Teensy++ 2.0
  //Ethernet.init(15);  // ESP8266 with Adafruit Featherwing Ethernet
  //Ethernet.init(33);  // ESP32 with Adafruit Featherwing Ethernet

  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  Serial.println("Ethernet Modbus TCP Example");

  // start the Ethernet connection and the server:
  Ethernet.begin(mac, ip);

  // Check for Ethernet hardware present
  if (Ethernet.hardwareStatus() == EthernetNoHardware) {
    Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(");
    while (true) {
      delay(1); // do nothing, no point running without Ethernet hardware
    }
  }
  if (Ethernet.linkStatus() == LinkOFF) {
    Serial.println("Ethernet cable is not connected.");
  }

  // start the server
  ethServer.begin();
  
  // start the Modbus TCP server
  if (!modbusTCPServer.begin()) {
    Serial.println("Failed to start Modbus TCP Server!");
    while (1);
  }

  // configure the LED
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);

  // configure a single coil at address 0x00
  modbusTCPServer.configureCoils(0x00, 1);
}

void loop() {
  // listen for incoming clients
  EthernetClient client = ethServer.available();
  
  if (client) {
    // a new client connected
    Serial.println("new client");

    // let the Modbus TCP accept the connection 
    modbusTCPServer.accept(client);

    while (client.connected()) {
      // poll for Modbus TCP requests, while client connected
      modbusTCPServer.poll();

      // update the LED
      updateLED();
    }

    Serial.println("client disconnected");
  }
}

void updateLED() {
  // read the current value of the coil
  int coilValue = modbusTCPServer.coilRead(0x00);

  if (coilValue) {
    // coil value set, turn LED on
    digitalWrite(ledPin, HIGH);
  } else {
    // coild value clear, turn LED off
    digitalWrite(ledPin, LOW);
  }
}
```

### Testing the Modbus TCP Client and Server

Once the Modbus TCP Client and Server code for each Opta™ device has been uploaded, a `Success!` message will be displayed on the Serial Monitor of Opta™ Client after each read-and-write task:

![Modbus TCP Client and Server communication status](assets/opta-modbus-client.svg)

## Conclusion

This tutorial demonstrates how to use the Arduino ecosystem's `ArduinoRS485` and `ArduinoModbus` libraries, as well as the Arduino IDE, to implement the Modbus TCP protocol between two Opta™ devices. These are necessary elements to enable connection with Modbus TCP compliant devices.

With the help of these examples, it is easy to understand how to enable Modbus TCP communication between a Server and a Client. For further project developments, it offers a scalable architecture to link additional Modbus Server devices, such as secondary Opta™ or a Modbus TCP-compatible module.

### Next Steps

Now that you know how to establish and use Modbus TCP communication with Opta™, you can take a look at [Opta User Manual](/tutorials/opta/user-manual) to discover more about all the connectivity possibilities that Opta™ has to offer.

## Support

If you encounter any issues or have questions while working with Opta™ devices, we provide various support resources to help you find answers and solutions.

### Help Center

Explore our Help Center, which offers a comprehensive collection of articles and guides for Opta™ devices. The Help Center is designed to provide in-depth technical assistance and help you make the most of your device.

- [Opta™ help center page](https://support.arduino.cc/hc/en-us/categories/360001637274-Hardware-Support)

### Forum

Join our community forum to connect with other Opta™ devices users, share your experiences, and ask questions. The Forum is an excellent place to learn from others, discuss issues, and discover new ideas and projects related to Opta™.

- [Opta™ category in the Arduino Forum](https://forum.arduino.cc/c/hardware/opta/179)

### Contact Us

Please get in touch with our support team if you need personalized assistance or have questions not covered by the help and support resources described before. We're happy to help you with any issues or inquiries about Opta™ devices.

- [Contact us page](https://www.arduino.cc/en/contact-us/)  