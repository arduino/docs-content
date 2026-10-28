---
title: Troubleshoot Device Connections
description: A practical reference for fixing common Arduino Cloud device issues — USB detection, Wi-Fi failures, offline devices, credentials, and OTA prerequisites.
tags: [Arduino Cloud, Troubleshooting, Devices]
author: Karl Söderby & Arduino Team
---

When a device won't connect, the cause is usually in one of a few places: the USB bridge, the network credentials, the board's stored configuration, or the prerequisites for a specific feature. This page groups the most common problems by symptom.

## Board Not Detected Over USB

The browser reaches a board through the [Cloud Agent](/arduino-cloud/devices/cloud-agent). If a connected board doesn't appear in the provisioning wizard or Cloud Editor:

- Confirm the Cloud Agent is installed **and running**.
- Reconnect the USB cable, and try a different cable or port — some cables are power-only and carry no data.
- Restart the browser so it re-scans the agent's local ports (`127.0.0.1:8991`–`9000`).
- Check that a firewall or security tool isn't blocking those local ports.

<Alert type="note">

Connection-refused errors to ports `8991`–`9000` in the browser console are harmless when the agent isn't needed — for example during Bluetooth®-only provisioning or when working with a manual device.

</Alert>

## Fails to Connect to Wi-Fi

If the board is provisioned but never comes online over Wi-Fi®:

- Double-check the SSID and password — re-enter them via [Network Configuration](/arduino-cloud/devices/network-configuration).
- Confirm the network is **2.4 GHz** where the board requires it, and isn't a captive-portal network that needs a browser login.
- Open the Serial Monitor and raise the debug level to read the connection errors the sketch prints:

  ```arduino
  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();
  ```

<Alert type="warning">

Needs verification: the exact debug strings printed on a failed Wi-Fi® or handshake attempt vary by board and library version. Read them from the Serial Monitor on your specific hardware rather than assuming a fixed message.

</Alert>

## Device Shows Offline

A device that provisioned successfully but reports **offline** in the Devices list (see [Device Status & Lifecycle](/arduino-cloud/devices/device-status-lifecycle)):

- Verify the board is powered and running the Cloud-generated sketch (not, for example, a plain Blink sketch that overwrote it).
- Confirm `ArduinoCloud.update()` is called every iteration of `loop()` — the connection drops if it isn't serviced.
- For manual devices, confirm your client is running and its `start()` / update loop hasn't exited.

## Credentials and Crypto Issues

- **Lost Secret Key** — the key is shown only once and can't be retrieved, only regenerated. Regenerate it from the device page and update your sketch or client.
- **Secure-element boards** — MKR, Nano 33 IoT, Portenta, and similar boards store a hardware-backed certificate. If provisioning fails at the crypto step, retry provisioning over USB; a corrupted or incomplete secure-element provisioning usually clears on a clean re-run.
- **Wrong network generation** — if credentials don't seem to apply, the board may be on the wrong [provisioning generation](/arduino-cloud/devices/network-configuration#provisioning-10-vs-20); migrating or clearing the stored configuration resolves stale credentials.

## Board Is Linked to Another Account

If a board was previously set up by someone else, for example a student who used it last term, and you can't set it up on your account, it's probably still **locked** to the previous owner's account:

- Ask the previous owner to open the device's page, turn **Lock to this account** off, and then delete the device from their account.
- If the device was already deleted while locked, the previous owner can no longer unlock it from their account.

See [Lock a Device to Your Account](/arduino-cloud/devices/device-lock) for how the lock works and the default for each type of space.

## OTA Prerequisites

Over-the-air uploads only work once a board has met their requirements:

- The board must have completed **at least one USB upload** of a Cloud-connected sketch first.
- It must be a Wi-Fi® or Ethernet board configured for OTA and currently online.
- Manual/generic devices do **not** support OTA — it's specific to Arduino firmware.

## Next Steps

- [Cloud Agent](/arduino-cloud/devices/cloud-agent)
- [Network Configuration](/arduino-cloud/devices/network-configuration)
- [Device Status & Lifecycle](/arduino-cloud/devices/device-status-lifecycle)
