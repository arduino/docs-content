---
title: Getting Started with Arduino
description: 'An introduction to hardware, software tools, and the Arduino API.'
tags: [Arduino, API]
---

The Arduino platform has since its start in 2005, grown to become one of the most recognizable brands in the space of electronics and embedded design. 

But what are the cornerstones of Arduino? What is a "board", how do I write code to it, and what are the tools needed to create my own project? The goal with this guide is to provide you with an overview to the Arduino project.

***In this guide, you will find links to articles that goes more in depth on a specific topic.***

## Overview

This guide is divided into three main sections: **hardware**, **software tools**, and **Arduino API**. The sections just below summarizes the learning outcome of this article:

### Hardware

In this section, we will dedicate some time to learn about some fundamentals in electronics, and about a basic operation of an Arduino board.

- The anatomy of an Arduino board.
- The "basic" operation of an Arduino board.
- Fundamental knowledge of microcontrollers, electronic signals, communication protocols, memory management.
- Embedded sensors.
- Creating a circuit with external sensors and actuators.
- Internet of Things (IoT) and different radio modules & wireless protocols.

### Software IDE, Tools & Services

In this section you will how to set up your development environment as well as learning about what options there are.s

- How to set up your development environment.
- Learn about the Arduino IDEs (Integrated Development Environment).
- Learn about the Arduino Cloud Service.
- Intro to the Arduino CLI (Command Line Interface).

### The Arduino API

In this section you will learn what the Arduino API is, and how to create code that can run on your Arduino board.

- What is the "Arduino API".
- How is an Arduino program (sketch) structured.
- How do I upload code to an Arduino board?
- What is a "core/platform"?
- Core specific API.
- Quick reference to the Arduino API.

## Arduino Hardware

Over the years, Arduino has released hundreds of hardware designs in many shapes and forms. 

### Anatomy of an Arduino Board

While all Arduino boards differ from each other, there are several key components that can be found on practically any Arduino. Let's take a look at the image below:

![Key components of an Arduino board.]()

- **1.** Microcontroller - this is the brain of the Arduino, and is the component that we load programs into. Think of it as a very tiny computer, designed to execute a specific number of things.
- **2.** USB port - used to connect a USB cable from your computer.
- **3.** USB to serial chip - the USB to Serial is an important component, as it helps translate data that comes from e.g. a computer to the microcontroller. This is what makes it possible to program it from your computer.
- **4.** Digital pins - pins that uses digital logic (0,1 or LOW/HIGH). Commonly used for switches and to turn on an LED.
- **5.** Analog pins - pins that can read analog values in a 10 bit resolution (0-1023).
- **6.** 5V / 3.3V pins- these pins are used to power external components.
- **7.** GND - also known as `ground`, `negative` or simply `-`, is used to complete a circuit, where the electrical level is at 0 volt.

Generally speaking, all Arduino boards have the above components, but there are of course many more than meets the eye.

### Basic Operation

Most Arduino boards are designed to have a single program running on the microcontroller. This program can be designed to perform one single action, such as blinking an LED. It can also be designed to execute a hundred different actions in a cycle. The scope varies from program to program.

The program that is loaded to the microcontroller will start execution as soon as it is powered. Every program has a function called a "loop". Inside the loop, you can for example:

- Read a sensor.
- Turn on a light.
- Check whether a condition is met.
- All of the above.

The speed of a program is incredibly fast, unless we tell it to slow down. It depends on the size of the program and how long it takes for the microcontroller to execute it, but it is generally in **microseconds(or one millionth of a second)**.  

![The basic operation of an Arduino]()

### Sensors & Actuators





### Circuit Basics




### Electronic Signals

![Electronic signals.]()

All communication between any electronic components are done through **electronic signals.** There are two main types of electronic signals: **analog & digital**. 

### Analog Signal

![Basics of an analog signal.]()

An analog signal is generally bound to a range. In an Arduino, that range is typically 0-5V, or 0-3.3V. 

If we for example use a potentiometer (an analog component used to change the resistance of a circuit), we can adjust this range (0-5V). In the program, this is represented in a range of 0-1023, which is a 10-bit resolution. 

### Digital Signal

![Basics of a digital signal.]()

A digital signal works a bit different, and measures only if it is in a high, or low state (0 or 1). This is the most common signal type in modern technology. 

You can easily write and read digital signals on an Arduino, and is very useful to read button states, or to turn something on or off.

Digital signals might seem very basic (just 0 or 1 right), but are actually way more advanced. For example, we can create a sequence by sending a high or low state rapidly a number of times. This is known as a **binary sequence** or a **bitstream**.

Let's take a look at two binary sequences:

```
101101
101110001110011
```

Which in decimal format is:

```
45
23667
```

This is a clever way of sending large amounts of data from one point to the other, by rapidly turning ON or OFF something. This particular operation is quite complex, and this is just a basic explanation of how a digital signal works.

### Serial Communication Protocols

![Serial communication protocols.]()

There are several serial communication protocols that uses the aforementioned digital signals to send data. The most common are **UART, SPI & I²C**. The UART protocol is used to send data between a computer and Arduino board, such as uploading a new program, or reading data directly from an Arduino.

The SPI and I²C protocols are used for communication between both internal and external components. The communication is handled by something called a **serial bus**, which is attached to a specific pin on the Arduino. 

Using the I²C protocol, we can connect several sensors on the same pin, and retrieve the data accurately. A device an address that we need to specify, where we can request this device to send back data. 

### Memory

The "standard" Arduino typically has two memories: SRAM and Flash memory. 

The SRAM (Static Random-Access Memory) is used to for example store the value of a variable (such as the state of a boolean). When powered off, this memory resets.

The Flash memory is primarily used to store the main program, or the instructions for the microcontroller. This memory is not erased when powered off so that the instructions for the microcontroller are executed as soon as the board is powered.

![Memory types on an Arduino.]()

### Embedded Components

An **embedded component** is a tiny component that is found on your board. As electronics are getting smaller and smaller, more and more can be fitted to smaller circuit boards.

Many new Arduino boards have sensors embedded directly, making them very compact. For example, the [Nano BLE Sense]() has 7 embedded sensors, but is only **45x18mm** (the size of a thumb). These are all connected via the I²C protocol as mentioned above, and has a unique address.

![Embedded sensors.]()

### Internet of Things (IoT)

Most modern Arduino boards now come equipped with a radio module, designed to communicate wirelessly. There are several different ones: Wi-Fi, Bluetooth, LoRa, GSM, NB-IoT and more. Each are designed to communicate using the various technologies available on the market.

The most popular and inexpensive modules are the Wi-Fi & Bluetooth modules. The Wi-Fi modules allow your board to connect to routers, and to request and send data over the Internet. In a way, it works the same as your computer when requesting various types of data over the Internet, just in a smaller scale. 

Bluetooth is used to communicate with nearby devices, and is really useful for maintaining a fast and reliable connection. For example, in real-life applications, Bluetooth is used for wireless headphones & speakers.

Similarly to serial protocols, radio modules use their own set of protocols to communicate, such as HTTP, MQTT and UPD.

![Wireless communication]().

## Arduino API

***Visit the [Arduino Language Reference]() to explore the full Arduino API.***

The Arduino API, aka the "Arduino Programming Language", consists of several functions, variables and structures based on the C/C++ language. 

### Main Parts

The Arduino API can be divided into three main parts: **functions, variables** and **structure**:

- **Functions:** for controlling the Arduino board and performing computations. For example, to read or write a state to a digital pin, map a value or use serial communication.
- **Variables:** the Arduino constants, data types and conversions. E.g. `int`, `boolean`, `array`.
- **Structure:** the elements of the Arduino (C++) code, such as 
  - *sketch* (`loop()`, `setup()`)
  - *control structure* (`if`, `else`, `while`, `for`)
  - *arithmetic operators* (multiplication, addition, subtraction)
  - *comparison operators*, such as `==` (equal to), `!=` (not equal to), `>` (greater than).

The Arduino API can be described as a simplification of the C++ programming language, with a lot of additions for controlling the Arduino hardware. 

### Program Structure

The absolute minimum requirement of an Arduino program is the use of two functions: `void setup()` and `void loop()`. The "void" indicates that nothing is returned on execution.

- `void setup()` - this function executes only once, when the Arduino is powered on. Here we define things such as the mode of a pin (input or output), the baud rate of serial communication or the initialization of a library.
- `void loop()` - this is where we write the code that we want to execute over and over again, such as turning on/off a lamp based on an input, or to conduct a sensor reading every X second.

The above functions are **always** required in an Arduino sketch, but you are of course able to add several more functions, which is very useful for longer programs. 

### The "Sketch"

![The Arduino Sketch.]()

In the Arduino project, a program is referred to as a "Sketch". A sketch is basically just a file that you write your program inside. It has the `.ino` extension, and is always stored in a folder of the same name. 

The folder can include other files, such as a **header file**, that can be included in your sketch. 

### Example Sketch

Below is an example of a standard Arduino sketch, which contains some popular Arduino programming elements. 

```arduino
/* 
This is a comment at the top of a program, 
it will not be recognized as code. Very good 
to add an explanation of what your code does 
here.

This sketch shows how to read a value from a
sensor connected to pin A1, print it out in 
the Serial Monitor, and turn on an LED connected
to pin number 2 if a conditional is met.
*/

int sensorPin = A1; //define pin A1 (analog pin)
int ledPin = 2; //define pin 2 (digital pin)
int sensorValue; //create variable for storing readings

//void setup is for configurations on start up
void setup() { 
    Serial.begin(9600); //initialize serial communication
    pinMode(ledPin, OUTPUT); //define ledPin as an output
}

void loop() {
    sensorValue = analogRead(sensorPin); // do a sensor reading
    
    Serial.print("Sensor value is: "); //print a message to the serial monitor
    Serial.println(sensorValue); //print the value to the serial monitor
    
    //check if sensorValue is below 200
    if(sensorValue < 200) { 
        digitalWrite(ledPin, HIGH); //if it is, turn on the LED on pin 2.
    }
    //if sensorValue is above 200, turn off the LED
    else{ 
        digitalWrite(ledPin, LOW);
    }
}
```

### Libraries

Arduino libraries are an extension of the standard Arduino API, and consists of **thousands of libraries**, both official and contributed by the community.

Libraries simplifies the use of otherwise complex code, such as reading a specific sensor, controlling a motor or connecting to the Internet. Instead of having to write all of this code yourself, you can just install a library, include it at the top of your code, and use any of the available functionalities of it. All Arduino libraries are open source and free to use by **anyone.**

To use a library, you need to include it at the top of your code, as the example below:

```arduino
#include <Library.h>
```

***You can browse through all official and contributed libraries in the [Arduino Libraries page]().***

### Core Specific API

Every Arduino board requires a "core", or "package", that needs to be installed in order to program it. All packages contain the standard Arduino API, but also a specific API that can only be used with specific boards. 

For example, the classic [ArduinoCore-avr](https://github.com/arduino/ArduinoCore-avr) package, automatically includes the [EEPROM](/learn/built-in-libraries/eeprom), and [SoftwareSerial](/learn/built-in-libraries/software-serial) libraries, and can be used freely without any additional installation. In this package you will find the classic Arduino UNO, Nano, Mega2560 and more.

Another example is the [ArduinoCore-mbed]() package, which includes over 40 libraries, designed for specific board features, such as:

- **PDM** - used for sampling Audio from microphones onboard the Nano BLE Sense and Nano RP2040 Connect boards.
- **Ethernet** - for using the Ethernet functionalities of the Portenta Vision Shield.
- **GSM** - to access GSM functionalities on the Portenta Cat. M1/NB IoT GNSS Shield.

These features are documented in the **documentation landing page** of each product. A list of all hardware can be found at [docs.arduino.cc](/).

## Arduino Software Tools

***The Arduino IDEs are available for download for free in the [Software downloads page]().***

Now that we have a bit of background on Arduino hardware, let us move on to another fundamental: the Arduino Software tools.

The Arduino IDE, as it is commonly referred to, is an **integrated development environment.** But what does that mean exactly?

In order to program your board, you need to write a program, compile that program into machine code, and finally: send over the new program to your board.

The Arduino IDE facilitates all this, from the first line of code written, to have it executed on the Arduino board's microcontroller. It is a program, or application, that you can download (or use an online version), to manage all of your code development. Back in the day, this was a complicated process, that required a good set of knowledge in electronics & computer science. Now, **anyone** can learn how to do it, with the help of the Arduino IDE.

Today, there are three Arduino IDEs available:

- Arduino IDE 1.8.x (classic)
- Arduino IDE 2.0.x (new)
- Arduino Web Editor (online)

### A Typical Workflow

To upload code to an Arduino board using the IDE, one typically does the following:

**1. Install your board** - this means installing the right "package" for your board. Without the package, you can simply not use your board. Installing is done directly in the IDE, and is a quick and easy operation.

**2. Create a new sketch** - a sketch is your main program file. Here we write a set of instructions we want to execute on the microcontroller.

**3. Compile your sketch** - the code we write is not exactly how it looks like when uploaded to our Arduino: compiling code means that we check it for errors, and convert it into a binary file (1s and 0s). If something fails, you will get this in the error console.

**4. Upload your sketch** - once the compilation is successful, the code can be uploaded to your board. In this step, we connect the board to the computer physically, and select the right serial port. 

**5. Serial Monitor (optional)** - for most Arduino projects, it is important to know what's going on on your board. The Serial Monitor tool available in all IDEs allow for data to be sent from your board to your computer. 

### Arduino IDE 1.8.x

![The classic Arduino IDE.]()

For what is now considered the "legacy" editor, the Arduino IDE 1.8.X, or "Java IDE", is the editor that was first released back when Arduino started.

***Learn more by visiting the [Arduino IDE 1 documentation]().***

### Arduino IDE 2.0.x

![The new Arduino IDE.]()

In 2021, the Arduino IDE 2.0 was released. The new IDE has the same functionality, but also supports features such as auto-completion and debugging. 

***Learn more by visiting the [Arduino IDE 2 documentation]().***

### Web Editor (Arduino Cloud)

![The Web Editor.]()

The Web Editor is an online IDE, part of the Arduino Cloud suite. Similar in function, this editor is completely web based, with online storage among other features.

***Learn more by visiting the [Web Editor documentation]().***

### Library Manager

![The Library Manager.]()

Every version of the IDE has a library manager for installing Arduino software libraries. Thousands of libraries, both official and contributed libraries, are available for direct download. Code examples for each library is made available on download.

We will go through what a library is and how to use them, further down in the [Arduino API section]() of this article.

### Arduino CLI

![The CLI (Command Line Interface).]()

The Arduino CLI is a command line tool that can be used to compile and upload code to your board. It has no visual UI, but is very useful for automation. It is designed for more advanced users.

A proper use of the CLI can speed up your development time by far, as any operation is executed much faster than in the regular IDE.


## Quick Reference

In this section, you will find a list of some of the most common elements in the standard Arduino API. This will help you get familiar with some key building blocks.

To explore the whole Arduino API, please refer to the [Arduino Language Reference](), which is an in-depth wiki maintained by Arduino and its community.


### General

#### `setup()`

The `setup()` function is where you can make program configurations.

```arduino
void setup() {
    //program configurations here
}
```

#### `loop()`

The `loop()` function is where your main program is stored. It will run as long as your board is powered.

```arduino
void loop() {
    //main program here
}
```

#### `delay(time)`

The `delay()` function pauses the program for a set number of milliseconds.

The classic blink sequence is found in the snippet below:

```arduino
void loop() {

digitalWrite(LED, HIGH); //turn on an LED
delay(1000); //as program is paused, with the LED on
digitalWrite(LED, LOW); //program is unpaused, and the LED is turned off
delay(1000); //program is paused, with the LED off

}
```

The `delay()` function is an incredibly useful function, and you will find it in almost all examples. But, for efficiency of the code, it is not the best option, as it prevents the Arduino from doing anything for the duration of the delay.

For this, we can use the `millis()` function.

#### `millis()`

The `millis()` function is a bit more advanced, but an incredibly resourceful function. It allows you to have multiple events happening simultaneously, without pausing the program. This is done by measuring time (in milliseconds) passed since the program started.

Then, with the use of **intervals** and continously storing the **time for last event**, a simple algorithm can be made to have events happening at specific times without pausing the program.

See the example below:

```arduino
unsigned long previousMillis_1 = 0; //store time for first event
unsigned long previousMillis_2 = 0; //store time for second event

const long interval_1 = 1000; //interval for first event
const long interval_2 = 2000; //interval for second event


void setup(){

}

void loop() {

//check time since program started, and store in "currentMillis"
unsigned long currentMillis = millis();

//conditional that checks whether 1 second has passed since last event
if (currentMillis - previousMillis_1 >= interval_1) {
    //execute a piece of code, every *1 second*
}

//conditional that checks whether 2 seconds have passed since last event
if (currentMillis - previousMillis_2 >= interval_2) {
    //execute a piece of code, every *2 seconds*
}

}
```

While the `millis()` function is a more advanced concept than the `delay()` function, it is a good to start practicing it early on.

#### Functions

You can create custom functions that either just executes code and returns to the program, or that returns a result.

Example of a `void` function that does not return:

```arduino
int x;

void loop(){
    thisFunction(); //execute the function
}

void thisFunction() {
    x = x++; //increase x by 1 each time function is run.
}
```

Example of a type `int` function that returns a value.

```arduino

int value;

void setup(){

}

void loop(){
    value = returnFunction();
}

int returnFunction() {
    int returnValue = 5 + 2;
    return returnValue;
}
```

#### Variable Definition

Variables can either be created **locally** or **globally**. Variables that are defined in the `loop()` are considered local, and variables defined at the top of your sketch are considered global. 

```arduino
int sensorReading = x; //global variable

void setup(){

}

void loop(){
    int sensorReading = x; //local variable
}
```

#### Data Types

There are several data types available for use, and below are some of the most common:

```
bool 
byte
char
double
float
int
long
short
String()
```

To store data in for example an `int` (integer):

```arduino
int exampleNumber = 25;
```

For numbers with a lot of decimals, we can use `float`:

```arduino
float exampleNumber = 22.2123002;
```

Or to store a string, we can use the `String` function:

```arduino
String exampleSentence = "This is a string!";
```

For simple switches and true/false, we use booleans:

```arduino
bool exampleSwitch = true/false;
```

***You can read more about this in the [variables & data types](https://www.arduino.cc/reference/en/#variables) in the Arduino Language Reference.***

### Serial Communication

Serial communication is **essential** to Arduino programming, as it is the easiest way to know what goes on on your board.

For this, we can use the `Serial` class.

#### `Serial.begin()`

Initializes serial communication between board & computer. This is defined in the `void setup()` function, where you also specify baud rate (speed of communication).

```arduino
void setup() {
    Serial.begin(9600);
}
```

#### `Serial.print()`

Prints data to the serial port, which can be viewed in the Arduino IDE **Serial Monitor** tool.

```arduino
void loop() {
    Serial.print();
}
```

#### `Serial.available()`

#### `Serial.read()`

### GPIO / Pin Management

Configuring, controlling and reading the state of a digital/analog pin on an Arduino.

#### `pinMode()`

Configures a digital pin to behave as an input or output. Is configured inside the `void setup()` function.

```arduino
pinMode(pin, INPUT); //configures pin as an input
pinMode(pin, OUTPUT); //configures pin as an output
pinMode(pin, INPUT_PULLUP); //enables the internal pull-up resistor
```

***You can read more about digital pins in the article about [Digital Pins](/learn/microcontrollers/digital-pins).***

#### `digitalRead()`

Reads the state of a digital pin. Used to for example detect a button click.

```arduino
int state = digitalRead(pin); //store the state in the "state" variable
```

#### `digitalWrite()`

Writes a high or low state to a digital pin. Used to switch on or off a component.

```arduino
digitalWrite(pin, HIGH); // writes a high (1) state to a pin (aka turn it on)
digitalWrite(pin, LOW); // writes a low (0) state to a pin (aka turn it off)
```

#### `analogRead()`

Reads the voltage of an analog pin, and returns a value between 0-1023 (10-bit resolution). Used to read analog components.

```arduino
sensorValue = analogRead(A1); //stores reading of A1 in "sensorValue" variable
```

#### `analogWrite()`

Writes a value between 0-255 (8-bit resolution). Used for dimming lights or setting the speed of a motor. Also referred to as **PWM**, or Pulse Width Modulation. 

```arduino
analogWrite(pin, value); //write a range between 0-255 to a specific pin
```

PWM is only available on specific pins (marked with a "~" symbol).

### Structure

The structure of the Arduino API is based on C++, and can be considered the building blocks of a program. 

#### Conditionals

Conditionals are some of the most popular used elements in any program. In Arduino, a typical conditional consists of an `if` and `else` statement.

```arduino
if(variable == true){
    //do something
}
else {
    //do something else
}
```

You can make use of several if/else statements in your code.

#### Loops / Iterations

The `for` and `while` loops are commonly used in programs, to execute a block of code *for* a set number of times, or *while* a condition is met.

A basic use of a `while` loop to execute a block of code while `variable` is true.

```arduino
while (variable == true) {
    //do something
}
```

A basic use of a `for` loop is to execute a block of code a number of times (in this case, 10).

```arduino
  for (int x = 0; x <= 10; x++) {
      //do something 10 times
  }
```

To break out of a loop, you can use `break`. In the snippet below, if a condition is met (variable is true), we break out of the loop.

```arduino
  for (int x = 0; x <= 10; x++) {
      if(variable == true) {
          break;
      }
  }
```

#### Arithmetic Operators

Arithmetic operators are used for addition, subtraction, multiplication, division and other mathematical calculations.

```arduino
int x = 5;
int y = 2;

x + y; //result is 7
x * y; //result is 10
x - y; //result is 3
```

#### Comparison Operators

Comparison operators are used for comparing one property to another, and are a key component of a conditional statement.

There are several comparison operators:

```arduino
!= //not equal to
< //less than
<= //less than or equal to
== //equal to
> //greater than
>= //greater than or equal to
```

To use them in a conditional, see the following example:

```arduino
if(value > 10) {
    //do something
}
```

#### Boolean Operators

Boolean operators (logical not `!`, and `&&`, or `||`) can for example be used for more advanced conditionals.

To use the and `&&` operator:

```arduino
if(value > 10 && otherValue > 10){
    //do something if only if *both* conditions are met
}
```

To use the or `||` operator:

```arduino
if(value > 10 || otherValue > 10){
    //do something if a one *or* the other condition is met
}
```

To use the not `!` operator:

if(!value){
    //do something if value is false (!)
}

#### Compund Operators

Compound operators consists of **two operators**, which are used to perform two operations in the same statement. This can for example be to add `+` and assign `=` a value at the same time.

Here are some examples:

```arduino
x = 5;
y = 2;

xx++; //increase by one, so x is now 6
xx--; //decrease by one, so x is now 4

x += y; //x is now 7 (add and assign)
x -= y; //x is now 3 (subtract and assign)
x *= y; //x is now 10 (multiply and assign)
```


