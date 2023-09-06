---
title: 'Firmata Library'
description: 'The Firmata library implements the Firmata protocol for communicating with software on the host computer.'
tags: 
  - Libraries
---


The **Firmata** library implements the [Firmata protocol](https://github.com/firmata/protocol) for communicating with software on the host computer. This allows you to write custom firmware without having to create your own protocol and objects for the programming environment that you are using.

To use this library
```
#include <Firmata.h>
```
## Methods
```
begin(); //start the library
begin(long); //start the library and override the default baud rate
begin(Stream &s); // start the library using a [Stream](http://www.arduino.cc/en/Reference/Stream) other than Serial (eg Serial1 or EthernetClient)
printVersion(); //send the protocol version to the host computer
blinkVersion(): //blink the protocol version on the build in LED (typically pin 13)
printFirmwareVersion(); //send the firmware name and version to the host computer
setFirmwareVersion(byte major, byte minor); //set the firmware name and version, using the sketch's filename, minus the '.ino'
setFirmwareNameAndVersion(const char *name, byte major, byte minor); //set both the name and version of the firmware
```
### `Sending Messages`
```
sendAnalog(byte pin, int value); //send an analog message
sendDigitalPort(byte portNumber, int portData); //send an 8-bit port in a single digital message
sendString(const char* string); //send a string to the host computer
sendString(byte command, byte bytec, byte *bytev); //send a string to the host computer using a custom command type
sendSysex(byte command, byte bytec, byte* bytev); //send a command with an arbitrary array of bytes
write(byte c); //write a byte to the Stream
```
### `Receiving Messages`
```
available(); //check to see if there are any incoming messages in the buffer
processInput(); //process incoming messages from the buffer, sending the data to any registered callback functions
attach(byte command, callbackFunction myFunction); //attach a function to an incoming message type
detach(byte command); //detach a function from an incoming message type
```
## Utility methods
```
sendValueAsTwo7bitBytes(int value); //writes value as 2 bytes
startSysex(void); //starts a sysex message
endSysex(void); //ends a sysex message
```
## Callback Functions
In order to attach your function to a message type, your function must match the standard callback function. There are currently three types of callback functions in Firmata: generic, string, and sysex.

**generic**
```
void callbackFunction(byte pin, int value);
```
**system_reset**
```
void systemResetCallbackFunction(void);
```
**string**
```
void stringCallbackFunction(char *myString);
```
**sysex**
```
void sysexCallbackFunction(byte command, byte byteCount, byte *arrayPointer);
```
### `Message Types`
There are various message types that you can attach callback functions to.
```

ANALOG_MESSAGE //the analog value for a single pin
DIGITAL_MESSAGE //8-bits of digital pin data (one port)
REPORT_ANALOG //enable/disable the reporting of an analog pin
REPORT_DIGITAL //enable/disable the reporting of a digital port
SET_PIN_MODE //change the pin mode between INPUT/OUTPUT/PWM/etc.
STRING_DATA //C-style strings, uses stringCallbackFunction for the function type
SYSEX_START //generic, arbitrary length messages (via MIDI SysEx protocol), uses sysexCallbackFunction for the function type
SYSTEM_RESET //message to reset firmware to its default state, uses systemResetCallbackFunction for the function type
```
## Example
This example shows how to send and receive analog messages using Firmata.
```
#include <Firmata.h>

byte analogPin;

void analogWriteCallback(byte pin, int value)
{
  pinMode(pin, OUTPUT);
  analogWrite(pin, value);
}

void setup()
{
  Firmata.setFirmwareVersion(FIRMATA_MAJOR_VERSION, FIRMATA_MINOR_VERSION);
  Firmata.attach(ANALOG_MESSAGE, analogWriteCallback);
  Firmata.begin();
}

void loop()
{
  while (Firmata.available()) {
    Firmata.processInput();
  }
  for (analogPin = 0; analogPin < TOTAL_ANALOG_PINS; analogPin++) {
    Firmata.sendAnalog(analogPin, analogRead(analogPin));
  }
}
```
