---
title: GIGA R1 Camera Guide
description: Learn about GIGA R1 and camera compatibility, and find examples that work out of the box with the GIGA R1.
tags: [ArduCAM, Camera, AI, OpenMV]
author: Karl Söderby
---

The GIGA R1 has a dedicated camera connector that allows certain camera modules to mount directly on the board. This makes it possible to add machine vision to your GIGA R1 board without much effort at all.

In this guide, we will explore the GIGA R1's camera support a bit more in-depth:

- Where the camera connector is located.
- What cameras are compatible.
- What library/examples are available.
- How to get started with machine vision using the OpenMV platform.

## Hardware Requirements

To follow and use the examples provided in this guide, you will need one of the following boards:

- [GIGA R1]()
- [GIGA R1 WiFi]()

## Supported Cameras

The GIGA R1 currently supports the following cameras, via the [Camera](https://github.com/arduino/ArduinoCore-mbed/tree/master/libraries/Camera) library that is bundled with the [Arduino Mbed Core](https://github.com/arduino/ArduinoCore-mbed):

- **OV7670** and **OV7675**
- **GC2145**
- **Himax HM01B0**
- **Himax HM0360**

## Camera Connector

![Camera Connector on GIGA R1](assets/camera-connector-pins.png)

The 20 pin camera connector onboard the GIGA R1 is designed to be directly compatible with some breakout boards from ArduCam. 

This allows you to simply connect the camera module directly to the board, without making any additional circuit.

Some of the 20 pin connector breakout boards from ArduCam can be found [here](https://www.arducam.com/product-category/stm32-camera-modules-dcmi-and-spi/).

The complete pin map can be found below:

| Left | Right |
| ---- | ----- |
| 3V3  | GND   |
| SCL1 | SDA1  |
| 54   | 55    |
| 56   | 57    |
| 58   | 59    |
| 60   | 61    |
| 62   | 63    |
| 64   | 65    |
| 66   | 67    |
| 66   | 67    |

![Camera connector, zoomed in.](assets/camera-connector-zoomed.png)

## OpenMV

[OpenMV](https://openmv.io/) is a platform for machine vision projects, and can be programmed with MicroPython, more specifically, [OpenMV's branch of MicroPython](https://github.com/openmv/micropython).

## Raw Bytes Over Serial (Processing)

![Live view of the camera.](assets/processing-example.png)

This example allows you to stream the sensor data from your camera to a Processing application, using serial over USB. This will allow you to see the image directly in your computer. 

***This example requires a version of [Processing](https://processing.org/download) on your machine.***

**Step 1: Arduino**

Upload the following sketch to your board.

This sketch is also available in the Arduino IDE via **Examples > Camera > CameraCaptureRawBytes**.

```arduino
#include "camera.h"

#ifdef ARDUINO_NICLA_VISION
  #include "gc2145.h"
  GC2145 galaxyCore;
  Camera cam(galaxyCore);
  #define IMAGE_MODE CAMERA_RGB565
#elif defined(ARDUINO_PORTENTA_H7_M7)
  #include "hm0360.h"
  HM0360 himax;
  Camera cam(himax);
  #define IMAGE_MODE CAMERA_GRAYSCALE
#elif defined(ARDUINO_GIGA)
  #include "ov7670.h"
  OV7670 ov7670;
  Camera cam(ov7670);
  #define IMAGE_MODE CAMERA_RGB565
#else
#error "This board is unsupported."
#endif

/*
Other buffer instantiation options:
  FrameBuffer fb(0x30000000);
  FrameBuffer fb(320,240,2);
*/
FrameBuffer fb;

unsigned long lastUpdate = 0;


void blinkLED(uint32_t count = 0xFFFFFFFF)
{
  pinMode(LED_BUILTIN, OUTPUT);
  while (count--) {
    digitalWrite(LED_BUILTIN, LOW);  // turn the LED on (HIGH is the voltage level)
    delay(50);                       // wait for a second
    digitalWrite(LED_BUILTIN, HIGH); // turn the LED off by making the voltage LOW
    delay(50);                       // wait for a second
  }
}

void setup() {
  // Init the cam QVGA, 30FPS
  if (!cam.begin(CAMERA_R320x240, IMAGE_MODE, 30)) {
    blinkLED();
  }

  blinkLED(5);
}

void loop() {
  if(!Serial) {    
    Serial.begin(921600);
    while(!Serial);
  }

  // Time out after 2 seconds and send new data
  bool timeoutDetected = millis() - lastUpdate > 2000;
  
  // Wait for sync byte.
  if(!timeoutDetected && Serial.read() != 1) return;  

  lastUpdate = millis();
  
  // Grab frame and write to serial
  if (cam.grabFrame(fb, 3000) == 0) {
    Serial.write(fb.getBuffer(), cam.frameSize());
  } else {
    blinkLED(20);
  }
}

```

**Step 2: Processing**

The following processing sketch will launch a Java app that allows you to view the camera. As data is streamed via serial, make sure you close the Serial Monitor during this process, else it won't work.

***Important! Make sure to replace the following line in the code below: `/dev/cu.usbmodem14301`, with the name of your port.***

Click on the big "PLAY" button to initialize the app.

```cpp
/*
  Use with the Examples -> CameraCaptureRawBytes Arduino sketch.
  This example code is in the public domain.
*/

import processing.serial.*;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;

Serial myPort;

// must match resolution used in the Arduino sketch
final int cameraWidth = 320;
final int cameraHeight = 240;

// Must match the image mode in the Arduino sketch
final boolean useGrayScale = true;

// Must match the baud rate in the Arduino sketch
final int baudRate = 921600;

final int cameraBytesPerPixel = useGrayScale ? 1 : 2;
final int cameraPixelCount = cameraWidth * cameraHeight;
final int bytesPerFrame = cameraPixelCount * cameraBytesPerPixel;
final int timeout =  int((bytesPerFrame / float(baudRate / 10)) * 1000 * 2); // Twice the transfer rate

PImage myImage;
byte[] frameBuffer = new byte[bytesPerFrame];
int lastUpdate = 0;
boolean shouldRedraw = false;

void setup() {
  size(640, 480);  

  // If you have only ONE serial port active you may use this:
  //myPort = new Serial(this, Serial.list()[0], baudRate);          // if you have only ONE serial port active

  // If you know the serial port name
  //myPort = new Serial(this, "COM5", baudRate);                    // Windows
  //myPort = new Serial(this, "/dev/ttyACM0", baudRate);            // Linux
  myPort = new Serial(this, "/dev/cu.usbmodem14301", baudRate);     // Mac

  // wait for a full frame of bytes
  myPort.buffer(bytesPerFrame);  

  myImage = createImage(cameraWidth, cameraHeight, ALPHA);
  
  // Let the Arduino sketch know we're ready to receive data
  myPort.write(1);
}

void draw() {
  // Time out after a few seconds and ask for new data
  if(millis() - lastUpdate > timeout) {
    println("Connection timed out.");    
    myPort.clear();
    myPort.write(1);
  }
  
  if(shouldRedraw){    
    PImage img = myImage.copy();
    img.resize(640, 480);
    image(img, 0, 0);
    shouldRedraw = false;
  }
}

int[] convertRGB565ToRGB888(short pixelValue){  
  //RGB565
  int r = (pixelValue >> (6+5)) & 0x01F;
  int g = (pixelValue >> 5) & 0x03F;
  int b = (pixelValue) & 0x01F;
  //RGB888 - amplify
  r <<= 3;
  g <<= 2;
  b <<= 3; 
  return new int[]{r,g,b};
}

void serialEvent(Serial myPort) {  
  lastUpdate = millis();
  
  // read the received bytes
  myPort.readBytes(frameBuffer);

  // Access raw bytes via byte buffer  
  ByteBuffer bb = ByteBuffer.wrap(frameBuffer);
  
  // Ensure proper endianness of the data for > 8 bit values.
  // The 1 byte bb.get() function will always return the bytes in the correct order.
  bb.order(ByteOrder.BIG_ENDIAN);

  int i = 0;

  while (bb.hasRemaining()) {
    if(useGrayScale){
      // read 8-bit pixel data
      byte pixelValue = bb.get();

      // set pixel color
      myImage.pixels[i++] = color(Byte.toUnsignedInt(pixelValue));
    } else {
      // read 16-bit pixel data
      int[] rgbValues = convertRGB565ToRGB888(bb.getShort());

      // set pixel RGB color
      myImage.pixels[i++] = color(rgbValues[0], rgbValues[1], rgbValues[2]);
    }       
  }
  
  myImage.updatePixels();
  
  // Ensures that the new image data is drawn in the next draw loop
  shouldRedraw = true;
  
  // Let the Arduino sketch know we received all pixels
  // and are ready for the next frame
  myPort.write(1);
}
```

If all goes well, you should now be able to see the camera feed.

### JPEG Webserver

The **JPEG Webserver** allows you to take an image every X amount of seconds and upload it to a webserver that can be accessed remotely. This setup can be used for asset monitoring, security systems, smart doorbells and many more applications. 

This setup also comes with a Golang script that you will need to launch via a terminal, which is required to make this setup work. 

**Step 1: Launch Golang Script**

First, create a file in a directory of your choice, and name it `main.go`. Paste the following code into it:

```go
package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"strconv"
	"time"
)

func uploadFile(w http.ResponseWriter, r *http.Request) {
	fmt.Println("File Upload Endpoint Hit")

	// Parse our multipart form, 10 << 20 specifies a maximum
	// upload of 10 MB files.
	r.ParseMultipartForm(10 << 20)
	// FormFile returns the first file for the given key `myFile`
	// it also returns the FileHeader so we can get the Filename,
	// the Header and the size of the file
	file, handler, err := r.FormFile("image1")
	if err != nil {
		fmt.Println("Error Retrieving the File")
		fmt.Println(err)
		return
	}
	defer file.Close()
	fmt.Printf("Uploaded File: %+v\n", handler.Filename)
	fmt.Printf("File Size: %+v\n", handler.Size)
	fmt.Printf("MIME Header: %+v\n", handler.Header)

	// Create a temporary file within our temp-images directory that follows
	// a particular naming pattern
	name := "upload-" + strconv.Itoa(int(time.Now().Unix())) + "*.jpg"
	tempFile, err := ioutil.TempFile("", name)
	if err != nil {
		fmt.Println(err)
	}
	defer tempFile.Close()
	fmt.Println("File ", tempFile.Name())

	// read all of the contents of our uploaded file into a
	// byte array
	fileBytes, err := ioutil.ReadAll(file)
	if err != nil {
		fmt.Println(err)
	}
	// write this byte array to our temporary file
	tempFile.Write(fileBytes)
	// return that we have successfully uploaded our file!
	fmt.Println("Successfully Uploaded File\n")
}

func setupRoutes() {
	http.HandleFunc("/upload", uploadFile)
	http.ListenAndServe(":8088", nil)
}

func main() {
	fmt.Println("Hello World")
	fmt.Println("Serving on :8088")
	setupRoutes()
}
```

Then, to launch the script, open a terminal on the directory and use the following command:

```
go run main.go
```

Which, on success will return `Serving on :8088`.

**Step 2: OpenMV Script**

Next step is to launch the OpenMV editor. If you are not yet familiar with OpenMV, visit the [Getting Started with OpenMV]() section.

Once the editor is open, connect your board. Then, copy and paste the script below into the editor, and click on the green "PLAY" button.

***Please note that the `WIFI_SSID = "yournetwork"` and `WIFI_PASS = "yourpassword"` strings will need to be replaced with your credentials to your Wi-Fi network.***

```python
import time
import network
import sensor
import urequests
import os

WIFI_SSID = "yournetwork"
WIFI_PASS = "yourpassword"

url = 'http://10.130.22.213:8088/upload'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    # Add more headers if needed
}

class RAMBlockDev:
    def __init__(self, block_size, num_blocks):
        self.block_size = block_size
        self.data = bytearray(block_size * num_blocks)

    def readblocks(self, block_num, buf, offset=0):
        addr = block_num * self.block_size + offset
        for i in range(len(buf)):
            buf[i] = self.data[addr + i]

    def writeblocks(self, block_num, buf, offset=None):
        if offset is None:
            # do erase, then write
            for i in range(len(buf) // self.block_size):
                self.ioctl(6, block_num + i)
            offset = 0
        addr = block_num * self.block_size + offset
        for i in range(len(buf)):
            self.data[addr + i] = buf[i]

    def ioctl(self, op, arg):
        if op == 4: # block count
            return len(self.data) // self.block_size
        if op == 5: # block size
            return self.block_size
        if op == 6: # block erase
            return 0

def sensor_init():
    sensor.reset()
    sensor.set_pixformat(sensor.RGB565)
    sensor.set_framesize(sensor.QVGA)
    sensor.skip_frames(time = 1000)

def wifi_connect():
    if not WIFI_SSID or not WIFI_PASS:
        raise (Exception("Network is not configured"))
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)
    while not wlan.isconnected():
        #raise (Exception("Network is not configured, add SSID and pass to secrets.py"))
        time.sleep_ms(500)
    print("WiFi Connected ", wlan.ifconfig())



if __name__ == "__main__":
    sensor_init()
    wifi_connect()
    bdev = RAMBlockDev(512, 100)
    os.VfsFat.mkfs(bdev)
    os.mount(bdev, '/ramdisk')
    while (True):
        img = sensor.snapshot()
        jpg = img.compress()
        with open('/ramdisk/img.jpg', 'w') as f:
            f.write(jpg)
        f.close()
        files = {
          'image1': ('img.jpg', open('/ramdisk/img.jpg', 'rb'))
        }
        r = urequests.post(url, files=files, headers=headers)
        print(f"sending {jpg}")
        time.sleep(20.0)
```

Once you run the script, the board will attempt to connect to the local Wi-Fi, and on success, it will capture an image and upload it. 

This can now be accessed if your device is on the same local network.

### Motion Detection

