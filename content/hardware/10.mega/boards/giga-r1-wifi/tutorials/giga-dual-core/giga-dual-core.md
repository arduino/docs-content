---
title: Guide to GIGA R1 Dual Cores
description: Learn how to access and control the M4 and M7 cores on the GIGA R1, and how to communicate between them using RPC.
author: Karl Söderby
tags: [Dual Core, M4, M7]
---

The GIGA R1's [STM32H747XI](static/resources/datasheets/stm32h747xi.pdf) has two cores, the M4 and the M7. Each core can be programmed individually, with M7 acting as the main processor, and the M4 as a co-processor.

The M7 is referred to as the main processor due its superior hardware features, as well as it is required to run to boot the M4 core (you boot the M4 from within the M7). 

These two cores can run applications in parallel, for example, running a servo motor on one core, and a display on another, without blocking each other. In a single core, such operations would slow down the program, resulting in lesser performance.

The M4 and M7 cores are programmed with separate sketches, using the same serial port. In the Arduino IDE, you can select the core you want to program, and then upload the sketch you want to run on that specific core. 

## Goals

In this guide you will discover:
- How to configure and program the M4/M7 cores and conventional approaches to do so.
- How to boot the M4 core.
- How to communicate between the cores via Remote Call Procedures (RPC).
- Useful examples based on the dual core & RPC features.
- The `RPC` library API.

## Hardware & Software Needed

- [GIGA R1 WiFi](/hardware/giga-r1-wifi)
- [Arduino IDE](https://www.arduino.cc/en/software)
- Arduino GIGA Core installed.\*

***\*For instructions on how to install the GIGA Core, follow the [Getting Started with GIGA R1 guide](/tutorials/giga-r1-wifi/giga-getting-started).***

## Programming M4/M7

Programming the cores is done via the Arduino IDE, in a special interface that appears only when you **select the Arduino GIGA R1 board** from the board menu. 

### Partitioning The Flash Memory

To allocate memory for the M4, the flash memory can be partitioned. This is done by navigating to **Tools > Flash Split** in the IDE.

![Flash partitioning in the IDE.](assets/flash-split.png)

- **2MB M7 + M4 in SDRAM (default)** - this option is the default configuration, which is for programming the M7 only. This allocates no memory to the M4.
- **1.5MB M7 + 0.5MB M4** - useful when larger amount of memory is required on the M7.
- **1MB M7 + 1MB M4** - useful when you need to balance the memory equally between the M4 and M7 cores.

***It is required to use option 2 or 3 if you intend to program the M4 via the IDE, as the default option provides no memory allocation for the M4.***

### Target Core

To select the core you want to program, navigate to **Tools > Target Core** in the IDE. 

![Flash partitioning in the IDE.](assets/target-core.png)

Here you can choose between:
- **Main Core** - this is the M7 core, the main processor on the board.
- **M4 Co-processor** - this is the M4 core, the co-processor on the board.

### Uploading 

As both cores share the same serial port, choosing the **Flash Split** + **Target Core** is required so that the program is uploaded to the correct core.

Uploading is no different than to any other Arduino board: simply click the upload button and wait for it to finish. 

### Booting M4 Core

The M4 core does not boot by itself as it requires interaction from the M7 core. This boot function is built into the `RPC` library, and needs to be included in the sketch uploaded to the M7:

```arduino
#include <RPC.h>

void setup() {
  RPC.begin(); //boots M4
}
void loop(){
}
```

Once the M4 is booted from the M7, both cores will run in parallel, much like two Arduinos sharing the same board.

### Writing Over Existing Sketch

Uploading new sketches works the same as a typical upload procedure. The new sketch will overwrite the current sketch running on the core you upload to.

## Limitations

The M7 and M4 cores are two separate cores, and when initialized, they will continue to execute their corresponding program.

In this section you will find some known limitations of using the two parallel cores. 

### Booting M4

As mentioned in the previous section, the M4 requires to be booted from the M7, by using the `RPC.begin()` method. If this is not included, the M4 will not boot.

### Serial Communication

Serial communication is not available by default on the M4 core. A work around for this is by sending data using the `RPC` library, and printing it from the M7 core. To achieve this, see the following examples:

**M4 Sketch**

```arduino
#include <RPC.h>

void setup() {
  RPC.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  RPC.println("Hello World!");
}
```

**M7 Sketch**

```arduino
#include <RPC.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  RPC.begin();
}

void loop() {
  String buffer = "";
    while (RPC.available()) {
      buffer += (char)RPC.read();
    }

    if (buffer.length() > 0) {
      Serial.print(buffer);
    }
}
```

***Note that both of these sketches needs to be uploaded to their corresponding cores.***

## Methods of Programming

Programming the M4 and M7 cores is straightforward, but can be complicated to track. Having a strategy for how you want to build your dual core applications is key. 

In this section we introduce the "single" and "multiple" sketch approach, and the pros and cons of each method.

### Single Sketch Approach

The single sketch approach means writing a single sketch that is **uploaded to both cores** each time a change is made. In the sketch, we can keep track of what each core does by using simply by querying the core used with a simple function:

```arduino
String currentCPU() {
  if (HAL_GetCurrentCPUID() == CM7_CPUID) {
    return "M7";
  } else {
    return "M4";
  }
}
```

With this function, we check whether the M4 or M7 is running, and we can write code for each of the core like this:

```arduino
  if (currentCPU() == "M4") {
    //run M4 code
  }

  if (currentCPU() == "M7") {
    //run M7 code
  }
```

The pros of using this approach is that you can write all code in a single file, therefore, revisioning code, as well as the provisioning is easier to manage.

The cons of using this approach is that you will run out of program memory faster. You will also upload code to the cores that will never execute (the M7 code will not execute on M4 and vice versa).

### Multiple Sketch Approach

The multiple sketch approach means developing two separate sketches, one for each core. This does not require the use of the `HAL_GetCurrentCPUID()` to retrieve the core you are using, you can instead just write sketches as you would normally do.

The pros of using this approach is that the code you write is optimized only for one core, and this saves a lot of program memory.

The cons is to manage the versions becomes harder, and while flashing the board, you'd need to keep track on which version is uploaded to which core. It is easier to upload to the wrong core by accident using this approach, but you have more optimized code.

When writing multiple sketches, there are some things to consider to make your development experience easier:
- Name your sketches with either `_M4` or `_M7` suffix or prefix. This will make it easier if the code is intended to be shared with others.
- Consider having a starting sequence (e.g. the blue LED blinking 3 times), whenever a core is initialized.
- Always include `RPC.begin()` on your M7 core sketch.
- 

## Remote Call Procedures (RPC)

RPC is a method that allows programs to make requests to programs located elsewhere. It is based on the client-server model (also referred to as caller/callee), where the client makes a request to the server. 

An RPC is a synchronous operation, and while a request is being made from the caller to another system, the operation is suspended. On return of the results, the operation is resumed. 

The server side then performs the subroutine on request, and suspends any other operation as well. After it sends the result to the client, it resumes its operation, while waiting for another request.

![Request routine.](assets/rpc-basics.png)

### RPCs in the Arduino Environment

At the moment, only a limited amount of boards supports RPC, as in this context, it is designed to be a communication line between **two cores.** The GIGA R1 is one of them.

What makes this implementation possible is the `RPC` library ([see API section](#rpc-library-api)), which utilises the [rpclib](https://github.com/rpclib/rpclib) C++ library as well as functions from the [Stream](https://www.arduino.cc/reference/en/language/functions/communication/stream/) class.

The library makes it possible to set up either of the M4/M7 cores as a server/client, where remote calls can be made between them. This is done by "binding" a function to a name on the server side, and calling that function from the client side. 

On the server side, it could look like this:

```arduino
//server side, for example M7
int addFunction(int a, int b){ 
  return a + b;
}

RPC.bind("addFunction", addFunction);
```

On the client side, it could look like this:

```arduino
int x,y = 10;

RPC.call("addFunction", x, y);
```

When `call()` is used, a request is sent, it is processed on the server side, and returned. The `x` and `y` variables are used as arguments, and the result returned should be 20 (10+10).

![Communication between M7 and M4 core.](assets/rpc-m7-m4.png)

## RPC Examples

In this section, you will find a series of examples that is based on the `RPC` library. 

### RPC Serial

The `Serial.print()` command only works on the **M7 core**. In order to print values on the **M4**, we need to:
- Use `RPC.println()` on the M4. This will print the values to the RPC1 stream.
- Use `RPC.available()` and `RPC.read()`.

**M4 Sketch:**

```arduino
#include <RPC.h>

void setup() {
RPC.begin();
}

void loop() {
RPC.println("Printed from M4 core");
delay(1000);
}
```

**M7 Sketch:**

```arduino
#include <RPC.h>

void setup() {
Serial.begin(9600);
RPC.begin();
}

void loop() {
  String buffer = "";
  while (RPC.available()) {
    buffer += (char)RPC.read();  // Fill the buffer with characters
  }
  if (buffer.length() > 0) {
    Serial.print(buffer);
  }
}
```

### RPC Sensor

This example demonstrates how to request a sensor reading from one core to the other, using:
- M4 as a client.
- M7 as a server.

**M4 Sketch:**

```arduino
#include "Arduino.h"
#include "RPC.h"

using namespace rtos;

Thread sensorThread;

void setup() {
  RPC.begin();
  Serial.begin(115200);

  /*
  Starts a new thread that loops the requestReading() function
  */
  sensorThread.start(requestReading);
}

void loop() {
}

/*
This thread calls the sensorThread() function remotely
every second. Result is printed to the RPC1 stream.
*/
void requestReading() {
  while (true) {
    delay(1000);
    auto result = RPC.call("sensorRead").as<int>();
    RPC.println("Result is " + String(result));
  }
}
```

**M7 Sketch:**

```arduino
#include "Arduino.h"
#include "RPC.h"

void setup() {
  RPC.begin();
  Serial.begin(115200);

  //Bind the sensorRead() function on the M7
  RPC.bind("sensorRead", sensorRead);
}

void loop() {
  // On M7, let's print everything that is received over the RPC1 stream interface
  // Buffer it, otherwise all characters will be interleaved by other prints
  String buffer = "";
  while (RPC.available()) {
    buffer += (char)RPC.read();  // Fill the buffer with characters
  }
  if (buffer.length() > 0) {
    Serial.print(buffer);
  }
}

/*
Function on the M7 that returns an analog reading (A0)
*/
int sensorRead() {
  int result = analogRead(A0);
  return result;
}
```

### RPC Servo Motor

This example demonstrates how to request a servo motor on another core to move to a specific angle, using:
- M4 as a client.
- M7 as a server.

Each example is written as a **single sketch** intended to be uploaded to **both cores**.

**M4 sketch:**

```arduino
#include "Arduino.h"
#include "RPC.h"

using namespace rtos;

Thread servoThread;

void setup() {
  RPC.begin();
  Serial.begin(115200);

  /*
  Starts a new thread that loops the requestServoMove() function
  */
  servoThread.start(requestServoMove);
}

void loop() {
}

/*
This thread calls the servoMove() function remotely
every second, passing the angle variable (0-180).
*/
void requestServoMove() {
  while (true) {
    //Read a pot meter
    int rawAnalog = analogRead(A0);

    //Map value to 180
    int angle = map(rawAnalog, 0, 1023, 0, 180);

    delay(1000);
    auto result = RPC.call("servoMove", angle).as<int>();
    RPC.println("Servo angle is: " + String(result));
  }
}
```

**M7 sketch:**

```arduino
#include "Arduino.h"
#include "RPC.h"
#include <Servo.h>

Servo myservo;

void setup() {
  RPC.begin();
  Servo.attach(5); //attach servo to pin 5

  Serial.begin(115200);

  //Bind the servoMove() function on the M7
  RPC.bind("servoMove", servoMove);
}

void loop() {
  // On M7, let's print everything that is received over the RPC1 stream interface
  // Buffer it, otherwise all characters will be interleaved by other prints
  String buffer = "";
  while (RPC.available()) {
    buffer += (char)RPC.read();  // Fill the buffer with characters
  }
  if (buffer.length() > 0) {
    Serial.print(buffer);
  }
}

/*
Function on the M7 that returns an analog reading (A0)
*/
int servoMove(int angle) {
  servo.write(angle);
  delay(10);
  return angle;
  /*
  After the operation is done, return angle to the client.
  The value passed to this function does not change, but this
  verifies it has been passed correctly.
  */
}
```

## RPC Library API

The `RPC` library is based on the [rpclib](https://github.com/rpclib/rpclib) C++ library which provides a client and server implementation. In addition, it provides a method for communication between the M4 and M7 cores. 

This library is included in the GIGA core, so it is automatically installed with the core. To use this library, you need to include `RPC.h`:

```arduino
#include <RPC.h>
```

### `begin()`

#### Description

Initializes the library. This function also boots the M4 core.

#### Syntax 

```arduino
RPC.begin()
```

#### Returns

- `1` on success.
- `0` on failure.

### `bind()`

Used on the server side to bind a name to a function, and makes it possible for remotely calling it from another system.

#### Syntax

```arduino
RPC.bind("this_function", thisfunction)
```

#### Parameters

- `"name_of_func"` - name given for the function to be called from the client side.
- `name_of_func` - name of the function on the server side.

#### Returns

- None.

### `call()`

Used on the client side to call a function with optional parameters.

```arduino
RPC.call("this_function", int args)
```

#### Parameters

- `"name_of_func"` - the name of the function declared on the server side.
- `args` - arguments to be passed to the function.

#### Returns

- Result of the function if arguments are passed.

## RPC Serial API

The RPC Serial methods are also included in the `RPC` library, and uses methods from the [Stream](https://www.arduino.cc/reference/en/language/functions/communication/stream/) base class, and is similar to the [Serial](https://www.arduino.cc/reference/en/language/functions/communication/serial/) class.

As the `Serial` class is only available on the M7 core, the M4 core uses `RPC` library to print data, where the M7 can read the data and print it to a computer.

### `println()`

Prints data to a serial port. This is used on the M4 core to send data to the M7.

#### Syntax

```
RPC.println(val);
```

#### Parameters

- The value to print. Can be any data type, but not multiple (e.g. string + integer in the same call).

#### Returns

- Number of bytes used. E.g. printing ("hello") returns 7. As hello (5) + new line (2) = 7. 

### `available()`

Get the number of available bytes to read from the M4.

#### Syntax

```arduino
RPC.available();
```

#### Paramaters

- None.

#### Returns

- The number of bytes available to read.
- `-1` if there is none.

### `read()`

Reads the first available byte from the M4.

#### Syntax

```arduino
RPC.read();
```

#### Paramaters

- None.

#### Returns

- The first available byte from the M4.
- `-1` if there is none.