---
title: 'Connecting to Arduino IoT Cloud using MicroPython'
description: 'Learn how to use the MicroPython library to connect to the Arduino IoT Cloud and control an LED.'
tags: 
  - IoT
  - MicroPython
author: 'Sebastian Romero'
libraries: 
  - name: Arduino IoT Cloud Python
    url: https://github.com/arduino/arduino-iot-cloud-py
---

## Introduction 

This tutorial guides you on how to use the MicroPython library to connect your Arduino device to the Arduino IoT Cloud.

## Goals

The goals of this tutorial are:

- Connect your Arduino device to your Wi-Fi network.
- Connect your Arduino device to the Arduino IoT Cloud.
- Control an LED using the Arduino IoT Cloud.

## Hardware & Software Needed

- Arduino Lab for MicroPython
- Arduino Giga or Portenta H7
- MicroPython >= 1.2 (installed on your Arduino device)



## Setting Up Your Device and IoT Cloud

Before we start, make sure you have MicroPython installed on your board. If you haven't you can follow [this tutorial](https://docs.arduino.cc/micropython/basics/board-installation). Then configure a "thing" in the [Arduino IoT Cloud](https://create.arduino.cc/iot/) consisting of two boolean variables called `led` and `ledSwitch`. To set up a "thing" and a corresponding dashboard, please follow these two tutorials:

- [IoT Cloud Variables](https://docs.arduino.cc/arduino-cloud/getting-started/cloud-variables)
- [IoT Cloud Dashboards & Widgets](https://docs.arduino.cc/arduino-cloud/getting-started/dashboard-widgets)

The resulting thing and dashboard should look similar to the following:

![Thing with two boolean variables.](./assets/thing.png)

![Dashboard with an LED and a Switch widget.](./assets/dashboard.png)

Also, your device needs to be registered. Follow the flow "Any Device" ("Manual") when clicking "Add" in the "Devices" tab.

![Dialog prompting to select setup flow](./assets/setup-device-prompt.png)

Give your board the desired name.

![Give your device a name of your choice.](./assets/set-device-name.png)

Eventually write down the Device ID / Secret Key pair that you will need to connect your device to Arduino IoT Cloud.

![The connection credentials to be written down.](./assets/get-key.png)

You will obtain a pair of device id and device key after registration. Store these details, along with your Wi-Fi credentials, in a `secrets.py` file. Here is an example of how `secrets.py` should look like:

```python
WIFI_SSID = "myNetwork"   # Network SSID
WIFI_PASSWORD = "passwordForWiFi"   # Network key
DEVICE_ID = b"ef77wer88-0432-4574-85e1-54e3d5cac861"
CLOUD_PASSWORD = b"TQHFHEKKKLSYMPB1OZLF"
```

This file should be copied over to the flash drive that mounts when MicroPython boots.  To do so you can use the file manager tool in Arduino Lab for MicroPython or drag & drop the file manually. Please note that the latter option is not recommended as the file system can potentially get corrupted when copying files manually.

After configuring your device, **assign** it to the thing that you created previously. This gives access permission to the registered board.



## Installing The Library

To install the Arduino IoT Cloud (Micro)Python library on your board, you first need to install `mpremote` if you haven't done it yet. You can install it using pip:

```bash
$ pip install mpremote
```

Run `mpremote connect list` to retrieve the serial number of your device. The output will look similar to this:

```
/dev/cu.usbmodem3871345733302 335B34603532 2341:055b Arduino Portenta Virtual Comm Port in HS Mode
```

Pass this serial number (the second value) to the install command:

```bash
$ mpremote connect id:335B34603532 mip install github:arduino/arduino-iot-cloud-py
```

This will install the library and all required dependencies on the board.

## Programming the Board

Here is the example code to copy and paste into your sketch. It connects your device

```python
from machine import Pin
import time
import network
import logging
from arduino_iot_cloud import ArduinoCloudClient

from secrets import WIFI_SSID
from secrets import WIFI_PASSWORD
from secrets import DEVICE_ID
from secrets import CLOUD_PASSWORD

led = Pin("LEDB", Pin.OUT) # Configure the desired LED pin as an output.

def on_switch_changed(client, value):
    # Toggles the hardware LED on or off.
    led.value(not value)
    
    # Sets the value of the cloud variable "led" to the current state of the LED
    # and thus mirrors the hardware state in the cloud.
    client["led"] = value

def wifi_connect():
    if not WIFI_SSID or not WIFI_PASSWORD:
        raise (Exception("Network is not configured. Set SSID and passwords in secrets.py"))
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wlan.isconnected():
        logging.info("Trying to connect. Note this may take a while...")
        time.sleep_ms(500)
    logging.info(f"WiFi Connected {wlan.ifconfig()}")

if __name__ == "__main__":
    # Configure the logger.
    # All message equal or higher to the logger level are printed.
    # To see more debugging messages, set level=logging.DEBUG.
    logging.basicConfig(
        datefmt="%H:%M:%S",
        format="%(asctime)s.%(msecs)03d %(message)s",
        level=logging.INFO,
    )
    
    # NOTE: Add networking code here or in boot.py
    wifi_connect()
    
    # Create a client object to connect to the Arduino IoT cloud.
    # For MicroPython, the key and cert files must be stored in DER format on the filesystem.
    # Alternatively, a username and password can be used to authenticate:
    client = ArduinoCloudClient(device_id=DEVICE_ID, username=DEVICE_ID, password=CLOUD_PASSWORD)

    # Register cloud objects.
    # Note: The following objects must be created first in the dashboard and linked to the device.
    # This cloud object is initialized with its last known value from the cloud. When this object is updated
    # from the dashboard, the on_switch_changed function is called with the client object and the new value.
    client.register("ledSwitch", value=None, on_write=on_switch_changed, interval=0.250)

    # This cloud object is updated manually in the switch's on_write_change callback to update the LED state in the cloud.
    client.register("led", value=None)

    # Start the Arduino IoT cloud client.
    client.start()

```

**Explanations:**

- `wifi_connect()` Connects to your local WiFi using the credentials specified in secrets.py.
- `client.register` Registers a variable that will be synced with the cloud.
- `on_switch_changed` Is the callback that gets executed when the `ledSwitch` variable is changed by toggling the switch on the cloud dashboard. This function in turn toggles the on-board LED and updates the cloud variable `led` that reflects the state of the on-board LED to be displayed in the cloud dashboard.
- `client.start()`Enters a loop that runs as long as the board is connected to the cloud and synchronises data as it runs.



## Testing It Out

Open Arduino Lab for MicroPython and connect to your board. Pasting the above code and run the script. Then open your Arduino IoT Cloud dashboard. You should see the registered "ledSwitch" and "led" widgets. Toggle the "ledSwitch", and the LED on your Arduino board should light up accordingly. The state of the "led" variable should also change, mirroring the state of the physical LED.



## Troubleshoot

If the code is not working, there are some common issues we can troubleshoot:

- Make sure MicroPython >= 1.2 is installed on your board.
- Check the Wi-Fi credentials in the `secrets.py` file.
- Ensure the device ID and Cloud password in the `secrets.py` file match with what is registered on the IoT Cloud.
- Make sure your IoT Cloud "thing" is correctly set up and your device is assigned to it.



## Conclusion

This tutorial has guided you through the process of connecting your Arduino device to the Arduino IoT Cloud using MicroPython. You learned how to install the necessary library, set up your device, and control an LED via the IoT Cloud. This opens up possibilities for more complex applications, as you can control and monitor your Arduino device remotely.