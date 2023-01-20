---
title: Home Automation
description: Documented examples for connecting your home, office & school.
author: Karl Söderby
---

**Home Automation** is an exciting topic to get into, and it is all about making smart solutions using technology to "automate your home". The Arduino IoT Cloud is a service that makes it simple for you to configure, deploy, monitor and interact with your Arduino devices. 

In this article, we will list out a series of examples that could become your next Home Automation project, along with code examples, circuits and a suggestion for bill of materials. 

***To follow this guide we recommend that you know how the Arduino IoT Cloud works. Below is a list of some essential resources to read through if you need help setting up.***

- [Getting Started with the Arduino IoT Cloud]() - overview of the service.
- [IoT Cloud Variables]() - how to use cloud variables that are shared between an Arduino and the Cloud. 
- [IoT Cloud Dashboards]() - setting up dashboards to monitor and control your devices.


## Temperature & Humidity Sensor

**Material required:**
- Arduino Cloud enabled board.
- Temp/humidity sensor.

Temperature & humidity sensing is an easy implementation that is inexpensive and quick to setup. This example is configured for the very popular **DHT11** temp/humidity sensor, but can be easily tweaked to fit other sensors.

To set it up in the Arduino Cloud, use the following circuit, cloud configuration, & code:

![DHT11 circuit.](assets/dht11.png)

| Variable     | Name          | Permission  |
| ------------ | ------------- | ----------- |
| float/double | `temperature` | `Read Only` |
| float/double | `humidity`    | `Read Only` |

```arduino
#include "thingProperties.h"
#include <dht.h>

dht DHT; 

#define DHT11_PIN 2 

void setup() {
  Serial.begin(9600);

  delay(1500); 

  initProperties();

  ArduinoCloud.begin(ArduinoIoTPreferredConnection);
}

void loop() {
  ArduinoCloud.update();

  humidity = dht.readHumidity();
  temperature = dht.readTemperature();
}
```

## Smart Switch

**Material required:**
- Arduino Cloud enabled board.
- Relay module.

Smart switches are great for control of your home, and can be helpful to minimize electricity costs and provide a comfortable way of switching on & off your appliances. 

This example demonstrates simply how to turn on/off a circuit using a relay connect to pin 2. 

To set it up in the Arduino Cloud, use the following circuit, cloud configuration, & code:

**Circuit:**

![DHT11 circuit.](assets/dht11.png)

***Warning: if you are intending to switch higher voltages, please get in touch with a professional.***

**Configuration:**

| Variable | Name          | Permission     |
| -------- | ------------- | -------------- |
| bool     | `smartSwitch` | `Read & Write` |

**Code:**

```arduino
#include "thingProperties.h"

void setup() {
  Serial.begin(9600);

  delay(1500); 

  initProperties();

  ArduinoCloud.begin(ArduinoIoTPreferredConnection);
}

void loop() {
  ArduinoCloud.update();
}

void onSmartSwitch(){
  if(smartSwitch){
    digitalWrite(2, HIGH);
  }
  else {
    digitalWrite(2, LOW);
  }
}
```

## Pump Watering System

## Climate Control

## Energy Monitor (Current Sensor)

**Material required:**
- Arduino Cloud enabled board.
- Current sensor module.

Current sensor modules can be used to monitor your energy consumption.

In this example we will setup a current sensor module based on the XXXX chip, that reads the current and converts it into a voltage that can be read through an analog pin.  

To set it up in the Arduino Cloud, use the following circuit, cloud configuration, & code:

**Circuit:**

![DHT11 circuit.](assets/dht11.png)

***Warning: if you are intending to switch higher voltages, please get in touch with a professional.***

**Configuration:**

| Variable | Name          | Permission     |
| -------- | ------------- | -------------- |
| float    | `raw`         | `Read Only`    |
| float    | `ampere`      | `Read Only`    |
| int      | `voltage`     | `Read & Write` |
| float    | `kWh`         | `Read`         |
| float    | `price`       | `Read & Write` |
| float    | `costPerHour` | `Read Only`    |

**Code:**

```arduino
#include "thingProperties.h"

void setup() {
  Serial.begin(9600);

  delay(1500); 

  initProperties();

  ArduinoCloud.begin(ArduinoIoTPreferredConnection);
}

void loop() {
  ArduinoCloud.update();

  raw = analogRead(A0);  
  ampere = (raw / 3.3);
  kWh = ampere * voltage;
  costPerHour = price * kWh;
  
}
```

**More examples:**

- [Energy Monitor with Arduino IoT Cloud & Modbus protocol](). 

## 




