---
title: GIGA Display Shield Microphone & LVGL Tutorial
description: "Learn how to use the GIGA Display Shield's microphone with LVGL."
author: Benjamin Dannegård
tags: [Display, microphone, LVGL]
---

The GIGA Display Shield comes equipped with on-board microphone that when combined with the visual element of the GIGA Display Screen can be used in a number of ways. For example, using the LVGL framework the display can be used to show an animated volume indicator. Using the [Arduino_Graphics]() or [Arduino_GigaDisplay_GFX](https://github.com/arduino-libraries/Arduino_GigaDisplay_GFX) libraries we can detect when a loud noise, like a clap is made and change a visual element on the screen. This tutorial will take a closer look at the [PDM library](https://docs.arduino.cc/learn/built-in-libraries/pdm) to see how this can be used. And then re-create the two sketches mentioned.

## Hardware & Software Needed

- [Arduino GIGA R1 WiFi](/hardware/giga-r1)
- [Arduino GIGA Display Shield](/hardware/giga-display-shield)
- [Arduino IDE](https://www.arduino.cc/en/software)

## Downloading the Library and Core

Make sure the latest GIGA core is installed in the Arduino IDE. **Tools > Board > Board Manager...**. Here you need to look for the **Arduino Mbed OS Giga Boards** and install it, the [Arduino_H7_Video library](https://github.com/arduino/ArduinoCore-mbed/tree/main/libraries/Arduino_H7_Video) and [PDM library](https://docs.arduino.cc/learn/built-in-libraries/pdm) are included in the core.

## Microphone Readings With The Shield

### Testing The Microphone

To test the microphone we can use the **PDMSerialPlotter** example sketch. This sketch can be found in **File > Examples > PDM** in the Arduino IDE. This sketch will print readings in the serial monitor. Upload the sketch and check so that readings are appearing in the serial monitor.

![Example sketch printing values in the serial monitor](assets/pdm-test-sketch.png)

### Using the Microphone Readings

Now let's take a look at the PDM sketch and how we can use the microphone readings.

First we need to define the number of output channels, output frequency, a variable for counting when reading from the buffer and creating the buffer which the readings will be put into. This is done with the following lines:

```arduino
// default number of output channels
static const char channels = 1;

// default PCM output frequency
static const int frequency = 16000;

// Buffer to read samples into, each sample is 16-bits
short sampleBuffer[512];

// Number of audio samples read
volatile int samplesRead;
```

A callback function needs to be set, which is called when new PDM data is ready to be read. We do this in the `setup()` function using:

```arduino
  PDM.onReceive(onPDMdata);
```

`onPDMdata` is the callback function that we will have to create at the end of the sketch.

Now when we want to print or use the readings lets do it with a `for` loop since they are inside a buffer, which we need to step through. But lets first check so that there are readings to be printed with a simple `if` statement. These lines will step through the buffer until all the readings inside are printed and then start over:

```arduino
if (samplesRead) {
    for (int i = 0; i < samplesRead; i++) {
      Serial.println(sampleBuffer[i]);
    }
}
```

Its inside this `for` loop where we can get readings that will then change visual elements on the screen. This is where you would put any code that needs to react to the microphone readings.

And the last important part is the callback function that we used in the `setup()` function. This will take care of reading the values into the buffer and setting the value of the `samplesRead` variable which we used in the previous step.


```arduino
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

### Clap Detection Sketch

This sketch uses the [Arduino_Graphics library](https://www.arduino.cc/reference/en/libraries/arduinographics/) to change the color of the background when a loud noise is detected, such as a clap.

```arduino

```

### Volume Indication Sketch

This sketch requires the [lvgl library](https://github.com/lvgl/lvgl), please make sure that is installed before you upload the sketch. The sketch will show a bar on the screen that is animated when noise is made, functionally making it display the volume of the microphones readings. For more information about using lvgl with the GIGA Display Shield, take a look at our documentation [here](tutorials/). You will find the full sketch in the example below:

```arduino
#include <PDM.h>
#include "Arduino_H7_Video.h"
#include "lvgl.h"

Arduino_H7_Video          Display(800, 480, GigaDisplayShield);

static void set_slider_val(void * bar, int32_t val) {
  lv_bar_set_value((lv_obj_t *)bar, val, LV_ANIM_ON);
}

// default number of output channels
static const char channels = 1;

// default PCM output frequency
static const int frequency = 16000;

// Buffer to read samples into, each sample is 16-bits
short sampleBuffer[512];

// Number of audio samples read
volatile int samplesRead;

lv_obj_t * obj;
lv_anim_t a;
int micValue;

void setup() {
  Display.begin();

  PDM.onReceive(onPDMdata);

  if (!PDM.begin(channels, frequency)) {
    Serial.println("Failed to start PDM!");
    while (1);
  }

  // Create the bar
  obj = lv_bar_create(lv_scr_act());
  lv_obj_set_size(obj, 600, 50);
  lv_obj_center(obj);
  lv_bar_set_value(obj, 500, LV_ANIM_OFF);
  
  // Create the animation for the bar
  lv_anim_init(&a);
  lv_anim_set_exec_cb(&a, set_slider_val);
  lv_anim_set_time(&a, 300);
  lv_anim_set_playback_time(&a, 300);
  lv_anim_set_var(&a, obj);
}

void loop() {
  
  // Wait for samples to be read
  if (samplesRead) {

    // Print samples to the serial monitor or plotter
    for (int i = 0; i < samplesRead; i++) {
      Serial.println(sampleBuffer[i]);
      micValue = sampleBuffer[i];
      micValue = micValue / 100;
      if (micValue > 500)
      {
        micValue = 500;
      }
      lv_anim_set_values(&a, 0, micValue);
      lv_anim_start(&a);
    }

    // Clear the read count
    samplesRead = 0;
    delay(10);
  }
  lv_timer_handler();
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

[GIF of sketch running]()

## Conclusion

Now you know how to get readings from the GIGA Display Shield's on-board microphone and how to create simple visual elements that react to those readings.

## Next Step
Now that you know how to use the on-board microphone, feel free to explore the shield's other features, like the IMU with our [Orientation tutorial](/tutorials/image-orientation). Or if you rather dive deeper into LVGL, take a look at our [LVGL guide](tutorials/lvgl-guide).