---
title: 'I2S Library'
description: 'Documentation for usage of the I2S (Inter-IC Sound) protocol on SAMD21 boards.'
author: 'Arduino'
tags: [I2S, Audio, SAMD]
---

## Overview

This library allows you to use the I2S protocol on SAMD21 based boards (i.e Arduino or Genuino Zero, MKRZero, MKR1000 or Nano 33 IoT).

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

The left and right channels are interleaved in the data stream, and "one sample" is one value for the left channel and one for the right. This means that the FS line oscillates at the sample rate.

In a typical setup, the sender of audio data is called a Transmitter and it transfers data to a Receiver at the other end. The device that controls the bus clock, SCK, together with the Word Select - WS - signal is the Controller in the network and in any network just one device can be Controller at any given time; all the other devices connected are in Peripheral mode. The Controller can be either the Transmitter, or the Receiver, or a standalone controller managing the transfer of data between two other devices. The digitized audio data samples can have a size ranging from 4 bits up to 32 bits for each channel. The data is in **signed** format, meaning that 8-bit values are interpreted as -128 to 127, not 0 to 255, and 16-bit values are interpreted as -32768 to 32767.

As a general rule of thumb, the higher the sample rate (kHz) and bits per sample, the better audio quality when the digital data is converted back to analog audio sound. A digitized signal with a sample rate of X Hz can capture sound frequencies of up to X/2 Hz. Higher frequencies in the sound will cause problems with **aliasing**. For more information on this, please refer to literature on digital sound processing.

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
mode: one of I2S_PHILIPS_MODE, I2S_RIGHT_JUSTIFIED_MODE or I2S_LEFT_JUSTIFIED_MODE
sampleRate: the desired sample rate in Hz - long
bitsPerSample: the desired number of bits per sample (i.e 8, 16, 32)

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
Get the number of **bytes** (not the number of samples) available for reading from the I2S interface. This is data that has already arrived and was stored in the I2S receive buffer. available() inherits from the Stream utility class.

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

### `write()`

#### Description
Writes binary data to the I2S interface. Data is sent either as one sample or a sequence of samples.

The single argument function `write(val)` writes one sample for one channel. A full write requires
calling this function twice, once for the left channel and once for the right channel.
If the device buffer is full, the function blocks until the data can be written.
Before writing, the value `val` will be converted to the appropriate number of bits per sample.

The two-argument function `write(buf, len)` writes a sequence of samples from the array `buf`.
Data must be stored in the proper format for the sample size, with the left and right channels
interleaved, and the argument `len` specifies the number of **bytes** in the buffer, not the
number of samples. If the device buffer is too full to hold all the data, the function writes
as much as will fit (possibly nothing), and returns without blocking. The return value is the
number of bytes that was actually written. It is the responsibility of the application to
handle any such partial writes and act accordingly.

#### Syntax

```
I2S.write(val)  // Might block for a moment until data can be written
I2S.write(buf, len) // Will not block, but might not write all the data

```

#### Parameters
val: a value to send as a single sample

buf: an array to send as a sequence of samples

len: the length of the buffer, in bytes (not in number of samples)

#### Returns
size_t 
- write(buf, len) will return the number of bytes written. Reading that number is optional, but partial writes that are not handled properly will cause popping, crackling or stutter in the sound.

### `availableForWrite()`

#### Description
Get the number of bytes available for writing in the buffer without blocking the write(val) operation, and without causing the write(buf, len) operation to return without writing all the data.

#### Syntax

```
I2S.availableForWrite()

```

#### Parameters
none

#### Returns
size_t
- the number of bytes available to write

### `onTransmit(handler)`

#### Description
Registers a function to be called when a block of data has been transmitted. This is used in conjunction with the two-argument function write(buf, len), and the callback function is called when the DMA write operation that was triggered by write(buf, len) finishes. The callback takes no arguments, which mean it cannot determine by itself if the write was completely successful or wrote only some part of the data. Partial writes need to be handled separately by the application.

The callback is not triggered by the single argument version `write(val)`, only by the two argument version `write(buf, len)`. The callback can be registered once at setup of the I2S interface, and will be called for every subsequent write() -- you do not need to register it anew for every write operation.

#### Parameters
handler: the function to be called when data is sent. It must be a function with no arguments returning nothing, e.g.: void myHandler()

#### Returns
None

### `read()`

#### Description
Reads binary data from the I2S interface. Data is read either as one sample or a sequence of samples.

The single argument function `read(val)` reads one sample for one channel. A full read requires
calling this function twice, once for the left channel and once for the right channel.
If the device buffer is empty, the function blocks until there is data available.
The return value is always an `int`. You will need to know the number of bits per sample
to handle the data correctly.

The two-argument function `read(buf, len)` reads a sequence of samples into the array `buf`.
Data will be stored in the binary format for the current sample size, with the left and right
channels interleaved. The argument `len` specifies the number of **bytes** in the buffer, not the
number of samples. If the device has more data available than what fits in `buf`,
the function retrieves as much as will fit. If the device has less data available, possibly
nothing, the function will read what is available and return without blocking. The return
value is the number of bytes that was actually read. It is the responsibility of the
application to read the return value and act accordingly.

#### Syntax

```
val = I2S.read()  // Might block until data is available for reading
I2S.read(buf, len) // Will not block, but might not read all the data

```

#### Parameters

buf: an array to store a sequence of samples

len: the length of the `buf` array, in bytes (not in number of samples)

#### Returns
size_t 
- read(buf, len) will return the number of bytes read. Reading that number is essential, as the transmitting device will typically not fill the buffer completely with every read operation.

### `onReceive(handler)`

#### Description
Registers a function to be called when a block of data has been received. This works just like the `onTransmit()` handler, but for the `read(buf, len)` function that receives data from a device. The callback is not triggered for the no-argument version of `read()` that reads a single sample value.

#### Parameters
handler: the function to be called when the device receives data. It must be a function with no arguments returning nothing, e.g.: void myHandler()

#### Returns
None

