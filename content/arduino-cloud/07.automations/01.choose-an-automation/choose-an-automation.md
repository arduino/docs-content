---
title: Choose an Automation
description: A decision guide to pick between Triggers, the Scheduler, Webhooks, and device connectivity alerts based on your goal.
tags: [Arduino Cloud, Automation]
author: Karl Söderby & Arduino Team
---

Arduino Cloud offers several ways to act on your project automatically. They
overlap a little, so this page maps a goal to the right tool. Start from what
you want to happen, then follow the link to set it up.

## Decision Guide

| Your goal | Use | Why |
|---|---|---|
| React when a variable crosses a threshold or matches a value (e.g. temperature > 30 → email/push) | [Triggers & Alerts](/arduino-cloud/automations/triggers-and-alerts) | Watches a Cloud Variable's condition and fires email, push, or a webhook. Paid plan. |
| Know when a device connects or disconnects | [Device Online/Offline Alerts](/arduino-cloud/automations/device-online-offline-alerts) | Reacts to connectivity state rather than a variable value. |
| Do something on a time schedule (e.g. run a pump every morning) | [Scheduler](/arduino-cloud/automations/scheduler) | Drives a variable's state on a recurring schedule, no timing code needed. |
| Send data or events to an external service (IFTTT, Zapier, your backend) | [Webhooks](/arduino-cloud/automations/webhooks) | POSTs variable updates or Trigger events to a URL you control. |

## How They Combine

These aren't mutually exclusive — a real project often uses several together:

- A **Trigger** can *use* a **webhook** as its action, so only a specific
  condition forwards data to an external service.
- A **Scheduler** changes a variable on a schedule, and a **Trigger** or
  **Thing-level webhook** can then react to that change.
- **Device alerts** complement value-based Triggers: one watches
  *connectivity*, the other watches *data*.

<Alert type="info">

If you only need to *see* data rather than act on it, you may not need an
automation at all — a [Dashboard](/arduino-cloud/dashboards/dashboards) with
the right widgets covers live monitoring and historical charts.

</Alert>

## Next Steps

- [Triggers & Alerts](/arduino-cloud/automations/triggers-and-alerts)
- [Scheduler](/arduino-cloud/automations/scheduler)
- [Webhooks](/arduino-cloud/automations/webhooks)
