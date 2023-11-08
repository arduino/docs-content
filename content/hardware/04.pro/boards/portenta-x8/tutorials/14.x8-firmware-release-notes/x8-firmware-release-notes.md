---
title: '14. Portenta X8 Firmware Release Notes'
difficulty: beginner
tags: [Linux, containers, factories, foundries]
description: 'This article contains release notes of the existing Portenta X8 firmwares.'
author: Taddy Ho Chung
hardware:
  - hardware/04.pro/board/portenta-x8

---

## Firmware Release Notes

The present document provides detailed release notes for each firmware version of the Portenta X8. Explore the changes, improvements, and fixes for the released firmwares.

### Hardware and Software Requirements

Supported Device:

- [Portenta X8](https://store.arduino.cc/portenta-x8)

Compatible carriers with supported device:

- [Portenta Breakout board](https://store.arduino.cc/portenta-breakout)
- [Portenta Max Carrier](http://store.arduino.cc/portenta-max-carrier)
- [Portenta Hat Carrier](https://store.arduino.cc/products/portenta-hat-carrier)

## Firmware Versions

Below is a list of all available firmware versions with their release notes.

<details>
  <summary>OS Image 746: Release arduino-88.91</summary>

  ### New Features
  - Added the Portenta HAT Carrier support
  - Added experimental support for Ditto

  ### Enhancements
  - Improved bridge implementation (X8H7)

  ### Bug Fixes
  - _u-boot env_ accessible in devel images
  - Patches for CAN bus protocol

  ### Security Updates
  - Security patches and updates to enhance protection.

  ### Additional Notes
  - Based on [LmP v88](https://foundries.io/products/releases/88/). NOTE: this is the Yocto manifest. For docker compose apps, check out [here](https://github.com/arduino/portenta-containers/tree/release).

</details>

For instructions on how to install or upgrade to the latest firmware version, you can use the [Portenta X8 Out-of-the-box](https://docs.arduino.cc/tutorials/portenta-x8/user-manual#out-of-the-box-experience) or [flash it manually](https://docs.arduino.cc/tutorials/portenta-x8/user-manual#update-using-uuu-tool) downloading the latest version directly from this [link](https://downloads.arduino.cc/portentax8image/image-latest.tar.gz).
