---
title: GIGA Display Shield emWin Guide
description: 'Learn to display RAW Images on the GIGA Display from USB Storage.'
author: Pedro Sousa Lima
tags: [Display, USB]
---

## Introduction

This guide explores how to read and display raw RGB565 images from a USB drive onto an Arduino GIGA Display Shield. Making it possible for you to list files from a USB drive, select an image, and render it.

![Display with image from USB](assets/image-example.png)

## Hardware Requirements

- [Arduino GIGA R1 WiFi](https://store.arduino.cc/products/giga-r1-wifi)
- [Arduino GIGA Display Shield](https://store.arduino.cc/products/giga-display-shield)
- USB mass storage device (formatted with FAT32)

## Software Requirements

- **USBHostMbed5** (for USB host functionality)
- **FATFileSystem** (to read files from USB)
- **ArduinoH7Video**(Included in the core) and [**ArduinoGraphics**](https://docs.arduino.cc/libraries/arduinographics/) libraries (for handling display rendering)

## Features

- Lists all files in the `/usb/` directory.
- Allows users to select an image via the Serial Monitor.
- Automatically reads and displays an **800x480 RGB565** image.
- Clears the display upon request.

## Preparing Your Image

To ensure your image is in the correct format (800x480, 16-bit RGB565), you can use an online converter such as the [**LVGL Image Converter**](https://lvgl.io/tools/imageconverter). Select **RGB565** as the output format and set the resolution to 800x480 before saving the file to your USB drive. Make sure the USB drive is formatted for FAT32.

## Code Breakdown

### Setting Up USB Host and Display

With the following code the USB host is initialized, enabling support for mass storage devices. The display is also set up using the `Arduino_H7_Video` class.

```cpp
USBHostMSD msd;
mbed::FATFileSystem usb("usb");
Arduino_H7_Video Display(800, 480, GigaDisplayShield);
```

### Listing Files on USB Storage

Once mounted, the USB drive is scanned for available files:

```cpp
void listRootDirectory() {
  fileCount = 0;
  DIR* dir = opendir("/usb/");
  if (!dir) return;
  while (true) {
    struct dirent* entry = readdir(dir);
    if (!entry || fileCount >= MAX_FILES) break;
    strncpy(fileNames[fileCount], entry->d_name, MAX_NAME_LEN - 1);
    fileCount++;
  }
  closedir(dir);
}
```

### Selecting an Image via Serial Input

Users can enter a file number in the Serial Monitor to select an image for display.

```cpp
void handleUserInput() {
  if (Serial.available() > 0) {
    int sel = Serial.parseInt();
    if (sel >= 1 && sel <= fileCount) {
      char path[256];
      snprintf(path, sizeof(path), "/usb/%s", fileNames[sel - 1]);
      displayRawRowByRow(path);
    }
  }
}
```

### Reading and Displaying RAW Images

The file is read row-by-row (800 pixels per row, 2 bytes per pixel). If the entire image (800x480 pixels) were loaded into memory at once, it would require approximately 768 KB of RAM (800 \* 480 \* 2 bytes). However, by processing only one row at a time (800 * 2 bytes), the memory usage is reduced to just `1.6 KB`, making this approach much more efficient and feasible for devices with restricted memory (like GIGA). This approach minimizes memory usage by processing smaller chunks of the image at one time, avoiding large allocations that may exceed available RAM (512 KB for the GIGA).
To manage this efficiently, we use `malloc()` and `free()` for dynamic memory allocation, ensuring that only the necessary amount of RAM is used rather than pre-allocating a large buffer. This approach helps optimize memory use while preventing fragmentation.
Similarly, `fopen()` and `fclose()` are used for file management. `fopen()` allows us to open the image file and read data as needed, rather than loading everything at once. `fclose()` ensures that the file is properly closed after reading, freeing up system resources and preventing potential memory leaks.


```cpp
bool displayRawRowByRow(const char* path) {
  FILE* f = fopen(path, "rb");
  if (!f) return false;

  uint8_t* rowBuffer = (uint8_t*) malloc(IMG_WIDTH * 2);
  if (!rowBuffer) {
    fclose(f);
    return false;
  }

  Display.beginDraw();
  for (int y = 0; y < IMG_HEIGHT; y++) {
    fread(rowBuffer, 1, IMG_WIDTH * 2, f);
    Image rowImage(ENCODING_RGB16, rowBuffer, IMG_WIDTH, 1);
    Display.image(rowImage, 0, y);
  }
  Display.endDraw();

  free(rowBuffer);
  fclose(f);
  return true;
}
```

### Clearing the Display

Reset the display by entering `clear` in to the Serial Monitor.

```cpp
void forceScreenClear() {
  Display.beginDraw();
  Display.fill(0x0000); // Fill with black
  Display.endDraw();
}
```

### Full code

^C

### Conclusion

This project demonstrates how to read and display **16-bit RGB565 images** from a USB drive onto the Arduino GIGA Display. The row-by-row approach optimizes memory usage while ensuring smooth rendering. This technique is useful for **digital signage, interactive kiosks, and embedded GUI projects**.


