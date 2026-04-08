---
title: Arduino App Lab and IoT Remote Phone App Integration
description: This tutorial teaches you how to leverage the Arduino IoT Remote app to use your phone sensors with Arduino App Lab applications.
author: Christopher Méndez
hardware:
  - hardware/uno/boards/uno-q
tags: [SBC, Linux, Debian, AI, Model]
difficulty: beginner
---

## Overview

In this tutorial, you will learn how to unlock your smartphone's potential within Arduino App Lab using the IoT Remote app. We will explore a powerful new feature that turns your phone into a wireless input device. Specifically, you will learn how to stream video from your phone directly to the Arduino App Lab to power the Object Detection Brick, allowing you to run AI vision projects without needing a USB webcam.

![](assets/thumbnail.png)

**Note:** Your smartphone will be used as a remote camera input. Both the Arduino UNO Q and your smartphone must be connected to the same network.

## Goals

- Understand the integration between the IoT Remote app and the Arduino App Lab.
- Configure your smartphone to act as a wireless camera input for your projects.
- Test an example application using the Object Detection Brick with the remote video feed as input.
- Run the project to detect and classify objects in real-time using your phone.

## How It Works

This integration transforms your smartphone into a wireless camera for the Arduino App Lab through a secure pairing process:

### The Pairing Process

1. **QR Code Generation**: When you run your app, the Arduino UNO Q generates a unique one-time password (OTP) and creates a QR code containing connection details (IP address, port, and the secret).
2. **Secure Handshake**: You scan the QR code with your phone's camera app. The IoT Remote app is opened automatically and receives the secret to authenticate with your board over a secure WebSocket connection.
3. **Video Streaming**: Once authenticated, your phone begins streaming video over HTTP on port `4912` by default. The board receives these frames and makes them available to your application.

### Architecture Overview

The system uses two communication channels:

- **WebSocket (Control Channel)**: Handles the initial pairing and sends control messages. Each session uses a unique secret for security.
- **HTTP (Data Channel)**: Delivers the actual video stream on port `4912`, providing continuous data transmission with minimal latency.

***Both devices communicate directly over your local network. No video data is sent to the cloud, making sure of privacy and low latency.***

## Required Hardware and Software

### Hardware Requirements

* [Arduino UNO Q](https://store.arduino.cc/products/uno-q) (x1)
* Smartphone (iOS or Android)
* Personal computer with internet access (to view the Web UI)

### Software Requirements

- [Arduino App Lab](https://www.arduino.cc/en/software/#app-lab-section)
- [IoT Remote App](https://cloud.arduino.cc/iot-remote-app/)
- Arduino Account 

## Mobile Camera Streaming

To test this feature, we will leverage the **Detect Objects on Smartphone Camera** example inside the Arduino App Lab. It will allow us to easily learn how this feature works and try it out without the need to develop an App from scratch. 

![Detect Objects on Smartphone Camera](assets/mobile-example.png)

***To stream your phone's camera feed to your UNO Q, both must be on the same network.***

***__Note__: The video stream is delivered over HTTP on __port 4912__. If you're on a corporate or restricted network, make sure this port is accessible. The initial pairing uses a separate WebSocket connection on a dynamically assigned port.***

### Arduino App Lab Setup

1. Ensure your Arduino UNO Q is powered and connected to the network.
2. Open the Arduino App Lab on your computer.
3. Run the **Detect Objects on Smartphone Camera** example in Arduino App Lab.
4. The App should open automatically in the web browser. You can open it manually via `<board-name>.local:7000`.
5. The Web UI will display a **QR Code**.
  ![QR Code in the browser](assets/qr-code-full.png)

### Arduino IoT Remote Setup

1. Make sure to have installed the [**Arduino IoT Remote**](https://cloud.arduino.cc/iot-remote-app/) app on your smartphone.
   ![App available in your favorite OS](assets/install-app.png)
2. Scan the QR code with your phone's camera app.
   ![QR code scan](assets/qr-code.png)
3. The Arduino IoT Remote app will open automatically on your phone. Log in with your Arduino account if you haven't already.
4. Once connected, the camera feed will be visible directly on your phone and the video stream will be transmitted to the Web UI.
5. Point your phone at objects and watch as the App detects and recognizes them.
   ![Phone's camera stream](assets/camera-stream.png)

### No QR Code Configuration (Optional)

You can also configure your phone from the IoT Remote app without scanning the QR code:

1. Go to Devices, tap on the plus icon to set up a new device and select **Stream phone camera to UNO Q**.
   ![IoT Remote setup](assets/iot-remote.png)
2. Select your Arduino UNO Q from the list. (It must be connected to the same network)
   ![Select your UNO Q](assets/search-uno-q.png)
3. Enter the 6 digits code below your QR code on the Web UI.
   ![Start streaming](assets/start-streaming.png)
4. The streaming will start right away.

![Smartphone Camera Streaming](assets/Companion-app.gif)

## Mobile Integration Feature

To add the smartphone camera integration to your own custom Arduino App Lab application, you need to implement a specific handshake mechanism between your board and the phone. It consists of a Python® backend that manages the secure connection and a JavaScript frontend that generates the pairing QR code.

### 1. Backend Implementation (`main.py`)

The backend is responsible for creating a secure "room" for the phone to connect to. Use the `WebSocketCamera` class to generate a one-time password (secret) that allows only the intended phone to connect to your board.

**Required Imports:**

```python
import secrets
import string
from arduino.app_peripherals.camera import WebSocketCamera
```

**Setup Logic:**

You must generate a random secret (OTP) and pass it to the `WebSocketCamera` instance. You also need to send these connection details to your frontend so it can generate the QR code.

```python
# 1. Generate a random 6-digit secret for security
def generate_secret() -> str:
    characters = string.digits
    return ''.join(secrets.choice(characters) for _ in range(6))

secret = generate_secret()

# 2. Initialize the Camera with the secret
# 'encrypt=True' ensures the handshake is secure
resolution = (480, 640)  # Portrait resolution for mobile devices
camera = WebSocketCamera(resolution=resolution, secret=secret, encrypt=True, adjustments=resized(resolution, maintain_ratio=True))

# 3. Send connection details to the Frontend when a client connects
# This passes the IP, Port, and Secret required for the QR Code
ui.on_connect(lambda sid: ui.send_message("welcome", {
    "client_name": camera.name,
    "secret": secret,
    "status": camera.status,
    "protocol": camera.protocol,
    "ip": camera.ip,
    "port": camera.port
}))
```

### 2. Frontend Implementation (`app.js`)

The frontend acts as the bridge. It receives the connection details from the backend and encodes them into a specific URL format inside a QR code. When the Arduino IoT Remote app scans this, it knows exactly where to send the video stream.

**Prerequisites:** Ensure you have a QR code library included in your HTML (e.g., `qrcode.min.js`).

**Handling the Handshake:**

In your `app.js`, listen for the "welcome" message from the backend. Use the data received to generate the pairing URL.

```javascript
// Listen for connection details from main.py
socket.on('welcome', async (message) => {
    // If the camera is not yet connected, generate the QR code
    if (message.status !== "connected") {
        generateQRCode(message.secret, message.protocol, message.ip, message.port);
    }
});

function generateQRCode(secret, protocol, ip, port) {
    const qrCodeContainer = document.getElementById('qrCodeContainer');
    
    // The specific URL format required by the IoT Remote App
    const connectionUrl = `https://cloud.arduino.cc/installmobileapp?otp=${secret}&protocol=${protocol}&ip=${ip}&port=${port}`;

    new QRCode(qrCodeContainer, {
        text: connectionUrl,
        width: 128,
        height: 128
    });
}
```

**Displaying the Stream:**

Once the phone connects, the video is not sent via WebSocket but served over HTTP on a specific port (default is usually `4912`). You should use an `<iframe>` to display it.

```javascript
// Logic to display video when status becomes 'streaming'
const streamUrl = `http://${window.location.hostname}:4912/embed`;
document.getElementById('videoIframe').src = streamUrl;
```

## Troubleshooting Tips

- **QR code won't scan**: Low screen brightness or poor lighting conditions can be the cause. Try increasing your computer's screen brightness and ensure the QR code is well lit. Hold your phone steady and at a comfortable distance (10-15 cm) from the screen.

- **"Connection failed" error**: Phone and Arduino UNO Q may be on different networks. Please verify that both devices are connected to the same Wi-Fi® network. Check your phone's Wi-Fi settings and ensure you're not on mobile data.

- **Video stream not loading**: Port 4912 may be blocked by your firewall or network restrictions. Check your computer's firewall settings and make sure port 4912 is open for incoming connections. If you're on a corporate network, you may need to request access from your IT administrator.

- **Laggy or stuttering video**: Network congestion or insufficient bandwidth can affect stream quality. Try reducing the resolution in your backend code to `(320, 480)` for better performance. Make sure no other devices are heavily using the network during streaming.

- **"Invalid secret" message**: The QR code has likely expired (typically after 5 minutes or after one successful connection). Refresh the web page to generate a new QR code with a fresh secret, then scan again.

- **Stream suddenly stops or freezes**: Your phone may have gone to sleep or lost network connection. Keep your phone awake by adjusting sleep settings in the IoT Remote app, or tap the screen occasionally. Verify that Wi-Fi® hasn't disconnected on your phone.

## Conclusion

In this tutorial, you learned how to transform your smartphone into a wireless input device for Arduino App Lab using the Arduino IoT Remote app. You successfully configured your network environment, paired your phone with the UNO Q via a QR code, and streamed live video to power an AI object detection model.

This integration eliminates the need for external USB webcams, allowing you to prototype computer vision applications more freely. By understanding the handshake mechanism between the Python® backend and the JavaScript frontend, you now have the foundation to build custom applications that leverage the powerful sensors already present in your mobile device.

### Next Steps

- **Integrate into Custom Apps:** Use the code snippets provided in the "Mobile Integration Feature" section to add phone camera support to your own Arduino App Lab projects.
- **Experiment with Other Bricks:** Try feeding the mobile camera stream into different Bricks, such as the `video_classifier` or `face_detection` Bricks.
- **Optimize Performance:** Experiment with different video resolutions and frame rates in the `WebSocketCamera` configuration to balance quality and latency for your specific network conditions.