---
title: Keep Secrets Out of Shared Sketches
description: Keep Wi-Fi credentials, API keys, and other secrets out of a sketch you share, embed, or download.
tags: [Arduino Cloud, Cloud Editor, Secrets]
author: Karl Söderby & Arduino Team
---

Sharing a sketch — by [embedding](/arduino-cloud/sketches-editor/share-embed-sketches),
link, GitHub, or download — risks leaking anything hardcoded in it, such as
Wi-Fi® credentials or API keys. The Cloud Editor's **Secrets tab** keeps that
data out of the shared or published copy.

## How It Works

Any identifier you write as `SECRET_SOMETHING` in your sketch gets a
corresponding entry in a separate **Secrets** tab, stored apart from the
sketch's visible code.

## Adding a Secret

1. Replace a sensitive literal (e.g. `"myssid"`) with an all-caps `SECRET_`
   identifier, e.g. `SECRET_SSID`.
2. Use the **+** icon next to the sketch name and choose **Add Secrets Tab**.
3. Enter the actual value in the new Secrets tab.

An optional-value convention also exists — `SECRET_OPTIONAL_PASS` for values
such as a Wi-Fi® password that might not always be required.

## What Happens When You Share or Download

| Action | Result |
|---|---|
| **Share via URL** | The Secrets tab's values are blank for anyone else opening the link. |
| **Download** | An `arduino_secrets.h` file is generated inside the `.zip`, ready to fill in again if you open it in the offline Arduino IDE. |

This is the same `arduino_secrets.h` pattern used when provisioning boards
manually.

## Next Steps

- [Share & Embed Sketches](/arduino-cloud/sketches-editor/share-embed-sketches)
- [Collaborative Coding](/arduino-cloud/sketches-editor/collaborative-coding)
- [Cloud Editor Overview](/arduino-cloud/sketches-editor/cloud-editor-overview)
