---
title: Network Configuration for Arduino App Lab
description: Learn about the ports, domains, and network types required for your board and App Lab.
overwriteSidebar: Network Configuration
tags: [app-lab, network, uno-q, troubleshooting, firewall]
---

Configure your network environment to ensure reliable remote connectivity. While standard home networks typically work without additional setup, this guide provides the port, domain, and mDNS requirements for advanced users and IT administrators operating on restricted or corporate networks.

## Local Network Discovery (mDNS)

Arduino App Lab uses **mDNS (Multicast DNS)** to automatically detect your board on the local network.

<Alert type="warning">

**Warning:** Some network environments—such as guest Wi-Fi, corporate networks, or VPNs—may block mDNS traffic, preventing the board from appearing in the App Lab interface.

</Alert>

To ensure discovery works correctly:

- **Allow UDP Port 5353:** Your firewall must allow traffic on this port, which is the standard for mDNS.
- **Approve mdns-discovery:** On Windows, you must allow `mdns-discovery.exe` through the Windows Defender Firewall when prompted during the first launch of App Lab.

## Required Ports

Depending on the features and Bricks you use, your board requires access to the following ports:

| Port | Protocol | Service | Usage |
| :--- | :--- | :--- | :--- |
| 5353 | UDP | mDNS | Automatic board discovery on the local network. |
| 22 | TCP | SSH | Used for "Network Mode" to deploy and manage Apps. |
| 80 / 443 | TCP | HTTP/HTTPS | Fetching system updates, Docker images, and API data. |
| 123 | UDP | NTP | Synchronizing the internal Linux system clock. |
| 7000 | TCP | WebUI | The default port for the WebUI Brick. Can be overridden when initializing the Brick. |
| 4912 | TCP | Video stream | Live camera preview of the video AI Bricks, and smartphone camera streams from the [IoT Remote app](../../integrations/companion-app/). |

App Lab reaches the Arduino App CLI daemon on the board through its USB (ADB) or SSH connection, so you don't need to open the daemon port on your network. To see which ports a specific App exposes, run `arduino-app-cli app ports <app>` on the board.

## Supported Network Types

- **WPA/WPA2 Personal:** Natively supported via the App Lab Wi-Fi setup wizard.
- **WPA2-Enterprise:** Supported by the underlying Debian OS but requires manual configuration via the terminal using `nmcli`.
- **Captive Portals:** Networks requiring a web-based login or "Agree" page are **not supported** by the App Lab setup wizard.

## Domain Whitelist

If you are operating behind a restrictive firewall, you must allow traffic to the following domains. Domains used by the board and domains used by the computer running App Lab are listed separately.

### Board: Core Infrastructure

- `downloads.arduino.cc`: System updates, toolchains, and library indexes.
- `apt-repo.arduino.cc`: Official Arduino Debian package repository.
- `ghcr.io` and `pkg-containers.githubusercontent.com`: Container images for App Lab Bricks.
- `public.ecr.aws`: Container images used by older system versions.
- `github.com` and `raw.githubusercontent.com`: Source code and package retrieval.
- `pypi.org` and `files.pythonhosted.org`: Python packages listed in an App's `requirements.txt`.

### Board: AI Models

- `huggingface.co` and its download CDNs (`*.huggingface.co`, `*.hf.co`): Language models, including models added from Hugging Face.
- `studio.edgeimpulse.com`: Edge Impulse models and custom models trained in Edge Impulse Studio.
- `*.aihub.qualcomm.com`: Models from Qualcomm AI Hub. Model files may be served from additional Qualcomm download servers, so allow outbound HTTPS if downloads fail.

### Arduino Cloud and Project Hub

- `app.arduino.cc`
- `login.arduino.cc`
- `projecthub.arduino.cc`: Publishing Apps on Project Hub from App Lab.

### Computer: Agent Mode

These domains are used by the computer running App Lab when you use [Agent Mode](../../integrations/agent-mode/):

- `nodejs.org` and `registry.npmjs.org`: Download of the agent runtime when you install an agent.
- `claude.ai`, `platform.claude.com`, and `api.anthropic.com`: Sign-in and requests to Claude.

### Application Specific

- `api.open-meteo.com`: Used by the Weather Forecast Brick and example.
- `time.nist.gov`: Used for NTP time synchronization.

Bricks that use cloud services, such as **Cloud LLM**, **Cloud ASR**, **Telegram Bot**, **Air Quality Monitoring**, or **TPS**, also need access to the domains of their service providers.
