---
tags: [Yún]
author: Arduino
title: 'Arduino Yún Mailbox Read Message'
description: 'Send text messages to the Arduino processor using REST API through a browser.'
---

This example for a Yún device shows how to use the Bridge library to send text messages from the Linux to the AVR. It demonstrate how you can create a queue of messages using REST style calls through the browser.

When running this example, make sure your computer is on the same network as the Yún device.
Once you have uploaded the sketch on the board you can start to append messages in the Yún mailbox. The Mailbox will be checked every 10 seconds and the available messages displayed on the Serial Monitor.
To use the REST APIs you need to insert the password or disable it from the Web panel.
You can use a browser with the following URL structure:
http://myArduinoYun.local/mailbox/hello

## Hardware Required

- Yún board or shield

- computer and Yún on the same wireless or wired network

## Software Required

- web browser

## Circuit

There is no circuit for this example.

![The circuit for this tutorial.](assets/Yun_Fritzing.png)

image developed using [Fritzing](http://www.fritzing.org). For more circuit examples, see the [Fritzing project page](http://fritzing.org/projects/)

## Code

The example code shows how it's possible to make REST requests to the Yún deviceto send messages from the Linux side to the AVR. The messages are stored in a message queue, internal to the Linux side, and read by the AVR only when the readMessage() method is called.

You need to include only the Mailbox library because it automatically include the Bridge library:

```arduino
#include <Mailbox.h>
```

In `setup()`, start serial communication for debugging purposes, and turn the built-in LED on pin 13 high while Bridge begins. `Bridge.begin()` is blocking, and should take about 2 seconds to complete. Once Bridge starts up, turn the LED off. `Mailbox.begin()` starts the Mailbox on the OpenWrt-Yun and on the Arduino processor.

```arduino
void setup() {

  pinMode(13, OUTPUT);

  digitalWrite(13, LOW);

  // Initialize Bridge and Mailbox

  Bridge.begin();

  Mailbox.begin();

  digitalWrite(13, HIGH);

  // Initialize Serial

  Serial.begin(9600);

  // Wait until a Serial Monitor is connected.

  while (!Serial);

  Serial.println("Mailbox Read Message\n");

  Serial.println("The Mailbox is checked every 10 seconds. The incoming messages will be shown below.\n");
}
```

In `loop()`, you'll create a String where to save the incoming message and call the `Mailbox.messageAvailable()` function to read if there is an available message in the Mailbox.

```arduino
void loop() {

  String message;

  // if there is a message in the Mailbox

  if (Mailbox.messageAvailable())

  {
```

If there is at least one message in the Mailbox, start to read all the messages in the queue and print it on the Serial Monitor.

```arduino
// read all the messages present in the queue

    while (Mailbox.messageAvailable())

    {

      Mailbox.readMessage(message);

      Serial.println(message);

    }
```

The Mailbox in the sketch is checked every 10 seconds using a `delay()`. This is also done to demonstrate the advantage to store data on the Linux processor instead of cluttering the RAM of the Arduino processor.

```arduino
Serial.println("Waiting 10 seconds before checking the Mailbox again");

  }

  // wait 10 seconds

  delay(10000);
}
```

The full code is below:

```arduino
/*

  Read Messages from the Mailbox

 This example for the YunShield/Yún shows how to

 read the messages queue, called Mailbox, using the

 Bridge library.

 The messages can be sent to the queue through REST calls.

 Append the message in the URL after the keyword "/mailbox".

 Example

 "/mailbox/hello"

 created 3 Feb 2014

 by Federico Vanzati & Federico Fissore

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/MailboxReadMessage

 */

#include <Mailbox.h>

void setup() {

  pinMode(13, OUTPUT);

  digitalWrite(13, LOW);

  // Initialize Bridge and Mailbox

  Bridge.begin();

  Mailbox.begin();

  digitalWrite(13, HIGH);

  // Initialize Serial

  SerialUSB.begin(9600);

  // Wait until a Serial Monitor is connected.

  while (!SerialUSB);

  SerialUSB.println("Mailbox Read Message\n");

  SerialUSB.println("The Mailbox is checked every 10 seconds. The incoming messages will be shown below.\n");
}

void loop() {

  String message;

  // if there is a message in the Mailbox

  if (Mailbox.messageAvailable()) {

    // read all the messages present in the queue

    while (Mailbox.messageAvailable()) {

      Mailbox.readMessage(message);

      SerialUSB.println(message);

    }

    SerialUSB.println("Waiting 10 seconds before checking the Mailbox again");

  }

  // wait 10 seconds

  delay(10000);
}
```

**Last revision 2016/05/25 by SM**
