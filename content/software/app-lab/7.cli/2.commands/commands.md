---
title: Arduino App CLI Command Reference
overwriteSidebar: Commands
description: 
tags: [Arduino App CLI, UNO Q, Linux, CLI]
---

A CLI to manage Arduino Apps

## arduino-app-cli

**Usage:**
`arduino-app-cli [subcommand]`

**Subcommands:**

* [app](#app)
* [brick](#brick)
* [completion](#completion)
* [config](#config)
* [daemon](#daemon)
* [model](#model)
* [monitor](#monitor)
* [properties](#properties)
* [system](#system)
* [version](#version)

### Global Options

* `--format`: Output format (text, json) (default "text")
* `--log-level`: Set the log level (debug, info, warn, error) (default "error")

---

## app

A CLI tool to manage Arduino Apps, including starting, stopping, logging, and provisioning.

**Usage:**
`arduino-app-cli app [subcommand]`

**Subcommands:**

* [clean-cache](#app-clean-cache)
* [destroy](#app-destroy)
* [export](#app-export)
* [import](#app-import)
* [list](#app-list)
* [logs](#app-logs)
* [new](#app-new)
* [restart](#app-restart)
* [start](#app-start)
* [stop](#app-stop)

## app clean-cache

Delete app cache

**Usage:**
`arduino-app-cli app clean-cache <app_id> [flags]`

**Options:**

* `--force`: Forcefully clean the cache even if the app is running

## app destroy

Destroy an Arduino App

**Usage:**
`arduino-app-cli app destroy <app_path>`

## app export

Export an existing Arduino App to a zip file.
Use '-' as output_path to write the zip to stdout.

**Usage:**
`arduino-app-cli app export <app_path> [output_path] [flags]`

**Options:**

* `--include-data`: Include data directory in the archive
* `--overwrite`: Overwrite output file if it exists

## app import

Import an Arduino App from a zip file.
Use '-' as zip_path to read the zip from stdin.

**Usage:**
`arduino-app-cli app import <zip_path>`

## app list

List the Arduino apps

**Usage:**
`arduino-app-cli app list [flags]`

**Options:**

* `--show-broken-apps`: Output a list of broken apps

## app logs

Show the logs of the Python app

**Usage:**
`arduino-app-cli app logs <app_path> [flags]`

**Options:**

* `--all`: Show all logs
* `--follow`: Follow the logs
* `--tail`: Tail the last N logs (default "100")

## app new

Creates a new Arduino App

**Usage:**
`arduino-app-cli app new <name> [flags]`

**Options:**

* `-b, --bricks`: List of bricks to include in the app
* `-d, --description`: Description for the app
* `--from-app`: Create the new app from the path of an existing app
* `-i, --icon`: Icon for the app
* `--no-sketch`: Do not include Sketch files

## app restart

Restart or Start an Arduino App

**Usage:**
`arduino-app-cli app restart <app_path>`

## app start

Start an Arduino App

**Usage:**
`arduino-app-cli app start <app_path>`

## app stop

Stop an Arduino App

**Usage:**
`arduino-app-cli app stop <app_path>`

## brick

Manage Arduino Bricks

**Usage:**
`arduino-app-cli brick [subcommand]`

**Subcommands:**

* [details](#brick-details)
* [list](#brick-list)

## brick details

Details of a specific brick

**Usage:**
`arduino-app-cli brick details <brick_id>`

## brick list

List all available bricks

**Usage:**
`arduino-app-cli brick list`

## completion

Generates completion scripts for various shells (bash, zsh, fish, powershell)

**Usage:**
`arduino-app-cli completion <shell> [flags]`

**Options:**

* `--no-descriptions`: Disable completion description for shells that support it

**Example:**
```text
  /var/folders/58/gntldnl9249ck9fjblgv9jdw0000gp/T/go-build862741151/b001/exe/gendoc completion bash > completion.sh
  source completion.sh
```

## config

Manage Arduino App CLI config

**Usage:**
`arduino-app-cli config [subcommand]`

**Subcommands:**

* [get](#config-get)

## config get

get configuration

**Usage:**
`arduino-app-cli config get`

## daemon

Run the Arduino App CLI as an HTTP daemon

**Usage:**
`arduino-app-cli daemon [flags]`

**Options:**

* `--port`: The TCP port the daemon will listen to (default "8080")

## model

Manage Arduino Models

**Usage:**
`arduino-app-cli model [subcommand]`

**Subcommands:**

* [delete](#model-delete)
* [list](#model-list)

## model delete

Delete the provided custom model

**Usage:**
`arduino-app-cli model delete <model_id> [flags]`

**Options:**

* `--force`: Delete model in use.

## model list

List all models

**Usage:**
`arduino-app-cli model list [flags]`

**Options:**

* `--exclude-builtin`: Do not show Arduino builtin models.

## monitor

Attach to the microcontroller serial monitor

**Usage:**
`arduino-app-cli monitor`

## properties

Manage apps properties, including setting and getting the default app.

**Usage:**
`arduino-app-cli properties [subcommand]`

**Subcommands:**

* [get](#properties-get)
* [set](#properties-set)

## properties get

Get properties, e.g., default

**Usage:**
`arduino-app-cli properties get default`

## properties set

Set properties. Use 'none' to unset a property.

**Usage:**
`arduino-app-cli properties set default <app_path>`

## system

Manage the board’s system configuration

**Usage:**
`arduino-app-cli system [subcommand]`

**Subcommands:**

* [cleanup](#system-cleanup)
* [keyboard](#system-keyboard)
* [network-mode](#system-network-mode)
* [set-name](#system-set-name)
* [update](#system-update)

## system cleanup

Removes unused and obsolete application images to free up disk space.

**Usage:**
`arduino-app-cli system cleanup`

## system keyboard

Manage the keyboard layout of the system

**Usage:**
`arduino-app-cli system keyboard [layout]`

## system network-mode

Manage the network mode of the system. Commands: enable, disable, status.

**Usage:**
`arduino-app-cli system network-mode <command>`

## system set-name

Set the custom name of the board

**Usage:**
`arduino-app-cli system set-name <name>`

## system update

Launches an update of the upgradable packages on the system

**Usage:**
`arduino-app-cli system update`

**Options:**

* `--only-arduino`: Only upgrades Arduino specific packages
* `--yes`: Automatically confirm all prompts

## version

Print the version number of Arduino App CLI

**Usage:**
`arduino-app-cli version [flags]`

**Options:**

* `--port`: The daemon network port (default "8800")

