---
title: Push Notifications
description: Receive push notifications on your phone from the Arduino IoT Remote app when a Trigger condition is met.
tags: [Arduino Cloud, Remote App, Push Notifications]
author: Karl Söderby & Arduino Team
---

The IoT Remote app can receive **push notifications** driven by [Triggers](/arduino-cloud/automations/triggers-and-alerts) — useful for alerts such as "sensor value dropped below threshold" or "power consumption too high." The app is the delivery target; the condition that fires the notification is defined by a Trigger in Arduino Cloud.

<Alert type="note">

Push notifications require a paid plan, because [Triggers](/arduino-cloud/automations/triggers-and-alerts) is plan-gated on the free tier.

</Alert>

## Setting Up Push Notifications

1. [Install the app](/arduino-cloud/iot-remote-app/iot-remote-app-overview) and log in.
2. In the app, open **Settings** (avatar, top right) → **Manage push notifications** and allow notifications. The OS-level permission prompt varies by phone.
3. In Arduino Cloud, [create a Trigger](/arduino-cloud/automations/triggers-and-alerts): click **Cloud Variable**, link your `boolean`/`string` variable, then select **Send Push Notifications** and fill in a **title** and **description** for the message. Click **Done**.

Once the Trigger's condition is met, the notification is delivered to the app on any phone logged in to that account. Push notifications currently support **boolean** and **string** variables — fired when a boolean is `true` or a string matches. Triggers can be toggled on/off from the Triggers page.

## Next Steps

- [Triggers & Alerts](/arduino-cloud/automations/triggers-and-alerts)
- [Browse Devices & Data](/arduino-cloud/iot-remote-app/browse-devices-data)
