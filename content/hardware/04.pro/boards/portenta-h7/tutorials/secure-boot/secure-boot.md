---
title: 'Secure Boot on Portenta H7'
description: 'Learn how to use secure boot on the Arduino Portenta H7.'
tags: 
  - Secure Boot
author: 'Umberto Baldi'
hardware:
  - hardware/04.pro/boards/portenta-h7

software:
  - ide-v1
  - ide-v2
  - cli
---

## Introduction
This short tutorial will guide the user through enabling the secure boot on the Portenta H7, generating custom security keys, and using them with the MCUboot bootloader.

## Hardware & Software Required
-   [Portenta H7](https://store.arduino.cc/portenta-h7)
-   Arduino IDE 1.8.19+  or Arduino IDE 2.0.0-rc5+ (https://www.arduino.cc/en/software)
-   [Arduino Mbed OS Portenta Boards](https://github.com/arduino/ArduinoCore-mbed) version 3.0.0+
-   [imgtool](https://github.com/arduino/imgtool-packing/releases/latest) (optional)

## Instructions

### Flashing the Latest Bootloader
In order to have secure boot enabled you must update the bootloader on your Portenta H7 and use [MCUboot](https://www.mcuboot.com/). You can find more info on how to perform the update in [this other tutorial](../por-ard-bl/content.md).

### Use Default Security Keys
Once The bootloader has been updated to MCUboot, it's possible to use [secure boot](https://www.keyfactor.com/blog/what-is-secure-boot-its-where-iot-security-starts/) to have an additional layer of security. From that point on it is required to upload a compiled sketch with the Custom Board Option **"Security settings"** set to **"Signature + Encryption"** (the option can be found under **Tools > Security settings** in the IDE when selecting Portenta H7 as board, or you can use `--board-options security=sien` if using the Arduino CLI). Failing to provide such option will cause the bootloader not to run the compiled sketch because it is not trusted.

If no operation is performed the default security keys are used.
These keys are embedded in the example sketch `STM32H747_updateBootloader` which can be found in  **Files > Examples > STM32H747_System > STM32H747_updateBootloader**. A private 256bit [ECDSA](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm) key is used for the encryption (`ecdsa-p256-encrypt-key.h`), while a public key is used for the signing (`ecdsa-p256-signing-key.h`). These two keys are the ones the bootloader uses to verify if a sketch is valid or not, before starting it for the first time. The default private keys used after compiling a sketch to sign and encrypt it are located in `Arduino15/packages/arduino/hardware/mbed_portenta/<version>/libraries/MCUboot/default_keys/`.

### 1. Generate Custom Cecurity Keys
The default keys provided with the mbed platform are obviously only intended for development purposes. In a production environment it is strongly recommended to generate a new key pair (public and private key).
This can be done with [**imgtool**](https://github.com/arduino/imgtool-packing/releases/latest). You can download and install it directly from the release section.

***Pro tip: imgtool is already installed by the mbed platform and can be found in the `%LOCALAPPDATA%\Arduino15\packages\arduino\tools\imgtool` directory on Windows, in `~/.arduino15/packages/arduino/tools/imgtool` on Linux and in `~/Library/Arduino15/packages/arduino/tools/imgtool` on macOS.***

To generate the new keys you can use this command line:
```
imgtool keygen --key my-sign-keyfile.pem -t ecdsa-p256
imgtool keygen --key my-encrypt-keyfile.pem -t ecdsa-p256
```
This command line will generate two private PEM encoded security keys and save them in the current directory with `my-sign-keyfile.pem`and `my-encrypt-keyfile.pem` names. The algorithm used to generate the keys is ECDSA 256bit.

Remember to **save the keys to a secure location** and not to lose them.

### 2. Upload the Custom Keys to the Board
Once the keys have been generated they have to be uploaded on the Portenta. This procedure has to be done only once, because it's persistent. To extract the public\private key and encode it in to a "C" byte array inside a `.h` header file you can use:
```
imgtool getpriv -k my-encrypt-keyfile.pem > ecsda-p256-encrypt-key.h 
imgtool getpub -k my-sign-keyfile.pem > ecsda-p256-signing-key.h
```

Now you have to replace the keys inside the Sketch to update the bootloader(**STM32H747_updateBootloader**).
To do so just save the sketch to another location and replace the `ecsda-p256-encrypt-key.h` and `ecsda-p256-signing-key.h` files with the newly generated ones and then [update the bootloader](../por-ard-bl/content.md) again.

***NOTE: In case the keys are compromised, this process can be performed again with a new set of keys, but any firmware signed with the previous pair will no longer work.***

### 3. Use the Custom Keys when Compiling
Since the default keys have been changed in favour of custom generated ones, the new ones have to be used when compiling and uploading a sketch, because the compiled sketch is signed and encrypted using such keys.

To override the security keys used during the compile you have to use the Arduino CLI and specify the keys with:
```
arduino-cli compile -b arduino:mbed_portenta:envie_m7 --board-options security=sien --keys-keychain <path-to-your-keys> --sign-key ecsdsa-p256-signing-key.pem --encrypt-key ecsdsa-p256-encrypt-key.pem /home/user/Arduino/MySketch
```

## Learn More
If you want to implement secure boot for your platform [this](https://arduino.github.io/arduino-cli/latest/guides/secure-boot/) should be helpful.
