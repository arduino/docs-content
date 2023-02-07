---
title: 'Getting Started with RS485 on Opta™'
description: "Learn how to make use of the RS485 communication interface on the Arduino Opta™."
difficulty: beginner 
tags:
  - Getting started
  - RS485
author: 'Benjamin Dannegård'
libraries:
  - name: ArduinoRS485
    url: https://www.arduino.cc/reference/en/libraries/arduinors485/
software:
  - ide-v1
  - ide-v2
hardware:
  - hardware/05.pro-solutions/solutions-and-kits/opta
---

## Overview

The Opta™ is equipped with the RS485 communication interface. Using this feature is easy with the help of the Arduino ecosystem tools, such as the Arduino IDE and the [ArduinoRS485 library](https://www.arduino.cc/reference/en/libraries/arduinors485/). This tutorial will follow the steps to connect two Opta™ devices via RS485 and the Arduino IDE; it will describe some essential library functions and show an example sketch that uses the library and the RS485 interface.

## Goals

- Learn how to connect two Opta™ devices through RS485 communication interface
- Learn to exchange information between two Opta™ devices through RS485 communication interface
  
### Required Hardware and Software

- [Opta™ RS485](https://store.arduino.cc/pages/opta) (x2)
- 12-24VDC, 1A power supply (x1)
- USB-C® cable (x1)
- [Arduino IDE 2](https://www.arduino.cc/en/software)
- [ArduinoRS485 library](https://www.arduino.cc/reference/en/libraries/arduinors485/)
- 24AWG twisted-pair cable (for connecting the Optas via their RS485 communication interface)

***Notice: This tutorial does not work with Opta™ Lite since it does not have an RS485 communication interface.***

## Instructions

### Setting up With Arduino IDE

First, ensure that you have installed the latest version of the Arduino IDE; you can download the IDE from [here](https://www.arduino.cc/en/software). Please look at our [getting started with Opta™ tutorial](/tutorials/opta/getting-started) if you need help setting up the Opta™ with the Arduino IDE.

Let's use a library to make it easier to use the RS485 protocol with Opta™. The library is called [ArduinoRS485](https://www.arduino.cc/reference/en/libraries/arduinors485/), which can be found in the Arduino IDE Library Manager. Once installed, let's take a look at a simple sketch to test the RS485 communication between two Opta™ devices.

### RS485 Communication with the Opta™

The sender sketch will let you send a message over the Arduino IDE Serial Monitor to the receiving device via RS485. The receiving device will take the received message, open or close the corresponding relay, and turn on or off a LED. If you send the number 0 through the Serial Monitor, the receiving Opta™ will open or close the relay one depending on its current status while turning on or off a status LED at the same time.

Here are some important functions in the sketch:

- `RS485.begin(baudrate)`: Initializes the RS485 object communication speed with assigned baud rate, `115200` in this case
- `RS485.beginTransmission()`: Enables RS485 transmission
- `RS485.print()`: Writes binary data over RS485; data is sent as a byte or series of bytes
- `RS485.endTransmission()`: Disables RS485 transmission

Connect the Opta™ devices according to the image shown below:

![RS485 connection between two Opta™ devices](assets/opta-modbus-connection.svg)

### RS485 Sender Sketch

Upload the following sender sketch to the Opta™ device you want to designate as the sender device:

```arduino
#include <ArduinoRS485.h>

constexpr auto baudrate{ 115200 };

// Calculate preDelay and postDelay in microseconds as per Modbus RTU Specification
constexpr auto bitduration{ 1.f / baudrate };
constexpr auto wordlen{ 9.6f };  // OR 10.0f depending on the channel configuration
constexpr auto preDelayBR{ bitduration * wordlen * 3.5f * 1e6 };
constexpr auto postDelayBR{ bitduration * wordlen * 3.5f * 1e6 };

void setup() {
  Serial.begin(baudrate);  // opens serial port
  while (!Serial);

  RS485.begin(baudrate);
  RS485.setDelays(preDelayBR, postDelayBR);
}

void loop() {
  auto aval = Serial.available();
  if (aval > 0) {
    auto input = Serial.readStringUntil('\r');

    // Discard \r\n
    auto read = input.length();
    while (aval > ++read)
      Serial.read();

    auto incomingByte = input.toInt();
    RS485.beginTransmission();
    Serial.print("- Sending: ");
    Serial.println(incomingByte);
    RS485.write(incomingByte);
    RS485.endTransmission();
  }
}
```

### RS485 Receiver Sketch

Some important functions in the receiver sketch:

- `RS485.begin(baudrate)`: Make sure this is set to the same baud rate as the sender device, `115200` in this case.
- `RS485.receive()`: Enables reception through the RS485 connection.
- `RS485.parseInt()`: We use this function to ensure that the correct value is received and read.

Now upload this sketch to the receiver Opta™ device:

```arduino
#include <ArduinoRS485.h>

constexpr auto baudrate{ 115200 };

// Calculate preDelay and postDelay in microseconds as per Modbus RTU Specification
constexpr auto bitduration{ 1.f / baudrate };
constexpr auto wordlen{ 9.6f };  // OR 10.0f depending on the channel configuration
constexpr auto preDelayBR{ bitduration * wordlen * 3.5f * 1e6 };
constexpr auto postDelayBR{ bitduration * wordlen * 3.5f * 1e6 };

int idx{ 0 };
bool newState{ false };

int relays[]{ D0, D1, D2, D3 };
int leds[]{ LED_D0, LED_D1, LED_D2, LED_D3 };
bool statuses[]{ true, true, true, true };

void setup() {
  for (int i = 0; i < 4; i++) {
    pinMode(relays[i], OUTPUT);
    pinMode(leds[i], OUTPUT);
  }

  RS485.begin(baudrate);
  RS485.setDelays(preDelayBR, postDelayBR);

  Serial.begin(baudrate);
  while (!Serial);
}

void loop() {

  RS485.receive();
  auto aval = RS485.available();
  if (aval > 0) {
    int readValue = RS485.read();

    // Manage out-of-range inputs
    if (readValue > 4)
      readValue = readValue % 4;

    Serial.print("Command for relay: ");
    Serial.println(readValue);
    newState = true;

    // Array indexes start at 0
    idx = readValue - 1;
  }
  RS485.noReceive();

  if (newState) {
    changeRelay();
    newState = false;
  }
}

void changeRelay() {
  // Get current status
  auto status = statuses[idx] ? HIGH : LOW;
  
  // Apply
  digitalWrite(relays[idx], status);
  digitalWrite(leds[idx], status);
  
  // Invert
  statuses[idx] = !statuses[idx];
}
```

### Testing Out the Sketches

Let's test the application with the sender Opta™ device connected to the Serial Monitor of the Arduino IDE and the receiver Opta™ device powered on. In the Serial Monitor, send a value between `1`and `4`; sending a `1` should open relay one and turn on the corresponding status LED, from left to right, of the receiver Opta™ device. Sending a `0` again should close the relay and turn off the status LED.

Here is a review of the values the receiver Opta™ device can receive and the result they produce:

- Sending `1`: Will turn on or off the first relay and the first status LED
- Sending `2`: Will turn on or off the second relay and the second status LED
- Sending `3`: Will turn on or off the third relay and the third status LED
- Sending `4`: Will turn on or off the fourth relay and the fourth status LED

## Conclusion

In this tutorial, we established an RS485 connection between two Opta™ devices. We learned how to use the `ArduinoRS485.h` library to send and receive values between these two devices. Finally, the tutorial showed how to take the values sent via RS485 to interact with the Opta™ hardware features, such as its onboard relays and LEDs.

### Next Steps

Now that you are familiar with the RS485 communication interface on the Opta™, look at our [getting started tutorial](/tutorials/opta/getting-started) to get a better overview of other features on the device.

If you wish to incorporate Wi-Fi/Bluetooth® Low Energy in your Opta™ solutions, have a look at our [connectivity tutorial](/tutorials/opta/getting-started-connectivity).

If you are interested in seeing the RS485 interface and the Opta™ being put to work in a real-life scenario, have a look at our [Tank level application note](/tutorials/opta/tank-level-app-note).