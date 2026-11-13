---
title: 'CLI: Install & Credentials'
description: Install arduino-cloud-cli and authenticate it with an API key, so you can manage Arduino Cloud entirely from a terminal.
tags: [Arduino Cloud, CLI]
author: Karl Söderby, Paolo Calao
---

**arduino-cloud-cli** is a command-line tool for managing Arduino Cloud resources — devices, Things, dashboards, templates, OTA updates — without opening a browser. It's ideal for scripting, CI/CD, and bulk operations. Source: [github.com/arduino/arduino-cloud-cli](https://github.com/arduino/arduino-cloud-cli) (license: AGPL v3).

## Install

Download a prebuilt binary from the [latest release](https://github.com/arduino/arduino-cloud-cli/releases/latest) for your OS/architecture, or build from source with Go:

```bash
git clone https://github.com/arduino/arduino-cloud-cli
cd arduino-cloud-cli
go build -o arduino-cloud-cli .
```

If you plan to provision physical boards with `device create`, also install [`arduino-cli`](https://arduino.github.io/arduino-cli/latest/installation) — it's used under the hood to compile and upload the provisioning sketch.

## Authenticate

Create an API key from **API Keys** in the account menu at [app.arduino.cc](https://app.arduino.cc) (Client ID + Secret), then store it:

```bash
arduino-cloud-cli credentials init
```

This prompts for the Client ID/Secret and writes them to a credentials file in the Arduino data directory by default. Useful variations:

```bash
# Write to a specific directory instead (e.g. a project folder)
arduino-cloud-cli credentials init --dest-dir <destinationFolder>

# Use JSON instead of the default YAML
arduino-cloud-cli credentials init --file-format json

# Overwrite an existing credentials file
arduino-cloud-cli credentials init --overwrite

# See which credentials file would be used from the current directory
arduino-cloud-cli credentials find
```

Credentials can optionally include an **organization ID** to scope every command to a specific organization.

### Lookup Order

Credentials are resolved from the current working directory → parent directories → the Arduino15 default directory. This lets you keep different credentials per project just by running the CLI from that project's folder.

An **environment variable override** takes priority over any credentials file: `ARDUINO_CLOUD_CLIENT`, `ARDUINO_CLOUD_SECRET`, and optionally `ARDUINO_CLOUD_ORGANIZATION`. Both `CLIENT` and `SECRET` must be set for the override to take effect.

## Output Conventions

The CLI is **quiet on success, verbose on error** — commands that succeed print only their actual result (so you can pipe/redirect it), while failures print an error message:

```bash
# Machine-readable output only, safe to redirect to a file
arduino-cloud-cli device create --name mydevice --format json > mydevice.json
```

Add `-v` to force logs to print even on success, useful while debugging. Most `list`/`show`/`extract` commands accept `--format json` or `--format yaml`.

## Command Groups

| Group | Covers |
|---|---|
| `credentials` | `init`, `find` |
| [`device`](/arduino-cloud/apis-cli/cli-devices) | Provision, list, tag, delete devices |
| [`thing`](/arduino-cloud/apis-cli/cli-things) | Create, clone, bind, list, tag Things |
| [`dashboard`](/arduino-cloud/apis-cli/cli-dashboards) | Create, list, extract, delete Dashboards |
| [`ota`](/arduino-cloud/apis-cli/cli-ota-mass-upload) | Firmware over-the-air updates, single or mass |
| `template` | Manage custom Thing + Dashboard templates |
| `version` | Print the CLI's own version |

Every command supports `--help` for its exact, current flags.

## Next Steps

- [CLI: Devices](/arduino-cloud/apis-cli/cli-devices)
- [CLI: Things](/arduino-cloud/apis-cli/cli-things)
- [REST API & SDKs](/arduino-cloud/apis-cli/rest-api-sdks)
