---
title: Network Configuration for Arduino App Lab
description: Learn about the ports, domains, and network types required for the Arduino UNO Q and App Lab.
overwriteSidebar: Network Configuration
tags: [app-lab, network, uno-q, troubleshooting, firewall]
---

Arduino App Lab relies on your local network for discovery, application deployment, and communication with your board. Use this guide to ensure your network environment is correctly configured.

## Local Network Discovery (mDNS)

Arduino App Lab uses **mDNS (Multicast DNS)** to automatically detect your UNO Q board on the local network.

<Alert type="warning">**Warning:** Some network environments—such as guest Wi-Fi, corporate networks, or VPNs—may block mDNS traffic, preventing the board from appearing in the App Lab interface.</Alert>

To ensure discovery works correctly:

* **Allow UDP Port 5353:** Your firewall must allow traffic on this port, which is the standard for mDNS.
* **Approve mdns-discovery:** On Windows, you must allow `mdns-discovery.exe` through the Windows Defender Firewall when prompted during the first launch of App Lab.

## Required Ports

Depending on the features and Bricks you use, the UNO Q requires access to the following ports:

| Port | Protocol | Service | Usage |
| :--- | :--- | :--- | :--- |
| 5353 | UDP | mDNS | Automatic board discovery on the local network. |
| 22 | TCP | SSH | Used for "Network Mode" to deploy and manage Apps. |
| 7000 | TCP | WebUI | The default port for the **WebUI Brick** dashboard. |
| 80 / 443 | TCP | HTTP/HTTPS | Fetching system updates, Docker images, and API data. |
| 123 | UDP | NTP | Synchronizing the internal Linux system clock. |

## Supported Network Types

* **WPA/WPA2 Personal:** Natively supported via the App Lab Wi-Fi setup wizard.
* **WPA2-Enterprise:** Supported by the underlying Debian OS but requires manual configuration via the terminal using `nmcli`.
* **Captive Portals:** Networks requiring a web-based login or "Agree" page are **not supported** by the App Lab setup wizard.

## Domain Whitelist

If you are operating behind a restrictive firewall, you must allow traffic to the following domains for the UNO Q to function correctly:

### Core Infrastructure

* `downloads.arduino.cc`: System updates, toolchains, and library indexes.
* `apt-repo.arduino.cc`: Official Arduino Debian package repository.
* `public.ecr.aws`: Docker container images for App Lab Bricks.
* `github.com` and `raw.githubusercontent.com`: Source code and package retrieval.

### Arduino Cloud

* `app.arduino.cc`
* `login.arduino.cc`

### Application Specific

* `api.open-meteo.com`: Used by the Weather Forecast example.
* `time.nist.gov`: Used for NTP time synchronization.
