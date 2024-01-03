---
title: APIs Overview
description: Arduino Cloud has two different set of APIs - Application and Device API.
author: Karl Söderby, Fabrizio Mirabito
tags: [Arduino Cloud, Device API, Application API, JavaScript]
---

The [Arduino Cloud](https://app.arduino.cc/) has different sets of APIs that provide different functionalities. This article serves as an introduction to how to work and what you can achieve with them.

## Application API

The main goal of the Application API is to allow you to create and manage IoT resources like dashboards, devices, things, and variables, along with the retrieval and handling of historical data coming from your IoT Devices. 

The core of those APIs is organized around  [REST](http://en.wikipedia.org/wiki/Representational_State_Transfer). Our API has predictable resource-oriented URLs, accepts  [form-encoded](https://en.wikipedia.org/wiki/POST_(HTTP)#Use_for_submitting_web_forms)  request bodies, returns  [JSON-encoded](http://www.json.org/) responses, and uses standard HTTP response codes, authentication, and verbs. 

You can use those APIs, both directly calling our HTTP endpoints or using our clients that wrap those calls into easy-to-use abstractions like objects and functions. We have Applications API clients available in `javascript`, `golang`, and `python`. To use the Application API, you need to create an **API Key** in the [API Keys](https://cloud.arduino.cc/api-keys) section.

With this API, you can:
- Build an automated script to create your things, in bulk
- Duplicate the configuration of things, dashboards, devices
- Create your own personal web application to manage your resources
- Build a script that reads your variables' data and provides custom analytics 

### Resources

You can find the full list of available resources and actions in the [Arduino Cloud Application API Technical Reference](https://www.arduino.cc/reference/en/iot/api/).

***For learning how to successfully authenticate and interface with this API, visit the [Arduino Cloud REST API & SDK](https://docs.arduino.cc/arduino-cloud/getting-started/arduino-iot-api) article. Examples using JavaScript, Python and Golang are available here.***

## Device API

The **Device API** allows sending and receiving any kind of data (sensors' values, commands for actuators, configuration changes...) from and to IoT Devices and the Cloud. Under the hood, they:

- take care of the data exchange with our MQTT broker
- handle best in class authentication & security 
- manage compression, data format, and transport protocols

With this API, you can:
- Send sensors' values to the cloud
- Send and receive input and commands from and to dashboards
- Listen for variables' values changes and act upon them

As a wrapper for the Device API, we have the following libraries:
	
- An official Arduino Cloud Library for your Arduino sketches: `ArduinoIoTCloud.h` 
- An NPM Javascript package: `arduino-iot-js` 

### ArduinoIoTCloud Library

The Arduino (C++) library allows your Arduino devices to connect and exchange data with the Arduino Cloud. If you use the Arduino Cloud online environment, you do not need to install this library.

This library is also available in the library manager for [Arduino IDE](https://www.arduino.cc/en/software). With a paid subscription, you can push/pull changes to your online sketches in the offline editor.

You can find more details at:

- The [official repository](https://github.com/arduino-libraries/ArduinoIoTCloud).
- The [Arduino C++ Library](/arduino-cloud/api/c-library) section.

### Arduino IoT JS

The `arduino-iot-js` NPM module is designed for communicating with the Arduino Cloud broker using the MQTT over Websocket protocol. It is primarily used to send and receive variable values.

Example:

```js
const { ArduinoIoTCloud } = require('@arduino/arduino-iot-js');

ArduinoIoTCloud.connect(options)
  .then(() => {
    console.log("Connected to Arduino Cloud");
    return ArduinoIoTCloud.onPropertyValue(thingId, variableName, showUpdates = value => console.log(value));
  })
  .then(() => console.log("Callback registered"))
  .catch(error => console.log(error));
```

Full examples and documentation can be found at:

- The [official repository](https://github.com/arduino/arduino-iot-js)
- The [NPM module](https://www.npmjs.com/package/arduino-iot-js) page  

### MicroPython

The [Arduino Cloud Python Client](https://github.com/arduino/arduino-iot-cloud-py) can be installed on a board running MicroPython, and is designed to be easy to use. With just a few lines of code you can connect to the cloud, using credentials obtained during the manual device configuration.

Below is a minimal example:

```python
DEVICE_ID = "YOUR_DEVICE_ID"
SECRET_KEY = "YOUR_SECRET_KEY"

client = ArduinoCloudClient(device_id=DEVICE_ID, username=DEVICE_ID, password=SECRET_KEY)

client.register("variable")  
client["variable"] = 255

client.start()
```

For more information, visit the [Connecting to Arduino Cloud using MicroPython](/arduino-cloud/getting-started/iot-cloud-micropython) guide.

### Python

The [Arduino Cloud Python Client](https://github.com/arduino/arduino-iot-cloud-py) can also be used with regular python, and is very similar to how you connect using MicroPython, with a few adjustments.

To find out more about how to connect using Python, you can refer to the Python section of the [Manual Device Configuration](/arduino-cloud/getting-started/manual-device#python) guide.

## Backward Compatibility Policy

Public Arduino Cloud APIs are exposing versioned endpoints and are committed to preserving compatibility with the following policies in place:
- When making a breaking change to the API signature or behavior, we will expose a new version of the endpoint.
- If we are making a change that is backward compatible with the existing version, we won't change the endpoint version.
- When introducing a new version of the API, we will preserve the previous version as deprecated for a reasonable amount of time to allow client migrations.
- We will not preserve multiple previous versions, just N-1 with respect to the current last released, hence upgrades are recommended.
- In any case, the frequency of version changes is expected to be less than once a year.
- It's also recommended that the client keeps the base URL of the API configurable because the base URL (currently api2.arduino.cc) might also change.