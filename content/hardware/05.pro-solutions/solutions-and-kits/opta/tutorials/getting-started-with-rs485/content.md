---
title: 'Getting Started with RS-485 on Opta™'
description: "Learn how to make use of the RS-485 communication interface on Opta™."
difficulty: beginner 
tags:
  - Getting started
  - RS-485
author: 'Benjamin Dannegård and Taddy Chung'
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

The Opta™ micro PLC offers an easy-to-use and readily-available RS-485 interface. The RS-485 interface provides balanced performance to transmit data reliably over a long distance, with a stable transmission rate. Thanks to the Arduino ecosystem tools, such as the [Arduino IDE](https://www.arduino.cc/en/software) and the [ArduinoRS485 library](https://www.arduino.cc/reference/en/libraries/arduinors485/), it is really easy to implement communication protocols using the RS-485 interface.

This tutorial will show the steps to connect two Opta™ devices via RS-485 and the Arduino ecosystem tools; it will describe some essential functions of the [ArduinoRS485](https://www.arduino.cc/reference/en/libraries/arduinors485/) library and show an [example sketch](assets/Opta_RS485_Example.zip) that uses the library.

## Goals

- Learn how to connect two Opta™ devices through the RS-485 interface
- Learn how to exchange information between two Opta™ devices through the RS-485 interface and use it to control the onboard features of the Opta™

### Required Hardware and Software

- Opta™ PLC with RS-485 support (x2)
- 12-24VDC/1A power supply (x1)
- 24AWG twisted-pair cable (used for electrical connections)
- USB-C® cable (x1)
- [Arduino IDE 1.8.10+](https://www.arduino.cc/en/software), [Arduino IDE 2.0+](https://www.arduino.cc/en/software), or [Arduino Web Editor](https://create.arduino.cc/editor)
- [ArduinoRS485 library](https://www.arduino.cc/reference/en/libraries/arduinors485/)
- [RS-485 example code](assets/Opta_RS485_Example.zip)

***Notice: Please note that this tutorial is intended to work only with the Opta™ variants that have an RS-485 interface. Check your product information to know more.***

## The RS-485 Interface

The RS-485 is an electrical standard using a differential bus with voltage levels between 0-5V. The multi-drop feature allows the addition of drivers and receivers to the transmission line. The RS-485 interface has good noise immunity thanks to the differential signaling, which is a well-suited characteristic for industrial environment applications.

The RS-485 does not define a data communication protocol since it does not know how to interpret such information nor when or what to do to process it: it is only an electrical standard. An example of a data communication protocol using RS-485 is Modbus RTU. For more information about this data communication protocol, you can check our [getting started with Modbus RTU tutorial](/tutorials/opta/getting-started-with-modbus-rtu) with the Opta™.

## Instructions

### Setting up the Arduino IDE

This tutorial will need the latest version of the Arduino IDE. You can download the Arduino IDE [here](https://www.arduino.cc/en/software). Please check the [getting started with the Opta™ tutorial](/tutorials/opta/getting-started) if it is your first time setting up the Opta™ with the Arduino IDE.

The [ArduinoRS485 library](https://www.arduino.cc/reference/en/libraries/arduinors485/) will be used to simplify the use of RS-485 communication interface on Opta™. This library can be installed via Arduino IDE Library Manager; make sure to install the latest version of the library.

### The RS-485 Interface in Opta™

Please refer to the following diagram for connecting two Opta™ devices via their RS-485 interface. The figure also indicates other onboard features of the Opta™, such as its status LEDs and relays which will be used during the tutorial.

![Connection of two Opta™ devices via RS-485](assets/opta-modbus-connection.svg)

### Example Overview

We will define one Opta™ as sender and the other as receiver device. As the roles suggest, each Opta™ has a specific task. In the case of the Opta™ acting as sender, the device will await for data from `1` to `4` via the serial monitor. The Arduino IDE provides a serial monitor that can be used for this task. Each number represents the relay to trigger and its corresponding status LED.

The Opta™ acting as receiver will get the incoming data, decode them, and discard non-valid or out-of-range data. The decoded data will switch the relay state and the status LED to the opposite of the current state. For instance, if the receiver captures a `2` from the sender while the receiver has its 2nd relay closed with a turned-on 2nd status LED, the receiver will open the relay and turn off the 2nd status LED as a deactivation indication.

The other way around, in case of an open relay/LED off status, Opta™ will close the relay and turn on the status LED corresponding to the number received in the recent transmission. The same occurs for all the pairs of relays/status LEDs.

### The Opta™ Sender Sketch

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

These transmission parameters, applied in the Opta™ initialization, are crucial for a stable RS-485 data transmission as they will define the communication timings to make sure the lines of the RS-485 are already in a stable state. **Remember that it is necessary to have a matching baud rate between the sender and the receiver devices for stable operation**. In this tutorial, we are using a baud rate of `115200`, but it can be configured at a different baud rate:

```arduino
void setup() {
  Serial.begin(baudrate); 
  while (!Serial);

  RS485.begin(baudrate);
  RS485.setDelays(preDelayBR, postDelayBR);
}
```

The sender's job is to pack and transmit data to the receiver. Inside the main loop of the sketch, the sender will capture input data from the serial port and write the data after a series of checks to avoid sending incorrect data. Before converting the data to an integer, it is necessary to discard the end-of-line (EOL) as shown in the sketch.

The `RS485.beginTransmission()` method enables the RS-485 transmission. Subsequently, the `RS485.write(incomingByte)` method sends data as a byte or a series of bytes by writing their binary data to the serial port. In this case, we are sending to the receiver the `incomingByte` variable that contains the input data converted to an integer. The `RS485.endTransmission()` method then ends the RS-485 transmission, finishing the operation cycle.

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

### The Opta™ Receiver Sketch

The receiver has the same configuration as the sender. Although, since it needs to trigger the relays with their corresponding status LEDs based on the received data, it also configures the relays, built-in LEDs, and their status:

```arduino
int idx{ 0 };
bool newState{ false };

int relays[]{ D0, D1, D2, D3 };
int leds[]{ LED_D0, LED_D1, LED_D2, LED_D3 };
bool statuses[]{ true, true, true, true };
```

After initializing the RS-485 interface, the relays and the status LEDs are set as `OUTPUTS`. It will later help to control the relay with its corresponding visual indicator based on the received data over the RS-485:

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

In the main loop of the sketch, we will seek data sent over RS-485 and handle them accordingly. The loop manages out-of-range inputs and considers in-range data for the actuation of the intended relay and status LED. If the sender device forwards values that are not between `1` and `4`, the `readValue` variable will go through a module operation and return the remainder from the integer division to use as a correct input.

The `RS485.receive()` method enables the data reception via RS-485, then the `RS485.available()` method is used to determine if there are data available to be read. Once the data are available, the `RS485.read()` method will read the data and store them in the `readValue` variable. Finally, after managing the received data, the `RS485.noReceive()` method is called to disable the data reception over RS-485:

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

The `changeRelay()` function manages the relay and status LED state based on the received input packet. This function is called after receiving data via RS-485 to update the relay and status LED states accordingly:

```arduino
/**
  Changes relay and status LED state given the received value. 
*/
void changeRelay() {
  // Get current status
  auto status = statuses[idx] ? HIGH : LOW;
  
  // Apply new status to the outputs
  digitalWrite(relays[idx], status);
  digitalWrite(leds[idx], status);
  
  // Invert the statuses array to be updated
  statuses[idx] = !statuses[idx];
}
```

### Full Example Code

You can access the complete example code [here](assets/Opta_RS485_Example.zip); after extracting the files, `Opta_RS485_Sender` and `Opta_RS485_Receiver` sketches are available to try with your Opta™ devices.

### Testing Out the Sketches

Now it is time to test the application. Using the Serial Monitor of the Arduino IDE, send a value between `1` and `4` with the sender device. Sending a `1` will close the 1st relay and turn on the corresponding status LED of the receiver Opta™ device. Sending a `1` again will open the 1st relay and turn off the status LED of the receiver device.

Here is a list of the values the receiver Opta™ device can receive and the result they produce:

- **Sending `1`**: The first relay and the first status LED will turn on or off
- **Sending `2`**: The second relay and the second status LED will turn on or off
- **Sending `3`**: The third relay and the third status LED will turn on or off
- **Sending `4`**: The fourth relay and the fourth status LED will turn on or off

## Conclusion

In this tutorial, we established an RS-485 connection between two Opta™ devices. We also learned how to use the `ArduinoRS485.h` library to send and receive values between these two devices using RS-485 layer. Finally, the tutorial showed how to take the data sent via RS-485 to interact with the Opta™ PLC's hardware features, such as its onboard relays and status LEDs.

### Next Steps

Now that you are familiar with the RS-485 communication interface on the Opta™, take a look at the following documentation to learn more:

* Take a look at [getting started tutorial](/tutorials/opta/getting-started) to get a better overview of the features of Opta™

* If you wish to incorporate Wi-Fi®/Bluetooth® Low Energy in your Opta™ solutions, have a look at [connectivity tutorial](/tutorials/opta/getting-started-connectivity)

* If you are interested in seeing the RS-485 interface and the Opta™ being put to work in a real-life scenario, check the [tank level application note](/tutorials/opta/tank-level-app-note)
