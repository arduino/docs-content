---
title: Microphone Tutorial
description: "Learn how to use the GIGA Display Shield's microphone."
author: Benjamin Dannegård
tags: [Display, microphone, LVGL]
---



## Hardware & Software Needed

- [Arduino GIGA R1 WiFi](/hardware/giga-r1)
- [Arduino GIGA Display Shield]()
- [Arduino IDE](https://www.arduino.cc/en/software)
- [LVGL library](https://reference.arduino.cc/reference/en/libraries/lvgl/)

## Downloading the Library and Core

Make sure the latest GIGA Core is installed in the Arduino IDE. **Tools > Board > Board Manager...**. Here you need to look for the **Arduino Mbed OS Giga Boards** and install it, the [Arduino_H7_Video library](https://github.com/arduino/ArduinoCore-mbed/tree/main/libraries/Arduino_H7_Video) is included in the core. Now you have to install the library needed for handling the image. Go to **Tools > Manage libraries..**, search for **LVGL**, and install it. This library will be used for the visual elements.

## Getting Microphone Readings

### Microphone Test Sketch

To test the microphone we can use the **PDMSerialPlotter** example sketch. This sketch can be found in **File > Examples > PDM** in the Arduino IDE. This sketch will print readings in the serial monitor. Upload the sketch and check so that readings are appearing in the serial monitor.

![]()


## Using the Microphone Readings

Now we can combine these readings with LVGL elements to visualize the readings. First, the libraries we need are:

```arduino

```


Creating the screen elements that will hold the bar that will react to the microphone readings.

```arduino
#include <PDM.h>
#include "Arduino_H7_Video.h"
#include "lvgl.h"
```

`PDM.h` will handle the microphone readings and `lvgl.h` will handle the visual elements on the screen.

Then we can create the bar:

```arduino
```

Now we have to include the microphone readings in the sketch:

```arduino
```

And lastly make the visual elements react to the readings:

```arduino
```

### Full Sketch

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
      //lastmicValue = micValue;
    }

    // Clear the read count
    samplesRead = 0;
    delay(100);
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
