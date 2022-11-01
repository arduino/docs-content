---
title: "Modbus"
description: "Modbus is an open serial communication protocol used for transmitting information over serial lines between electronic devices."
author: "Hannes Siebeneicher"
---

***Controller/peripheral is formerly known as master/slave. Arduino no longer supports the use of this terminology. Devices formerly known as master are referred to as controller and devices formerly known as slaves are referred to as peripheral.***

## What is Modbus?
Modbus is an open serial communication protocol used for transmitting information over serial lines between electronic devices. It was originally published by Modicon (now Schneider Electric) in 1979. The Modbus protocol is the oldest and by far the most popular automation protocol in the field of process automation. It enables devices, such as energy meters or humidity sensors connected to the same network to communicate the results to a supervisory computer or a Programmable Logic Computer (PLC). 

Several versions of the Modbus protocol exist for serial port and Ethernet and the most common are Modbus RTU, Modbus ASCII, Modbus TPU and Modbus Plus. It is based on a controller-peripheral (formerly known as master-slave) architecture and communication between nodes is achieved with send request and read response type messages. Modbus communicates over several types of physical media such as RS-232/RS-485 or Ethernet. The original Modbus interface ran on RS-232 serial communication but most of the later Modbus implementations use RS-485 because it allows for longer distances, higher speeds and the possibility of multiple devices on a single multi-drop network. The communication over serial RS-485 physical media works with two-wire transmit and receive connections.

On simple interfaces like RS-485 and RS-232, the Modbus messages are sent in plain form over the network and the network will be dedicated to only Modbus communication. However, if your network requires multiple heterogeneous devices using a more versatile system like TCP/IP over ethernet is recommended. In this case, Modbus and other types of mixed protocols can co-exist in the same physical interface at the same time. The main Modbus message structure is peer-to-peer, but it can also function on point-to-point and multidrop networks. As mentioned, the Modbus protocol communicates using a controller-peripheral technique in which only one device can initiate transactions, called queries.

## How does Modbus work?
Each Modbus message has the same structure, consisting of four basic elements which are present in each message and the sequence and order of these elements are the same for all messages. This allows for easy parsing of the content. The conversation is always started by the controller and when a message is sent the peripheral interprets the message and responds to it. Modbus sends functions which communicate read and write instructions to the peripheral’s internal memory registers to configure, monitor and control the peripheral’s inputs and outputs. Modbus devices will typically include a register map outlining where the configuration input and output data can be written and read from. You should always refer to the peripheral’s register map of your device to gain a better understanding of its overall operation.  

Modbus requests follow a simple structure:
![](assets/requestFrame.png)

### Device Address
Every peripheral device has its own address which it responds to when addressed by the controller, while all other devices ignore the message if the address doesn't match their own. Devices addresses are assigned in the range of 1 - 247.

### Function Code
The Function code tells the peripheral device if it should read or write data from the internal memory registers. Many of the data types are named from their use in driving relays, for example, a single-bit physical output is called a coil, and a single-bit physical input is called a discrete input or a contact. The following functions are supported by the Modbus poll:

- 01 READ COIL STATUS
- 02 READ INPUT STATUS
- 03 READ HOLDING REGISTERS
- 04 READ INPUT REGISTERS
- 05 WRITE SINGLE COIL
- 06 WRITE SINGLE REGISTER
- 15 WRITE MULTIPLE COILS
- 16 WRITE MULTIPLE REGISTERS

### Data
The data field contains the requested or send data. In the request form used by the Arduino Modbus library, the data field requires you to enter the starting registers and register count.

### CRC Error Check
The error checking is a value the controller or peripheral creates at the beginning of the transmission or response which is then checked when the message is received, to verify if the contents are correct. If the peripheral device accepts the request without error, it will return the same code in its response. However, if an error occurs, the peripheral will return 1 byte containing 8 binary bits `1000 0011` in the function code field and append a unique code in the data field of the response message, that tells the controller device what kind of error occurred or the reason for the error.

## Use Modbus with Arduino
Now that you have learned about the basics and functionalities of Modbus it is time to talk about how you can use your Arduino to establish Modbus communication across devices. You can use your Arduino either as a controller or as a peripheral device depending on the setup. To make your life easier you can use the [Arduino Modbus library](https://www.arduino.cc/reference/en/libraries/arduinomodbus/) which allows you to implement the Modbus protocol over two different types of transport: serial communication over RS485 with RTU or Ethernet and WiFi communication using the TCP protocol. Because the Modbus library is based on the [RS-485 library](https://www.arduino.cc/reference/en/libraries/arduinors485/) you must include both of them in your code.

A lot of Arduino boards are Modbus compatible especially if you consider Ethernet-type messages but if you want to communicate via RS485 there is the [MKR 485 Shields](https://store-usa.arduino.cc/products/arduino-mkr-485-shield) which can convert any MKR board into a Modbus compatible device. Check out [this Tutorial](https://docs.arduino.cc/tutorials/mkr-485-shield/mkr-485-communication) to learn more about sending data between two [MKR 485 Shields](https://store-usa.arduino.cc/products/arduino-mkr-485-shield). 

When using the [Modbus library](https://www.arduino.cc/reference/en/libraries/arduinomodbus/) sending messages is fairly straightforward as you can see in the examplary request format function below:

| Device Address |  Function Code  | Starting Register |  Register Count | 
|   -----------  |   -----------   |    -----------    |   -----------   |
|       0x21     | INPUT REGISTERS |       30107       |        2        |

***Note that this request form is specific to the [Modbus library](https://www.arduino.cc/reference/en/libraries/arduinomodbus/) and only works with boards compatible with this library. Make sure to check the specifications for the board you are using!***

You have to check the device-specific documentation to attain the right address, function code, starting registers and register count. The CRC error check is taken care of by the Modbus library. To make it easier to understand the example below shows how to use the Modbus library.

### Example
Let's say you have a Modbus-compatible energy meter working with RS-485. In our case, we use a model from [Finder](https://cdn.findernet.com/app/uploads/2021/09/20090052/Modbus-7M24-7M38_v2_30062021.pdf) but you can use a different one.

Take a look at the request frame inside the Finder documentation:

![](assets/finderRequestFrame.png)

We can see that the device address is 21 (or 0x21).

The function code states 04 which we know stands for INPUT REGISTERS ([see Function Code](#function-code)).

The starting register is 00 6B (or 0x6B) but for the Modbus library to work we need to change it from hexadecimal to decimal.
In this example, the starting register is stated as hexadecimal but if we scroll down further in the documentation we can see that the registers are written in decimals: 

![](assets/modbusMeasurmentFinder.png)

We can also see that the register for U1 takes up 30107 and 30108 which means that the register count is 2.

With all this information we can now use the function requestFrom() inside the readVoltage() function:

```
float readVoltage() {
  float volt = 0.;
  // Send reading request over RS485 
  if (!ModbusRTUClient.requestFrom(0x21, INPUT_REGISTERS, 30017, 2)) {
    // Error handling
    Serial.print("- Failed to read the voltage! ");
    Serial.println(ModbusRTUClient.lastError()); 
  } else {
    // Response handler 
    uint16_t word1 = ModbusRTUClient.read();  // Read word1 from buffer
    uint16_t word2 = ModbusRTUClient.read();  // Read word2 from buffer
    uint32_t millivolt = word1 << 16 | word2; // Join word1 and word2 to retrieve voltage value in millivolts
    volt = millivolt/1000.0;                  // Convert to volts
  }

  return volt;
}
```


### Modbus compatible Boards
- all boards compatible with the [MKR 485 Shield](https://docs.arduino.cc/hardware/mkr-485-shield) and the [MKR ETH Shield](https://docs.arduino.cc/hardware/mkr-eth-shield)
- all boards compatible with the [Ethernet Shield Rev2](https://docs.arduino.cc/hardware/ethernet-shield-rev2)
- [Portenta Machine Control](https://docs.arduino.cc/hardware/portenta-machine-control)
- [Max Carrier](https://docs.arduino.cc/hardware/portenta-max-carrier)

### Libraries
- [ArduinoRS485](https://www.arduino.cc/reference/en/libraries/arduinors485/)
- [ArduinoModbus](https://www.arduino.cc/reference/en/libraries/arduinomodbus/)