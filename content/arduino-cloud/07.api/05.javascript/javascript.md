---
title: JavaScript / Node.js Library
description: The JavaScript Library allows you to connect to the Arduino Cloud using Node.js.
author: Karl Söderby
tags: [JavaScript, Arduino Cloud]
---

This library provides interaction with the Arduino IoT Cloud MQTT broker and can be used both from the browser and Node.js.

Connection via this library is achieved by registering a [manual device](), i.e. a virtual device that is not associated with an Arduino hardware board. This virtual device can connect through a simple username/password (Device ID, Secret Key) which is generated in the Arduino Cloud when configuring a device.

This library requires a version of [Node.js]() to be installed on your machine.

## GitHub

To view the source code and report issues, follow the links below to the GitHub repository:
- [arduino-iot-js](https://github.com/arduino/arduino-iot-js)

## Requirements

- [Node.js]()

## Installation

You can install this library using either `npm` or `yarn`.

- [arduino-iot-js (NPM)](https://www.npmjs.com/package/arduino-iot-js)
```
$ npm install arduino-iot-js
```

- [arduino-iot-js (Yarn)](https://yarnpkg.com/package?q=arduino%20cloud&name=arduino-iot-js)
```
$ yarn add arduino-iot-js
```

***Check out the [JavaScript Setup guide]() for more information and a detailed step by step tutorial.***  

## Connection Methods

There are three available methods for connection:
- Using device credentials (recommended method). 
- Using an API key (generated and listed at [Arduino Cloud API keys](app.arduino.cc/app-keys)).
- Using a [JWT token](https://jwt.io/)

### Device Credentials

Device credentials is the easiest method. These credentials are generated when [configuring a manual device]() in the Arduino Cloud, and works like a username/password. The example below uses device credentials:

```js
//JavaScript code

const { ArduinoIoTCloud } = require('arduino-iot-js');

(async () => {
  const client = await ArduinoIoTCloud.connect({
    deviceId: 'YOUR_DEVICE_ID',
    secretKey: 'YOUR_SECRET_KEY',
    onDisconnect: (message) => console.error(message),
  });

  const value = 20;
  let cloudVar = "test_value"

  client.sendProperty(cloudVar, value);
  console.log(cloudVar, ":", value);

  client.onPropertyValue(cloudVar, (value) => console.log(cloudVar, ":", value));
})();
```

### API Key

You can also connect using an API key generated from the [Arduino Cloud API Key Section](), a method that is almost identical to Device Credentials, but where you also need to specify your Thing ID. This is available in the metadata section of your Thing.

```js
import { ArduinoIoTCloud } from 'arduino-iot-js';

(async () => {
  const client = await ArduinoIoTCloud.connect({
    clientId: 'YOUR_CLIENT_ID',
    clientSecret: 'YOUR_CLIENT_SECRET',
    onDisconnect: (message) => console.error(message),
  });

  // Send a value to a thing property
  const value = 'some value';
  client.sendProperty('YOUR_THING_ID', 'YOUR_VARIABLE_NAME', value);

  // Listen to a thing property's changes
  client.onPropertyValue('YOUR_THING_ID', 'ANOTHER_VARIABLE_NAME', (value) => console.log(value));
})();
```

### JSON Web Token (JWT)

To connect using a JWT, you can use the script below:

```js
import { ArduinoIoTCloud } from 'arduino-iot-js';

async function retrieveUserToken() {
  // Retrieve JWT Token here
}

(async () => {
  const token = await retrieveUserToken();

  const client = await ArduinoIoTCloud.connect({
    token,
    onDisconnect: (message) => console.error(message),
  });

  // Send a value to a thing property
  const value = 'some value';
  client.sendProperty('YOUR_THING_ID', 'YOUR_VARIABLE_NAME', value);

  // Listen to a thing property's changes
  client.onPropertyValue('YOUR_THING_ID', 'ANOTHER_VARIABLE_NAME', (value) => console.log(value));
})();
```