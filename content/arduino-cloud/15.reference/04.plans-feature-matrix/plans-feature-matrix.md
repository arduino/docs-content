---
title: Plans Feature Matrix
description: A feature-by-plan comparison of Arduino Cloud tiers — Things limit, data retention, OTA, Triggers, advanced widgets, sharing, API access, and compile time.
tags: [Arduino Cloud, Plans, Reference]
author: TODO
---

A side-by-side comparison of what each Arduino Cloud plan includes. Use it to
pick a tier or to understand why a feature is locked. For current pricing and
the authoritative limits, see
[Plans, Limits & Quotas](/arduino-cloud/spaces-plans-account/plans-limits-quotas).

<Alert type="warning">

Needs verification: the exact numbers below (Things limits, retention
periods, compile time, API quotas) change with plan updates and were not
re-confirmed against live pricing this pass. Treat every cell as indicative
and verify against [Plan Usage](https://app.arduino.cc/plan-usage) and the
official pricing page before publishing.

</Alert>

## Feature Comparison

| Feature | Free | Maker | Maker Plus | Business / Enterprise |
|---|---|---|---|---|
| Things | Limited (e.g. 2) | More | More | Scales (multiples of 50) |
| Historical data retention | Short (e.g. 1 day) | Extended | Longer | Longest / configurable |
| Over-the-air (OTA) updates | — | Yes | Yes | Yes |
| Triggers / alerts | Limited | Yes | Yes | Yes |
| Advanced widgets (Advanced Map/Chart, Image Map) | — | Yes | Yes | Yes |
| Dashboard sharing | Limited | Yes | Yes | Yes + RBAC |
| API access | Limited | Yes | Yes | Yes |
| Compile/upload time | Limited/day | Extended | Unlimited | Unlimited |
| Node-RED integration | — | Yes | Yes | Yes |
| Fleet management / RBAC | — | — | — | Yes |
| Custom branding / white labeling | — | — | — | Yes |
| Data export (e.g. AWS S3) | — | — | Varies | Yes |

<Alert type="note">

The three plan-gated dashboard widgets — Advanced Map, Advanced Chart, and
Image Map — appear in a locked "Upgrade to unlock" state on the Free tier.
See the [Widget Catalog](/arduino-cloud/reference/widget-catalog).

</Alert>

## Next Steps

- [Plans, Limits & Quotas](/arduino-cloud/spaces-plans-account/plans-limits-quotas)
- [Arduino Cloud for Business](/arduino-cloud/business)
- [Widget Catalog](/arduino-cloud/reference/widget-catalog)
