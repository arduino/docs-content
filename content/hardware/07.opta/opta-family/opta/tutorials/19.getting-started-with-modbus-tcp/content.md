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

The Opta™ offers industrial-grade hardware and software capabilities, along with the Arduino ecosystem tools such as the Arduino IDE and its libraries, allowing easy implementation of different Modbus communication protocols, including Modbus TCP.

In this tutorial, we will learn how to set up and use the Modbus TCP communication protocol over Ethernet between two Opta™ devices.

## Goals

- Learn how to set up the workspace environment for Modbus TCP using Arduino IDE.
- Learn how to use the Modbus TCP communication protocol between two Opta™ devices.
- Learn how to verify that Opta™ has been correctly set up using an example that uses Modbus TCP communication.

## Required Hardware and Software

### Hardware Requirements

- [Opta™ Lite](https://store.arduino.cc/products/opta-lite), [Opta™ RS485](https://store.arduino.cc/products/opta-rs485), or [Opta™ WiFi](https://store.arduino.cc/products/opta-wifi) (x2)
- 12 VDC / 1 A DIN rail power supply (x1)
- [USB-C® cable](https://store.arduino.cc/products/usb-cable2in1-type-c) (x1)
- Ethernet cable with RJ45 connectors - Cat5e, Cat6, Cat6e (x1)
- Power cables for supply and load: Wires with a cross-sectional area ranging from 13.3 mm² to 21.2 mm², corresponding to AWG sizes 6 to 4

### Software Requirements

- [Arduino IDE 2.0+](https://www.arduino.cc/en/software) or [Arduino Web Editor](https://create.arduino.cc/editor)
- If you choose an offline Arduino IDE, you must install the following libraries via the Library Manager: [**ArduinoRS485**](https://github.com/arduino-libraries/ArduinoRS485) and [**ArduinoModbus**](https://github.com/arduino-libraries/ArduinoModbus).
- [Modbus TCP example code](assets/Opta_Modbus_TCP_Example.zip)

## Modbus Protocol

Modbus is a widely used, open, and royalty-free serial communication protocol based on a client/server architecture. It is commonly known in industrial electronic devices, such as Building Management Systems (BMS) and Industrial Automation Systems (IAS).

Developed by Modicon (now Schneider Electric) in 1979, Modbus has become a standard communication protocol for industrial electronic devices, particularly those using programmable logic controllers (PLCs).

The Modbus protocol is frequently used to connect supervisory devices with Remote Terminal Units (RTUs) in Supervisory Control and Data Acquisition (SCADA) systems. Modbus ensures reliable communication between electronic devices through simple 16-bit messages with a Cyclic Redundant Checksum (CRC) for error-checking.

For more information on the Modbus protocol, check out the [Modbus article](https://docs.arduino.cc/learn/communication/modbus) complying with Opta™.

## Modbus TCP

The Modbus protocol is a messaging service that uses Client/Server or Controller/Peripheral communications. It keeps its data handling separate from its transmission method as an *application protocol*.

**Modbus over TCP/IP**, commonly known as **Modbus TCP**, is a variant of the Modbus RTU protocol. It uses the TCP/IP interface over Ethernet for data transfer between compatible devices. Here are some key points about Modbus TCP:

* The **Transmission Control Protocol (TCP)** manages packet transmissions.

* The **Internet Protocol (IP)** sets the addresses to guide message routing.

* Modbus TCP maintains data integrity by encapsulating the primary data frame within a TCP frame, relying on the Ethernet TCP/IP layer’s checksum technique instead of the traditional Modbus checksum.

* Modbus over TCP/IP sticks to TCP/IP networking standards on Ethernet, using the Modbus messaging service as its data intermediary. Connections involve Modbus TCP/IP Client and Server devices, but routers, gateways, or bridges can also create a TCP/IP network.

***The terms __Controller__ and __Peripheral__ replace the outdated __Master__ and __Slave__ terminology. The Modbus Organization now refers to devices previously known as __Masters__ as __Controllers/Clients__ and devices previously known as __Slaves__ as __Peripherals/Servers__.***

## Instructions

### Setting Up the Arduino IDE

This tutorial requires the latest version of the Arduino IDE, which you can download [here](https://www.arduino.cc/en/software). In the Arduino IDE, you need to install the **`Arduino Mbed OS Opta Boards`** core for Opta™ devices.

To install the core for Opta™, navigate to **Tools > Board > Boards Manager** or click the **Boards Manager** icon in the left tab of the IDE.

In the Boards Manager tab, search for `opta` and install the latest `Arduino Mbed OS Opta Boards` core version.

![Installing the Opta™ core in the Arduino IDE](assets/opta-core.png)

### Installing the Required Libraries

Install the latest versions of the following libraries required for Modbus TCP communication:

- [**ArduinoModbus**](https://github.com/arduino-libraries/ArduinoModbus)
- [**ArduinoRS485**](https://github.com/arduino-libraries/ArduinoRS485)

You can easily install them through the Library Manager in the Arduino IDE. The Library manager can be accessed using the **"ctrl + shift+ i"** shortcut, by going to **Tools > Manage Libraries...**, or by navigating the left panel of the Arduino IDE and selecting the third option from the top.

### Connecting the Opta™ Over Ethernet LAN

Set up the connection by attaching the Ethernet LAN (RJ-45) cable to both devices using the `ETH RJ45` port. The following image provides a connection diagram for both devices:

![Connecting two Opta™ devices via Ethernet cable with RJ45 connector](assets/opta-modbus-connection.png)

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

Once the Modbus TCP Client and Server code for each Opta™ device has been uploaded, the user LED will be toggles along with the coil value on the Serial Monitor of the Opta™ Client after each read-and-write task:

![Modbus TCP Client and Server communication status](assets/opta-modbus-client.svg)

## Conclusion

This tutorial demonstrates how to use the Arduino ecosystem's `ArduinoRS485` and `ArduinoModbus` libraries and the Arduino IDE to implement the Modbus TCP protocol between two Opta™ devices. These elements are essential for allowing connections with Modbus TCP-compliant devices.

With these examples, you can easily understand how to establish Modbus TCP communication between a Server and a Client using Opta™. This setup provides a scalable architecture for connecting additional Modbus Server devices, such as another Opta™ or a Modbus TCP-compatible module.

### Next Steps

Now that you know how to establish and use Modbus TCP communication with Opta™, you can explore the [Opta User Manual](/tutorials/opta/user-manual) to discover more about all the connectivity possibilities that Opta™ offers.

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