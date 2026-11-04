---
title: Widget Catalog
description: Every Arduino Cloud dashboard widget, grouped by category, with a preview and a note on the three plan-gated widgets.
tags: [Arduino Cloud, Dashboards, Widgets, Reference]
author: Karl Söderby & Arduino Team
---

The full catalog of [Dashboard](/arduino-cloud/dashboards/dashboards) widgets, organized into the three picker categories — **Interaction**, **Visualisation**, and **Annotation**. Every widget can be added without linking a variable first; it renders with placeholder data until you bind it to a [Cloud Variable](/arduino-cloud/things-data/cloud-variables).

## Interaction

Widgets that let a dashboard write back to a device.

| Widget | Preview | What It Does | Variable Types |
|---|---|---|---|
| Switch | ![Switch](assets/widgets/01-switch.png) | Binary ON/OFF toggle. | `bool` |
| Push Button | ![Push Button](assets/widgets/02-push-button.png) | Momentary press — sends a value only while held. | `bool` |
| Slider | ![Slider](assets/widgets/03-slider.png) | Drag to set a numeric value within a min/max range. | `int`, `float` |
| Stepper | ![Stepper](assets/widgets/04-stepper.png) | Increment/decrement a numeric value by 1. | `int`, `float` |
| Messenger | ![Messenger](assets/widgets/05-messenger.png) | Two-way text messages between dashboard and device. | `String` |
| Color | ![Color](assets/widgets/06-color.png) | HSB/hex color picker. | `CloudColor` |
| Dimmed Light | ![Dimmed Light](assets/widgets/07-dimmed-light.png) | ON/OFF plus a brightness percentage. | `CloudDimmedLight` |
| Colored Light | ![Colored Light](assets/widgets/08-colored-light.png) | ON/OFF plus a full color picker. | `CloudColoredLight` |
| Time Picker | ![Time Picker](assets/widgets/09-time-picker.png) | Set a specific date/time value. | `CloudTime` |
| Scheduler | ![Scheduler](assets/widgets/10-scheduler.png) | Define a recurring schedule — see [Scheduler](/arduino-cloud/automations/scheduler). | `CloudSchedule` |

## Visualisation

Widgets for displaying data coming from a device.

| Widget | Preview | What It Does | Variable Types |
|---|---|---|---|
| Value | ![Value](assets/widgets/11-value.png) | Plain numeric/text readout. | Most types |
| Value Selector | ![Value Selector](assets/widgets/12-value-selector.png) | Current value as mutually-exclusive buttons. | `int`, `String` |
| Value Dropdown | ![Value Dropdown](assets/widgets/13-value-dropdown.png) | Same as Value Selector, as a dropdown. | `int`, `String` |
| Status | ![Status](assets/widgets/14-status.png) | A short text/state label. | `bool` |
| Gauge | ![Gauge](assets/widgets/15-gauge.png) | Circular gauge with configurable min/max. | `int`, `float` |
| Percentage | ![Percentage](assets/widgets/16-percentage.png) | A 0–100% readout with icon/color thresholds. | `int`, `float` |
| LED | ![LED](assets/widgets/17-led.png) | Simple on/off indicator light. | `bool` |
| Map | ![Map](assets/widgets/18-map.png) | Plots a `Location` variable on a live map. | `CloudLocation` |
| Chart | ![Chart](assets/widgets/19-chart.png) | Time-series line chart, one variable, with selectable range. | `int`, `float` |
| Advanced Map 🔒 | ![Advanced Map locked](assets/widgets/20-advanced-map-locked.png) | Location history/path for a device. **Plan-gated.** | `CloudLocation` |
| Advanced Chart 🔒 | ![Advanced Chart locked](assets/widgets/21-advanced-chart-locked.png) | Up to 5 variables on one chart. **Plan-gated.** | `int`, `float` |

## Annotation

Non-data widgets for organizing a dashboard.

| Widget | Preview | What It Does | Variable Types |
|---|---|---|---|
| Sticky Note | ![Sticky Note](assets/widgets/23-sticky-note.png) | A markdown-formatted note. | None (not linkable) |
| Image | ![Image](assets/widgets/24-image.png) | An uploaded or URL image (JPG/PNG/WEBP); URL images can auto-refresh. | None (not linkable) |
| Image Map 🔒 | ![Image Map locked](assets/widgets/22-image-map-locked.png) | Live variable markers, controls, and labels on a custom image (e.g. a floor plan). **Plan-gated.** See [Image Map Widget](/arduino-cloud/dashboards/image-map-widget). | `int`, `float`, `String`, `bool` |
| Link | ![Link](assets/widgets/25-link.png) | A clickable link/button to an external URL. | None (not linkable) |

<Alert type="note">

**Three widgets are plan-gated:** Advanced Map, Advanced Chart, and Image Map show an "Upgrade to unlock widget" state on the Free tier (the previews above show that locked state, not a working instance). See the [Plans Feature Matrix](/arduino-cloud/reference/plans-feature-matrix) for details.

</Alert>

## Next Steps

- [Dashboards](/arduino-cloud/dashboards/dashboards)
- [Cloud Variable Types](/arduino-cloud/reference/cloud-variable-types)
- [Plans Feature Matrix](/arduino-cloud/reference/plans-feature-matrix)

## Trademark Acknowledgments

- **LoRa®** is a registered trademark of Semtech Corporation.
