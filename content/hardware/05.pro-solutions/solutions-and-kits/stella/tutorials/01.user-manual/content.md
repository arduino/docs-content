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
- [USB-C® cable (SKU: TPX00094)](https://store.arduino.cc/products/usb-cable2in1-type-c) (x1)
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

So, how does UWB technology works?

UWB uses a technique called "Time of Flight" (ToF) or "Time Difference of Arrival" (TDoA) to determine the distance between UWB-enabled devices. In a nutshell, this technique consists of the following steps:

1. A UWB transmitter sends a signal with a precise timestamp.
2. A UWB receiver detects the signal and calculates the time it took to arrive.
3. Since radio waves travel at the speed of light (approximately 30 cm per nanosecond), the system can calculate the distance with high precision.

For even greater accuracy, UWB can use the "Two-Way Ranging" (TWR) technique, where devices exchange several messages to account for clock synchronization issues. The Angle of Arrival (AoA) capability enhances positioning by not only determining distance but also the angle from which a signal arrives, enabling with this more accurate 2D or 3D positioning.

In a UWB positioning system, devices typically operate in one of two roles:

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
- **User interfaces**: The board includes a user-programmable button, a user-programmable LED and a buzzer (FUET-5020) producing 75 dB at 10 cm for audible alerts.
- **Connectors**: The Stella features a USB-C® port for power and data, a QWIIC connector for I²C expansion, a CR2032 battery holder and a J-Link connector for debugging and alternative power input.

### Board Libraries

The [`ardUWBSr040` library](https://github.com/arduino-libraries/ardUWBSr040) contains an application programming interface (API) to read data from the board and control its parameters and behavior. This library supports the following: 

- One-way ranging (Time Difference of Arrival - TDoA) and two-way ranging (TWR).
- Power management for battery-efficient operation.
- Accelerometer control for motion detection.
- BLE connectivity for configuration and communication.

***The Arduino mbed OS Boards core is required to work with the Stella's nRF52840 microcontroller.***

To install the Stella library, navigate to `Tools > Manage libraries...` or click the **Library Manager** icon in the left tab of the Arduino IDE. In the Library Manager tab, search for `ardUWBSr040` and install the latest version of the library.

![Installing the board's library in the Arduino IDE](assets/user-manual-3.png)

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
#include <ArduinoStella.h>

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