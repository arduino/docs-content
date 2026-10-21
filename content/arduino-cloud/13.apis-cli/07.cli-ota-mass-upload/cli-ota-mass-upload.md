---
title: 'CLI: OTA & Mass Upload'
description: Push firmware over-the-air to one or many Arduino Cloud devices from the terminal, by device ID or by tags.
tags: [Arduino Cloud, CLI, OTA]
author: Karl Söderby, Paolo Calao
---

See [Install & Credentials](/arduino-cloud/apis-cli/cli-install-credentials)
first for setup. All commands below are under `arduino-cloud-cli ota`.

<Alert type="warning">

Only boards listed as OTA-capable support this — cross-check
[ArduinoIoTCloud](https://github.com/arduino-libraries/ArduinoIoTCloud)'s board
table and [Devices](/arduino-cloud/devices/devices-overview).

</Alert>

## Compiling the Binary

`--file` expects a compiled `.ino.bin`, not the raw `.ino` sketch —
`arduino-cloud-cli` doesn't compile sketches itself. Two ways to produce it:

```bash
arduino-cli compile -b <deviceFQBN> /path/to/MySketch
```

Or, from the Arduino IDE with the sketch open: **Sketch > Export Compiled
Binary**, then **Sketch > Show Sketch Folder** to find the generated `.bin`
inside the sketch's `build/` subfolder.

<Alert type="info">

Run `arduino-cli board listall` if you don't already know the target device's
FQBN.

</Alert>

## Upload to a Single Device

```bash
arduino-cloud-cli ota upload --device-id <deviceID> --file <sketch-file.ino.bin>
```

This schedules the OTA and prints its ID. Check status by OTA ID or by device:

```bash
arduino-cloud-cli ota status --ota-id <otaID>
arduino-cloud-cli ota status --device-id <deviceID>
```

### Deferred Upload

An OTA upload must normally complete within 10 minutes. Add `--deferred` to
extend that window up to one week, letting offline devices pick up the update
when they reconnect:

```bash
arduino-cloud-cli ota upload --device-id <deviceID> --file <sketch-file.ino.bin> --deferred
```

## Mass Upload

Push the same binary to many devices at once. `--fqbn` is mandatory (all target
devices must match it), and you select targets either by explicit IDs or by
tags:

```bash
# By device IDs
arduino-cloud-cli ota mass-upload --fqbn <deviceFQBN> --device-ids <deviceIDs> --file <sketch-file.ino.bin>

# By tags
arduino-cloud-cli ota mass-upload --fqbn <deviceFQBN> --device-tags <key0>=<value0>,<key1>=<value1> --file <sketch-file.ino.bin>
```

Tagging devices (see [CLI: Devices](/arduino-cloud/apis-cli/cli-devices#tags))
makes it easy to target a fleet subset for a rollout.

## Cancel, Encode, Decode

`ota cancel`, `ota encode`, and `ota decode` round out the group.

<Alert type="warning">

Needs verification: the exact flags for `ota cancel`/`encode`/`decode` weren't
walked through hands-on in this pass — run `arduino-cloud-cli ota <command>
--help` to confirm before quoting specific flag names.

</Alert>

## Next Steps

- [CLI: Devices](/arduino-cloud/apis-cli/cli-devices)
- [CLI: Install & Credentials](/arduino-cloud/apis-cli/cli-install-credentials)
