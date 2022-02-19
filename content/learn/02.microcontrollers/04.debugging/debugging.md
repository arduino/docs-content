---
title: 'Debugging Fundamentals'
description: 'Learn the basics of debugging microcontroller-based systems.'
tags: 
  - Debugging
  - Embedded systems
author: 'José Bagur, Taddy Chung'
---

**Embedded systems** are microprocessor or microcontroller-based systems with a dedicated operational role. Rather than being made of separate components, like desktop computers, laptops or, gaming consoles, embedded systems integrate all the hardware and software necessary for a particular purpose. Nowadays, embedded systems are everywhere: automobiles, cameras, household appliances, and mobile devices are just some examples.

Embedded systems design can be challenging since it combines hardware design, firmware, and software development, all in one particular device or product. In order to produce high-quality embedded firmware and software for a particular device or product, **debugging** is a necessary step in their development process. **Debugging is the process of confirming that, one by one, many things that we believe to be true and functional in our code are true**. We find a "**bug**" in our code when one our more assumptions are not valid. 

***People worldwide have been talking about "bugs" for a long time; even [Thomas Alva Edison](https://spectrum.ieee.org/did-you-know-edison-coined-the-term-bug) used the word back in his days. The word bug has been used as an old term for "monster"; like gremlins in machinery, bugs are malicious.***

The following article will discuss different debugging tools and techniques used to find bugs in microcontroller-based systems, especially those based on Arduino® hardware.  

## Debugging tools and techniques

There are some basic debugging techniques that we can implement to validate our code:

* The compiler and syntax errors.
* Traditional techniques: trace code and GPIOs.
* Remote debuggers.
* Simulators.
* In-Circuit Emulators and In-Circuit Debuggers.
* Hardware tools: oscilloscopes, logic analyzers and software-defined radios. 

Let us take a look into each one of the debugging tools and techniques.

### The Compiler and Syntax Errors

**Compiling** is transforming high-level code into machine language that can be understood by a processor, for example a microcontroller. In this process, the compiler also helps to identify **syntax errors**. Syntax errors indicate something wrong with the program's syntax; for example, **when a semi-colon is omitted at the end of a statement in a program**, the compiler generates a syntax error. Using the compiler for debugging this type of errors can be sometimes tricky; let us analyze two commonly encountered situations: 

* **The compiler shows 100 errors**: This usually does not mean there are 100 errors; it often gets thrown off track for a while when the compiler finds an error. The compiler tries to recover and pick up again after the first error, but sometimes it reports false errors. **Only the first error message is genuinely reliable**; try to fix one error at a time and then recompile the program.
* **Getting weird compiler messages**: Compiler errors are shown in terse jargon, sometimes hard to read and understand, but with hidden and valuable information. **Read the error message carefully**; it will always tell where, inside the program, the error occurred.

### Traditional Techniques: Trace Code and GPIO's

Adding **trace code** is probably the simplest and most basic debugging technique used in embedded systems design. This method adds trace code to the program to print out messages or values of variables (using `Serial.print()` function, for example) as the program executes. For example, determining if a particular function is halting or freezing in our code can be made with trace code as shown in the example code below:

```arduino
// Print a message if the execution gets here
Serial.println("Code got here");

// Try to execute myFunction1()
myFunction1(); 

// Print a message if the execution gets here
Serial.println("Code got here, myFunction1 executed"); 

// Try to execute myFunction2()
myFunction2(); 

// Print a message if the execution gets here
Serial.println("Code got here, myFunction2 executed"); 
```

Using trace code for debugging is usually applicable only during the early stages of an embedded system code development. **Adding trace code to our programs takes a significant amount of processing time and resources**. Therefore, it can easily disrupt critical timing tasks in our programs. Additionally, if we use the UART for other tasks, we can have problems displaying trace code. 

***You can pass flash-memory based strings to `Serial.print()` instruction by wrapping them with `F()`.***

Another trace code technique consists of **dumping strategic information into an array at run time**, we can then observe the contents of the array at a later time (for example, when the program terminates); this technique is also known as **dump into array**. Assume `good` and `bad` are two strategic variables we want to capture. The first step is to define a debug buffer in RAM to save the debugging measurements as shown in the code below:

```arduino
#define DUMP_BUFFER_SIZE 32
unsigned char GoodBuffer[DUMP_BUFFER_SIZE 32];
Unsigned char BadBuffer[DUMP_BUFFER_SIZE 32];
unsigned long Count = 0;
```

`Count` is used to index into the debug buffer, it must be initialized to zero before the debugging process begins. The code shown below dumps strategic information from the `good` and `bad` variables into the debug buffer: 

```arduino
void Save_Debug_Buffer(void) {
  if (Count < DUMP_BUFFER_SIZE) {
    GoodBuffer[Count] = good;
    BadBuffer[Count] = bad;
    Count++;
  }
}
```

**General Purpose Input/Output (GPIO) pins** can help debug purposes when the UART is in use or adding trace code is not particularly helpful. For example, we can turn on or off the built-in LED of an Arduino® board by inserting a `digitalWrite(13, HIGH)` instruction before or after questionable areas in our programs as shown in the example code below. If the built-in LED turns on, then we know that a particular line of code executed:

```arduino
// Print a message if the execution gets here
Serial.println("Code got here");

// Try to execute myFunction1()
myFunction1(); 

// Turn on the built-in LED for one second to indicate that myFunction1 was executed
digitalWrite(13, HIGH); 
delay(1000);
digitalWrite(13, LOW); 

// Try to execute myFunction2()
myFunction2(); 

// Turn on the built-in LED for one second to indicate that myFunction2 was executed
digitalWrite(13, HIGH); 
delay(1000);
digitalWrite(13, LOW);
```

### Remote Debuggers

**Remote debugging** is another common approach used to debug embedded systems. **Remote debuggers work by connecting a particular embedded system to a host computer** and then using software in the host computer to interact with the embedded system hardware. Remote debuggers are helpful when the development environment is on a different architecture rather than the target system. For example, think about developing code on a Windows-based computer for an ARM-based microcontroller system. 

Remote debuggers usually have two essential parts: a front-end debugger and a back-end debugger. 

* The front-end debugger contains the user interface (can be graphical or command-line-based user interface) and offers the programmer choices about the execution of the code in the embedded system hardware.
* The back-end debugger, also known as the "debug monitor," is specific for a particular processor. It starts when the processor resets and handles the runtime instruction between the front-end debugger and the embedded system hardware. 

### Simulators

Simulators are tools used to **simulate the functionality and the instruction set of the target processor**. These tools, usually, can only simulate the target processor functionalities but not its environment and external parts and components. Simulators are handy in the early stages of the development process, where we only have the software but have not implemented any hardware yet.

***[Tinkercad Circuits](https://www.tinkercad.com/learn/circuits) is an excellent simulator for beginners in the Arduino® ecosystem. This tool can simulate the instruction set of an Arduino® UNO board and the functionalities of several electronic components such as resistors, LEDs, motors, LCDs, and some sensors.***

### In-Circuit Emulators and In-Circuit Debuggers

An in-circuit emulators (or ICE) is a specialized tool that allows developers to examine the state of the processor while a particular program is running. ICEs are considered embedded systems by themselves, they are basically a copy of the target processor and memory (RAM, ROM). Emulators use remote debuggers to interact with the programmer or the developer. They support powerful debugging features such as hardware breakpoints and real-time tracing.

An in-circuit debugger (ICD) is also a specialized tool, connected between a computer and the analyzed system, that is used to debug real-time applications faster and easier. With an ICD a monitor program runs in the microcontroller in the test circuit. The programmer can set breakpoints, run code, single step the program, examine variables and registers on the real device, and, if required, change their values. An in-circuit debugger uses some memory and I/O pins of the target PIC microcontroller during the debugging operations.

***The fundamental difference between an ICE and an ICD relies on the resources used to control the debug target. In ICEs, resources are provided by the emulation hardware; in ICDs, resources are provided by the target processor.*** 

### Hardware Tools

Embedded systems developers and typical software developers differ on a key aspect: their "closeness" to hardware; embedded system developers are usually closer to hardware than typical software developers. There are several tools that embedded systems developers use to find out what is going on with the hardware, which is very helpful for low-level software debugging. These tools are **logic analyzers**, **oscilloscopes**, and **software-defined radios** (SDRs). 

Let us take a look at each one of the hardware debugging tools. A basic understanding of these tools can significantly improve debugging skills, especially while developing embedded systems devel. 

***Logic analyzers and oscilloscopes help debug interactions between the processor and other electronic parts on an embedded system. These tools do not control the flow of execution of the code of an embedded system.*** 

#### Logic Analyzers

A logic analyzer is a hardware tool designed specifically for capturing, displaying, and measuring electrical signals in a digital circuit. This tool consists of several digital inputs pins capable of detecting whether an electric signal is at a specific logic level (1 or 0). Logic analyzers are also capable of showing the relationship and timing of different electrical signals in a digital circuit and often capable also of analyzing digital communication protocols (for example, SPI).

#### Oscilloscopes

An oscilloscope is a hardware tool that graphically displays electrical signals and shows how those signals change over time. Signals are measured in an oscilloscope with the help of a sensor.

#### Software-Defined Radios

A software-defined radio (SDR) is a radio communication system that uses software for the modulation and demodulation of radio signals. Traditional radio communications systems processing relies on hardware components; this limits their reprogramming to a very low level. SDRs are much more flexible since they can be reconfigured by software. 

#### Debugging with Hardware Tools

While there may be several debugging techniques, using an LED indicator as a pass mark for the debugging process is the simplest yet fastest method one can utilize. The indicator will be set in different points of interest to observe the correct execution of tasks visually. For instance, there can be multiple points located simultaneously to turn it on or off the LED or a single point of interest at a time for step-by-step verification. This will provide just enough information to construct an additional layer of the code or proceed to the following structure sector to debug its behavior. It will not give precise or in-depth information about registry or data exchange, so it has to be used as a tool for code structures that are not complex in their architectural nature and behave mainly in a linear trend execution. It is handy when a debugger is not available and quickly understand how the code behaves.

Sometimes, LEDs might not be present or might not be available in a particular system; there is no way to make a visual inspection in the system. However, we can use an oscilloscope directly to measure the GPIO pins of the system in this case. The oscilloscope, in this case, can be used to monitor specific GPIO pins and see if the code gives specific feedback by driving the GPIO pin to the desired logic state. A **multimeter** can also be handy for the same task. 

To get the most out of an oscilloscope and GPIO pins is by measuring its **performance**. Oscilloscopes can also be used to determine specific signal's **electrical and timing properties**. For example, an unnecessary delay in the code can be identified with this information: 

`myFunction()` execution duration can be measured by setting a GPIO pin to be driven to a high logic level when its execution begins; when `myFunction()` execution ends, the GPIO pin can be driven to a low logic level. The oscilloscope can then provide information if the function execution took precisely the defined time, longer or shorter than expected, or if it has any unaccounted electrical behavior that changes the expected behavior.

Wireless communications help the development of new Internet of Things (IoT) devices with different requirements or specifications and for different purposes. Wireless communication is present on many embedded systems, and Arduino® hardware is no exception for this feature. The question now is: how do we debug wireless communications between devices? 

A simple technique used to debug wireless communications between devices consists of using acknowledge flags. Acknowledge flags are used to verify successful communication between devices; this process is found on physical communication layers, such as I2C or SPI, providing the present status between these devices. It goes the same for wireless communication between devices. Due to different protocol types in wireless communication, acknowledged methods may differ. The easiest way to confirm that the data exchange was successful is to check the log on each end device. So why would we need to debug on a radio frequency spectrum that is working correctly? It is to verify that the transceiver configuration is correct, mainly its transmission power. 

There are several software to assist this process and one of them is GQRX supported on OSX and Linux. For the Windows operating system, AirSpy could be software of choice to assist for this type of task. The SDR via USB stick can be used as a low cost spectrum analyzer, using the user's computer as a host for radio station. The devices to be debugged are powered on while SDR takes care of catching any present transmission on the air and display it on the screen. 

Shown visual representation of the signal via SDR software can now be used to verify the transmission power outputted by the device and the amount of data that flew on the air. This will help to visualize the properties of the device's wireless communication configuration. It will be possible to verify the transmission and reception power, the amount of bytes transmitted, and the frequency on which it is supposed to be transmitting. A very handy tool to debug wireless communication states of the devices. 

All these properties can be debugged through the radio frequency spectrum and refined to provide edge wireless communication performance on embedded systems. 

## Final Thoughts about Debugging and Embedded Software Development

Debugging is a necessary step for developing robust and reliable embedded systems. We can end this article by mentioning the **four** most essential phases of debugging:

* Testing.
* Stabilization.
* Localization.
* Correction.
 
The **testing** phase exercises the capability of the embedded software by stimulating it with a wide range of input values. The **stabilization** phase attempt to control the conditions that generate a specific bug. **The localization** phase involves narrowing the range of possibilities until the bug can be isolated to a specific code segment. The **correction** phase, the final phase, involves eradicating the bug from the software. 

## Further Reading and Resources

Debugging is an exciting topic to study, if you want to learn more about debugging tools and techniques, check out the following links: 

- Do you want to learn more bout [oscilloscopes](https://www.tek.com/en/blog/what-is-an-oscilloscope)? Learn more about them in this article from Tektronix®.
- Do you want to learn more about [logic analyzers](https://articles.saleae.com/logic-analyzers/what-is-a-logic-analyzer)? Learn more about them in this article from Saleae®.