---
title: 'QR Code Recognition'
description: 'The QR library allows you to recognize QR code markers and data.'
tags: [QR Code, Camera]
difficulty: 'advanced'
author: Arduino
---

This example shows the flexibility and power of the FPGA architecture. A QR code recognition set of APIs is included in the VidorGraphics library and the corresponding IP is in the bitstream that is loaded in the FPGA together with the sketch for the SAMD Board Package. The example highlights on video the QR code markers and prints on the serial monitor the coordinates of the markers found.

## Hardware Required

- [Arduino MKR Vidor 4000](https://store.arduino.cc/arduino-vidor-4000)
- Omnivision OV5647 camera

- microHDMI to HDMI cable or adaptor

- Monitor with HDMI input

## Circuit

There is no circuit for this example.

![The circuit for this tutorial.](assets/vidor-circuit.png)

## Code

Include the VidorCamera library, which is part of VidorGraphics.
`#include "VidorGraphics.h"`
`#include "VidorCamera.h"`

You have a number of functions available to manage the recognition of a QR Code. VidorQR is part of the VidorCam library; the functions are accessible with **cam.qrrec**.

- `void begin()` - start recognition algorithm

- `void end()` - stops recognition

- `void setMode(uint8_t mode);` - change video mode

- `void setThr(uint8_t thr);` - set recognition threshold

- `int readQRCode(void);` - perform qr code recognition

- `sQrDet qr;` - structure containing detected points

```arduino

#include "VidorGraphics.h"
#include "VidorCamera.h"

VidorCamera vcam;

#define MAXDIM 10

static uint16_t x[QR_PT_DET_NUM], y[QR_PT_DET_NUM];

struct qrPtn {

  uint16_t x[QR_PT_DET_NUM];

  uint16_t y[QR_PT_DET_NUM];
};

static qrPtn qrBufferPtn[MAXDIM];

uint16_t count = 0, last;

void setup() {

  Serial.begin(9600);

  // wait for the serial monitor to open,

  // if you are powering the board from a USB charger remove the next line

  while (!Serial);

  if (!FPGA.begin()) {

    Serial.println("Initialization failed!");

    while (1) {}

  }

  /**

    begin() enable the I2C communication and initialize the display for the camera

  */

  if (!vcam.begin()) {

    Serial.println("Camera begin failed");

    while (1) {}

  }

  /**

      qrrec.begin(); enable the QR code recognition

  */

  vcam.qrrec.begin();

  delay(4000);

  Serial.println("Power ON");
}

void loop()  {

  /**

     qrrec.readQRCode(); get, if available, the coordinates of the QR code in the screen

  */

  vcam.qrrec.readQRCode();

  for (int i = 0; i < QR_PT_DET_NUM; i++) {

    if (vcam.qrrec.qr.pt[i].valid) {

      x[i] = (vcam.qrrec.qr.pt[i].xs + vcam.qrrec.qr.pt[i].xe) / 2;

      y[i] = (vcam.qrrec.qr.pt[i].ys + vcam.qrrec.qr.pt[i].ye) / 2;

      vcam.vgfx.Cross(x[i], y[i], 65535);

    }

  }

  last = count % MAXDIM;

  for (int i = 0; i < QR_PT_DET_NUM; i++) {

    vcam.vgfx.Cross(qrBufferPtn[last].x[i], qrBufferPtn[last].y[i], 0, 0);

    qrBufferPtn[last].x[i] = x[i];

    qrBufferPtn[last].y[i] = y[i];

  }

  count++;
}
```

**Last revision 2018/07/22 by SM**
