---
title: Schedule jobs with the Scheduler
description: Automate a variable's value on a recurring time schedule with the CloudSchedule variable type and the Scheduler widget.
tags: [Arduino Cloud, Scheduler, Automation]
author: Karl Söderby & Arduino Team
---

The **Scheduler** automates a variable's value on a recurring schedule, entirely from a [Dashboard](/arduino-cloud/dashboards/dashboards) — no timing logic to write in your sketch. It's built around a dedicated variable type, `CloudSchedule`, and a matching **Scheduler** widget that configures when the variable is "on." Typical uses are turning a light on and off at fixed times, running an irrigation pump for a few minutes every morning, or firing any periodic action a device needs.

## How It Works

A `CloudSchedule` variable holds a boolean-like state: **active** or **inactive**. Your sketch only checks that state; the actual schedule (when it turns on, for how long, how often) lives in the cloud and is set from the widget:

```arduino
if (schedule_variable.isActive()) {
  // runs for as long as the schedule says "on"
}
```

Add a `CloudSchedule` like any other [Cloud Variable](/arduino-cloud/things-data/cloud-variables), from the **Time** category in the variable type picker.

![A schedule configured to run for 10 seconds every minute.](assets/cloud-scheduler-img-01.png)

### Core API Usage

In the sketch you only act on the state — typically driving an output while the schedule is active and clearing it otherwise:

```arduino
if (schedule_variable.isActive()) {
  digitalWrite(relay, HIGH);   // active window, e.g. pump/light ON
} else {
  digitalWrite(relay, LOW);    // inactive window, OFF
}
```

You can declare multiple `CloudSchedule` variables to run independent jobs at different times. A related `CloudTime` variable holds the current time and can be read with `ArduinoCloud.getLocalTime()`:

```arduino
time_variable = ArduinoCloud.getLocalTime();
```

For an end-to-end build (Thing, device, dashboard, and the full sketch), see [Smart Light Scheduler](/arduino-cloud/application-notes/automate-smart-light-scheduler).


## Configuring a Recurring Schedule

1. Open a [Dashboard](/arduino-cloud/dashboards/dashboards) in edit mode and add a **Scheduler** widget.
2. Click **Link Variable** and select the `CloudSchedule` variable of your Thing.
3. Optionally, set how the widget displays the start time (**Date and Time** or **Time only**), the **Date Formats** and the **Time Formats**. Click **Done**.

   ![The Scheduler widget settings, with Link Variable and the start time, date and time display options.](assets/scheduler-widget.png)

4. Set the schedule in the widget. The widget also shows the timezone the schedule uses.

| Parameter | Description |
|---|---|
| **Starting on** | Date and time of the first occurrence. |
| **Duration** | How long the "active" state lasts once triggered. |
| **Repeat every** | How often it recurs: minute, hour, day, week, month, or year. |
| **End recurrence** | Date and time after which the schedule stops firing, or never. |

A job set to **Starting on: today, Duration: 10 seconds, Repeat every: minute, End recurrence: never** activates the variable for 10 seconds every minute, indefinitely:

![The Scheduler in action, driving an LED widget and a counter.](assets/scheduler-action.gif)

<Alert type="note">

The schedule is interpreted using the Thing's [Timezone](/arduino-cloud/things-data/things) — set it correctly before relying on a schedule, otherwise the job fires at the wrong local time.

</Alert>

<Alert type="info">

The Scheduler widget only accepts `CloudSchedule` variables, and variable names are case-sensitive — a mismatch between the sketch and the Thing's variable name is the most common reason a schedule appears to do nothing.

</Alert>

## Related Articles

- [Choose an Automation](/arduino-cloud/automations/choose-an-automation)
- [Add & Link Widgets](/arduino-cloud/dashboards/add-link-widgets)
- [Cloud Variables](/arduino-cloud/things-data/cloud-variables)
