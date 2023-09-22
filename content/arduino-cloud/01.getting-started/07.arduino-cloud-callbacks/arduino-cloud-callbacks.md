---
title: 'IoT Cloud Event & Callbacks'
description: 'Learn how to subscribe to events and add callback functions.'
tags: [IoT Cloud, Events, Callbacks]
author: 'Karl Söderby'
---

The [Arduino IoT Cloud](https://create.arduino.cc/iot/) has support for events and callbacks. This can be used to trigger specific functionalities depending on what state your device is in. 

You can for example trigger a specific block of code whenever the board is in a **connecting**, **synchronized** or **disconnected** state. In this brief document, we will explore how to set it up, using an example from the [ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud/blob/master/examples/ArduinoIoTCloud-Callbacks/ArduinoIoTCloud-Callbacks.ino) library.   

## Events

The `ArduinoIoTCloudEvent` enumeration class has three possible events:
- `CONNECT` (0) - Board successfully connects to IoT Cloud.
- `SYNC` (1) - Data is successfully synced between Board and IoT Cloud.
- `DISCONNECT` (2) -  Board has lost connection to IoT Cloud.

The `CONNECT` and `DISCONNECT` events can occur even though no variable is created inside the Thing. However, `SYNC` requires a variable to be created, as this triggers whenever data is synchronized between the board and cloud.

These events can be subscribed to using the `addCallback()` function, which is documented in the next section.

## Callbacks

Callbacks can be added for each event, and essentially triggers a custom function whenever the event occurs.

Callbacks are added via the `addCallback()` method from the `ArduinoIoTCloud` class, where the **event** and **custom function** are added as parameters. 

```arduino
ArduinoCloud.addCallback(ArduinoIoTCloudEvent::CONNECT, doThisOnConnect);
```

The above code will trigger the `doThisOnConnect()`
function whenever the `CONNECT` event occurs.

***Please note that callback functions should be added inside the `setup()` of your sketch.***

## Full Example

The example below demonstrates how to use events & callbacks in the IoT Cloud. 

<CodeBlock url="https://github.com/arduino-libraries/ArduinoIoTCloud/blob/master/examples/ArduinoIoTCloud-Callbacks/ArduinoIoTCloud-Callbacks.ino" className="arduino"/>

## Summary

This document covers the use of events & callbacks using the [ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud) library.