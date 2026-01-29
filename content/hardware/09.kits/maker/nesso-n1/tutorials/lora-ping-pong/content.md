---
title: 'LoRa® Ping-Pong with Nesso N1'
description: 'Learn how to implement a two-way LoRa® communication between two Nesso N1 boards, understanding the antenna switching mechanism.'
tags: 
  - LoRa
  - Nesso N1
  - Wireless
  - Ping Pong
  - Antenna
author: 'Arduino'
libraries: 
  - name: RadioLib
    url: https://github.com/jgromes/RadioLib
  - name: Arduino_Nesso_N1
    url: https://github.com/arduino-libraries/Arduino_Nesso_N1
hardware:
  - hardware/09.kits/maker/nesso-n1
software:
  - ide-v1
  - ide-v2
---

## Introduction

This tutorial demonstrates how to establish a peer-to-peer LoRa® communication between two Nesso N1 boards. Unlike simple transmitter/receiver examples, this "Ping-Pong" sketch enables two-way communication where devices exchange packets back and forth. You will also learn how to correctly configure the onboard RF switches to handle the transmission and reception paths using the SX1262 module.

## Goals

The goals of this tutorial are:

- Understand the Nesso N1 LoRa® antenna switching logic.
- Configure the SX1262 module using the RadioLib library.
- Implement a two-way communication system where one node initiates the exchange and the other responds.

## Hardware & Software Needed

- 2x [Arduino Nesso N1](https://store.arduino.cc/products/nesso-n1)
- [Arduino IDE](https://www.arduino.cc/en/software) (offline or Cloud Editor)
- **RadioLib** library (available via Library Manager)
- **Arduino_Nesso_N1** library (available via Library Manager)

## LoRa® Antenna Switching

The Nesso N1 features a sophisticated RF front-end design that includes an RF Antenna Switch (FM8625) and a Low Noise Amplifier (SGM1300). Proper control of these components is essential for optimal range and performance.

### Key Control Pins

- **`LORA_ANTENNA_SWITCH`**: This pin controls the supply to the RF antenna switch.
  - **HIGH**: Switch is powered and active. This is required for normal operation.
  - **LOW**: Switch is off.

- **`LORA_LNA_ENABLE`**: This pin controls the Low Noise Amplifier (LNA) on the receive path.
  - **HIGH**: LNA is ON. The signal from the antenna is amplified and passed to the SX1262's receive input (SRFI).
  - **LOW**: LNA is OFF. The path between the antenna and the receiver is disabled.

### Automated Tx/Rx Switching

The actual switching of the antenna between the Transmitter Output (SRFO) and Receiver Input (SRFI) is handled by the SX1262 module itself via its **DIO2** pin. 

In the code, we enable this feature with:
```cpp
radio.setDio2AsRfSwitch(true);
```
This ensures that the hardware automatically routes the signal to the correct path whenever the radio creates a transmission or starts listening.

## Programming the Board

The following code implements the Ping-Pong logic. One device acts as the "Initiator" (sending the first "Ping"), and the other listens and replies ("Pong").

### Configuration

You need to upload the code to **two** separate Nesso N1 boards with a slight difference:

1.  **Node A (Initiator)**: Uncomment the line `#define INITIATING_NODE` at the top of the sketch.
2.  **Node B (Listener)**: Keep the line `#define INITIATING_NODE` commented out.

```cpp
/*
  RadioLib SX126x Ping-Pong Example for Arduino Nesso N1

  This example is intended to run on two Nesso N1 devices,
  and send packets between the two.
  One device will initiate the transfer and this behaviour is marked by a #define

  For RadioLib's full API reference, see the GitHub Pages
  https://jgromes.github.io/RadioLib/
*/

#include <Arduino_Nesso_N1.h>
// include the library
#include <RadioLib.h>

// uncomment the following only on one
// of the nodes to initiate the pings
// #define INITIATING_NODE

// The Nesso N1 has an RF Antenna Switch (https://www.lcsc.com/datasheet/C2857391.pdf)
// that allows physically commuting the antenna's signal between RFin and RFout of the SX1262.
// driving LORA_ANTENNA_SWITCH LOW  will switch the antenna connector to SRFO (Tx)
// driving LORA_ANTENNA_SWITCH HIGH will switch the antenna connector to SRFI (Rx)

// On Nesso N1, SX1262 has the following connections:
// ANT SW     :   LORA_ANTENNA_SWITCH (EXP P6)        FM8625  VDD    (HIGH:ON / LOW:OFF)
// LNA enable :   LORA_LNA_ENABLE     (EXP P5)        SGM1300 ENABLE   (HIGH: Rx ON/amplified | LOW:Rx off)
// Note       :   The antenna signal will not pass through the LNA when off (must be ON).
//                Keeping it ON all the time will of course consume more power.
//                If the devices are very close receiving will work but it's to be considered a fluke.
//                
//                
// CS pin     :   LORA_CS             (C6 GPIO23)     SX1262  /NSS
// NRST pin   :   LORA_ENABLE         (EXP P7)        SX1262  /nRESET
// BUSY pin   :   LORA_BUSY           (C6 GPIO19)     SX1262  /BUSY
// IRQ pin    :   LORA_IRQ            (C6 )           SX1262  /DIO1
//


SX1262 radio = new Module(LORA_CS, LORA_IRQ, -1, LORA_BUSY);
// The 3rd parameter (-1) is referred to what to do with the SX1262's DIO2 pin.
// On Nesso N1 this GPIO is connected to the antenna Rx/Tx switch and is able to control it transparently.
// The configuration is enabled in setup() - radio.setDio2AsRfSwitch(true)

// save transmission states between loops
int transmissionState = RADIOLIB_ERR_NONE;

// flag to indicate transmission or reception state
bool transmitFlag = false;

// flag to indicate that a packet was sent or received
volatile bool operationDone = false;

// this function is called when a complete packet
// is transmitted or received by the module
// IMPORTANT: this function MUST be 'void' type
//            and MUST NOT have any arguments!
#if defined(ESP8266) || defined(ESP32)
  ICACHE_RAM_ATTR
#endif
void setFlag(void) {
  // we sent or received a packet, set the flag
  operationDone = true;
}

void setup() {
  Serial.begin(9600);
  unsigned long msNow = millis();
  while (!Serial && (millis() - msNow < 3000));

  // SX1262 is enabled on (nRST HIGH)
  pinMode(LORA_ENABLE, OUTPUT);
  digitalWrite(LORA_ENABLE, HIGH);

  // Input signal amplifier is turned on (HIGH)
  // If the devices are close enough this will have no effect
  // The amplifier can be turned ON all the time
  // Turning it off (LOW) will disable the route between the antenna and the SRFI of SX1262
  pinMode(LORA_LNA_ENABLE, OUTPUT);
  digitalWrite(LORA_LNA_ENABLE, HIGH);

  // The IO Expander pin P6 control the supply to the RF switch VDD pin
  // If the devices are close enough, even if this switch is turned off
  // the signal will be strong enough to be received/sent (consider it a fluke)
  
  pinMode(LORA_ANTENNA_SWITCH, OUTPUT);
  digitalWrite(LORA_ANTENNA_SWITCH, HIGH);

  // initialize SX1262 with default settings
  Serial.print(F("[SX1262] Initializing ... "));
  int state = radio.begin();
  if (state == RADIOLIB_ERR_NONE) {
    Serial.println(F("success!"));
  } else {
    Serial.print(F("failed, code "));
    Serial.println(state);
    while (true) { delay(10); }
  }

  // set the function that will be called
  // when new packet is received 
  radio.setDio1Action(setFlag);

  // tell the SX1262 to use its DIO2 pin to control the antenna switch (Tx/Rx)
  radio.setDio2AsRfSwitch(true);

  #if defined(INITIATING_NODE)
    // send the first packet on this node
    Serial.print(F("[SX1262] Sending first packet ... "));
    transmissionState = radio.startTransmit("Hello World!");
    transmitFlag = true;
  #else
    // start listening for LoRa packets on this node
    Serial.print(F("[SX1262] Starting to listen ... "));
    state = radio.startReceive();
    if (state == RADIOLIB_ERR_NONE) {
      Serial.println(F("success!"));
    } else {
      Serial.print(F("failed, code "));
      Serial.println(state);
      while (true) { delay(10); }
    }
  #endif
}

void loop() {
  // check if the previous operation finished
  // operationDone is set by the callback to DIO1 action (done transmitting or done receiving)
  // if the operation is done, it will check wether or not it is in transmit mode
  // and act accordingly

  if(operationDone) {
    Serial.println("operation done");
    delay(1000);
    // reset flag
    operationDone = false;

    if(transmitFlag) {
      // the previous operation was transmission, listen for response
      // print the result
      if (transmissionState == RADIOLIB_ERR_NONE) {
        // packet was successfully sent
        Serial.println(F("transmission finished!"));

      } else {
        Serial.print(F("failed, code "));
        Serial.println(transmissionState);

      }

      // listen for response
      // enable LNA here
      radio.startReceive();
      transmitFlag = false;

    } else {
      // the previous operation was reception
      // print data and send another packet
      String str;
      int state = radio.readData(str);
      // disable LNA here
      if (state == RADIOLIB_ERR_NONE) {
        // packet was successfully received
        Serial.println(F("[SX1262] Received packet!"));

        // print data of the packet
        Serial.print(F("[SX1262] Data:\t\t"));
        Serial.println(str);

        // print RSSI (Received Signal Strength Indicator)
        Serial.print(F("[SX1262] RSSI:\t\t"));
        Serial.print(radio.getRSSI());
        Serial.println(F(" dBm"));

        // print SNR (Signal-to-Noise Ratio)
        Serial.print(F("[SX1262] SNR:\t\t"));
        Serial.print(radio.getSNR());
        Serial.println(F(" dB"));

      }

      // wait a second before transmitting again
      delay(1000);

      // send another one
      Serial.print(F("[SX1262] Sending another packet ... "));
      transmissionState = radio.startTransmit("Hello World!");
      transmitFlag = true;
    }
  
  }
}
```

## Testing It Out

1.  Connect both boards to your computer.
2.  Open the Serial Monitor for both boards. Set the baud rate to **9600**.
3.  **Initiator Node**: You should see it initializing, then sending the first "Hello World!" packet.
4.  **Listener Node**: You should see it receive the packet, print the RSSI/SNR data, and then send a reply back.
5.  The communication should continue in a loop, with each device responding to the other.

### Troubleshoot

If communication is failing or unreliable:

- **Check Antenna**: Ensure the external LoRa® antenna is securely connected to the MMCX connector on both boards. **Do not transmit without an antenna.**
- **Frequency**: Ensure both boards are initialized to the same frequency. The `radio.begin()` function uses a default frequency (usually 434.0 MHz). You may need to specify a frequency that matches your region (e.g., `radio.begin(868.0)` for Europe or `radio.begin(915.0)` for US).
- **LNA Configuration**: Verify that `LORA_LNA_ENABLE` is set to `HIGH`. If this pin is LOW, the receiver is effectively disconnected from the antenna.

## Conclusion

In this tutorial, you learned how to configure the Nesso N1 for robust two-way LoRa® communication. By correctly managing the `LORA_ANTENNA_SWITCH` and `LORA_LNA_ENABLE` pins, and leveraging the `RadioLib` library's features, you can ensure your Nesso N1 projects achieve their maximum potential range and reliability.
