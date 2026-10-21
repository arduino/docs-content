---
title: Browse Devices & Data
description: View your Arduino Cloud devices and their latest and historical Cloud Variable data from the IoT Remote mobile app.
tags: [Arduino Cloud, Remote App, Devices, Data]
author: TODO
---

Beyond [Dashboards](/arduino-cloud/iot-remote-app/use-dashboards-on-phone),
the IoT Remote app lets you check in on your
[devices](/arduino-cloud/devices/devices-overview) and the data their
[Cloud Variables](/arduino-cloud/things-data/cloud-variables) are producing —
a quick way to confirm a device is online and see its latest readings without
opening a browser.

## Checking a Device's Status

Each of your devices shows a status indicator reflecting whether it's
currently connected to Arduino Cloud, the same **Online**/**Offline** state
shown in the browser's Devices list. Use it to confirm a device is reachable
before expecting fresh data from it. For what drives this state, see
[Device Status & Lifecycle](/arduino-cloud/devices/device-status-lifecycle).

## Viewing Latest and Historical Values

Because the app reads from the same Cloud Variables as the browser, each
variable shows its **latest value** live, and widgets backed by time-series
data (such as a Chart) let you look back over a selected time range — the
same [historical data](/arduino-cloud/things-data/historical-data-export)
stored behind every variable.

<Alert type="info">

The most reliable way to browse a device's data in the app is through a
[Dashboard](/arduino-cloud/dashboards/dashboards) whose widgets are linked to
that device's variables. Build the dashboard once in the browser and it's
available on the phone immediately.

</Alert>

<Alert type="warning">

Needs verification: the exact in-app navigation for browsing devices directly
(screen names, whether a standalone device/data browser exists separate from
dashboards, and the labels used) wasn't confirmed hands-on this pass. Verify
against a current app build before documenting a specific tap-by-tap flow.

</Alert>

## Next Steps

- [Use Dashboards on Your Phone](/arduino-cloud/iot-remote-app/use-dashboards-on-phone)
- [Device Status & Lifecycle](/arduino-cloud/devices/device-status-lifecycle)
- [Historical Data & Export](/arduino-cloud/things-data/historical-data-export)
