---
title: Changelog
description: Features, enhancements and announcements launched in Arduino Cloud, grouped by month with the newest first.
tags: [Arduino Cloud, Changelog, What's New]
author: Karl Söderby & Arduino Team
---

This page lists the features launched in Arduino® Cloud, grouped by month, with the newest at the top. Each entry is tagged with its type:

| Tag | Meaning |
|---|---|
| **Feature** | A new, generally available feature. |
| **Preview** | A feature in Public Preview that is not yet generally available. |
| **Enhancements & improvements** | A change that upgrades, expands, or refines an existing feature. |
| **Announcement** | An API deprecation, a removal, or another important change. |

## October 2026

### New Roles and Revised Permissions

**Feature**

Shared spaces have two new roles, **Viewer** and **Service**, and the permissions of the existing roles have been revised. Viewers have read-only access with selected non-destructive interactions, such as using dashboard widgets and downloading historical data. Service members have operational access to selected device, dashboard, Trigger, Template and Sketch operations, without managing members, branding or payments. Editors can now invite Service and Viewer members and change roles between them.

[Learn more: Members, Roles & Permissions](/arduino-cloud/spaces-plans-account/members-roles)

## September 2026

### Custom Color Palette for White-Label Experiences

**Enhancements & improvements**

Spaces with a white-label plan can set a custom color palette, so the Arduino Cloud interface matches the organization's brand together with its logo, custom URL and sign-in options.

[Learn more: Custom Branding](/arduino-cloud/spaces-plans-account/custom-branding)

### IoT Remote App Migration to Android 17

**Enhancements & improvements**

The IoT Remote app for Android has been migrated to Android 17 and supports the new SDK.

[Learn more: IoT Remote App Overview](/arduino-cloud/iot-remote-app/iot-remote-app-overview)

## August 2026

### New Provisioning Flow for UNO Q and VENTUNO Q

**Feature**

UNO Q and VENTUNO Q boards are now connected to Arduino Cloud directly from Arduino App Lab. Select **Connect** in the Cloud section of the device settings, choose a space, and the board is provisioned automatically, with no Device ID or Secret Key to copy.

[Learn more: Add an UNO Q or VENTUNO Q](/arduino-cloud/devices/add-q-boards)

## June 2026

### Ingested IoT Data Counting and Plan Usage Metric

**Feature**

Arduino Cloud now counts the IoT data records ingested by each space and shows the metric on the plan usage page and in the space statistics. The metric is informational only and does not limit your usage.

[Learn more: Space Statistics](/arduino-cloud/spaces-plans-account/space-statistics)

## May 2026

### Spaces Overview

**Feature**

The new Spaces Overview shows aggregate statistics, plan usage and devices across every space you belong to, without switching between spaces.

[Learn more: Spaces Overview](/arduino-cloud/spaces-plans-account/spaces-overview)

### Lock or Unlock Devices to an Account After Provisioning

**Feature**

The **Lock to this account** setting on the device page keeps a board tied to your account, or unlocks it so someone else can set it up after you delete it. Each type of space has its own default: Business spaces lock devices by default, while private and Education spaces leave them unlocked.

[Learn more: Lock a Device to Your Account](/arduino-cloud/devices/device-lock)

## April 2026

### Smart Folders

**Feature**

Smart Folders group Things, devices and dashboards by rules, such as a tag or a device status, and keep each folder up to date automatically as resources are added or change.

[Learn more: Organize Resources With Smart Folders](/arduino-cloud/things-data/smart-folders)

### Dashboard Pages

**Feature**

A dashboard can now be split into multiple pages, each with its own widgets, name and icon, to organize large dashboards.

[Learn more: Dashboard Pages](/arduino-cloud/dashboards/dashboard-pages)

### IoT Remote App Migration to iOS 26

**Enhancements & improvements**

The IoT Remote app for iOS has been migrated to iOS 26.

[Learn more: IoT Remote App Overview](/arduino-cloud/iot-remote-app/iot-remote-app-overview)

## February 2026

### Things Page Redesign

**Enhancements & improvements**

The Things page has been redesigned, with a **Data** tab for Cloud Variables, a **Sketch** tab for the generated code, and side panels for the associated device and the Thing's metadata.

[Learn more: Things](/arduino-cloud/things-data/things)

### Dark Theme Across the Platform

**Enhancements & improvements**

The dark theme now extends to the Cloud Editor, dashboards, lists and resource pages.

[Learn more: Cloud Editor Overview](/arduino-cloud/sketches-editor/cloud-editor-overview)

### IoT Remote App Support for the UNO Q Companion

**Feature**

The IoT Remote app can act as a companion for UNO Q and VENTUNO Q boards running Arduino App Lab, streaming the phone's sensors and camera to the board over the local network.

[Learn more: Use Your Phone With Arduino App Lab](/arduino-cloud/iot-remote-app/arduino-app-lab)

## January 2026

### Provisioning Enhancements

**Enhancements & improvements**

The device provisioning workflows have been improved. More boards, including the GIGA R1 WiFi, can be set up over Bluetooth Low Energy, and Provisioning 1.0 boards can be prepared for Bluetooth® setup with the `arduino-cloud-cli device provisioning migrate` command.

[Learn more: Set Up a Device Over Bluetooth](/arduino-cloud/devices/bluetooth-device-setup)
