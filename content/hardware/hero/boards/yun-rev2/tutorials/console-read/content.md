---
author: Arduino
tags: [Yún]
title: 'Arduino Yún Console Read'
description: 'Parse information from the Console and repeat it back.'
---

This example for a Yún device reads data coming from Bridge using  `Console.read()` and stores it in a string.

To see the Console, pick your Yún's name and IP address in the Port menu then open the Serial Monitor. You can also see it by opening a terminal window and typing:  `ssh root@ yourYunsName.local 'telnet localhost 6571'` then pressing enter. When prompted for the password, enter it.

When running this example, make sure your computer is on the same network as the Yún device.

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

Create a string to hold the information from the Bridge
`String name;`

In `setup()` initialize the Bridge and Console. Wait for a Console connection, then ask for some information :

```arduino
void setup() {

  Bridge.begin();

  Console.begin();

  while (!Console);

  Console.println("Hi, what's your name?");
}
```

In `loop()`, check to see if there are bytes in the Console buffer. If there's something available, read the the oldest character into a local variable.

```arduino
void loop() {

  if (Console.available() > 0) {

    char c = Console.read();


```

If the character is a newline ("\n"), it is the last character in the incoming string. Print out the string to the Console, ask for more information, and clear the string.

```arduino
if (c == '\n') {

      Console.print("Hi ");

      Console.print(name);

      Console.println("! Nice to meet you!");

      Console.println();

      Console.println("Hi, what's your name?");

      name = "";

    }
}
```

If the character in the buffer is not a newline, add it to the end of the string.

```arduino
else {

      name += c;

    }

  }
}
```

The complete sketch is below :

```arduino

/*

Console Read example for YunShield/Yún

 Read data coming from bridge using the Console.read() function

 and store it in a string.

 To see the Console, pick your Yún's name and IP address in the Port menu

 then open the Port Monitor. You can also see it by opening a terminal window

 and typing:

 ssh root@ yourYunsName.local 'telnet localhost 6571'

 then pressing enter. When prompted for the password, enter it.

 created 13 Jun 2013

 by Angelo Scialabba

 modified 16 June 2013

 by Tom Igoe

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/ConsoleRead

 */

#include <Console.h>

String name;

void setup() {

  // Initialize Console and wait for port to open:

  Bridge.begin();

  Console.begin();

  // Wait for Console port to connect

  while (!Console);

  Console.println("Hi, what's your name?");
}

void loop() {

  if (Console.available() > 0) {

    char c = Console.read(); // read the next char received

    // look for the newline character, this is the last character in the string

    if (c == '\n') {

      //print text with the name received

      Console.print("Hi ");

      Console.print(name);

      Console.println("! Nice to meet you!");

      Console.println();

      // Ask again for name and clear the old name

      Console.println("Hi, what's your name?");

      name = "";  // clear the name string

    } else {     // if the buffer is empty Console.read() returns -1

      name += c; // append the read char from Console to the name string

    }

  } else {

    delay(100);

  }
}
```


**Last revision 2016/05/25 by SM**
