---
title: Arduino / C++ Library
description: The ArduinoIoTCloud C++ library — connection classes, initProperties/begin/update, thingProperties.h, and variable callbacks that run on an Arduino board.
tags: [Arduino Cloud, C++, Device Libraries]
author: Karl Söderby & Arduino Team
---

[ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud) is the
device-side C++ library every Arduino/C++
[Thing](/arduino-cloud/things-data/things)'s
[generated sketch](/arduino-cloud/sketches-editor/sketchbook-and-sketches)
depends on. It handles the MQTT connection and keeps your
[Cloud Variables](/arduino-cloud/things-data/cloud-variables) synced, relying on
[Arduino_ConnectionHandler](https://github.com/arduino-libraries/Arduino_ConnectionHandler)
for the underlying Wi-Fi®/LoRa®/GSM/NB/Ethernet transport.

You rarely write against this library directly — associating a device
auto-generates the sketch and `thingProperties.h` that call it. This page
covers the API surface so you know what the generated code is doing.

## Connection Classes

`ArduinoCloud` resolves to one of two underlying classes automatically based on
the device you associate — you don't pick this yourself:

| Class | Used for | Transport |
|---|---|---|
| `ArduinoIoTCloudTCP` | Wi-Fi®, Ethernet, GSM, NB-IoT | MQTT over TCP/IP |
| `ArduinoIoTCloudLPWAN` | LoRa® | Routed via The Things Network |

## Key API Surface

| Call | Purpose |
|---|---|
| `initProperties()` | Declared in `thingProperties.h`; registers every Cloud Variable. Call once in `setup()`. |
| `ArduinoCloud.begin(connectionHandler, enableWatchdog = true)` | Starts the connection. `enableWatchdog` covers ATSAMD21G18 boards' built-in watchdog; pass `false` to disable. |
| `ArduinoCloud.update()` | Must run every `loop()` iteration — drives the MQTT connection and property sync. |
| `ArduinoCloud.addProperty(var, permission, updatePolicy, callback)` | Registers a Cloud Variable (auto-generated into `thingProperties.h`). |
| `ArduinoCloud.setThingId(id)` | Links the sketch to a specific Thing (auto-generated). |

Most sketches never call anything beyond `initProperties()`, `begin()`, and
`update()` — Automatic Sketch Generation wires the rest.

## The Generated Sketch

The main `.ino` file follows a fixed shape — add your logic around it:

```arduino
#include "thingProperties.h"

void setup() {
  Serial.begin(9600);
  delay(1500);
  initProperties();
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);
  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  ArduinoCloud.update();
  // your logic here
}
```

Each line of the generated skeleton has a specific job:

| Line | What it does |
|---|---|
| `#include "thingProperties.h"` | Pulls in the auto-generated variable declarations, credentials, and `initProperties()`. Always the first include. |
| `Serial.begin(9600)` + `delay(1500)` | Opens the serial port for debug output; the short delay gives the Serial Monitor time to attach before the first messages print. |
| `initProperties()` | Registers every Cloud Variable with the library. Must run before `begin()`. |
| `ArduinoCloud.begin(ArduinoIoTPreferredConnection)` | Starts the connection. `ArduinoIoTPreferredConnection` is the connection-handler instance (Wi-Fi®, GSM, Ethernet, …) that `thingProperties.h` created for your device. |
| `setDebugMessageLevel(2)` | Optional. Sets how verbose the serial debug output is, from `0` (errors only) to `4` (most verbose). Level `2` is a good default while developing. |
| `ArduinoCloud.printDebugInfo()` | Optional. Prints the current connection/sync state to Serial — useful for diagnosing why a board won't come online. |
| `ArduinoCloud.update()` | The one call that *must* run on every `loop()` iteration. It services the MQTT connection, pushes changed values up, and applies incoming cloud-side changes. |

### Where Your Code Goes

The generated regions are stable — regenerating the sketch won't overwrite your
additions as long as you keep them in the right place:

- **Hardware setup** (`pinMode`, `begin()` for sensors/displays) → after
  `ArduinoCloud.begin()` inside `setup()`.
- **Reading sensors and updating the cloud** → in `loop()`, after
  `ArduinoCloud.update()`. Assigning a Cloud Variable (`temperature = 22.5;`)
  is all it takes to publish it.
- **Reacting to cloud-side changes** → in the generated
  [variable callbacks](#variable-callbacks), not in `loop()`.

<Alert type="note">

Keep `loop()` non-blocking. Long `delay()` calls or blocking `while` loops stop
`ArduinoCloud.update()` from running, which drops the connection. See
[Best Practices for Cloud Sketches](/arduino-cloud/sketches-editor/best-practices).

</Alert>

The companion files generated alongside the `.ino` (`thingProperties.h`, the
secret/credentials file, and `ReadMe.adoc`) are described in
[Generated Sketch Files](/arduino-cloud/reference/generated-sketch-files).


## thingProperties.h

`thingProperties.h` is auto-generated and auto-maintained. It declares each
Cloud Variable, sets the connection handler and credentials, and registers an
`addProperty(...)` call — permission, update policy, and callback — for every
variable on the Thing.

Do not hand-edit this file. It's regenerated whenever you change
variables, device, or network settings from the Thing UI.

<Alert type="note">

If no device is associated yet, `thingProperties.h` can't generate a real
connection handler — it inserts an `#error` directive instead, so the sketch
intentionally fails to compile until a device is linked.

</Alert>

## Variable Callbacks

Every Cloud Variable with **Read & Write** permission gets a matching callback
function generated in your sketch, called whenever its value changes from the
cloud side (a dashboard control, an API call, or a
[Trigger](/arduino-cloud/automations/triggers-and-alerts) action):

```arduino
void onLedChange() {
  digitalWrite(LED_BUILTIN, led);
}
```

This is registered automatically in `thingProperties.h`:

```arduino
ArduinoCloud.addProperty(led, READWRITE, ON_CHANGE, onLedChange);
```

- **On-change** policy: the callback runs once per value change arriving from
  the cloud.
- **Periodic** policy: used for the device pushing values *up*, not for
  reacting to cloud-side writes.

Write-only variables don't get a callback (nothing reads them on the device);
read-only variables never receive cloud-side writes, so there's nothing to call
back on.

## Connection Events & Callbacks

Beyond per-variable callbacks, you can react to the board's **connection state**
using the `ArduinoIoTCloudEvent` enumeration:

| Event | Value | Fires when |
|---|---|---|
| `CONNECT` | 0 | The board connects to Arduino Cloud. |
| `SYNC` | 1 | Data is synced between board and Cloud (requires at least one variable). |
| `DISCONNECT` | 2 | The board loses its connection. |

Subscribe to an event with `addCallback()`, passing the event and your function.
Register callbacks inside `setup()`:

```arduino
void setup() {
  // ...
  ArduinoCloud.addCallback(ArduinoIoTCloudEvent::CONNECT, doThisOnConnect);
  ArduinoCloud.addCallback(ArduinoIoTCloudEvent::SYNC, doThisOnSync);
  ArduinoCloud.addCallback(ArduinoIoTCloudEvent::DISCONNECT, doThisOnDisconnect);
}

void doThisOnConnect()    { Serial.println("Board connected to Arduino Cloud"); }
void doThisOnSync()       { Serial.println("Thing properties synchronised"); }
void doThisOnDisconnect() { Serial.println("Board disconnected from Arduino Cloud"); }
```

`CONNECT` and `DISCONNECT` fire even with no variables defined; `SYNC` requires
at least one variable. See the library's
[ArduinoIoTCloud-Callbacks](https://github.com/arduino-libraries/ArduinoIoTCloud/blob/master/examples/ArduinoIoTCloud-Callbacks/ArduinoIoTCloud-Callbacks.ino)
example for the full sketch.

## Using It Offline

Install both libraries from the Library Manager to compile and monitor offline:

- `ArduinoIoTCloud`
- `Arduino_ConnectionHandler`

Offline edits won't stay in sync with the Thing configuration in the web UI —
changes need manual reconciliation, or use the sketch synchronization feature
in Arduino IDE 2.

## Next Steps

- [Sketches & Editor](/arduino-cloud/sketches-editor/sketchbook-and-sketches)
- [Cloud Variables](/arduino-cloud/things-data/cloud-variables)
- [Things](/arduino-cloud/things-data/things)

## Trademark Acknowledgments

- **LoRa®** is a registered trademark of Semtech Corporation.
