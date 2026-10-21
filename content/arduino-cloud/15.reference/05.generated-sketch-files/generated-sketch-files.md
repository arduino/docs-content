---
title: Generated Sketch Files
description: The files Arduino Cloud generates for a Thing's sketch — the .ino, thingProperties.h, the Secret/arduino_secrets.h file, and the ReadMe.
tags: [Arduino Cloud, Sketch, Reference]
author: Karl Söderby & Arduino Team
---

When you generate a sketch for an Arduino/C++
[Thing](/arduino-cloud/things-data/things), Arduino Cloud creates a small set
of files that together connect your board to the Cloud and keep your
[Cloud Variables](/arduino-cloud/things-data/cloud-variables) in sync. This
page describes what each generated file is for. See
[Sketches](/arduino-cloud/sketches-editor/sketchbook-and-sketches) for the
editor workflow.

## The Sketch File (`.ino`)

Your main, editable sketch — named `<thing-name>_<date>.ino`. It's generated
with the Cloud essentials already wired in:

- `initProperties()` — initializes the variables declared in your Thing.
- `ArduinoCloud.begin(ArduinoIoTPreferredConnection)` — starts the library
  with your preferred connection (Wi-Fi®, Ethernet, Cellular, or LoRaWAN®).
- `ArduinoCloud.update()` — called every `loop()` to sync data between the
  board and Arduino Cloud.

Any Read & Write variable also gets a callback — a variable named `test`
generates `void onTestChange() {}`, which runs whenever the value changes in
the Cloud. Add your own logic here; this is the file you edit.

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

A non-editable, auto-maintained file that mirrors your Thing's configuration.
It declares each Cloud Variable, registers `addProperty(...)` calls (with
permission, update policy, and callback), and sets the connection
handler/credentials.

- Creating a variable adds it here automatically.
- Changing the device or network updates the connection method stored here.

Don't hand-edit this file — it's regenerated whenever you change the Thing's
variables, device, or network settings.

<Alert type="info">

If no device is associated yet, `thingProperties.h` can't produce a real
connection handler — it inserts an `#error` directive (with a comment showing
the `WiFiConnectionHandler(SSID, PASS)` pattern), so the sketch intentionally
fails to compile until a device is linked.

</Alert>

## The Secret File (`arduino_secrets.h`)

Contains your secret credentials — Wi-Fi® SSID/password or the device secret
key — when the board uses provisioning version 1.0. On version 2.0, the
credentials are stored on the board itself instead. The file appears as a
**Secret** tab in the Cloud Editor and is never shown on the Cloud platform.

<Alert type="note">

If you're working offline (Arduino IDE / Arduino CLI), you must create
`arduino_secrets.h` manually. See
[Keep Secrets Out of Your Sketch](/arduino-cloud/sketches-editor/keep-secrets-out).

</Alert>

## The ReadMe (`ReadMe.adoc`)

A short, auto-generated notes file describing the generated sketch.

## Next Steps

- [Sketchbook & Sketches](/arduino-cloud/sketches-editor/sketchbook-and-sketches)
- [Keep Secrets Out of Your Sketch](/arduino-cloud/sketches-editor/keep-secrets-out)
- [Cloud Variable Types](/arduino-cloud/reference/cloud-variable-types)

## Trademark Acknowledgments

- **LoRa®** and **LoRaWAN®** are registered trademarks of Semtech Corporation.
