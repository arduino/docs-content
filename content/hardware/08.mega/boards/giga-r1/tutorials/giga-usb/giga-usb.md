---
title: Guide to Arduino GIGA USB Features
description: 'Learn how you can turn your USB device into a mouse or keyboard, how to read & write to a USB mass storage, and how to send MIDI signals.'
author: Karl Söderby
---

## USB Mass Storage

The USB-A connector onboard the GIGA R1 can be used to connect **USB mass storage devices**, for example, a USB stick. This can be used for a number of applications, including:
- Accessing large files such as images & audio files,
- Logging large amounts of data,
- Storing images or videos captured with a camera.

USB mass storage devices connected needs to be formatted with the **FAT32** as a file system, using the **MBR partioning scheme**. This is a requirement, and reading & writing will not work otherwise.

### USB Designation

To access the correct USB mass storage device, we need to specify the **designation** in the code.

```
mbed::FATFileSystem usb("USB_DRIVE_DESIGNATION")
```

This is so that our GIGA R1 can target the right USB device.

### List File Directory

Below is an example sketch that can be used to **list** files in a USB mass storage device.

```arduino
/*
  Portenta - DirList

  The sketch shows how to mount an usb storage device and how to
  get a list of the existing folders and files.

  The circuit:
   - Portenta H7

  This example code is in the public domain.
*/

#include <DigitalOut.h>
#include <FATFileSystem.h>
#include <USBHostMbed5.h>

USBHostMSD msd;
mbed::FATFileSystem usb("usb");

// If you are using a Portenta Machine Control uncomment the following line
// mbed::DigitalOut otg(PB_14, 0);

void setup()
{
    Serial.begin(115200);
    while (!Serial)
        ;

    Serial.println("Starting USB Dir List example...");

    // if you are using a Max Carrier uncomment the following line
    // start_hub();

    while (!msd.connect()) {
        //while (!port.connected()) {
        delay(1000);
    }

    Serial.print("Mounting USB device... ");
    int err = usb.mount(&msd);
    if (err) {
        Serial.print("Error mounting USB device ");
        Serial.println(err);
        while (1);
    }
    Serial.println("done.");

    char buf[256];

    // Display the root directory
    Serial.print("Opening the root directory... ");
    DIR* d = opendir("/usb/");
    Serial.println(!d ? "Fail :(" : "Done");
    if (!d) {
        snprintf(buf, sizeof(buf), "error: %s (%d)\r\n", strerror(errno), -errno);
        Serial.print(buf);
    }
    Serial.println("done.");

    Serial.println("Root directory:");
    unsigned int count { 0 };
    while (true) {
        struct dirent* e = readdir(d);
        if (!e) {
            break;
        }
        count++;
        snprintf(buf, sizeof(buf), "    %s\r\n", e->d_name);
        Serial.print(buf);
    }
    Serial.print(count);
    Serial.println(" files found!");

    snprintf(buf, sizeof(buf), "Closing the root directory... ");
    Serial.print(buf);
    fflush(stdout);
    err = closedir(d);
    snprintf(buf, sizeof(buf), "%s\r\n", (err < 0 ? "Fail :(" : "OK"));
    Serial.print(buf);
    if (err < 0) {
        snprintf(buf, sizeof(buf), "error: %s (%d)\r\n", strerror(errno), -errno);
        Serial.print(buf);
    }
}

void loop()
{
}
```

### File Read

Below is an example sketch that can be used to **read** files from a USB mass storage device.

```arduino
/*
  Portenta - FileRead

  The sketch shows how to mount an usb storage device and how to
  read from an existing file.
  to use this sketch create a .txt file named Arduino.txt,
  in your storage device and write some content inside.

  The circuit:
   - Portenta H7

  This example code is in the public domain.
*/

#include <USBHostMbed5.h>
#include <DigitalOut.h>
#include <FATFileSystem.h>

USBHostMSD msd;
mbed::FATFileSystem usb("usb");

// If you are using a Portenta Machine Control uncomment the following line
mbed::DigitalOut otg(PB_14, 0);
 
void setup() {
  Serial.begin(115200);
  while (!Serial);

  delay(2500);
  Serial.println("Starting USB File Read example...");

  // if you are using a Max Carrier uncomment the following line
  //start_hub();

  while (!msd.connect()) {
    delay(1000);
  }

  Serial.println("Mounting USB device...");
  int err =  usb.mount(&msd);
  if (err) {
    Serial.print("Error mounting USB device ");
    Serial.println(err);
    while (1);
  }
  Serial.print("read done ");
  mbed::fs_file_t file;
  struct dirent *ent;
  int dirIndex = 0;
  int res = 0;
  Serial.println("Open file..");
  FILE *f = fopen("/usb/Arduino.txt", "r+");
  char buf[256];
  Serial.println("File content:");

  while (fgets(buf, 256, f) != NULL) {
    Serial.print(buf);
  }

  Serial.println("File closing");
  fflush(stdout);
  err = fclose(f);
  if (err < 0) {
    Serial.print("fclose error:");
    Serial.print(strerror(errno));
    Serial.print(" (");
    Serial.print(-errno);
    Serial.print(")");
  } else {
    Serial.println("File closed");
  }
}

void loop() {

}
```

### File Write

Below is an example sketch that can be used to **write** files from a USB mass storage device.

```arduino
/*
  Portenta - FileWrite

  The sketch shows how to mount an usb storage device and how to
  write a file, eventually overwriting the original content.

  The circuit:
   - Portenta H7

  This example code is in the public domain.
*/

#include <USBHostMbed5.h>
#include <DigitalOut.h>
#include <FATFileSystem.h>

USBHostMSD msd;
mbed::FATFileSystem usb("usb");

// mbed::DigitalOut pin5(PC_6, 0);
mbed::DigitalOut otg(PB_8, 1);

void setup() {
  Serial.begin(115200);
  while (!Serial);
  msd.connect();

  while (!msd.connected()) {
    //while (!port.connected()) {
    delay(1000);
  }

  Serial.println("Mounting USB device...");
  int err =  usb.mount(&msd);
  if (err) {
    Serial.print("Error mounting USB device ");
    Serial.println(err);
    while (1);
  }
  Serial.print("read done ");
  mbed::fs_file_t file;
  struct dirent *ent;
  int dirIndex = 0;
  int res = 0;
  Serial.println("Open /usb/numbers.txt");
  FILE *f = fopen("/usb/numbers.txt", "w+");
  for (int i = 0; i < 10; i++) {
    Serial.print("Writing numbers (");
    Serial.print(i);
    Serial.println("/10)");
    fflush(stdout);
    err = fprintf(f, "%d\n", i);
    if (err < 0) {
      Serial.println("Fail :(");
      error("error: %s (%d)\n", strerror(errno), -errno);
    }
  }

  Serial.println("File closing");
  fflush(stdout);
  err = fclose(f);
  if (err < 0) {
    Serial.print("fclose error:");
    Serial.print(strerror(errno));
    Serial.print(" (");
    Serial.print(-errno);
    Serial.print(")");
  } else {
    Serial.println("File closed");
  }
}

void loop() {

}
```

## USB HID

It is possible to turn your GIGA R1 board into a Human Interface Device **(HID)**, aka mouse & keyboard, using the [USBHID](https://github.com/arduino/ArduinoCore-mbed/tree/master/libraries/USBHID) library which is included in the GIGA core. 

Among other things, you can:
- Create a custom keyboard, or a keyboard accessory,
- Create sophisticated game controllers,
- Accessories for VR/AR applications.

### Keyboard

***Important! When using the GIGA as a keyboard, make sure to include some sort of delay. Otherwise, you may end up printing things very fast, which can be very annoying. If this happens nontheless, double tap the reset button and upload a blank sketch to reset the board.*** 

To emulate a keyboard, we need to include `PluggableUSBHID.h` and `USBKeyboard.h`, and create an object using the `USBkeyboard` constructor. 

```arduino
#include "PluggableUSBHID.h"
#include "USBKeyboard.h"

USBKeyboard Keyboard;
```

To send a single character, we can use the `putc()` method.

```arduino
Keyboard.putc(97); //prints the letter 'a'
```

See the `DEC` column at [ascii-code.com](https://www.ascii-code.com/) to understand what number you need to print a specific character.

To print a whole string, use the `printf()` method.

```arduino
Keyboard.printf("Hello World!"); 
```

To use modifiers and function keys, use the `key_code()` method.

```
Keyboard.key_code(KEY_F1);
```

To use media keys, use the `media_control()` method.

```
Keyboard.media_control(KEY_NEXT_TRACK);
```

***All modifiers, function and media control keys can be found in [this header file](https://github.com/arduino/ArduinoCore-mbed/blob/master/libraries/USBHID/src/USBKeyboard.h).***

### Mouse

To emulate a mouse, we need to include `PluggableUSBHID.h` and `USBMouse.h`, and create an object using the `USBMouse` constructor. 

```arduino
#include "PluggableUSBHID.h"
#include "USBMouse.h"

USBMouse Mouse;
```

To move the cursor, we can write the **x** and **y** coordinates directly, using the `move()` method.

```arduino
Mouse.move(100,100);
```

For clicking the mouse, use the `click()` method.

```arduino
Mouse.click(MOUSE_LEFT);
Mouse.click(MOUSE_RIGHT);
Mouse.click(MOUSE_MIDDLE);
```

For double clicking the mouse, use the `double_click()` method.

```
Mouse.double_click(MOUSE_LEFT);
```

To press and release the buttons on the mouse, we can use the `press()` and `release()` methods. This way, we can define how long we want the button to be pressed for.

```arduino
Mouse.press(MOUSE_LEFT);
Mouse.press(MOUSE_RIGHT);
Mouse.press(MOUSE_MIDDLE);

delay(1000);

Mouse.release(); 
```

## USB Host

## GIGA R1 as a USB Stick

It is possible to expose the external flash (16MB) on the GIGA R1 as a USB device. This makes it possible to store smaller files directly on the GIGA R1, which can be accessed through the sketch.

```arduino
#include "PluggableUSBMSD.h"
#include "QSPIFBlockDevice.h"
#include "MBRBlockDevice.h"
#include "FATFileSystem.h"

static QSPIFBlockDevice root;
mbed::MBRBlockDevice wifi_data(&root, 1);
mbed::MBRBlockDevice ota_data(&root, 2);
static mbed::FATFileSystem wifi("wifi");
static mbed::FATFileSystem ota("ota");

void USBMSD::begin()
{
  int err = wifi.mount(&wifi_data);
  if (err) {
    while (!Serial);
    Serial.println("Please run WiFiFirmwareUpdater before");
    return;
  }
  ota.mount(&ota_data);
}


USBMSD MassStorage(&root);

void setup() {
  Serial.begin(115200);
  MassStorage.begin();
}

void printDirectory(char* name) {
  DIR *d;
  struct dirent *p;

  d = opendir(name);
  if (d != NULL) {
    while ((p = readdir(d)) != NULL) {
      Serial.println(p->d_name);
    }
  }
  closedir(d);
}

void loop() {
  if (MassStorage.media_removed()) {
    // list the content of the partitions
    // you may need to restart the board for the list to update if you copied new files
    Serial.println("Content of WiFi partition:");
    printDirectory("/wifi");
    Serial.println("Content of OTA partition:");
    printDirectory("/ota");
  }
  delay(1000);
}
```