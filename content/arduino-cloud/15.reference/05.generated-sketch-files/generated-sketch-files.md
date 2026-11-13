---
title: Generated Sketch Files
description: The files Arduino Cloud generates for a Thing's sketch — the .ino, thingProperties.h, the Secret/arduino_secrets.h file, and the ReadMe.
tags: [Arduino Cloud, Sketch, Reference]
author: Karl Söderby & Arduino Team
---

When you generate a sketch for an Arduino/C++ [Thing](/arduino-cloud/things-data/things), Arduino Cloud creates a small set of files that together connect your board to the Cloud and keep your [Cloud Variables](/arduino-cloud/things-data/cloud-variables) in sync. This page describes what each generated file is for. See [Sketches](/arduino-cloud/sketches-editor/sketchbook-and-sketches) for the editor workflow.

## The Sketch File (`.ino`)

Your main, editable sketch — named `<thing-name>_<date>.ino`. It's generated with the Cloud essentials already wired in:

- `initProperties()` — initializes the variables declared in your Thing.
- `ArduinoCloud.begin(ArduinoIoTPreferredConnection)` — starts the library with your preferred connection (Wi-Fi®, Ethernet, Cellular, or LoRaWAN®).
- `ArduinoCloud.update()` — called every `loop()` to sync data between the board and Arduino Cloud.

Any Read & Write variable also gets a callback — a variable named `test` generates `void onTestChange() {}`, which runs whenever the value changes in the Cloud. Add your own logic here; this is the file you edit.

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

void onTestChange() {
  // runs each time the variable changes in the Cloud
}
```

A sync policy can be set with `setSyncPolicy(...)`:

| Policy | Behavior |
|---|---|
| `MOST_RECENT_WINS` | The latest update, from device or cloud, is used. |
| `CLOUD_WINS` | The cloud value always overwrites the device value. |
| `DEVICE_WINS` | The device value always overwrites the cloud value. |

## The Configuration Header (`thingProperties.h`)

A non-editable, auto-maintained file that mirrors your Thing's configuration. It declares each Cloud Variable, registers `addProperty(...)` calls (with permission, update policy, and callback), and sets the connection handler/credentials.

- Creating a variable adds it here automatically.
- Changing the device or network updates the connection method stored here.

Don't hand-edit this file — it's regenerated whenever you change the Thing's variables, device, or network settings.

<Alert type="info">

If no device is associated yet, `thingProperties.h` can't produce a real connection handler — it inserts an `#error` directive (with a comment showing the `WiFiConnectionHandler(SSID, PASS)` pattern), so the sketch intentionally fails to compile until a device is linked.

</Alert>

## The Secret File (`arduino_secrets.h`)

Contains your secret credentials — Wi-Fi® SSID/password or the device secret key — when the board uses provisioning version 1.0. On version 2.0, the credentials are stored on the board itself instead. The file appears as a **Secret** tab in the Cloud Editor and is never shown on the Cloud platform.

<Alert type="note">

If you're working offline (Arduino IDE / Arduino CLI), you must create `arduino_secrets.h` manually. See [Keep Secrets Out of Your Sketch](/arduino-cloud/sketches-editor/keep-secrets-out).

</Alert>

## The ReadMe (`ReadMe.adoc`)

A short, auto-generated notes file describing the generated sketch.

## NetworkConfigurator

Boards registered with Provisioning 2.0 get a `thingProperties.h` with the NetworkConfigurator enabled. It stores network credentials in Non-Volatile Storage (NVS) instead of `arduino_secrets.h`, and lets you provide new network settings over Bluetooth® LE or Serial without reflashing. See [Provisioning & Network Configuration](/arduino-cloud/devices/network-configuration).

It is built from three parts:

- **Configurator agents** handle the communication between the board and your PC or phone. The library provides `BLEAgent` (Bluetooth® LE) and `SerialAgent` (Serial over USB).
- **A key-value store** that implements `KVStoreInterface` saves the configuration. Arduino provides the `Arduino_KVStore` library.
- **A ConnectionHandler** manages the board's Internet connection.

### Default Setup

The relevant lines generated in `thingProperties.h`:

```arduino
#include <Arduino_NetworkConfigurator.h>
#include <configuratorAgents/agents/BLEAgent.h>
#include <configuratorAgents/agents/SerialAgent.h>

KVStore kvStore;
BLEAgentClass BLEAgent;
SerialAgentClass SerialAgent;
WiFiConnectionHandler ArduinoIoTPreferredConnection;
NetworkConfiguratorClass NetworkConfigurator(ArduinoIoTPreferredConnection);

void initProperties(){
  NetworkConfigurator.addAgent(BLEAgent);
  NetworkConfigurator.addAgent(SerialAgent);
  NetworkConfigurator.setStorage(kvStore);
  ArduinoCloud.setConfigurator(NetworkConfigurator);
  // ...addProperty() calls
}
```

<Alert type="info">

The changes below apply only to boards registered with Provisioning 2.0.

</Alert>

### Disable Components to Save Memory

After provisioning, you can remove parts of the NetworkConfigurator to save storage and memory (BSS and Data):

| Remove | Lines to Comment Out or Delete | Saves | Trade-Off |
|---|---|---|---|
| `BLEAgent` | The `BLEAgent.h` include, `BLEAgentClass BLEAgent;`, and `addAgent(BLEAgent)` | ~30 kB storage, ~2 kB memory | Credentials can no longer be changed over Bluetooth® LE. |
| `SerialAgent` | The `SerialAgent.h` include, `SerialAgentClass SerialAgent;`, and `addAgent(SerialAgent)` | ~1 kB | Credentials can no longer be changed over USB. |
| NetworkConfigurator | All the lines shown in [Default Setup](#default-setup) | ~40 kB storage, ~2.9 kB memory | Credentials come from `arduino_secrets.h` again, and can only be changed by reflashing — not from the Arduino Cloud web page or the mobile app. |

Without the NetworkConfigurator, add `arduino_secrets.h` manually with the needed defines, and pass the credentials to the connection handler:

```arduino
WiFiConnectionHandler ArduinoIoTPreferredConnection(SECRET_SSID, SECRET_OPTIONAL_PASS);
```

### Reconfiguration Pin

When Provisioning 2.0 ends, the Bluetooth® LE interface is turned off. To restart it and update the network settings, the [Arduino_NetworkConfigurator](https://github.com/arduino-libraries/Arduino_NetworkConfigurator) library provides a reconfiguration procedure based on shorting two pins of the board. The default pin for each board is listed in [Resetting the Board Configuration](/arduino-cloud/devices/network-configuration#resetting-the-board-configuration).

<Alert type="info">

Internally, the pin designated for the procedure is set as `INPUT_PULLUP` (except for Arduino Opta), and it is attached to an ISR fired on every change of the pin's status.

</Alert>

Customize the procedure by adding these lines to `initProperties()` in `thingProperties.h`:

```arduino
// Run your own void func(void) every time the pin's state changes
NetworkConfigurator.addReconfigurePinCallback(onReconfigurationPinInterrupt);

// Use a different pin (must support interrupts, see attachInterrupt())
NetworkConfigurator.setReconfigurePin(your_pin);

// Or disable the reconfiguration procedure
NetworkConfigurator.setReconfigurePin(DISABLE_PIN);
```

See [attachInterrupt()](https://docs.arduino.cc/language-reference/en/functions/external-interrupts/attachInterrupt/) for the pins usable for interrupts.

## Next Steps

- [Sketchbook & Sketches](/arduino-cloud/sketches-editor/sketchbook-and-sketches)
- [Keep Secrets Out of Your Sketch](/arduino-cloud/sketches-editor/keep-secrets-out)
- [Cloud Variable Types](/arduino-cloud/reference/cloud-variable-types)

## Trademark Acknowledgments

- **LoRa®** and **LoRaWAN®** are registered trademarks of Semtech Corporation.
