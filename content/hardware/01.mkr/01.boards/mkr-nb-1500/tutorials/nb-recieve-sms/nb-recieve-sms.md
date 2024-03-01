---
title: 'Receive an SMS with MKR NB 1500'
difficulty: intermediate
compatible-products: [mkr-nb-1500]
description: 'Learn how to setup your board to print incoming text messages in the Serial Monitor.'
tags:
  - NB-IoT
  - CAT-M1
  - SMS
author: 'Benjamin Dannegård'
libraries: 
  - name: MKRNB
    url: https://www.arduino.cc/reference/en/libraries/mkrnb/
hardware:
  - hardware/01.mkr/01.boards/mkr-nb-1500
  - _snippets/hardware/dipole-antenna
  - _snippets/hardware/sim-card
software:
  - ide-v1
  - ide-v2
  - web-editor
---

## Introduction 

This tutorial is a continuation of the [Send an SMS with MKR NB 1500](/tutorials/mkr-nb-1500/nb-send-sms) tutorial, where you can read more about how the available networks for the NB 1500 work. In the previous tutorial we set up the MKR NB 1500 to send a text message to a phone, and in this tutorial, we will see how we can also receive text messages!

## Goals

The goals of this project are:

- Receive an SMS using the selected NB network.
- Print the message + sender in the Serial Monitor.

## Hardware & Software Needed

- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software)).
- [MKRNB](https://www.arduino.cc/en/Reference/MKRNB) library installed. 
- Arduino MKR NB 1500 ([link to store](https://store.arduino.cc/arduino-mkr-nb-1500-1413)).
- Antenna ([link to store](https://store.arduino.cc/antenna))
- SIM card from an operator in your country.

## Useful Scenarios for Receiving SMS

Using IoT technology is gaining more and more popularity, as it is gaining more and more coverage around the world. Practically speaking, where your phone has coverage, the MKR NB 1500 has coverage. This of course varies depending on what type of antenna you use. But often enough, even in remote woods, mountain areas and generally desolate places, we have coverage. We might not be able to stream movies or download larger files, but we are able to send and receive messages, either over Internet, or through calls or text messages.

If we manage to get access to one radio tower, it means we can reach the rest of the country we live in, and, of course, the world (for calls and text messages, this may be quite expensive however). This opens up many possibilities for projects in both rural and urban areas, when we either need to be updated, or to update something when we can't physically access it.

Now, in this tutorial, we will simply see how we can use a smartphone (or regular phone) to send a text message to our MKR NB 1500 board, and print the message in the Serial Monitor.

### Circuit

The circuit for this tutorial is easy: simply attach the dipole antenna to the board.

![Simple circuit of board and antenna](assets/MKRNB_T2_IMG01.png)

## Creating the Program

We will now get to the programming part of this tutorial. 

**1.** First, let's make sure we have the drivers installed. If we are using the Web Editor, we do not need to install anything. If we are using an offline editor, we need to install it manually. This can be done by navigating to **Tools > Board > Board Manager...**. Here we need to look for the **Arduino SAMD boards (32-bits Arm® Cortex®-M0+)** and install it. 

**2.** Now, we need to install the libraries needed. If we are using the Web Editor, there is no need to install anything. If we are using an offline editor, simply go to **Tools > Manage libraries..**, and search for **MKRNB** and install it.

**3.** We can now go to **File > Examples > MKRNB > ReceiveSMS** in the editor. This will open a new window, which has a sketch tab, but also a header file, called `arduino_secrets.h`. Inside this file, we need to enter our pin number between the "". 
   
```cpp
#define SECRET_PINNUMBER     "" //enter pin code between ""
```
   
The pin number is often 1234 or 0000, but for more information, check the SIM plan that you bought.

**4.** Let's take a look at some of the core functions of this sketch:

- `NB nbAccess` - base class for all NB functions.
- `NB_SMS sms` - base class for all NB functions for SMS.
- `nbAccess.begin(pin)` - connects to the selected network with the pin number as a parameter, e.g. 0123.
- `sms.available()`
- `sms.remoteNumber(number, 20)` - retrieves a sender's number. 
- `sms.beginSMS(number);` - creates an SMS for a specific number.  
- `sms.endSMS()` - sends the SMS.
- `sms.flush()` - deletes the message from the modem memory.

The sketch can also be found in the snippet below. Select the right board and port, and upload the sketch to the board.

```cpp
// include the NB library
#include <MKRNB.h>

#include "arduino_secrets.h" 
// Please enter your sensitive data in the Secret tab or arduino_secrets.h
// PIN Number
const char PINNUMBER[] = SECRET_PINNUMBER;

// initialize the library instances
NB nbAccess;
NB_SMS sms;

// Array to hold the number an SMS is retrieved from
char senderNumber[20];

void setup() {
  // initialize serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  Serial.println("SMS Messages Receiver");

  // connection state
  bool connected = false;

  // Start connection
  while (!connected) {
    if (nbAccess.begin(PINNUMBER) == NB_READY) {
      connected = true;
    } else {
      Serial.println("Not connected");
      delay(1000);
    }
  }

  Serial.println("NB initialized");
  Serial.println("Waiting for messages");
}

void loop() {
  int c;

  // If there are any SMSs available()
  if (sms.available()) {
    Serial.println("Message received from:");

    // Get remote number
    sms.remoteNumber(senderNumber, 20);
    Serial.println(senderNumber);

    // An example of message disposal
    // Any messages starting with # should be discarded
    if (sms.peek() == '#') {
      Serial.println("Discarded SMS");
      sms.flush();
    }

    // Read message bytes and print them
    while ((c = sms.read()) != -1) {
      Serial.print((char)c);
    }

    Serial.println("\nEND OF MESSAGE");

    // Delete message from modem memory
    sms.flush();
    Serial.println("MESSAGE DELETED");
  }

  delay(1000);

}
```

## Testing It Out

After the code has been successfully uploaded, we need to open the Serial Monitor to initialize the rest of the program. For these type of projects, we use the `while(!Serial)` command, so we can read any available information only after we open the Serial Monitor.

After we open the Serial Monitor, the board will attempt to connect to the selected network, and if it is successful, the following message can be seen in the Serial Monitor:

![Waiting for messages.](assets/MKRNB_T2_IMG02.png)

This means that we are ready to receive text messages. Now, we can open our phone, and send a text message to the number attached to your SIM card. 

We can send something simple, such as: 

```
Hi there NB 1500, can you read?
```

After we have sent the message, it should appear in the Serial Monitor after a few seconds. If it successful, we will see the following message printed:

![SMS received.](assets/MKRNB_T2_IMG03.png)

### Troubleshoot

If the code is not working, there are some common issues we can troubleshoot:

- Wrong pin number.
- SIM card lacking a data plan.
- Wrong network technology was selected when running the RAT example
- Antenna not attached properly. 
- We have sent the message to the wrong number.

## Conclusion

In this tutorial, we have used the `ReceiveSMS` example, which allows us to receive SMS from an external device, and print it in the Serial Monitor.

Feel free to explore the [MKRNB](https://www.arduino.cc/en/Reference/MKRNB) library further, and try out some of the many cool functions in this library.

### More Tutorials

You can find more tutorials for this board in the [MKR NB 1500 getting started page](https://www.arduino.cc/en/Guide/MKRNB1500).

