---
author: 'Arduino'
description: ''
title: 'Upgrading the OpenWrt-Yun Image on the Yún'
tags: [Yún]
---

***Note: this procedure is applicable only on the Yún; if you have anything different, you may still be able to upgrade it to the current image, but using a different process that we do not encourage nor suggest. It has dangers and difficulties and you could easily brick your board. The warranty of our boards that go through this process is void. If you still want to try it, you need to  to upgrade the bootloader following the [bootloader update](https://www.arduino.cc/en/Tutorial/YunUBootReflash) procedure and then proceed with the kernel and rootfs as explained on the same page.***

**Yún Shield owners only**
The [Yún Shield](https://www.arduino.cc/en/Main/ArduinoYunShield) is shipped with a different OpenWRT Linux image which is incompatible with the v1.5.3 Yún update you can find on the main [download page](https://www.arduino.cc/en/Main/Software). The stock OpenWRT Linux image of the Yún Shield has the version number 1.6.2 and there aren't yet available updates. However the sysupgrade image is available for download [here](https://downloads.arduino.cc/openwrtyun/1.6.2/YunSysupgradeImage_v1.6.2.zip).

The list of available packages for the Yún is available [here](https://downloads.arduino.cc/openwrtyun/1.6.2/packages/index.html).
See the list of [changes](https://github.com/arduino/openwrt-yun-1505/blob/15.05-openwrt-patched/CHANGELOG).

**If you erroneously upgraded a Yún board with the image for the Yún Shield (1.6.2) the device won't boot because it has an incompatible bootloader. You can still recover your device following this [Image Restore procedure](https://www.arduino.cc/en/Tutorial/YunSysRestore) and keep your original warranty status.**

## Preparation

To upgrade or reinstall the OpenWrt-Yun image on your Yún, you'll need to download the zip file from the [download page](https://www.arduino.cc/en/Main/Software#toc8). Once you've  unpacked the file, move the binary image file to the root folder of a microSD card and insert the card into the Yún, or put it in the root folder of a USB flash drive and insert it in the USB Host of the  Yún.

**Updating the OpenWrt-Yun image will cause the loss of all files and configurations you previously saved on the flash memory of the Yún. **
Before upgrading, we strongly advise you to upload YunSerialTerminal example (File -> Examples -> Bridge -> YunSerialTerminal) because other sketches may interfere with the boot process and may make your Yún  unresponsive.

## Upgrading Using the Web Panel

Make sure the Yún and your computer are on the same network, and open a browser. Connect to the Yún's web panel page by entering the IP address or the name you gave to the board in the browser. With the default name you reach the Yún at `http://arduino.local`.

Once logged in, on the first page with the network information, scroll to the bottom, where you should see a notification informing you that a file containing an upgrade image has been found.

If you want to proceed resetting the Yún, click the red **RESET** button at the very bottom of the page.

![Click on "reset".](assets/YunSysupgrade_1.png)

The process of upgrading the Yún  will take around 3 minutes. During this time the WLAN led will flash until the process has been completed.

![Wait until the LED stops blinking.](assets/YunSysupgrade_2.png)

While you are upgrading the image you can't use the Yún

## Upgrading Using the Command Line

You can connect to the Yún via SSH and use a command line tool on your computer to upgrade the system's image.

Note that accessing the command line via the serial monitor and YunSerialTerminal will not work.

If you're unfamiliar with the command line and terminal, you may want to use the web tool.

To learn more about the terminal, see [these notes](https://www.arduino.cc/en/Tutorial/LinuxCLI).

To connect to your Yún via SSH, open the terminal application of your choice, and enter :

`ssh root@myYun.local`

Where `myYun` is the name of your board. You'll be asked for the password to the board. Once logged in, enter:

`run-sysupgrade /mnt/sda1/openwrt-ar71xx-generic-yun-squashfs-sysupgrade.bin`

The output on the console will look like this:

```arduino
run-sysupgrade /mnt/sda1/openwrt-ar71xx-generic-yun-squashfs-sysupgrade.bin

Sending TERM to remaining processes ... uhttpd dbus-daemon dnsmasq avahi-daemon thd ntpd uSDaemon sleep syslogd klogd hotplug2 procd ubusd netifd

Sending KILL to remaining processes ...

Switching to ramdisk...

Performing system upgrade...

Unlocking firmware ...

Writing from <stdin> to firmware ...

Upgrade completed

Rebooting system...
```

As with the web panel method, the process will take a few minutes, and the WLAN led will flash until the update has  completed.



**Last revision 2018/05/29 by SM**