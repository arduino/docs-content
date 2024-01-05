---
title: "IoT Smart Garden Setup with MKR IoT Carrier"
description: "Build a smart garden setup with the MKR IoT Carrier, a pump, and a moisture sensor."
tags: [IoT Cloud, Water Pump, Moisture Sensor, Temperature, Humidity]
difficulty: beginner
author: "Jacob Hylén, Hannes Siebeneicher, Karl Söderby"
---

![Smart garden setup with MKR IoT Carrier.](assets/hero-image.png)

Decorating your home with plants is an easy way to bring some life into your day-to-day. The only problem is - those plants need water to survive, and if you forget to pay attention to them for a while you may need to start over. So instead of staying ever vigilant, why don't you spend an afternoon creating a setup that will let you both monitor the amount of moisture in your plants soil, and water your plants from afar using the [Arduino Cloud](https://docs.arduino.cc/cloud/iot-cloud)?

## How It Works

The MKR IoT Carrier has built in relays that can let you control circuits that are powered separately. In this tutorial we will be using one of the relay modules on the carrier to control a pump that can provide one of your plants with water from the Arduino Cloud thanks to the functionality of the [Arduino MKR WiFi 1010](https://store.arduino.cc/products/arduino-mkr-wifi-1010). 

We will also connect a soil moisture sensor, and together with the sensors onboard the MKR IoT Carrier, we will create a sophisticated smart garden setup, capable of:

- Remote watering of a plant **(with a pump)**.
- Check the moisture of your plant **(with a moisture sensor)**.
- Check the temperature/humidity **(using the onboard HTS221 sensor)**.

![Live data streamed to the Arduino Cloud.](assets/cloud-dashboard.gif)

## Hardware & Software Needed

- [MKR WiFi 1010](https://store.arduino.cc/products/arduino-mkr-wifi-1010)
- [MKR IoT Carrier](https://store.arduino.cc/products/arduino-mkr-iot-carrier)
- 5V submersible pump.
- 1 meter watering pipe.
- Water container.
- USB adapter with at least 2 USB ports.
- Micro-USB cable.
- Open ended USB Cable.
- [Soil moisture sensor](https://store.arduino.cc/products/grove-moisture-sensor).

### Apps and Online Services

- [Arduino Cloud](https://docs.arduino.cc/cloud/iot-cloud)

## Hardware & Circuit Assembly

Begin by connecting the MKR WiFi 1010 board to the MKR IoT Carrier. Then, we need to connect the moisture sensor via a Grove cable to the "A6" connector.

From the open ended USB cable, connect the positive wire (+) directly to relay 1 on the carrier, labelled "NO" (normally open). Connect the negative wire (-) together with the pump's negative wire. 

Finally, connect the pump's positive wire, to the "COM" (common) pin on the relay. As a result, you have created a circuit that can be switched on/off via a relay. See next section for the full circuit.

### Circuit

Below is the complete circuit for this setup.

![Circuit for this project.](assets/circuit.png)

To connect the wires to the relay, see the image below:

![Connecting the wires to relay 1.](assets/relay-connection.png)

***Tip: to connect the power, pump & relay, you can use a connector strip. This will make your connections much more reliable & sturdy.*** 

## IoT Cloud Setup

***If you are new to the Arduino Cloud, please refer to the [Getting Started Guide](https://docs.arduino.cc/cloud/iot-cloud/tutorials/iot-cloud-getting-started) or visit the [full documentation](https://docs.arduino.cc/cloud/iot-cloud) to learn more about the service.*** 

Begin by navigating to the [Arduino Cloud](https://create.arduino.cc/iot/things). You will need to have a registered account with Arduino to use it. Follow the steps below to set up the Arduino Cloud. 

**1.** Create a new Thing, and select/configure the MKR WiFi 1010 board. Note that the board needs to be connected to your computer during this setup.

**2.** Create variables according to the table below:

| Name        | Data Type | Function                               | Permission   |
| ----------- | --------- | -------------------------------------- | ------------ |
| watering    | boolean   | Activate / de-activate pump            | Read & Write |
| waterTime   | int       | How long the pump should run (seconds) | Read & Write |
| moisture    | int       | Read moisture                          | Read Only    |
| temperature | float     | Read temperature                       | Read Only    |
| humidity    | float     | Read humidity                          | Read Only    |

**3.** Enter your credentials to your Wi-Fi network in the network section. 

**4.** Your Thing overview should now look like the following:

![Thing overview complete.](assets/thing-overview.png)

**5.** Go to the sketch tab, and use the following code:

```arduino
/*
  MKR IoT Carrier Smart Garden Setup Project

  A setup that allows for remote/local control of
  a pump, as well as reading sensors (moisture,
  temperature, humidity).

  Built using the Arduino Cloud service.

  Components used:
  - MKR WiFi 1010
  - MKR IoT Carrier
  - Moisture Sensor
  - 5V water pump
  - USB Adapter with 2x slots
  - Micro USB Cable
  - Open ended USB Cable
  - Grove cable 

  Code by (c) Alessandro Ranelucci for Arduino.
*/

#include "arduino_secrets.h"
#include "thingProperties.h"

#include <Arduino_MKRIoTCarrier.h>
#include <Arduino_OplaUI.h>

const int moistPin = A6;

unsigned long startedWatering;

MKRIoTCarrier opla;
CycleWidgetsApp app;
Gauge2_Widget moistureWidget;
Bool_Widget wateringToggleWidget;

void setup() {
  Serial.begin(9600);
  delay(1500);

  // Make sure the pump is not running
  stopWatering();

  // Connect to Arduino Cloud
  initProperties();
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);
  setDebugMessageLevel(4);
  ArduinoCloud.printDebugInfo();

  // Configure widgets
  moistureWidget.attachValue(moisture);
  moistureWidget.setTitle("MOISTURE");
  moistureWidget.setRange(0, 100);
  moistureWidget.setDigits(0);
  moistureWidget.setSuffix(" %");
  moistureWidget.setReadOnly(true);

  wateringToggleWidget.attachValue(watering);
  wateringToggleWidget.setTitle("PUMP");
  wateringToggleWidget.onValueChange(onWateringChange);
  
  // Initialize Oplà
  CARRIER_CASE = true;
  opla.begin();

  // Initialize the widget application
  app.begin(opla);
  app.addWidget(moistureWidget);
  app.addWidget(wateringToggleWidget);
}

void loop() {
  ArduinoCloud.update();
  app.loop();
  
  // Read the sensor and convert its value to a percentage 
  // (0% = dry; 100% = wet)
  int raw_moisture = analogRead(moistPin);
  moisture = map(raw_moisture, 0, 1023, 0, 100);

  temperature = opla.Env.readTemperature();
  humidity = opla.Env.readHumidity();

  // Set the LED color according to the moisture percentage
  if (moisture > 40) {
    opla.leds.setPixelColor(1, 50, 0 , 0);  // green
  } else if (moisture > 10) {
    opla.leds.setPixelColor(1, 50, 50 , 0); // yellow
  } else {
    opla.leds.setPixelColor(1, 0, 50 , 0);  // red
  }
  opla.leds.show();
  
  // Stop watering after the configured duration
  if (watering && (millis() - startedWatering) >= waterTime*1000) {
    stopWatering();
  }
  
  delay(100);
}

// This function is triggered whenever the server sends a change event,
// which means that someone changed a value remotely and we need to do
// something.
void onWateringChange() {
  if (watering) {
    startWatering();
  } else {
    stopWatering();
  }
}

void startWatering () {
  watering = true;
  startedWatering = millis();
  opla.Relay2.open();
}

void stopWatering () {
  watering = false;
  opla.Relay2.close();
}

void onWaterTimeChange()  {
  // Add your code here to act upon WaterTime change
}
```

**6.** Upload the code. When successful, you can navigate over to the **"Dashboards"** section. Create a new dashboard.

**7.** Inside the dashboard view, click on **"Add"** then **"Things"** and select your Thing. This will generate a list of widgets and you can click on **"Create Widget"** to complete it. You should now see something similar to this dashboard:

![Dashboard overview.](assets/dashboard-overview.png)

Once you see the values changing, we know that the connection is successful, and we can monitor and interact with our device.

***In this dashboard, we replaced some of the widgets with nicer representations, like gauges and percentage.***

## Final Setup

We have now assembled the hardware + configured the Arduino Cloud, and we are ready to start using our setup. Now, let's start using it.

**1.** If you have confirmed that the connection works, we can unplug the setup from the computer, and move it to the plant we want to monitor.

**2.** Place the moisture sensor into the soil of the plant.

![Moisture sensor in a plant.](assets/soil-sensor.png)

**3.** Place the pump inside a water container. Attach the plastic pipe to the pump, and place the other end into the plant pot. Place the MKR IoT Carrier next to the plant. Your setup could now look like this:

![Plant setup.](assets/smart-garden-setup.png)

**4.** Finally, plug in the USB adapter into the wall. This will now power the MKR IoT Carrier, which should now connect to the IoT Cloud, via your Wi-Fi network. And that is it, you now have a Smart Garden setup! 

## Usage

Let's take a look at what our Smart Garden can do. To control it, we can either use the dashboard in the Arduino Cloud, or the Arduino Remote app ([Playstore](https://play.google.com/store/apps/details?id=cc.arduino.cloudiot&hl=en&gl=US) / [Appstore](https://apps.apple.com/us/app/arduino-iot-cloud-remote/id1514358431)).

![Control and monitor your Smart Garden!](assets/cloud-dashboard.gif)

***In this dashboard, we have also added a chart widget for each of the variables we monitor.***

**Watering:** to activate the pump, do the following:
- Select number of seconds that you want the pump to run for.
- Click on the switch widget. The pump will now run for `x` amount of seconds, and then it will turn off.
- You can also activate the pump through the MKR IoT Carrier. This is done via the touch buttons.

**Moisture:** monitor the moisture of your plant: if it is low, turn on the pump, and watch the moisture levels rise. The moisture of your plant can be viewed in the Cloud dashboard, on the carrier's display or through the LED indicator (red is bad, green is good).

**Display, buttons:** you can also view the moisture level locally, and activate the pump through the capacitive buttons. 

**Temperature:** check temperature levels. Note that this may be inaccurate if placed directly in a sunny window!

**Humidity:** measure the relative humidity of your room. Some plants like it dry; some doesn't!

## Conclusion

With a smart garden setup, you can easily monitor the environment of your plant, and water it remotely. In this tutorial, we have gone through the basic elements needed for achieving just that: but there are more things you can do. Below is a list of some fun ideas that you can do with your plant:

- **Automatic watering** - instead of watering your plant remotely, you can also activate the pump automatically whenever moisture drops too low. We do however think it is more fun to control it from a phone, but the choice is yours.
- **Cooling/heating fan** - you can use the other relay to connect a cooling/heating fan. This can help you bring the temperature to a perfect level (some plants like it cold, some hot).
- **Humidifier** - a humidifier is an awesome component that increases the humidity (a perfect combo with the humidity sensor).
- **UV lights** - a UV light allows you to grow plants even when there's no natural sun light.





