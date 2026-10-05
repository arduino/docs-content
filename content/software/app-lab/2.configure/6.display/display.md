---
title: 'MIPI-DSI Display'
description: 'Configure a MIPI-DSI display connected via the UNO Media Carrier in Arduino App Lab.'
author: Karl Söderby
tags: [Arduino App Lab, UNO Q, MIPI, Display, Media Carrier, DSI]
---

The **Arduino® UNO Media Carrier** provides a 22-pin MIPI-DSI connector (DISPLAY) for attaching touch displays. The display must be connected to the carrier while the UNO Q is unpowered.

<Alert type="info">

The supported displays are the Waveshare DSI Touch "A" series:

- Waveshare 5" DSI Touch Display (A)
- Waveshare 8" DSI Touch Display (A)
- Waveshare 10" DSI Touch Display (A)

</Alert>

## Enable Carrier Mode

In the Arduino App Lab **Settings**, enable the **Media Carrier** under the **Carriers** section.

![Enable carrier mode](assets/enable-carrier.png)

## Select Display

1. Select the display size that matches your connected display (5", 8", 10" supported).
2. Click **Apply and Reboot** to apply changes. This will reboot your board.

![Select display type](assets/select-display.png)

After rebooting, the display is active and the desktop environment will render on it. Touch input is available immediately without additional configuration.

## How Carrier Configuration Works

MIPI-DSI displays do not support plug-and-play detection, so the Linux kernel must be told explicitly what hardware is attached. When you select a display size and click **Apply and Reboot**, App Lab stages a Device Tree Overlay (`.dtbo`) that is merged onto the board's base device tree. The Qualcomm kernel reads the device tree only once at startup to configure the display drivers, which is why a full reboot is required for any change to take effect.

<Alert type="info">

These settings apply to the **UNO Q** used with the UNO Media Carrier. The **VENTUNO Q** instead provides a native HDMI port that handles EDID autodiscovery, so no configuration or reboot is required and the display does not appear in the **Carriers** settings.

</Alert>

## Further Reading

- [UNO Media Carrier Hardware Page](https://docs.arduino.cc/hardware/uno-media-carrier/)
- [UNO Media Carrier User Manual](https://docs.arduino.cc/tutorials/uno-media-carrier/user-manual/)
