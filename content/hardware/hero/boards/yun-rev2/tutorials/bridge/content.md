---
title: 'Arduino Yún Bridge'
description: 'Access the pins of the board with a web browser.'
author: Arduino
tags: [Yún]
---

This example for a Yún device shows how to use the Bridge library to access the digital and analog pins on the board through REST calls. It demonstrates how you can create your own API when using REST style calls through the browser.

When running this example, make sure your computer is on the same network as the Yún device.
When you have have programmed the board, you can request the value on a pin, write a value to a pin, and configure a pin as an input or output.

When the REST password is turned off, you can use a browser with the following URL structure :

- http://myArduinoYun.local/arduino/digital/13 : calls `digitalRead(13);`
- http://myArduinoYun.local/arduino/digital/13/1 : calls `digitalWrite(13,1);`
- http://myArduinoYun.local/arduino/analog/9/123 : `analogWrite(9,123);`
- http://myArduinoYun.local/arduino/analog/2 : `analogRead(2);`
- http://myArduinoYun.local/arduino/mode/13/input : `pinMode(13, INPUT);`
- http://myArduinoYun.local/arduino/mode/13/output : `pinMode(13, OUTPUT);`

You can use the CURL command from the command line instead of a browser if you prefer.

## Hardware Required

- Yún board or shield

- computer and Yún device on the same wireless or wired network

## Software Required

- web browser

## Circuit

There is no circuit for this example.

![The circuit for this tutorial.](assets/Yun_Fritzing.png)

image developed using [Fritzing](http://www.fritzing.org). For more circuit examples, see the [Fritzing project page](http://fritzing.org/projects/)

## Code

The example code shows how it is possible to make REST requests to the Yún device to read from and write information to the board's pins.

You need to include the Bridge, YunServer, and YunClient libraries :

```arduino
#include <Bridge.h>
#include <YunServer.h>
#include <YunClient.h>
```

Instantiate a server enabling the the Yún device to listen for connected clients.

`YunServer server;`

In `setup()`, start serial communication for debugging purposes, and turn the built-in LED on pin 13 high while Bridge begins. `Bridge.begin()` is blocking, and should take about 2 seconds to complete. Once Bridge starts up, turn the LED off.

```arduino
void setup() {

  Serial.begin(9600);

  pinMode(13,OUTPUT);

  digitalWrite(13, LOW);

  Bridge.begin();

  digitalWrite(13, HIGH);
```

In the second part of `setup()`, tell the instance of YunServer to listen for incoming connections only coming from localhost. Connections made to Linux will be passed to the 32U4 processor for parsing and controlling the pins. This happens on port 5555. Start the server with `server.begin()`.

```arduino
server.listenOnLocalhost();

  server.begin();
}
```

In `loop()`, you'll create an instance of the YunClient for managing the connection. If the client connects, process the requests in a custom function (described below) and close the connection when finished.

Putting a delay at the end of `loop()` will be helpful in keeping the processor from doing too much work.

```arduino
void loop() {

  YunClient client = server.accept();

  if (client) {

    process(client);

    client.stop();

  }

  delay(50);
}
```

Create a function named `process` that accepts the YunClient as its argument. Read the command by creating a string to hold the incoming information. Parse the REST commands by their functionality (digital, analog, and mode) and pass the information to the appropriately named function.

```arduino
void process(YunClient client) {

  String command = client.readStringUntil('/');

  if (command == "digital") {

    digitalCommand(client);

  }

  if (command == "analog") {

    analogCommand(client);

  }

  if (command == "mode") {

    modeCommand(client);

  }
}
```

Create a function to deal with **digital** commands. Accept the client as the argument. Create some local variables to hold the pin and value of the command.

```arduino
void digitalCommand(YunClient client) {

  int pin, value;
```

Parse the client's request for the pin to work with using `client.parseInt()`.

If the character after the pin is a "/", it means the URL is going to have a value of 1 or 0 following. This value will assign a value to the pin, turning it HIGH or LOW. If there is no trailing "/", read the value from the specified pin.

```arduino
pin = client.parseInt();

  if (client.read() == '/') {

    value = client.parseInt();

    digitalWrite(pin, value);

  }

  else {

    value = digitalRead(pin);

  }
```

Print the value to the client and update the datastore key with the current pin value.

By wrapping the value to the client in `F()`, you'll be printing form the flash memory. This helps conserve space in SRAM, which is useful when dealing with long strings like URLs.

The key will be the pin, and type. For example **D2** will be saved for for digital pin 2. The value will be whatever value the pin is currently set to, or was read from the pin.

```arduino
client.print(F("Pin D"));

  client.print(pin);

  client.print(F(" set to "));

  client.println(value);

  String key = "D";

  key += pin;

  Bridge.put(key, String(value));
}
```

Set up a function to handle analog calls in the same fashion, except setting the key to A instead of D when working with the analog input pins :

```arduino
void analogCommand(YunClient client) {

  int pin, value;

  pin = client.parseInt();

  if (client.read() == '/') {

    value = client.parseInt();

    analogWrite(pin, value);

    // Send feedback to client

    client.print(F("Pin D"));

    client.print(pin);

    client.print(F(" set to analog "));

    client.println(value);

    String key = "D";

    key += pin;

    Bridge.put(key, String(value));

  }

  else {

    value = analogRead(pin);

    client.print(F("Pin A"));

    client.print(pin);

    client.print(F(" reads analog "));

    client.println(value);

    String key = "A";

    key += pin;

    Bridge.put(key, String(value));

  }
}
```

Create one more function to handle pin mode changes. Accept the YunClient as the argument, and create a local variable to hold the pin number. Read the pin value just as you did in the digital and analog functions.

```arduino
void modeCommand(YunClient client) {

  int pin;

  pin = client.parseInt();
```

Check to make sure the URL is valid

```arduino
if (client.read() != '/') {

    client.println(F("error"));

    return;

  }
```

If it's a valid URL, store the URL as a string. If the mode is an `input` or `output`, configure the pin and report it to client. If the string doesn't match those values, return an error.

```arduino
String mode = client.readStringUntil('\r');

  if (mode == "input") {

    pinMode(pin, INPUT);

    // Send feedback to client

    client.print(F("Pin D"));

    client.print(pin);

    client.print(F(" configured as INPUT!"));

    return;

  }

  if (mode == "output") {

    pinMode(pin, OUTPUT);

    // Send feedback to client

    client.print(F("Pin D"));

    client.print(pin);

    client.print(F(" configured as OUTPUT!"));

    return;

  }

  client.print(F("error: invalid mode "));

  client.print(mode);
}
```

The complete sketch is below :

```arduino

/*

  Arduino Yún Bridge example

  This example for the YunShield/Yún shows how

  to use the Bridge library to access the digital and

  analog pins on the board through REST calls.

  It demonstrates how you can create your own API when

  using REST style calls through the browser.

  Possible commands created in this shetch:

  "/arduino/digital/13"     -> digitalRead(13)

  "/arduino/digital/13/1"   -> digitalWrite(13, HIGH)

  "/arduino/analog/2/123"   -> analogWrite(2, 123)

  "/arduino/analog/2"       -> analogRead(2)

  "/arduino/mode/13/input"  -> pinMode(13, INPUT)

  "/arduino/mode/13/output" -> pinMode(13, OUTPUT)

  This example code is part of the public domain

  http://www.arduino.cc/en/Tutorial/Bridge

*/

#include <Bridge.h>
#include <BridgeServer.h>
#include <BridgeClient.h>

// Listen to the default port 5555, the Yún webserver
// will forward there all the HTTP requests you send

BridgeServer server;

void setup() {

  // Bridge startup

  pinMode(13, OUTPUT);

  digitalWrite(13, LOW);

  Bridge.begin();

  digitalWrite(13, HIGH);

  // Listen for incoming connection only from localhost

  // (no one from the external network could connect)

  server.listenOnLocalhost();

  server.begin();
}

void loop() {

  // Get clients coming from server

  BridgeClient client = server.accept();

  // There is a new client?

  if (client) {

    // Process request

    process(client);

    // Close connection and free resources.

    client.stop();

  }

  delay(50); // Poll every 50ms
}

void process(BridgeClient client) {

  // read the command

  String command = client.readStringUntil('/');

  // is "digital" command?

  if (command == "digital") {

    digitalCommand(client);

  }

  // is "analog" command?

  if (command == "analog") {

    analogCommand(client);

  }

  // is "mode" command?

  if (command == "mode") {

    modeCommand(client);

  }
}

void digitalCommand(BridgeClient client) {

  int pin, value;

  // Read pin number

  pin = client.parseInt();

  // If the next character is a '/' it means we have an URL

  // with a value like: "/digital/13/1"

  if (client.read() == '/') {

    value = client.parseInt();

    digitalWrite(pin, value);

  } else {

    value = digitalRead(pin);

  }

  // Send feedback to client

  client.print(F("Pin D"));

  client.print(pin);

  client.print(F(" set to "));

  client.println(value);

  // Update datastore key with the current pin value

  String key = "D";

  key += pin;

  Bridge.put(key, String(value));
}

void analogCommand(BridgeClient client) {

  int pin, value;

  // Read pin number

  pin = client.parseInt();

  // If the next character is a '/' it means we have an URL

  // with a value like: "/analog/5/120"

  if (client.read() == '/') {

    // Read value and execute command

    value = client.parseInt();

    analogWrite(pin, value);

    // Send feedback to client

    client.print(F("Pin D"));

    client.print(pin);

    client.print(F(" set to analog "));

    client.println(value);

    // Update datastore key with the current pin value

    String key = "D";

    key += pin;

    Bridge.put(key, String(value));

  } else {

    // Read analog pin

    value = analogRead(pin);

    // Send feedback to client

    client.print(F("Pin A"));

    client.print(pin);

    client.print(F(" reads analog "));

    client.println(value);

    // Update datastore key with the current pin value

    String key = "A";

    key += pin;

    Bridge.put(key, String(value));

  }
}

void modeCommand(BridgeClient client) {

  int pin;

  // Read pin number

  pin = client.parseInt();

  // If the next character is not a '/' we have a malformed URL

  if (client.read() != '/') {

    client.println(F("error"));

    return;

  }

  String mode = client.readStringUntil('\r');

  if (mode == "input") {

    pinMode(pin, INPUT);

    // Send feedback to client

    client.print(F("Pin D"));

    client.print(pin);

    client.print(F(" configured as INPUT!"));

    return;

  }

  if (mode == "output") {

    pinMode(pin, OUTPUT);

    // Send feedback to client

    client.print(F("Pin D"));

    client.print(pin);

    client.print(F(" configured as OUTPUT!"));

    return;

  }

  client.print(F("error: invalid mode "));

  client.print(mode);
}
```
