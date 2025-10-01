---
tags: [Yún]
author: Arduino
title: 'Arduino Yún Process'
description: 'Demonstrates how to use Process to run Linux commands.'
---

This example for a Yún device shows how to use the Bridge library's Process class to run Linux processes on the AR9331. Specifically, in this example, you'll be using `curl` and `cat` to transfer data from a web server and get information on the Linux processor.

## Hardware Required

- Yún board or shield

- a network connection to the internet

There is no circuit for this example.

![The circuit for this tutorial.](assets/Yun_Fritzing.png)

image developed using [Fritzing](http://www.fritzing.org). For more circuit examples, see the [Fritzing project page](http://fritzing.org/projects/)

## Code

Include the Process class in your sketch.
`#include <Process.h>`

In `setup()`, you'll want to initialize Bridge and start a serial connection. Before running the rest of `setup()` wait for a serial connection to become active.

```arduino
void setup() {

  Bridge.begin();

  Serial.begin(9600);

  while (!Serial);
```

The rest of `setup()` is used to call your two custom functions, `runCurl()` and `runCpuInfo()`. There's nothing in `loop()`.

```arduino
runCurl();

  runCpuInfo();
}

void loop() {

  // Do nothing here.
}
```

`runCurl()` will launch the `curl` command and download the Arduino logo as ASCII. Create a named Process and start it by calling `myProcess.begin("curl");`. Add the URL to retrieve with the `addParameter()` method, and run it all with `run()`.

```arduino
void runCurl() {

  Process p;

  p.begin("curl");

  p.addParameter("http://arduino.tips/asciilogo.txt");

  p.run();
```

When there is data available from the process, print it out to the serial monitor :

```arduino
while (p.available()>0) {

    char c = p.read();

    Serial.print(c);

  }

  Serial.flush();
}
```

For the `runCpuInfo()` function, you'll create a new process for `cat`. Add the parameter to `cat` passing it the path to the cpu Info file, then run the process.

```arduino
void runCpuInfo() {

  Process p;

  p.begin("cat");

  p.addParameter("/proc/cpuinfo");

  p.run();
```

When there is data available from the process, print it out to the serial monitor :

```arduino
while (p.available()>0) {

    char c = p.read();

    Serial.print(c);

  }

  Serial.flush();
}
```

The full code is below :

```arduino

/*

  Running process using Process class.

 This sketch demonstrate how to run linux processes

 using a YunShield/Yún

 created 5 Jun 2013

 by Cristian Maglie

 This example code is in the public domain.

 http://www.arduino.cc/en/Tutorial/Process

 */

#include <Process.h>

void setup() {

  // Initialize Bridge

  Bridge.begin();

  // Initialize Serial

  SerialUSB.begin(9600);

  // Wait until a Serial Monitor is connected.

  while (!SerialUSB);

  // run various example processes

  runCurl();

  runCpuInfo();
}

void loop() {

  // Do nothing here.
}

void runCurl() {

  // Launch "curl" command and get Arduino ascii art logo from the network

  // curl is command line program for transferring data using different internet protocols

  Process p;        // Create a process and call it "p"

  p.begin("curl");  // Process that launch the "curl" command

  p.addParameter("http://arduino.tips/asciilogo.txt"); // Add the URL parameter to "curl"

  p.run();      // Run the process and wait for its termination

  // Print arduino logo over the Serial

  // A process output can be read with the stream methods

  while (p.available() > 0) {

    char c = p.read();

    SerialUSB.print(c);

  }

  // Ensure the last bit of data is sent.

  SerialUSB.flush();
}

void runCpuInfo() {

  // Launch "cat /proc/cpuinfo" command (shows info on Atheros CPU)

  // cat is a command line utility that shows the content of a file

  Process p;        // Create a process and call it "p"

  p.begin("cat");   // Process that launch the "cat" command

  p.addParameter("/proc/cpuinfo"); // Add the cpuifo file path as parameter to cut

  p.run();      // Run the process and wait for its termination

  // Print command output on the SerialUSB.

  // A process output can be read with the stream methods

  while (p.available() > 0) {

    char c = p.read();

    SerialUSB.print(c);

  }

  // Ensure the last bit of data is sent.

  SerialUSB.flush();
}
```


**Last revision 2016/05/25 by SM**
