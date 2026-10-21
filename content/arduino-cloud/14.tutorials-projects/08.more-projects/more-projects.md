---
title: More Arduino Cloud Projects
description: A curated list of additional Arduino Cloud projects and tutorials — voice control, messaging notifications, and more — with links to the building blocks that power them.
tags: [Arduino Cloud, Projects, Tutorial]
author: TODO
---

Beyond the projects in this section, there's a wide library of Arduino Cloud
tutorials across the Arduino Project Hub and documentation site. This page
curates a few popular ones and points to the Arduino Cloud building blocks
each relies on, so you can adapt them to your own hardware.

<Alert type="warning">

Needs verification: the external project URLs below live on the Arduino
Project Hub / main docs site, outside this documentation tree. Confirm each
exact link is current and published before shipping this page.

</Alert>

## Voice & Smart Home

- **Voice-Controlled TV With Alexa** — expose a `CloudTelevision` variable and
  control channel, volume, and power from Amazon Alexa. Built on the
  [Amazon Alexa integration](/arduino-cloud/integrations/amazon-alexa) and the
  television [Cloud Variable type](/arduino-cloud/reference/cloud-variable-types).
- **Google Home Light Control** — drive a `ColoredLight` or `DimmedLight` from
  Google Assistant via the
  [Google Home integration](/arduino-cloud/integrations/google-home).

## Messaging & Notifications

- **Telegram Notifications From a Sensor** — send chat alerts when a reading
  crosses a threshold, typically via a
  [webhook](/arduino-cloud/automations/webhooks) or a
  [Node-RED flow](/arduino-cloud/integrations/node-red).
- **IFTTT / Zapier Automations** — trigger thousands of third-party actions
  from a Cloud Variable using
  [IFTTT, Zapier & Webhooks](/arduino-cloud/integrations/ifttt-zapier-webhooks).

## Data & Analytics

- **Export Data to AWS S3** — stream historical data to your own storage with
  the [AWS S3 Exporter](/arduino-cloud/integrations/aws-s3-exporter).
- **Historical Data Download** — pull a Thing's recorded data for offline
  analysis via [Historical Data Export](/arduino-cloud/things-data/historical-data-export).

## Next Steps

- [Integrations Overview](/arduino-cloud/integrations/integrations-overview)
- [Automations](/arduino-cloud/automations/choose-an-automation)
- [Tutorials & Projects](/arduino-cloud/tutorials-projects)
