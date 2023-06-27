---
title: "SD Sketch Update "
description: "How to use the new Arduino SDU library for SAMD boards to update the sketch on your board, putting it on an SD!"
coverImage: "assets/full_sd_with_5v_bb_qeGy7GuPFG.jpg"
tags: [update, updating]
author: "Arduino_Genuino"
difficulty: beginner
source: "https://create.arduino.cc/projecthub/Arduino_Genuino/sd-sketch-update-534404"
---

## Components and Supplies

- [Arduino MKR1000](https://store.arduino.cc/arduino-mkr1000)
- [Arduino MKR Zero](/hardware/mkr-zero)
- SD card

## Apps and Online Services

- [Arduino Web Editor](https://create.arduino.cc/editor)
- [Arduino IDE](https://www.arduino.cc/en/main/software)

## About This Project

### SD Update

Executing an SD update using the SAMD SDU (Secure Digital Update) library is very easy! You simply have to include the SDU library with your sketch to gain access to this very cool feature.

The library includes the routine. This routine starts when the boards boot and search for a file on the SD called **UPDATE.bin**. If file is found, the current sketch on the board will be overwritten with the new one.

### What Do You Need?

* Arduino MKRZero
* SD card

or

* Arduino/Genuino MKR1000
* MKR SD Proto Shield
* SD card

or

* Arduino MKRFox1200
* MKR SD Proto Shield
* SD card

### Example

* First of all, open the blink example under File->Examples->01.Basics->Blink and modify it to include the OTA library like shown below.

```arduino
#include <SDU.h> 
// the setup function runs once when you press reset or power the board 
void setup() { 
 // initialize digital pin LED_BUILTIN as an output. 
 pinMode(LED_BUILTIN, OUTPUT); 
} 
// the loop function runs over and over again forever 
void loop() { 
 digitalWrite(LED_BUILTIN, HIGH);   // turn the LED ON
 delay(1000);                       // wait for a second 
 digitalWrite(LED_BUILTIN, LOW);    // turn the LED OFF
 delay(1000);                       // wait for a second 
```

* Upload it on the board
* Now modify the Blink code to have a faster LED in this way

```arduino
#include <SDU.h> 
// the setup function runs once when you press reset or power the board 
void setup() { 
 // initialize digital pin LED_BUILTIN as an output. 
 pinMode(LED_BUILTIN, OUTPUT); 
} 
// the loop function runs over and over again forever 
void loop() { 
 digitalWrite(LED_BUILTIN, HIGH);   // turn the LED ON
 delay(250);                        // wait for a second 
 digitalWrite(LED_BUILTIN, LOW);    // turn the LED OFF
 delay(250);                        // wait for a second 
} 
```

* Export the binary by clicking on Sketch->Export compiled Binary
* Go in the folder you chose to save your sketch and rename the .bin file in **UPDATE.bin**
* Put this file on the SD card and then insert it in the MKRZero or the MKR SD ProtoShield
* Reset the board

You should now see the **BUILTIN\_LED** that blinks faster so your sketch has been updated!