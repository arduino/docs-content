---
title: Clone and Bulk-Create
description: Clone Things and roll out templates to many devices and dashboards from the terminal with arduino-cloud-cli.
tags: [Arduino Cloud, Templates, CLI]
author: TODO
---

When you need the same setup on more than one device, the web UI's one-at-a-time
flow becomes slow. The [arduino-cloud-cli](/arduino-cloud/apis-cli/cli-things)
turns Things, Dashboards, and templates into scriptable building blocks you can
clone and replicate in a batch — ideal for provisioning a fleet or a classroom
set of identical projects.

<Alert type="info">

All commands below assume the CLI is installed and authenticated. See
[arduino-cloud-cli › Things](/arduino-cloud/apis-cli/cli-things) for setup.

</Alert>

## Cloning a Thing

Duplicate an existing Thing's variable layout into a new one. `--name` is
required:

```bash
arduino-cloud-cli thing clone --name <newThingName> --clone-id <thingToCloneID>
```

To templatize a Thing instead — turning it into a reusable file you can create
many Things from — extract it:

```bash
arduino-cloud-cli thing extract --id <thingID> --format yaml > thing-template.yaml
arduino-cloud-cli thing create --name <thingName> --template thing-template.yaml
```

## Replicating a Dashboard

Dashboards can only be created from a template, which makes them easy to
replicate. Build one dashboard against a "template" Thing, extract it, then
re-create it against each real Thing — `--override` swaps the template's
`thing_id` placeholder(s) for real Thing IDs:

```bash
arduino-cloud-cli dashboard extract --id <dashboardID> --format yaml > dash.yaml

arduino-cloud-cli dashboard create \
  --name <dashboardName> \
  --template dash.yaml \
  --override <thing-0>=<actualThingID>
```

## Bulk-Applying a Template to Many Devices

A custom template bundles the Thing(s) and Dashboard(s) together, so applying
it to a device provisions everything at once. Loop over device IDs and apply
the same template, using `-p` to prefix each batch's generated names so the
results stay distinguishable:

```bash
for dev in <deviceID1> <deviceID2> <deviceID3>; do
  arduino-cloud-cli template apply \
    -d "$dev" -t <templateID> -p "floor1-$dev" \
    -n SECRET_SSID=<ssid>,SECRET_OPTIONAL_PASS=<pwd>
done
```

Each device gets its own generated Thing and Dashboard from the one template —
the core pattern for fleet-style rollouts.

## Next Steps

- [arduino-cloud-cli › Things](/arduino-cloud/apis-cli/cli-things)
- [Custom Templates](/arduino-cloud/templates/custom-templates)
- [Use Templates](/arduino-cloud/templates/use-templates)
