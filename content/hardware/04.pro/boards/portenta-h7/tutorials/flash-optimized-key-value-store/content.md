---
title: 'Creating a Flash-Optimized Key-Value Store'
description: 'This tutorial explains how to create a Flash-optimized key-value store using the Flash memory of the Portenta H7.'
coverImage: assets/por_ard_block_device_cover.svg
difficulty: advanced
tags:
  - Storage
  - Key-Value store
  - Flash
author: 'Giampaolo Mancini, Sebastian Romero'
libraries:
  - name: Arduino PRO Tutorials
    url: https://github.com/arduino-libraries/Arduino_Pro_Tutorials/releases/latest
hardware:
  - hardware/04.pro/boards/portenta-h7
software:
  - ide-v1
  - ide-v2
  - web-editor
---

## Overview
This tutorial explains how to create a Flash-optimized key-value store using the Flash memory of the Portenta H7. It builds on top of the **Flash In-Application Programming** tutorial.

## Goals

In this tutorial you will learn how to use the Mbed OS [TDBStore API](https://os.mbed.com/docs/mbed-os/v6.9/apis/kvstore.html) to create a [Key value store](https://en.wikipedia.org/wiki/Key%E2%80%93value_database) in the free space of the microcontroller's internal Flash.

### Required Hardware and Software

- [Portenta H7 (ABX00042)](https://store.arduino.cc/products/portenta-h7),  [Portenta H7 Lite (ABX00045)](https://store.arduino.cc/products/portenta-h7-lite) or [Portenta H7 Lite Connected (ABX00046)](https://store.arduino.cc/products/portenta-h7-lite-connected)
- USB-C® cable (either USB-A to USB-C® or USB-C® to USB-C®)
- [Arduino IDE 2.0+](https://www.arduino.cc/en/software) or [Arduino CLI 0.13.0+](https://www.arduino.cc/pro/software-pro-cli/)

## Instructions

### MbedOS APIs for Flash Storage
The core software of Portenta H7 is based on the Mbed OS operating system, allowing developers to integrate the Arduino API with the APIs exposed by Mbed OS.

Mbed OS has a rich API for managing storage on different mediums, ranging from the small internal Flash memory of a microcontroller to external SecureDigital cards with large data storage space.

In this tutorial, you are going to save a value persistently inside the Flash memory. That allows to access that value even after a reset of the microcontroller. You will retrieve some information from a Flash block by using the [FlashIAPBlockDevice](https://os.mbed.com/docs/mbed-os/v6.9/apis/flashiapblockdevice.html) and the [TDBStore](https://os.mbed.com/docs/mbed-os/v6.9/apis/kvstore.html) APIs. You will use the `FlashIAPBlockDevice` class to create a block device on the free space of the Flash and you will create a Key-Value Store in it using the `TDBStore` API.

***Important: The TBStore API optimizes for access speed, reduce [wearing of the flash](https://en.wikipedia.org/wiki/Flash_memory#Memory_wear) and minimize storage overhead. TBStore is also resilient to power failures. If you want to use the Flash memory of the microcontroller, always prefer the TDBStore approach over a direct access to the FlashIAP block device.***

### 1. The Basic Setup
Begin by plugging in your Portenta board to the computer using a USB-C® cable and open the Arduino IDE. If this is your first time running Arduino sketch files on the board, we suggest you check out how to [set up the Portenta H7 for Arduino](https://docs.arduino.cc/tutorials/portenta-h7/setting-up-portenta) before you proceed.

### 2. Create the Structure of the Program
Let's program the Portenta with a sketch. You will also define a few helper functions in a supporting header file.

* Create a new sketch named `FlashKeyValue.ino` 
* Create a new file named `FlashIAPLimits.h` to store the helper functions in a reusable file.

**Note:** Finished sketch its inside the tutorials library wrapper at:  
**Examples > Arduino_Pro_Tutorials > Creating a Flash-Optimized Key-Value Store > FlashKeyValueStore**

### 3. Populate the Helper Functions
First let's add the helper functions to the `FlashIAPLimits.h` header. This will determine the available Flash limits to allocate the custom data.

```cpp
/**
Helper functions for calculating FlashIAP block device limits
**/

// Ensures that this file is only included once
#pragma once 

#include <Arduino.h>
#include <FlashIAP.h>
#include <FlashIAPBlockDevice.h>

using namespace mbed;

// A helper struct for FlashIAP limits
struct FlashIAPLimits {
  size_t flash_size;
  uint32_t start_address;
  uint32_t available_size;
};

// Get the actual start address and available size for the FlashIAP Block Device
// considering the space already occupied by the sketch (firmware).
FlashIAPLimits getFlashIAPLimits()
{
  // Alignment lambdas
  auto align_down = [](uint64_t val, uint64_t size) {
    return (((val) / size)) * size;
  };
  auto align_up = [](uint32_t val, uint32_t size) {
    return (((val - 1) / size) + 1) * size;
  };

  size_t flash_size;
  uint32_t flash_start_address;
  uint32_t start_address;
  FlashIAP flash;

  auto result = flash.init();
  if (result != 0)
    return { };

  // Find the start of first sector after text area
  int sector_size = flash.get_sector_size(FLASHIAP_APP_ROM_END_ADDR);
  start_address = align_up(FLASHIAP_APP_ROM_END_ADDR, sector_size);
  flash_start_address = flash.get_flash_start();
  flash_size = flash.get_flash_size();

  result = flash.deinit();

  int available_size = flash_start_address + flash_size - start_address;
  if (available_size % (sector_size * 2)) {
    available_size = align_down(available_size, sector_size * 2);
  }

  return { flash_size, start_address, available_size };
}
```

### 4. Make the Key Store Program
Go to `FlashKeyValue.ino` and include the libraries that you need from **MBED** and your header helper (`FlashIAPLimits.h`). The `getFlashIAPLimits()` function which is defined in the `FlashIAPLimits.h` header takes care of not overwriting data already stored on the Flash and aligns the start and stop addresses with the size of the Flash sector. You can use those calculated limits to create a block device and a `TDBStore` on top of them.

```cpp
#include <FlashIAPBlockDevice.h>
#include <TDBStore.h>

using namespace mbed;

// Get limits of the In Application Program (IAP) flash, ie. the internal MCU flash.
#include "FlashIAPLimits.h"
auto iapLimits { getFlashIAPLimits() };

// Create a block device on the available space of the FlashIAP
FlashIAPBlockDevice blockDevice(iapLimits.start_address, iapLimits.available_size);

// Create a key-value store on the Flash IAP block device
TDBStore store(&blockDevice);

// Dummy sketch stats data for demonstration purposes
struct SketchStats {
  uint32_t startupTime;
  uint32_t randomValue;
  uint32_t runCount;
};
```

In the `setup()` function at the beginning you will have to wait until the Serial port is ready and then print some info about the FlashIAP block device (`blockDevice`).

```cpp
void setup()
{
  Serial.begin(115200);
  while (!Serial);

  //  Wait for terminal to come up
  delay(1000);

  Serial.println("FlashIAPBlockDevice + TDBStore Test");

  // Feed the random number generator for later content generation
  srand(micros());

  // Initialize the flash IAP block device and print the memory layout
  blockDevice.init();  
  Serial.print("FlashIAP block device size: ");
  Serial.println(blockDevice.size());
  Serial.print("FlashIAP block device read size: ");
  Serial.println(blockDevice.get_read_size());
  Serial.print("FlashIAP block device program size: ");
  Serial.println(blockDevice.get_program_size());
  Serial.print("FlashIAP block device erase size: ");
  Serial.println(blockDevice.get_erase_size());
  // Deinitialize the device
  blockDevice.deinit();

```

After that, initialize the TDBstore (our storage space), set the key for the store data (`stats`), initialize the value that you will save `runCount` and declare an object to fetch the previous values (`previousStats`).

```cpp
  // Initialize the key-value store
  Serial.print("Initializing TDBStore: ");
  auto result = store.init();
  Serial.println(result == MBED_SUCCESS ? "OK" : "Failed");
  if (result != MBED_SUCCESS)
    while (true); // Stop the sketch if an error occurs

  // An example key name for the stats on the store
  const char statsKey[] { "stats" };

  // Keep track of the number of sketch executions
  uint32_t runCount { 0 };

  // Previous stats
  SketchStats previousStats;
```

Now that you have everything ready, let's retrieve the previous values from the store and update the store with the new values. 

```cpp
  // Get previous run stats from the key-value store
  Serial.println("Retrieving Sketch Stats");
  result = getSketchStats(statsKey, &previousStats);

  if (result == MBED_SUCCESS) {
    Serial.println("Previous Stats");
    Serial.print("\tStartup Time: ");
    Serial.println(previousStats.startupTime);
    Serial.print("\tRandom Value: ");
    Serial.println(previousStats.randomValue);
    Serial.print("\tRun Count: ");

    Serial.println(previousStats.runCount);

    runCount = previousStats.runCount;

  } else if (result == MBED_ERROR_ITEM_NOT_FOUND) {
    Serial.println("No previous data was found.");
  } else {
    Serial.println("Error reading from key-value store.");
    while (true);
  }

  // Update the stats and save them to the store
  SketchStats currentStats { millis(), rand(), ++runCount };  
  result = setSketchStats(statsKey, currentStats);
  
  if (result == MBED_SUCCESS) {
    Serial.println("Sketch Stats updated");
    Serial.println("Current Stats");
    Serial.print("\tStartup Time: ");
    Serial.println(currentStats.startupTime);
    Serial.print("\tRandom Value: ");
    Serial.println(currentStats.randomValue);
    Serial.print("\tRun Count: ");

    Serial.println(currentStats.runCount);
  } else {
    Serial.println("Error while saving to key-value store");
    while (true);
  }
}
```

To finish the sketch, create `getSketchStats` and `setSketchStats` functions above `setup()` and `loop()`. 

The `getSketchStats` function tries to retrieve the stats values stored in the Flash using the key `key` and returns them via the `stats` pointer parameter. Our `SketchStats` data struct is very simple and has a fixed size. You can therefore deserialize the buffer with a simple `memcpy`.

The `setSketchStats` function stores the `stats` data and assigns the key `key` to it. The key will be created in the key-value store if it does not exist yet.

```cpp
// Retrieve SketchStats from the key-value store
int getSketchStats(const char* key, SketchStats* stats)
{
  // Retrieve key-value info
  TDBStore::info_t info;
  auto result = store.get_info(key, &info);

  if (result == MBED_ERROR_ITEM_NOT_FOUND)
    return result;

  // Allocate space for the value
  uint8_t buffer[info.size] {};
  size_t actual_size;

  // Get the value
  result = store.get(key, buffer, sizeof(buffer), &actual_size);
  if (result != MBED_SUCCESS)
    return result;

  memcpy(stats, buffer, sizeof(SketchStats));
  return result;
}

// Store a SketchStats to the the k/v store
int setSketchStats(const char* key, SketchStats stats)
{
  return store.set(key, reinterpret_cast<uint8_t*>(&stats), sizeof(SketchStats), 0);  
}
```

### 5. Results

Upload the sketch, the output should be similar to the following:

```
FlashIAPBlockDevice + TDBStore Test
FlashIAP block device size: 1572864
FlashIAP block device read size: 1
FlashIAP block device program size: 32
FlashIAP block device erase size: 131072
Initializing TDBStore: OK
Retrieving Sketch Stats
Previous Stats
        Startup Time: 12727
        Random Value: 1514801629
        Run Count: 13
Sketch Stats updated
Current Stats
        Startup Time: 4285
        Random Value: 2133170025
        Run Count: 14
```

***Note that the Flash memory will be __erased__ when a new sketch is uploaded.***

Push the reset button to restart the sketch. The values of the stats have been updated. `Previous Stats` which is retrieved from the key-value store now contains values from the previous execution.

## Conclusion
You have learned how to use the available space in the Flash memory of the microcontroller to create a key-value store and use it to retrieve and store data.

It is not recommended to use the Flash of the microcontroller as the primary storage for data-intensive applications. It is best suited for read/write operations that are performed only once in a while such as storing and retrieving application configurations or persistent parameters.

### Next Steps

- Learn how to retrieve a collection of keys using TDBStore iterators via [`iterator_open`](https://os.mbed.com/docs/mbed-os/v6.9/mbed-os-api-doxy/classmbed_1_1_k_v_store.html#a77661adec54b9909816e7492a2c61a91) and [`iterator_next`](https://os.mbed.com/docs/mbed-os/v6.9/mbed-os-api-doxy/classmbed_1_1_k_v_store.html#a5116b40a3480462b88dc3f1bb8583ad4)
- Learn how to create an incremental TDBStore set sequence via [`set_start`](https://os.mbed.com/docs/mbed-os/v6.9/mbed-os-api-doxy/classmbed_1_1_k_v_store.html#a6e882a0d4e0cbadf6269142ac3c4e693), [`set_add_data`](https://os.mbed.com/docs/mbed-os/v6.9/mbed-os-api-doxy/classmbed_1_1_k_v_store.html#adbe636bf8c05834fe68b281fc638c348) and [`set_finalize`](https://os.mbed.com/docs/mbed-os/v6.9/mbed-os-api-doxy/classmbed_1_1_k_v_store.html#a346da66252added46d3b93902066b548)
- Learn how to use the 16 MB QSPI Flash on the Portenta H7
