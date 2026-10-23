---
title: Integrations Overview
description: A comparison of the ways Arduino Cloud connects to external services, from voice assistants to data exporters, and when to use each.
tags: [Arduino Cloud, Integrations]
author: Karl Söderby & Arduino Team
---

Arduino Cloud connects to external services in several different ways, each suited to a different goal — exposing a variable to a voice assistant, pushing every update to an automation platform, pulling data into a flow editor, or exporting long-term history to your own data store. This page compares the options so you can pick the right one before diving into its setup page.

## Choosing an Integration

| Integration | Direction | Best for | Plan |
|---|---|---|---|
| [Amazon Alexa](/arduino-cloud/integrations/amazon-alexa) | Cloud ⇄ service | Voice/app control of a smart-home variable | Free |
| [Google Home](/arduino-cloud/integrations/google-home) | Cloud ⇄ service | Voice/app control via Google Assistant | Free |
| [IFTTT, Zapier & Webhooks](/arduino-cloud/integrations/ifttt-zapier-webhooks) | Cloud → service | Reacting to variable updates on any webhook-capable platform | Free (Thing-level) |
| [Node-RED](/arduino-cloud/integrations/node-red) | Cloud ⇄ flow | Custom logic, notifications, bridging to other systems | Paid |
| [AWS S3 Exporter](/arduino-cloud/integrations/aws-s3) | Cloud → store | Long-term CSV export of time-series data | Paid / Business |
| [The Things Stack](/arduino-cloud/integrations/the-things-stack) | Network → Cloud | Bringing LoRaWAN® device data into the Cloud | Free |
| [PLC IDE](/arduino-cloud/integrations/plc-ide) | Device → Cloud | Connecting industrial PLC projects to the Cloud | Varies |

## Voice Assistants

[Amazon Alexa](/arduino-cloud/integrations/amazon-alexa) and [Google Home](/arduino-cloud/integrations/google-home) both expose smart-home-compatible Cloud Variables (switches, dimmers, colored lights) as devices you can control by voice or from each platform's app. They require no extra device code — the assistant writes directly to the variable, and the sketch's `on...Change()` callback drives the hardware.

## Automation Platforms

[Webhooks](/arduino-cloud/automations/webhooks) are the generic bridge to automation platforms. [IFTTT, Zapier & Webhooks](/arduino-cloud/integrations/ifttt-zapier-webhooks) covers connecting a Thing's outgoing webhook to services like Google Sheets, where each variable update becomes a spreadsheet row or triggers another action.

## Flow Editors and Code

[Node-RED](/arduino-cloud/integrations/node-red) uses a dedicated node package to read and write variables inside a visual flow — the right choice when an integration needs custom logic, filtering, or fan-out to multiple destinations. For full programmatic control, the [APIs and CLI](/arduino-cloud/apis-cli/developer-overview) underpin every integration here.

## Data Export and Networks

The [AWS S3 Exporter](/arduino-cloud/integrations/aws-s3) periodically writes aggregated time-series data to an S3 bucket as CSV, for warehousing and offline analysis. [The Things Stack](/arduino-cloud/integrations/the-things-stack) is the LoRaWAN® network server used when [adding a LoRaWAN® device](/arduino-cloud/devices/add-lorawan-device).

## Next Steps

- [Amazon Alexa](/arduino-cloud/integrations/amazon-alexa)
- [Webhooks](/arduino-cloud/automations/webhooks)
- [AWS S3 Exporter](/arduino-cloud/integrations/aws-s3)
