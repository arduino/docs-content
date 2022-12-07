---
title: Arduino IoT Cloud APIs
description: A summary of the three APIs available in the Arduino IoT Cloud
author: Karl Söderby
tags: IoT Cloud, API, JavaScript
---

The [Arduino IoT Cloud](https://create.arduino.cc/iot/) has several APIs that each provide a different set of functionalities. This article serves an entry point to these different APIs, how they function, and how you can utilize them in your projects.

## Arduino IoT Cloud APIs

There are three APIs to consider when working with the Arduino IoT Cloud.

- **ArduinoIoTCloud library** - an Arduino library for handling authentication, connection & data exchange on the device side. 
- **Device Communication API** - a JavaScript package for communicating with the Arduino IoT Cloud MQTT broker.
- **Integrations API (REST)** - for managing Arduino IoT Cloud endpoints, such as **properties, devices, things**. Can be called with any HTTP Client or through our [JavaScript](https://www.npmjs.com/package/@arduino/arduino-iot-client), [Python](https://pypi.org/project/arduino-iot-client/), or [Golang](https://github.com/arduino/iot-client-go) modules.

## Arduino Libraries 

There are two main Arduino libraries that are included in each Arduino IoT Cloud project.

- [ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud)
- [Arduino_ConnectionHandler](https://github.com/arduino-libraries/Arduino_ConnectionHandler)

Both libraries are automatically installed in the online environment, and any dependencies of these libraries are also automatically handled. 



### ArduinoIoTCloud

The [ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud) library handles the data exchange between your board and cloud. This library is a requirement when creating projects with the Arduino IoT Cloud, as it is used for several purposes:

- Configuring the ECCX08 crypto chip onboard official Arduino hardware.
- Publishing and subscribing to channels using MQTTS (secure exchange of data over the Internet).
- Maintaining the connection between the board and cloud.
- Handling timers for update frequencies.

The ArduinoIoTCloud library requires no installation, as it is automatically included in the online environment. When creating a Thing inside the IoT Cloud, a sketch is also automagically generated where the library is also included at the top of the sketch.

### Arduino_ConnectionHandler

The [Arduino_ConnectionHandler](https://github.com/arduino-libraries/Arduino_ConnectionHandler) library handles the various ways of connecting to the Arduino IoT Cloud:

- Wi-Fi
- LoRa
- 5G
- GSM
- Ethernet

It also provides a keep-alive functionality and automatic reconnection if the board loses its connection.

### Libraries API

In this section, you will find a list of most commonly used APIs in both libraries.

- `initProperties()` - initializes all properties/variables based on your configurations.
- `ArduinoCloud.begin(ArduinoIoTPreferredConnection)` begins the connection to network based on your chosen preference (this is determined by the device you are using).
- `setDebugMessageLevel(2)` - level of granularity on error debug message. Default is `2`.
- `ArduinoCloud.printDebugInfo()` - prints the debug info in the Serial Monitor. 
- `ArduinoCloud.update()` - synchronizes the variables on the board with the cloud. 
- `ArduinoCloud.getLocalTime()` - gets the local time of your device. Your timezone is configured inside your Thing.


### Offline Usage

The [ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud) & [Arduino_ConnectionHandler](https://github.com/arduino-libraries/Arduino_ConnectionHandler) libraries can be installed using an offline version of the IDE, including the Arduino CLI. 

Please note that updates made in your Thing configuration are not automatically reflected in your sketch when used locally. This is a great advantage of using the online environment.

## Device Communication API

Source: https://www.npmjs.com/package/arduino-iot-js

The **Device Communication API** is designed for communicating with the Arduino IoT Cloud MQTT broker. It is primarily used to publish and subscribe to MQTT channels, as it connects to the cloud via websockets.

This can for example be used in a browser or node.js project to interact with your properties (variables). This allows you to for example build custom webpages that can stream data directly from an Arduino, or to interact with the Arduino from the browser.

For interaction with the data, 4 parameters are required:
- **Thing ID:** found inside your Thing.
- **Property Name:** the name of your variable, also found inside your Thing.
- **Client ID:** found in the [API keys](https://cloud.arduino.cc/home/api-keys) section.
- **Client Secret:** found in the [API keys](https://cloud.arduino.cc/home/api-keys) section. Only visible when generating a new API key.

To connect to the Arduino Cloud, use:

```js
ArduinoIoTCloud.connect(options)
```

Listen to a property value:

```js
ArduinoIoTCloud.onPropertyValue(thingId, propertyName)
```

Send a property value:

```js
ArduinoCloud.sendProperty(thingId, propertyName, value)
```

***Please see the full examples at [arduino-iot-js](https://www.npmjs.com/package/arduino-iot-js) for more information.***

## Integrations API (REST)

The **Integrations API** is a REST API that allows you to connect from any HTTP client. With this API, you can interact with a lot of different endpoints in the Arduino IoT cloud, including:

- Check value / update value of a property.
- List all variables attached to a Thing.
- Perform OTA uploads to devices.
- Create / delete dashboards, Things, variables etc.

To use the Integrations API, we need to get an **access token**. This can be obtained by providing the **Client ID** and **Client Secret**. 

With the access token, we can start making HTTP requests. For example, to list out the properties of a Thing using **curl**:

```
curl -X GET "https://api2.arduino.cc/iot/v2/things/{id}/properties"
```

Using JavaScript, you can create an access token and make a request in the same script. As access tokens expires after 300 seconds, this is needed for automations.

A full JavaScript example of authentication + and making a POST request can be seen below:

```js
var IotApi = require('@arduino/arduino-iot-client');
var rp = require('request-promise');

async function getToken() {
    var options = {
        method: 'POST',
        url: 'https://api2.arduino.cc/iot/v1/clients/token',
        headers: { 'content-type': 'application/x-www-form-urlencoded' },
        json: true,
        form: {
            grant_type: 'client_credentials',
            client_id: 'YOUR_CLIENT_ID',
            client_secret: 'YOUR_CLIENT_SECRET',
            audience: 'https://api2.arduino.cc/iot'
        }
    };

    try {
        const response = await rp(options);
        return response['access_token'];
    }
    catch (error) {
        console.error("Failed getting an access token: " + error)
    }
}
```

For more examples and detailed instructions, visit the links below:

- [Full Integrations API (REST)](https://www.arduino.cc/reference/en/iot/api/) - the complete API with hundreds of curl + JavaScript examples.
- [Arduino IoT Cloud Integrations API (REST) Guide](/arduino-cloud/getting-started/arduino-iot-api) - a guide to using the API with JavaScript, Python & Golang. 

## Backward Compatibility Policy

Public Arduino IoT Cloud APIs are exposing versioned endpoints, and are commited to preserve compatibility with the following policies in place:

- When making a breaking change to the API signature or behavior, we will expose a new version of the endpoint.
- If we are making a change which is backward compatible with existing version, we won't change the endpoint version.
- When introducing a new version of the API, we will preserve the previous version as deprecated for a reasonable amount of time to allow client migrations.
- We will not preserve multiple previous versions, just N-1 with respect to the current last released, hence upgrades are recommended.
- In any case, the frequency of version changes is expected be less than once a year.
- It's also recommended that the client keeps the base URL of the API configurable because base URL (currently api2.arduino.cc) might also change.