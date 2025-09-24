---
author: Arduino
tags: [Yún]
title: 'Arduino Yún Console Pixel'
description: 'Control an LED through the Console.'
---

An example of using a Yún device to receive data on the Console from a computer.  In this case, the Yún device turns the on-board LED connected to digital pin 13 on  when it receives the character 'H', and off when it receives the character 'L'.

The Console, based on Bridge, enables you to send information between the Yún device and a computer just as you would with the serial monitor, but wirelessly. It creates a secure connection between the Yún device and your computer via SSH.

To see the Console, make sure your Yún device and computer are in the same wireless network. Pick your Yún's name and IP address in the Port menu in the Arduino Software (IDE) then open the Serial Monitor. You can also see it by opening a terminal window and typing `ssh root@ yourYúnsName.local 'telnet localhost 6571'` then pressing enter. When prompted for the password, enter it.

## Hardware Required

- Yún board or shield

- computer and Yún device on the same wireless network

## Circuit

There is no circuit for this example.

![The circuit for this tutorial.](assets/Yun_Fritzing.png)

image developed using [Fritzing](http://www.fritzing.org). For more circuit examples, see the [Fritzing project page](http://fritzing.org/projects/)

## Code

Include the Console library, which inherits from Bridge.
`#include <Console.h>`

Create variables and name the pin to write to, and another one to store the incoming byte from the Console.

```arduino
const int ledPin = 13;
char incomingByte;
```

In `setup()` initialize the Bridge and Console, and wait for a connection to the Console port.

```arduino
void setup() {

  Bridge.begin();

  Console.begin();

  while(!Console);
```

Once connected, print out some basic instructions to the Console window with `Console.println()` and set the LED pin as an output.

```arduino
Console.println("type H or L to turn pin 13 on or off");

  pinMode(ledPin, OUTPUT);
}
```

In `loop()`, check to see if there is information from the Console. If there is, read the oldest byte in the buffer and echo it back to the Console window.

```arduino
void loop() {

  if (Console.available() > 0) {

    incomingByte = Console.read();

    Console.println(incomingByte);
```

If the incoming byte is a capital "H", turn the LED on, if it is a "L", turn the LED off.

```arduino
if (incomingByte == 'H') {

      digitalWrite(ledPin, HIGH);

    }

    if (incomingByte == 'L') {

      digitalWrite(ledPin, LOW);

    }

  }
}
```

The complete sketch is below :

```arduino

/*

  Console Pixel

 An example of using YunShield/Yún board to receive data from the

 Console on the Yún.  In this case, the board turns on an LED when

 it receives the character 'H', and turns off the LED when it

 receives the character 'L'.

 To see the Console, pick your Yún's name and IP address in the Port menu

 then open the Port Monitor. You can also see it by opening a terminal window

 and typing

 ssh root@ yourYunsName.local 'telnet localhost 6571'

 then pressing enter. When prompted for the password, enter it.

 The circuit:

 * LED connected from digital pin 13 to ground

 created 2006

 by David A. Mellis

 modified 25 Jun 2013

 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/ConsolePixel

 */

#include <Console.h>

const int ledPin = 13; // the pin that the LED is attached to
char incomingByte;      // a variable to read incoming Console data into

void setup() {

  Bridge.begin();   // Initialize Bridge

  Console.begin();  // Initialize Console

  // Wait for the Console port to connect

  while (!Console);

  Console.println("type H or L to turn pin 13 on or off");

  // initialize the LED pin as an output:

  pinMode(ledPin, OUTPUT);
}

void loop() {

  // see if there's incoming Console data:

  if (Console.available() > 0) {

    // read the oldest byte in the Console buffer:

    incomingByte = Console.read();

    Console.println(incomingByte);

    // if it's a capital H (ASCII 72), turn on the LED:

    if (incomingByte == 'H') {

      digitalWrite(ledPin, HIGH);

    }

    // if it's an L (ASCII 76) turn off the LED:

    if (incomingByte == 'L') {

      digitalWrite(ledPin, LOW);

    }

  }
}
```

**Last revision 2016/05/25 by SM**
