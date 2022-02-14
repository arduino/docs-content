---
title: 'Debugging Fundamentals'
description: 'Learn the basics of debugging microcontroller-based systems.'
tags: 
  - Debugging
  - Embedded systems
author: 'José Bagur, Taddy Chung'
---

# Debugging Fundamentals

**Embedded systems** are microprocessor or microcontroller-based systems with a dedicated operational role. Rather than being made of separate components, like desktop computers, laptops or, gaming consoles, embedded systems integrate all the hardware and software necessary for a particular purpose. Nowadays, embedded systems are everywhere: automobiles, cameras, household appliances, and mobile devices are just some examples.

Embedded systems design can be challenging since it combines hardware design, firmware, and software development, all in one particular device or product. In order to produce high-quality embedded firmware and software for a particular device or product, **debugging** is a necessary step in their development process. **Debugging is the process of confirming that, one by one, many things that we believe to be true and functional in our code are true**. We find a "bug" in our code when one our assumptions are not valid. 

The following article will discuss different debugging techniques used to find bugs in microcontroller-based systems, especially those based on Arduino® hardware.  

## Debugging Techniques

There are some basic debugging techniques that we can implement to validate our code:

* The compiler and syntax errors
* Traditional techniques: trace code and GPIOs.
* Remote debuggers.
* Simulators.
* In-circuit Emulators (ICE) and In-Circuit Debuggers (ICD).
* Hardware tools: oscilloscopes and logic analyzers. 

Let us take a look into each one of the techniques.

### The compiler and syntax errors

The compiler helps identify **syntax errors**. Syntax errors indicate something wrong with the program's syntax; for example, **when a semi-colon is omitted at the end of a statement in a program**, the compiler generates a syntax error. Using the compiler for debugging this type of errors can be sometimes tricky; let us analyze two commonly encounterd situations: 

* **The compiler shows 100 errors**: This usually does not mean there are 100 errors; it often gets thrown off track for a while when the compiler finds an error. The compiler tries to recover and pick up again after the first error, but sometimes it reports false errors. **Only the first error message is genuinely reliable**; try to fix one error at a time and then recompile the program.
* **Getting weird compiler messages**: Compiler errors are shown in terse jargon, sometimes hard to read and understand, but with hidden and valuable information. Please read the error message carefully; it will always tell where, inside the program, the error occurred.

### Traditional techniques: trace code and GPIO's

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

Another trace code technique consits of **dumping strategic information into an array at run time**, we can then observe the contents of the array at a later time (for example, when the program terminates); this technique is also known as **dump into array**. Assume `good` and `bad` are two strategic variables we want to capture. The first step is to define a debug buffer in RAM to save the debugging measurements as shown in the code below:

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

GPIOs help debug purposes when the UART is in use or adding trace code is not particularly helpful. For example, we can turn on or off the built-in LED of an Arduino® board by inserting a `digitalWrite(13, HIGH)` instruction just before or after questionable areas in our programs, as shown in the example code below. If the built-in LED turns on, then we know that a particular line of code executed:

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

### Remote debuggers

Remote debugging is one of the common approaches used to download, execute, and debug embedded software. Remote debuggers work by connecting the embedded software to a computer and then using a software GUI to interact with the hardware. Remote debuggers have two parts: 

* Front-end debugger: This is the part of the debugger that contains the GUI and offers the programmer choices about the execution of the code.
* Back-end debugger: The "debug monitor" is a piece of software designed specifically for an embedded processor. It starts when the processor is reset and handles the runtime instruction between the front-end debugger and the hardware. An example of a debugging monitor is the GNU portable debugger.

### Simulators

A simulator can be installed on any computer and is used to simulate the functionality and instructions set by the target processor. Simulators are very valuable in the early stages of the design process, where we only have the software but have not implemented any hardware yet. However, the disadvantage of simulators is that they only simulate the processor and not the environmental interaction peripherals.

### In-circuit emulators and In-circuit debuggers

In-circuit emulators (or ICEs) are specialized software that allows the developer to examine the state of the processor while the program is running. ICEs are considered embedded systems by themselves, with their copy of the processor and memory (RAM, ROM). Emulators use remote debuggers to interact with the programmer or the developer. They support powerful debugging features such as hardware breakpoints and real-time tracing.

An in-circuit debugger is a hardware device, connected between a PC and the target microcontroller test system, and is used to debug real-time applications faster and easier. With in-circuit debugging, a monitor program runs in the microcontroller in the test circuit. The programmer can set breakpoints on the PIC, run code, single step the program, examine variables and registers on the real device, and, if required, change their values. An in-circuit debugger uses some memory and I/O pins of the target PIC microcontroller during the debugging operations.

### Hardware Tools
As mentioned before, one of the key aspects that differentiates the embedded developer from the typical software developer is “closeness” to the hardware. Several tools are available to assist you with finding out what is going on with the hardware. A
basic understanding ofhow to use these tools is essential to developing good debugging skills, particularly since these same tools are very useful for low-level software debugging. Once you have access to your target hardware—and especially during hardware debug—logic analyzers and oscilloscopes can be indispensable debug tools. A logic analyzer and an oscilloscope are most useful for debugging the interactions between the processor and other chips on the board. Because they can view only signals that lie outside the processor, however, these tools cannot control the flow of execution of software. This lack of software execution control makes them significantly less useful by themselves, but coupled with a software debug tool such as a remote debugger or an emulator, they can be extremely valuable.

### Logic Analyzers
A logic analyzer is a piece of laboratory equipment designed specifically for troubleshooting digital hardware. It can have dozens or even hundreds ofinputs, each capable ofdetecting only one thing: whether the electrical signal it is attached to is currently at logic level 1 or 0. Any subset ofthe inputs that you select can be displayed against a timeline as illustrated in Figure 5-4. Most logic analyzers will also let you begin capturing data, or trigger, on a particular pattern. For example, you might make this request: “Display the values ofinput signals 1 through 10, but don’t start recording what happens until inputs 2 and 5 are both zero at the same time.”

### Oscilloscope

An oscilloscope is another piece oflaboratory equipment for hardware debugging. But this one is used to examine any electrical signal—analog or digital—on any piece of hardware. Oscilloscopes are sometimes useful for quickly observing the voltage or signal waveform on a particular pin, or, in the absence of a logic analyzer, for something slightly more complex. However, the number ofinputs is much smaller (there are usually two to four), and advanced triggering logic is not often available.

### Debugging with Hardware Tools

One ofthe most primitive debug techniques available is the use ofan LED as an indicator ofsuccess or failure. The basic idea is to slowly walk the LED enable code through the larger program. In other words, first begin with the LED enable code at the reset address. Ifthe LED turns on, you can edit the program—moving the LED enable code to just after the next execution milestone—and then rebuild and test. Because this technique gives you very little information about the state of the processor, it is most appropriate for very simple, linearly executed programs such as the startup code. But ifyou don’t have access to a remote debugger or any ofthe other debug tools, this type of debugging might be your only choice.

If an LED is not present on your hardware platform, you can still use this debug technique with an I/O signal and an oscilloscope. In this case, set the I/O signal to a specific level once you reach a particular execution milestone. Using the oscilloscope, you can then probe that I/O pin to determine whether the code has set it appropriately. Ifso, you know that the code executed successfully up to that point, and you can now move the I/O signal code to the next milestone. 

The method ofusing an I/O signal and an oscilloscope can also be used as a basic performance measurement tool. An I/O pin can be used to measure how long a program is spending in a given routine, or how long it takes to execute a particular fragment
of code. This can show potential bottlenecks in the program. For example, to precisely measure the length oftime spent in the delay_ms routine (when passed in a parameter of1), we could set an I/O pin high when we enter the routine and then set the same I/O pin low before exiting. We could then attach an oscilloscope lead to this I/O pin to measure the amount oftime that the I/O pin is high, which is the time spent in the delay_ms routine.
