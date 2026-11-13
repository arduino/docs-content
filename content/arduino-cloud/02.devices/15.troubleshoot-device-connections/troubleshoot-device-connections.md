---
title: Troubleshoot Device Connections
description: A practical reference for fixing common Arduino Cloud device issues — adding a device, Wi-Fi failures, offline devices, credentials, and OTA prerequisites.
tags: [Arduino Cloud, Troubleshooting, Devices]
author: Karl Söderby & Arduino Team
---

When a device won't connect, the cause is usually in one of a few places: the USB bridge, the network credentials, the board's stored configuration, or the prerequisites for a specific feature. This page groups the most common problems by symptom.

## Device Can't Be Added

The browser reaches a board through the [Cloud Agent](/arduino-cloud/devices/cloud-agent). If a connected board doesn't appear in the setup wizard or Cloud Editor, or the setup fails, try these steps in order.

### 1. Quick Checks

1. Disconnect and reconnect the board, and allow the connection if prompted.
2. Check that the board is powered: its power LED should be on. The Arduino Opta has no power LED, so it may be powered even if no LEDs are lit.
3. Confirm that the Cloud Agent is installed and running.
4. Close Arduino IDE or any other application that may be using the board, then try adding it again.

### 2. Check the USB Cable and Peripherals

- Use a working USB cable that supports data transfer. Some cables only carry power. If possible, try a different cable.
- If you use a USB hub or dock, make sure it is powered and working. If possible, connect the board directly to your computer.

### 3. Disconnect Shields and External Circuitry

External hardware can interfere with power, reset or serial communication. Detach the board from any shield or carrier, and disconnect jumper wires and external circuits.

### 4. Reset the Sketch

A faulty sketch or a broken Cloud configuration can prevent the computer from programming the board.

- **Setup over USB**: press the board's reset button twice quickly and check that the on-board LED pulses, then continue the setup. If the setup proceeds but fails again, repeat the double-press reset and continue. If it still fails, upload a safe sketch such as **Blink** or **BareMinimum** from Arduino IDE or the Cloud Editor, then add the device again.
- **Setup over Bluetooth®**: the board must run the Arduino Cloud provisioning sketch, shown by a pulsing "heartbeat" LED. If it doesn't, set the board up over USB first. If it runs the sketch but isn't detected, reset its Cloud configuration as described in [Provisioning & Network Configuration](/arduino-cloud/devices/network-configuration#resetting-the-board-configuration).

### 5. Install Drivers (Windows and Linux)

The Cloud Agent may not install all the drivers or configuration files that every board needs. Install the board package for your board once using [Arduino IDE](https://support.arduino.cc/hc/en-us/articles/360016119519-Add-boards-to-Arduino-IDE), allow the driver installation if prompted, and upload the Blink example to confirm it works. On Linux, you can also [fix the udev rules](https://support.arduino.cc/hc/en-us/articles/9005041052444-Fix-udev-rules-on-Linux) directly. This step is not needed on macOS.

### 6. Free the Serial Port

If Arduino Cloud shows "We could not find any Arduino device" or "Failed to open serial port. Is the device already in use?", another application is using the port:

- Close the Serial Monitor in Arduino IDE and any other application that may use the port.
- Restart the Cloud Agent, or restart your computer.
- If it still fails, [find and stop the process blocking the port](https://support.arduino.cc/hc/en-us/articles/4407830972050-Find-and-stop-process-blocking-a-port).

### 7. Repartition the Memory (QSPI Boards)

GIGA R1 WiFi, Opta, Portenta H7, Portenta H7 Lite, Portenta H7 Lite Connected and Portenta Machine Control boards use QSPI memory. If the partition scheme is corrupted or outdated, a red LED may blink, the board may not be detected, or you may see "Storage partition failed!" or "Storage Initialization Fail!" during setup. [Repartition the memory](https://support.arduino.cc/hc/en-us/articles/16206977438748-Reset-the-flash-memory-on-STM32H747-based-devices) with a supported scheme, then add the device again.

<Alert type="note">

The Cloud Agent listens on local ports `8991` to `9000`. Make sure a firewall or security tool doesn't block them. When you don't need the agent, for example during Bluetooth®-only setup or when working with a manual device, connection errors to these ports in the browser console can be ignored.

</Alert>

## Fails to Connect to Wi-Fi

If the board is set up but never connects over Wi-Fi®:

- **Use a 2.4 GHz network.** Arduino boards only work with 2.4 GHz networks. If your network only operates on the 5 GHz band, you can [create a 2.4 GHz hotspot on your phone](https://support.arduino.cc/hc/en-us/articles/14144656051740-Supported-Wi-Fi-bands#create-hotspot). See [Supported Wi-Fi Frequencies](/arduino-cloud/reference/supported-wifi-frequencies).
- **Use a distinct network name.** Avoid generic SSIDs such as "default" or "home": the board may try to connect to a different network with the same name.
- **Check the credentials.** Open the device page, select **Change** in the **Network** section, and re-enter the SSID and password. Check for typos. Then upload the sketch again to apply the new settings. For Provisioning 2.0 boards, you can also update the credentials as described in [Provisioning & Network Configuration](/arduino-cloud/devices/network-configuration#updating-a-stored-configuration).
- **Check the power supply.** Wi-Fi® uses more power than other operations. Connect the board directly to a USB port on your computer or to a dedicated power supply instead of a USB hub, use a good-quality cable, and check that the supply meets the board's input voltage.
- **Read the serial output.** Open the Serial Monitor and raise the debug level to see the connection errors printed by the sketch:

  ```arduino
  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();
  ```

## Device Shows Offline

If a device was set up successfully but shows **Offline** (see [Device Status & Lifecycle](/arduino-cloud/devices/device-status-lifecycle)), check the following. LoRaWAN® devices don't support device status, so this section does not apply to them.

1. **Power and network**: disconnect and reconnect the power, and check the power LED (the Opta has none). For Wi-Fi® devices, check that your router or access point is on and reachable.
2. **Credentials and sketch**: the board must run the sketch generated for its Thing. If another sketch, such as Blink, was uploaded, the board won't connect. On the device page, select the network name or type in the **Network** section, check the credentials, and upload the Thing sketch again if prompted.
3. **Network settings**: a home network with a default configuration usually allows Arduino Cloud connections. On managed networks, see [Configure your network for Arduino Cloud](https://support.arduino.cc/hc/en-us/articles/360017279260-Configure-your-network-for-Arduino-Cloud).
4. **Serial output**: connect the board over USB, open the Serial Monitor, and read the output. If nothing is printed, press the reset button. If there is still no output, the board is probably not running the Cloud sketch; upload it again.
5. **Sketch loop**: confirm that `ArduinoCloud.update()` is called on every iteration of `loop()` and is not blocked by long `delay()` calls.
6. **Manual devices**: confirm that your client is running and its `start()` or update loop hasn't exited.
7. **Delete and add the device again**: if nothing else helps, delete the device, add it again, and associate it with its Thing.

## Credentials Issues

- **Lost Secret Key** (third-party ESP32/ESP8266 and manual devices): the Secret Key is shown only once and cannot be retrieved. Delete the device and add it again to generate a new Device ID and Secret Key, then enter the new key in the device's network settings or in your client code.
- **LoRaWAN® credentials**: the credentials are added automatically when you set up the device. To reset them, delete the device and add it again.
- **Credentials don't seem to apply**: check which [provisioning version](/arduino-cloud/devices/network-configuration#provisioning-10-vs-20) the board uses. Provisioning 1.0 boards need a new sketch upload after you change the credentials. On Provisioning 2.0 boards, you can update or clear the stored configuration as described in [Provisioning & Network Configuration](/arduino-cloud/devices/network-configuration).

## Board Is Linked to Another Account

If a board was previously set up by someone else, for example a student who used it last term, and you can't set it up on your account, it's probably still **locked** to the previous owner's account:

- Ask the previous owner to open the device's page, turn **Lock to this account** off, and then delete the device from their account.
- If the device was already deleted while locked, the previous owner can no longer unlock it from their account.

See [Lock a Device to Your Account](/arduino-cloud/devices/device-lock) for how the lock works and the default for each type of space.

## OTA Prerequisites

Over-the-air uploads only work once a board meets these requirements:

- The board must have completed **at least one USB upload** of a Cloud-connected sketch.
- The board must support OTA and be **online**. OTA support depends on the board and its connectivity; see [Supported Boards & Capabilities](/arduino-cloud/reference/supported-boards-capabilities) and [Upload Over the Air](/arduino-cloud/sketches-editor/upload-over-the-air).
- Manual/generic devices do **not** support OTA, because it is specific to Arduino firmware.

## More Help

- [If your device can't be added to Arduino Cloud](https://support.arduino.cc/hc/en-us/articles/360019355679-If-your-device-can-t-be-added-to-Arduino-Cloud)
- [If your device is offline in Arduino Cloud](https://support.arduino.cc/hc/en-us/articles/13459093156764-If-your-device-is-offline-in-Arduino-Cloud)
- [If your Arduino device can't connect to a Wi-Fi network](https://support.arduino.cc/hc/en-us/articles/14794496872732-If-your-Arduino-device-can-t-connect-to-a-Wi-Fi-network)

## Next Steps

- [Cloud Agent](/arduino-cloud/devices/cloud-agent)
- [Provisioning & Network Configuration](/arduino-cloud/devices/network-configuration)
- [Device Status & Lifecycle](/arduino-cloud/devices/device-status-lifecycle)
