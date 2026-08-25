---
title: 'Linux on VENTUNO Q: System Configuration and Optimization'
overwriteSidebar: Linux Configuration
description: "Learn how to manage system services, schedule tasks, and monitor system resources on the Arduino® VENTUNO™ Q using standard Ubuntu Linux tools."
difficulty: advanced
tags:
  - Linux
  - Ubuntu
  - systemd
  - System administration
  - VENTUNO Q
author: 'José Bagur'
software:
  - app-lab
hardware:
  - hardware/14.ventuno/boards/ventuno-q
---

## Overview

The **Arduino® VENTUNO™ Q** runs a full Ubuntu Linux distribution on its Qualcomm® Dragonwing™ QCS8275 System on Chip (SoC), exposing the board as a complete single-board computer rather than just a development target for sketches and Apps. While the Arduino App Lab provides a streamlined workflow for building and deploying Apps, many production scenarios require direct interaction with the underlying operating system: launching custom processes at boot, scheduling periodic tasks, monitoring resource usage during long-running workloads, or integrating the board into a broader system administered through standard Linux tools.

This tutorial covers the core system administration tasks needed to operate the VENTUNO Q as a Linux device in production. The content is organized around standard Ubuntu utilities (`systemd`, `cron`, `journalctl`, and common monitoring tools) applied to scenarios relevant to the VENTUNO Q, such as running custom Python® services alongside the Arduino App Lab, observing resource consumption during AI inference, and managing services that interact with the board's peripherals.

This tutorial assumes the board has already been set up and that you have a working terminal session, either via SSH or ADB. If you have not yet configured access to the board, refer to the [VENTUNO Q User Manual](/tutorials/ventuno-q/user-manual) for the initial setup procedure.

## Goals

- Manage system services on the VENTUNO Q using `systemctl`.
- Create custom services that run user-defined scripts at boot.
- Schedule recurring tasks using `cron` and `systemd` timers.
- Monitor CPU, memory, storage, and process activity from the terminal.
- Apply general performance considerations relevant to long-running workloads.

## Hardware and Software Requirements

### Hardware Requirements

- [Arduino® VENTUNO™ Q](https://store.arduino.cc/products/ventuno-q) (x1)
- [Arduino® USB Type-C Cable (2in1)](https://store.arduino.cc/products/usb-cable2in1-type-c) (x1) or Ethernet connection for remote access
- Power supply (+7-24 VDC via barrel jack or screw terminal or USB-C® PD 9-20 V)

### Software Requirements

- A terminal session to the VENTUNO Q via SSH or ADB. Refer to the [Access via SSH or ADB](/tutorials/ventuno-q/user-manual#access-via-ssh-or-adb-terminal) section of the user manual.
- Basic familiarity with the Linux command line.

<Alert type="info">
The commands shown in this tutorial are standard Ubuntu utilities and behave identically to a desktop Ubuntu installation. The examples are related to the VENTUNO Q where the device context is relevant.
</Alert>

## Managing System Services with Systemd

Ubuntu uses `systemd` as its init system and service manager. On the VENTUNO Q, `systemd` is responsible for starting the network stack, the SSH server, the Bluetooth® stack, and the services that support the Arduino App Lab, among others. Managing these services from the terminal is essential when configuring the board for unattended operation or when troubleshooting a service that is not behaving as expected.

The main command-line interface to `systemd` is `systemctl`. Most operations that modify the system state require `sudo`.

### Listing Services

To see all services currently active on the board, run the following command:

```bash
systemctl list-units --type=service
```

The output of the command lists each service along with its load state, active state, and a short description. To inspect every service unit installed on the system (active or not), run:

```bash
systemctl list-unit-files --type=service
```

If you need to quickly identify services that have entered a failed state, run:

```bash
systemctl --failed
```

This command is particularly useful as **a first diagnostic step** when the board is not behaving as expected after a reboot or a software update.

### Checking the Status of a Service

To examine the current state of a specific service, use `systemctl status` followed by the service name. For example, to inspect the SSH server, run:

```bash
systemctl status ssh
```

The output reports whether the service is loaded, whether it is active, the process ID of the main service process, recent log entries, and the path to the unit file that defines the service. **This is the most informative command when diagnosing service issues**.

### Starting, Stopping, and Restarting Services

The basic lifecycle operations on a service are performed with the following commands:

```bash
sudo systemctl start <service-name>      # Start the service
sudo systemctl stop <service-name>       # Stop the service
sudo systemctl restart <service-name>    # Stop and start the service
sudo systemctl reload <service-name>     # Reload the service configuration without restarting
```

Not every service supports `reload`. When in doubt, `restart` is the safe option, although **it interrupts the service briefly**.

### Enabling and Disabling Services at Boot

Starting a service with `systemctl start` only affects the current session; the service will not start automatically on the next boot unless it is enabled. To configure a service to start at boot, run:

```bash
sudo systemctl enable <service-name>
```

To prevent a service from starting at boot, use `disable`:

```bash
sudo systemctl disable <service-name>
```

To check whether a service is configured to start at boot, run:

```bash
systemctl is-enabled <service-name>
```

A common shortcut when configuring a new service is to enable and start it in a single step:

```bash
sudo systemctl enable --now <service-name>
```

### Viewing Service Logs with Journalctl

The `systemd` command collects the output and diagnostic messages of every service into a **centralized journal**, which is queried using `journalctl`. To view the logs of a specific service, run:

```bash
journalctl -u <service-name>
```

For real-time monitoring, append the `-f` flag as shown below to follow new log entries as they are written:

```bash
journalctl -u <service-name> -f
```

The journal supports time-based filtering, which is useful when investigating an issue that occurred during a known window, for example:

```bash
journalctl -u <service-name> --since "1 hour ago"
journalctl -u <service-name> --since "2026-05-12 09:00" --until "2026-05-12 10:00"
```

To inspect everything logged since the last boot, run:

```bash
journalctl -b
```

<Alert type="info">

**The journal is stored in volatile memory by default on some Ubuntu configurations**, meaning **logs are lost on reboot**. To make the journal persistent across reboots, create the directory `/var/log/journal` and restart the `systemd-journald` service. **Verify the configuration on your VENTUNO Q before relying on long-term journal log retention**.

</Alert>

## Creating Custom Services

When the **Run at startup** feature in Arduino App Lab is not enough (for example, when running scripts that are not packaged as Apps, or when a process needs to start before Arduino App Lab is available) defining a custom `systemd` service provides fine-grained control over how and when a process runs, how it is restarted, and how its output is logged.

### Anatomy of a Service Unit

A service is defined by a unit file with the `.service` extension, typically placed in `/etc/systemd/system/` for system-wide services. The file is organized into three sections, as shown in the following template:

```bash
[Unit]
Description=Description of what this service does
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/arduino/my-script.py
WorkingDirectory=/home/arduino
Restart=on-failure
User=arduino

[Install]
WantedBy=multi-user.target
```

Each section has a different purpose:

- The `[Unit]` section describes the service and its ordering with respect to other units. `After=network.target` ensures the service starts only after the network stack is available, which is necessary for any process that requires connectivity. Other common targets are described in the note below.
- The `[Service]` section defines how the service runs. `Type=simple` indicates that the main process runs in the foreground, which is the most common case for scripts and long-running programs. `ExecStart` specifies the command to execute and must use absolute paths. `WorkingDirectory` sets the directory the process runs from, which is important for scripts that reference relative paths. `Restart=on-failure` instructs `systemd` to restart the service automatically if it exits with a non-zero status. `User` defines the account under which the process runs; on the VENTUNO Q, the default non-root user is `arduino`.
- The `[Install]` section determines when the service is activated. `WantedBy=multi-user.target` causes the service to start during a normal boot, after the system has reached multi-user mode.

<Alert type="info">

Common targets for the `After=` and `WantedBy=` directives include `multi-user.target` (system has reached multi-user mode without a graphical interface), `graphical.target` (graphical session is available), and `network-online.target` (network is fully configured and online, as opposed to merely available). Select the target that matches the requirements of the service.

</Alert>

### Example: Running a Python® Script at Boot

To illustrate the workflow explained before, we will configure a small Python® script that writes a timestamped entry to a log file every 10 seconds, starting automatically at boot. The procedure has three stages: writing the script, defining the service, and enabling it.

First, create the script at `/home/arduino/heartbeat.py` with the following content:

```python
import time
from datetime import datetime

LOG_FILE = "/home/arduino/heartbeat.log"

while True:
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now().isoformat()} - heartbeat\n")
    time.sleep(10)
```

Verify that the script runs correctly from the terminal before continuing:

```bash
python3 /home/arduino/heartbeat.py
```

Press `Ctrl+C` to stop the script and check that entries have been written to `/home/arduino/heartbeat.log`.

Next, create the service unit file at `/etc/systemd/system/heartbeat.service`. **Root privileges are required to write in this directory**:

```bash
sudo nano /etc/systemd/system/heartbeat.service
```

Paste the following content into the file:

```bash
[Unit]
Description=Heartbeat logger
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/arduino/heartbeat.py
WorkingDirectory=/home/arduino
Restart=on-failure
User=arduino

[Install]
WantedBy=multi-user.target
```

Save the file and reload the `systemd` configuration so it picks up the new unit as follows:

```bash
sudo systemctl daemon-reload
```

Enable the service so that it starts at boot, and start it immediately in the current session:

```bash
sudo systemctl enable --now heartbeat.service
```

Verify that the service is running and inspect its output using the commands covered in the previous section as follows:

```bash
systemctl status heartbeat.service
journalctl -u heartbeat.service -f
```

To stop the service, run `sudo systemctl stop heartbeat.service`. To remove it permanently, disable it, stop it, and delete the unit file, run the following:

```bash
sudo systemctl disable --now heartbeat.service
sudo rm /etc/systemd/system/heartbeat.service
sudo systemctl daemon-reload
```

<Alert type="info">

Whenever a unit file is created or modified, `sudo systemctl daemon-reload` must be run for the changes to take effect. **Forgetting this step is one of the most common causes of services not behaving as expected after edits**.

</Alert>

### Using a Python® Virtual Environment

If the script depends on libraries installed in a virtual environment, the `ExecStart` directive must point to the Python® interpreter inside that environment rather than to the system interpreter. For example, if the virtual environment is located at `/home/arduino/venv`, the directive becomes:

```bash
ExecStart=/home/arduino/venv/bin/python /home/arduino/my-script.py
```

This approach allows the service to use the correct set of dependencies without requiring the environment to be activated manually before each run.

### System Services and User Services

The services defined in `/etc/systemd/system/` run at the system level and are started before any user logs in. This is the appropriate choice for unattended workloads, services that must be available immediately at boot, and any process that needs to run regardless of user sessions.

`systemd` also supports user-level services, which are managed independently for each user and only run while that user's session is active. User unit files are placed in `~/.config/systemd/user/`, and the `systemctl` commands take a `--user` flag:

```bash
systemctl --user enable my-service.service
systemctl --user start my-service.service
```

**For most VENTUNO Q deployment scenarios, system services are the appropriate choice**. User services are useful primarily in development workflows or in setups where the board operates as a single-board computer with a logged-in graphical session.

## Scheduling Recurring Tasks

In addition to running services continuously, the VENTUNO Q can execute tasks on a schedule, such as periodic data uploads, log rotation, or maintenance scripts. Ubuntu offers two mechanisms for this: the traditional `cron` daemon and `systemd` timers. Both are valid, and the choice depends on the requirements of the task.

### Using Cron

`cron` is the classic Unix scheduler and is well suited to simple recurring tasks. Each user has a personal schedule, called a crontab, which is edited with:

```bash
crontab -e
```

The first time this command is run, you may be prompted to select a text editor. Each line in a crontab defines a scheduled task using five time fields followed by the command to run:

```text
* * * * * command
| | | | |
| | | | +---- Day of the week (0-7, where both 0 and 7 represent Sunday)
| | | +------ Month (1-12)
| | +-------- Day of the month (1-31)
| +---------- Hour (0-23)
+------------ Minute (0-59)
```

The following examples illustrate common schedules:

```bash
# Run a script every day at 2:00 AM
0 2 * * * /home/arduino/venv/bin/python /home/arduino/backup.py

# Run a script every 15 minutes
*/15 * * * * /home/arduino/check-status.sh

# Run a script once at every boot
@reboot /home/arduino/startup-task.sh
```

To list the current user's scheduled tasks, run `crontab -l`. To edit the root user's crontab (for tasks that require elevated privileges), use `sudo crontab -e`.

<Alert type="info">

Tasks executed by `cron` run in a minimal environment that does not load your shell profile. Always use absolute paths for both the interpreter and the script, and avoid relying on environment variables that are only defined in interactive sessions.

</Alert>

### Using Systemd Timers

`systemd` timers provide an alternative to `cron` with tighter integration into the rest of the system. Because the task runs as a regular service, its output is captured in the journal and can be inspected with `journalctl`, and it can declare dependencies on other units. Timers are a good choice when the scheduled task is closely tied to other services or when centralized logging is important.

A timer requires two unit files: a service that defines the task and a timer that defines the schedule. As an example, consider a daily backup task.

First, create the service file at `/etc/systemd/system/backup.service`. Note that `Type=oneshot` is used because the task runs to completion and then exits, rather than running continuously:

```bash
[Unit]
Description=Daily backup task

[Service]
Type=oneshot
ExecStart=/home/arduino/venv/bin/python /home/arduino/backup.py
User=arduino
```

Next, create the timer file at `/etc/systemd/system/backup.timer`:

```bash
[Unit]
Description=Run the backup task daily

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
```

The `OnCalendar` directive defines when the task runs. The `Persistent=true` directive ensures that if the board was powered off at the scheduled time, the task runs once the board boots again. The `OnCalendar` syntax is flexible:

```bash
OnCalendar=daily                      # Every day at midnight
OnCalendar=*-*-* 02:00:00             # Every day at 2:00 AM
OnCalendar=Mon *-*-* 09:00:00         # Every Monday at 9:00 AM
OnCalendar=*:0/15                     # Every 15 minutes
```

After creating both files, reload the configuration and enable the timer (not the service):

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now backup.timer
```

To list all active timers along with their next scheduled run time, use:

```bash
systemctl list-timers
```

This command provides a clear overview of every scheduled task managed by `systemd`, which is useful for confirming that a timer is configured correctly.

## Monitoring System Resources

Monitoring how the VENTUNO Q uses its resources is important when running demanding workloads such as AI inference, multi-camera capture, or continuous data processing. The following tools provide visibility into CPU, memory, storage, and process activity directly from the terminal.

### Processes and CPU Usage

The `top` command provides a live, continuously updated view of running processes, sorted by CPU usage by default. It is available on every Ubuntu installation:

```bash
top
```

A more readable and interactive alternative is `htop`, which presents per-core CPU usage, color-coded memory bars, and an easier interface for sorting and filtering processes. If it is not already installed, it can be added with:

```bash
sudo apt install htop
```

To obtain a one-time snapshot of all running processes, use `ps`. The following command lists the processes consuming the most memory:

```bash
ps aux --sort=-%mem | head
```

### Memory Usage

The VENTUNO Q is equipped with 16 GB of LPDDR5 RAM. To view current memory usage in a human-readable format, run:

```bash
free -h
```

The output shows total, used, free, and available memory, as well as any configured swap space. Monitoring the available memory while running AI models or processing large datasets helps determine whether a workload fits comfortably within the available RAM.

### Storage Usage

The VENTUNO Q includes 64 GB of eMMC storage, with the option to extend it through an M.2 connector using an NVMe drive. To view the usage of all mounted filesystems, run:

```bash
df -h
```

Each mounted filesystem appears as a separate entry, including the eMMC and any attached M.2 storage. To find which directories are consuming the most space within a given location, use `du`:

```bash
du -sh /home/arduino/*
```

### Network Activity

To inspect active network connections and listening ports, use `ss`:

```bash
ss -tulpn
```

This lists the TCP and UDP ports the board is listening on, along with the associated processes, which is helpful when verifying that a service is bound to the expected port or when diagnosing connectivity issues.

## Performance Considerations

Beyond monitoring, several system parameters influence how the VENTUNO Q performs under sustained load. The mechanisms described in this section are standard across Ubuntu systems, but the available options and their effects depend on the specific kernel and the Dragonwing™ QCS8275 platform.

<Alert type="warning">
The settings described in this section affect system behavior, power consumption, and thermal output. The available options, default values, and optimal configurations depend on the specific kernel and hardware of the VENTUNO Q. Verify each setting on your board, and test changes under your actual workload before applying them in a production deployment.
</Alert>

### Identifying Bottlenecks First

**Performance tuning should always begin with measurement**. Before changing any system parameter, use the monitoring tools from the previous section to identify the actual constraint. A workload limited by memory will not benefit from CPU adjustments, and a workload limited by storage throughput requires a different approach than one limited by CPU. Establishing a baseline with `top`, `free`, and `df` ensures that any change can be evaluated against measurable results.

### CPU Frequency Scaling

Linux manages processor clock speed through frequency scaling governors, which balance performance against power consumption and heat. The current governor and the frequencies available on the system can be queried through the `sysfs` interface:

```bash
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
```

Typical governors include `performance` (which keeps the processor at its highest available frequency) and `powersave` (which favors lower frequencies to reduce power draw). **The set of governors available on the VENTUNO Q depends on the kernel configuration for the Dragonwing™ QCS8275 and should be confirmed on the board before use**.

### Memory and Swap Behavior

The kernel parameter `vm.swappiness` controls **how aggressively the system moves data from RAM to swap**. A lower value keeps more data in RAM, which can benefit memory-intensive workloads, provided sufficient RAM is available. The current value can be inspected with:

```bash
cat /proc/sys/vm/swappiness
```

It can be adjusted temporarily with `sysctl`:

```bash
sudo sysctl vm.swappiness=10
```

To make a change persistent across reboots, add it to a file under `/etc/sysctl.d/`. Because this parameter only has an effect when swap is configured, first confirm the swap configuration of the board using `free -h`.

### Storage Considerations

**The onboard eMMC storage has a finite number of write cycles, like all flash-based storage**. Workloads that perform frequent or large writes (such as continuous logging or buffering large datasets) benefit from being directed to an M.2 NVMe drive when one is installed, both to improve throughput and to reduce wear on the eMMC. The journal persistence and logging configurations discussed earlier are worth reviewing for write-heavy deployments.

### Thermal and Power Awareness

Sustained high-performance workloads increase both power consumption and heat generation. The VENTUNO Q has defined power limits that depend on the supply voltage, as described in the [Power Overview](/tutorials/ventuno-q/user-manual#power-overview) section of the user manual. When configuring the board for demanding, continuous operation, ensure that the power supply is adequate for the expected load and that the board has enough ventilation.

## Troubleshooting

This section collects common issues encountered when configuring services and scheduled tasks on the VENTUNO Q, along with the recommended diagnostic steps.

### A Service Fails to Start

If a service does not start, begin by inspecting its status and logs:

```bash
systemctl status <service-name>
journalctl -u <service-name>
```

The most frequent causes are an incorrect absolute path in `ExecStart`, insufficient permissions for the configured `User`, or a missing `daemon-reload` after editing the unit file. Confirm that the command in `ExecStart` runs correctly when executed manually from the terminal.

### A Service Starts but Exits Immediately

A service that starts and then stops usually indicates that the program itself exited. Run the program manually to check its output and confirm it behaves as expected. For scripts that depend on a virtual environment, verify that `ExecStart` points to the interpreter inside the environment rather than to the system interpreter.

### A Scheduled Task Does Not Run

For `cron`, confirm that the entry uses absolute paths and that the command runs correctly in a minimal environment. For `systemd` timers, confirm that the timer (not the service) was enabled, and check the schedule:

```bash
systemctl list-timers
```

### The Journal Consumes Excessive Storage

If logs are filling the storage, the journal can be trimmed. The following commands limit the journal by size or by age:

```bash
sudo journalctl --vacuum-size=200M
sudo journalctl --vacuum-time=7d
```

These commands reduce the stored journal to the specified size or retention period and are useful for reclaiming space on a board that has been running for an extended period.

## Conclusion

In this tutorial, you learned how to operate the VENTUNO Q as a Linux system administered through standard Ubuntu tools. You now know how to manage services with `systemd`, create custom services that run scripts at boot, schedule recurring tasks with `cron` and `systemd` timers, monitor the board's resources, and approach performance tuning methodically.

These skills extend the capabilities of the VENTUNO Q beyond the Arduino App Lab workflow, enabling unattended deployments and tighter integration with the broader Linux ecosystem. To continue exploring the VENTUNO Q, refer to the [VENTUNO Q User Manual](/tutorials/ventuno-q/user-manual) for hardware details and initial setup, and to the other tutorials in the Linux category for related topics.
