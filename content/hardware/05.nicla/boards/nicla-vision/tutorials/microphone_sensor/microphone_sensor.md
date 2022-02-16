---
title: 'Testing and Controlling the Microphone'
difficulty: easy
compatible-products: [nano-33-ble-sense]
description: 'Learn how to create a soundmeter using the built-in microphone with the Nicla Vision.'
tags:
  - OpenMV
  - Microphone
  - Sound
  - Sensor
author: Pablo Marquínez
libraries: 
  - name: Arduino PDM
    url: https://www.arduino.cc/en/Reference/PDM
hardware:
  - hardware/05.nicla/boards/nicla-vision
software:
  - OpenMV
  - ide-v1
  - ide-v2
  - web-editor
  - cli
featuredImage: 'chip'
---

## Overview

In this tutorial you will use the **Arduino Nicla VIsion** board to get the microphone (MP34DT06JTR) readings and change the LED brightness.

## Goals

- Get the microphone data.
- Use the PDM(Pulse-density modulation) library.
- Print the microphone values in the Serial Monitor.
- Change RGB brightness with the stored microphone values.

### Required Hardware and Software

- Arduino Nicla Vision
- Latest mbed Core version

## Set up

To check that you set up correctly the board please visit our [Getting Started Guide]() for both **OpenMV** and **Arduino** available instructions.

## OpenMV

Open the program by going to **Examples > Arduino > NanoRP2040 > Audio > Audio_fft.py**.

***Using the same sketch as  the NanoRP2040, cause both boards have the same microphone***

Make sure you linked the board by checking the Serial Port and upload the program.

You will see an spectrum analizer on the top right panel that reflects the audio readings input.

## Arduino

### Setting up the sketch

We will edit the example from the mbed Core, go to **Examples > PDM > PDMSerialPlotter** and save it into your sketchbook.

You can run the sketch to see the result, it will show the data that the microphone is getting on the **Serial Plotter**.

### Controlling the LED brightness

Now that you can get the microphone data, let's control the built-in RGB LED and change its brightness depending on the values.

**4. Complete code**

You can access the example sketch at **Examples > PDM > PDMSerialPlotter** and then edit as we shown.
Or the full edited sketch on our Arduino_Pro_Tutorials library.

```arduino
  /*
    This example reads audio data from the on-board PDM microphones, and prints
    out the samples to the Serial console. The Serial Plotter built into the
    Arduino IDE can be used to plot the audio data (Tools -> Serial Plotter)
    Circuit:
    - Arduino Nano 33 BLE board, or
    - Arduino Nano RP2040 Connect, or
    - Arduino Portenta H7 board plus Portenta Vision Shield
    This example code is in the public domain.
  */

  #include <PDM.h>

  // default number of output channels
  static const char channels = 1;

  // default PCM output frequency
  static const int frequency = 16000;

  // Buffer to read samples into, each sample is 16-bits
  short sampleBuffer[512];

  // Number of audio samples read
  volatile int samplesRead;

  // Variable to save the brightness of the LED
  int brightness;

  void setup() {
    Serial.begin(9600);
    while (!Serial);

    // Configure the data receive callback
    PDM.onReceive(onPDMdata);

    // Optionally set the gain
    // Defaults to 20 on the BLE Sense and 24 on the Portenta Vision Shield
    // PDM.setGain(30);

    // Initialize PDM with:
    // - one channel (mono mode)
    // - a 16 kHz sample rate for the Arduino Nano 33 BLE Sense
    // - a 32 kHz or 64 kHz sample rate for the Arduino Portenta Vision Shield
    if (!PDM.begin(channels, frequency)) {
      Serial.println("Failed to start PDM!");
      while (1);
    }

    // Set the LED
    pinMode(LEDB, OUTPUT);
    analogWrite(LEDB, 0); // Used with PWM to control the 255-0% 0-100%
  }

  void loop() {
    // Wait for samples to be read
    if (samplesRead) {

      // Print samples to the serial monitor or plotter
      for (int i = 0; i < samplesRead; i++) {
        if(channels == 2) {
          Serial.print("L:");
          Serial.print(sampleBuffer[i]);
          Serial.print(" R:");
          i++;
        }
        Serial.println(sampleBuffer[i]);

        // Control the LED's brightness
        brightness = (int)map(sampleBuffer[i], 0, 512, 0, 255);
        analogWrite(LEDB, brightness);
      }

      // Clear the read count
      samplesRead = 0;
    }
  }

  /**
  * Callback function to process the data from the PDM microphone.
  * NOTE: This callback is executed as part of an ISR.
  * Therefore using `Serial` to print messages inside this function isn't supported.
  * */
  void onPDMdata() {
    // Query the number of available bytes
    int bytesAvailable = PDM.available();

    // Read into the sample buffer
    PDM.read(sampleBuffer, bytesAvailable);

    // 16-bit, 2 bytes per sample
    samplesRead = bytesAvailable / 2;
  }
```



## Testing It Out

After you have successfully verified and uploaded the sketch to the board, open the Serial Monitor from the menu on the left. You will now see the new values printed.

![Microphone data in the Serial Monitor.](assets/nano33BS_08_printing_values.png)

If you want to test it, the only thing you need to do is to place the board next to a speaker and speak or play some sound to see how the brightness of the RGB LED change based on the input.

### Troubleshoot

## Conclusion

