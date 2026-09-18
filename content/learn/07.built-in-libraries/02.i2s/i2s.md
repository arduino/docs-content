---
title: 'I2S Library'
description: 'Documentation for usage of the I2S (Inter-IC Sound) protocol on SAMD21 boards.'
author: 'Arduino'
tags: [I2S, Audio, SAMD]
---

## Overview

This library allows you to use the I2S protocol on SAMD21 based boards (i.e Arduino or Genuino Zero, MKRZero or MKR1000 Board).

To use this library

```
#include <I2S.h>
```

I2S (Inter-IC Sound), is an electrical serial bus interface standard used for connecting digital audio devices together. It is used to communicate PCM audio data between integrated circuits in an electronic device.

An I2S bus that follows the Philips standard is made up of at least three wires:

- **SCK** (Serial Clock): is the clock signal also referred as **BCLK** (Bit Clock Line);
- **FS** (Frame Select): used to discriminate Right or Left Channel data also referred **WS** (Word Select);
- **SD** (Serial Data): the serial data to be transmitted;

As detailed below, the device who generates **SCK** and **WS** is the Controller.

The SCK line has a frequency that depends on the sample rate, the number of bits for channel and the number of channels in the following way:

- **Frequency = SampleRate x BitsPerChannel x numberOfChannels**

In a typical setup, the sender of audio data is called a Transmitter and it transfers data to a Receiver at the other end. The device that controls the bus clock, SCK, together with the Word Select - WS - signal is the Controller in the network and in any network just one device can be Controller at any given time; all the other devices connected are in Peripheral mode. The Controller can be the Transmitter, or the Receiver, or a standalone controller. The digitized audio data sample can have a size ranging from 4 bits up to 32.

As a general rule of thumb, the higher the sample rate (kHz) and bits per sample, the better audio quality (when the digital data is converted back to analog audio sound).

## I2S Class

### `begin()`

#### Description
Initializes the I2S interface with the given parameters to enable communication.

#### Syntax

```
I2S.begin(mode, sampleRate, bitsPerSample); // controller device
I2S.begin(mode, bitsPerSample); // peripheral device

```

#### Parameters
mode: one between I2S_PHILIPS_MODE, I2S_RIGHT_JUSTIFIED_MODE or I2S_LEFT_JUSTIFIED_MODE
sampleRate: the desired sample rate in Hz - long
bitsPerSample: the desired bits per sample (i.e 8, 16, 32)

#### Returns
1 if initialization is ok, 0 otherwise

### `end()`

#### Description
Disables I2S communication, allowing the I2S pins to be used for general input and output. To re-enable I2S communication, call I2S.begin().

#### Syntax

```
I2S.end()

```

#### Parameters
none

#### Returns
nothing

### `available()`

#### Description
Get the number of bytes available for reading from the I2S interface. This is data that has already arrived and was stored in the I2S receive buffer. available() inherits from the Stream utility class.

#### Syntax

```
I2S.available()

```

#### Parameters
none

#### Returns
the number of bytes available to read

### `peek()`

#### Description
Returns the next sample of incoming I2S data without removing it from the internal I2S buffer. That is, successive calls to peek() will return the same sample, as will the next call to read(). peek() inherits from the Stream utility class.

#### Syntax

```
I2S.peek()

```

#### Parameters
None

#### Returns
The next sample of incoming I2S data available (or 0 if no data is available)


### `read()`

#### Description

Reads incoming I2S data from the I2S interface. This method reads and removes the next sample of incoming I2S data available from the internal I2S buffer. read() inherits from the Stream utility class.

#### Syntax

```
I2S.read()
```

```
I2S.read(buffer, length)
```

#### Parameters

None (for single sample read)

buffer: an array to read data into

length: the number of samples to read

#### Returns

The first sample of incoming I2S data available (or -1 if no data is available) - int

For buffer read: the number of samples read into the buffer
### `write()`

#### Description
Writes binary data to the I2S interface. This data is sent as a sample or series of samples.

#### Syntax

```
I2S.write(val) // blocking
I2S.write(buf, len) // not blocking

```

#### Parameters
val: a value to send as a single sample

buf: an array to send as a series of samples

len: the length of the buffer

#### Returns
byte 
- write() will return the number of bytes written, though reading that number is optional.

### `availableForWrite()`

#### Description
Get the number of bytes available for writing in the buffer without blocking the write operation.

#### Syntax

```
I2S.availableForWrite()

```

#### Parameters
none

#### Returns
the number of bytes available to write.

### `onTransmit(handler)`

#### Description
Registers a function to be called when a block of data has been transmitted.

#### Parameters
handler: the function to be called when data is sent and return nothing, e.g.: void myHandler()

#### Returns
None

### `onReceive(handler)`

#### Description
Registers a function to be called when a block of data has been received.

#### Parameters
handler: the function to be called when the device receives data and return nothing, e.g.: void myHandler()

#### Returns
None

