---
title: 'Getting Started with RS-485 on the Arduino Opta™'
description: "Learn how to make use of the RS-485 communication interface on the Arduino Opta™."
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

The Opta™ is equipped with the RS-485 communication interface. Using this feature is easy with the help of the Arduino ecosystem tools, such as the Arduino IDE and the [ArduinoRS485 library](https://www.arduino.cc/reference/en/libraries/arduinors485/). This tutorial will follow the steps to connect two Opta™ devices via RS-485 and the Arduino IDE; it will describe some essential library functions and show an example sketch that uses the library and the RS-485 interface.

## Goals

- Learn how to connect two Opta™ devices through their RS-485 communication interface
- Learn how to send and receive information between two Opta™ devices through their RS-485 communication interface
  
### Required Hardware and Software

- USB-C® cable (x1)
- [Opta™ RS485](https://store.arduino.cc/pages/opta) (x2)
- 12-24VDC, 1A power supply (x1)
- [Arduino IDE 2](https://www.arduino.cc/en/software)
- [ArduinoRS485 library](https://www.arduino.cc/reference/en/libraries/arduinors485/)
- 24AWG twisted-pair cable (for connecting the Optas via their RS-485 communication interface)

***Notice: This tutorial does not work with Opta™ Lite since it does not have an RS-485 communication interface.***

## Instructions

### Setting up With Arduino IDE

First, ensure that you have installed the latest version of the Arduino IDE; you can download the IDE from [here](https://www.arduino.cc/en/software). Please look at our [getting started with Opta™ tutorial](/tutorials/opta/getting-started) if you need help setting up the Opta™ with the Arduino IDE.

Let's use a library to make it easier to use the RS485 protocol with Opta™. The library is called [ArduinoRS485](https://www.arduino.cc/reference/en/libraries/arduinors485/), which can be found in the Arduino IDE Library Manager. Once installed, let's take a look at a simple sketch to test the RS-485 communication between two Opta™ devices.

### RS-485 Communication with the Opta™

The sender sketch will let you send a message over the Arduino IDE Serial Monitor to the receiving device via RS-485. The receiving device will take the received message, open or close the corresponding relay, and turn on or off a LED. If you send the number 0 through the Serial Monitor, the receiving Opta™ will open or close the relay one depending on its current status while turning on or off a status LED at the same time.

Here are some important functions in the sketch:

- `RS485.begin(9600)`: Initializes the RS-485 object communication speed with assigned baud rate, `9600` in this case
- `RS485.beginTransmission()`: Enables RS-485 transmission
- `RS485.print()`: Writes binary data over RS-485; data is sent as a byte or series of bytes
- `RS485.endTransmission()`: Disables RS-485 transmission

Connect the Opta™ devices according to the image shown below:

![RS-485 connection between two Opta™ devices](assets/opta-modbus-connection.png)

### RS-485 Sender Sketch

Upload the following sender sketch to the Opta™ device you want to designate as the sender device:

```arduino
#include <ArduinoRS485.h>

int incomingByte = 0; // for incoming serial data

void setup() {
  Serial.begin(115200); // opens serial port
  RS485.begin(9600);
}

void loop() {

  if (Serial.available() > 0)
  {
    incomingByte = Serial.read();
    RS485.beginTransmission();
    Serial.print("- Sending: ");
    Serial.println(incomingByte);
    RS485.print(incomingByte);
    RS485.endTransmission();
    delay(1000);
  }
}
```


### RS-485 Receiver Sketch

Some important functions in the receiver sketch:

- `RS485.begin(9600)`: Make sure this is set to the same baud rate as the sender device, `9600` in this case.
- `RS485.receive()`: Enables reception through the RS-485 connection.
- `RS485.parseInt()`: We use this function to ensure that the correct value is received and read.

Now upload this sketch to the receiver Opta™ device:

```arduino
#include <ArduinoRS485.h>
int readValue = 0;
bool newState = false;

int relays[] = {D0, D1, D2, D3};
int leds[] = {LED_D0, LED_D1, LED_D2, LED_D3};

void setup() {
    for (int i = 0; i < 4; i++) {
        pinMode(relays[i], OUTPUT);
        pinMode(leds[i], OUTPUT);
    }

    RS485.begin(9600);
    RS485.receive();

    Serial.begin(9600);
    while (!Serial);
}

void loop() {
    while (RS485.available() > 0) {
        readValue = RS485.parseInt();
        Serial.print("- Incoming byte: ");
        Serial.println(readValue);
        newState = true;
    }

    if (newState) {
        changeRelay();
        newState = false;
    }
}

void changeRelay() {
    if (digitalRead(relays[readValue]) == 1) {
        digitalWrite(relays[readValue], LOW);
        digitalWrite(leds[readValue], LOW);
    }else {
        digitalWrite(relays[readValue], HIGH);
        digitalWrite(leds[readValue], HIGH);
    }
}
```

### Testing Out the Sketches

Let's test the application with the sender Opta™ device connected to the Serial Monitor of the Arduino IDE and the receiver Opta™ device powered on. In the Serial Monitor, send a value between `0`and `3`; sending a `0` should open relay one and turn on the first status LED, from left to right, of the receiver Opta™ device. Sending a `0` again should close the relay and turn off the status LED. 

Here is a review of the values the receiver Opta™ device can receive and the result they produce:

- Sending `0`: Will turn on or off the first relay and the first status LED
- Sending `1`: Will turn on or off the second relay and the first status LED
- Sending `2`: Will turn on or off the third relay and the first status LED
- Sending `3`: Will turn on or off the fourth relay and the first status LED

## Conclusion

In this tutorial, we established an RS-485 connection between two Opta™ devices. We learned how to use the `ArduinoRS485.h` library to send and receive values between these two devices. Finally, the tutorial showed how to take the values sent via RS-485 to interact with the Opta™ hardware features, such as its onboard relays and LEDs.

### Next Steps

Now that you are familiar with the RS-485 communication interface on the Opta™, look at our [getting started tutorial](/tutorials/opta/getting-started) to get a better overview of other features on the device.

If you wish to incorporate Wi-Fi/Bluetooth® Low Energy in your Opta™ solutions, have a look at our [connectivity tutorial](/tutorials/opta/getting-started-connectivity).

If you are interested in seeing the RS-485 interface and the Opta™ being put to work in a real-life scenario, have a look at our [Tank level application note](/tutorials/opta/tank-level-app-note).