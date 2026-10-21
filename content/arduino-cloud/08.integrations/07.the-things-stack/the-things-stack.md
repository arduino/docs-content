---
title: The Things Stack
description: How Arduino Cloud connects to The Things Stack LoRaWAN network server when adding a LoRaWAN device.
tags: [Arduino Cloud, LoRaWAN, The Things Stack]
author: Karl Söderby & Arduino Team
---

[The Things Stack](https://www.thethingsindustries.com/stack/) is the LoRaWAN®
network server Arduino Cloud uses to receive data from LoRaWAN® devices. Rather
than a standalone integration you configure separately, it is set up as part of
registering a LoRaWAN® device — the device joins a The Things Stack application,
and its uplinks are forwarded into Arduino Cloud as Cloud Variable updates.

Because the configuration (application, device registration, and the webhook
that links the two) happens during device setup, the full walkthrough lives
with the device documentation.

## Next Steps

- [Add a LoRaWAN Device](/arduino-cloud/devices/add-lorawan-device)
- [Integrations Overview](/arduino-cloud/integrations/integrations-overview)
