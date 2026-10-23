---
title: Glossary
description: Alphabetical definitions of the key Arduino Cloud terms — Device, Thing, Cloud Variable, Dashboard, Trigger, OTA, and more.
tags: [Arduino Cloud, Glossary, Reference]
author: Karl Söderby & Arduino Team
---

Short definitions of the core Arduino Cloud concepts, each linking to its main documentation page.

## A–C

- **Cloud Agent** — A small local application that lets the browser talk to a board plugged into your computer over USB, for provisioning and uploads. See [Cloud Agent](/arduino-cloud/devices/cloud-agent).
- **Cloud Variable** — A data point a Thing exchanges between a device and Arduino Cloud, kept in sync on both sides. See [Cloud Variables](/arduino-cloud/things-data/cloud-variables).
- **Connection Handler** — The object (e.g. `WiFiConnectionHandler`) in `thingProperties.h` that manages a device's network connection to the Cloud. See [Generated Sketch Files](/arduino-cloud/reference/generated-sketch-files).

## D

- **Dashboard** — A page of widgets bound to Cloud Variables, used to visualize and control a project. See [Dashboards](/arduino-cloud/dashboards/dashboards).
- **Device** — The physical (or virtual) hardware registered in Arduino Cloud that runs your code and exchanges data. See [Devices Overview](/arduino-cloud/devices/devices-overview).
- **Device ID** — A device's unique, non-secret identifier, safe to reference in code. See [Device Identity & Secrets](/arduino-cloud/security-privacy/device-identity-secrets).

## O–P

- **OTA (Over-the-Air)** — Uploading a new sketch to a device wirelessly, after its first USB upload. See [Upload Over the Air](/arduino-cloud/sketches-editor/upload-over-the-air).
- **Provisioning** — The one-time process of registering a device with the Cloud and configuring its secure credentials. See [Add a Wi-Fi Board](/arduino-cloud/devices/add-wifi-board).

## S

- **Secret Key** — A private credential, shown only once at device creation, used (with the login) to authenticate boards without a secure element. See [Device Identity & Secrets](/arduino-cloud/security-privacy/device-identity-secrets).
- **Sketch** — The Arduino/C++ program that runs on a device and connects it to the Cloud. See [Generated Sketch Files](/arduino-cloud/reference/generated-sketch-files).
- **Space** — A workspace that groups Things, devices, dashboards, and members; can be private or shared. See [Spaces](/arduino-cloud/spaces-plans-account/spaces).

## T–U

- **Thing** — The container for a project — its device association, Cloud Variables, and data history. See [Things](/arduino-cloud/things-data/things).
- **Template** — A pre-built Thing/dashboard/sketch bundle that sets up a project in a few steps. See [Integrations](/arduino-cloud/integrations/integrations-overview).
- **Trigger** — An automation that runs an action (email, webhook, push notification) when a condition is met. See [Triggers & Alerts](/arduino-cloud/automations/triggers-and-alerts).
- **Update Policy** — Whether a variable publishes **On change** or **Periodically**. See [Cloud Variables](/arduino-cloud/things-data/cloud-variables).

## Next Steps

- [Troubleshooting & FAQ](/arduino-cloud/reference/troubleshooting-faq)
- [Cloud Variable Types](/arduino-cloud/reference/cloud-variable-types)
