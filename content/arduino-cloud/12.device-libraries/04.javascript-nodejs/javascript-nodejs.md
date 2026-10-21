---
title: JavaScript / Node.js
description: Connect a browser or Node.js client to Arduino Cloud with arduino-iot-js — as a single device or as a user across all your properties.
tags: [Arduino Cloud, JavaScript, Node.js, Device Libraries]
author: Karl Söderby & Arduino Team
---

[arduino-iot-js](https://github.com/arduino/arduino-iot-js) interacts with the
Arduino Cloud MQTT broker and runs in both the browser and Node.js. It powers a
[manual (generic) device](/arduino-cloud/devices/add-manual-device) written in
JavaScript, and can also connect with user-level credentials (API key or JWT) to
reach any of your properties, not just one device's.

<Alert type="warning">

Not to be confused with `@arduino/arduino-iot-client` — that's the REST CRUD
client covered in [REST API & SDKs](/arduino-cloud/apis-cli/rest-api-sdks). This
page is the real-time MQTT client.

</Alert>

## Create a Generic Device

From the web UI, go to **Devices → + Device → Manual Setup → Any device**, or
from the terminal:

```bash
arduino-cloud-cli device create-generic --name <deviceName>
```

Then create a [Thing](/arduino-cloud/things-data/things), bind it to the generic
device, and add [Cloud Variables](/arduino-cloud/things-data/cloud-variables).

## Install

```bash
npm install arduino-iot-js
```

## Connection Methods

The library supports three ways to connect:

- **Device credentials** (recommended) — Device ID + Secret Key, same as the
  Python/C++ clients.
- **API key** — a client ID/secret from
  [API keys](https://app.arduino.cc/api-keys); also requires your Thing ID.
- **JWT token** — connect as a user with a valid token.

## Example: Device Credentials

Send a property with `sendProperty()` and listen for updates with
`onPropertyValue()`. Create a `test_value` (`int`) variable on the Thing and
replace the credentials:

```javascript
const { ArduinoIoTCloud } = require('arduino-iot-js');

(async () => {
  const client = await ArduinoIoTCloud.connect({
    deviceId: 'YOUR_DEVICE_ID',
    secretKey: 'YOUR_SECRET_KEY',
    onDisconnect: (message) => console.error(message),
  });

  const value = 20;
  let cloudVar = "test_value";

  client.sendProperty(cloudVar, value);
  console.log(cloudVar, ":", value);

  client.onPropertyValue(cloudVar, (value) => console.log(cloudVar, ":", value));
})();
```

This pushes `test_value = 20` and then prints any change received from the
Cloud (e.g. from a value widget on a dashboard) as `test_value : <value>`.

## Example: API Key

With an API key you address properties by Thing ID and variable name:

```javascript
import { ArduinoIoTCloud } from 'arduino-iot-js';

(async () => {
  const client = await ArduinoIoTCloud.connect({
    clientId: 'YOUR_CLIENT_ID',
    clientSecret: 'YOUR_CLIENT_SECRET',
    onDisconnect: (message) => console.error(message),
  });

  client.sendProperty('YOUR_THING_ID', 'YOUR_VARIABLE_NAME', 'some value');
  client.onPropertyValue('YOUR_THING_ID', 'ANOTHER_VARIABLE_NAME', (value) => console.log(value));
})();
```

A JWT token connection is identical, passing `token` instead of
`clientId`/`clientSecret` to `connect()`.

<Alert type="info">

Common issues: `Error: Cannot find module` means the package isn't installed in
the current directory; `connection failed: client not connected` usually means a
wrong Device ID or Secret Key.

</Alert>

## Managing the Cloud Side From JavaScript

This library is for **real-time device connection** only. To script
Thing/Device/Dashboard management, use the separate REST client
(`@arduino/arduino-iot-client`) — see
[REST API & SDKs](/arduino-cloud/apis-cli/rest-api-sdks).

## Next Steps

- [Add a Manual Device](/arduino-cloud/devices/add-manual-device)
- [Cloud Variables](/arduino-cloud/things-data/cloud-variables)
- [REST API & SDKs](/arduino-cloud/apis-cli/rest-api-sdks)
