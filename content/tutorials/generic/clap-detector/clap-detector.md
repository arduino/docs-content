---
title: 'Clap Detector'
description: 'Learn how to build a clap detector'
difficulty: intermediate
tags: 
  - Amplitude
  - Audio 
  - LED
libraries:
  - name: ArduinoSound
    url: https://www.arduino.cc/en/Reference/ArduinoSound
hardware:
  - hardware/01.mkr/01.boards/mkr-zero
  - hardware/01.mkr/01.boards/mkr-1000-wifi
  - hardware/02.hero/boards/zero
software:
  - ide-v1
  - ide-v2
  - web-editor
author: "Arduino"
contributeURL: content/tutorials/generic
---
## Introduction
This example reads audio data from an Invensense's ICS43432I2S microphone breakout board, and uses the input to detect clapping sounds. The built-in LED is toggled when a clap is detected.

## Goals

- How to use and read audio data.
- How to use audio as an input.

## Hardware & Software Needed

- [Arduino Zero](https://store.arduino.cc/arduino-zero), [MKRZero](https://store.arduino.cc/arduino-mkr-zero-i2s-bus-sd-for-sound-music-digital-audio-data?queryID=undefined)  or [MKR1000 WiFi](/hardware/mkr-1000-wifi) Board

- Invensense's ICS43432I2S microphone
- Arduino IDE ([online](https://create.arduino.cc/) or [offline](https://www.arduino.cc/en/main/software)).
- [ArduinoSound Library](https://www.arduino.cc/en/Reference/ArduinoSound)
- Jumper wires
- Breadboard

### Circuit

![Clap detector circuit](assets/I2SMIC.png)


## Programming the Board


**1.** First, let's make sure we have correct the drivers installed. If we are using the Web Editor, we do not need to install anything. If we are using an offline editor, we need to install it manually. This can be done by navigating to **Tools > Board > Board Manager...**. Here we need to look for the **Arduino SAMD boards (32-bits Arm® Cortex®-M0+)** and install it. 

**2.** Now, we need to install the libraries needed. If we are using the Web Editor, there is no need to install anything. If we are using an offline editor, simply go to **Tools > Manage libraries...** and search for **ArduinoSound** and install it.


The sketch can be found in the snippet below. Upload the sketch to the board.



## Code

```arduino

/*

 This example reads audio data from an Invensense's ICS43432 I2S microphone

 breakout board, and uses the input to detect clapping sounds. An LED is

 toggled when a clap is detected.

 Circuit:

 * Arduino Zero, MKRZero or MKR1000 board

 * ICS43432:

   * GND connected GND

   * 3.3V connected 3.3V (Zero) or VCC (MKR1000, MKRZero)

   * WS connected to pin 0 (Zero) or pin 3 (MKR1000, MKRZero)

   * CLK connected to pin 1 (Zero) or pin 2 (MKR1000, MKRZero)

   * SD connected to pin 9 (Zero) or pin A6 (MKR1000, MKRZero)

 created 18 November 2016

 by Sandeep Mistry

 */

#include <ArduinoSound.h>

// the LED pin to use as output

const int ledPin = LED_BUILTIN;

// the amplitude threshold for a clap to be detected

const int amplitudeDeltaThreshold = 100000000;

// create an amplitude analyzer to be used with the I2S input

AmplitudeAnalyzer amplitudeAnalyzer;

// variable to keep track of last amplitude
int lastAmplitude = 0;

void setup() {

  // setup the serial

  Serial.begin(9600);

  // configure the LED pin as an output

  pinMode(ledPin, OUTPUT);

  // setup the I2S audio input for 44.1 kHz with 32-bits per sample

  if (!AudioInI2S.begin(44100, 32)) {

    Serial.println("Failed to initialize I2S input!");

    while (1); // do nothing

  }

  // configure the I2S input as the input for the amplitude analyzer

  if (!amplitudeAnalyzer.input(AudioInI2S)) {

    Serial.println("Failed to set amplitude analyzer input!");

    while (1); // do nothing

  }
}

void loop() {

  // check if a new analysis is available

  if (amplitudeAnalyzer.available()) {

    // read the new amplitude

    int amplitude = amplitudeAnalyzer.read();

    // find the difference between the new amplitude and the last

    int delta = amplitude - lastAmplitude;



    // check if the difference is larger than the threshold

    if (delta > amplitudeDeltaThreshold) {

      // a clap was detected

      Serial.println("clap detected");



      // toggle the LED

      digitalWrite(ledPin, !digitalRead(ledPin));



      // delay a bit to debounce

      delay(100);

    }



    // update the last amplitude with the new amplitude

    lastAmplitude = amplitude;

  }
}
```

## Testing It Out

After you have uploaded the code, start clapping. The in-built LED should now light up!

### Troubleshoot

If the code is not working, there are some common issues we can troubleshoot:

- The microphone is not wired correctly.
- Make sure there are no missing curly brackets {}.
- You have not installed the [ArduinoSound Library](https://www.arduino.cc/en/Reference/ArduinoSound).
- You have not selected the right port and board.

## Conclusion

In this example, we have learned how to create a clap detector using the [ArduinoSound Library](https://www.arduino.cc/en/Reference/ArduinoSound) with a microphone to turn on the in-built LED. With this knowledge in the bag you can start to think about how sound can be used as an input to control various outputs!