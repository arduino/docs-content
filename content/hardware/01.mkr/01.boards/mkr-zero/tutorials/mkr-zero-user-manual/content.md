---
title: 'MKR Zero User Manual'
difficulty: beginner
compatible-products: []
description: ''
tags:
  - Cheat sheet
  - User manual
author: 'Benjamin Dannegård'
hardware:
  - hardware/
software:
  - ide-v1
  - ide-v2
  - web-editor
---

This user manual provides a comprehensive overview of the MKR Zero board, highlighting its hardware and software elements. With it, you will learn how to set up, configure, and use all the main features of a MKR Zero board.

![ ](assets/hero-banner.png)

## Hardware and Software Requirements

### Hardware Requirements

- [Arduino MKR Zero](https://store.arduino.cc/products/arduino-mkr-zero-i2s-bus-sd-for-sound-music-digital-audio-data)
- [USB-B® cable](https://store.arduino.cc/products/usb-cable-type-a-male-to-micro-type-b-male)

### Software Requirements

- [Arduino IDE 2.0+](https://www.arduino.cc/en/software) or [Arduino Web Editor](https://create.arduino.cc/editor)
- [SD library](https://docs.arduino.cc/libraries/sd/)
- [Arduino SAMD boards core](https://github.com/arduino/ArduinoCore-samd) (required to work with the MKR Zero board)

## Maker Zero Overview

The MKR ZERO brings you the power of a Zero in the smaller format established by the MKR form factor. The MKR ZERO board acts as a great educational tool for learning about 32-bit application development. It has an on-board SD connector with dedicated SPI interfaces (SPI1) that allows you to play with MUSIC files with no extra hardware!  The board is powered by Atmel’s SAMD21 MCU, which features a 32-bit ARM® Cortex® M0+ core.

![ ](assets/front_page.png)

The board contains everything needed to support the microcontroller; simply connect it to a computer with a micro-USB cable or power it by a LiPo battery. The battery voltage can also be monitored since a connection between the battery and the analog converter of the board exists.

### Board Libraries

The [`SD` library](https://www.arduino.cc/reference/en/libraries/sd/) enables reading and writing on SD cards. Once an SD memory card is connected to the SPI interface of the Arduino board you can create files and read/write on them. You can also move through directories on the SD card.

To install the `SD` library, navigate to `Tools > Manage libraries...` or click the **Library Manager** icon in the left tab of the Arduino IDE. In the Library Manager tab, search for `SD` and install the latest version of the library.

![Installing the board's library in the Arduino IDE](assets/user-manual-3.png)

### Pinout

The full pinout is available and downloadable as PDF from the link below:

- [MKR Zero pinout](https://docs.arduino.cc/resources/pinouts/ABX00012-full-pinout.pdf)

### Tech Specs

The tech specs are available from the link below:

- [MKR Zero tech specs](https://docs.arduino.cc/hardware/mkr-zero/#tech-specs)

### Schematics

The complete schematics are available and downloadable as PDF from the link below:

- [MKR Zero schematics](https://docs.arduino.cc/resources/schematics/ABX00012-schematics.pdf)

## First Use

### Connecting the Board

As shown in the image below, the Nicla Sense Env can be connected to a Portenta or MKR family board using the onboard ESLOV connector and the included ESLOV cable. Alternatively, you can connect the Nicla Sense Env as a shield by using the MKR-style pins on the Portenta or MKR family boards.

![Connecting the Nicla Sense Env](assets/user-manual-23.png)

For other compatible boards, such as those from the Nano family, the Nicla Sense Env can also be connected using the 2.54 mm pins of the Nicla Sense Env board.

### Powering the Board

The Nicla Sense Env can be powered by:

- Using the onboard **ESLOV connector**, which has a dedicated +5 VDC power line regulated onboard to +3.3 VDC.
- Using an **external +3.3 VDC power supply** connected to the `VCC` pin (please refer to the [board pinout section](#pinout) of the user manual).

### Blink Example

Let's control the MKR Zero board to reproduce the classic `blink` example used in the Arduino ecosystem. We will use this example to verify the MKR Zero board's connection to the Arduino IDE.

Now, connect the host board to your computer using a USB-B® cable, open the Arduino IDE, and connect the board to it.

Copy and paste the example sketch below into a new sketch in the Arduino IDE: 

```arduino

```

To upload the sketch to the host board, click the **Verify** button to compile the sketch and check for errors, then click the **Upload** button to program the device with the sketch.

![Uploading a sketch to the board in the Arduino IDE](assets/user-manual-7.png)

You should see the onboard orange LED of your Nicla Sense Env board turn on for one second, then off for one second, repeatedly.

### SD card example



### Low Power Mode Management

Saving energy is vital for many projects, particularly those deployed in remote areas or with a limited power supply. The Nicla Sense Env supports a deep sleep mode that can help to minimize the board's power consumption.

***Deep sleep is essential for extending battery life and minimizing energy consumption when the board is not collecting data or performing tasks. It is necessary for battery-powered or power-constrained applications.***

The example sketch shown below demonstrates how to put the Nicla Sense Env board into deep sleep mode using the `Arduino_NiclaSenseEnv` library API: 

```arduino
/**
  Low Power Mode Management Example for Nicla Sense Env
  Name: nicla_sense_env_low_power_mode_example.ino
  Purpose: This sketch demonstrates how to put the Nicla Sense Env 
  into deep sleep mode using the Arduino_NiclaSenseEnv library API.
  
  @author Arduino Product Experience Team
  @version 1.0 31/05/24
*/

// Include the NiclaSenseEnv library
#include "NiclaSenseEnv.h"

// Global device object for Nicla Sense Env
NiclaSenseEnv device;

void setup() {
    // Initialize serial communication and wait up to 2.5 seconds for a connection
    Serial.begin(115200);
    for (auto startNow = millis() + 2500; !Serial && millis() < startNow; delay(500));

    if (device.begin()) {
        // Putting the device to sleep
        Serial.println("- Going to deep sleep mode...");
        device.deepSleep();
    } else {
        Serial.println("- Device could not be found. Please double-check the wiring!");
    }
}

void loop() {
    // Nothing to do here. The device is in deep sleep mode.
}
```

Here is a detailed breakdown of the example sketch shown before and the `Arduino_NiclaSenseEnv` library API functions used in the sketch:

- `device.deepSleep()`: This function puts the Nicla Sense Env board into a deep sleep state, minimizing power consumption to the lowest possible level.

After uploading the example sketch to the host board, you should see the following output in the Arduino IDE's Serial Monitor:

![Example sketch output in the Arduino IDE's Serial Monitor](assets/user-manual-12.png)

***Waking up a Nicla Sense Env board from deep sleep mode can only be done by a hardware reset.***

You can download the example sketch [here](assets/nicla_sense_env_low_power_mode_example.zip).

## Support

If you encounter any issues or have questions while working with your MKR Zero board, we provide various support resources to help you find answers and solutions.

### Help Center

Explore our Help Center, which offers a comprehensive collection of articles and guides for MKR family boards. The Help Center is designed to provide in-depth technical assistance and help you make the most of your device.

- [MKR family help center page](https://support.arduino.cc/hc/en-us/sections/360004641919-MKR-Family)

### Forum

Join our community forum to connect with other MKR family board users, share your experiences, and ask questions. The Forum is an excellent place to learn from others, discuss issues, and discover new ideas and projects related to the MKR Zero.

- [MKR category in the Arduino Forum](https://forum.arduino.cc/c/official-hardware/mkr-boards/79)

### Contact Us

Please get in touch with our support team if you need personalized assistance or have questions not covered by the help and support resources described before. We're happy to help you with any issues or inquiries about the MKR family boards.

- [Contact us page](https://www.arduino.cc/en/contact-us/)