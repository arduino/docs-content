---
title: 'Environmental Monitoring with the Nicla Sense Env'
description: "This application note describes how to implement a simple environmental monitor with the Nicla Sense."
difficulty: intermediate
compatible-products: [nicla-sense-env]
tags:
  - Environmental monitor
  - Air quality
  - Application note
  - Nicla Sense Env
  - Portenta C33
author: 'José Bagur'
hardware:
  - hardware/04.pro/boards/portenta-c33
  - hardware/06.nicla/boards/nicla-sense-env
software:
  - ide-v1
  - ide-v2
  - IoT-Cloud
---

## Introduction

Air pollution is a growing concern in urban and industrial areas due to the harmful effects of airborne pollutants such as airborne particulate matter (PM), nitrogen dioxide (NO2), and ozone (O3) on human health and the environment. This application note presents the development of an outdoor air quality monitor using the Portenta C33, the Nicla Sense Env and the PMS7003 sensor, which measures PM2.5 and PM10 levels. The environmental monitor provides real-time data on temperature, humidity, concentrations of NO2 and O3, and the outdoor air quality index (AQI), making it suitable for use in urban areas, industrial zones, or environmental research.

## Goals

The main goals of this application note are as follows:

- Develop a simple outdoor air quality monitor that provides real-time data on temperature, humidity, and pollutants such as nitrogen dioxide (NO2), ozone (O3) and airborne particulate matter (PM 2.5 and PM 10).
- Interface the Portenta C33 board with the Nicla Sense Env and the PMS7003 sensor to measure environmental parameters, including airborne particulate matter and gas pollutants.
- Collect accurate readings of NO2, O3 and the outdoor air quality index (AQI) to assess overall outdoor air quality.
- Display real-time Arduino IDE Serial Monitor data for immediate observation and analysis.
- Establish a connection to the Arduino Cloud to enable remote monitoring and data analysis of the collected air quality data.

## Hardware and Software Requirements

### Hardware Requirements

- [Portenta C33](https://store.arduino.cc/products/portenta-c33) (x1)
- [Nicla Sense Env](https://store.arduino.cc/products/nicla-sense-env) (x1)
- PMS7003 airborne particulate matter sensor (x1)
- USB-C® cable (x1)
- Wi-Fi® W.FL antenna (x1)

### Software Requirements

- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2.0+](https://www.arduino.cc/en/software), or [Arduino Cloud Editor](https://create.arduino.cc/editor).
- For the Wi-Fi® connectivity feature of Portenta C33, we will use the [Arduino Cloud](https://create.arduino.cc/iot/things). If you do not have an account, create one for free [here](https://cloud.arduino.cc/).
- The [environmental monitor example sketch](assets/environmental_monitor.zip).

## Hardware Setup Overview

The electrical connections of the proposed environmental monitor are shown in the diagram below:

![Environmental monitor electrical connections overview](assets/C33_application_4.png)

The diagram illustrates the connection of all the environmental monitor's components. The Portenta C33 is the monitor's main controller; the Nicla Sense Env board provides temperature, humidity, and outdoor air quality data, while the PMS7003 sensor provides airborne particulate matter data. 

The Nicla Sense Env is connected to the Portenta C33 via ESLOV and the PMS7003 via Serial. The monitor has one main voltage bus (+5 VDC from the Portenta C33) that powers both the Nicla Sense Env and the PMS7003 sensor. The Portenta C33 is powered through its onboard USB-C port for testing purposes.

## Understanding Outdoor Air Quality

Air pollution is not just a problem in urban areas; rural environments also face significant risks from pollutants like nitrogen dioxide (NO2) and ozone (O3). These gases and particulate matter (PM) pose serious health risks, especially for vulnerable populations. NO2, produced by combustion engines and industrial processes, can travel far beyond urban centers. O3, formed by atmospheric chemical reactions, affects urban and rural regions, especially during warmer seasons.

Real-time monitoring is critical in urban and rural settings to manage exposure to these pollutants properly. Air quality tracking helps individuals and communities proactively reduce health risks.

### The Role of Sensors in Air Quality Monitoring

This application note uses modern sensors to provide accurate, real-time measurements of various pollutants. The Nicla Sense Env, with the PMS7003 sensor, offers an interesting solution for monitoring outdoor air quality:

- **Particulate Matter (PM2.5 and PM10)**: Measures fine particles suspended in the air, which can penetrate the lungs and cause health problems.
- **NO2 Sensor**: Detects nitrogen dioxide, a harmful gas released by vehicles and industrial activities.
- **O3 Sensor**: Measures ozone, a gas that forms in the atmosphere through reactions between pollutants and sunlight, contributing to respiratory problems.
- **Outdoor Air Quality Index (AQI)**: The AQI simplifies the interpretation of air quality by combining data from multiple pollutants (PM, NO2, O3) into a single value. This index is based on a scale that ranges from 0 to 500, where:
  - 0-50 indicates good air quality.
  - 51-100 is moderate.
  - 101-150 is unhealthy for sensitive groups.
  - 151-200 is unhealthy for everyone.
  - 201-300 is very unhealthy.
  - 301-500 signals hazardous conditions.

The AQI makes it easy to understand how outdoor air quality might affect public health, particularly when pollutant levels rise to unhealthy levels.

Monitoring PM, NO2, O3, and AQI in real-time allows for immediate responses when air quality worsens. This is especially important in rural areas with less visible air quality issues. The data collected can be sent to platforms like Arduino Cloud, enabling remote monitoring and long-term trend analysis, improving public awareness and policy decisions.

## Environmental Monitor Example Sketch

Now that we have covered the hardware components of our environmental monitor and how they are interconnected, let's study the software that brings this monitor to life. The example sketch in the following section manages data collection from the Nicla Sense Env board and the PMS7003 sensor connected to the Portenta C33 board, allowing us to monitor real-time environmental data such as temperature, humidity, outdoor air quality, and particulate matter concentrations.

This section breaks down the provided example sketch, guiding you through its functionality. We will explore how the sensors are initialized, how the data is collected every 10 seconds, and how the results are displayed in the Arduino IDE's Serial Monitor. 

The complete example sketch is shown below.

```arduino
/**
  Outdoor Air Quality Monitoring with Arduin
  Name: outdoor_air_quality_monitor.ino
  Purpose: This sketch reads temperature, humidity, outdoor air quality,
  and particulate matter (PM 2.5 and PM 10) from the Nicla Sense Env
  and a PMS7003 sensor from Plantower connected to the Portenta C33 board. 
  The data is reported Arduino IDE's Serial Monitor every 10 seconds.
  
  @version 1.0 01/09/24
  @author Arduino Product Experience Team
*/

// Include the necessary libraries for Nicla Sense Env and PMS7003 sensors
#include "Arduino_NiclaSenseEnv.h"
#include "PMS.h"

// PMS sensor object for particle matter measurements
PMS pms(Serial);

// Time interval (in milliseconds) for sensor readings of 10 seconds
static const uint32_t READ_INTERVAL = 10000; 
uint32_t lastReadTime = 0;

// Sensor objects for Nicla Sense Env data (using pointers)
NiclaSenseEnv device;
TemperatureHumiditySensor* tempHumSensor;
OutdoorAirQualitySensor* airQualitySensor;

/**
  Initializes the sensors and serial communication.
  Configures the Nicla Sense Env board to enable the onboard
  temperature/humidity sensor and the onboard outdoor air 
  quality sensor.
*/
void setup() {
    // Initialize serial communication at 115200 bits per second.
    Serial.begin(115200);
    
    // Wait for Serial to be ready with a timeout of 5 seconds
    for(auto start = millis(); !Serial && millis() - start < 5000;); 

    // Initialize NiclaSenseEnv sensors
    if (device.begin()) {
        Serial.println("- Nicla Sense Env is connected");

        // Get the temperature and humidity sensor (use pointer)
        tempHumSensor = &device.temperatureHumiditySensor();

        // Get and enable the outdoor air quality sensor (use pointer)
        airQualitySensor = &device.outdoorAirQualitySensor();
        airQualitySensor->setEnabled(true);  
    } else {
        // Error message if the Nicla Sense Env is not found
        Serial.println("- ERROR: Nicla Sense Env device not found!");
    }

    // Initialize PMS7003 sensor in passive mode
    pms.passiveMode();
    pms.wakeUp();
}

/**
  Main loop that reads sensor data every 10 seconds.
  This function continuously checks the time interval and calls
  the displayAllData() function to print sensor readings.
*/
void loop() {
    // Get the current time (in milliseconds)
    uint32_t currentTime = millis();

    // Read sensors every 10 seconds and update the last read time
    if (currentTime - lastReadTime >= READ_INTERVAL) {
        lastReadTime = currentTime;  

        // Read and display all sensor data in a single line
        displayAllData();
    }
}

/**
  Displays temperature, humidity, air quality, and particulate matter data.
  Reads data from the Nicla Sense Env and PMS7003 sensors and prints it in a single line format.
*/
void displayAllData() {
    // Check if both temperature/humidity and air quality sensors are enabled
    if (tempHumSensor->enabled() && airQualitySensor->enabled()) {
        // Read data from the Nicla Sense Env sensors
        float temperature = tempHumSensor->temperature();
        float humidity = tempHumSensor->humidity();
        int airQualityIndex = airQualitySensor->airQualityIndex();
        float NO2 = airQualitySensor->NO2();
        float O3 = airQualitySensor->O3();

        // Read data from the PMS7003 sensor
        PMS::DATA data;
        pms.requestRead();
        if (pms.readUntil(data)) {
            // Print all sensor data in a single line, separated by commas
            Serial.print("- Temperature: ");
            Serial.print(temperature, 2);
            Serial.print(" °C, Humidity: ");
            Serial.print(humidity, 2);
            Serial.print(" %, Air Quality Index: ");
            Serial.print(airQualityIndex);
            Serial.print(", NO2: ");
            Serial.print(NO2, 2);
            Serial.print(" ppb, O3: ");
            Serial.print(O3, 2);
            Serial.print(" ppb, PM 2.5: ");
            Serial.print(data.PM_AE_UG_2_5);
            Serial.print(" µg/m³, PM 10: ");
            Serial.println(data.PM_AE_UG_10_0);
        } else {
            // Error message if PMS7003 data is not available
            Serial.println("- ERROR: No data from PMS sensor!");
        }
    } else {
        // Error message if one or more sensors are disabled
        Serial.println("- ERROR: One or more sensors are disabled!");
    }
}
```

The following sections will help you to understand the main parts of the example sketch shown before, which can be divided into the following:

- Library imports
- Sensors initialization
- Data collection
- Data display

### Library Imports

The first step is to ensure that all necessary libraries are included to control the Nicla Sense Env board and the PMS7003 sensor. These libraries provide all the functionality to communicate with and extract sensor data.

```arduino
// Include the necessary libraries for Nicla Sense Env and PMS7003 sensors
#include "Arduino_NiclaSenseEnv.h"
#include "PMS.h"

// PMS sensor object for particle matter measurements
PMS pms(Serial);

// Time interval (in milliseconds) for sensor readings of 10 seconds
static const uint32_t READ_INTERVAL = 10000; 
uint32_t lastReadTime = 0;

// Sensor objects for Nicla Sense Env data (using pointers)
NiclaSenseEnv device;
TemperatureHumiditySensor* tempHumSensor;
OutdoorAirQualitySensor* airQualitySensor;
```

The Nicla Sense Env library handles data such as temperature, humidity, and outdoor air quality, while the PMS7003 library enables the measurement of airborne particulate matter.

### Sensors Initialization

The `setup()` function initializes the monitor sensors and prepares them to start collecting data. This is where the sensors "wake up" and prepare to make measurements.

```arduino
void setup() {
    // Initialize serial communication at 115200 bits per second.
    Serial.begin(115200);
    
    // Wait for Serial to be ready with a timeout of 5 seconds
    for(auto start = millis(); !Serial && millis() - start < 5000;); 

    // Initialize NiclaSenseEnv sensors
    if (device.begin()) {
        Serial.println("- Nicla Sense Env is connected!");

        // Get the temperature and humidity sensor (use pointer)
        tempHumSensor = &device.temperatureHumiditySensor();

        // Get and enable the outdoor air quality sensor (use pointer)
        airQualitySensor = &device.outdoorAirQualitySensor();
        airQualitySensor->setEnabled(true);  
    } else {
        // Error message if the Nicla Sense Env is not found
        Serial.println("- ERROR: Nicla Sense Env device not found!");
    }

    // Initialize PMS7003 sensor in passive mode
    pms.passiveMode();
    pms.wakeUp();
}
```

In the code snippet shown before:

- Serial communication is initialized to allow data transmission.
- The Nicla Sense Env board is initialized to read temperature, humidity, and outdoor air quality.
- The PMS7003 sensor is configured in passive mode, which means it will only take readings when specifically requested.

### Data Collection

Once the sensors are ready, the example sketch must continuously collect data. The `loop()` function ensures that data is captured every 10 seconds and sent to the IDE's Serial Monitor.

```arduino
void loop() {
    // Get the current time (in milliseconds)
    uint32_t currentTime = millis();

    // Read sensors every 10 seconds and update the last read time
    if (currentTime - lastReadTime >= READ_INTERVAL) {
        lastReadTime = currentTime;  

        // Read and display all sensor data in a single line
        displayAllData();
    }
}
```

In the code snippet shown before:

- A time-based condition ensures that readings are taken every 10 seconds.
- Calls the `displayAllData()` function every 10 seconds to gather and print sensor data to the IDE's Serial Monitor.

### Data Display

The `displayAllData()` function pulls together the data from each sensor and displays it in a single line on the IDE's Serial Monitor. This is the most dynamic part of the example sketch, where the sensors provide real-time readings.

```arduino
void displayAllData() {
    // Check if both temperature/humidity and air quality sensors are enabled
    if (tempHumSensor->enabled() && airQualitySensor->enabled()) {
        // Read data from the Nicla Sense Env sensors
        float temperature = tempHumSensor->temperature();
        float humidity = tempHumSensor->humidity();
        int airQualityIndex = airQualitySensor->airQualityIndex();
        float NO2 = airQualitySensor->NO2();
        float O3 = airQualitySensor->O3();

        // Read data from the PMS7003 sensor
        PMS::DATA data;
        pms.requestRead();
        if (pms.readUntil(data)) {
            // Print all sensor data in a single line, separated by commas
            Serial.print("- Temperature: ");
            Serial.print(temperature, 2);
            Serial.print(" °C, Humidity: ");
            Serial.print(humidity, 2);
            Serial.print(" %, Air Quality Index: ");
            Serial.print(airQualityIndex);
            Serial.print(", NO2: ");
            Serial.print(NO2, 2);
            Serial.print(" ppb, O3: ");
            Serial.print(O3, 2);
            Serial.print(" ppb, PM 2.5: ");
            Serial.print(data.PM_AE_UG_2_5);
            Serial.print(" µg/m³, PM 10: ");
            Serial.println(data.PM_AE_UG_10_0);
        } else {
            // Error message if PMS7003 data is not available
            Serial.println("- ERROR: No data from PMS sensor!");
        }
    } else {
        // Error message if one or more sensors are disabled
        Serial.println("- ERROR: One or more sensors are disabled!");
    }
}
```

In the code snippet shown before:

- The function first checks that the temperature/humidity sensor and the air quality sensor are enabled.
- The function retrieves temperature, humidity, air quality index, and gas concentrations (NO2 and O3) from the Nicla Sense Env board.
- The function also fetches PM2.5 and PM10 particulate readings from the PMS7003 sensor.
- Finally, the data is printed in a single line on the IDE's Serial Monitor.
  
### Complete Example Sketch

The complete example sketch can be downloaded [here](assets/environmental_monitor.zip).

## Conclusions

The development of this outdoor air quality monitor demonstrates the effectiveness of using affordable and accessible sensors to measure key environmental parameters in real-time. Integrating the Nicla Sense Env and the PMS7003 sensor with the Portenta C33 allows the system to track temperature, humidity, airborne particulate matter (PM2.5 and PM10), NO2, and O3 levels. The ability to monitor these pollutants, combined with the outdoor AQI, provides valuable insights for understanding air quality in urban and rural areas. Furthermore, the system's connection to the Arduino Cloud allows for remote monitoring and analysis, making it versatile for various applications, from personal use to environmental research.

## Next Steps

Several improvements can be considered to extend the functionality of the environmental monitor:

- Add sensors to measure pollutants such as carbon monoxide (CO) or sulfur dioxide (SO2).
- Improve the monitor's energy efficiency for long-term deployment in remote or outdoor environments.
- Build a custom dashboard on Arduino Cloud to visualize trends over time and allow for more detailed analysis of air quality data.
- Implement an alert system that notifies users when pollutant levels exceed safe thresholds.
- Scale the system for use in different geographical regions to collect comparative data on air quality.