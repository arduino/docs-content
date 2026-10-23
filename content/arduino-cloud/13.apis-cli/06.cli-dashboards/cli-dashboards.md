---
title: 'CLI: Dashboards'
description: List, extract, create from a template, and delete Arduino Cloud Dashboards from the terminal with arduino-cloud-cli.
tags: [Arduino Cloud, CLI, Dashboards]
author: Karl Söderby, Paolo Calao
---

See [Install & Credentials](/arduino-cloud/apis-cli/cli-install-credentials) first for setup. All commands below are under `arduino-cloud-cli dashboard`.

## List

```bash
arduino-cloud-cli dashboard list --show-widgets
```

## Delete

```bash
arduino-cloud-cli dashboard delete --id <dashboardID>
```

## Extract as a Template

Print an existing dashboard's definition to stdout:

```bash
arduino-cloud-cli dashboard extract --id <dashboardID> --format <json|yaml>
```

## Create From a Template

Dashboards can only be created from a template (JSON or YAML) — there's no "create empty dashboard" command, unlike the web UI. `--name` overrides the template's name if given. Use `--override` to substitute the template's `thing_id` placeholder(s) with real Thing IDs:

```bash
arduino-cloud-cli dashboard create \
  --name <dashboardName> \
  --template <template.(json|yaml)> \
  --override <thing-0>=<actualThingID>,<thing-1>=<otherActualThingID>
```

A practical workflow: build a dashboard once in the web UI against a "template" Thing, `dashboard extract` it, then `dashboard create --override` it against each real Thing you want the same layout applied to.

## Next Steps

- [CLI: Things](/arduino-cloud/apis-cli/cli-things)
- [CLI: OTA & Mass Upload](/arduino-cloud/apis-cli/cli-ota-mass-upload)
