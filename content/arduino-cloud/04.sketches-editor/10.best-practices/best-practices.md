---
title: Best Practices for Cloud Sketches
description: Recommended code patterns for sketches with an attached Thing — watchdog, non-blocking loops, and I2C ordering.
tags: [Arduino Cloud, Sketch, Best Practices]
author: Karl Söderby & Arduino Team
---

Sketches with an attached [Thing](/arduino-cloud/things-data/things) depend on the [ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud) library, which has a few implications for how you should write your `loop()`. Following these patterns keeps the cloud connection responsive and stable.

## Keep the Loop Non-Blocking

The `loop()` calls `ArduinoCloud.update()`, which sends and receives data. For the best responsiveness, `loop()` should run as fast as possible — avoid any blocking calls, and in particular avoid `delay()`.

Instead of a `delay()`-based blink:

```arduino
void loop() {
  ArduinoCloud.update();

  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

use a non-blocking pattern with `millis()`:

```arduino
void loop() {
  ArduinoCloud.update();

  digitalWrite(LED_BUILTIN, (millis() % 2000) < 1000);
}
```

The first version blocks for two seconds between updates, degrading cloud communication; the second never blocks.

## The Watchdog Timer

Arduino Cloud sketches enable a **Watchdog Timer (WDT)** by default on boards that support it. The WDT resets the board if it stops responding; it's kept alive by the regular `ArduinoCloud.update()` calls in `loop()`. This is the main reason long blocking code is discouraged — a long `delay()` can let the WDT expire and reset the board mid-operation.

To disable the watchdog, pass `false` to `begin()`:

```arduino
ArduinoCloud.begin(ArduinoIoTPreferredConnection, false);
```

## I2C Ordering

On boards with an onboard crypto chip (the ECCX08 secure element), I²C peripherals share the bus with the chip that holds your cloud credentials. Because the crypto chip is needed to establish the connection, initialize other I²C libraries **after** `ArduinoCloud.begin(...)`:

```arduino
void setup() {
  Serial.begin(9600);
  delay(1500);

  initProperties();
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);

  // Initialize other I2C peripherals AFTER the cloud connection
  if (!ENV.begin()) {
    Serial.println("Failed to initialize MKR ENV shield!");
    while (1);
  }
}
```

## Avoid Blocking on Serial

`while (!Serial) {}` blocks until the Serial Monitor is opened. In an autonomous IoT device this prevents the board from connecting to the network and Arduino Cloud until you manually open the monitor — remove it when it isn't needed. If you want a chance to catch the first debug lines, add a short delay after `Serial.begin()` instead:

```arduino
Serial.begin(9600);
delay(1500);
```

## Next Steps

- [Arduino C++ Library](/arduino-cloud/device-libraries/arduino-cpp)
- [Cloud Variables](/arduino-cloud/things-data/cloud-variables)
- [Cloud Editor Overview](/arduino-cloud/sketches-editor/cloud-editor-overview)
