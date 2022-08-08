---
title: "Saving Images as Bitmaps Into the SD Card"
difficulty: easy
tags: [Camera, Bitmap, SD Card]
description: This tutorial shows you how to capture a frame from the Portenta Vision Shield Camera module and save the output as a bitmap image.
author: Pablo Marquínez
libraries:
  - name: Arduino_Pro_Tutorials
    url: https://github.com/arduino-libraries/Arduino_Pro_Tutorials
hardware:
  - hardware/04.pro/boards/portenta-h7
  - hardware/04.pro/shields/portenta-vision-shield
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
- 1x USB-C cable (either USB-A to USB-C or USB-C to USB-C)
- Micro SD card
- Arduino IDE or Arduino-cli

## Instructions

### 1. The Setup
Connect the Vision Shield to your Portenta H7 as shown in the figure. The top and bottom high density connectors are connected to the corresponding ones on the underside of the H7 board. Plug in the H7 to your computer using the USB C cable.

![Connecting the Vision Shield to Portenta](assets/vs_ard_gs_attach_boards.svg)

#### The Camera

You will be using the **Himax HM-01B0 camera module** which has a resolution of 320 by 240 and the output data its in grayscale with 8 bits per pixel (bpp), this is important to have in mind as the `.bmp` (bitmap) format has some needed configuration depending on the data being used.

Inside the sketch you can use these libraries to access the camera APIs, also compatible with the [Arduino Nicla Vision](hardware/nicla-vision)
```cpp
#include "camera.h" // Arduino Mbed Core Camera APIs
#include "himax.h"  // Exclusive Camera library for the Portenta Vision Shield  //Only for the Vision Shield
```

#### Bitmap File Format

The bitmap binary file needs to contain some information in order to tell the computer some required information, for example the resolution of the picture and the bit-depth (bpp). Bit depth refers to the color information stored in the image. The higher the bit depth of an image, the more colors it can store. As the bit depth increases, the file size of the image also increases because more color information has to be stored for each pixel in the image.

The following table shows all the headers, the size of its buffer, offsets, the settings that we used and a details column:

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
#include "SDMMCBlockDevice.h"   // Multi Media Card APIs
#include "FATFileSystem.h"      // Mbed API for portable  and embedded systems

#include "camera.h" // Arduino Mbed Core Camera APIs
#include "himax.h"  // Exclusive Camera library for the Portenta Vision Shield
```

Then we define the following objects with their respective constructor (`blockDevice` and `fileSystem` objects), needed for getting access to the SD Card and the file system.

```cpp
#include "SDMMCBlockDevice.h"   // Multi Media Card APIs
#include "FATFileSystem.h"      // Mbed API for portable  and embedded systems
SDMMCBlockDevice blockDevice;
mbed::FATFileSystem fileSystem("fs");

#include "camera.h" // Arduino Mbed Core Camera APIs
#include "himax.h"  // Exclusive Camera library for the Portenta Vision Shield
HM01B0 himax;
Camera cam(himax);
```

For the bitmap headers binary file we will need some information like the resolution of the image, the bits per pixel and more, so we define our settings as shown:
```cpp
// Settings for our setup
#define RES_H (unsigned int)240
#define RES_W (unsigned int)320
#define IMAGE_MODE CAMERA_GRAYSCALE
#define IMAGE_BPP (unsigned int)8
// Headers info
#define HEADER_FILE_HEADER (unsigned int)14
#define HEADER_DIB_SIZE (unsigned int)40
#define HEADER_FULL_SIZE (HEADER_FILE_HEADER + HEADER_DIB_SIZE)
#define PALETTE_SIZE (2 ^ IMAGE_BPP) * 4 // 4 bytes per color
```

To mount the SD Card we will use the following function in the sketch:
```cpp
// Mount File system block
void mountSD()
{
    Serial.println("Mounting SD Card...");

    int error = fileSystem.mount(&blockDevice);
    if (error)
    {
        Serial.println("No SD Card found");
        while (1)
            ;
    }
}
```

Another function that the sketch contains is the one to generate the `.bmp` file called `parseData()`.
This function will create the needed headers that we will need later to encode our bitmap into a file.

***Take a look at the section [Bitmap File Format](#bitmap-file-format) to better understand the file headers that are created with this function***

```cpp
void parseData()
{
    unsigned char *imgData = NULL;
    int fileSize = HEADER_FILE_HEADER + RES_W * RES_H;

    FILE *file = fopen("/fs/image.bmp", "w+");

    // Get a Frame
    if (cam.grabFrame(fb, 3000) == 0)
    {
        // Save the raw image data (8bpp grayscale)
        imgData = fb.getBuffer();
    }
    else
    {
        Serial.println("could not grab the frame");
        while (1)
            ;
    }
    // Bitmap structure (Head + DIB Head + ColorMap + binary image)
    unsigned char bitmapFileHeader[HEADER_FILE_HEADER];
    unsigned char bitmapDIBHeader[HEADER_DIB_SIZE];
    unsigned char colorMap[PALETTE_SIZE]; // Needed for <=8bpp grayscale bitmaps

    // Set the file headers to 0
    memset(bitmapFileHeader, (unsigned char)(0), HEADER_FILE_HEADER);
    memset(bitmapDIBHeader, (unsigned char)(0), HEADER_DIB_SIZE);
    memset(colorMap, (unsigned char)(0), PALETTE_SIZE);

    // Write the headers info
    // File header
    bitmapFileHeader[0] = 'B';
    bitmapFileHeader[1] = 'M';
    bitmapFileHeader[2] = (unsigned char)(fileSize);
    bitmapFileHeader[3] = (unsigned char)(fileSize >> 8);
    bitmapFileHeader[4] = (unsigned char)(fileSize >> 16);
    bitmapFileHeader[5] = (unsigned char)(fileSize >> 24);
    bitmapFileHeader[10] = (unsigned char)HEADER_FULL_SIZE + PALETTE_SIZE;

    // Info header
    bitmapDIBHeader[0] = (unsigned char)(HEADER_DIB_SIZE);
    bitmapDIBHeader[4] = (unsigned char)(RES_W);
    bitmapDIBHeader[5] = (unsigned char)(RES_W >> 8);
    bitmapDIBHeader[8] = (unsigned char)(RES_H);
    bitmapDIBHeader[8] = (unsigned char)(RES_H >> 8);
    bitmapDIBHeader[14] = (unsigned char)(IMAGE_BPP);

    // Color palette for grayscale Bitmaps (8bpp)
    for (int i = 0; i < (2 ^ IMAGE_BPP); i++)
    {
        colorMap[i * 4] = i;
        colorMap[i * 4 + 1] = i;
        colorMap[i * 4 + 2] = i;
    }

    // Write theh bitmap file
    fwrite(bitmapFileHeader, 1, HEADER_FILE_HEADER, file);
    fwrite(bitmapDIBHeader, 1, HEADER_DIB_SIZE, file);
    fwrite(colorMap, 1, PALETTE_SIZE, file); // Color map
    fwrite(imgData, 1, RES_H * RES_W, file);

    // Close the stream (bitmap file)
    fclose(file);
}
```

The `setup()` will Initialize the Serial monitor, mount the SD Card, initialize the camera module and parse the image data into the bitmap with its needed headers.

```cpp
void setup()
{
    Serial.begin(115200);
    while (!Serial)
        ;

    // Mount SD Card
    mountSD();

    // Init the cam QVGA, 30FPS, Grayscale
    if (!cam.begin(CAMERA_R320x240, IMAGE_MODE, 30))
    {
        Serial.println("Unable to find the camera");
    }

    // Save the headers and the image data into the .bmp file
    parseData();
}
```

The `loop()` is empty, as it only does one shot once the Serial monitor is open.

### 3. Upload the Sketch

Select the right serial port on your IDE and upload the Arduino sketch to your H7. After a successful upload.

### 4. Try It Out

Insert a micro SD Card into the Portenta Vision Shield.

Connect the Portenta Vision shield to the Portenta H7.

Once the sketch is uploaded, open the Serial monitor, you should see that everything is fine and the capture has been taken.

Once the capture is saved, remove the SD Card and plug it into a computer/phone with an SD Card reader, open the storage unit and look for a bitmap called `image.bmp` then open it to check the result, you will be able to see a grayscale image on your device's image viewer.

![Output bitmap example](assets/output-view.png)

#### Full Sketch

```cpp
#include "SDMMCBlockDevice.h"   // Multi Media Card APIs
#include "FATFileSystem.h"      // Mbed API for portable  and embedded systems
SDMMCBlockDevice blockDevice;
mbed::FATFileSystem fileSystem("fs");

#include "camera.h" // Arduino Mbed Core Camera APIs
#include "himax.h"  // Exclusive Camera library for the Portenta Vision Shield
HM01B0 himax;
Camera cam(himax);

// Settings for our setup
#define RES_H (unsigned int)240
#define RES_W (unsigned int)320
#define IMAGE_MODE CAMERA_GRAYSCALE
#define IMAGE_BPP (unsigned int)8
// Headers info
#define HEADER_FILE_HEADER (unsigned int)14
#define HEADER_DIB_SIZE (unsigned int)40
#define HEADER_FULL_SIZE (HEADER_FILE_HEADER + HEADER_DIB_SIZE)
#define PALETTE_SIZE (2 ^ IMAGE_BPP) * 4 // 4 bytes per color

void setup()
{
    Serial.begin(115200);
    while (!Serial)
        ;

    // Mount SD Card
    mountSD();

    // Init the cam QVGA, 30FPS, Grayscale
    if (!cam.begin(CAMERA_R320x240, IMAGE_MODE, 30))
    {
        Serial.println("Unable to find the camera");
    }

    // Save the headers and the image data into the .bmp file
    parseData();
}

void loop()
{
    while (1)
        ;
}

// Mount File system block
void mountSD()
{
    Serial.println("Mounting SD Card...");

    int error = fileSystem.mount(&blockDevice);
    if (error)
    {
        Serial.println("No SD Card found");
        while (1)
            ;
    }
}

void parseData()
{
    unsigned char *imgData = NULL;
    int fileSize = HEADER_FILE_HEADER + RES_W * RES_H;

    FILE *file = fopen("/fs/image.bmp", "w+");

    // Get a Frame
    if (cam.grabFrame(fb, 3000) == 0)
    {
        // Save the raw image data (8bpp grayscale)
        imgData = fb.getBuffer();
    }
    else
    {
        Serial.println("could not grab the frame");
        while (1)
            ;
    }
    // Bitmap structure (Head + DIB Head + ColorMap + binary image)
    unsigned char bitmapFileHeader[HEADER_FILE_HEADER];
    unsigned char bitmapDIBHeader[HEADER_DIB_SIZE];
    unsigned char colorMap[PALETTE_SIZE]; // Needed for <=8bpp grayscale bitmaps

    // Set the file headers to 0
    memset(bitmapFileHeader, (unsigned char)(0), HEADER_FILE_HEADER);
    memset(bitmapDIBHeader, (unsigned char)(0), HEADER_DIB_SIZE);
    memset(colorMap, (unsigned char)(0), PALETTE_SIZE);

    // Write the headers info
    // File header
    bitmapFileHeader[0] = 'B';
    bitmapFileHeader[1] = 'M';
    bitmapFileHeader[2] = (unsigned char)(fileSize);
    bitmapFileHeader[3] = (unsigned char)(fileSize >> 8);
    bitmapFileHeader[4] = (unsigned char)(fileSize >> 16);
    bitmapFileHeader[5] = (unsigned char)(fileSize >> 24);
    bitmapFileHeader[10] = (unsigned char)HEADER_FULL_SIZE + PALETTE_SIZE;

    // Info header
    bitmapDIBHeader[0] = (unsigned char)(HEADER_DIB_SIZE);
    bitmapDIBHeader[4] = (unsigned char)(RES_W);
    bitmapDIBHeader[5] = (unsigned char)(RES_W >> 8);
    bitmapDIBHeader[8] = (unsigned char)(RES_H);
    bitmapDIBHeader[8] = (unsigned char)(RES_H >> 8);
    bitmapDIBHeader[14] = (unsigned char)(IMAGE_BPP);

    // Color palette for grayscale Bitmaps (8bpp)
    for (int i = 0; i < (2 ^ IMAGE_BPP); i++)
    {
        colorMap[i * 4] = i;
        colorMap[i * 4 + 1] = i;
        colorMap[i * 4 + 2] = i;
    }

    // Write theh bitmap file
    fwrite(bitmapFileHeader, 1, HEADER_FILE_HEADER, file);
    fwrite(bitmapDIBHeader, 1, HEADER_DIB_SIZE, file);
    fwrite(colorMap, 1, PALETTE_SIZE, file); // Color map
    fwrite(imgData, 1, RES_H * RES_W, file);

    // Close the stream (bitmap file)
    fclose(file);
}
```

## Conclusion

In this tutorial you learned how to capture the frames from your Vision Shield's Camera in the Arduino IDE, encode it with the bitmap standards and save it to an SD Card. 

## Next Steps

With this sketch format, you could easily add some code in the `loop()` in order to capture 1 new frame each second and save it with a name, for example `image<time/count>.bmp`