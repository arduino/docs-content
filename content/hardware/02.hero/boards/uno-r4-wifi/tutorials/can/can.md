---
title: 'Arduino UNO R4 WiFi CAN Bus'
description: 'Learn how to send messages using the CAN bus on the UNO R4 WiFi.'
tags:
  - CAN
author: 'Karl Söderby'
---

In this tutorial you will learn how to use the CAN controller on the **Arduino UNO R4 WiFi** board. The CAN controller is embedded in the UNO R4 WiFi's microcontroller (RA4M1). CAN is a serial protocol that is mainly used in the automotive industry.

***Please note that CAN controller requires an external transceiver to function. Instructions and hardware examples are provided in this tutorial.***

## Goals

The goals of this tutorial are:
- Get an overview of the built-in CAN library
- Learn how to connect a board to a CAN transceiver module
- Send a CAN message between two Arduinos

## Hardware & Software Needed

- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software))
- [Arduino R4 WiFi](https://store.arduino.cc/products/arduino-uno-r4-wifi)
- [Arduino Renesas Core](https://github.com/bcmi-labs/ArduinoCore-renesas)
- CAN transceiver module\* 
- Jumper wires

\*In this tutorial, we are using a SN65HVD230 breakout module. 

## Controller Area Network (CAN)

The CAN bus uses two wires: **CAN high** and **CAN low**. On the UNO R4 WiFi, these pins are: 
- D5/CANRX0 (receive)
- D4/CANTX0 (transmit)

To communicate with other CAN devices however, you need a transceiver module. In this tutorial, we will be using a SN65HVD230 breakout. To connect this, you can follow the circuit diagram available in the section below.

For this tutorial, we will use a simple example that sends a CAN message between two UNO R4 WiFi devices. If you wish, you can also connect an existing CAN device to the UNO R4 WiFi.

## Circuit

To connect the CAN transceiver, follow the table and circuit diagram below:

| UNO R4 WiFi | CAN Transceiver |
| ------------- | --------------- |
| D5 (CANRX0)   | CANRX           |
| D4 (CANTX0)   | CANTX           |
| 5V            | VIN/VCC/5V      |
| GND           | GND             |

Then, between the CAN transceivers, connect the following:

| CAN Transceiver 1 | CAN Transceiver 2 |
| ----------------- | ----------------- |
| CANH (HIGH)       | CANH (HIGH)       |
| CANL (LOW)        | CANL (LOW)        |

## Code Examples

The following code examples needs to be uploaded to each of the UNO R4 WiFi boards, one will send a message, one will receive it. These examples are available in the Renesas core, and using the Arduino IDE, you can access them by navigating to **File > Examples > Arduino_CAN > CANWrite/CANRead**

The library used is built in to the core, so no need to install the library if you have the core installed.

To initialize the library, use `CAN.begin(CanBitRate::BR_250k)`, where a CAN bit rate is specified. Choose between:
- BR_125k (125000)
- BR_250k (250000)
- BR_500k (500000)
- BR_1000k (1000000)

### CAN Write

To send a CAN message, you can create a `CanMsg` object, which should contain the `CAN_ID`, size and message data. Below is an example on how to create such object.

```arduino
uint8_t const msg_data[] = {0xCA,0xFE,0,0,0,0,0,0};
memcpy((void *)(msg_data + 4), &msg_cnt, sizeof(msg_cnt));
CanMsg msg(CAN_ID, sizeof(msg_data), msg_data);
```

After you have crafted a CAN message, we can send it off, by using the `CAN.write()` method. The following example creates a CAN message that increases each time `void loop()` is executed. 

```arduino
#include <Arduino_CAN.h>

static uint32_t const CAN_ID = 0x20;

void setup()
{
  Serial.begin(115200);
  while (!Serial) { }

  if (!CAN.begin(CanBitRate::BR_250k))
  {
    Serial.println("CAN.begin(...) failed.");
    for (;;) {}
  }
}

static uint32_t msg_cnt = 0;

void loop()
{
  /* Assemble a CAN message with the format of
   * 0xCA 0xFE 0x00 0x00 [4 byte message counter]
   */
  uint8_t const msg_data[] = {0xCA,0xFE,0,0,0,0,0,0};
  memcpy((void *)(msg_data + 4), &msg_cnt, sizeof(msg_cnt));
  CanMsg msg(CAN_ID, sizeof(msg_data), msg_data);

  /* Transmit the CAN message, capture and display an
   * error core in case of failure.
   */
  if (int const rc = CAN.write(msg); rc < 0)
  {
    Serial.print  ("CAN.write(...) failed with error code ");
    Serial.println(rc);
    for (;;) { }
  }

  /* Increase the message counter. */
  msg_cnt++;

  /* Only send one message per second. */
  delay(1000);
}
```

### CAN Read

To read an incoming CAN message, first use `CAN.available()` to check if data is available, before using `CAN.read()` to read the message.

```arduino
#include <Arduino_CAN.h>

void setup()
{
  Serial.begin(115200);
  while (!Serial) { }

  if (!CAN.begin(CanBitRate::BR_250k))
  {
    Serial.println("CAN.begin(...) failed.");
    for (;;) {}
  }
}

void loop()
{
  if (CAN.available())
  {
    CanMsg const msg = CAN.read();
    Serial.println(msg);
  }
}
```

## Summary

This tutorial shows how to use the CAN bus available on the UNO R4 WiFi, and how to send and receive data using the Arduino_CAN library.

Read more about this board in the [Arduino UNO R4 WiFi documentation](/hardware/uno-r4-wifi).
