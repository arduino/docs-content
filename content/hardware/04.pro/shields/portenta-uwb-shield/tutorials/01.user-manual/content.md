---
title: 'Portenta UWB Shield User Manual'
difficulty: intermediate
compatible-products: [portenta-uwb-shield]
description: 'Learn about the hardware and software features of the Arduino® Portenta UWB Shield.'
tags:
  - UWB
  - Positioning
  - Real-time location
  - Sensors
  - User manual
author: 'José Bagur'
hardware:
  - hardware/06.portenta/shields/portenta-uwb-shield
software:
  - ide-v2
---

This user manual provides a comprehensive overview of the Portenta UWB Shield, highlighting its hardware and software elements. With it, you will learn how to set up, configure, and use all the main features of the Portenta UWB Shield.

![ ](assets/hero-banner.png)

## Hardware and Software Requirements

### Hardware Requirements

- [Portenta UWB Shield (SKU: ASX00074)](https://store.arduino.cc/products/portenta-uwb-shield) (x1)
- [Portenta C33 (SKU: ABX00074)](https://store.arduino.cc/products/portenta-c33) (x1)
- [USB-C® cable (SKU: TPX00094)](https://store.arduino.cc/products/usb-cable2in1-type-c) (x1)

### Software Requirements

- [Arduino IDE 2.0+](https://www.arduino.cc/en/software)
- ardUWBSr150 library
- [Arduino Renesas Portenta Boards core](https://github.com/arduino/ArduinoCore-renesas) (required to work with the Portenta C33 board)

***The Portenta UWB Shield is not intended as a standalone device but as a shield to work alongside a Portenta family board. In this user manual, we will use the Portenta C33 as the main board and show how to use the Portenta UWB Shield with it.***

## Portenta UWB Shield Overview

Enhance your positioning and real-time location capabilities with the Portenta UWB Shield. Based on the Truesense DCU150 module, this versatile Ultra-Wideband (UWB) communication solution integrates with the Portenta C33 board via its High-Density connectors and functions as a base station for two-way ranging and real-time location services (RTLS).

The Portenta UWB Shield incorporates the NXP® Trimension™ SR150 UWB integrated circuit (IC) within the DCU150 module, three embedded PCB antennas, onboard power management, clock control, filters and peripheral components. With +1.8 to +3.3 VDC level shifters and dual High-Density board-to-board connectors, it plugs directly into the Portenta C33 board, making it an excellent choice for projects that require precise positioning and real-time location tracking.

### Understanding UWB Technology

UWB is a radio technology that uses very low energy levels for short-range, high-bandwidth communications over a large portion of the radio spectrum. Unlike traditional narrow-band radio systems, like Bluetooth® or Wi-Fi®, UWB transmits across a wide range of frequency bands (typically 500 MHz or more).

Some of the key characteristics of UWB are the following:

- **High precision**: UWB can determine the relative position of devices with centimeter-level accuracy (typically 5-10 cm), far more precise than GPS, Bluetooth® or Wi-Fi®.
- **Low-power consumption**: Despite its high data rates, UWB consumes very little power, making it suitable for battery-operated devices.
- **Short range**: Typically effective within 10-30 meters, making it ideal for indoor positioning applications.
- **Strong security**: The unique physical layer characteristics of UWB make it more resistant to relay attacks compared to other wireless technologies.

So, how does UWB technology works?

UWB uses a technique called "Time of Flight" (ToF) or "Time Difference of Arrival" (TDoA) to determine the distance between UWB-enabled devices. In a nutshell, this technique consists of the following steps:

1. An UWB transmitter sends a signal with a precise timestamp.
2. An UWB receiver detects the signal and calculates the time it took to arrive.
3. Since radio waves travel at the speed of light (approximately 30 cm per nanosecond), the system can calculate the distance with high precision.

For even greater accuracy, UWB can use the "Two-Way Ranging" (TWR) technique, where devices exchange several messages to account for clock synchronization issues. The Angle of Arrival (AoA) capability, which the Portenta UWB Shield supports, enhances positioning by not only determining distance but also the angle from which a signal arrives, enabling with this more accurate 2D or 3D positioning.

In an UWB positioning system, devices typically operate in one of two roles:

- **Anchors**: Fixed-position devices (like the Portenta UWB Shield with a Portenta C33) that provide reference points for the positioning system.
- **Tags**: Mobile devices that communicate with anchors to determine their position in space.

Some of the key applications of UWB technology are the following:

- **Asset tracking:** Monitor the location of valuable items in warehouses, hospitals or construction sites.
- **Secure access**: Contactless entry systems that unlock only when an authorized device is in proximity.
- **Precision navigation**: Guide robots, vehicles or drones in environments where GPS is unavailable.
- **Social distancing**: Measure precise distances between individuals in workplaces or public venues.

### Portenta UWB Shield Architecture Overview

The Portenta UWB Shield features a secure, certified and durable design that suits various applications, such as smart logistics, precision proximity sensing, high precision RTLS, industrial applications, access control and secure payments.

The top view of the Portenta UWB Shield is shown in the image below:

![The Portenta UWB Shield main components (top view)](assets/user-manual-1.png)

The bottom view of the Portenta UWB Shield is shown in the image below:

![The Portenta UWB Shield main components (bottom view)](assets/user-manual-2.png)

Here's an overview of the shield's main components shown in the images:

- **UWB module**: At the heart of the Portenta UWB Shield is the DCU150 module from Truesense, which incorporates the NXP® Trimension™ SR150 UWB IC. This module supports UWB channels CH5 and CH9 in the 6.0-8.5 GHz range and complies with the IEEE 802.15.4 HRP UWB standard.
- **UWB antennas**: The shield features three embedded PCB antennas for optimal signal reception and transmission.
- **Processor**: The module includes an Arm® Cortex®-M33 32-bit processor running at 125 MHz with 128 kB code RAM, 128 kB data RAM, 128 kB ROM, Arm® TrustZone technology and S-DMA for security.
- **DSP**: An onboard programmable DSP (BSP32 CoolFlux DSP core) with 32 kB RAM for code and 2x 16kB RAM for data enhances signal processing capabilities.
- **Level shifters**: The shield includes +1.8 to +3.3 VDC level shifters for compatible communication with the Portenta C33 board.
- **High-Density connectors**: Dual High-Density board-to-board connectors allow the shield to plug directly into the Portenta C33 board.
- **Shielding can**: Located on top of the DCU150 module, it enhances anti-interference performance.

### Board Libraries

The [`ardUWBSr150` library](https://github.com/arduino-libraries/ardUWBSr150) contains an application programming interface (API) to read data from the shield and control its parameters and behavior. This library supports the following: 

- One-way ranging (Time Difference of Arrival - TDoA) and two-way ranging (TWR).
- Angle of Arrival (AoA) measurement for 2D positioning.
- SPI and GPIO communication with the host board through dedicated level translators.

***The Portenta family boards support the `ardUWBSr150` library.***

To install the `ardUWBSr150` library, navigate to `Tools > Manage libraries...` or click the **Library Manager** icon in the left tab of the Arduino IDE. In the Library Manager tab, search for `ardUWBSr150` and install the latest version of the library.

![Installing the board's library in the Arduino IDE](assets/user-manual-3.png)

### Pinout

The full pinout is available and downloadable as PDF from the link below:

- [Portenta UWB Shield pinout](https://docs.arduino.cc/resources/pinouts/ASX00074-full-pinout.pdf)

### Datasheet

The complete datasheet is available and downloadable as PDF from the link below:

- [Portenta UWB Shield datasheet](https://docs.arduino.cc/resources/datasheets/ASX00074-datasheet.pdf)

### Schematics

The complete schematics are available and downloadable as PDF from the link below:

- [Portenta UWB Shield schematics](https://docs.arduino.cc/resources/schematics/ASX00074-schematics.pdf)

### STEP Files 

The complete STEP files are available and downloadable from the link below:

- [Portenta UWB Shield STEP files](../../downloads/ASX00074-step.zip)

## First Use

### Unboxing the Product

When you open the box of the Portenta UWB Shield, you will find the shield itself featuring two High-Density connectors designed to interface with compatible boards from the Portenta family. The shield also includes three pins for UART communications, which can be used primarily for debugging purposes.

![Unboxing the Portenta UWB Shield](assets/user-manual-4.png)

**It's important to note that the Portenta UWB Shield is not designed to function as a standalone device. Rather, it works as a shield that must be paired with a compatible Arduino board from the Portenta family.** Throughout this user manual, we will be using the Portenta C33 as the main (host) board and the Portenta UWB Shield as the client board, connected via the High-Density pins.

***When properly configured, the combined Portenta C33 and Portenta UWB Shield function as a <strong>UWB anchor node</strong> in a positioning system. This anchor can receive signals from UWB tags (mobile devices with UWB capability), precisely calculate their distance using time-of-flight principles, and when used in a network of anchors, determine their exact position in space.***

### Connecting the Shield

The Portenta UWB Shield is designed to be connected directly to a Portenta C33 board through its High-Density connectors, as shown in the animation below:

![Connecting the the Portenta UWB Shield](assets/user-manual-5.gif)

To connect the shield to the board, align first the shield's High-Density connectors with those on the Portenta C33 board. Then, gently press the shield onto the Portenta C33 until it is firmly seated.

***<strong>Important note:</strong> Ensure that the Portenta C33 is powered off before connecting or disconnecting the shield to prevent potential damage to either of the boards.***

### Powering the Shield

The Portenta UWB Shield is powered exclusively through the `VCC` pins (+3.3 VDC) of its High-Density Connectors. These connectors are designed to be used with boards from the Portenta family, such as the Portenta C33 board. The power is supplied directly from the connected Portenta family board, which acts as the power source for the Portenta UWB Shield.

***<strong>Important note:</strong> The Portenta UWB Shield does not have an independent power input. It receives power only through the High-Density connectors when properly connected to a Portenta C33 board.***

### Nearby World Example

Let's use the Portenta UWB Shield with the Portenta C33 to create a real-time distance measurement system using UWB technology. We will implement what we call the `Nearby World` example (based on the `NearbyDemo` sketch), which serves as our `Hello World` sketch for UWB technology. This example will verify the Portenta UWB Shield's connection to the host board, the host board's connection to the Arduino IDE and that the `ardUWBSr150` library and both boards are working as expected.

***This example sketch leverages Apple's Nearby Interaction protocol and similar UWB implementations on Android devices to establish a communication channel between the Portenta UWB Shield and a UWB-enabled smartphone, allowing precise distance and angle measurements.***

#### How it Works

The `Nearby World` example demonstrates the core functionality of UWB technology through a simple example sketch that can be described in the following key steps:

1. **BLE connection setup**: The Portenta UWB Shield establishes a Bluetooth Low Energy (BLE) connection with a compatible smartphone app.
2. **Configuration exchange**: The BLE connection is used to exchange necessary UWB configuration parameters.
3. **UWB ranging**: Once configured, the actual UWB ranging session begins, providing precise distance measurements.
4. **Real-time feedback**: Distance data is continuously updated and can be viewed both on the IDE's Serial Monitor and on the smartphone app.

This process demonstrates the working principle of many UWB applications, where BLE is used primarily for discovery and configuration, while UWB handles the precise ranging.

#### Uploading the Sketch

First, connect the Portenta UWB Shield to the Portenta C33 as described in the [Connecting the Shield section](#connecting-the-shield). Now, connect the Portenta C33 to your computer using a USB-C® cable, open the Arduino IDE and connect the board to it.

***If you are new to the Portenta C33, please refer to the board's [user manual](https://docs.arduino.cc/tutorials/portenta-c33/user-manual/) for more detailed information.***

Copy and paste the example sketch below into a new sketch in the Arduino IDE:

```arduino 
/**
  Nearby Demo Example for Portenta UWB Shield
  Name: portenta_uwb_nearby.ino
  Purpose: This sketch demonstrates how to use the Portenta UWB Shield
  to measure distance between the shield and a UWB-enabled smartphone.
  
  @author Pierpaolo Lento from Truesense, modified by the Arduino Product Experience Team
  @version 1.0 15/04/25
*/

// Include required libraries
#include <ArduinoBLE.h>
#include <ardUWBSr150.h>

// Track the number of connected BLE clients
uint16_t numConnected = 0;

/**
  Processes ranging data received from UWB communication.
  @param rangingData Reference to UWB ranging data object.
*/
void rangingHandler(UWBRangingData &rangingData) {
  Serial.print("- GOT RANGING DATA - Type: ");
  Serial.println(rangingData.measureType());
  
  // Nearby interaction uses Double-sided Two-way Ranging method
  if(rangingData.measureType()==MEASUREMENT_TYPE_TWOWAY) {
    // Get the TWR (Two-Way Ranging) measurements
    RangingMeasures twr = rangingData.twoWayRangingMeasure();
    
    // Loop through all available measurements
    for(int j=0; j<rangingData.available(); j++) {
      // Only process valid measurements
      if(twr[j].status==0 && twr[j].distance!=0xFFFF) {
        // Display the distance measurement in millimeters
        Serial.print("- Distance: ");
        Serial.println(twr[j].distance);
      }
    }
  }
}

/**
  Handles new BLE client connection events.
  @param dev The connecting BLE device.
*/
void clientConnected(BLEDevice dev) {
  // Initialize UWB stack on first connection
  if (numConnected == 0) {
    // Start the UWB engine
    UWB.begin(); 
  }
  // Increment connected clients counter
  numConnected++;
}

/**
  Handles BLE client disconnection events.
  @param dev The disconnecting BLE device.
*/
void clientDisconnected(BLEDevice dev) {
  // Decrement connected clients counter
  numConnected--;
  // Shut down UWB when no clients are connected
  if(numConnected==0) {
    UWB.end();
  }
}

/**
  Handles UWB session start events.
  @param dev The BLE device starting the session.
*/
void sessionStarted(BLEDevice dev) {
  Serial.println("- Session started!");
}

/**
  Handles UWB session termination events.
  @param dev The BLE device ending the session.
*/
void sessionStopped(BLEDevice dev) {
  Serial.println("- Session stopped!");
}

void setup() {
  // Initialize serial communication at 115200 bits per second
  Serial.begin(115200);
  
  // On the Portenta C33, initialize the onboard RGB LED
  #if defined(ARDUINO_PORTENTA_C33)
    pinMode(LEDR, OUTPUT);
    digitalWrite(LEDR, LOW);
  #endif

  Serial.println("- Nearby interaction app start...");
  
  // Register callback handlers
  UWB.registerRangingCallback(rangingHandler);
  UWBNearbySessionManager.onConnect(clientConnected);
  UWBNearbySessionManager.onDisconnect(clientDisconnected);
  UWBNearbySessionManager.onSessionStart(sessionStarted);
  UWBNearbySessionManager.onSessionStop(sessionStopped);
  
  // Initialize BLE services and start advertising as "Portenta UWB Shield"
  UWBNearbySessionManager.begin("Portenta UWB Shield");
}

void loop() {
  // Small delay to prevent CPU overload
  delay(100);
  
  // Process BLE events
  UWBNearbySessionManager.poll();
}
```

To upload the sketch to the Portenta C33, click the Verify button to compile the sketch and check for errors, then click the Upload button to program the device with the sketch.

![Uploading a sketch to the Portenta C33 board in the Arduino IDE](assets/user-manual-6.png)

Once the sketch is uploaded, open the Serial Monitor by clicking on the icon in the top right corner of the Arduino IDE. You should see the message `- Nearby interaction app start...` in the IDE's Serial Monitor.

![Arduino IDE Serial monitor](assets/user-manual-7.png)

#### Try it Yourself

To complete the test, you will need an UWB-enabled smartphone with one of the compatible applications installed:

**For iPhone (iPhone 11 or newer with UWB capability):**

- [NXP Trimensions AR](https://apps.apple.com/us/app/nxp-trimensions-ar/id1606143205)
- [Qorvo Nearby Interaction](https://apps.apple.com/us/app/qorvo-nearby-interaction/id1615369084)

**For Android (UWB-enabled Android devices):**

- [Truesense Android demo](https://github.com/Truesense-it/TSUwbDemo-Android) (recommended)
- [NXP Android demo](https://github.com/nxp-uwb/UWBJetpackExample)

***<strong>Important note for Android devices:</strong> It is recommended to enable Developer Mode to ensure proper UWB functionality. To activate Developer Mode, go to Settings > About phone and tap "Build number" seven times. Some UWB features may require additional developer permissions that can be granted through this menu.***

Install one of these apps on your smartphone and follow these steps:

1. Open the app on your smartphone.
2. Look for a device named `Portenta UWB Shield` in the app's device list.
3. Connect to the device.
4. Once connected, the app will begin an UWB ranging session.
5. Move your phone closer to and further from the Portenta UWB Shield.

You should see the distance measurements updating in real-time both on your smartphone app and in the IDE's Serial Monitor. The distances are shown in millimeters, providing centimeter-level accuracy characteristic of the UWB technology.

![Distance measurements from the Portenta UWB Shield to the smartphone](assets/user-manual-8.png)

## NearbyDemo Example

### About the NearbyDemo Example

The NearbyDemo example sketch is a fundamental demonstration of the Portenta UWB Shield's core capabilities. This example showcases how to implement a direct distance measurement system between a stationary UWB device (the Portenta UWB Shield, acting as an UWB anchor) and a mobile UWB device (the UWB-enabled smartphone, acting as an UWB tag).

This example sketch demonstrates the following:

- **Hybrid communication protocol:** It shows the integration of BLE for device discovery and configuration with UWB for precise distance measurements, a common pattern in production UWB applications.
- **Standards compatibility:** The implementation is compatible with Apple's Nearby Interaction API and similar Android standards, demonstrating how the Arduino ecosystem can interact with mainstream consumer devices.
- **Foundation for advanced applications:**: The ranging capability demonstrated is the building block for more sophisticated applications such as indoor positioning systems, geofencing, secure access and proximity-based automation.

Some of the real-life applications for this example sketch are the following:

- **Industrial automation:** Creating safety zones around machinery that can detect when workers approach with centimeter precision.
- **Smart buildings:** Enabling location-aware services within facilities where GPS is unavailable.
- **Healthcare:** Tracking the movement of patients, staff and equipment with high accuracy.
- **Retail:** Implementing contactless payment systems with a higher degree of security than current NFC solutions.
- **Consumer electronics:** Enabling precise "Find My Device" features and spatial awareness between gadgets.

Now, let's take a closer look at the sketch:

```arduino
/**
  Nearby Demo Example for Portenta UWB Shield
  Name: portenta_uwb_nearby.ino
  Purpose: This sketch demonstrates how to use the Portenta UWB Shield
  to measure distance between the shield and an UWB-enabled smartphone.
  
  @author Pierpaolo Lento from Truesense, modified by the Arduino Product Experience Team
  @version 1.0 15/04/25
*/

// Include required libraries
#include <ArduinoBLE.h>
#include <ardUWBSr150.h>

// Track the number of connected BLE clients
uint16_t numConnected = 0;

/**
  Processes ranging data received from UWB communication.
  @param rangingData Reference to UWB ranging data object.
*/
void rangingHandler(UWBRangingData &rangingData) {
  Serial.print("- GOT RANGING DATA - Type: ");
  Serial.println(rangingData.measureType());
  
  // Nearby interaction uses Double-sided Two-way Ranging method
  if(rangingData.measureType()==MEASUREMENT_TYPE_TWOWAY) {
    // Get the TWR (Two-Way Ranging) measurements
    RangingMeasures twr = rangingData.twoWayRangingMeasure();
    
    // Loop through all available measurements
    for(int j=0; j<rangingData.available(); j++) {
      // Only process valid measurements
      if(twr[j].status==0 && twr[j].distance!=0xFFFF) {
        // Display the distance measurement in millimeters
        Serial.print("- Distance: ");
        Serial.println(twr[j].distance);
      }
    }
  }
}

/**
  Handles new BLE client connection events.
  @param dev The connecting BLE device.
*/
void clientConnected(BLEDevice dev) {
  // Initialize UWB stack on first connection
  if (numConnected == 0) {
    // Start the UWB engine
    UWB.begin(); 
  }
  // Increment connected clients counter
  numConnected++;
}

/**
  Handles BLE client disconnection events.
  @param dev The disconnecting BLE device.
*/
void clientDisconnected(BLEDevice dev) {
  // Decrement connected clients counter
  numConnected--;
  // Shut down UWB when no clients are connected
  if(numConnected==0) {
    UWB.end();
  }
}

/**
  Handles UWB session start events.
  @param dev The BLE device starting the session.
*/
void sessionStarted(BLEDevice dev) {
  Serial.println("- Session started!");
}

/**
  Handles UWB session termination events.
  @param dev The BLE device ending the session.
*/
void sessionStopped(BLEDevice dev) {
  Serial.println("- Session stopped!");
}

void setup() {
  // Initialize serial communication at 115200 bits per second
  Serial.begin(115200);
  
  // On the Portenta C33, initialize the onboard RGB LED
  #if defined(ARDUINO_PORTENTA_C33)
    pinMode(LEDR, OUTPUT);
    digitalWrite(LEDR, LOW);
  #endif

  Serial.println("- Nearby interaction app start...");
  
  // Register callback handlers
  UWB.registerRangingCallback(rangingHandler);
  UWBNearbySessionManager.onConnect(clientConnected);
  UWBNearbySessionManager.onDisconnect(clientDisconnected);
  UWBNearbySessionManager.onSessionStart(sessionStarted);
  UWBNearbySessionManager.onSessionStop(sessionStopped);
  
  // Initialize BLE services and start advertising as "Portenta UWB Shield"
  UWBNearbySessionManager.begin("Portenta UWB Shield");
}

void loop() {
  // Small delay to prevent CPU overload
  delay(100);
  
  // Process BLE events
  UWBNearbySessionManager.poll();
}
```

### Key Components of the Example Sketch

The `NearbyDemo` code follows an event-driven architecture that employs callback functions to handle various events in the UWB communication process. Here is an explanation of the most important parts of the example sketch:

1. **Libraries and Global Variables**
   
```arduino
#include <ArduinoBLE.h>
#include <ardUWBSr150.h>

uint16_t numConnected = 0;
```

The code includes two essential libraries:

- `ArduinoBLE`: Provides Bluetooth Low Energy functionality for device discovery and initial connection.
- `ardUWBSr150`: The core library that enables interaction with the UWB hardware on the Portenta UWB Shield.

The `numConnected` variable tracks how many BLE clients are currently connected to the Portenta UWB Shield.

2. **Ranging Data Handler**

```arduino
void rangingHandler(UWBRangingData &rangingData) {
  // ...
  if(rangingData.measureType()==MEASUREMENT_TYPE_TWOWAY) {
    RangingMeasures twr = rangingData.twoWayRangingMeasure();
    // ...
    if(twr[j].status==0 && twr[j].distance!=0xFFFF) {
      Serial.print("- Distance: ");
      Serial.println(twr[j].distance);
    }
  }
}
```

This callback function is the heart of the UWB functionality:

- It's triggered whenever new ranging data is received from the UWB subsystem.
- It checks if the measurement type is Two-Way Ranging (TWR), which is the method used by Apple's Nearby Interaction protocol.
- It extracts the distance measurements in millimeters and prints them to the IDE's Serial Monitor-
- It validates the measurement (`status = 0` indicates a valid measurement, while `distance = 0xFFFF` is a reserved value indicating an invalid distance).

3. **Connection Management**

```arduino
void clientConnected(BLEDevice dev) {
  if (numConnected == 0) {
    UWB.begin(); 
  }
  numConnected++;
}

void clientDisconnected(BLEDevice dev) {
  numConnected--;
  if(numConnected==0) {
    UWB.end();
  }
}
```

These functions handle BLE connection events:

- `clientConnected` initializes the UWB subsystem when the first client connects.
- `clientDisconnected` shuts down the UWB subsystem when no clients are connected.

This approach saves power by only running the shield's UWB hardware when it's actually needed.

4. **Session Management**

```arduino
void sessionStarted(BLEDevice dev) {
  Serial.println("- Session started!");
}

void sessionStopped(BLEDevice dev) {
  Serial.println("- Session stopped!");
}
```

These callbacks track the UWB session state:

- A session begins after the BLE connection is established and the UWB configuration is exchanged.
- A session ends when the UWB communication is terminated, either by the client disconnecting or other factors.

5. **Setup and Initialization**

```arduino
void setup() {
  // ...
  UWB.registerRangingCallback(rangingHandler);
  UWBNearbySessionManager.onConnect(clientConnected);
  UWBNearbySessionManager.onDisconnect(clientDisconnected);
  UWBNearbySessionManager.onSessionStart(sessionStarted);
  UWBNearbySessionManager.onSessionStop(sessionStopped);
  
  UWBNearbySessionManager.begin("Portenta UWB Shield");
}
```

The setup function:

- Registers all the callback functions with the UWB subsystem.
- Initializes the BLE advertising with the name `Portenta UWB Shield`. This name is what will appear in the smartphone app's device list.

6. **Main Loop**

```arduino
void loop() {
  delay(100);
  UWBNearbySessionManager.poll();
}
```

The main loop is quite simple:

- It calls the `UWBNearbySessionManager.poll()` function to process BLE events.
- The actual UWB ranging happens asynchronously through the callback system.
  
This event-driven architecture allows the system to respond quickly to UWB and BLE events without blocking the main program flow.

### Extending the Example Sketch

The `NearbyDemo` example sketch provides a great foundation that you can build upon for more complex projects. Some possible extensions of this sketch include the following:

- **Adding visual feedback:** Using LEDs or displays to indicate distance ranges.
- **Implementing proximity alerts:** Triggering actions when devices come within a certain distance.
- **Data logging:** Recording distance measurements for analysis and visualization.
- **Integrating with other sensors:** Combining UWB data with other environmental sensors for context-aware applications.

***<strong>Note:</strong> If you want to try this example yourself, please follow the same steps described in the [Nearby World Example](#nearby-world-example) section. The process for uploading the sketch and testing it with a smartphone is the same.***

## Support

If you encounter any issues or have questions while working with your Portenta UWB Shield, we provide various support resources to help you find answers and solutions.

### Help Center

Explore our Help Center, which offers a comprehensive collection of articles and guides for the Portenta family boards and shields. The Help Center is designed to provide in-depth technical assistance and help you make the most of your device.

  - [Portenta family help center page](https://support.arduino.cc/hc/en-us/sections/360004767859-Portenta-Family)

### Forum

Join our community forum to connect with other Nicla family board users, share your experiences, and ask questions. The Forum is an excellent place to learn from others, discuss issues, and discover new ideas and projects related to the Portenta UWB Shield.

- [Portenta UWB shield in the Arduino Forum](https://forum.arduino.cc/c/official-hardware/portenta-family/91)

### Contact Us

Please get in touch with our support team if you need personalized assistance or have questions not covered by the help and support resources described before. We're happy to help you with any issues or inquiries about the Portenta family boards and shields.

- [Contact us page](https://www.arduino.cc/en/contact-us/)