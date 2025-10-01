---
title: 'Upgrading the WiFi Shield Firmware'
description: 'Learn how to upgrade the firmware for your Arduino WiFi Shield.'
tags: [WiFi Shield, Firmware Upgrade]
---

The WiFi shield provides wireless connectivity per the IEEE 802.11 b/g standard through the HDG204 (or HDG104) module. The TCP/IP stack and the APIs for WiFi library are managed by the AT32UC3A1512 (or AT32UC3A1256) called AT32UC3 for short microcontroller on the shield. Your Arduino connects to the shield using SPI through the WiFi library.

Both the AT32UC3 and the HDG204/HDG104 modules have firmware upgradable through the mini USB connector.

This tutorial shows you how to upgrade :

The HDG204/HDG104 WiFi module firmware, for when the manufacturer provides a new firmware binary for their device.
The AT32UC3 when there is a new version of the firmware available from Arduino. Alternately, if you are an expert C programmer you can customise the official source code to make a derivative firmware for yourself. Check the [WiFi library repository](https://github.com/arduino/ArduinoCore-avr/tree/master/firmwares/wifishield) for the source code.
When upgrading the firmware, the WiFi shield should not be connected to the Arduino board.

Upgrading the firmware on the devices is a two step process:

- The HDG204/HDG104 firmware is named "wifi_dnld.elf". The H&D module doesn't have static memory so you'll upload its firmware to AT32UC3 controller, then the AT32UC3 will transfer the firmware into the HDG204 module's dedicated flash memory.
- Once the firmware for the HDG204/HDG104 is uploaded, you're ready to the upload the WiFi shield firmware for the AT32UC3. The "wifiHD.elf" is the file that contains the the application for the controller.

## Download a DFU Programmer
You'll need additional software to update the code on the 32UC3.

**Windows:** Download Atmel's flip programmer

**Mac:** Install MacPorts following the instructions on [this page](https://www.macports.org/install.php#pkg). Once MacPorts is installed, in a Terminal window, type: `sudo port install dfu-programmer`

To update macPorts:

```
sudo port selfupdate
```

To update dfu-programmer and other ports to the most recent version:

``` 
sudo port upgrade outdated
```

Make sure you're using dfu-programer version 0.5.4 or later

>NB: If you've never used sudo before, it will ask for your password. Use the password you login to your Mac with. sudo allows you to run commands as the administrator of the computer

Linux: from a command line type

```
sudo apt-get install dfu-programme
```

or

```
sudo aptitude install dfu-programmer
```

depending on your distribution.

## Download updated firmware for the 32UC3A1256/AT32UC3A1256
The latest version is [here](https://github.com/arduino/ArduinoCore-avr/tree/master/firmwares/wifishield). Choose WiFi shield firmware.

The firmware is also located with the Arduino software in the /hardware/avr/arduino/firmwares/wifishield folder. On OSX, right-click or command-click on the Arduino application and select "show package contents" to find this folder.

Windows procedure

On Windows, you need to install the [AVR 32 Drivers](https://www.arduino.cc/en/uploads/Hacking/AVR32_USB_Driver.zip). On Windows use the [Flip](https://www.microchip.com/) software provided by Atmel to program the device using the DFU mode (Device Firmware Update). Flip supplies a utility called batchisp that you'll use to make the upgrade. Once you've installed Flip, open a command prompt (CMD) and reach the following path contained inside the Flip installation directory, usually: `cd C:\Program Files (x86)\Atmel\Flip 3.4.5\bin` but it depends where the Atmel software is installed. Now you are able to download the firmware on the shield.

>Note: Flip needs needs a 32-bit JRE. A 64-bit JRE do not work.


Connect the J3 jumper to put the shield in the programming mode, then plug it to the computer through the mini USB socket. On the command prompt type:

```
batchisp.exe -device AT32UC3A1512 -hardware usb -operation erase f memory flash blankcheck loadbuffer /Arduino/hardware/avr/arduino/firmwares/wifishield/binary/wifi_dnld.elf program verify start reset 0
```

or

```
batchisp.exe -device AT32UC3A1256 -hardware usb -operation erase f memory flash blankcheck loadbuffer /Arduino/hardware/avr/arduino/firmwares/wifishield/binary/wifi_dnld.elf program verify start reset 0
```

Depending on the chip you have.

To download the HDG204/HDG104 WiFi module firmware inside the dataflash.

```
batchisp.exe -device AT32UC3A1512 -hardware usb -operation erase f memory flash blankcheck loadbuffer /Arduino/hardware/avr/arduino/firmwares/wifishield/binary/wifiHD.elf program verify start reset 0
```

or

batchisp.exe -device AT32UC3A1256 -hardware usb -operation erase f memory flash blankcheck loadbuffer /Arduino/hardware/avr/arduino/firmwares/wifishield/binary/wifiHD.elf program verify start reset 0
```

Depending on the chip you have.

To download the WiFi shield firmware on the AT32UC3A1512/AT32UC3A1256.

Once the upgrade is done you can remove the J3 jumper and restart the shield. Now it's ready to be used. Look at the Optional section at the bottom of this page for details on checking if the firmware upgrade was a success.

## Linux and Mac procedure

On Linux and Mac we wrote a script that automates the process. The script is a command line utility, so in order to use it you need to open a terminal on your system.

You can find the script inside your IDE at the following path: `~/arduino1.x.x/hardware/avr/arduino/firmwares/wifishield/scripts`

The WiFi shield upgrading script also make use of the [dfu-programmer](http://dfu-programmer.sourceforge.net/) that you need to install on your system previously (make sure that the version is 0.5.4 or later).

Connect a jumper on the J3 connector, that put the shield in the programming mode. Then connect the USB cable to the shield USB mini socket.

Open a Terminal window and move to the path were you saved the script and type as following to get the help:

- Mac: `./ArduinoWifiShield_upgrade.sh -h`
- Linux: `sudo ./ArduinoWifiShield_upgrade.sh -h`

On Linux you need to run the script as root in order to access correctly to the USB DFU peripherals.

With the `-a` parameter you'll pass to the script the current Arduino installation path, for example: `/home/user/Coding`

With the `-f` parameter you'll make the choice of which firmware install:

- `shield` to upgrade only the shield firmware
- `all` to upgrade both the firmwares
Optional: to test if the WiFi shield has been updated, you can connect an USB to Serial adapter to the FTDI socket and access to the serial debug terminal if the startup message contains the updated date. Look at the apposite page to learn more about the serial debug option.