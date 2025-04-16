---
title: 'Webhooks Integration with Arduino Cloud'
description: 'Learn how to set up webhooks with the Arduino Cloud to integrate with third-party platforms like IFTTT.'
tags:
  - Webhooks
  - Arduino Cloud
  - IFTTT
author: 'Liam Aljundi'
---

## Introduction

Webhooks allow your devices on Arduino Cloud to automatically send and receive messages from other services. For instance, you can use webhooks to get notifications when a device’s status changes or send data from your Arduino projects to services like Google Sheets or IFTTT.

This guide will walk you through setting up webhooks in Arduino Cloud and connecting them to third-party platforms, specifically IFTTT, to automate tasks.

## Goals

By the end of this guide, you will:

- Learn how to set up and configure webhooks in Arduino Cloud.
- Understand the integration process with third-party platforms like IFTTT.
- Set up an example where data from Arduino Cloud is sent to Google Sheets using IFTTT.

## Hardware & Software Requirements

Before starting, ensure you have the following:

- **Arduino Create Agent** installed on your system: [Download Here](https://github.com/arduino/arduino-create-agent)
- **Arduino account**: [Sign Up Here](http://create.arduino.cc/iot)
- A Cloud-compatible Arduino board.

You can read more about compatible boards [here](/arduino-cloud/guides/overview#compatible-boards).

## Setting Up the Webhook

Webhooks in Arduino Cloud can be linked to **Things**—which are virtual representations of your devices. These webhooks enable real-time data sharing with third-party platforms. For example, you can receive notifications when a device gets disconnected, or send live sensor data to a Google Spreadsheet.

In this tutorial, we’ll use **IFTTT** (If This Then That), a platform that enables you to automate actions between different services. IFTTT lets you create **Applets** that trigger actions like updating a Google Sheet when a webhook receives data.

### IFTTT Configuration

Start by creating an Applet on IFTTT. Here’s how:

1. Go to the [IFTTT website](https://maker.ifttt.com) and log in.
2. Click **Create** in the top-right corner, then select **If This**.
3. In the search bar, type **Webhooks** and select the Webhooks service.
4. Choose **Receive a web request**.
5. In the **Event Name** field, type `message` and click **Create trigger**.
6. Click on **Then That**, search for **Google Sheets**, and select the **"Add row to spreadsheet"** option.
7. Keep the default settings and click **Create action**.
8. Click **Continue**, optionally change the Applet title, and hit **Finish**.

Now, your trigger and action are set. The next step is to grab the Webhook URL you will use in Arduino Cloud.

To find the Webhook URL:
1. Go to your IFTTT profile (click your profile picture in the top right).
2. Click on **My Services** > **Webhooks** > **Documentation**.

![Finding Webhook Link](assets/finding-webhook-link.png)

### Linking Webhook to an Arduino Cloud Thing

Now that your IFTTT Applet is ready, it’s time to link it to an Arduino Cloud **Thing**:

1. [Sign in to Arduino Cloud](https://create.arduino.cc/iot) and open the **Arduino Cloud** dashboard.
2. Navigate to **Things** > **Create Thing** to start a new Thing.
3. Create a **Variable** for your Thing. In this case, create a **message** variable with the type set to **Character String**.
4. Select your **Device** and configure your **Network** in the menu on the right.
5. Under **Data Forwarding (Webhook)**, click **Configure**.
6. Enter the Webhook URL you got from IFTTT in the provided field.

![Set Webhook](./assets/webhooks-02.png)

7. Finally, navigate to the **Sketch** tab and upload the automatically generated code to your board. This will enable your device to send data via the webhook.

When data is sent from Arduino Cloud, the following information will be shared through the webhook:

- `"event_id": "EVENT_UUID"`
- `"webhook_id": "WEBHOOK_ID"`
- `"device_id": "DEVICE_UUID"`
- `"thing_id": "THING_UUID"`
- **Variable values**: Each variable in your Thing will be represented as an object with details such as the value and timestamp.

Example:

```js
{
  "values": [
    {
      "id": "VARIABLE_01_ID",
      "name": "NAME_OF_VARIABLE_01",
      "value": "VARIABLE_01_VALUE",
      "persist": true/false,
      "updated_at": "DATE",
      "created_by": "USERID"
    },
    {
      "id": "VARIABLE_02_ID",
      "name": "NAME_OF_VARIABLE_02",
      "value": "VARIABLE_02_VALUE",
      "persist": true/false,
      "updated_at": "DATE",
      "created_by": "USERID"
    }
  ]
}
```

## Testing the Webhook

To test the webhook, we need to create a *Messenger widget*. We can do that by:

**1.** Navigating to [*Dashboards*](https://app.arduino.cc/dashboards) -> *Edit* -> *Add* -> stay on the *Widgets tab* -> select "Messenger".

![Add Messenger Widget](./assets/webhooks-04.png)

**2.** Press on *Link Variable*, select the Thing we created, then the **"message"** Variable.

![Link Widge](./assets/webhooks-05.png)

In the "messenger widget", we are modifying the value of the "message" Variable. Whenever we send a message, the "message" Variable is updated and using the webhook we set, the updates are sent to the spreadsheet file created by IFTTT.

To try it out, all you need to do is to navigate to your **Dashboards** on the Arduino Cloud and send messages using the **Messenger Widget**. The messages, along with the exact date and time will be found in the Google Sheets file created by IFTTT, on our Google account. To access this file, you need to navigate to your [Google Sheets](https://docs.google.com/spreadsheets) -> find and open the file names **"IFTTT_Maker_Webhooks_Events"**.

![Setting a webhook](assets/ezgif.com-crop.gif)

## Available Platforms

In addition to IFTTT, here are examples of platforms that you can use webhooks with:

### Zapier

[Zapier](https://zapier.com/) works similarly to IFTTT. In addition to connecting your APIs quickly using **Zaps**, you can use Zapier's visual builder, which allows you to build an integration and preview data in real time.

### Google Services

- [**Google Cloud APIs**](https://cloud.google.com/apis/docs/overview): with Google APIs you can develop application programming interfaces (APIs) to communicate with Google services such as Search, Gmail, Translate or Google Maps apps or other applications like Arduino Cloud.

- [**Google Script**](https://developers.google.com/apps-script): allows you to interact with all your Google G-Suite files such as Google Sheets, Docs and more.

## Additional Tools for Webhook Testing

- **Beeceptor**: A powerful tool to intercept and test your webhooks.
- **httpbin**: A simple HTTP request/response service that can be used to test webhooks.
