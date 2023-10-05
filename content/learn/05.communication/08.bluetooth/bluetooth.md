---
title: 'Bluetooth® Low Energy'
description: 'Bluetooth LE is a wireless communication technology designed for short-range communication between electronic devices.'
author: Hannes Siebeneicher
tags: [bluetooth]
difficulty: 'intermediate'
hardware:
  - hardware/01.mkr/01.boards/mkr-wifi-1010
  - hardware/02.hero/boards/uno-r4-wifi
  - hardware/03.nano/boards/nano-33-ble
  - hardware/03.nano/boards/nano-33-sense
  - hardware/03.nano/boards/nano-33-sense-rev2
  - hardware/03.nano/boards/nano-33-iot
  - hardware/03.nano/boards/nano-esp32
  - hardware/03.nano/boards/nano-rp2040-connect
  - hardware/04.pro/boards/portenta-h7
  - hardware/04.pro/boards/portenta-h7-lite-connected
  - hardware/05.pro-solutions/solutions-and-kits/portenta-machine-control
  - hardware/06.nicla/boards/nicla-voice
  - hardware/07.opta/opta-family/opta
  - hardware/10.mega/boards/giga-r1-wifi
software:
  - ide-v1
  - ide-v2
  - web-editor
---

## Introduction

Bluetooth Low Energy®, often referred to as Bluetooth LE, is a wireless communication technology designed for short-range data exchange between electronic devices. It emerged as a response to the need for energy-efficient wireless communication in various applications, especially those where power consumption is a critical concern.

Unlike its predecessor, Bluetooth Classic, which is optimized for continuous and relatively high-data-rate communication, Bluetooth LE focuses on minimizing energy consumption while maintaining connectivity. This makes Bluetooth LE particularly suitable for applications that require long battery life, such as fitness trackers, healthcare devices, smart sensors, and Internet of Things (IoT) devices.

The aim of this article is to highlight the basic concepts of Bluetooth Low Energy and explain how to use the ArduinoBLE library to create Bluetooth LE projects with compatible Arduino boards.

***To follow along this article you need a compatible board and the [ArduinoBLE library](https://www.arduino.cc/reference/en/libraries/arduinoble/)***

### Harald Blåtand

Harald Blåtand was a 10th-century Danish king who ruled from approximately 958 to 986 AD and he originally inspired the name Bluetooth. He is best known for his role in uniting various Danish tribes and for his conversion to Christianity, which had a significant impact on the history of Denmark. His nickname “Blåtand” (translated: Bluetooth) is believed to have been inspired by his dead or discolored tooth, which may have appeared blue or black.

Similar to how Harald Blåtand united Denmark the Bluetooth protocol was meant to unite various devices and communication protocols.

## Technical Specifications

The following parts explore the core concepts and technical specifications of Bluetooth LE.

### Frequency Bands and Range

Bluetooth Low Energy operates in the 2.4 GHz ISM (Industrial, Scientific, and Medical) band, which is commonly used for various wireless technologies. This frequency band is divided into multiple channels that Bluetooth LE devices use for communication.

### Typical Bluetooth Low Energy Range

The range of a Bluetooth LE connection can vary depending on several factors, but in typical scenarios, it can extend up to approximately 50 meters (or roughly 164 feet) in a line-of-sight environment. This range can be affected by several factors:

**Obstacles**: Physical obstacles such as walls, furniture, and other objects can significantly reduce the range of a Bluetooth LE connection. Thick walls and materials like concrete can be particularly challenging for Bluetooth LE signals to penetrate.

**Interference**: As mentioned earlier, the 2.4 GHz band is shared by various wireless devices. Interference from other devices operating in the same frequency range can impact the range and reliability of Bluetooth LE connections.

**Antenna Design**: The design and quality of the antennas in both the central and peripheral devices can influence the range. Devices with well-designed antennas tend to have better coverage.

**Orientation**: The relative orientation of the central and peripheral devices also affects range. A clear line of sight between devices typically results in the best range, while obstructed lines of sight can reduce it.

### Central / Peripheral Devices

Bluetooth Low Energy devices operate using different roles and modes that define how devices interact with each other.

**Central Device**: A central device in Bluetooth  LE is typically a more capable device with features like a higher CPU power, more memory, or a larger battery. Central devices take on the role of initiating connections to peripheral devices. For example, your smartphone is often a central device when connecting to Bluetooth LE peripherals like fitness trackersy, smart sensors or an Arduino board.

**Peripheral Device**: Peripheral devices are generally resource-constrained compared to central devices (e.g. an Arduino board compared with your smartphone). Peripheral devices advertise their presence and data to central devices. Compared to Bluetooth classic, Bluetooth LE devices don't maintain a continues connection to the central device to save power.

![Bluetooth LE Roles](./assets/ble_roles.png)

### Advertising / Connection Mode

**Advertising Mode**: Advertising mode is primarily used to make a Bluetooth LE peripheral device discoverable by other devices, particularly central devices. During advertising mode, the peripheral device periodically broadcasts advertising packets. These packets contain information about the peripheral's identity, services, and characteristics. Central devices continuously scan for these advertising packets to discover nearby peripherals. In advertising mode, the peripheral device is not actively connected to any central device. It remains in a low-power state while broadcasting advertising packets. It is "waiting" for a central device to establish a connection.

**Connection Mode**: Connection mode is activated once a central device successfully establishes a connection with a peripheral device. During this mode, devices can exchange data bi-directionally. Central devices can read data from and write data to the peripheral device. The connection mode is crucial for ongoing communication between BLE devices.

![Bluetooth LE Modes](./assets/ble_mode.gif)

### Services and Characteristics

In Bluetooth LE, services and characteristics are fundamental concepts that organize and describe the data exchanged between devices. Let's explore these concepts in detail:

**Services** 

In Bluetooth LE, a service can be thought of as a logical grouping of related data measurements or functionalities provided by a peripheral device. These data measurements can represent various aspects of the device's capabilities or the information it collects.

For example, consider a weather monitoring sensor. It might have a service called "Weather Data" that encompasses measurements like temperature, humidity, and wind speed. Another service, "Energy Information," could include data related to battery level and energy consumption.

**Characteristics**

Within each service, we have characteristics. Characteristics are individual data points or attributes that provide specific information or measurements.

For instance, in the "Weather Data" service mentioned earlier, characteristics may include "Temperature," "Humidity," and "Wind Speed." These characteristics continuously record data and update as new measurements become available.

Similarly, the "Energy Information" service may consist of characteristics like "Battery Level" and "Energy Consumption."

**Unique Universal Identifier(UUIDs)**:

To distinguish services and characteristics, Bluetooth LE relies on a unique identifier called a UUID (Unique Universal Identifier).

A UUID is a 128-bit value that serves as a universally unique name for a service or characteristic. It acts like a label or identifier that central devices use to identify and communicate with specific services and characteristics.

UUIDs play a crucial role in Bluetooth LE communication because they ensure that central devices can accurately locate and interact with the desired data points on peripheral devices. They eliminate ambiguity and allow for precise data retrieval and control.

In practical terms, understanding services and characteristics is essential when designing or interacting with Bluetooth LE devices. Services provide a high-level organization of data, while characteristics represent the individual data points within those services. UUIDs act as the keys that enable central devices to access and utilize the data provided by peripheral devices.

As you explore Bluetooth LE further, you'll encounter various predefined services and characteristics used in common applications. These standardized profiles simplify the development process, making it easier to create Bluetooth LE-based projects and applications.

**Profiles**

Bluetooth LE profiles are predefined sets of services and characteristics that standardize how Bluetooth LE devices interact with each other. These profiles define the behavior and capabilities of Bluetooth LE devices, making it easier for different devices to communicate seamlessly. Let's delve into Bluetooth LE profiles:

**Defining Bluetooth LE Profiles**

Bluetooth LE profiles serve as blueprints that specify how data should be organized and exchanged between devices in a standardized manner. They define the roles, services, and characteristics that devices can use to communicate effectively.

Each profile is tailored to a specific use case or application, ensuring that devices of different manufacturers can work together seamlessly when using the same profile.

**Common Standard Profiles**

Bluetooth LE includes a range of standard profiles that simplify the development of Bluetooth LE applications. Some of the most well-known standard profiles include:

- Battery Service: The Battery Service provides information about the battery level of a device. It typically includes a Battery Level characteristic that central devices can read to monitor the battery status of a peripheral device, such as a wireless headset or smartwatch.

- Heart Rate Service: The Heart Rate Service is commonly used in fitness and health monitoring applications. It includes characteristics that provide real-time heart rate data, allowing central devices like smartphones or fitness trackers to monitor a user's heart rate during exercise.

- Generic Access Profile (GAP): While not a service in itself, GAP defines the roles and procedures for device discovery and connection establishment in Bluetooth LE. It plays a vital role in enabling devices to find and connect to each other seamlessly.

***You can read more about Bluetooth profiles [here](https://en.wikipedia.org/wiki/List_of_Bluetooth_profiles).***

**Creating Custom Profiles**

In addition to standard profiles, developers have the flexibility to create custom profiles tailored to their specific application needs. These custom profiles define unique services and characteristics that match the requirements of a particular project.

Using Bluetooth LE profiles, developers can leverage standardized profiles for common applications or create custom profiles for specialized projects. This standardized approach simplifies the development process, enhances interoperability, and allows for the creation of diverse Bluetooth LE-based applications, from health monitoring to home automation.

As you explore Bluetooth LE further, you'll discover a wide range of profiles designed to support various use cases. These profiles play a crucial role in ensuring that Bluetooth LE devices can seamlessly communicate and provide valuable data to central devices.

## Bluetooth Classic

Bluetooth Low Energy is distinctively different from Bluetooth Classic. Bluetooth Classic operates in a manner similar to a serial port or UART (Universal Asynchronous Receiver-Transmitter), which is commonly used for point-to-point communication.

Some key differences are:

### Power Consumption

-	**Bluetooth Classic**: is designed for continuous, relatively high-data-rate communication. As a result, it consumes more power, making it less suitable for battery-operated devices with limited power sources.

-	**Bluetooth Low Energy**: is optimized for energy efficiency. It is specifically designed for applications where power consumption is a critical consideration, such as fitness trackers, IoT sensors, and wearable devices. BLE devices can operate for extended periods on small batteries or even energy harvesting solutions.

### Data Transfer Rates

-	**Bluetooth Classic**: offers higher data transfer rates suitable for tasks like streaming audio or transferring files between devices.

-	**Bluetooth Low Energy**: sacrifices data transfer speed in favor of energy efficiency. It's ideal for applications that require intermittent or small bursts of data, such as sending sensor readings or control commands.

### Connection Types

-	**Bluetooth Classic**: establishes a continuous and relatively power-hungry connection, making it suitable for applications requiring real-time, continuous communication.

-	**Bluetooth Low Energy**: supports two primary modes - advertising and connection. In advertising mode, a BLE peripheral periodically broadcasts its presence but doesn't maintain a continuous connection, conserving power. When needed, a central device can establish a connection for data exchange.


## ArduinoBLE Library

To enable Bluetooth LE on your Arduino board you must first download and install the ArduinoBLE library. See our [instructions](https://docs.arduino.cc/software/ide-v2/tutorials/ide-v2-installing-a-library) on how to install a library. Arduino boards can act as central and peripheral devices. You need to adapt the code according to the steps shown below:

**Initialize ArduinoBLE**

To use the ArduinoBLE library you must include it at the top of your code like so:
```arduino
#include <ArduinoBLE.h>
```

### Arduino as Central Device

The following steps show how to set up your Arduino board as central device.

#### Initialize the BLE Library

To set up your board as central device you begin by initializing the BLE library using `BLE.begin()` inside `setup()`. Make sure to check if the initialization was successful.

```arduino
void setup() {
  if (!BLE.begin()) {
    Serial.println("Failed to initialize BLE!");
    while (1);
  }
}
```

#### Start Scanning

Start scanning for peripheral Devices by calling `BLE.scan()` inside `setup()`:

```arduino
BLE.scan();
```

#### Print Peripheral Devices

If a peripheral is found print its `address`, `name`, and `advertised service`.

```arduino
void loop() {
  // check if a peripheral has been discovered
  BLEDevice peripheral = BLE.available();

  if (peripheral) {
    // discovered a peripheral, print out address, local name, and advertised service
    Serial.print("Found ");
    Serial.print(peripheral.address());
    Serial.print(" '");
    Serial.print(peripheral.localName());
    Serial.print("' ");
    Serial.print(peripheral.advertisedServiceUuid());
    Serial.println();
  }
}
```

#### Connect to Peripheral

If you know which peripheral to connect to, specify the name and connect to that device by executing `explorerPeripheral()` if the condition for the correct name is met:

Connect to a specific peripheral by specifying the peripheral's name and execute `explorerPeripheral()` if the condition for the correct name is met:

```arduino
void loop() {
  // check if a peripheral has been discovered
  BLEDevice peripheral = BLE.available();

  if (peripheral) {
    // discovered a peripheral, print out address, local name, and advertised service
    Serial.print("Found ");
    Serial.print(peripheral.address());
    Serial.print(" '");
    Serial.print(peripheral.localName());
    Serial.print("' ");
    Serial.print(peripheral.advertisedServiceUuid());
    Serial.println();

    // check for peripheral's name
    if (peripheral.localName() == "<PERIPHERAL_NAME>") {
      // stop scanning
      BLE.stopScan();

      explorerPeripheral(peripheral);

      // peripheral disconnected, we are done
      while (1) {
        // do nothing
      }
    }
  }
}
```

***The peripheral.connect() function calls several inner functions. They are explained below:***

**explorerPeripheral()**

The `explorerPeripheral()`function responsible for exploring the attributes of a Bluetooth Low Energy peripheral device after it has been successfully connected. It gathers information about the device's services, characteristics, descriptors, and other details that are advertised by the peripheral.

```arduino
void explorerPeripheral(BLEDevice peripheral) {
  // connect to the peripheral
  Serial.println("Connecting ...");

  if (peripheral.connect()) {
    Serial.println("Connected");
  } else {
    Serial.println("Failed to connect!");
    return;
  }

  // discover peripheral attributes
  Serial.println("Discovering attributes ...");
  if (peripheral.discoverAttributes()) {
    Serial.println("Attributes discovered");
  } else {
    Serial.println("Attribute discovery failed!");
    peripheral.disconnect();
    return;
  }

  // read and print device name of peripheral
  Serial.println();
  Serial.print("Device name: ");
  Serial.println(peripheral.deviceName());
  Serial.print("Appearance: 0x");
  Serial.println(peripheral.appearance(), HEX);
  Serial.println();

  // loop the services of the peripheral and explore each
  for (int i = 0; i < peripheral.serviceCount(); i++) {
    BLEService service = peripheral.service(i);

    exploreService(service);
  }

  Serial.println();

  // we are done exploring, disconnect
  Serial.println("Disconnecting ...");
  peripheral.disconnect();
  Serial.println("Disconnected");
}
```

**exploreCharacteristic()**

The `exploreCharacteristic()` function is responsible for examining the characteristics of the Bluetooth LE service and printing their information. It iterates through the characteristics of a service and, for each characteristic, prints its UUID, properties, and value (if readable).

```arduino
void exploreService(BLEService service) {
  // print the UUID of the service
  Serial.print("Service ");
  Serial.println(service.uuid());

  // loop the characteristics of the service and explore each
  for (int i = 0; i < service.characteristicCount(); i++) {
    BLECharacteristic characteristic = service.characteristic(i);

    exploreCharacteristic(characteristic);
  }
}
```

**exploreDescriptor()**

```arduino
void exploreDescriptor(BLEDescriptor descriptor) {
  // print the UUID of the descriptor
  Serial.print("\t\tDescriptor ");
  Serial.print(descriptor.uuid());

  // read the descriptor value
  descriptor.read();

  // print out the value of the descriptor
  Serial.print(", value 0x");
  printData(descriptor.value(), descriptor.valueLength());

  Serial.println();
}
```

**printData()**

The `printData()` function is a utility function used to print out binary data in hexadecimal format. It takes as input an array of bytes (data) and the length of the data (length) and prints each byte in hexadecimal format.

```arduino
void printData(const unsigned char data[], int length) {
  for (int i = 0; i < length; i++) {
    unsigned char b = data[i];

    if (b < 16) {
      Serial.print("0");
    }

    Serial.print(b, HEX);
  }
}
```

#### Complete Code

```arduino
#include <ArduinoBLE.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);

  // begin initialization
  if (!BLE.begin()) {
    Serial.println("starting Bluetooth® Low Energy module failed!");

    while (1);
  }

  Serial.println("Bluetooth® Low Energy Central - Peripheral Explorer");

  // start scanning for peripherals
  BLE.scan();
}

void loop() {
  // check if a peripheral has been discovered
  BLEDevice peripheral = BLE.available();

  if (peripheral) {
    // discovered a peripheral, print out address, local name, and advertised service
    Serial.print("Found ");
    Serial.print(peripheral.address());
    Serial.print(" '");
    Serial.print(peripheral.localName());
    Serial.print("' ");
    Serial.print(peripheral.advertisedServiceUuid());
    Serial.println();

    // check for peripheral's name
    if (peripheral.localName() == "<PERIPHERAL_NAME>") {
      // stop scanning
      BLE.stopScan();

      explorerPeripheral(peripheral);

      // peripheral disconnected, we are done
      while (1) {
        // do nothing
      }
    }
  }
}

void explorerPeripheral(BLEDevice peripheral) {
  // connect to the peripheral
  Serial.println("Connecting ...");

  if (peripheral.connect()) {
    Serial.println("Connected");
  } else {
    Serial.println("Failed to connect!");
    return;
  }

  // discover peripheral attributes
  Serial.println("Discovering attributes ...");
  if (peripheral.discoverAttributes()) {
    Serial.println("Attributes discovered");
  } else {
    Serial.println("Attribute discovery failed!");
    peripheral.disconnect();
    return;
  }

  // read and print device name of peripheral
  Serial.println();
  Serial.print("Device name: ");
  Serial.println(peripheral.deviceName());
  Serial.print("Appearance: 0x");
  Serial.println(peripheral.appearance(), HEX);
  Serial.println();

  // loop the services of the peripheral and explore each
  for (int i = 0; i < peripheral.serviceCount(); i++) {
    BLEService service = peripheral.service(i);

    exploreService(service);
  }

  Serial.println();

  // we are done exploring, disconnect
  Serial.println("Disconnecting ...");
  peripheral.disconnect();
  Serial.println("Disconnected");
}

void exploreService(BLEService service) {
  // print the UUID of the service
  Serial.print("Service ");
  Serial.println(service.uuid());

  // loop the characteristics of the service and explore each
  for (int i = 0; i < service.characteristicCount(); i++) {
    BLECharacteristic characteristic = service.characteristic(i);

    exploreCharacteristic(characteristic);
  }
}

void exploreCharacteristic(BLECharacteristic characteristic) {
  // print the UUID and properties of the characteristic
  Serial.print("\tCharacteristic ");
  Serial.print(characteristic.uuid());
  Serial.print(", properties 0x");
  Serial.print(characteristic.properties(), HEX);

  // check if the characteristic is readable
  if (characteristic.canRead()) {
    // read the characteristic value
    characteristic.read();

    if (characteristic.valueLength() > 0) {
      // print out the value of the characteristic
      Serial.print(", value 0x");
      printData(characteristic.value(), characteristic.valueLength());
    }
  }
  Serial.println();

  // loop the descriptors of the characteristic and explore each
  for (int i = 0; i < characteristic.descriptorCount(); i++) {
    BLEDescriptor descriptor = characteristic.descriptor(i);

    exploreDescriptor(descriptor);
  }
}

void exploreDescriptor(BLEDescriptor descriptor) {
  // print the UUID of the descriptor
  Serial.print("\t\tDescriptor ");
  Serial.print(descriptor.uuid());

  // read the descriptor value
  descriptor.read();

  // print out the value of the descriptor
  Serial.print(", value 0x");
  printData(descriptor.value(), descriptor.valueLength());

  Serial.println();
}

void printData(const unsigned char data[], int length) {
  for (int i = 0; i < length; i++) {
    unsigned char b = data[i];

    if (b < 16) {
      Serial.print("0");
    }

    Serial.print(b, HEX);
  }
}
```

### Arduino as Peripheral

The following steps show how to set up your Arduino board as peripheral.

#### Initialize the BLE Library

To set up your board as central device you begin by initializing the BLE library using `BLE.begin()` inside `setup()`. Make sure to check if the initialization was successful.

```arduino
void setup() {
  Serial.begin(9600);
  if (!BLE.begin()) {
    Serial.println("Failed to initialize BLE!");
    while (1);
  }
}
```

#### Name your Board

To recognize your device give it a unique name by adding this line to your `setup()`:

```arduino
  BLE.setLocalName("Arduino Board");
```

#### Create Services

To create a new service (using the UUID for "Device Information service") add this line **above** `setup()`:

```arduino
BLEService newService("180A");
```

Read more about standard services in the [Assigned Numbers document](https://www.bluetooth.com/specifications/assigned-numbers/).

#### Create Characteristics

Depending on your needs you can create different `BLECharacteristic`.

For creating an **analog value** characteristics write:

```arduino
BLEUnsignedCharCharacteristic analogReading("2A58", BLERead | BLENotify);
```

For creating a **digital value** characteristics write:

```arduino
BLEByteCharacteristic digitalReading("2A57", BLERead | BLEWrite);
```

You can see the full list of available characteristics [here](https://reference.arduino.cc/reference/en/libraries/arduinoble/blecharacteristic/).

#### Set the Advertised Service

To ensure that central devices can correctly identify and discover your peripheral's service, you should set the advertised service by calling `BLE.setAdvertisedService()` inside `setup()`:

```arduino
BLE.setAdvertisedService(newService);
```

#### Add Characteristics to the Service

Next, you need to add the characteristics created in the previous step to the service also created previously calling `newService.addCharacteristic()` inside `setup()`:

```arduino
newService.addCharacteristic(digitalReading);
newService.addCharacteristic(analogReading);
```

#### Set Initial Values for Characteristics

You can set initial values for your characteristics, which will be sent to central devices when they connect to your peripheral. Add these lines inside `setup()`:

```arduino
digitalReading.writeValue(0);
analogReading.writeValue(0);
```

#### Start Advertising

Once you've configured your peripheral device with services and characteristics, it's time to start advertising these services to allow central devices to discover your Arduino. In your code, you've initiated advertising using `BLE.advertise()` inside `setup()`:

```arduino
BLE.advertise();
Serial.println(" Bluetooth® device active, waiting for connections...");
```

#### Set Board as Central

Inside `loop()` start looking for connections by setting the board as `central`:

```arduino
BLEDevice central = BLE.central();
```

#### Establish Connection

Next, add a conditional `if statement` and check if the board is connected. If so print the connection details and turn on the `BUILTIN LED` to signal a connection. Continue to check analog values `while (central.connected()` every 200ms.

```arduino
  if (central) {
    Serial.print("Connected to central: ");

    // print the central's address
    Serial.println(central.address()); 
    
    // turn on the LED to indicate the connection
    digitalWrite(LED_BUILTIN, HIGH); 
  }
```

#### Read Analog Signals

Inside the conditional statement perform an `analogRead()` as usual and write the value to the analog characteristic by using `analogReading.writeValue(analogValue)`. If the board disconnects the `BUILTIN LED` is turned off. 

```arduino
  if (central) {
    Serial.print("Connected to central: ");
    
    // print the central's address
    Serial.println(central.address());
    
    // turn on the LED to indicate the connection
    digitalWrite(LED_BUILTIN, HIGH); 

    // while the central is connected:
    while (central.connected()) {
      long currentMillis = millis();
      
      //Check values every 200ms
      if (currentMillis - previousMillis >= 200) { 
        previousMillis = currentMillis;

        //Read analog value and write it to the characteristic
        int analogValue = analogRead(A1);
        analogReading.writeValue(analogValue);
        }
      }
    
    //Turn off LED when disconnecting
    digitalWrite(LED_BUILTIN, LOW);
    Serial.print("Disconnected from central: ");
    Serial.println(central.address());
  }
```

#### Read Digital Signals

The steps for reading a digital and analog signals are almost identical, but instead perform a `digitalRead()` and write the digital characteristic by using `digitalReading.writeValue(digitalValue)`.

```arduino
  if (central) {
    Serial.print("Connected to central: ");
    
    // print the central's address
    Serial.println(central.address());
    
    // turn on the LED to indicate the connection
    digitalWrite(LED_BUILTIN, HIGH); 

    // while the central is connected:
    while (central.connected()) {
      long currentMillis = millis();
      
      //Check values every 200ms
      if (currentMillis - previousMillis >= 200) { 
        previousMillis = currentMillis;

        //Read digital value and write it to the characteristic
        int digitalValue = digitalRead(2);
        digitalReading.writeValue(digitalValue);
        }
      }
    
    //Turn off LED when disconnecting
    digitalWrite(LED_BUILTIN, LOW); // 
    Serial.print("Disconnected from central: ");
    Serial.println(central.address());
  }
```

#### Complete Code

```arduino
#include <ArduinoBLE.h>
BLEService newService("180A"); // creating the service

BLEUnsignedCharCharacteristic analogReading("2A58", BLERead | BLENotify); // creating the analog characteristic
BLEByteCharacteristic digitalReading("2A57", BLERead | BLEWrite); // creating the digital characteristic

long previousMillis = 0;


void setup() {
  Serial.begin(9600);    // initialize serial communication
  while (!Serial);       //starts the program if we open the serial monitor.

  pinMode(LED_BUILTIN, OUTPUT); // initialize the built-in LED pin to indicate when a central is connected
  
  //initialize ArduinoBLE library
  if (!BLE.begin()) {
    Serial.println("starting Bluetooth® Low Energy failed!");
    while (1);
  }

  BLE.setLocalName("MKR WiFi 1010"); //Setting a name that will appear when scanning for Bluetooth® devices
  BLE.setAdvertisedService(newService);

  newService.addCharacteristic(digitalReading); //add characteristics to a service
  newService.addCharacteristic(analogReading);

  BLE.addService(newService);  // adding the service

  digitalReading.writeValue(0); //set initial value for characteristics
  analogReading.writeValue(0);

  BLE.advertise(); //start advertising the service
  Serial.println(" Bluetooth® device active, waiting for connections...");
}

void loop() {
  
  BLEDevice central = BLE.central(); // wait for a Bluetooth® Low Energy central

  if (central) {  // if a central is connected to the peripheral
    Serial.print("Connected to central: ");
    
    Serial.println(central.address()); // print the central's address
    
    digitalWrite(LED_BUILTIN, HIGH); // turn on the LED to indicate the connection

    // check the battery level every 200ms
    // while the central is connected:
    while (central.connected()) {
      long currentMillis = millis();
      
      if (currentMillis - previousMillis >= 200) { //Check values every 200ms
        previousMillis = currentMillis;

        int analogValue = analogRead(A1);
        analogReading.writeValue(analogValue);

        int digitalValue = digitalRead(2);
        digitalReading.writeValue(digitalValue);

      }
    }
    
    digitalWrite(LED_BUILTIN, LOW); // when the central disconnects, turn off the LED
    Serial.print("Disconnected from central: ");
    Serial.println(central.address());
  }
}
```

## Example

By now you should have a good understanding of how Bluetooth LE works and how you can use it together with your Arduino board. Below you will find an example showing how to use your smartphone to read analog values and send digital data to your Arduino board.

### Send / Read data using your smartphone

To access the Arduino board we are using an app called LightBlue, which is available for [Android](https://play.google.com/store/apps/details?id=com.punchthrough.lightblueexplorer&hl=en&pli=1) and [iOS](https://apps.apple.com/us/app/lightblue/id557428110).

Upload the following code:

```arduino
#include <ArduinoBLE.h>
BLEService newService("180A"); // creating the service

BLEUnsignedCharCharacteristic analogReading("2A58", BLERead | BLENotify); // creating the analog characteristic
BLEByteCharacteristic digitalReading("2A57", BLERead | BLEWrite); // creating the digital characteristic

long previousMillis = 0;

void setup() {
  Serial.begin(9600);    // initialize serial communication
  while (!Serial);       //starts the program if we open the serial monitor.

  pinMode(LED_BUILTIN, OUTPUT); // initialize the built-in LED pin to indicate when a central is connected

  //initialize ArduinoBLE library
  if (!BLE.begin()) {
    Serial.println("starting Bluetooth® Low Energy failed!");
    while (1);
  }

  BLE.setLocalName("Arduino Board"); //Setting a name that will appear when scanning for Bluetooth® devices
  BLE.setAdvertisedService(newService);

  newService.addCharacteristic(digitalReading); //add characteristics to a service
  newService.addCharacteristic(analogReading);

  BLE.addService(newService);  // adding the service

  digitalReading.writeValue(0); //set initial value for characteristics
  analogReading.writeValue(0);

  BLE.advertise(); //start advertising the service
  Serial.println(" Bluetooth® device active, waiting for connections...");
}

void loop() {
  
  BLEDevice central = BLE.central(); // wait for a Bluetooth® Low Energy central

  if (central) {  // if a central is connected to the peripheral
    Serial.print("Connected to central: ");
    
    Serial.println(central.address()); // print the central's BT address
    
    digitalWrite(LED_BUILTIN, HIGH); // turn on the LED to indicate the connection

    // check the battery level every 200ms
    // while the central is connected:
    while (central.connected()) {
      long currentMillis = millis();
      
      if (currentMillis - previousMillis >= 200) { // if 200ms have passed, we check the battery level
        previousMillis = currentMillis;

        int analogValue = analogRead(A1);
        analogReading.writeValue(analogValue);

        if (digitalReading.written()) {
          if (digitalReading.value()) {   // any value other than 0
            Serial.println("LED on");
            digitalWrite(LED_BUILTIN, HIGH);         // will turn the LED on
          } else {                              // a 0 value
            Serial.println(F("LED off"));
            digitalWrite(LED_BUILTIN, LOW);          // will turn the LED off
          }
        }

      }
    }
    
    digitalWrite(LED_BUILTIN, LOW); // when the central disconnects, turn off the LED
    Serial.print("Disconnected from central: ");
    Serial.println(central.address());
  }
}
```

Now you can start interacting with your board by following the steps as shown in the image below:

![LightBlue steps](./assets/bluetooth_app.png)

## Summary

In this article we explored the use of Arduino and the ArduinoBLE library for Bluetooth Low Energy communication, how to set up your board as either peripheral or central device and reading / sending data via Bluetooth LE. 

We highlighted the differences between Bluetooth Low Energy and Bluetooth Classic and finally provided an additional example showcasing how to use your smartphone for connecting to your Arduino board.