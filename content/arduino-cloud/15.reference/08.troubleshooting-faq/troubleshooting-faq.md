---
title: Troubleshooting & FAQ
description: Common Arduino Cloud questions and quick fixes, grouped by area — devices, sketches and upload, dashboards, data, and account/plans.
tags: [Arduino Cloud, Troubleshooting, FAQ, Reference]
author: Karl Söderby & Arduino Team
---

Quick answers to the most common Arduino Cloud questions and issues. For the
full device connection walkthrough, see
[Troubleshoot Device Connections](/arduino-cloud/devices/troubleshoot-device-connections).

## Devices

**My device won't provision over USB.**
Confirm the [Cloud Agent](/arduino-cloud/devices/cloud-agent) is installed and
running, try a different USB cable/port, and make sure no other app (e.g. the
Serial Monitor) is holding the port.

**My device shows as offline.**
Check that its network credentials are correct, that it's within Wi-Fi® range
on a 2.4 GHz network (see
[Supported Wi-Fi Frequencies](/arduino-cloud/reference/supported-wifi-frequencies)),
and that the sketch calls `ArduinoCloud.update()` every loop.

**Where do I find my Device ID and Secret Key?**
The Device ID is on the device's page; the Secret Key is shown only once at
creation and can only be regenerated, not retrieved. See
[Device Identity & Secrets](/arduino-cloud/security-privacy/device-identity-secrets).

## Sketches & Upload

**The sketch won't compile — there's an `#error` about the connection handler.**
No device is associated with the Thing yet, so `thingProperties.h` can't
generate a real handler. Associate a device and the file regenerates. See
[Generated Sketch Files](/arduino-cloud/reference/generated-sketch-files).

**My callback isn't firing.**
Variable names are case-sensitive — the callback name must match the variable
exactly (a `test` variable → `onTestChange()`), and the variable must be Read
& Write.

**Can I upload wirelessly?**
Yes, via [OTA](/arduino-cloud/sketches-editor/upload-over-the-air) after the
first USB upload, on supported boards.

## Dashboards

**My widget shows placeholder data.**
It isn't linked to a variable yet — open the widget's settings (gear icon) and
bind it to a Cloud Variable.

**A widget is locked / says "Upgrade to unlock."**
It's one of the plan-gated widgets (Advanced Map, Advanced Chart, Image Map).
See the [Widget Catalog](/arduino-cloud/reference/widget-catalog).

## Data

**My data history looks truncated.**
Historical retention depends on your plan — see the
[Plans Feature Matrix](/arduino-cloud/reference/plans-feature-matrix).

**How do I get my data out?**
Use [Historical Data Export](/arduino-cloud/things-data/historical-data-export)
or the [AWS S3 Exporter](/arduino-cloud/integrations/aws-s3).

## Account & Plans

**Why is a feature unavailable?**
Many features (OTA, Triggers, advanced widgets, Node-RED) require a paid plan.
See [Plans, Limits & Quotas](/arduino-cloud/spaces-plans-account/plans-limits-quotas).

**How do I share with a team?**
Use a shared [Space](/arduino-cloud/spaces-plans-account/spaces) and invite
[Members](/arduino-cloud/spaces-plans-account/members-roles).

## Next Steps

- [Troubleshoot Device Connections](/arduino-cloud/devices/troubleshoot-device-connections)
- [Glossary](/arduino-cloud/reference/glossary)
- [What's New](/arduino-cloud/reference/whats-new)

## Trademark Acknowledgments

- **Wi-Fi®** is a registered trademark of Wi-Fi Alliance.
