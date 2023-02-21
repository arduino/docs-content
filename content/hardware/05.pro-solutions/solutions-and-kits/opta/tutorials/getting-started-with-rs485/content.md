---
title: 'Getting Started with RS-485 on Opta™'
description: "Learn how to make use of the RS-485 communication interface on Opta™."
difficulty: beginner 
tags:
  - Getting started
  - RS-485
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

The Opta™ micro PLC offers an easy-to-use and ready-available RS-485 interface. The RS-485 interface provides balanced performance to transmit data reliably over a long distance with a stable transmission rate. Thanks to the Arduino ecosystem tools, such as the [Arduino IDE](https://www.arduino.cc/en/software) and the [ArduinoRS485 library](https://www.arduino.cc/reference/en/libraries/arduinors485/), it is really easy to implement communication protocols using the RS-485 interface.

This tutorial will show the steps to connect two Opta™ devices via RS-485 and the Arduino ecosystems tools; it will describe some essential functions of the ArduinoRS485 library and show an example sketch that uses the library.

## Goals

- Learn how to connect two Opta™ devices through the RS-485 interface
- Learn how to exchange information between two Opta™ devices through the RS-485 interface and use it to control the onboard features of the Opta™

  
### Required Hardware and Software

- Opta™ PLC with RS-485 support (x2)
- 12-24VDC/1A power supply (x1)
- USB-C® cable (x1)
- [Arduino IDE 2](https://www.arduino.cc/en/software)
- [ArduinoRS485 library](https://www.arduino.cc/reference/en/libraries/arduinors485/)
- 24AWG twisted-pair cable (used for electrical connections)

***Notice: Please note that this tutorial is intended to work only with the Opta™ variants that have an RS-485 interface. Check your product information to know more.***

## RS-485 Interface

The RS-485 is an electrical-only standard that uses a differential bus with voltage levels between 0-5V. The multi-drop feature allows the addition of drivers and receivers to the transmission line. This RS-485 interface has good noise immunity thanks to differential signaling; which is a well-suited characteristic for industrial environment applications.

The RS-485 does not define a data communication protocol since it does not know how to interpret such information nor when or what to do to process it; it is only an electrical standard. An example of a data communication protocol that uses RS-485 is Modbus RTU. For more information about this data communication protocol, you can check our [getting started with Modbus RTU tutorial](/tutorials/opta/getting-started-with-modbus-rtu) with the Opta™.


## Instructions

### Setting up the Arduino IDE

This tutorial will need the latest version of the Arduino IDE. You can download the Arduino IDE [here](https://www.arduino.cc/en/software). Please check the [getting started with the Opta™ tutorial](/tutorials/opta/getting-started) if it is your first time setting up the Opta™ with the Arduino IDE.


The [ArduinoRS485 library](https://www.arduino.cc/reference/en/libraries/arduinors485/) will enable the RS-485 interface of the Opta™. This library can be installed via Arduino IDE Library Manager; make sure to install the latest version of the library.

### The RS-485 Interface in Opta™


Please refer to the following diagram for connecting two Opta™ via its RS-485 interface. The figure also indicates other onboard features of the Opta™, such as its status LEDs and relays; which will be also used during the tutorial.

![Connection of two Opta™ devices via RS-485](assets/opta-modbus-connection.svg)

### Example Overview

We will assign an Opta™ either as a sender or a receiver device. As the roles suggest, each Opta™ has a specific task. In the case of the Opta™ that acts as a sender, the device will await data from `1` to `4` via the serial monitor. The Arduino IDE provides a serial monitor that can be used for this task. Each number represents the relay to trigger and its corresponding status LED.

The receiver Opta™ will intercept incoming data, decode them, and process out-of-range incoming data. The decoded data will update the relay state and the status LED accordingly, given its present condition. For instance, if the receiver receives a `2` from the sender while the receiver has a second relay closed with a turned-on second status LED, the receiver will open the relay and turn off the second status LED as a deactivation indication. The process is vice-versa and applies to the rest of the relays with their respective status LEDs.

###  The Opta™ Sender Sketch

The first step to do is to define the RS-485 transmission parameters:

```arduino
#include <ArduinoRS485.h>

constexpr auto baudrate{ 115200 };

// Calculate preDelay and postDelay in microseconds for stable RS-485 transmission
constexpr auto bitduration{ 1.f / baudrate };
constexpr auto wordlen{ 9.6f };  // OR 10.0f depending on the channel configuration
constexpr auto preDelayBR{ bitduration * wordlen * 3.5f * 1e6 };
constexpr auto postDelayBR{ bitduration * wordlen * 3.5f * 1e6 };
```

These transmission parameters, applied in the Opta™ initialization, are crucial for a stable RS-485 data transmission as they will define communication timings. **Remember that it is necessary to have a matching baud rate between the sender and the receiver devices for stable operation**. In this tutorial, we use a baud rate of `115200`, but it can be configured at a different baud rate:

```arduino
void setup() {
  Serial.begin(baudrate); 
  while (!Serial);

  RS485.begin(baudrate);
  RS485.setDelays(preDelayBR, postDelayBR);
}
```

The sender's job is to pack and transmit data to the receiver. Inside the main loop of the sketch, the sender will capture input data from the serial port and write the data after a series of checks to avoid sending incorrect data. Before converting the data to an integer, it is necessary to discard the end-of-line (EOL) as it can be seen in the sketch.

The `RS485.beginTransmission()` method enables RS-485 transmission. Subsequently, the `RS485.write(incomingByte)` method sends data as a byte or a series of bytes by writing its binary data to the serial port. In this case, we are sending to the receiver the `incomingByte` variable that contains input data converted to an integer. The `RS485.endTransmission()` method then ends the RS-485 transmission. With this, an operation cycle is finished. It is all processed within the loop function.

```arduino
void loop() {
  auto aval = Serial.available();
  if (aval > 0) {
    auto input = Serial.readStringUntil('\r');

    // Discard EOL
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

### Receiver Sketch

The receiver has the same configuration as the sender. Although, since it needs to trigger the relays with their corresponding status LEDs based on the received data, it also configures the relays, and built-in LEDs and their states handled in an array with other flags:

```arduino
int idx{ 0 };
bool newState{ false };

int relays[]{ D0, D1, D2, D3 };
int leds[]{ LED_D0, LED_D1, LED_D2, LED_D3 };
bool statuses[]{ true, true, true, true };
```

After initializing the RS-485 interface, we will set the relays and the status LEDs as `OUTPUTS`. These will allow controlling the relays, and their corresponding visual indicators, given the received data over the RS-485:

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

In the main loop of the sketch, we will seek data sent over RS-485 and handle it accordingly. It manages out-of-range inputs and applies in-range data to the intended relay and status LED. If the sender device forwards values that are not between `1` and `4`, the `readValue` variable will go through module operation and return the remainder from the integer division; this is an example of how to manage out-of-range data.

The `RS485.receive()` method enables data reception via RS-485, then the `RS485.available()` method is used to determine if there is data available to read it; when data is available, the `RS485.read()` method will read the data and store it in the readValue variable. Finally, after managing the received data, the `RS485.noReceive()` method is called to disable data reception over RS-485:

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

The `changeRelay()` function manages the relay and status LED state based on the received input. This function is called after receiving data via RS-485 to update the relays and status LED states accordingly:

```arduino
/**
  Changes relay and status LED state given the received value. 

  @param none
  @return none
*/
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

### Complete Example Code

You can access the complete example code [here](assets/Opta_RS485_Example.zip); after extracting the files, `Opta_RS485_Sender` and `Opta_RS485_Receiver` sketches are available to try with your Opta™ devices.

### Testing Out the Sketches

Now it's time to test the application. Using the Serial Monitor of the Arduino IDE, send a value between `1` and `4` with the sender device; sending a `1` should close the relay one and turn on the corresponding status LED of the receiver Opta™ device. Sending a `1` again should open the relay and turn off the status LED of the receiver device.

Here is a review of the values the receiver Opta™ device can receive and the result they produce:

- **Sending `1`**: The first relay and the first status LED will turn on or off.
- **Sending `2`**: The second relay and the second status LED will turn on or off.
- **Sending `3`**: The third relay and the third status LED will turn on or off.
- **Sending `4`**: The fourth relay and the fourth status LED will turn on or off.

## Conclusion

In this tutorial, we established an RS-485 connection between two Opta™ devices. We also learned how to use the `ArduinoRS485.h` library to send and receive values between these two devices. Finally, the tutorial showed how to take the data sent via RS-485 to interact with the Opta™ hardware features, such as its onboard relays and status LEDs.

### Next Steps

Now that you are familiar with the RS-485 communication interface on the Opta™, look at [getting started tutorial](/tutorials/opta/getting-started) to get a better overview of other features on the device.

If you wish to incorporate Wi-Fi®/Bluetooth® Low Energy in your Opta™ solutions, have a look at [connectivity tutorial](/tutorials/opta/getting-started-connectivity).

If you are interested in seeing the RS-485 interface and the Opta™ being put to work in a real-life scenario, have a look at [tank level application note](/tutorials/opta/tank-level-app-note).
