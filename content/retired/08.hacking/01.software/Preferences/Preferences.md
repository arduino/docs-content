---
title: 'Arduino Preferences'
description: 'The Arduino preferences file contains many options for customizing the way Arduino compiles and upload sketches.'
tags: 
  - Preferences
---

Some preferences can be controlled from the **Preferences** dialog within the Arduino environment. Access it from the **File** menu in Windows or Linux, or the **Arduino** menu on the Mac.

Other preferences must be changed in the preferences.txt file. This file's location is displayed in the preferences dialog. It should be:

- \Arduino15\preferences.txt (Windows, Arduino IDE 1.6.6 and newer)
- \Arduino15\preferences.txt (Windows, Arduino IDE 1.6.0 - 1.6.5)
- \Arduino\preferences.txt (Windows, Arduino IDE 1.0.6 and older)
- \Documents\ArduinoData\preferences.txt (Windows app version)
- ~/Library/Arduino15/preferences.txt (Max OS X, Arduino IDE 1.6.0 and newer)
- ~/Library/Arduino/preferences.txt (Max OS X, Arduino IDE 1.0.6 and older)
- ~/.arduino15/preferences.txt (Linux, Arduino IDE 1.6.0 and newer)
- ~/.arduino/preferences.txt (Linux, Arduino IDE 1.0.6 and older)
- `<Arduino IDE installation folder>`/portable/preferences.txt (when used in portable mode)

Only edit the file when Arduino is *not* running - otherwise your changes will be overwritten when Arduino exits.

The definitions that determine the contents of the Board menu are found in boards.txt in the hardware/ sub-directory of the Arduino application directory. The definitions for the Burn Bootloader menu are in the programmers.txt file in the same directory. To create a new board or programmer definition, copy an existing one, change the prefix used in the preference keys (e.g. "diecimila." or "avrisp."), and alter the values to fit your hardware.

