---
title: Developer Overview
description: How the Arduino Cloud developer surface fits together — the REST management API vs. the device-connection libraries, and which to reach for.
tags: [Arduino Cloud, API, Developer]
author: Karl Söderby, Fabrizio Mirabito
---

"The API" for Arduino Cloud actually covers two distinct things. Keeping them separate avoids the most common source of confusion — they use different protocols, different credentials, and run in different places.

| | REST API | Device-connection libraries |
|---|---|---|
| **Purpose** | CRUD + history on Devices/Things/Properties/Dashboards | Real-time property sync for a running device |
| **Protocol** | HTTPS | MQTT |
| **Used from** | Servers, scripts, CI, backends | The device itself (or a manual/generic virtual device) |
| **Auth** | OAuth2 client-credentials (API key) | Device ID + Secret Key, or cert + key |
| **Covered in** | [REST API & SDKs](/arduino-cloud/apis-cli/rest-api-sdks) | [Device Libraries](/arduino-cloud/device-libraries) |

## Which Tool for Which Job

- **Administer the account** (create a Thing, provision a device, read history, bulk-tag devices): use the [REST API](/arduino-cloud/apis-cli/rest-api-sdks), an SDK, or [arduino-cloud-cli](/arduino-cloud/apis-cli/cli-install-credentials).
- **Connect a running device** and exchange live variable values: use the [device library](/arduino-cloud/device-libraries) for your language.
- **Script repeatable terminal operations** (CI/CD, mass OTA): the [CLI](/arduino-cloud/apis-cli/cli-install-credentials) wraps the common REST operations. Anything the CLI doesn't expose yet (e.g. raw history/Series queries) needs a direct REST call.

<Alert type="warning">

Naming gotcha: `arduino-iot-js` (MQTT, device-side) and `@arduino/arduino-iot-client` (REST, server-side) are two completely different npm packages with similar names — the same pattern applies in Python (`arduino-iot-cloud` vs. `arduino-iot-client`). Double-check which one a task actually needs before installing.

</Alert>

## Compatibility Policy

The REST API is versioned per resource group (for example Devices and Things are at v2, Dashboards at v3), and the generated SDKs track the same OpenAPI spec. Versions bump over time, so verify exact method and field names against the [generated client repos](/arduino-cloud/apis-cli/rest-api-sdks) or the [interactive spec](https://docs.arduino.cc/cloud-api/) rather than assuming a field hasn't moved.

<Alert type="warning">

Needs verification: Arduino Cloud does not publish a formal API deprecation or backward-compatibility SLA at a known URL. Confirm the current policy before documenting specific support guarantees.

</Alert>

## Next Steps

- [REST API & SDKs](/arduino-cloud/apis-cli/rest-api-sdks)
- [Device Libraries](/arduino-cloud/device-libraries)
- [CLI: Install & Credentials](/arduino-cloud/apis-cli/cli-install-credentials)
