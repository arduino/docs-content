---
title: Push Notifications
description: Receive push notifications on your phone from the Arduino IoT Remote app when a Trigger condition is met.
tags: [Arduino Cloud, Remote App, Push Notifications]
author: Karl Söderby & Arduino Team
---

The IoT Remote app can receive **push notifications** driven by [Triggers](/arduino-cloud/automations/triggers-and-alerts) — useful for alerts such as "sensor value dropped below threshold" or "power consumption too high." The app is the delivery target; the condition that fires the notification is defined by a Trigger in Arduino Cloud.

<Alert type="note">

Push notifications require a Maker plan or higher, because [Triggers](/arduino-cloud/automations/triggers-and-alerts) is plan-gated on the free tier.

</Alert>

## Requirements

- An [Arduino Cloud](https://app.arduino.cc/) account with a Maker plan or higher.
- A [configured device](/arduino-cloud/devices/devices-overview) in Arduino Cloud.
- An Android phone or iPhone.
- The Arduino IoT Remote app:
  - [App Store](https://apps.apple.com/us/app/arduino-iot-cloud-remote/id1514358431)
  - [Google Play](https://play.google.com/store/apps/details?id=cc.arduino.cloudiot)

## Setting Up Push Notifications

Push notifications support **Boolean** and **String** variables, fired when a Boolean is `true` or a String matches. The notification is delivered to every phone logged in to the account.

1. [Install the app](/arduino-cloud/iot-remote-app/iot-remote-app-overview) and log in. Open **Settings** (avatar, top right) > **Manage push notifications** and allow notifications. The OS-level permission prompt varies by phone.
2. In Arduino Cloud, create a [Thing](/arduino-cloud/things-data/things) with a Boolean variable named `trigger`, attach your device, and add a callback that resets the variable so it can fire again:

    ```arduino
    void onTriggerChange() {
      trigger = false;
    }
    ```

3. Upload the sketch and check that the device is online.
4. Open **Triggers**, create a Trigger, click **Cloud Variable**, and link the `trigger` variable.
5. Select **Send Push Notifications**, enter a **title** and **description** (for example, `Reminder to make coffee!`), and click **Done**.
6. To test, add a **Switch** widget linked to `trigger` on a [dashboard](/arduino-cloud/dashboards/dashboards) and flip it. The switch returns to off and the notification appears on your phone.

A Trigger is active as soon as it is created. Disable or enable it at any time with its switch on the **Triggers** page.

<Alert type="info">

Notifications count toward a daily notification quota that depends on your plan. See [Arduino Cloud plans](https://cloud.arduino.cc/plans) for details.

</Alert>

## Next Steps

- [Triggers & Alerts](/arduino-cloud/automations/triggers-and-alerts)
- [Browse Devices & Data](/arduino-cloud/iot-remote-app/browse-devices-data)
