---
title: PDM Library
description: The PDM library allows you to use Pulse-density modulation microphones, found onboard the Nano RP2040 Connect & Nano 33 BLE Sense boards.
author: 'Arduino'
tags: [Microphone, PDM]
---

## Overview

The PDM library allows you to use PDM ([Pulse-density modulation](https://en.wikipedia.org/wiki/Pulse-density_modulation)) microphones, such as the onboard MP34DT05 on the Arduino Nano 33 BLE Sense.

To use this library:

```
#include <PDM.h>
```

The library takes care of the audio that will be accessible also through the [ArduinoSound](https://www.arduino.cc/en/Reference/ArduinoSound) library.


## Functions

### `begin()`

#### Description

Initialize the PDM interface.

#### Syntax

```
PDM.begin(channels, sampleRate)

```

#### Parameters
- channels: the number of channels, 1 for mono, 2 for stereo
- sampleRate: the sample rate to use in Hz

#### Returns
1 on success, 0 on failure

#### Example

```
  if (!PDM.begin(1, 16000)) {
    Serial.println("Failed to start PDM!");
    while (1);
  }


```

### `end()`

#### Description

De-initialize the PDM interface.

#### Syntax

```
PDM.end()

```

#### Parameters
None

#### Returns
Nothing

#### Example

```
  if (!PDM.begin(1, 16000)) {
    Serial.println("Failed to start PDM!");
    while (1);
  }


  // 

  PDM.end();


```

### `available()`

#### Description

Get the number of bytes available for reading from the PDM interface. This is data that has already arrived and was stored in the PDM receive buffer.

#### Syntax

```
PDM.available()

```

#### Parameters
None

#### Returns
The number of bytes available to read

#### Example

```
// buffer to read samples into, each sample is 16-bits
short sampleBuffer[256];

// number of samples read
volatile int samplesRead;

// 

  // query the number of bytes available
  int bytesAvailable = PDM.available();

  // read into the sample buffer
  PDM.read(sampleBuffer, bytesAvailable);


```

### `read()`

#### Description

Read data from the PDM into the specified buffer.

#### Syntax

```
PDM.read(buffer, size)

```

#### Parameters
- buffer: array to store the PDM data into
- size: number of bytes to read

#### Returns
The number of bytes read

#### Example

```
// buffer to read samples into, each sample is 16-bits
short sampleBuffer[256];

// number of samples read
volatile int samplesRead;

// 

  // query the number of bytes available
  int bytesAvailable = PDM.available();

  // read into the sample buffer
  Int bytesRead = PDM.read(sampleBuffer, bytesAvailable);

  // 16-bit, 2 bytes per sample
  samplesRead = bytesRead / 2;


```

### `onReceive()`

#### Description

Set the callback function that is called when new PDM data is ready to be read.

#### Syntax

```

PDM.onReceive(callback)

```

#### Parameters
callback: function that is called when new PDM data is ready to be read

#### Returns
Nothing

#### Example

```
// buffer to read samples into, each sample is 16-bits
short sampleBuffer[256];

// number of samples read
volatile int samplesRead;

// 

  // configure the data receive callback
  PDM.onReceive(onPDMdata);

  // initialize PDM with:
  // - one channel (mono mode)
  // - a 16 kHz sample rate
  if (!PDM.begin(1, 16000)) {
    Serial.println("Failed to start PDM!");
    while (1);
  }


  // 

void onPDMdata() {
  // query the number of bytes available
  int bytesAvailable = PDM.available();

  // read into the sample buffer
  Int bytesRead = PDM.read(sampleBuffer, bytesAvailable);

  // 16-bit, 2 bytes per sample
  samplesRead = bytesRead / 2;
}



```

### `setGain()`

#### Description

Set the gain value used by the PDM interface.

#### Syntax

```
PDM.setGain(gain)

```

#### Parameters
gain: gain value to use, 0 - 255, defaults to 20 if not specified.

#### Returns
Nothing

#### Example

```
  // optionally set the gain, defaults to 20
  PDM.setGain(30);

  // initialize PDM with:
  // - one channel (mono mode)
  // - a 16 kHz sample rate
  if (!PDM.begin(1, 16000)) {
    Serial.println("Failed to start PDM!");
    while (1);
  }



```

### `setBufferSize()`

#### Description

Set the buffer size (in bytes) used by the PDM interface. Must be called before PDM.begin(...), a default buffer size of 512 is used if not called. This is enough to hold 256 16-bit samples.

#### Syntax

```
PDM.setBufferSize(size)

```

#### Parameters
size: buffer size to use in bytes

#### Returns
Nothing

#### Example

```
  PDM.setBufferSize(1024);

  // initialize PDM with:
  // - one channel (mono mode)
  // - a 16 kHz sample rate
  if (!PDM.begin(1, 16000)) {
    Serial.println("Failed to start PDM!");
    while (1);
  }

```