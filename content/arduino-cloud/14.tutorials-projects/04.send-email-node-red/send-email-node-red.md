---
title: Send Email Alerts With Node-RED
description: Build a Node-RED flow that reads an Arduino Cloud variable, filters it to threshold-crossing events, and emails you when a limit is crossed.
tags: [Arduino Cloud, Node-RED, Automation, Tutorial]
author: TODO
---

In this project you'll connect Arduino Cloud to [Node-RED](https://nodered.org/)
and build a flow that watches a sensor variable and emails you only when it
crosses a threshold — instead of spamming you with every reading. You'll pull
a Cloud Variable into a flow, filter it with a function node, and wire the
result to an email node.

**What you need:**

- A paid Arduino Cloud plan (Node-RED integration isn't available on Free).
- Node-RED installed locally (`npm install -g --unsafe-perm node-red`, then
  `node-red`, opening at `http://localhost:1880`).
- A Thing exposing a numeric variable (e.g. `humidity`).
- An API key (Client ID/Secret) from
  [API Keys](/arduino-cloud/apis-cli/cli-install-credentials).

## Step 1 — Install the Arduino Cloud Nodes

In the Node-RED editor, open **menu → Manage palette → Install**, search for
**Arduino**, and install `@arduino/node-red-contrib-arduino-iot-cloud`. This
adds five Arduino Cloud nodes, including **property out**.

![The Node-RED editor.](assets/nodered-01.png)

<Alert type="info">

Node-RED community packages are maintained outside Arduino Cloud's release
cycle — confirm the current package name/version in the palette manager (or
on npm) before installing.

</Alert>

## Step 2 — Read a Cloud Variable

Drag a **property out** node onto the canvas and configure it: add an Arduino
connection authenticated with your Client ID/Secret, then pick your Thing and
the variable to read (e.g. `humidity`):

![Selecting a Thing and variable to pull data from.](assets/nodered-05.gif)

Wire an `inject` node into it and a `debug` node on its output, then **Deploy**
— you should see the variable's live value in the sidebar console.

## Step 3 — Filter to Threshold Crossings

Add a **function** node between **property out** and the email node. This
JavaScript forwards a message only the first time the value rises above 60
(and again when it drops back below), instead of on every reading:

```javascript
let data = msg.payload;
let trigger = context.get("status");

if (typeof trigger == "undefined") trigger = false;

if (data > 60 && !trigger) {
  trigger = true;
  context.set("status", trigger);
  return msg;
}

if (data < 60 && trigger) {
  trigger = false;
  context.set("status", trigger);
  return msg;
}
```

## Step 4 — Send the Email

Install an email node the same way as the Arduino nodes — in **Manage
palette**, search **Email** and install `node-red-node-email`. Wire the
**email** node to the function node's output and configure it with your SMTP
credentials and recipient address.

<Alert type="warning">

Needs verification: email node setup (SMTP host, port, and app-password
requirements) depends on your mail provider. Confirm your provider's current
SMTP settings before publishing.

</Alert>

Deploy the flow. Now, whenever `humidity` crosses 60, you get a single email
alert rather than a constant stream.

## Next Steps

- [Node-RED Integration](/arduino-cloud/integrations/node-red)
- [REST API & SDKs](/arduino-cloud/apis-cli/rest-api-sdks)
- [Cloud Variables](/arduino-cloud/things-data/cloud-variables)
