---
title: 'Getting Started with Nano Connector Carrier'
difficulty: beginner
description: 'This short guide takes you through the features of the Nano Connector Carrier, along with some important considerations when using this product.'
tags: [Prototyping]
author: 'Pedro Sousa Lima'
hardware:
  - hardware/03.nano/carriers/nano-connector-carrier
---

The Arduino Connector Carrier is a versatile expansion board designed for the Arduino Nano form factor. It provides an easy way to interface your Arduino Nano with various sensors, modules, and storage options through industry-standard connectors. This carrier board eliminates the need for complex wiring and breadboarding, allowing you to focus on your project's functionality rather than connectivity challenges.

![The Nano Connector Carrier](assets/cover.gif)

## Compatibility

The carrier is designed to work with all Arduino Nano form factor boards. Its standardized layout ensures compatibility with current and future Arduino Nano boards, giving you flexibility in your project development.

![Carrier With a Nano Board](assets/nano-formfactor.png)

## Features

The Arduino Connector Carrier comes packed with useful features to enhance your Arduino Nano projects:

### Voltage Level Switch

To ensure compatibility and as some Arduino Nano boards can be configured to change its voltage level the carrier includes a switch to select 3.3V or 5V voltage levels. The voltage selector switch allows you to choose the appropriate voltage for your specific Nano board and connected peripherals.

![Onboard Voltage Switch](assets/power-switch-01.gif)

This flexibility ensures compatibility with a wide range of sensors and modules that operate at different voltage levels, eliminating the need for additional level shifters in most cases.

### Connectors

The Carrier includes a both QWIIC and Grove connectors for expanding the board capability with external sensors aswell a MicroSD:
![Available Connectors](assets/connector-list.png)

#### Qwiic Connector

The carrier features a single Qwiic connector, allowing you to easily interface with Arduino Modulinos and other I²C-based sensors and modules.

![QWIIC Connector](assets/qwiic-01.gif)

The Qwiic connector uses a 4-pin JST SH connector with standardized pinout:

| Pin | Connection                               |
|-----|------------------------------------------|
| GND | Ground                                   |
| VCC | 3.3V/5V (selected by the voltage switch) |
| SDA | I²C Data (connected to A4 on the Nano)   |
| SCL | I²C Clock (connected to A5 on the Nano)  |

A single Qwiic connector is all you need since it's designed to be daisy-chainable, allowing you to connect multiple Modulinos or other Qwiic-compatible devices in series. This connector makes it plug-and-play simple to add sensors, displays, and other I²C devices to your project.

#### Grove Connectors

The board includes 4 Grove connectors, compatible with the extensive ecosystem of Grove modules.

![Grove Connector](assets/grove-01.gif)

Each Grove connector has a specific pin configuration:

**Grove (J5) - Analog**

| Pin | Connection                           |
|-----|--------------------------------------|
| GND | Ground                               |
| VCC | 5V or 3.3V (based on voltage switch) |
| A3  | Analog pin A3                        |
| A2  | Analog pin A2                        |

**Grove (J7) - Analog**

| Pin | Connection                           |
|-----|--------------------------------------|
| GND | Ground                               |
| VCC | 5V or 3.3V (based on voltage switch) |
| A1  | Analog pin A1                        |
| A0  | Analog pin A0                        |

**Grove (J4) - SPI**

| Pin  | Connection                           |
|------|--------------------------------------|
| GND  | Ground                               |
| VCC  | 5V or 3.3V (based on voltage switch) |
| MOSI | SPI MOSI (D11)                       |
| MISO | SPI MISO (D12)                       |

**Grove (J6) - I²C**

| Pin | Connection                           |
|-----|--------------------------------------|
| GND | Ground                               |
| VCC | 5V or 3.3V (based on voltage switch) |
| SDA | I²C Data (A4, shared with Qwiic)     |
| SCL | I²C Clock (A5, shared with Qwiic)    |

These standardized connectors eliminate the need for soldering or breadboarding and simplify connecting various sensors, actuators, and displays to your Arduino Nano.

#### Micro SD Card Slot

For projects requiring data logging or file storage, the carrier includes a Micro SD card slot.

![MicroSD Card Slot](assets/sd-card-01.gif)

The Micro SD card connects to the Arduino Nano through the SPI interface:

| SPI Signal | Arduino Pin                            |
|------------|----------------------------------------|
| MISO       | D12                                    |
| MOSI       | D11                                    |
| SCK        | D13                                    |
| CS         | D4 (default, configurable to D2 or D3) |

By default, pin D4 is used as the SPI SS (Chip Select) for the Micro SD card, but you can configure solder jumpers to use D2 or D3 instead if needed.

![SS Pin Selector Jumpers](assets/solder-jumper-01.gif)

With this feature, your Arduino Nano can read and write files on a Micro SD card, perfect for data logging applications, playing audio files, or storing configuration data.

## Pinout

The Arduino Connector Carrier features a comprehensive pinout that makes it easy to connect various peripherals to your Arduino Nano. The board is divided into two main sections:

![Nano Carrier Pinout](assets/ASX00061-pinout-v2.png)

The pinout includes clearly labeled connections for all interfaces:
- Arduino Nano pins (Digital and Analog)
- SPI interface pins
- I²C interface pins
- Power lines (5V, 3.3V, GND)
- UART/Serial pins

All connectors on the board are mapped to specific Arduino Nano pins, making it straightforward to program your projects. The voltage level switch affects all VCC pins on the Grove and Qwiic connectors, allowing you to match your peripherals voltage requirements.

## What to Do Next?

I'll add a snippet of the code to your section:

## What to Do Next?

### Example Project: Teamometer

The Teamometer is a practical demonstration of how different Modulino sensor modules can work together to solve a real-world problem. This project combines temperature sensing, LED visual feedback, button interaction, and audio alerts to create a smart tea temperature monitor. It's a fun way to see how easily the Connector Carrier can connect to different sensors and modules at once, giving you visual cues, sounds, and temperature readings all in one simple project even with different connectors.

![Teamometer overview](assets/teamometer.png)

**Components needed:**
- Modulino Buttons module
- Modulino Pixels module
- Modulino Thermo module
- Grove Buzzer sensor 
- Thick rubber band (for securing the Thermo module to your cup)
- Cup
- Your favorite tea

**Assembly instructions:**
1. Connect the Modulino Buttons, Pixels, and Thermo modules to your Arduino
2. Attach the Thermo module to the outside of your cup using the thick rubber band
3. Connect the Grove Buzzer sensor (connected to pin A0)
4. Upload the code provided below
5. Fill your cup with hot tea
6. Wait a few seconds to allow the temperature to transfer to the sensor
7. Press button A to begin monitoring

![Connection guide](assets/moduleConnection.png)

**Code Example:**
```Arduino
#include <Modulino.h>

// Create object instances
ModulinoThermo thermo;
ModulinoButtons buttons;
ModulinoPixels leds;

// Define temperature thresholds (in Celsius) feel free tpo change these as the heat transfer will depend a lot on your cup. Thermal paste can be added to improve this.
const float HOT_TEMP = 80.0;       // Fresh tea temperature
const float LUKEWARM_TEMP = 40.0;  // Ideal drinking temperature
const float ROOM_TEMP = 25.0;      // Room temperature

// Define pin for buzzer
const int BUZZER_PIN = A0;

// Variables to track state
bool measuring = false;    // Are we actively measuring temperature?
bool buzzing = false;      // Is the buzzer currently active?
int brightness = 25;       // LED brightness (0-255)

void setup() {
  Serial.begin(9600);
  
  // Initialize Modulino I2C communication
  Modulino.begin();
  
  // Detect and connect to modules
  thermo.begin();
  buttons.begin();
  leds.begin();
  
  // Set up buzzer pin as output
  pinMode(BUZZER_PIN, OUTPUT);
  
  // Initial message
  Serial.println("Tea Temperature Monitor");
  Serial.println("Press Button A to start monitoring");
  
  // Show all LEDs off initially
  leds.clear();
  leds.show();
}

void loop() {
  // Check for new button events
  if (buttons.update()) {
    // Check which button was pressed (0=A, 1=B, 2=C)
    if (buttons.isPressed(0)) {
      Serial.println("Button A pressed - Start measuring!");
      measuring = true;
    } else if (buttons.isPressed(1)) {
      Serial.println("Button B pressed - Stop buzzer!");
      // Turn off buzzer if it's on
      if (buzzing) {
        noTone(BUZZER_PIN);
        buzzing = false;
      }
    }
  }
  
  // If we're in measuring mode, check temperature
  if (measuring) {
    // Read temperature in Celsius from the sensor
    float celsius = thermo.getTemperature();
    
    Serial.print("Temperature (C): ");
    Serial.println(celsius);
    
    // Update the LED progress bar based on temperature
    updateTemperatureDisplay(celsius);
    
    // Check if tea has cooled to lukewarm
    if (celsius <= LUKEWARM_TEMP && celsius > ROOM_TEMP) {
      // Tea is ready to drink! Activate buzzer if not already buzzing
      if (!buzzing) {
        Serial.println("Tea is ready to drink!");
        tone(BUZZER_PIN, 1000); // 1kHz tone
        buzzing = true;
      }
    } 
    // If the tea is removed (temperature drops to near room temp)
    else if (celsius <= ROOM_TEMP) {
      // Turn off buzzer
      if (buzzing) {
        noTone(BUZZER_PIN);
        buzzing = false;
      }
      // Reset measuring state as tea is likely removed
      measuring = false;
      Serial.println("Tea removed or cooled to room temperature");
      Serial.println("Press Button A to start new measurement");
      leds.clear();
      leds.show();
    }
    
    // If tea is still too hot
    else if (celsius > LUKEWARM_TEMP) {
      // Ensure buzzer is off
      if (buzzing) {
        noTone(BUZZER_PIN);
        buzzing = false;
      }
    }
  }
  
  // Small delay to prevent reading too frequently
  delay(500);
}

// Function to update LED display based on temperature
void updateTemperatureDisplay(float celsius) {
  // Calculate how many LEDs to light based on temperature
  // Hotter = more LEDs lit
  
  // Map temperature range to LED count (0-8)
  // If temperature is at or above HOT_TEMP, all LEDs are on
  // If temperature is at or below ROOM_TEMP, no LEDs are on
  int ledCount = map(celsius * 100, ROOM_TEMP * 100, HOT_TEMP * 100, 0, 8);
  
  // Constrain to valid range
  ledCount = constrain(ledCount, 0, 8);
  
  // Update LEDs
  leds.clear(); // Use the class's built-in clear method
  
  // Light up LEDs based on temperature with color coding
  for (int i = 0; i < ledCount; i++) {
    // Choose color based on temperature ranges
    if (celsius >= 70) {
      // Very hot (70°C+): RED
      leds.set(i, RED, brightness);
    } else if (celsius >= 55) {
      // Hot (55-70°C): VIOLET
      leds.set(i, VIOLET, brightness);
    } else if (celsius >= LUKEWARM_TEMP) {
      // Warm (40-55°C): WHITE
      leds.set(i, WHITE, brightness);
    } else if (celsius >= 30) {
      // Getting cool (30-40°C): GREEN
      leds.set(i, GREEN, brightness);
    } else {
      // Cool (below 30°C): BLUE
      leds.set(i, BLUE, brightness);
    }
  }
  
  // Update the LEDs
  leds.show();
}
```

The temperature information will be displayed on both the serial console and the Modulino Pixels. As your tea cools, fewer LEDs will light up, and the colors will change from red (very hot) through violet, white, and green, to blue (cool). When your tea reaches the perfect drinking temperature, the buzzer will sound to let you know it's ready!

### Example Project: Motion Logger

The Motion Tracker demonstrates how the Nano Connector Carrier can integrate with the Movement sensor to record precise motion data. This project showcases real-time motion sensing, button control, and data logging to create a portable motion capture system that can be used for activity tracking, sports analysis, or interactive projects.

**Components needed:**
- Modulino Movement module
- Modulino Buttons module  
- SD card
- Nano Connector Carrier

**Assembly instructions:**
1. Connect the Modulino Movement and Buttons modules to your Nano Connector Carrier
2. Insert a micro SD card into the Nano Connector Carrier
3. Upload the code provided below
4. Open the serial monitor to view real-time motion data
5. Press button A to start recording motion data to the SD card
6. Move the sensor to capture the desired motion
7. Press button A again to stop recording

**Code Example:**
```Arduino
/*
 * Modulino Movement Logger
 *
 * Records movement data from a Modulino Movement sensor to an SD card.
 * Press Button A to start/stop recording.
 */
#include "Modulino.h"
#include <SD.h>

// Create objects for the modules
ModulinoMovement movement;
ModulinoButtons buttons;

// SD card configuration
#define SD_CS    4    // SD Card chip select (D4 on Modulino carrier)
File dataFile;

// Variables to track state
bool recordingActive = false;
unsigned long lastRecordTime = 0;
const unsigned long RECORD_INTERVAL = 100;  // Record every 100ms (10Hz)
String fileName = "/movement.csv";  // File name on SD card

// Movement data
float x, y, z;          // Acceleration
float roll, pitch, yaw; // Gyroscope

void setup() {
  // Initialize serial communication
  Serial.begin(115200);
  delay(1000);  // Give serial monitor time to connect
  
  Serial.println("===================================");
  Serial.println("Modulino Movement Logger");
  Serial.println("===================================");
  
  // Initialize Modulino I2C communication
  Modulino.begin();
  
  // Initialize modules
  movement.begin();
  buttons.begin();
  
  Serial.println("Press Button A to start/stop recording");
  
  // Initialize SD card
  Serial.print("Initializing SD card...");
  if (!SD.begin(SD_CS)) {
    Serial.println("SD card initialization failed!");
    Serial.println("Check connections and continue anyway.");
  } else {
    Serial.println("SD card initialized successfully.");
  }
  
  // Create CSV file with headers if it doesn't exist
  if (!SD.exists(fileName)) {
    dataFile = SD.open(fileName, FILE_WRITE);
    if (dataFile) {
      dataFile.println("Time,AccelX,AccelY,AccelZ,Roll,Pitch,Yaw");
      dataFile.close();
      Serial.println("Created new CSV file with headers");
    } else {
      Serial.println("Error creating file!");
    }
  } else {
    Serial.println("File exists, will append to it");
  }
  
  Serial.println("Setup complete!");
  Serial.println("===================================");
}

void loop() {
  // Read new movement data from the sensor (always do this to keep data current)
  movement.update();
  
  // Get acceleration and gyroscope values
  x = movement.getX();
  y = movement.getY();
  z = movement.getZ();
  roll = movement.getRoll();
  pitch = movement.getPitch();
  yaw = movement.getYaw();
  
  // Print current values to serial monitor
  Serial.print("A: ");
  Serial.print(x, 3);
  Serial.print(", ");
  Serial.print(y, 3);
  Serial.print(", ");
  Serial.print(z, 3);
  Serial.print(" | G: ");
  Serial.print(roll, 1);
  Serial.print(", ");
  Serial.print(pitch, 1);
  Serial.print(", ");
  Serial.println(yaw, 1);
  
  // Check for button presses
  if (buttons.update()) {
    // Check if button A was pressed (index 0)
    if (buttons.isPressed(0)) {
      // Toggle recording mode
      recordingActive = !recordingActive;
      
      if (recordingActive) {
        Serial.println("------------------------------------");
        Serial.println("RECORDING STARTED - Button A pressed");
        Serial.println("------------------------------------");
      } else {
        Serial.println("------------------------------------");
        Serial.println("RECORDING STOPPED - Button A pressed");
        Serial.println("------------------------------------");
      }
      
      // Small delay after button press to debounce
      delay(300);
    }
  }
  
  // If recording is active, save data to SD card at the specified interval
  if (recordingActive) {
    unsigned long currentTime = millis();
    if (currentTime - lastRecordTime >= RECORD_INTERVAL) {
      // Open the file for writing
      dataFile = SD.open(fileName, FILE_APPEND);
      
      if (dataFile) {
        // Write timestamp and movement data to CSV file
        dataFile.print(currentTime);
        dataFile.print(",");
        dataFile.print(x, 3);
        dataFile.print(",");
        dataFile.print(y, 3);
        dataFile.print(",");
        dataFile.print(z, 3);
        dataFile.print(",");
        dataFile.print(roll, 1);
        dataFile.print(",");
        dataFile.print(pitch, 1);
        dataFile.print(",");
        dataFile.println(yaw, 1);
        
        // Close the file
        dataFile.close();
      } else {
        Serial.println("Error opening file for writing");
      }
      
      lastRecordTime = currentTime;
    }
  }
  
  // Small delay to keep things responsive but not flood serial monitor
  delay(50);
}
```

The Motion Tracker continuously reads acceleration and orientation data from the Movement sensor, displaying it in real-time on the serial monitor. When recording is activated, the data is saved to a CSV file on the SD card, creating a detailed motion profile that can be analyzed later in spreadsheet software or data visualization tools. This project is perfect for capturing movement patterns, analyzing sports techniques, or creating interactive motion-controlled devices.


Now that you understand the features of the Arduino Connector Carrier, here are some exciting project ideas to get you started:

- **Weather Station**: Connect temperature, humidity, and pressure sensors via Grove connectors to create a simple weather monitoring system
- **Plant Monitor**: Use soil moisture and light sensors to monitor your houseplants and alert you when they need attention
- **Data Logger**: Use the Micro SD card slot to record sensor readings over time - perfect for environmental monitoring or tracking experiments
- **Smart Home Interface**: Create a hub that interfaces with multiple sensors around your home and logs data or sends alerts

For additional project inspiration, check out the Arduino Project Hub or join the Arduino community forums to share your creations and learn from others.

## Conclusion

The Arduino Connector Carrier transforms your Arduino Nano into a versatile platform capable of interfacing with numerous sensors, displays, and storage options. By eliminating complex wiring and providing standardized connectors, the carrier allows you to focus on developing your application rather than dealing with connection issues.