---
title: Add & Link Widgets
description: Add widgets to an Arduino Cloud Dashboard and link them to Cloud Variables to read and control your project.
tags: [Arduino Cloud, Dashboards, Widgets]
author: TODO
---

Widgets are the building blocks of a [Dashboard](/arduino-cloud/dashboards/dashboards):
each one either displays a [Cloud Variable](/arduino-cloud/things-data/cloud-variables)
or writes back to it. This page covers adding widgets and binding them to
variables; for the full list of every widget type, see the
[Widget Catalog](/arduino-cloud/reference/widget-catalog).

## Adding a Widget

Open a dashboard, select **Edit** to enter edit mode, then **ADD** to open
the widget picker. It's organized into three categories — **Interaction**,
**Visualisation**, and **Annotation**:

![The widget picker.](assets/widget-picker.png)

Pick a widget and it drops onto the canvas. Every widget can be added
**without linking a variable first** — it renders with example/placeholder
data immediately, so you can preview its look and arrange your layout before
committing to a variable.

## Linking a Widget to a Variable

To make a widget show real data, link it to a Cloud Variable:

1. In edit mode, select the widget to open its floating toolbar.
2. Open its **settings** (gear icon).
3. Choose the Cloud Variable to bind — the widget picker lists the variables
   across your Things that are compatible with that widget type.
4. Confirm. The widget immediately swaps its example data for the live value.

<Alert type="info">

A widget only lists variables whose type it supports. A **Switch** needs a
Boolean, a **Map** needs a `Location`, a **Chart** needs a numeric type, and
so on. If a variable doesn't appear, check its type on the
[Thing](/arduino-cloud/things-data/things).

</Alert>

## Interaction vs. Visualisation

Whether a widget can *control* a device depends on both the widget and the
variable's permission:

- **Interaction** widgets (Switch, Slider, Push Button, Color, …) write a new
  value back to the device — they need a variable with **Read & Write**
  permission.
- **Visualisation** widgets (Value, Gauge, Chart, Map, …) only display
  incoming values and work with any permission.

A read-only variable linked to an interaction widget renders as display-only.
See [Cloud Variables](/arduino-cloud/things-data/cloud-variables) for setting
a variable's permission.

## Editing and Removing a Widget

In edit mode, select any widget to open its floating toolbar — settings,
duplicate, delete, and close. The settings (gear) icon is also where you
change or re-link its variable later.

## Next Steps

- [Widget Catalog](/arduino-cloud/reference/widget-catalog)
- [Multiple-Variable Chart](/arduino-cloud/dashboards/multiple-variable-chart)
- [Track Location on a Map](/arduino-cloud/dashboards/track-location-map)
