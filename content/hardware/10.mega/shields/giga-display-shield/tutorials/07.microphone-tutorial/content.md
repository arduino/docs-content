---
title: GIGA Display Shield Microphone Guide
description: "Learn how to use the GIGA Display Shield's microphone with LVGL."
author: Benjamin Dannegård
tags: [Display, microphone, LVGL]
---

The GIGA Display Shield comes equipped with on-board microphone and with the help of LVGL the microphones readings can be visualized on the screen. This tutorial will show you how to create a sketch that ties together the microphones readings with visual elements on the screen.

## Hardware & Software Needed

- [Arduino GIGA R1 WiFi](/hardware/giga-r1)
- [Arduino GIGA Display Shield](/hardware/giga-display-shield)
- [Arduino IDE](https://www.arduino.cc/en/software)
- [LVGL library](https://reference.arduino.cc/reference/en/libraries/lvgl/)

## Downloading the Library and Core

Make sure the latest GIGA core is installed in the Arduino IDE. **Tools > Board > Board Manager...**. Here you need to look for the **Arduino Mbed OS Giga Boards** and install it, the [Arduino_H7_Video library](https://github.com/arduino/ArduinoCore-mbed/tree/main/libraries/Arduino_H7_Video) and [PDM library](https://docs.arduino.cc/learn/built-in-libraries/pdm) are included in the core. Now you have to install the library needed for handling the visual component. Go to **Tools > Manage libraries..**, search for **LVGL**, and install it.

## Microphone Readings With The Shield

### Test Microphone

To test the microphone we can use the **PDMSerialPlotter** example sketch. This sketch can be found in **File > Examples > PDM** in the Arduino IDE. This sketch will print readings in the serial monitor. Upload the sketch and check so that readings are appearing in the serial monitor.

![Example sketch printing values in the serial monitor](assets/pdm-test-sketch.png)

### Using the Microphone Readings

Now let's create a sketch that combines the microphone readings with a visual component. First, the libraries we need are, `PDM.h` which will handle the microphone readings and `lvgl.h` will handle the visual elements on the screen.

```arduino
#include <PDM.h>
#include "Arduino_H7_Video.h"
#include "lvgl.h"
```

In the `setup()` we can start the display with `Display.begin();` and the microphone with `PDM.onReceive(onPDMdata);`. This will call the `void onPDMdata()` function at the bottom of the sketch. This function handles collecting and storing the readings from the microphone.

```arduino
void setup() {
  Display.begin();

  PDM.onReceive(onPDMdata);

  if (!PDM.begin(channels, frequency)) {
    Serial.println("Failed to start PDM!");
    while (1);
  }
}
```

In the `setup()` we will also create our LVGL bar and animation for that bar. Make sure you also define the `lv_obj_t * obj;` and `lv_anim_t a;` variables outside of the `setup()` function so they can be used in the `loop()` function later. Now `obj` will be the name of bar object. These next lines will set the bar's position, size and values. After that we can initialize the animation and set the time for the animation. Then we set the animation to our bar with `lv_anim_set_var(&a, obj);`.

```arduino
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
```

The microphone readings will be put into a buffer, in the `loop()` we will need to go through all the samples in the buffer. We can do this with a simple `for()` loop. If you ran the previous mic test sketch you will know that the readings can get pretty high in value, to make it fit our LVGL component reduce that value. By assigning the value to our `micValue` variable we can make it fit the visual element and easily use it to set the end value of the animation with `lv_anim_set_values(&a, 0, micValue)`.

```arduino
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
```

In the section below you can find the full sketch. If you upload it to your GIGA Display Shield, you should see the same result as the GIF below is showing.

[GIF of sketch running]()

### Full Sketch

You will find the full sketch in the example below:

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

## Conclusion

Now you know how to get readings from the GIGA Display Shield's on-board microphone and how to create simple visual elements with LVGL. And lastly, how these two components could be put together in a sketch to utilize the shield's screen and on-board components.

## Next Step
Now that you know how to use the on-board microphone, feel free to explore the shield's other features, like the IMU with our [Orientation tutorial](/tutorials/image-orientation). Or if you rather dive deeper into LVGL, take a look at our [LVGL guide](tutorials/lvgl-guide).