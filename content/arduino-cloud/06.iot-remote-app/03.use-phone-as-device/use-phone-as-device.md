---
title: Use Your Phone as a Device
description: Stream your phone's built-in sensors (GPS, IMU, light, and more) into Arduino Cloud as Cloud Variables.
tags: [Arduino Cloud, Remote App, Mobile Sensors]
author: Jacob Hylén
---

The IoT Remote app can turn your phone into an Arduino Cloud device. Its
built-in sensors — GPS, accelerometer/gyroscope, light sensor, compass, and
more depending on the phone — stream directly into
[Cloud Variables](/arduino-cloud/things-data/cloud-variables), usable on
dashboards or synchronized to control other Things (for example, driving a
servo based on the phone's orientation).

## Enabling Phone as Device

In the app, open **Settings** (top-right) and select **Phone as Device**, then
complete the short configuration process. This registers your phone in Arduino
Cloud: a **Thing and a dashboard are created automatically**, named after your
account and phone (e.g. `Karl_s S20_Dashboard`), showing your phone's sensor
data in real time — typically GPS location, accelerometer, and compass,
depending on the phone.

The phone's data is stored in ordinary [Cloud Variables](/arduino-cloud/things-data/cloud-variables),
so you can chart, store, and sync them like any other. Note the auto-created
Thing **cannot be programmed as a regular device**.

## Typical Workflow

1. [Install the app](/arduino-cloud/iot-remote-app/iot-remote-app-overview)
   and log in.
2. Enable **Phone as Device** and pick the sensors you want to stream.
3. Add the phone's variables to a [Thing](/arduino-cloud/things-data/things),
   then build a [Dashboard](/arduino-cloud/dashboards/dashboards) around them —
   for example, a [Map](/arduino-cloud/dashboards/track-location-map) showing
   the phone's GPS location.
4. Optionally link a phone variable to another device's variable so the phone
   drives real hardware.

<Alert type="info">

Because the phone appears as an ordinary device, its sensor variables behave
like any other Cloud Variable — they're charted, stored as
[historical data](/arduino-cloud/things-data/historical-data-export), and can
be shared across Things.

</Alert>

## Next Steps

- [Use Dashboards on Your Phone](/arduino-cloud/iot-remote-app/use-dashboards-on-phone)
- [Browse Devices & Data](/arduino-cloud/iot-remote-app/browse-devices-data)
- [Cloud Variables](/arduino-cloud/things-data/cloud-variables)
