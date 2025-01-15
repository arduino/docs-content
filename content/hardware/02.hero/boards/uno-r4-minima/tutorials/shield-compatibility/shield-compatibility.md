---
title: 'Arduino UNO R4 Shield Compatibility'
description: 'This article covers popular shields and their compatibility including the libraries used.'
tags:
  - shields
  - compatibility
  - UNO R4 Minima
  - UNO R4 WiFi
author: 'Hannes Siebeneicher'
hardware:
  - hardware/02.hero/boards/uno-r4-minima
  - hardware/02.hero/boards/uno-r4-wifi
---

This article covers a list of shields compatible with the [UNO R4 Minima](/hardware/uno-r4-minima) and the [UNO R4 WiFi](/hardware/uno-r4-wifi).

## Compatible Shields

### Official Arduino Shields

| Name                             | Compatible | Libraries                                                                               |
| -------------------------------- | ---------- | --------------------------------------------------------------------------------------- |
| Arduino 4 Relays Shield          | Yes        | None                                                                                    |
| Arduino Ethernet Shield Rev2     | Yes        | [Ethernet.h](https://github.com/arduino-libraries/Ethernet)                             |
| Arduino Motor Shield Rev3        | Yes        | None                                                                                    |
| Arduino Education Shield         | Yes        | [EducationShield.h](https://github.com/arduino-libraries/EducationShield)               |

### Third-Party Shields

| Name                              | Compatible | Libraries                |
| ------------------------------    | ---------- | ---------------------------------------------------------------------------------------------------- |
| Adafruit Capacitve Touch Shield   | Yes        |  [Adafruit_MPR121.h](https://github.com/adafruit/Adafruit_MPR121)                                    |
| Adafruit NFC/RFID Shield          | No         | [Adafruit-PN532.h](https://github.com/adafruit/Adafruit-PN532)                                       |
| Olimex MIDI Shiel                 | Yes        | [MIDI](https://github.com/FortySevenEffects/arduino_midi_library)                                    |
| Sparkfun CAN-Bus                  | No         | [SparkFun_CAN-Bus_Arduino_Library](https://github.com/sparkfun/SparkFun_CAN-Bus_Arduino_Library)     |
| Sparkfun MP3 Player Shield        | -          | -                                                                                                    |
| SeedStudio Touch Shield           | -          | -                                                                                                    |
| Adafruit Neopixel Shield          | No         |  [Adafruit_NeoPixel.h](https://github.com/adafruit/Adafruit_NeoPixel)                                |
| Adafruit Wave Shield              | No         |   [WaveHC.h](https://github.com/adafruit/WaveHC)                                                     |
| Adafruit 1.8 TFT Shield           | No         |   [ST7735.h](https://github.com/adafruit/Adafruit-ST7735-Library)                                    |
| SeedStudio Base Shield            | Yes        |  None                                                                                                |
| Adafruit WINC1500 WiFi Shield     | No         |   [WiFi101.h](https://github.com/arduino-libraries/WiFi101)                                          |
| Adafruit Music Maker shield       | Yes        |   [Adafruit_VS1053.h](https://github.com/adafruit/Adafruit_VS1053_Library)                           |
| Adafruit Motor Shield             | -          |   [Adafruit_Motor_Shield_V2_Library](https://github.com/adafruit/Adafruit_Motor_Shield_V2_Library)   |
| TinkerKit DMX master shield       | -          |   [DmxMaster](https://github.com/TinkerKit/DmxMaster)                                                |