---
title: Cloud Variable Types
description: The complete list of Arduino Cloud Variable types — basic, specialized, and complex — with each one's underlying C++ type, plus the Alexa-compatible subset.
tags: [Arduino Cloud, Variables, Reference]
author: Karl Söderby & Arduino Team
---

[Cloud Variables](/arduino-cloud/things-data/cloud-variables) come in three
categories: **basic** primitives, **specialized** wrappers that add semantic
meaning (for smarter integrations and widgets), and **complex** types that
hold multiple values. This page lists every type and the C++ type it maps to
in your generated sketch.

## Basic Types

| Type | C++ Declaration |
|---|---|
| Boolean | `bool variableName;` |
| Character String | `String variableName;` |
| Floating Point Number | `float variableName;` |
| Integer Number | `int variableName;` |

## Specialized Types

Specialized types are wrappers around a basic type that declare the
variable's semantics explicitly. You use them like a normal variable of the
wrapped type — they support assignment and comparison operators.

| Type | C++ Declaration | Wrapped Type |
|---|---|---|
| Acceleration | `CloudAcceleration variableName;` | `float` |
| Angle | `CloudAngle variableName;` | `float` |
| Area | `CloudArea variableName;` | `float` |
| Capacitance | `CloudCapacitance variableName;` | `float` |
| Contact Sensor | `CloudContactSensor variableName;` | `bool` |
| Counter | `CloudCounter variableName;` | `int` |
| Data Rate | `CloudDataRate variableName;` | `float` |
| Electric Current | `CloudElectricCurrent variableName;` | `float` |
| Electric Potential | `CloudElectricPotential variableName;` | `float` |
| Electric Resistance | `CloudElectricResistance variableName;` | `float` |
| Energy | `CloudEnergy variableName;` | `float` |
| Flow Rate | `CloudFlowRate variableName;` | `float` |
| Force | `CloudForce variableName;` | `float` |
| Frequency | `CloudFrequency variableName;` | `float` |
| Heart Rate | `CloudHeartRate variableName;` | `float` |
| Information Content | `CloudInformationContent variableName;` | `int` |
| Length | `CloudLength variableName;` | `float` |
| Light | `CloudLight variableName;` | `bool` |
| Logarithmic Quantity | `CloudLogarithmicQuantity variableName;` | `float` |
| Luminance | `CloudLuminance variableName;` | `float` |
| Luminous Flux | `CloudLuminousFlux variableName;` | `float` |
| Luminous Intensity | `CloudLuminousIntensity variableName;` | `float` |
| Mass | `CloudMass variableName;` | `float` |
| Motion Sensor | `CloudMotionSensor variableName;` | `bool` |
| Percentage | `CloudPercentage variableName;` | `float` |
| Power | `CloudPower variableName;` | `float` |
| Pressure | `CloudPressure variableName;` | `float` |
| Relative Humidity | `CloudRelativeHumidity variableName;` | `float` |
| Smart Plug | `CloudSmartPlug variableName;` | `bool` |
| Switch | `CloudSwitch variableName;` | `bool` |
| Temperature | `CloudTemperature variableName;` | `float` |
| Temperature Sensor | `CloudTemperatureSensor variableName;` | `float` |
| Time | `CloudTime variableName;` | `float` |
| Velocity | `CloudVelocity variableName;` | `float` |
| Volume | `CloudVolume variableName;` | `float` |

## Complex Types

These hold multiple internal values, accessed through methods.

| Type | C++ Declaration | Holds |
|---|---|---|
| CloudSchedule | `CloudSchedule variableName;` | Active state + start/end/length timestamps (`isActive()`, `getCloudValue()`). |
| DimmedLight | `CloudDimmedLight variableName;` | Switch (`bool`) + brightness (`float` 0–100). |
| ColoredLight | `CloudColoredLight variableName;` | Switch + hue/saturation/brightness + RGB. |
| CloudColor | `CloudColor variableName;` | Hue/saturation/brightness, read via `getValue()`. |
| CloudLocation | `CloudLocation variableName;` | Latitude/longitude, set with a `Location` object. |
| Television | `CloudTelevision variableName;` | Switch, volume, mute, playback command, input, channel. |

<Alert type="info">

Complex types expose getters/setters rather than direct assignment — for
example `cLight.getSwitch()` / `cLight.setSwitch()`, or
`schedule.isActive()`. See
[Cloud Variables](/arduino-cloud/things-data/cloud-variables) for usage
examples.

</Alert>

## Alexa-Compatible Types

The [Amazon Alexa integration](/arduino-cloud/integrations/amazon-alexa)
supports only a subset of variable types. Variables of any other type won't
appear in the Alexa app.

| Type | Values |
|---|---|
| Colored Light | `bool` + `float` (complex) |
| Dimmed Light | `bool` + `float` (complex) |
| Television | `bool` + `int` (complex) |
| Contact Sensor | `bool` |
| Light | `bool` |
| Motion Sensor | `bool` |
| Smart Plug | `bool` |
| Switch | `bool` |
| Temperature Sensor | `float` |

## Next Steps

- [Cloud Variables](/arduino-cloud/things-data/cloud-variables)
- [Widget Catalog](/arduino-cloud/reference/widget-catalog)
- [Amazon Alexa Integration](/arduino-cloud/integrations/amazon-alexa)

## Trademark Acknowledgments

- **LoRa®** is a registered trademark of Semtech Corporation.
