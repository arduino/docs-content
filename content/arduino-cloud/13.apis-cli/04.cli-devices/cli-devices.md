---
title: 'CLI: Devices'
description: Provision physical, LoRaWAN, and generic devices, then list, tag, and delete them from the terminal with arduino-cloud-cli.
tags: [Arduino Cloud, CLI, Devices]
author: Karl Söderby, Paolo Calao
---

See [Install & Credentials](/arduino-cloud/apis-cli/cli-install-credentials)
first for setup. All commands below are under `arduino-cloud-cli device`.

## Provision a Physical Board

Specify the port/FQBN, or let the CLI auto-detect the first board it finds:

```bash
arduino-cloud-cli device create --name <deviceName> --port <port> --fqbn <deviceFqbn>
```

Supported FQBNs (re-check against
[ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud)'s
supported-board table before assuming this hasn't changed):

```
arduino:samd:nano_33_iot
arduino:samd:mkrwifi1010
arduino:mbed_nano:nanorp2040connect
arduino:mbed_portenta:envie_m7
arduino:mbed_nicla:nicla_vision
arduino:samd:mkr1000
arduino:samd:mkrgsm1400
arduino:samd:mkrnb1500
arduino:mbed_opta:opta
arduino:mbed_giga:giga
arduino:esp32:nano_nora
arduino:renesas_uno:unor4wifi
```

If a board supports more than one connectivity type (e.g. Wi-Fi® + Ethernet),
set which one to use:

```bash
arduino-cloud-cli device create --name <deviceName> --port <port> --fqbn <deviceFqbn> --connection <deviceConnectivity>
```

`<deviceConnectivity>` is one of: `wifi`, `eth`, `wifiandsecret`, `gsm`, `nb`,
`lora`.

## LoRaWAN® Devices

Same idea, plus a mandatory frequency plan:

```bash
arduino-cloud-cli device create-lora --name <deviceName> --frequency-plan <freqID> --port <port> --fqbn <deviceFqbn>
```

Supported LoRaWAN® FQBNs: `arduino:samd:mkrwan1310`, `arduino:samd:mkrwan1300`.
List available frequency plans:

```bash
arduino-cloud-cli device list-frequency-plans
```

## Generic (Virtual) Devices

A generic device isn't tied to a physical board — any client that can
authenticate with its credentials (Python/MicroPython/Node.js) can connect as
it. Handy for testing or non-Arduino hardware:

```bash
arduino-cloud-cli device create-generic --name <deviceName> --fqbn <fqbn>
```

`--fqbn` is optional and defaults to `generic:generic:generic`. List supported
FQBNs with `arduino-cloud-cli device list-fqbn`. See
[Add a Manual Device](/arduino-cloud/devices/add-manual-device) for the
connection side.

## List, Show, Delete

```bash
# All devices
arduino-cloud-cli device list

# Only devices matching all given tags
arduino-cloud-cli device list --tags <key0>=<value0>,<key1>=<value1>

# Delete by ID
arduino-cloud-cli device delete --id <deviceID>

# Delete every device matching all given tags (bulk cleanup)
arduino-cloud-cli device delete --tags <key0>=<value0>,<key1>=<value1>
```

`--id` and `--tags` are mutually exclusive on `delete` — pick one.

## Tags

```bash
# Add tags
arduino-cloud-cli device create-tags --id <deviceID> --tags <key0>=<value0>,<key1>=<value1>

# Remove specific tag keys
arduino-cloud-cli device delete-tags --id <deviceID> --keys <key0>,<key1>
```

Tagging every device created for a specific purpose (e.g. `purpose=docs-demo`)
makes later bulk cleanup with `device delete --tags` trivial.

## Next Steps

- [CLI: Things](/arduino-cloud/apis-cli/cli-things)
- [CLI: OTA & Mass Upload](/arduino-cloud/apis-cli/cli-ota-mass-upload)

## Trademark Acknowledgments

- **LoRa®** and **LoRaWAN®** are registered trademarks of Semtech Corporation.
