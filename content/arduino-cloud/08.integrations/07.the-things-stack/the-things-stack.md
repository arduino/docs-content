---
title: The Things Stack
description: How Arduino Cloud connects to The Things Stack LoRaWAN network server when adding a LoRaWAN device.
tags: [Arduino Cloud, LoRaWAN, The Things Stack]
author: Karl Söderby & Arduino Team
---

[The Things Stack](https://www.thethingsindustries.com/stack/) (TTS) is the LoRaWAN network server Arduino® Cloud uses to receive data from LoRaWAN devices. It is connected to thousands of public LoRa® gateways. Rather than a standalone integration you configure separately, it is set up as part of adding a LoRaWAN® device: when you configure a device such as the MKR WAN 1300/1310 in Arduino Cloud, it is automatically registered on The Things Stack platform.

Because this registration happens during device setup, the full walkthrough lives with the device documentation.

<Alert type="info">

To set up a LoRaWAN device and its The Things Stack account, follow [Add a LoRaWAN Device](/arduino-cloud/devices/add-lorawan-device). It covers the frequency plan, the automatic registration, activating your The Things Stack account, and checking that data arrives.

</Alert>

## Related Articles

- [Add a LoRaWAN Device](/arduino-cloud/devices/add-lorawan-device)
- [Integrations Overview](/arduino-cloud/integrations/integrations-overview)
