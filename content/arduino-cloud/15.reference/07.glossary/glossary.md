---
title: Glossary
description: Alphabetical definitions of the key Arduino Cloud terms — Device, Thing, Cloud Variable, Dashboard, Trigger, OTA, and more.
tags: [Arduino Cloud, Glossary, Reference]
author: Karl Söderby & Arduino Team
---

Short definitions of the core Arduino® Cloud concepts, each linking to its main documentation page.

## API Key

A Client ID and Client Secret pair used to authenticate with the Arduino Cloud REST API and arduino-cloud-cli. See [REST API & SDKs](/arduino-cloud/apis-cli/rest-api-sdks).

## arduino-cloud-cli

The command-line tool for managing Arduino Cloud devices, Things, dashboards, templates and OTA updates from a terminal. See [CLI: Install & Credentials](/arduino-cloud/apis-cli/cli-install-credentials) and [CLI Commands](/arduino-cloud/apis-cli/cli-commands).

## Cloud Agent

A small local application that lets the browser talk to a board plugged into your computer over USB, for provisioning and uploads. See [Cloud Agent](/arduino-cloud/devices/cloud-agent).

## Cloud Variable

A data point a Thing exchanges between a device and Arduino Cloud, kept in sync on both sides. See [Cloud Variables](/arduino-cloud/things-data/cloud-variables).

## Connection Handler

The object (e.g. `WiFiConnectionHandler`) in `thingProperties.h` that manages a device's network connection to the Cloud. See [Generated Sketch Files](/arduino-cloud/reference/generated-sketch-files).

## Dashboard

A page of widgets bound to Cloud Variables, used to visualize and control a project. See [Dashboards](/arduino-cloud/dashboards/dashboards).

## Device

The physical (or virtual) hardware registered in Arduino Cloud that runs your code and exchanges data. See [Devices Overview](/arduino-cloud/devices/devices-overview).

## Device ID

A device's unique, non-secret identifier, safe to reference in code. See [Device Identity & Secrets](/arduino-cloud/security-privacy/device-identity-secrets).

## Device Lock

A device page setting that keeps a physical board tied to your account, or unlocks it so someone else can set it up after you delete it. See [Lock a Device to Your Account](/arduino-cloud/devices/device-lock).

## Device Status

Whether a device is currently connected to Arduino Cloud: Online, Offline or Unknown. See [Device Status & Lifecycle](/arduino-cloud/devices/device-status-lifecycle).

## FQBN (Fully Qualified Board Name)

The identifier the Arduino tools use to compile for a specific board, for example `arduino:samd:mkrwifi1010`. It is shown on the device page.

## Historical Data

The stored history of a Cloud Variable's values, shown in chart widgets and available for export as CSV. See [Historical Data & Export](/arduino-cloud/things-data/historical-data-export).

## IoT Remote App

The Arduino mobile app for Android and iOS, used to view and control dashboards, add boards over Bluetooth®, use the phone as a device and receive push notifications. See [IoT Remote App Overview](/arduino-cloud/iot-remote-app/iot-remote-app-overview).

## Manual Device

A generic device with no generated sketch, used to connect Python, MicroPython or JavaScript clients with a Device ID and Secret Key. See [Add a Manual Device](/arduino-cloud/devices/add-manual-device).

## OTA (Over-the-Air)

Uploading a new sketch to a device wirelessly, after its first USB upload. See [Upload Over the Air](/arduino-cloud/sketches-editor/upload-over-the-air).

## Permission

Whether a Cloud Variable can be changed from Arduino Cloud (**Read & Write**) or only from the board (**Read Only**). See [Cloud Variables](/arduino-cloud/things-data/cloud-variables).

## Provisioning

The one-time process of registering a device with the Cloud and configuring its secure credentials. See [Add a Wi-Fi® Board](/arduino-cloud/devices/add-wifi-board).

## Secret Key

A private credential, shown only once at device creation, used (with the login) to authenticate boards without a secure element. See [Device Identity & Secrets](/arduino-cloud/security-privacy/device-identity-secrets).

## Secure Element

A crypto chip on many Arduino boards that stores the board's certificate and private key, so no secret key is exposed in the sketch. See [Device Identity & Secrets](/arduino-cloud/security-privacy/device-identity-secrets).

## Sketch

The Arduino/C++ program that runs on a device and connects it to the Cloud. See [Generated Sketch Files](/arduino-cloud/reference/generated-sketch-files).

## Smart Folder

A saved set of search and filter rules that groups Things, devices or dashboards and keeps itself up to date automatically. See [Organize Resources With Smart Folders](/arduino-cloud/things-data/smart-folders).

## Space

A workspace that groups Things, devices, dashboards, and members; can be private or shared. See [Spaces](/arduino-cloud/spaces-plans-account/spaces).

## Sync Variables

Linking Cloud Variables of the same type on different Things, so that a change on one updates the others. See [Sync Variables Between Things](/arduino-cloud/things-data/sync-variables).

## Tag

A key/value label added to a Thing or device, used to organize, filter and select resources. See [Manage Devices at Scale](/arduino-cloud/devices/manage-devices-at-scale).

## Template

A pre-built bundle of Things, variables, dashboards and Triggers that sets up a complete project in one step. See [Use Templates](/arduino-cloud/templates/use-templates).

## Thing

The container for a project — its device association, Cloud Variables, and data history. See [Things](/arduino-cloud/things-data/things).

## Trigger

An automation that sends an email or push notification when a condition on a Boolean or String variable is met. See [Triggers & Alerts](/arduino-cloud/automations/triggers-and-alerts).

## Update Policy

Whether a variable publishes **On change** or **Periodically**. See [Cloud Variables](/arduino-cloud/things-data/cloud-variables).

## Webhook

A URL that Arduino Cloud calls with a JSON payload whenever a Thing's variables change, used to send data to external services. See [Webhooks](/arduino-cloud/automations/webhooks).

## Widget

A dashboard element that displays or controls a Cloud Variable, such as a switch, gauge, chart or map. See [Working With Dashboards](/arduino-cloud/dashboards/dashboards) and the [Widget Catalog](/arduino-cloud/reference/widget-catalog).

## Related Articles

- [Troubleshooting & FAQ](/arduino-cloud/reference/troubleshooting-faq)
- [Cloud Variable Types](/arduino-cloud/reference/cloud-variable-types)
