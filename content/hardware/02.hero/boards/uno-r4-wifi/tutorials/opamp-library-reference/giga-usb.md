---
title: OPAMP Library API Documentation
description: 'Learn how to use the on-board OPAMP on the Arduino R4 boards.'
author: Pedro Sousa Lima
tags: [AMPOP, OPAMP]
---

## Overview

The OPAMP library allows control over the on-board OP AMP encontered on Arduino R4 boards.
More information on implementation can be found [here](https://docs.arduino.cc/tutorials/uno-r4-wifi/opamp/).

## Supported Boards

- Arduino UNO R4 WiFi
- Arduino UNO R4 Minima

## Functions

### `bool begin(OpampSpeedMode)`

Initializes the default op-amp channel. You can specify the speed mode as either high-speed or low-speed. If no speed mode is specified, the op-amp will default to high-speed mode.

**Parameters**

  `speed` (optional): The speed mode of the op-amp. Options are:
  - `OPAMP_SPEED_LOWSPEED`
  - `OPAMP_SPEED_HIGHSPEED` (default)

**Returns**

- `true` if initialization was successful.
- `false` if initialization failed.

### `bool isRunning(uint8_t channel)`
Checks whether a specific op-amp channel is currently running.

**Parameters**
- `channel`: The channel number to check (0 to 3).

**Returns**
- `true` if the channel is active.
- `false` if the channel is inactive.

### `void end()`
Deactivates all op-amp channels.

### `void end(uint8_t channel_mask)`
Deactivates specified op-amp channels.

**Parameters**
- `channel_mask`: A bitmask specifying which channels to deactivate.

## Example Usage
Here is an example demonstrating how to initialize and check the status of the op-amp:

```cpp
#include <OPAMP.h>

void setup() {
    Serial.begin(9600);
    delay(2000); // serial monitor delay

    // Activate OPAMP on the default channel (channel 0)
    // Plus: Analog A1
    // Minus: Analog A2
    // Output: Analog A3
    if (!OPAMP.begin(OPAMP_SPEED_HIGHSPEED)) {
        Serial.println("Failed to start OPAMP!");
    }

    bool const isRunning = OPAMP.isRunning(0);
    if (isRunning) {
        Serial.println("OPAMP running on channel 0!");
    } else {
        Serial.println("OPAMP channel 0 is not running!");
    }
}

void loop() {
    delay(1000); // do nothing
}
```