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

The RS485 interface provides balanced performance to transmit data reliably over a long distance with a stable transmission rate. The Opta™ provisions the RS485 interface. Using this feature is easy with the help of the Arduino ecosystem tools, such as the Arduino IDE and the [ArduinoRS485 library](https://www.arduino.cc/reference/en/libraries/arduinors485/). This tutorial will follow the steps to connect two Opta™ devices via RS485 and the Arduino IDE; it will describe some essential library functions and show an example sketch that uses the library and the RS485 interface.

## Goals

- Learn how to connect two Opta™ devices through RS485 interface
- Learn to exchange information between two Opta™ devices through RS485 interface
  
### Required Hardware and Software

- [Opta™ RS485](https://store.arduino.cc/pages/opta) (x2)
- 12-24VDC, 1A power supply (x1)
- USB-C® cable (x1)
- [Arduino IDE 2](https://www.arduino.cc/en/software)
- [ArduinoRS485 library](https://www.arduino.cc/reference/en/libraries/arduinors485/)
- 24AWG twisted-pair cable (for connecting the Opta™ devices via RS485 interface)

***Notice: This tutorial does not work with Opta™ Lite since it does not have an RS485 interface.***

## RS485 101

The RS485 is an electrical-only standard that uses a differential bus with voltage levels of 0-5V and the multi-drop feature, allowing to add drivers and receivers to the transmission line. It characterizes good noise immunity thanks to differential signaling. Thus it is well suited to industrial environment applications.

The RS485 does not define a protocol since it does not know how to interpret such information nor when or what it should do to process it. Modbus RTU is a communication protocol over the RS485 interface that helps maintain interoperability. Although it is out of the scope of this tutorial, you can check out further by reading the [getting started with Modbus RTU tutorial](/tutorials/opta/getting-started-with-modbus-rtu) after this tutorial for a better understanding.

## Instructions

### Setting up With Arduino IDE

We will need to have the latest version of the Arduino IDE. You can download the Arduino IDE from [here](https://www.arduino.cc/en/software). Please look at [getting started with Opta™ tutorial](/tutorials/opta/getting-started) if it is your first time setting up the Opta™ with the Arduino IDE.

The [ArduinoRS485](https://www.arduino.cc/reference/en/libraries/arduinors485/) library will be used to enable the RS485 interface with Opta™. The library can be found via Arduino IDE Library Manager and make sure to install the latest version of the library. Once it's installed, we will use a simple sketch to verify and help you understand the RS485 interface of two Opta™ devices.

### RS485 Interface with the Opta™

Please refer to the following diagram for establishing the RS485 interface between Opta™ devices. The figure also indicates elements of interest, such as the status LEDs and relays, for the current tutorial's purpose.

![RS485 interface connection between two Opta™ devices](assets/opta-modbus-connection.svg)

### RS485 Example Overview

You will assign an Opta™ either as a sender or a receiver. As the role suggests, each Opta™ has a specific task.

The Sender Opta™ will await user input from `1` to `4` via Arduino IDE Serial Monitor. Each number represents the relay to trigger and its corresponding status LED.

The Receiver Opta™ will intercept incoming Bytes and decode them to take proper action. It will update the relay state and the status LED accordingly, given its present condition.

For instance, if it receives `2` from Sender while the Receiver has a second relay closed with a lit second status LED, the Receiver will open the relay and turn off the second status LED as a deactivation indication. The process is vice-versa and applies to the rest of the relays with their respective status LEDs.

We will highlight portions of the example code with a brief description for better understanding in the continuing sections.

### RS485 Sender Sketch

The Sender Opta™ is defined with adequate parameters for correct data transmission via RS485 interface. This is defined per specification with following setup:

```arduino
#include <ArduinoRS485.h>

constexpr auto baudrate{ 115200 };

// Calculate preDelay and postDelay in microseconds as per Modbus RTU Specification
constexpr auto bitduration{ 1.f / baudrate };
constexpr auto wordlen{ 9.6f };  // OR 10.0f depending on the channel configuration
constexpr auto preDelayBR{ bitduration * wordlen * 3.5f * 1e6 };
constexpr auto postDelayBR{ bitduration * wordlen * 3.5f * 1e6 };
```

This will then be used within `setup()` to initialize RS485 interface alongside appropriate configuration. In this tutorial, we are using baud rate of `115200` but it can be configured at a different rate. It is important to have matching baud rate between sender and receiver for stable operation.

```arduino
void setup() {
  Serial.begin(baudrate);  // opens serial port
  while (!Serial);

  RS485.begin(baudrate);
  RS485.setDelays(preDelayBR, postDelayBR);
}
```

As the Sender's job is to pack the data and transfer it to the Receiver, it will need to transmit perspicuous data. Inside the `loop()` method, it will capture the input and write the Byte after a series of checks to avoid sending bogus characters.

```arduino
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

The Receiver Opta™ has the same configuration as Sender Opta™. But since it needs to trigger the relays with their corresponding status LEDs based on the received data, we will define such properties and their states handled in an array with other flags.

```arduino
int idx{ 0 };
bool newState{ false };

int relays[]{ D0, D1, D2, D3 };
int leds[]{ LED_D0, LED_D1, LED_D2, LED_D3 };
bool statuses[]{ true, true, true, true };
```

On top of initializing the RS485 interface, we will set the relays and the status LEDs as an `OUTPUT` state. These will allow controlling the relays with their visual indicators given captured data over the RS485 interface.

```arduino
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
```

The `loop()` will seek available data over the RS485 interface and handle the packet accordingly when captured. It will manage out-of-range inputs and apply them to the intended relay and status LED.

```arduino
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
```

The `changeRelay()` method manages the relay and status LED state based on the input.

```arduino
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

### Complete RS485 Example Code

You can access the complete example code by accessing [here](assets/Opta_RS485_Example.zip). The examples are easy to locate as their names suggest: `Opta_RS485_Sender` and `Opta_RS485_Receiver` after extracting the files.

### Testing Out the Sketches

Let's test the application with the sender Opta™ device connected to the Serial Monitor of the Arduino IDE and the receiver Opta™ device powered on. In the Serial Monitor, send a value between `1` and `4`; sending a `1` should close relay one and turn on the corresponding status LED, from left to right, of the receiver Opta™ device. Sending a `1` again should open the relay and turn off the status LED.

Here is a review of the values the receiver Opta™ device can receive and the result they produce:

- Sending `1`: Will turn on or off the first relay and the first status LED
- Sending `2`: Will turn on or off the second relay and the second status LED
- Sending `3`: Will turn on or off the third relay and the third status LED
- Sending `4`: Will turn on or off the fourth relay and the fourth status LED

## Conclusion

In this tutorial, we established the RS485 connection between two Opta™ devices. We learned how to use the `ArduinoRS485.h` library to send and receive values between these two devices. Finally, the tutorial showed how to take the data sent via RS485 to interact with the Opta™ hardware features, such as its on-board relays and status LEDs.

### Next Steps

Now that you are familiar with the RS485 communication interface on the Opta™, look at our [getting started tutorial](/tutorials/opta/getting-started) to get a better overview of other features on the device.

If you wish to incorporate Wi-Fi/Bluetooth® Low Energy in your Opta™ solutions, have a look at our [connectivity tutorial](/tutorials/opta/getting-started-connectivity).

If you are interested in seeing the RS485 interface and the Opta™ being put to work in a real-life scenario, have a look at our [Tank level application note](/tutorials/opta/tank-level-app-note).