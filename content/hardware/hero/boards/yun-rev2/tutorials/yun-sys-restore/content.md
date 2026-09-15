---
author: 'Arduino'
description: 'Restore the 1.5.3 image after you did sysupgrade to 1.6.2 on old Yún'
title: 'Restoring the 1.5.3 Image on Arduino Yún'
tags: [Yún]
---

This procedure is the way to recover the OpenWrt-Yun functionalities on a Yún board that was upgraded to newer firmware with the old bootloader present. The upgrade on an old board brings the Yún to a situation where the Linux environment doesn't boot up properly. It is necessary to restore the 1.5.3 image to keep the warranty and recover the full functionality of the OpenWrt-Yun.

## Software Needed

Download the [1.5.3 image](https://downloads.arduino.cc/openwrtyun/1/YunSysupgradeImage_v1.5.3.zip)

## Preparation

Upload the Yun Serial terminal (Examples -> Bridge - YunSerialTerminal) on the Yún and open a serial monitor of the Arduino Software (IDE), then press YUN RST button. If you have an old Yún board the message from the console may vary. When on serial monitor you should read:

`type 'ard' to enter u-boot console`

please type `ard` in the input field of Serial Monitor and press enter

This way you enter in U-boot and the `ar7240>`  prompt is shown.

**Note: if your board does NOT show `type 'ard' to enter u-boot console` , you need to refer to the board manufacturer to get the proper instructions and image to reflash.**

Copy and paste the following command line:

```arduino
setenv bootargs board=YUN console=ttyATH0,250000 mtdparts=spi0.0:256k(u-boot)ro,64k(u-boot env)ro,14656k(rootfs),1280k(kernel),64k(nvram),64k(art),15936k@0x50000(firmware) rootfstype=squashfs,jffs2 noinitrd
```

Then when the console ( `ar7240>` ) returns, type:
`boot`

## Chaos Calmer Image Boot

Following the command, your Yún should start booting the 1.6.2 image. Once OpenWRT (Chaos Calmer) finishes booting and you have gained access to the console (`root@arduino#:`) you can follow the procedure to do a  sysupgrade as described in the tutorial [upgrade OpenWrt image on the Yún](https://www.arduino.cc/en/Tutorial/YunSysupgrade) to restore the [1.5.3 image](https://downloads.arduino.cc/openwrtyun/1/YunSysupgradeImage_v1.5.3.zip).

**Remember that you must use the files of the 1.5.3 image and NOT the 1.6.2 ones.**

At the end of the process your Yún will reboot and have 1.5.3 version of OpenWrt-Yun.