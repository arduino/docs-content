---
title: 'Arduino Stella User Manual'
difficulty: intermediate
compatible-products: [arduino-stella]
description: 'Learn about the hardware and software features of the Arduino® Stella.'
tags:
  - UWB
  - Positioning
  - Real-time location
  - Sensors
  - User manual
author: 'José Bagur'
hardware:
  - hardware/06.portenta/boards/arduino-stella
software:
  - ide-v2
---

This user manual provides a comprehensive overview of the Stella, highlighting its hardware and software elements. With it, you will learn how to set up, configure and use all the main features of the Stella.

![ ](assets/hero-banner.png)

## Hardware and Software Requirements

### Hardware Requirements

- [Arduino Stella (SKU: ABX00131)](https://store.arduino.cc/products/arduino-stella) (x1)
- [Portenta UWB Shield (SKU: ASX00074)](https://store.arduino.cc/products/portenta-uwb-shield) (x1)
- [Portenta C33 (SKU: ABX00074)](https://store.arduino.cc/products/portenta-c33) (x1)
- [USB-C® cable (SKU: TPX00094)](https://store.arduino.cc/products/usb-cable2in1-type-c) (x2)
- CR2032 battery (x1) (optional)

### Software Requirements

- [Arduino IDE 2.0+](https://www.arduino.cc/en/software)
- ardUWBSr040 library
- [Arduino mbed OS Boards core](https://github.com/arduino/ArduinoCore-mbed) (required for the nRF52840 microcontroller of the Stella)

## Arduino Stella Overview

The Stella redefines location tracking with its advanced microcontroller, the nRF52840 from Nordic Semiconductor, and the DCU040 Ultra-Wide Band (UWB) module from Truesense. Tailored for modern tracking needs, the Stella excels in pinpointing warehouse assets, ensuring healthcare safety and automating smart buildings. Seamlessly integrating with the Portenta UWB Shield and UWB-enabled smartphones through the dedicated NXP® Trimension App, Apple's Nearby Interaction APIs or Android's UWB Jetpack library, the Stella delivers robust finder functionality, precise point-to-point triggering and comprehensive tracking capabilities for applications demanding reliable, real-time location data.

### Understanding UWB Technology

UWB is a radio technology that uses very low energy levels for short-range, high-bandwidth communications over a large portion of the radio spectrum. Unlike traditional narrow-band radio systems, like Bluetooth® or Wi-Fi®, UWB transmits across a wide range of frequency bands (typically 500 MHz or more) operating in the 6.0-8.5 GHz frequency range.

Some of the key characteristics of UWB are the following:

- **High precision**: UWB can determine the relative position of devices with centimeter-level accuracy (typically 5-10 cm), far more precise than GPS, Bluetooth® or Wi-Fi®.
- **Low-power consumption**: Despite its high data rates, UWB consumes very little power, making it suitable for battery-operated devices.
- **Short range**: Typically effective within 10-30 meters, making it ideal for indoor positioning applications.
- **Strong security**: The unique physical layer characteristics of UWB make it more resistant to relay attacks compared to other wireless technologies.

So, how does UWB technology work?

UWB uses a technique called "Time of Flight" (ToF) or "Time Difference of Arrival" (TDoA) to determine the distance between UWB-enabled devices. In a nutshell, this technique consists of the following steps:

1. An UWB transmitter sends a signal with a precise timestamp.
2. An UWB receiver detects the signal and calculates the time it took to arrive.
3. Since radio waves travel at the speed of light (approximately 30 cm per nanosecond), the system can calculate the distance with high precision.

***<strong>Important note:</strong> UWB operates in specific frequency bands regulated by authorities worldwide. The Portenta UWB Shield specifically uses channels in the 6.0 to 8.5 GHz range (channels CH5 and CH9), allowing for high bandwidth communication while minimizing interference with other wireless technologies.***

For even greater accuracy, UWB can use the "Two-Way Ranging" (TWR) technique, where devices exchange several messages to account for clock synchronization issues. The Angle of Arrival (AoA) capability enhances positioning by not only determining distance but also the angle from which a signal arrives, enabling with this more accurate 2D or 3D positioning.

In an UWB positioning system, devices typically operate in one of two roles:

- **Anchors**: Fixed-position devices (like the Portenta UWB Shield with a Portenta C33) that provide reference points for the positioning system.
- **Tags**: Mobile devices that communicate with anchors to determine their position in space. The Stella is designed to function as a tag in UWB positioning systems.

Some of the key applications of UWB technology are the following:

- **Asset tracking**: Monitor the location of valuable items in warehouses, hospitals or construction sites.
- **Secure access**: Contactless entry systems that unlock only when an authorized device is in proximity.
- **Precision navigation**: Guide robots, vehicles or drones in environments where GPS is unavailable.
- **Social distancing**: Measure precise distances between individuals in workplaces or public venues.

### Stella Architecture Overview

The Stella features a secure, certified and durable design that suits various applications, such as asset tracking, healthcare monitoring, smart building automation and consumer applications.

The top view of the Stella is shown in the image below:

![The Stella's main components (top view)](assets/user-manual-1.png)

The bottom view of the Arduino Stella is shown in the image below:

![The Stella's main components (bottom view)](assets/user-manual-2.png)

Here's an overview of the board's main components shown in the images:

- **Microcontroller**: At the heart of the Stella is the nRF52840 microcontroller from Nordic Semiconductor. This powerful 32-bit ARM Cortex-M4 processor runs at 64 MHz and features 1 MB Flash and 256 kB RAM, providing ample processing power and memory for sophisticated applications.
- **UWB Module**: The Truesense DCU040 module (based on the NXP Trimension SR040 UWB IC) enables precise distance measurement with accuracy better than ±10 cm using two-way ranging techniques.
- **Connectivity**: Besides UWB, the Stella includes Bluetooth 5.0 connectivity through the nRF52840's integrated radio, supporting IEEE 802.15.4-2006 and 2.4 GHz transceiver capabilities.
- **Accelerometer**: A 3-axis MEMS digital output accelerometer (SC7A20) enhances the board's motion detection capabilities, with programmable sensitivity ranges of ±2G/±4G/±8G/±16G and features like orientation detection, free-fall detection, and click detection.
- **User interfaces**: The board includes a user-programmable button, a user-programmable LED and a buzzer (FUET-5020) that can be used for audible alerts.
- **Connectors**: The Stella features a USB-C® port for power and data, a QWIIC connector for I²C expansion, a CR2032 battery holder and a J-Link connector for debugging and alternative power input.

### Board Libraries

The Arduino Stella and Portenta UWB Shield use different libraries and board cores due to their different microcontrollers and UWB modules:

#### Arduino Stella Library

The [`ardUWBSr040` library](https://github.com/arduino-libraries/ardUWBSr040) contains an application programming interface (API) to read data from the Stella and control its parameters and behavior. This library is designed to work with the DCU040 module on the Stella and supports the following:

- One-way ranging (Time Difference of Arrival - TDoA) and two-way ranging (TWR).
- Power management for battery-efficient operation.
- Accelerometer control for motion detection.
- BLE connectivity for configuration and communication.

***The [Arduino mbed OS Boards core](https://github.com/arduino/ArduinoCore-mbed) is required to work with the Stella's nRF52840 microcontroller.***

#### Portenta UWB Shield Library

If you plan to use the Stella with a Portenta UWB Shield for two-way ranging experiments, you'll also need the [`ardUWBSr150` library](https://github.com/arduino-libraries/ardUWBSr150) for the Portenta UWB Shield. This library is specifically designed for the DCU150 module used in the shield.

***The [Arduino Renesas Portenta Boards core](https://github.com/arduino/ArduinoCore-renesas) is required to work with the Portenta C33 board that hosts the UWB Shield.***

#### Bluetooth Communication

For examples that use Bluetooth Low Energy (BLE) communication, you'll also need the [`ArduinoBLE` library](https://github.com/arduino/ArduinoBLE). This library enables BLE functionality for device discovery and initial connection setup before UWB ranging begins.

#### Installing the Libraries and Board Cores

To install the required libraries:

1. Navigate to `Tools > Manage libraries...` or click the **Library Manager** icon in the left tab of the Arduino IDE.
2. In the Library Manager tab, search for the library name (`ardUWBSr040`, `ardUWBSr150`, or `ArduinoBLE`).
3. Click "Install" to install the latest version of each library.

![Installing the board's library in the Arduino IDE](assets/user-manual-3.png)

To install the required board cores:

1. Navigate to `Tools > Board > Boards Manager...`
2. For the Arduino Stella: Search for "Arduino mbed OS Boards" and install the latest version.
3. For the Portenta C33: Search for "Arduino Renesas Boards" and install the latest version.

***<strong>Important note:</strong> Make sure to install both the appropriate library and board core for your specific hardware. The Arduino Stella requires the `ardUWBSr040` library and Arduino mbed OS Boards core, while the Portenta UWB Shield with Portenta C33 requires the `ardUWBSr150` library and Arduino Renesas Boards core. For examples involving BLE communication, both devices will need the `ArduinoBLE` library installed.***

### Pinout

The full pinout is available and downloadable as PDF from the link below:

- [Stella pinout](https://docs.arduino.cc/resources/pinouts/ABX00131-full-pinout.pdf)

### Datasheet

The complete datasheet is available and downloadable as PDF from the link below:

- [Stella datasheet](https://docs.arduino.cc/resources/datasheets/ABX00131-datasheet.pdf)

### Schematics

The complete schematics are available and downloadable as PDF from the link below:

- [Stella schematics](https://docs.arduino.cc/resources/schematics/ABX00131-schematics.pdf)

### STEP Files 

The complete STEP files are available and downloadable from the link below:

- [Stella STEP files](../../downloads/ABX00131-step.zip)

## First Use

### Unboxing the Product

When you open the box of the Stella, you will find the board itself with its distinctive octagonal shape, featuring a USB-C® port on one edge. The Stella is a compact board with dimensions of 38 mm x 38 mm, designed to be easily integrated into various tracking applications.

![Unboxing the Stella](assets/user-manual-4.png)

The Stella comes ready to use, but you may want to add a CR2032 battery if you plan to use it in portable applications that require battery power.

### Powering the Board

The Stella can be powered through one of these interfaces:

- **USB-C® port**: The simplest way to power the Stella is through its onboard USB-C® port.
- **+3 VDC battery**: For portable applications, you can use the onboard CR2032 battery holder.
- **J-Link connector**: The Stella can also be powered through the board's J-Link connector, primarily used for debugging purposes.

![Powering options for the Stella](assets/user-manual-5.png)

***<strong>Important note:</strong> When using battery power, ensure the correct polarity when inserting the CR2032 battery into the holder. The positive (+) side should face up, away from the PCB.***

### Connecting to Your Computer

To program the Stella, connect it to your computer using a USB-C® cable:

1. Insert the USB-C® connector into the port on the Stella.
2. Connect the other end to an available USB port on your computer.

![Connecting the Arduino Stella to your computer](assets/user-manual-6.png)

Once connected, you should see a power indicator light up on the board, indicating it's receiving power from the USB port.

## Nearby World Example

Let's use the Stella to create a real-time distance measurement system using UWB technology. We will implement what we call the `Nearby World` example, which serves as our `Hello World` sketch for UWB technology. This example will verify the Stella's UWB capabilities and its ability to communicate with UWB-enabled smartphones.

***This example sketch leverages Apple's Nearby Interaction protocol and similar UWB implementations on Android devices to establish a communication channel between the Stella and a UWB-enabled smartphone, allowing precise distance and angle measurements.***

#### How it Works

The `Nearby World` example demonstrates the core functionality of UWB technology through a simple example sketch that can be described in the following key steps:

1. **BLE connection setup**: The Stella broadcasts using Bluetooth® Low Energy (BLE) to make itself discoverable to compatible smartphone apps.
2. **Configuration exchange**: The BLE connection is used to exchange necessary UWB configuration parameters between the Stella and the smartphone.
3. **UWB ranging**: Once configured, the actual UWB ranging session begins, providing precise distance measurements.
4. **Real-time feedback**: Distance data is continuously updated and can be viewed both on the IDE's Serial Monitor and on the smartphone app. The Stella's buzzer and LED can also provide feedback based on distance.

This process demonstrates the working principle of many UWB applications, where BLE is used primarily for discovery and configuration, while UWB handles the precise ranging.

#### Uploading the Sketch

First, connect the Stella to your computer using a USB-C® cable, open the Arduino IDE and connect the board to it.

***If you are new to the Stella, ensure you have installed the required board support package by going to Tools > Board > Boards Manager and searching for "mbed OS Boards".***

Copy and paste the example sketch below into a new sketch in the Arduino IDE:

```arduino 
/**
  Nearby World Example for Arduino Stella
  Name: arduino_stella_nearby.ino
  Purpose: This sketch demonstrates how to use the Arduino Stella
  to measure distance between the board and a UWB-enabled smartphone.
  
  @author Arduino Product Experience Team
  @version 1.0 15/04/25
*/

// Include required libraries
#include <ArduinoBLE.h>
#include <ArduinoStella.h>

// Track the number of connected BLE clients
uint16_t numConnected = 0;

// Buzzer activation thresholds (in mm)
#define PROXIMITY_CLOSE 500     // 50cm
#define PROXIMITY_MEDIUM 1500   // 1.5m
#define PROXIMITY_FAR 3000      // 3m

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
        
        // Provide feedback based on distance
        provideFeedback(twr[j].distance);
      }
    }
  }
}

/**
  Provides audio and visual feedback based on distance.
  @param distance The measured distance in millimeters.
*/
void provideFeedback(uint32_t distance) {
  // LED pattern based on distance
  if (distance < PROXIMITY_CLOSE) {
    // Fast blinking for close proximity
    digitalWrite(LED_BUILTIN, HIGH);
    // Short beep for close proximity
    buzzer.beep(50);
    delay(50);
    digitalWrite(LED_BUILTIN, LOW);
  } 
  else if (distance < PROXIMITY_MEDIUM) {
    // Medium pace blinking for medium proximity
    digitalWrite(LED_BUILTIN, HIGH);
    delay(200);
    digitalWrite(LED_BUILTIN, LOW);
  }
  else if (distance < PROXIMITY_FAR) {
    // Slow blinking for far proximity
    digitalWrite(LED_BUILTIN, HIGH);
    delay(500);
    digitalWrite(LED_BUILTIN, LOW);
  }
  else {
    // Very slow pulsing for very distant objects
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000);
    digitalWrite(LED_BUILTIN, LOW);
  }
  
  // Ensure delay between feedback cycles
  delay(100);
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
  Serial.println("- Client connected!");
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
  Serial.println("- Client disconnected!");
}

/**
  Handles UWB session start events.
  @param dev The BLE device starting the session.
*/
void sessionStarted(BLEDevice dev) {
  Serial.println("- Session started!");
  // Beep once to indicate session start
  buzzer.beep(200);
}

/**
  Handles UWB session termination events.
  @param dev The BLE device ending the session.
*/
void sessionStopped(BLEDevice dev) {
  Serial.println("- Session stopped!");
  // Beep twice to indicate session end
  buzzer.beep(100);
  delay(100);
  buzzer.beep(100);
}

void setup() {
  // Initialize serial communication at 115200 bits per second
  Serial.begin(115200);
  
  // Initialize the onboard LED
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
  
  // Initialize the accelerometer
  if (!accelerometer.begin()) {
    Serial.println("- Failed to initialize accelerometer!");
  }
  
  // Initialize the buzzer
  buzzer.begin();

  Serial.println("- Nearby interaction app start...");
  
  // Register callback handlers
  UWB.registerRangingCallback(rangingHandler);
  UWBNearbySessionManager.onConnect(clientConnected);
  UWBNearbySessionManager.onDisconnect(clientDisconnected);
  UWBNearbySessionManager.onSessionStart(sessionStarted);
  UWBNearbySessionManager.onSessionStop(sessionStopped);
  
  // Initialize BLE services and start advertising as "Arduino Stella"
  UWBNearbySessionManager.begin("Arduino Stella");
  
  // Beep three times to indicate setup complete
  for (int i = 0; i < 3; i++) {
    buzzer.beep(50);
    delay(50);
  }
}

void loop() {
  // Small delay to prevent CPU overload
  delay(100);
  
  // Process BLE events
  UWBNearbySessionManager.poll();
}
```

To upload the sketch to the Stella, click the Verify button to compile the sketch and check for errors, then click the Upload button to program the device with the sketch.

![Uploading a sketch to the Stella in the Arduino IDE](assets/user-manual-7.png)

Once the sketch is uploaded, open the Serial Monitor by clicking on the icon in the top right corner of the Arduino IDE. You should see the message `- Nearby interaction app start...` in the IDE's Serial Monitor, followed by three short beeps from the Stella's buzzer.

![Arduino IDE Serial Monitor](assets/user-manual-8.png)

#### Try it Yourself

To complete the test, you will need a UWB-enabled smartphone with one of the compatible applications installed:

**For iPhone (iPhone 11 or newer with UWB capability):**

- [NXP Trimensions AR](https://apps.apple.com/us/app/nxp-trimensions-ar/id1606143205)
- [Qorvo Nearby Interaction](https://apps.apple.com/us/app/qorvo-nearby-interaction/id1615369084)

**For Android (UWB-enabled Android devices):**

- [Truesense Android demo](https://github.com/Truesense-it/TSUwbDemo-Android) (recommended)
- [NXP Android demo](https://github.com/nxp-uwb/UWBJetpackExample)

***<strong>Important note for Android devices:</strong> It is recommended to enable Developer Mode to ensure proper UWB functionality. To activate Developer Mode, go to Settings > About phone and tap "Build number" seven times. Some UWB features may require additional developer permissions that can be granted through this menu.***

Install one of these apps on your smartphone and follow these steps:

1. Open the app on your smartphone.
2. Look for a device named `Arduino Stella` in the app's device list.
3. Connect to the device.
4. Once connected, the app will initiate a UWB ranging session, and you'll hear a single beep from the Stella.
5. Move your phone closer to and further from the Arduino Stella.

You should see the distance measurements updating in real-time both on your smartphone app and in the IDE's Serial Monitor. The distances are shown in millimeters, providing centimeter-level accuracy characteristic of UWB technology. Additionally, the Stella's LED and buzzer will provide feedback based on the measured distance, with more frequent responses as you get closer to the device.

![Distance measurements from the Stella to the smartphone](assets/user-manual-9.png)

## NearbyDemo Example

### About the NearbyDemo Example

The NearbyDemo example sketch is a fundamental demonstration of the Stella's core capabilities. This example showcases how to implement a direct distance measurement system between the Stella (acting as a UWB tag) and a UWB-enabled smartphone (acting as a UWB anchor).

This example sketch demonstrates the following:

- **Hybrid communication protocol:** It shows the integration of BLE for device discovery and configuration with UWB for precise distance measurements, a common pattern in production UWB applications.
- **Standards compatibility:** The implementation is compatible with Apple's Nearby Interaction API and similar Android standards, demonstrating how the Arduino ecosystem can interact with mainstream consumer devices.
- **Foundation for advanced applications:** The ranging capability demonstrated is the building block for more sophisticated applications such as indoor positioning systems, geofencing, secure access and proximity-based automation.

Some of the real-life applications for this example sketch are the following:

- **Asset tracking:** Creating systems where Stella boards attached to valuable items can be precisely located within warehouses or facilities.
- **Smart building automation:** Implementing room-level presence detection that can adjust lighting, temperature, and other environmental factors based on the location of people wearing or carrying Stella devices.
- **Healthcare:** Tracking the movement of patients, staff, and medical equipment with high accuracy within hospital environments.
- **Retail analytics:** Analyzing customer movement patterns in stores to optimize layout and product placement.
- **Consumer item finding:** Creating tag-based systems that allow users to precisely locate misplaced items through smartphone interactions.

Now, let's take a closer look at the sketch:

```arduino
/**
  NearbyDemo Example for Arduino Stella
  Name: arduino_stella_nearbydemo.ino
  Purpose: This sketch demonstrates how to use the Arduino Stella
  to measure distance between the board and a UWB-enabled device.
  
  @author Arduino Product Experience Team
  @version 1.0 15/04/25
*/

// Include required libraries
#include <ArduinoBLE.h>
#include <ardUWBSr040.h>

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
  
  // Initialize the onboard LED
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  Serial.println("- Nearby interaction app start...");
  
  // Register callback handlers
  UWB.registerRangingCallback(rangingHandler);
  UWBNearbySessionManager.onConnect(clientConnected);
  UWBNearbySessionManager.onDisconnect(clientDisconnected);
  UWBNearbySessionManager.onSessionStart(sessionStarted);
  UWBNearbySessionManager.onSessionStop(sessionStopped);
  
  // Initialize BLE services and start advertising as "Arduino Stella"
  UWBNearbySessionManager.begin("Arduino Stella");
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
#include <ArduinoStella.h>

uint16_t numConnected = 0;
```

The code includes two essential libraries:

- `ArduinoBLE`: Provides Bluetooth Low Energy functionality for device discovery and initial connection.
- `ArduinoStella`: The core library that enables interaction with the UWB hardware on the Stella.

The `numConnected` variable tracks how many BLE clients are currently connected to the Stella.

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
- It extracts the distance measurements in millimeters and prints them to the IDE's Serial Monitor.
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

This approach saves power by only running the board's UWB hardware when it's actually needed, which is crucial for battery-powered applications.

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
  
  UWBNearbySessionManager.begin("Arduino Stella");
}
```

The setup function:

- Registers all the callback functions with the UWB subsystem.
- Initializes the BLE advertising with the name `Arduino Stella`. This name is what will appear in the smartphone app's device list.

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

- **Adding visual feedback:** Using the onboard LED to indicate distance ranges.
- **Implementing audio feedback:** Using the onboard buzzer to create proximity alerts or distance-based tones.
- **Incorporating accelerometer data:** Combining motion detection with UWB ranging for smarter tracking applications.
- **Power optimization:** Implementing sleep modes and wake-on-motion features for extended battery life.
- **Data logging:** Recording distance measurements over time for analysis and visualization.

***<strong>Note:</strong> If you want to try this example yourself, please follow the same steps described in the [Nearby World Example](#nearby-world-example) section. The process for uploading the sketch and testing it with a smartphone is the same.***

## Two-Way Ranging Example

### About the Two-Way Ranging Example

The Two-Way Ranging example demonstrates direct UWB communication between two Arduino devices: the Portenta UWB Shield (acting as a Controlee/Responder) and the Arduino Stella (acting as a Controller/Initiator). This example showcases the fundamental distance measurement capabilities of UWB technology in a dedicated device-to-device setup without requiring external UWB-enabled consumer devices such as smartphones.

***<strong>Note:</strong> In UWB communication, the terms "Controller" and "Controlee" refer to specific roles within a ranging session. A Controller (also called an Initiator) is the device that initiates and controls the ranging process, sending the initial signal and managing the timing of exchanges. A Controlee (also called a Responder) is the device that responds to the Controller's signals. These terms are used interchangeably in UWB documentation: Controller/Initiator and Controlee/Responder refer to the same roles. In positioning systems, Controllers/Initiators often correspond to mobile "tags" while Controlees/Responders often serve as stationary "anchors".***

This example demonstrates the following:

- **Direct device-to-device communication:** Unlike the `NearbyDemo` example, which requires a smartphone, this example establishes direct UWB communication between two UWB-enabled Arduino devices.
- **Controller-Controlee architecture:** It shows how to configure one device as a Controller (initiator of the ranging) and another as a Controlee (responder).
- **Double-Sided Two-Way Ranging (DS-TWR):** This technique provides higher accuracy in distance measurements by accounting for clock drift between devices.
- **Simple MAC addressing:** The implementation shows how to use short MAC addresses for device identification in UWB networks.

Some of the real-life applications for this example include:

- **Multi-node positioning systems:** Creating networks of UWB nodes for advanced indoor positioning.
- **Robot navigation:** Enabling precise distance measurements between robots or between robots and fixed stations.
- **Asset tracking:** Building custom tracking solutions with multiple Arduino-based UWB anchors.
- **Proximity detection systems:** Creating safety systems that can detect precise distances between industrial equipment and personnel.
- **Interactive installations:** Enabling position-based interactive exhibits in museums or public spaces.

Here's the code for the Portenta UWB Shield, which acts as the Controlee (Responder) in this Two-Way Ranging scenario:

```arduino
/**
  Two-Way Ranging Controlee Example for Portenta UWB Shield
  Name: portenta_uwb_twr_controlee.ino
  Purpose: This sketch configures the Portenta UWB Shield as a Controlee (Responder)
  for Two-Way Ranging with an Arduino Stella configured as Controller.
  
  @author Pierpaolo Lento from Truesense, modified by the Arduino Product Experience Team
  @version 1.0 15/04/25
*/

// Include required UWB library
#include <ardUWBSr150.h>

/**
  Processes ranging data received from UWB communication.
  @param rangingData Reference to UWB ranging data object.
*/
void rangingHandler(UWBRangingData &rangingData) {
  Serial.print("- GOT RANGING DATA - Type: ");
  Serial.println(rangingData.measureType());
  if(rangingData.measureType()==MEASUREMENT_TYPE_TWOWAY) {
    // Get the TWR (Two-Way Ranging) measurements
    RangingMeasures twr=rangingData.twoWayRangingMeasure();
    
    // Loop through all available measurements
    for(int j=0;j<rangingData.available();j++) {
      // Only process valid measurements
      if(twr[j].status==0 && twr[j].distance!=0xFFFF) {
        // Display the distance measurement in millimeters
        Serial.print("- Distance: ");
        Serial.println(twr[j].distance);  
      }
    }
  }
}

void setup() {
  // Initialize serial communication at 115200 bits per second
  Serial.begin(115200);

  #if defined(ARDUINO_PORTENTA_C33)
    // Only the Portenta C33 has an RGB LED
    pinMode(LEDR, OUTPUT);
    digitalWrite(LEDR, LOW);
  #endif

  // Define MAC addresses for this device and the target
  // This device (Controlee) has address 0x2222
  // Target device (Controller) has address 0x1111
  uint8_t devAddr[]={0x22,0x22};
  uint8_t destination[]={0x11,0x11};
  UWBMacAddress srcAddr(UWBMacAddress::Size::SHORT,devAddr);
  UWBMacAddress dstAddr(UWBMacAddress::Size::SHORT,destination);
  
  // Register the callback and start UWB
  UWB.registerRangingCallback(rangingHandler);
  UWB.begin();
  Serial.println("- Starting UWB ...");

  // Wait until UWB stack is initialized
  while(UWB.state()!=0)
    delay(10);

  // Configure the UWB session
  Serial.println("- Starting session ...");
  UWBSession session1;
  session1.sessionID(0x11223344);
  session1.sessionType(UWBD_RANGING_SESSION);
    
  // Set application parameters
  if(!session1.appParams.addOrUpdateParam(UWB_SET_APP_PARAM_VALUE(NO_OF_CONTROLEES,1)))
    Serial.println("- Could not add to app params!");
  if(!session1.appParams.destinationMacAddr(dstAddr))
    Serial.println("- Could not add to app params!");
    
  // Apply default values for measurement repetition rate and antenna config
  session1.applyDefaults();

  // Configure ranging parameters
  session1.rangingParams.deviceMacAddr(srcAddr);
  session1.rangingParams.deviceRole(kUWB_DeviceRole_Responder);
  session1.rangingParams.deviceType(kUWB_DeviceType_Controlee);
  session1.rangingParams.multiNodeMode(kUWB_MultiNodeMode_UniCast);
  session1.rangingParams.rangingRoundUsage(kUWB_RangingRoundUsage_DS_TWR);
  session1.rangingParams.scheduledMode(kUWB_ScheduledMode_TimeScheduled);
  
  // Add the session to the manager and start it
  UWBSessionManager.addSession(session1);
  session1.init();
  session1.start();
}

void loop() {
  // Toggle the LED to show the system is running
  #if defined(ARDUINO_PORTENTA_C33)
    // Only the Portenta C33 has an RGB LED
    digitalWrite(LEDR, !digitalRead(LEDR));
  #else
    Serial.println(millis());
  #endif
  
  // Small delay using FreeRTOS scheduler
  vTaskDelay(configTICK_RATE_HZ/4);
}
```

Here's the code for the Arduino Stella, which acts as the Controller (Initiator) in this Two-Way Ranging scenario:

```arduino
/**
  Two-Way Ranging Controller Example for Arduino Stella
  Name: stella_uwb_twr_controller.ino
  Purpose: This sketch configures the Arduino Stella as a Controller (Initiator)
  for Two-Way Ranging with a Portenta UWB Shield configured as Controlee.
  
  @author Pierpaolo Lento from Truesense, modified by the Arduino Product Experience Team
  @version 1.0 15/04/25
*/

// Include required UWB library
#include "ardUWBSr040.h"

/**
  Processes ranging data received from UWB communication.
  @param rangingData Reference to UWB ranging data object.
*/
void rangingHandler(UWBRangingData &rangingData) {
  Serial.print("- GOT RANGING DATA - Type: ");
  Serial.println(rangingData.measureType());
  if(rangingData.measureType()==MEASUREMENT_TYPE_TWOWAY) {
    // Get the TWR (Two-Way Ranging) measurements
    RangingMeasures twr=rangingData.twoWayRangingMeasure();
    
    // Loop through all available measurements
    for(int j=0;j<rangingData.available();j++) {
      // Only process valid measurements
      if(twr[j].status==0 && twr[j].distance!=0xFFFF) {
        // Display the distance measurement in millimeters
        Serial.print("- Distance: ");
        Serial.println(twr[j].distance);
      }
    }
  }
}

void setup() {
  // Initialize serial communication at 115200 bits per second
  Serial.begin(115200);
  
  // Define MAC addresses for this device and the target
  // This device (Controller) has address 0x1111
  // Target device (Controlee) has address 0x2222
  uint8_t devAddr[]={0x11,0x11};
  uint8_t destination[]={0x22,0x22};
  UWBMacAddress srcAddr(UWBMacAddress::Size::SHORT,devAddr);
  UWBMacAddress dstAddr(UWBMacAddress::Size::SHORT,destination);
  
  // Register the ranging notification handler before starting
  UWB.registerRangingCallback(rangingHandler);
  
  // Start the UWB stack
  UWB.begin();
  Serial.println("- Starting UWB ...");
  
  // Wait until the stack is initialized
  while(UWB.state()!=0)
    delay(10);
  
  // Setup and start the UWB session
  Serial.println("- Starting session ...");
  
  // Create a tracker with session ID 0x11223344
  // This automatically configures the device as Controller/Initiator
  UWBTracker myTracker(0x11223344,srcAddr,dstAddr);
  
  // Add the session to the manager
  UWBSessionManager.addSession(myTracker);
  
  // Initialize with default parameters
  myTracker.init();
  
  // Start the ranging session
  myTracker.start();
}

void loop() {
  // Simple delay, the ranging happens asynchronously via callbacks
  delay(1000);
}
```

### Key Components of the Example Sketch

The Two-Way Ranging example demonstrates a more direct approach to UWB communication compared to the `NearbyDemo`. Let's analyze the key components of both example sketches:

1. **Libraries and MAC Addressing**

Both devices use their respective UWB libraries:

- The Portenta UWB Shield uses `ardUWBSr150.h` (for the DCU150 module)
- The Stella uses ardUWBSr040.h (for the DCU040 module)

Both sketches configure MAC addresses for identification:

```arduino
// On Portenta UWB Shield
uint8_t devAddr[]={0x22,0x22};
uint8_t destination[]={0x11,0x11};

// On Arduino Stella
uint8_t devAddr[]={0x11,0x11};
uint8_t destination[]={0x22,0x22};
```

***<strong>Important note:</strong> Notice how the MAC addresses are reversed between the two devices; this is critical for proper communication. In UWB communication, each device must know both its own address (`devAddr`) and the address of the device it is communicating with (`destination`). The Portenta UWB Shield identifies itself as `0x2222` and expects to communicate with `0x1111`, while the Arduino Stella identifies itself as `0x1111` and expects to communicate with `0x2222`. If these addresses don't match correctly, the devices won't be able to establish a ranging session. The prefix `0x` indicates these are hexadecimal values, which is a common notation in programming for representing memory addresses and identifiers.***

The MAC addresses used in this example are short (2-byte) addresses for simplicity, but UWB also supports extended (8-byte) addressing for larger networks where unique identification is required. For basic two-device setups, these short addresses are enough, but for multi-node positioning systems, you may want to use extended addressing to avoid conflicts.

2. **Setup and Initialization**

The setup process for UWB communication differs between the two devices due to their different roles in the ranging session:

**Portenta UWB Shield (Controlee/Responder):**

```arduino
// Configure the UWB session
UWBSession session1;
session1.sessionID(0x11223344);  // Unique identifier for this session
session1.sessionType(UWBD_RANGING_SESSION);
    
// Set application parameters
if(!session1.appParams.addOrUpdateParam(UWB_SET_APP_PARAM_VALUE(NO_OF_CONTROLEES,1)))
  Serial.println("could not add to app params");
if(!session1.appParams.destinationMacAddr(dstAddr))
  Serial.println("could not add to app params");
    
// Apply default values for measurement repetition rate and antenna config
session1.applyDefaults();

// Configure ranging parameters
session1.rangingParams.deviceMacAddr(srcAddr);
session1.rangingParams.deviceRole(kUWB_DeviceRole_Responder);
session1.rangingParams.deviceType(kUWB_DeviceType_Controlee);
session1.rangingParams.multiNodeMode(kUWB_MultiNodeMode_UniCast);
session1.rangingParams.rangingRoundUsage(kUWB_RangingRoundUsage_DS_TWR);
session1.rangingParams.scheduledMode(kUWB_ScheduledMode_TimeScheduled);
  
// Add the session to the manager and start it
UWBSessionManager.addSession(session1);
session1.init();
session1.start();
```

**Arduino Stella (Controller/Initiator):**

```arduino
// Create a tracker with session ID 0x11223344
// This automatically configures the device as Controller/Initiator
UWBTracker myTracker(0x11223344,srcAddr,dstAddr);
  
// Add the session to the manager
UWBSessionManager.addSession(myTracker);
  
// Initialize with default parameters
myTracker.init();
  
// Start the ranging session
myTracker.start();
```

***<strong>Important note:</strong> The session configuration is more detailed for the Portenta UWB Shield because it explicitly defines all the ranging parameters. The Arduino Stella uses the simplified `UWBTracker` class which automatically sets up the device as a Controller/Initiator with appropriate defaults. However, both devices must use the same session ID (`0x11223344` in this example) to communicate with each other. This session ID acts as a shared identifier for the ranging session between these specific devices.***

Let's examine some of the key configuration parameters:

- `sessionID`: A unique 32-bit identifier (`0x11223344`) that must match between devices in the same session.
- `deviceRole`: Defines whether the device is a Responder (Controlee) or Initiator (Controller).
- `multiNodeMode`: Set to UniCast for direct device-to-device communication.
- `rangingRoundUsage`: Set to DS_TWR (Double-Sided Two-Way Ranging) for highest accuracy.
- `scheduledMode`: `TimeScheduled` mode allows the Controller to manage the timing of ranging exchanges.

The initialization follows a specific sequence on both devices:

- Register the ranging callback.
- Start the UWB subsystem.
- Configure the session parameters.
- Initialize the session (apply the configuration).
- Start the session (begin the ranging process).

This process ensures both devices are properly configured before ranging begins, establishing a synchronized communication channel for precise distance measurements.

1. **Ranging Data Handler**

Both devices use nearly identical callback functions to process ranging data:

```arduino
void rangingHandler(UWBRangingData &rangingData) {
  // ...
  if(rangingData.measureType()==MEASUREMENT_TYPE_TWOWAY) {
    RangingMeasures twr=rangingData.twoWayRangingMeasure();
    for(int j=0;j<rangingData.available();j++) {
      if(twr[j].status==0 && twr[j].distance!=0xFFFF) {
        Serial.print("Distance: ");
        Serial.println(twr[j].distance);
      }
    }
  }
}
```

This function:

- Is triggered whenever new ranging data is available.
- Checks if the measurement type is Two-Way Ranging (TWR).
- Validates the data (`status = 0` indicates a valid measurement, while `distance = 0xFFFF` is a reserved value indicating an invalid distance).
- Outputs the distance measurements in millimeters and prints them to the IDE's Serial Monitor.

4. **Main Loop**

The main loops of the two devices have different behaviors:

**Portenta UWB Shield (Controlee/Responder):**

```arduino
void loop() {
  digitalWrite(LEDR, !digitalRead(LEDR)); // Toggle LED
  vTaskDelay(configTICK_RATE_HZ/4);       // Delay using FreeRTOS scheduler
}
```

**Arduino Stella (Controller/Initiator):**

```arduino
void loop() {
  delay(1000); // Simple 1-second delay
}
```

The actual ranging operations happen asynchronously through the callback system, so the main loop primarily handles visual feedback and timing.

### Try it Yourself

To test this two-device ranging setup:

1. Connect the Portenta UWB Shield to your Portenta C33.
2. Upload the Controlee/Responder example sketch to the Portenta C33.
3. Connect the Arduino Stella to your computer.
4. Upload the Controller/Initiator example sketch to the Arduino Stella.
5. Open two separate Serial Monitor windows (one for each device) set to 115200 baud.

You should see distance measurements appearing in both Serial Monitors. Try moving the devices closer together and further apart to see the distance values change in real-time.

**Tips for optimal performance:**

- For best results, position the devices so their antennas have clear line-of-sight to each other.
- Keep the devices at least 20 cm away from large metal objects, as these can reflect UWB signals and interfere with measurements.
- Maintain the devices in a similar orientation (parallel to each other) for more consistent results, as antenna positioning affects signal strength.
- Start testing at distances between 0.5 to 3 meters, as extremely close or far distances might produce less reliable measurements.

The distances are reported in millimeters, providing centimeter-level accuracy. For example, a reading of `- Distance: 1234` indicates the devices are approximately 1.234 meters apart.

### Extending the Two-Way Ranging Example

This basic example can be extended in several ways for more advanced applications:

- **Adding multiple nodes:** Modify the example sketch to support multiple anchors or tags for triangulation and full positioning.
- **Integrating additional sensors:** Combine UWB ranging with IMU data for more robust positioning.
- **Implementing position calculation:** Add algorithms to convert distance measurements to coordinates.
- **Creating a visualization interface:** Develop a graphical interface to display the relative positions of devices.
- **Adding data communication:** Use UWB not just for ranging but also for data exchange between devices.

## Support

If you encounter any issues or have questions while working with your Arduino Stella, we provide various support resources to help you find answers and solutions.

### Help Center

Explore our Help Center, which offers a comprehensive collection of articles and guides for Arduino boards and shields. The Help Center is designed to provide in-depth technical assistance and help you make the most of your device.

- [Arduino Help Center](https://support.arduino.cc/hc/en-us)

### Forum

Join our community forum to connect with other Stella users, share your experiences, and ask questions. The Forum is an excellent place to learn from others, discuss issues, and discover new ideas and projects related to the Stella.

- [Arduino Stella in the Arduino Forum](https://forum.arduino.cc/c/hardware/stella/91)

### Contact Us

Please get in touch with our support team if you need personalized assistance or have questions not covered by the help and support resources described before. We're happy to help you with any issues or inquiries about the Stella.

- [Contact us page](https://www.arduino.cc/en/contact-us/)