---
title: 'MIPI-CSI Camera'
description: 'Configure a MIPI-CSI camera connected via the UNO Media Carrier in Arduino App Lab.'
author: Karl Söderby
tags: [Arduino App Lab, UNO Q, MIPI, camera, Media Carrier]
---

The **Arduino® UNO Media Carrier** provides two 22-pin (0.5mm pitch) MIPI-CSI connectors (CAMERA0 and CAMERA1) for attaching IMX219-based cameras, such as the Raspberry Pi Camera Module 2. The Raspberry Pi Camera Module 2 uses a 15-pin (1.0mm pitch) ribbon cable, so an adapter cable is required to connect it to the carrier's 22-pin connectors. Cameras must be connected to the carrier while the UNO Q is unpowered.

<Alert type="info">

Only IMX219-based cameras are supported at this time.

</Alert>

## Enable Carrier Mode

In the Arduino App Lab **Settings**, enable the **Media Carrier** under the **Carriers** section.

![Enable carrier mode](assets/enable-carrier.png)

## Select Camera and Port

1. Select the camera port that is being used (CAMERA0 and/or CAMERA1)
2. Select the type of camera: choose **1-2 lanes** if using a standard 15-pin Raspberry Pi Camera Module 2 with an adapter cable, or **1-4 lanes** if using a native 22-pin camera module.
3. Click **Apply and Reboot** to apply changes. This will reboot your board.

![Select camera type and connector](assets/select-camera.png)

After rebooting, the camera is available to the Linux OS. Any App Lab example that uses camera input, such as the Object Detection example, will now use the camera connected via the Media Carrier's MIPI-CSI port instead.
