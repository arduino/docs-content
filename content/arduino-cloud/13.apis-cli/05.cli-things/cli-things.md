---
title: 'CLI: Things'
description: Create, clone, bind, list, tag, extract, and delete Arduino Cloud Things from the terminal with arduino-cloud-cli.
tags: [Arduino Cloud, CLI, Things]
author: TODO
---

See [Install & Credentials](/arduino-cloud/apis-cli/cli-install-credentials)
first for setup. All commands below are under `arduino-cloud-cli thing`.

## Create From a Template

Things are created from a **thing template** file (JSON or YAML) describing their
variables. `--name` is optional and overrides the name in the template:

```bash
arduino-cloud-cli thing create --name <thingName> --template <template.(json|yaml)>
```

## Clone an Existing Thing

`--name` is mandatory here:

```bash
arduino-cloud-cli thing clone --name <thingName> --clone-id <thingToCloneID>
```

## List

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

## Delete

```bash
# By ID
arduino-cloud-cli thing delete --id <thingID>

# All things matching all given tags
arduino-cloud-cli thing delete --tags <key0>=<value0>,<key1>=<value1>
```

`--id` and `--tags` are mutually exclusive.

## Extract as a Template

Turn an existing Thing back into a reusable template, printed to stdout:

```bash
arduino-cloud-cli thing extract --id <thingID> --format <json|yaml>
```

## Bind to a Device

```bash
arduino-cloud-cli thing bind --id <thingID> --device-id <deviceID>
```

Equivalent to associating a device from the Thing's Device panel in the web UI.

## Tags

```bash
arduino-cloud-cli thing create-tags --id <thingID> --tags <key0>=<value0>,<key1>=<value1>
arduino-cloud-cli thing delete-tags --id <thingID> --keys <key0>,<key1>
```

## Next Steps

- [CLI: Dashboards](/arduino-cloud/apis-cli/cli-dashboards)
- [CLI: Devices](/arduino-cloud/apis-cli/cli-devices)
