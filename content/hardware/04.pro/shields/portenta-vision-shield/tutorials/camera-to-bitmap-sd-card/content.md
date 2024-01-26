---
title: "Saving Bitmap Camera Images to the SD Card"
difficulty: beginner
tags: [Camera, Bitmap, SD Card]
description: This tutorial shows you how to capture a frame from the Portenta Vision Shield Camera module and save the output as a bitmap image.
author: Pablo Marquínez
libraries:
  - name: Arduino_Pro_Tutorials
    url: https://github.com/arduino-libraries/Arduino_Pro_Tutorials
hardware:
  - hardware/04.pro/shields/portenta-vision-shield
  - hardware/04.pro/boards/portenta-h7
software:
  - ide-v1
  - ide-v2
  - web-editor
  - cli
---

## Overview
This tutorial shows you how to capture a frame from the Portenta Vision Shield Camera module and save the output as a bitmap image. It will allow you to see the output directly on your computer without using any third party tool.  

## Goals

- Capturing a frame from the camera.
- Make the bitmap binary file with the correct settings.
- Save the bitmap on an SD Card.
- Visualize the captured image on your computer.

### Required Hardware and Software

- [Portenta H7](https://store.arduino.cc/portenta-h7)
- Portenta Vision Shield ([LoRa](https://store.arduino.cc/portenta-vision-shield-lora) or [Ethernet](https://store.arduino.cc/portenta-vision-shield))
- 1x USB-C® cable (either USB-A to USB-C® or USB-C® to USB-C®)
- Micro SD card
- Arduino IDE or Arduino-cli

## Instructions

### 1. The Setup
Connect the Portenta Vision Shield to your Portenta H7 as shown in the figure. The top and bottom high density connectors are connected to the corresponding ones on the underside of the H7 board. Plug in the H7 to your computer using the USB-C® cable.

![Connecting the Portenta Vision Shield to Portenta](assets/vs_ard_gs_attach_boards.svg)

#### The Camera

You will be using the **Himax HM-01B0 camera module** which has a resolution of 320 by 240 and the output data its in grayscale with 8 bits per pixel (bpp). It is important to have this in mind as the `.bmp` (bitmap) format has some needed configuration depending on the data being used.

Inside the sketch, you can use these libraries to access the camera APIs, also compatible with the [Arduino Nicla Vision](https://docs.arduino.cc/hardware/nicla-vision)
```cpp
#include "camera.h" // Multi Media Card APIs
#include "himax.h"  // API to read from the Himax camera found on the Portenta Vision Shield
```

#### Bitmap File Format

The bitmap binary file needs to contain some information in order to tell the computer for example the resolution of the picture and the bit-depth (bpp). Bit depth refers to the color information stored in the image. The higher the bit depth of an image, the more colors it can store. As the bit depth increases, the file size of the image also increases, because more color information has to be stored for each pixel in the image.

The following table shows all the headers, the size of its buffer, offsets, the settings that are being used with their details:

| Name                | Size        | Details                                                      |
| ------------------- | ----------- | ------------------------------------------------------------ |
| DIB                 | 14 Bytes    | Bitmap information, setting the size of the file.            |
| File Header         | 40 Bytes    | This header requires the resolution and the bpp               |
| Palette (Color Map) | 1025 Bytes  | This header is mandatory on bitmaps with a bpp ≤ 8, setting the grayscale |
| Image data          | 76800 Bytes | The raw image data, in this case each pixel has 8 bits (1 Byte) and the resolution is 320 x 240, with no compression |

The final size of the file is **77.879 KB**.


### 2. The Sketch

You can find the sketch on the latest version of the [Arduino_Pro_Tutorials](https://github.com/arduino-libraries/Arduino_Pro_Tutorials) at `examples > Vision Shield to SD Card bmp > visionShieldBitmap.ino`

***You can see the full sketch in the [Full sketch section](#full-sketch)***

First you need to include the needed libraries
```cpp
#include "SDMMCBlockDevice.h" // Multi Media Card APIs
#include "FATFileSystem.h"    // Mbed API for portable  and embedded systems

#include "camera.h" // Arduino Mbed Core Camera APIs
#include "himax.h"  // API to read from the Himax camera found on the Portenta Vision Shield
```

Then define the following objects with their respective constructor (`blockDevice` and `fileSystem` objects), needed for getting access to the SD Card and the file system.

```cpp
#include "SDMMCBlockDevice.h" // Multi Media Card APIs
#include "FATFileSystem.h"    // API to run operations on a FAT file system
SDMMCBlockDevice blockDevice;
mbed::FATFileSystem fileSystem("fs");

#include "camera.h" // Arduino Mbed Core Camera APIs
#include "himax.h"  // API to read from the Himax camera found on the Portenta Vision Shield
HM01B0 himax;
Camera cam(himax);

FrameBuffer frameBuffer; // Buffer to save the camera stream
```

For the bitmap headers binary file you will need some information like the resolution of the image, the bits per pixel and more; so you can define your settings as shown:
```cpp
// Settings for our setup
#define IMAGE_HEIGHT (unsigned int)240
#define IMAGE_WIDTH (unsigned int)320
#define IMAGE_MODE CAMERA_GRAYSCALE
#define BITS_PER_PIXEL (unsigned int)8
#define PALETTE_COLORS_AMOUNT (unsigned int)(pow(2, BITS_PER_PIXEL))
#define PALETTE_SIZE  (unsigned int)(PALETTE_COLORS_AMOUNT * 4) // 4 bytes = 32bit per color (3 bytes RGB and 1 byte 0x00)
#define IMAGE_PATH "/fs/image.bmp"

// Headers info
#define BITMAP_FILE_HEADER_SIZE (unsigned int)14 // For storing general information about the bitmap image file
#define DIB_HEADER_SIZE (unsigned int)40 // For storing information about the image and define the pixel format
#define HEADER_SIZE (BITMAP_FILE_HEADER_SIZE + DIB_HEADER_SIZE)
```

The program has the following functions declared:
* `void mountSDCard()`
* `unsigned char * captureImage()`
* `void setFileHeaders(bitmapFileHeaders, bitmapDIBHeader, fileSize)`
* `void setColorMap(colorMap)`
* `saveImage(imageData, imagePath)`

To mount the SD Card you will use the following function in the sketch:
```cpp
// Mount File system block
void mountSDCard(){
    int error = fileSystem.mount(&blockDevice);
    if (error){
        Serial.println("Trying to reformat...");
        int formattingError = fileSystem.reformat(&blockDevice);
        if (formattingError) {            
            Serial.println("No SD Card found");
            while (1);
        }
    }
}
```

The function to capture the frame from the camera:
```cpp
// Get the raw image data (8bpp grayscale)
unsigned char * captureImage(){
    if (cam.grabFrame(frameBuffer, 3000) == 0){
        return frameBuffer.getBuffer();
    } else {
        Serial.println("could not grab the frame");
        while (1);
    }
}
```

To manipulate the file you will need to set the headers on the binary information as follows:
```cpp
// Set the headers data
void setFileHeaders(unsigned char *bitmapFileHeader, unsigned char *bitmapDIBHeader, int fileSize){
    // Set the headers to 0
    memset(bitmapFileHeader, (unsigned char)(0), BITMAP_FILE_HEADER_SIZE);
    memset(bitmapDIBHeader, (unsigned char)(0), DIB_HEADER_SIZE);

    // File header
    bitmapFileHeader[0] = 'B';
    bitmapFileHeader[1] = 'M';
    bitmapFileHeader[2] = (unsigned char)(fileSize);
    bitmapFileHeader[3] = (unsigned char)(fileSize >> 8);
    bitmapFileHeader[4] = (unsigned char)(fileSize >> 16);
    bitmapFileHeader[5] = (unsigned char)(fileSize >> 24);
    bitmapFileHeader[10] = (unsigned char)HEADER_SIZE + PALETTE_SIZE;

    // Info header
    bitmapDIBHeader[0] = (unsigned char)(DIB_HEADER_SIZE);
    bitmapDIBHeader[4] = (unsigned char)(IMAGE_WIDTH);
    bitmapDIBHeader[5] = (unsigned char)(IMAGE_WIDTH >> 8);
    bitmapDIBHeader[8] = (unsigned char)(IMAGE_HEIGHT);
    bitmapDIBHeader[9] = (unsigned char)(IMAGE_HEIGHT >> 8);
    bitmapDIBHeader[14] = (unsigned char)(BITS_PER_PIXEL);
}
```

***Take a look at the section [Bitmap File Format](#bitmap-file-format) to better understand the file headers that are created with this function***

In this case that our image (320x240) is 8 bits per pixel and grayscale on the bitmap rules you need to define the color table (color map) to assign an specific RGB color for our 8 bit color.
On the following function it sets the color map as a grayscale of RGB colors from [R:0x00 G:0x00 B:0x00] to [R:0xFF G:0xFF B:0xFF]
```cpp
void setColorMap(unsigned char *colorMap){
    //Init the palette with zeroes
    memset(colorMap, (unsigned char)(0), PALETTE_SIZE);
    
    // Gray scale color palette, 4 bytes per color (R, G, B, 0x00)
    for (int i = 0; i < PALETTE_COLORS_AMOUNT; i++) {
        colorMap[i * 4] = i;
        colorMap[i * 4 + 1] = i;
        colorMap[i * 4 + 2] = i;
    }
}
```

The function in charge to save the image will use the previous functions to set the headers and write the buffers into the file `image.bmp`
```cpp

// Save the headers and the image data into the .bmp file
void saveImage(unsigned char *imageData, const char* imagePath){
    int fileSize = BITMAP_FILE_HEADER_SIZE + DIB_HEADER_SIZE + IMAGE_WIDTH * IMAGE_HEIGHT;
    FILE *file = fopen(imagePath, "w");

    // Bitmap structure (Head + DIB Head + ColorMap + binary image)
    unsigned char bitmapFileHeader[BITMAP_FILE_HEADER_SIZE];
    unsigned char bitmapDIBHeader[DIB_HEADER_SIZE];
    unsigned char colorMap[PALETTE_SIZE]; // Needed for <= 8bpp grayscale bitmaps    

    setFileHeaders(bitmapFileHeader, bitmapDIBHeader, fileSize);
    setColorMap(colorMap);

    // Write the bitmap file
    fwrite(bitmapFileHeader, 1, BITMAP_FILE_HEADER_SIZE, file);
    fwrite(bitmapDIBHeader, 1, DIB_HEADER_SIZE, file);
    fwrite(colorMap, 1, PALETTE_SIZE, file);
    fwrite(imageData, 1, IMAGE_HEIGHT * IMAGE_WIDTH, file);

    // Close the file stream
    fclose(file);
}
```

Then to have visual feedback lets add a blink function to make 3 blinks after the photo is taken, once the blue LED is ON it means the picture was taken.
```cpp
void countDownBlink(){
    for (int i = 0; i < 6; i++){
        digitalWrite(LEDG, i % 2);
        delay(500);
    }
    digitalWrite(LEDG, HIGH);
    digitalWrite(LEDB, LOW);
}
```
Now that you have all the functions to be used, inside the `setup()` its call them only once after the board restarts.
```cpp
void setup(){
    Serial.begin(115200);
    while (!Serial && millis() < 5000);
    
    Serial.println("Mounting SD Card...");
    mountSDCard();
    Serial.println("SD Card mounted.");

    // Init the cam QVGA, 30FPS, Grayscale
    if (!cam.begin(CAMERA_R320x240, IMAGE_MODE, 30)){
        Serial.println("Unable to find the camera");
    }

    countDownBlink();
    Serial.println("Fetching camera image...");
    unsigned char *imageData = captureImage();
    
    Serial.println("Saving image to SD card...");
    saveImage(imageData, IMAGE_PATH);
    
    fileSystem.unmount();
    Serial.println("Done. You can now remove the SD card.");
}
```
The `loop()` is empty, as it only does one shot when the Serial Monitor is open or after 5 seconds passed after boot.

### 3. Upload the Sketch

Select the right serial port on your IDE and upload the Arduino sketch to your Portenta H7. 

### 4. Try It Out

Insert a micro SD Card into the Portenta Vision Shield.

Connect the Portenta Vision Shield to the Portenta H7.

Once the sketch is uploaded, open the Serial Monitor or wait 5 seconds: you should see that everything is fine and the capture has been taken.

Once the capture is saved, remove the SD Card and plug it into a computer/phone with an SD Card reader, open the storage unit, look for a bitmap called `image.bmp` and open it to check the result. You will be able to see a grayscale image on your device's image viewer.

![Output bitmap example](assets/output-view.png)

#### Full Sketch

```cpp
#include "SDMMCBlockDevice.h" // Multi Media Card APIs
#include "FATFileSystem.h"    // API to run operations on a FAT file system
SDMMCBlockDevice blockDevice;
mbed::FATFileSystem fileSystem("fs");

#include "camera.h" // Arduino Mbed Core Camera APIs
#include "himax.h"  // API to read from the Himax camera found on the Portenta Vision Shield
HM01B0 himax;
Camera cam(himax);

FrameBuffer frameBuffer; // Buffer to save the camera stream

// Settings for our setup
#define IMAGE_HEIGHT (unsigned int)240
#define IMAGE_WIDTH (unsigned int)320
#define IMAGE_MODE CAMERA_GRAYSCALE
#define BITS_PER_PIXEL (unsigned int)8
#define PALETTE_COLORS_AMOUNT (unsigned int)(pow(2, BITS_PER_PIXEL))
#define PALETTE_SIZE  (unsigned int)(PALETTE_COLORS_AMOUNT * 4) // 4 bytes = 32bit per color (3 bytes RGB and 1 byte 0x00)
#define IMAGE_PATH "/fs/image.bmp"

// Headers info
#define BITMAP_FILE_HEADER_SIZE (unsigned int)14 // For storing general information about the bitmap image file
#define DIB_HEADER_SIZE (unsigned int)40 // For storing information about the image and define the pixel format
#define HEADER_SIZE (BITMAP_FILE_HEADER_SIZE + DIB_HEADER_SIZE)


void setup(){
    Serial.begin(115200);
    while (!Serial && millis() < 5000);
    
    Serial.println("Mounting SD Card...");
    mountSDCard();
    Serial.println("SD Card mounted.");

    // Init the cam QVGA, 30FPS, Grayscale
    if (!cam.begin(CAMERA_R320x240, IMAGE_MODE, 30)){
        Serial.println("Unable to find the camera");
    }
    countDownBlink();
    Serial.println("Fetching camera image...");
    unsigned char *imageData = captureImage();
    digitalWrite(LEDB, HIGH);
    
    Serial.println("Saving image to SD card...");
    saveImage(imageData, IMAGE_PATH);
    
    fileSystem.unmount();
    Serial.println("Done. You can now remove the SD card.");
}

void loop(){
}

// Mount File system block
void mountSDCard(){
    int error = fileSystem.mount(&blockDevice);
    if (error){
        Serial.println("Trying to reformat...");
        int formattingError = fileSystem.reformat(&blockDevice);
        if (formattingError) {            
            Serial.println("No SD Card found");
            while (1);
        }
    }
}

// Get the raw image data (8bpp grayscale)
unsigned char * captureImage(){
    if (cam.grabFrame(frameBuffer, 3000) == 0){
        return frameBuffer.getBuffer();
    } else {
        Serial.println("could not grab the frame");
        while (1);
    }
}

// Set the headers data
void setFileHeaders(unsigned char *bitmapFileHeader, unsigned char *bitmapDIBHeader, int fileSize){
    // Set the headers to 0
    memset(bitmapFileHeader, (unsigned char)(0), BITMAP_FILE_HEADER_SIZE);
    memset(bitmapDIBHeader, (unsigned char)(0), DIB_HEADER_SIZE);

    // File header
    bitmapFileHeader[0] = 'B';
    bitmapFileHeader[1] = 'M';
    bitmapFileHeader[2] = (unsigned char)(fileSize);
    bitmapFileHeader[3] = (unsigned char)(fileSize >> 8);
    bitmapFileHeader[4] = (unsigned char)(fileSize >> 16);
    bitmapFileHeader[5] = (unsigned char)(fileSize >> 24);
    bitmapFileHeader[10] = (unsigned char)HEADER_SIZE + PALETTE_SIZE;

    // Info header
    bitmapDIBHeader[0] = (unsigned char)(DIB_HEADER_SIZE);
    bitmapDIBHeader[4] = (unsigned char)(IMAGE_WIDTH);
    bitmapDIBHeader[5] = (unsigned char)(IMAGE_WIDTH >> 8);
    bitmapDIBHeader[8] = (unsigned char)(IMAGE_HEIGHT);
    bitmapDIBHeader[9] = (unsigned char)(IMAGE_HEIGHT >> 8);
    bitmapDIBHeader[14] = (unsigned char)(BITS_PER_PIXEL);
}

void setColorMap(unsigned char *colorMap){
    //Init the palette with zeroes
    memset(colorMap, (unsigned char)(0), PALETTE_SIZE);
    
    // Gray scale color palette, 4 bytes per color (R, G, B, 0x00)
    for (int i = 0; i < PALETTE_COLORS_AMOUNT; i++) {
        colorMap[i * 4] = i;
        colorMap[i * 4 + 1] = i;
        colorMap[i * 4 + 2] = i;
    }
}

// Save the headers and the image data into the .bmp file
void saveImage(unsigned char *imageData, const char* imagePath){
    int fileSize = BITMAP_FILE_HEADER_SIZE + DIB_HEADER_SIZE + IMAGE_WIDTH * IMAGE_HEIGHT;
    FILE *file = fopen(imagePath, "w");

    // Bitmap structure (Head + DIB Head + ColorMap + binary image)
    unsigned char bitmapFileHeader[BITMAP_FILE_HEADER_SIZE];
    unsigned char bitmapDIBHeader[DIB_HEADER_SIZE];
    unsigned char colorMap[PALETTE_SIZE]; // Needed for <= 8bpp grayscale bitmaps    

    setFileHeaders(bitmapFileHeader, bitmapDIBHeader, fileSize);
    setColorMap(colorMap);

    // Write the bitmap file
    fwrite(bitmapFileHeader, 1, BITMAP_FILE_HEADER_SIZE, file);
    fwrite(bitmapDIBHeader, 1, DIB_HEADER_SIZE, file);
    fwrite(colorMap, 1, PALETTE_SIZE, file);
    fwrite(imageData, 1, IMAGE_HEIGHT * IMAGE_WIDTH, file);

    // Close the file stream
    fclose(file);
}

void countDownBlink(){
    for (int i = 0; i < 6; i++){
        digitalWrite(LEDG, i % 2);
        delay(500);
    }
    digitalWrite(LEDG, HIGH);
    digitalWrite(LEDB, LOW);
}
```

## Conclusion

In this tutorial you learned how to capture frames with your Portenta Vision Shield's Camera in the Arduino IDE, encode it with the bitmap standards and save it to an SD Card. 

## Next Steps

With this sketch format, you could easily add some code in the `loop()` in order to capture 1 new frame each second and save it with a name, for example `image<time/count>.bmp`.
