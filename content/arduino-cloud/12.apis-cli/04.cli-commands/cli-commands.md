---
title: CLI Commands
description: Manage Arduino Cloud Devices, Things, Dashboards, custom Templates, and OTA updates from the terminal with arduino-cloud-cli.
tags: [Arduino Cloud, CLI]
author: Karl Söderby, Paolo Calao
---

`arduino-cloud-cli` lets you manage your Arduino® Cloud resources from the terminal, which makes it easy to script repeatable operations such as provisioning a fleet of devices or rolling out a firmware update. This page lists the available commands, grouped by resource.

See [CLI: Install & Credentials](/arduino-cloud/apis-cli/cli-install-credentials) first to install the CLI and set up your API credentials. Every command supports `--help` for its exact, current flags.

- [Devices](#devices)
- [Things](#things)
- [Dashboards](#dashboards)
- [Templates](#templates)
- [OTA & Mass Upload](#ota--mass-upload)

## Devices

All commands in this section are under `arduino-cloud-cli device`.

### Provision a Physical Board

Specify the port/FQBN, or let the CLI auto-detect the first board it finds:

```bash
arduino-cloud-cli device create --name <deviceName> --port <port> --fqbn <deviceFqbn>
```

Supported FQBNs:

```bash
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

If a board supports more than one connectivity type (e.g. Wi-Fi® + Ethernet), set which one to use:

```bash
arduino-cloud-cli device create --name <deviceName> --port <port> --fqbn <deviceFqbn> --connection <deviceConnectivity>
```

`<deviceConnectivity>` is one of: `wifi`, `eth`, `wifiandsecret`, `gsm`, `nb`, `lora`.

### LoRaWAN® Devices

Same idea, plus a mandatory frequency plan:

```bash
arduino-cloud-cli device create-lora --name <deviceName> --frequency-plan <freqID> --port <port> --fqbn <deviceFqbn>
```

Supported LoRaWAN FQBNs: `arduino:samd:mkrwan1310`, `arduino:samd:mkrwan1300`. List available frequency plans:

```bash
arduino-cloud-cli device list-frequency-plans
```

### Generic (Virtual) Devices

A generic device isn't tied to a physical board — any client that can authenticate with its credentials (Python®/MicroPython/Node.js) can connect as it. Handy for testing or non-Arduino hardware:

```bash
arduino-cloud-cli device create-generic --name <deviceName> --fqbn <fqbn>
```

`--fqbn` is optional and defaults to `generic:generic:generic`. List supported FQBNs with `arduino-cloud-cli device list-fqbn`. See [Add a Manual Device](/arduino-cloud/devices/add-manual-device) for the connection side.

### List, Show, Delete

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

### Device Tags

```bash
# Add tags
arduino-cloud-cli device create-tags --id <deviceID> --tags <key0>=<value0>,<key1>=<value1>

# Remove specific tag keys
arduino-cloud-cli device delete-tags --id <deviceID> --keys <key0>,<key1>
```

Tagging every device created for a specific purpose (e.g. `purpose=docs-demo`) makes later bulk cleanup with `device delete --tags` trivial.

## Things

All commands in this section are under `arduino-cloud-cli thing`.

### Create a Thing From a Thing Template

Things are created from a **thing template** file (JSON or YAML) describing their variables. `--name` is optional and overrides the name in the template:

```bash
arduino-cloud-cli thing create --name <thingName> --template <template.(json|yaml)>
```

### Clone an Existing Thing

`--name` is mandatory here:

```bash
arduino-cloud-cli thing clone --name <thingName> --clone-id <thingToCloneID>
```

### List Things

```bash
# All things, with their variables
arduino-cloud-cli thing list --show-variables

# Only specific things by ID
arduino-cloud-cli thing list --ids <thingOneID>,<thingTwoID>

# The thing associated with a specific device
arduino-cloud-cli thing list --device-id <deviceID>

# Only things matching all given tags
arduino-cloud-cli thing list --tags <key0>=<value0>,<key1>=<value1>
```

### Delete Things

```bash
# By ID
arduino-cloud-cli thing delete --id <thingID>

# All things matching all given tags
arduino-cloud-cli thing delete --tags <key0>=<value0>,<key1>=<value1>
```

`--id` and `--tags` are mutually exclusive.

### Extract a Thing as a Template

Turn an existing Thing back into a reusable template, printed to stdout:

```bash
arduino-cloud-cli thing extract --id <thingID> --format <json|yaml>
```

### Bind a Thing to a Device

```bash
arduino-cloud-cli thing bind --id <thingID> --device-id <deviceID>
```

Equivalent to associating a device from the Thing's Device panel in the web UI.

### Thing Tags

```bash
arduino-cloud-cli thing create-tags --id <thingID> --tags <key0>=<value0>,<key1>=<value1>
arduino-cloud-cli thing delete-tags --id <thingID> --keys <key0>,<key1>
```

## Dashboards

All commands in this section are under `arduino-cloud-cli dashboard`.

### List Dashboards

```bash
arduino-cloud-cli dashboard list --show-widgets
```

### Delete a Dashboard

```bash
arduino-cloud-cli dashboard delete --id <dashboardID>
```

### Extract a Dashboard as a Template

Print an existing dashboard's definition to stdout:

```bash
arduino-cloud-cli dashboard extract --id <dashboardID> --format <json|yaml>
```

### Create a Dashboard From a Template

In the CLI, dashboards can only be created from a template (JSON or YAML) — there's no "create empty dashboard" command, unlike the web UI. `--name` overrides the template's name if given. Use `--override` to substitute the template's `thing_id` placeholder(s) with real Thing IDs:

```bash
arduino-cloud-cli dashboard create \
  --name <dashboardName> \
  --template <template.(json|yaml)> \
  --override <thing-0>=<actualThingID>,<thing-1>=<otherActualThingID>
```

A practical workflow: build a dashboard once in the web UI against a "template" Thing, `dashboard extract` it, then `dashboard create --override` it against each real Thing you want the same layout applied to.

## Templates

All commands in this section are under `arduino-cloud-cli template` and work with [custom templates](/arduino-cloud/templates/custom-templates): reusable bundles of Things, Dashboards, and Triggers that are shared as `.tino` archives.

<Alert type="note">

Triggers are not supported by the CLI yet. If you want a custom template to include Triggers, create it in the web UI (see [Custom Templates](/arduino-cloud/templates/custom-templates)). You can then list, export, import, and apply it with the commands below.

</Alert>

### List Custom Templates

List the custom templates in your account, including their IDs:

```bash
arduino-cloud-cli template list
```

### Export a Custom Template

Export a custom template as a `.tino` archive, using the template ID returned by `template list`:

```bash
arduino-cloud-cli template export -t <templateID>
```

The archive is saved in the current directory. Use `-d` (`--directory`) to choose a different output directory:

```bash
arduino-cloud-cli template export -t <templateID> -d <outputDirectory>
```

### Import a Custom Template

Import a `.tino` archive, for example one that someone shared with you, into your account:

```bash
arduino-cloud-cli template import -f <template.tino>
```

### Apply a Custom Template to a Device

Applying a template to a device generates the resources defined in the template (such as the Thing and Dashboard) and links them to the device:

```bash
arduino-cloud-cli template apply -d <deviceID> -t <templateID> -p "<namePrefix>" -n SECRET_SSID=<ssid>,SECRET_OPTIONAL_PASS=<pwd>
```

| Flag | Required | Description |
|---|---|---|
| `-d`, `--device-id` | Yes | ID of the target device. The device must not already be linked to a Thing. |
| `-t`, `--template-id` | Yes | ID of the custom template to apply. |
| `-p`, `--prefix` | Yes | Prefix added to the names of the generated resources. |
| `-n`, `--network-credentials` | No | Comma-separated `<key>=<value>` network credentials for the device. Supported keys: `SECRET_SSID`, `SECRET_OPTIONAL_PASS`, `SECRET_DEVICE_KEY`. |

See [Clone & Bulk-Create](/arduino-cloud/templates/clone-bulk-create) for an example that applies one template to many devices in a loop.

## OTA & Mass Upload

All commands in this section are under `arduino-cloud-cli ota`.

<Alert type="warning">

Only boards listed as OTA-capable support this — check the [Supported Boards & Capabilities](/arduino-cloud/reference/supported-boards-capabilities) reference before scheduling an update.

</Alert>

### Compiling the Binary

`--file` expects a compiled `.ino.bin`, not the raw `.ino` sketch — `arduino-cloud-cli` doesn't compile sketches itself. Two ways to produce it:

```bash
arduino-cli compile -b <deviceFQBN> /path/to/MySketch
```

Or, from the Arduino IDE with the sketch open: **Sketch > Export Compiled Binary**, then **Sketch > Show Sketch Folder** to find the generated `.bin` inside the sketch's `build/` subfolder.

<Alert type="info">

Run `arduino-cli board listall` if you don't already know the target device's FQBN.

</Alert>

### Upload to a Single Device

```bash
arduino-cloud-cli ota upload --device-id <deviceID> --file <sketch-file.ino.bin>
```

This schedules the OTA and prints its ID. Check status by OTA ID or by device:

```bash
arduino-cloud-cli ota status --ota-id <otaID>
arduino-cloud-cli ota status --device-id <deviceID>
```

### Deferred Upload

An OTA upload must normally complete within 10 minutes. Add `--deferred` to extend that window up to one week, letting offline devices pick up the update when they reconnect:

```bash
arduino-cloud-cli ota upload --device-id <deviceID> --file <sketch-file.ino.bin> --deferred
```

### Mass Upload

Push the same binary to many devices at once. `--fqbn` is mandatory (all target devices must match it), and you select targets either by explicit IDs or by tags:

```bash
# By device IDs
arduino-cloud-cli ota mass-upload --fqbn <deviceFQBN> --device-ids <deviceIDs> --file <sketch-file.ino.bin>

# By tags
arduino-cloud-cli ota mass-upload --fqbn <deviceFQBN> --device-tags <key0>=<value0>,<key1>=<value1> --file <sketch-file.ino.bin>
```

Tagging devices (see [Device Tags](#device-tags)) makes it easy to target a fleet subset for a rollout.

### Cancel, Encode, Decode

`ota cancel`, `ota encode`, and `ota decode` round out the group: `cancel` stops a scheduled OTA upload, `encode` adds the OTA header to a binary file, and `decode` reads the header of an OTA file. Run `arduino-cloud-cli ota <command> --help` to list the flags of each command.

## Related Articles

- [CLI: Install & Credentials](/arduino-cloud/apis-cli/cli-install-credentials)
- [Custom Templates](/arduino-cloud/templates/custom-templates)
- [Clone & Bulk-Create](/arduino-cloud/templates/clone-bulk-create)
- [REST API & SDKs](/arduino-cloud/apis-cli/rest-api-sdks)
