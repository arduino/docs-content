---
title: 'Getting Started With the Arduino SPE Shield'
difficulty: beginner
tags: [Getting Started]
description: 'This tutorial will give you an overview of the core features of the SPE Shield.'
author: 'Pedro Lima'
---
Learn how to establish Single Pair Ethernet (SPE) communication using the Arduino® UNO SPE Shield, enabling industrial IoT connectivity with minimal wiring complexity.

## Overview

The Arduino® UNO SPE Shield brings industrial-grade Single Pair Ethernet (10BASE-T1S) connectivity to Arduino boards, revolutionizing how we connect devices in industrial and IoT applications. This shield combines the simplicity of Ethernet communication with the efficiency of using just a single twisted pair of wires, making it ideal for environments where cable reduction and reliable communication are crucial.

In this guide, you'll learn how to set up your first SPE network, understand the fundamentals of 10BASE-T1S communication, and implement both point-to-point and multidrop network configurations.

![Arduino UNO SPE Shield](assets/overview.png)

## Hardware and Software Requirements

### Hardware Requirements

- Arduino® UNO SPE Shield
- Compatible Arduino UNO board
- USB cables for programming
- Twisted pair cable for SPE connection

### Software Requirements

- [Arduino IDE 2.0](https://www.arduino.cc/en/software) or [Arduino Web Editor](https://create.arduino.cc/editor)
- [Arduino_10BASE_T1S library](https://github.com/arduino-libraries/Arduino_10BASE_T1S) (available through Library Manager)
- [ArduinoModbus library](https://github.com/arduino-libraries/ArduinoModbus) (for industrial protocols)

## Product Overview

The Arduino UNO SPE Shield is a versatile solution for industrial communication, IoT, and automation, combining Single Pair Ethernet (10BASE-T1S) and RS-485. It enables integration into low-power Ethernet networks and robust serial communication systems, ensuring efficient connectivity in embedded environments.

Compatible with the Arduino UNO form factor, it supports SPI, UART, and I2C, facilitating interoperability with various devices. Additionally, it features screw terminals for additional connectivity and power options. Its robust design and advanced protection makes it ideal for applications in industrial environments for remote monitoring and automated control.


### Key Features

- **Single Pair Ethernet**: 10BASE-T1S standard with 10 Mbps data rate, supporting up to 25 meters in multidrop topology with up to 8 nodes
- **RS-485 Communication**: Half-duplex operation at 20 Mbps with 120Ω termination jumper and fail-safe biasing
- **Multiple Interfaces**: UART, SPI, and I2C connectivity through Arduino UNO headers
- **Robust Design**: Operating temperature range -40°C to +85°C with advanced protection features
- **Dimensions**: Standard Arduino shield form factor at 68.58 mm x 53.34 mm

### Pinout

The full pinout is available below:

![Arduino UNO SPE Shield Pinout](assets/UNO_SPE_Pinout.png)

### Datasheet

The complete datasheet is available and downloadable as PDF from the link below:
- [Arduino UNO SPE Shield datasheet](https://docs.arduino.cc/resources/datasheets/ASX00073-datasheet.pdf)

### Schematics

The complete schematics are available and downloadable as PDF from the link below:

- [Arduino UNO SPE Shield schematics](https://docs.arduino.cc/resources/schematics/ASX00073-schematics.pdf)

### STEP Files

The complete STEP files are available and downloadable from the link below:

- [Arduino UNO SPE Shield STEP files](../../downloads/ASX00073-step.zip)

### Form Factor

The Arduino UNO SPE Shield follows the standard Arduino UNO shield form factor, ensuring compatibility with all Arduino UNO boards and enabling stackable designs. With dimensions of 68.58 mm x 53.34 mm, the shield maintains the familiar Arduino ecosystem layout while adding industrial-grade communication capabilities.
The shield features the standard Arduino UNO header arrangement with digital and analog pin access, ICSP connector placement, and proper mounting hole alignment.

![Simplified Form Factor Dimensions](assets/SPE-form-factor.png)

This standardized form factor allows seamless integration into existing Arduino UNO projects and ensures that the shield can be easily incorporated into enclosures and mounting systems designed for the Arduino UNO ecosystem.


## Connectors
The Arduino UNO SPE Shield features several connectors for establishing communication and providing power.

### SPE
The shield offers two primary ways to connect to a Single Pair Ethernet (SPE) 10BASE-T1S network:

![SPE Connectors](assets/spi-connectors.png)

- **SPE using dedicated T1S Connector:** The shield includes a dedicated connector for robust, direct SPE connections to compatible devices.
- **SPE using Screw Terminals:** Screw terminals marked for N (Negative) and P (Positive) pins are also available.

**Technical/Physical Limitations for SPE Connection:**

- A twisted pair cable must be used.
- Maximum bus length of the bus is 25 meters 
- Allows up to eight nodes in a multidrop network. 
- Stub distance (the length of the cable connecting a node to the main bus) must be 5 cm to ensure stable communication and signal integrity.

### RS-485

- **Screw Terminals:** Screw terminals marked for A and B with both GND and +5V positions also available on the terminal.
 ![RS-485 Connector](assets/spi-connectors.png)

**Technical/Physical Limitations:**

- Supports distances up to 1,200 meters with reduced speeds. 
- In a bus topology, supports up to 80 nodes. 
- Half-duplex. 

### Power
A screw connector for powering the board and Shield assembly is provided with two positions for GND and two for VIN.
![Power Screw Connector](assets/power-connector.png)


## Termination Jumpers:

### SPE Termination Jumper:

To enable or disable the onboard termination resistors for the SPE bus there are two pairs of contact you can bridge. 
![Termination jumpers](assets/jumpers.png)
These are necessary always in the edge nodes both when using a multidrop or point-to-point connection.

### RS-485 Termination Jumper:

The same principle applies to the RS-485 connector however in this case there is only a single jumper that needs to be bridged.
![Termination jumpers](assets/RS485-termination.png)

## First Use of Your Arduino UNO SPE Shield

### Stack the Shield

1. Align the Arduino UNO SPE Shield with your Arduino board
2. Carefully press down on the headers to ensure proper connection
3. Verify all pins are properly seated

### Power the Board

The shield can be powered through multiple sources:

- **USB Power**: Via the board's USB connection.
- **Power Jack**: Via the board's power jack.
- **External Power**: Through the VIN terminal.
- **Power over Data Line (PoDL)**: through the T1SP terminal.

![Powering your board](assets/SPE-power.gif)

## Simple Broadcast Example 

This example demonstrates a simple broadcast communication system between multiple nodes on an SPE network. Each node can broadcast messages to all other nodes, and automatically responds with "pong" when it receives a "ping" message. This creates an interactive network where you can test connectivity and response times between different devices.

![Overview of the Ping/Pong example](assets/SPE-ping-pong-01.gif)

### Hardware Setup

1. **Configure Termination Jumpers**: For point-to-point connections, close the termination jumpers on both shields
2. **Connect the SPE Cable**: Wire the twisted pair between the two shields' SPE terminals (N and P pins)
3. **Apply terminator caps**: On edge nodes (first and last) in the bus
4. **Power Both Systems**: Ensure both Arduino boards are powered

### Sketch

The system uses UDP broadcasting to send messages to all nodes simultaneously, making it perfect for testing your SPE network setup and verifying that all nodes are communicating properly. Each node operates independently, listening for incoming messages while also being able to send its own broadcasts.

**Important**: Before uploading this code to each board, you must change the `NODE_ID` constant to a unique value between 0 and 7. Each node on the network must have a different ID to ensure proper communication and avoid conflicts. For example:
- First board: `MY_NODE_NUMBER = 0;`
- Second board: `MY_NODE_NUMBER = 1;`
- Third board(optional): `MY_NODE_NUMBER = 2;`

Remember that any termination nodes should have the termination headers properly closed, more info on the [Arduino UNO SPE Shield datasheet](https://docs.arduino.cc/resources/datasheets/ASX00073-datasheet.pdf).

The node ID determines the device's IP address (192.168.42.100 + NODE_ID) and its position in the PLCA (Physical Layer Collision Avoidance) cycle. When you type a message in the Serial Monitor and press Enter, it's broadcast to all nodes on the network. If any node receives the word "ping", it automatically responds with "pong" to the sender.

```arduino
// Simple 10BASE-T1S Ping-Pong Network
// Each board can send messages to all others
// Automatically replies "pong" when it receives "ping"

#include <Arduino_10BASE_T1S.h>
#include <SPI.h>

// CHANGE THIS NUMBER FOR EACH BOARD (0, 1, 2, 3, etc.)
const int MY_NODE_NUMBER = 0;

// Network addresses (like house addresses on a street)
const IPAddress MY_IP_ADDRESS(192, 168, 42, 100 + MY_NODE_NUMBER);
const IPAddress SUBNET_MASK(255, 255, 255, 0);
const IPAddress GATEWAY_ADDRESS(192, 168, 42, 100);
const IPAddress BROADCAST_ADDRESS(192, 168, 42, 255);  // Sends to everyone
const int NETWORK_PORT = 8888;

// Hardware objects (think of these as your network components)
TC6::TC6_Io* networkIO = nullptr;
TC6::TC6_Arduino_10BASE_T1S* networkController = nullptr;
Arduino_10BASE_T1S_UDP* messageService = nullptr;

// For reading typed messages
char typedMessage[128];
int messageLength = 0;

void setup() {
  // Start serial communication
  Serial.begin(115200);
  delay(1000);
  
  // Show which node this is
  Serial.print("\n=== Network Node #");
  Serial.print(MY_NODE_NUMBER);
  Serial.println(" ===");
  Serial.print("My IP address: ");
  Serial.println(MY_IP_ADDRESS);
  
  // Set up the network hardware
  if (!setupNetwork()) {
    Serial.println("ERROR: Network setup failed!");
    while(1) {
      delay(1000);  // Stop here if network won't start
    }
  }
  
  Serial.println("\n✓ Ready to communicate!");
  Serial.println("Type a message and press Enter to send to everyone");
  Serial.println("I'll automatically reply 'pong' if someone sends 'ping'\n");
}

void loop() {
  // Keep the network running (like keeping your phone connected to WiFi)
  (*networkController).service();
  
  // Check if user typed something
  checkForTypedMessages();
  
  // Check if someone sent us a message
  checkForIncomingMessages();
  
  // Show we're still alive every 10 seconds
  showHeartbeat();
}

bool setupNetwork() {
  Serial.println("Setting up network hardware...");
  
  // Create the network components
  networkIO = new TC6::TC6_Io(SPI, CS_PIN, RESET_PIN, IRQ_PIN);
  networkController = new TC6::TC6_Arduino_10BASE_T1S(networkIO);
  messageService = new Arduino_10BASE_T1S_UDP();
  
  // Set up interrupt (this lets the network chip tell us when data arrives)
  pinMode(IRQ_PIN, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(IRQ_PIN), []() {
    if (networkIO) (*networkIO).onInterrupt();
  }, FALLING);
  
  // Start the low-level network interface
  if (!(*networkIO).begin()) {
    Serial.println("Failed to start network interface");
    return false;
  }
  
  // Create unique network identity
  MacAddress myMacAddress = MacAddress::create_from_uid();
  T1SPlcaSettings plcaSettings(MY_NODE_NUMBER);
  T1SMacSettings macSettings;
  
  // Connect to the network with our address
  if (!(*networkController).begin(MY_IP_ADDRESS, SUBNET_MASK, GATEWAY_ADDRESS, 
                                myMacAddress, plcaSettings, macSettings)) {
    Serial.println("Failed to join network");
    return false;
  }
  
  // Configure output pins (not used in this simple example)
  (*networkController).digitalWrite(TC6::DIO::A0, false);
  (*networkController).digitalWrite(TC6::DIO::A1, false);
  
  // Start the message service
  if (!(*messageService).begin(NETWORK_PORT)) {
    Serial.println("Failed to start message service");
    return false;
  }
  
  Serial.print("Network ID (MAC): ");
  Serial.println(myMacAddress);
  Serial.println("✓ Network setup complete");
  
  return true;
}

void checkForTypedMessages() {
  // Read characters as user types
  while (Serial.available()) {
    char newChar = Serial.read();
    
    // If user pressed Enter, send the message
    if (newChar == '\n' || newChar == '\r') {
      if (messageLength > 0) {
        typedMessage[messageLength] = '\0';  // End the string
        sendMessageToEveryone(typedMessage);
        messageLength = 0;  // Reset for next message
      }
    }
    // Add character to our message (if there's room)
    else if (messageLength < sizeof(typedMessage) - 1) {
      typedMessage[messageLength] = newChar;
      messageLength++;
    }
  }
}

void sendMessageToEveryone(const char* message) {
  // Don't send empty messages
  if (!messageService || strlen(message) == 0) {
    return;
  }
  
  // Send to broadcast address (everyone on network gets it)
  (*messageService).beginPacket(BROADCAST_ADDRESS, NETWORK_PORT);
  (*messageService).write((const uint8_t*)message, strlen(message));
  (*messageService).endPacket();
  
  Serial.print("📤 Sent to all: ");
  Serial.println(message);
}

void checkForIncomingMessages() {
  // See if a message arrived
  int messageSize = (*messageService).parsePacket();
  
  // No message or message too big
  if (messageSize <= 0 || messageSize >= 256) {
    return;
  }
  
  // Read the message
  char receivedMessage[256] = {0};
  IPAddress senderAddress = (*messageService).remoteIP();
  
  int bytesRead = (*messageService).read((uint8_t*)receivedMessage, 
                                       min(messageSize, 255));
  if (bytesRead <= 0) {
    return;
  }
  
  receivedMessage[bytesRead] = '\0';  // End the string properly
  
  // Show who sent what
  Serial.print("📥 From ");
  Serial.print(senderAddress);
  Serial.print(": ");
  Serial.println(receivedMessage);
  
  // If someone sent "ping", automatically reply "pong"
  if (strcmp(receivedMessage, "ping") == 0) {
    // Small delay to avoid message collisions (each node waits different time)
    delay(10 + (MY_NODE_NUMBER * 5));
    replyPongTo(senderAddress);
  }
}

void replyPongTo(IPAddress targetAddress) {
  // Send "pong" back to whoever sent "ping"
  (*messageService).beginPacket(targetAddress, NETWORK_PORT);
  (*messageService).write((const uint8_t*)"pong", 4);
  (*messageService).endPacket();
  
  Serial.println("🏓 Auto-replied: pong");
}

void showHeartbeat() {
  static unsigned long lastHeartbeat = 0;
  
  // Every 10 seconds, show we're still running
  if (millis() - lastHeartbeat > 10000) {
    lastHeartbeat = millis();
    Serial.println("💓 [System running normally]");
  }
}
```

### SPI/RS-485 Network Example

This example demonstrates a hierarchical control system where a central SPE controller manages multiple Arduino Opta boards through gateway nodes. The system uses SPE (Single Pair Ethernet) for the main network backbone and RS-485 for connecting to end devices, combining the benefits of modern Ethernet with the reliability of industrial serial communication.

The architecture consists of three layers: a central control node that issues commands, gateway nodes that translate between SPE and RS-485 protocols, and Opta boards that execute the actual control operations. This design allows for scalable industrial automation where multiple Opta boards can be distributed across a facility while being managed from a single control point.

### Central Control Node (Server)

The central control node (Node 7) acts as the command center of the system, sending LED control commands to specific Opta boards through their associated gateway nodes. Operating on the SPE network, this node provides a simple serial interface where operators can type commands like "LED 3" to toggle specific LEDs on remote Optas.

![Central SPE Controller](assets/SPE-rs485-transducer-main.png)

```arduino 
work in progress
```

### Transducer Node SPE/RS-485

The gateway nodes serve as protocol translators between the SPE network and RS-485 devices. Each gateway consists of an Arduino board with an SPE shield, where the board's hardware serial port (Serial1) connects to the RS-485 transceiver on the shield. These nodes receive UDP packets from the SPE network, extract the command data, and forward it to the RS-485 bus.

![Shields Addressing the Endpoints Across Protocols](assets/SPE-rs485-transducer-transducer.png)

When an Opta board responds via RS-485, the gateway captures the response and sends it back to the central controller as a UDP packet. This bidirectional translation allows transparent communication between the SPE-based control system and RS-485 devices, making it possible to control multiple Opta boards from a single point on the network.

```arduino
In Progress
```

### Opta RS-485 Interface

The Arduino Opta boards represent the end devices in this system, receiving commands via RS-485 and executing the requested actions. Each Opta configures pins 2-13 as digital outputs and listens for specific command formats on its serial interface. The boards can process three types of commands: reading individual pin states, writing to specific pins, or reading all pin states at once.

![Opta as Endpoint](assets/SPE-rs485-transducer-end.png)

When an Opta receives a command, it parses the instruction, performs the requested operation, and sends back a formatted response. This simple protocol allows the central SPE controller to remotely monitor and control multiple Opta boards across the RS-485 network, creating a flexible and scalable industrial control system.

```arduino
In progress
```

## Troubleshooting

### Common Issues and Solutions

   **No Communication**
   - Verify termination jumpers are correctly set (closed for P2P, only endpoints for multidrop)
   - Check cable connections and polarity
   - Ensure twisted pair cable is used

   **Intermittent Communication**
   - Reduce cable length (maximum 25m)
   - Check for proper grounding
   - Verify stub lengths in multidrop (< 5cm)

   **Power Issues**
   - When using PoDL, ensure power supply can provide sufficient current
   - Check voltage levels are within specification (7-24V)
   - Verify Arduino board voltage compatibility

### LED Indicators

The shield provides status LEDs for diagnostics:
- **PWR**: Power status
- **SPE**: Link activity
- **TX/RX**: Data transmission indicators

## Summary

In this guide, you've learned how to:
- Set up the Arduino UNO SPE Shield for Single Pair Ethernet communication
- Implement point-to-point and multidrop network configurations
- Use Power over Data Line for remote device powering
- Integrate industrial protocols like Modbus over SPE
- Troubleshoot common connectivity issues

The Arduino UNO SPE Shield opens up new possibilities for industrial IoT applications, providing reliable, cost-effective communication with minimal wiring requirements.

## Next Steps

- Explore the [Arduino_10BASE_T1S library documentation](https://github.com/arduino-libraries/Arduino_10BASE_T1S)
- Learn about [RS-485 communication](link-to-rs485-guide) with the same shield
- Build industrial IoT projects with [Arduino Cloud](https://app.arduino.cc)
- Implement advanced protocols like [Modbus](https://github.com/arduino-libraries/ArduinoModbus) over SPE