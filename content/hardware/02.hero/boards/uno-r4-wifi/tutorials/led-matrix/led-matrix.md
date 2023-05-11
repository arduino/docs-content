---
title: 'Using the Arduino UNO R4 WiFi LED matrix.'
description: 'Get off the ground with the Arduino UNO R4 WiFi's built in LED matrix. Learn the different techniques for controlling it, create animations, graphics or even games.'
tags:
  - Guide
  - LED Matrix
author: 'Jacob Hylén'
hardware:
  - hardware/02.hero/boards/uno-r4-wifi
software:
  - ide-v1
  - ide-v2
  - web-editor
---

The **Arduino UNO R4 WiFi** comes with a built in 12x8 LED Matrix, that is available to be programmed to display graphics, animations, act as an interface, or even play games on. 

## Goals

The matrix and its' API is developed to be programmed in a few different ways, each suited for different applications. This guide will walk you through the basic concepts for programming the LED matrix, and get you started with creating your own animations. While highlighting two different ways of handling the LEDs to create animations and images. Making it easier for you to decide what method fits your needs best!

## Hardware & Software Needed
To follow along with this guide, you will of course need:
- an [Arduino UNO R4 WiFi](https://store.arduino.cc/products/arduino-uno-r4-wifi),
- and the [Arduino IDE](https://www.arduino.cc/en/software).

## Initializing Matrix

```
#include "Arduino_LED_Matrix.h"

ArduinoLEDMatrix matrix;

void setup() {
  Serial.begin(115200);
  matrix.begin();
}
```


## How to Write a Frame
The LED matrix library for the UNO R4 WiFi works on the principle of creating a frame, and then loading it into a buffer which displays the frame.

How this frame is created can vary quite a lot, and you can choose whatever way is the easiest for your application, but most of the time you'll be creating an array that holds the frame in 3 32bit integers. A frame like this is difficult for a person to interpret, but it is efficient and therefore the way to go if you're making animations or graphics to display states of a program or interfaces. You can create frames and animations such as this one by using tools such as [FotogramMatrice](#fotogrammatrice). Such a frame may look similar to this:

```
const uint32_t heart[] = {
	0x3184a444,
	0x44042081,
	0x100a0040
};
```

Now if you've got several different frames, you can load and display them like this:
```
const uint32_t happy[] = {
	0x19819,
	0x80000001,
	0x81f8000
};

const uint32_t heart[] = {
	0x3184a444,
	0x44042081,
	0x100a0040
};

matrix.loadFrame(happy);
  delay(500);
  matrix.loadFrame(heart);
  delay(500);
```


You may also represent your frame with an array of individual bits, where each pixel is represented by a bit, and can be accessed by its row and column(this way being a good choice if you need to generate frames from within a sketch, for instance if you are making a game). This `frame` array contains a representation of each pixel in the matrix laid out in the same 12x8 grid.

```
uint8_t frame[8][12] = {
  { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
  { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
  { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
  { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
  { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
  { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
  { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
  { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 }
};

```
To target an individual pixel you select its' address and change the value, remember that you'll need to start counting at 0. So, the following line will target the third pixel from the left and the second from the top, then turn it on:
```
frame[2][1] = 1;
matrix.renderBitmap(frame, 8, 12);
```

## FotogramMatrice
The FotogramMatrice tool is used to generate frames and animations to be rendered on the LED matrix. 

It also features a live preview of the frames you're creating displayed right on the LED matrix of the Arduino UNO R4 WiFi, although this is only supported in Google Chrome. 
// THIS PART IS UNFINISHED, waiting to learn where the live preview sketch will be hosted.

With the live preview sketch loaded on your board, connect the port to the browser, and watch as the pixels turn on and off as you edit the grid in your browser. 

// waiting for the interface to be developed 

## Conclusion
In this article we've gone over the basics of using the LED matrix built in on the Arduino UNO R4 WiFi, we've gone over the differnet practices for building frames and animations, as well as how to load them onto your board. 

Have fun creating interactive interfaces or animation on your UNO R4 WiFi!

## API 

 Members                        | Descriptions                                
--------------------------------|---------------------------------------------
`public ` [`ArduinoLEDMatrix`](#)`()` | The main class for controlling the LED matrix.
`public void` [`autoscroll`](#)`(int32_t interval_ms)` | Sets the time in ms for each frame to be displayed
`public void` [`on`](#)`(size_t pin)` | Turn an individual pixel on.
`public void` [`off`](#)`(size_t pin)` | Turn an individual pixel off.
`public void` [`begin`](#)`()` | Start the LED matrix.
`public void` [`next`](#)`()` | Manually move to the next frame in the sequence.
`public void` [`loadFrame`](#)`(const uint32_t buffer[3])` | Load a new single frame that is not in any sequence.
`public void` [`renderFrame`](#)`(uint8:t frameNumber)` | Render the loaded frame.
`public void` [`play`](#)`(bool loop = false)` | Start playing the sequence of frames, with the option to loop indefinetly or play once.
`public bool` [`sequenceDone`](#)`()` | checks if the sequence has finished playing.
`public void` [`loadPixels`](#)`(uint8_t *arr, size_t size)` |Loads the pixels into the buffer but does not display them.
`public void` [`loadWrapper`](#)`(`[`const uint32_t frames[][4], uint32_t howMany`](#)` callback)` | Sets the current frame to number 0 in the sequence.

## Members

### `public ` [`ArduinoLEDMatrix`](#)`()` 

Construct a new [LEDMatrix](#) object.

### `public void` [`autoscroll`](#)`(int32_t interval_ms)` 

Enable autoscrolling through the frames in a sequence. 

#### Parameters
* `interval_ms` Sets the time in milliseconds that should be spent on a frame before switching to the next frame in the sequence.


### `public void` [`on`](#)`(size_t pin)` 

Turn on an individual LED.

#### Parameters
* `pin` Defines which LED should be turned on. Accepted values are 0-95. 
### `public void` [`off`](#)`(size_t pin)` 

Turn off an individual LED.

#### Parameters
* `pin` Defines which LED should be turned off. Accepted values are 0-95. 

### `public void` [`begin`](#)`()` 

Starts the LED matrix.

### `public void` [`next`](#)`()` 

Manually moves to the next frame in the sequence.

### `public void` [`loadFrame`](#)`(const uint32_t buffer[3])` 
 
loads a single frame that is not part of a sequence.
 
#### Parameters
* `buffer[3]` an array of three 32bit integers, where each bit represents an LED.  

### `public void` [`renderFrame`](#)`(uint8_t frameNumber)` 

Render a specific frame from a sequence

#### Parameters
* `frameNumber` Specifies which frame of the sequence should be rendered. 

### `public void` [`play`](#)`(bool loop)` 

Starts playing the loaded sequence. 

#### Parameters
* `loop` true to enable looping the sequence, false to play once.

### `public bool` [`sequenceDone`](#)`()` 

Check for if the sequence is finished playing or if the frame should be advanced another step.

#### Returns
false if the sequence is not finished, true if it is.

### `public void` [`loadPixels`](#)`(uint8_t *arr, size_t size)` 

Loads the pixels into the frame but does not load them.

#### Parameters
* `arr` Pointer to an array that holds the frame

* `size` the amount of pixels in your frame. 

### `public void` [`loadWrapper`](#)`(const uint32_t frames[][4], uint32_t howMany)` 

Sets the current frame to frame 0 in the sequence.