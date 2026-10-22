---
title: Arduino App CLI Command Reference
overwriteSidebar: Commands
description: Complete reference of all Arduino App CLI commands and options for managing Apps, Bricks, AI models, and system settings on your board.
tags: [Arduino App CLI, UNO Q, VENTUNO Q, Linux, CLI]
---

Manage Arduino Apps directly from the terminal using this command-line interface. Control the lifecycle of your applications, manage Bricks, and configure system settings without a graphical UI.

This reference covers Arduino App CLI 0.14. To check the version installed on your board, run `arduino-app-cli version`. For a task-oriented introduction, see [Manage Apps Using Arduino App CLI](../cli/).

Commands that take an `<app_path>` also accept an App ID, such as `user:my-app` or `examples:inspirational/blink`. See [Refer to Apps](../cli/#refer-to-apps).

<Alert type="info">

**Note:** `model install` takes one argument: a model ID from the catalog, a Hugging Face ID (`llamacpp:owner/repo:quant`, or `owner/repo` to let the board choose the quantization), or the URL of a model file. For example: `arduino-app-cli model install llamacpp:unsloth/Qwen3.5-0.8B-GGUF:Q4_K_M`. In Arduino App CLI 0.14, the `llamacpp:` form requires a quantization: `llamacpp:owner/repo` alone fails.

</Alert>

<!-- arduino-app-cli commands start -->
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

* `--format`: Output format (text, json, json-lines) (default "text")
* `--log-level`: Set the log level (debug, info, warn, error) (default "error")

---

## app

A CLI tool to manage Arduino Apps, including starting, stopping, logging, and provisioning.

**Usage:**
`arduino-app-cli app [subcommand]`

**Subcommands:**

* [brick](#app-brick)
* [build](#app-build)
* [clean-cache](#app-clean-cache)
* [destroy](#app-destroy)
* [details](#app-details)
* [export](#app-export)
* [import](#app-import)
* [install](#app-install)
* [list](#app-list)
* [logs](#app-logs)
* [new](#app-new)
* [ports](#app-ports)
* [ps](#app-ps)
* [restart](#app-restart)
* [start](#app-start)
* [stop](#app-stop)

## app brick

Manage the bricks of an Arduino App

**Usage:**
`arduino-app-cli app brick [subcommand]`

**Subcommands:**

* [config](#app-brick-config)

## app brick config

Set the value of a brick's variables in an Arduino App.

Variables given as "name" without a value will be prompted for a value on the terminal.
Variables given as "name=value" will be changed, without any prompt.
Variables given as "name=" with an empty value will be cleared, without any prompt.

On an App Release, only secret variables can be changed.

**Usage:**
`arduino-app-cli app brick config <app_path> brick_id name[=value] [name[=value] ...] [flags]`

**Options:**

* `--model`: The AI model the brick runs, by id

## app build

Build an Arduino App into a release archive.

A release is the app built for one board: the compiled sketch, the python
environment and the compose files. It is named after the app, the release label
and the target board, which defaults to the one running the build.

**Usage:**
`arduino-app-cli app build <app_path> [flags]`

**Options:**

* `--include-data`: Include data directory in the archive
* `--notes`: File with the release notes, or - to read them from the standard input
* `-o, --output`: Output archive, which names the release folder as well, or the directory to write it in
* `--overwrite`: Overwrite the output archive if it exists
* `--release-label`: Optional label to attach to the release, stored in its manifest
* `--target`: Board the release is built for (unoq, ventunoq). Defaults to the board running the build
* `-v, --verbose`: Enable verbose output

## app clean-cache

Delete app cache

**Usage:**
`arduino-app-cli app clean-cache <app-id> [flags]`

**Options:**

* `--force`: Forcefully clean the cache even if the app is running

## app destroy

Destroy an Arduino App

**Usage:**
`arduino-app-cli app destroy <app_path>`

## app details

Show an Arduino App's details

**Usage:**
`arduino-app-cli app details <app_path>`

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

## app install

Install an Arduino App release archive.

A release is the app built for one board, and it must be built for this board.
It is installed read only in the releases dir, apart from the apps.

The install then downloads what the release needs to run, its containers and its
models, which a start would otherwise wait for. Pass --no-prepare to install the
release alone, and prepare it later with 'start --prepare'.

A release can run commands on this device, so the install asks for a
confirmation first. Install a release only from trusted sources. Pass --yes to
install it without being asked.

**Usage:**
`arduino-app-cli app install release_path [flags]`

**Options:**

* `--no-prepare`: Install the release alone, without downloading its containers and its models
* `--yes`: Install without asking for confirmation

## app list

List the Arduino apps catalog.
By default the user apps and the apps installed from a release are shown. Use --examples to list the example apps, --releases to list only the apps installed from a release, or --all to list everything.
To see the live status of the apps on the board, use 'app ps' instead.

**Usage:**
`arduino-app-cli app list [flags]`

**Options:**

* `-a, --all`: List user apps, example apps and apps installed from a release
* `--examples`: Only list the example apps
* `--releases`: Only list the apps installed from a release
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
* `--from-app`: Create the new app from an existing app, example or App Release (path or ID)
* `-i, --icon`: Icon for the app
* `--no-sketch`: Do not include Sketch files

## app ports

Show the ports exposed by an app: the ones declared by its app.yaml, the ones declared by its bricks, and the ones published by the services the bricks require.

**Usage:**
`arduino-app-cli app ports <app_path>`

## app ps

List the Arduino apps that have been initialized at least once, and their live status.
By default, only starting, running, stopping and failed apps are shown. Use --all to also include stopped apps. Apps that have never been started are never shown; use 'app list' to browse the full catalog instead.

**Usage:**
`arduino-app-cli app ps [flags]`

**Options:**

* `-a, --all`: Also show stopped apps

## app restart

Restart or Start an Arduino App

**Usage:**
`arduino-app-cli app restart <app_path> [flags]`

**Options:**

* `-v, --verbose`: Enable verbose output

## app start

Start an Arduino App

**Usage:**
`arduino-app-cli app start <app_path> [flags]`

**Options:**

* `--no-prepare`: Start the app without preparing it first, failing if its containers or models are not already on the board
* `-v, --verbose`: Enable verbose output

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
  arduino-app-cli completion bash > completion.sh
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
* [install](#model-install)
* [list](#model-list)

## model delete

Delete the provided custom model

**Usage:**
`arduino-app-cli model delete <model_id> [flags]`

**Options:**

* `--force`: Delete model in use.

## model install

Install the provided model.

The argument is a model id from the catalog, a llama.cpp Hugging Face id
("llamacpp:owner/repo[:quant]"), or the URL of a model file the catalog does not
declare.

**Usage:**
`arduino-app-cli model install [flags]`

**Options:**

* `--mmproj-url`: URL of the companion mmproj file, when installing from a URL or a llama.cpp id

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

* [check](#system-check)
* [cleanup](#system-cleanup)
* [keyboard](#system-keyboard)
* [network-mode](#system-network-mode)
* [set-name](#system-set-name)
* [update](#system-update)

## system check

Verify the board provides what the apps need of it

**Usage:**
`arduino-app-cli system check`

## system cleanup

Removes unused and obsolete application images to free up disk space.

**Usage:**
`arduino-app-cli system cleanup [flags]`

**Options:**

* `--releases`: Also remove the images of the installed releases

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

<!-- arduino-app-cli commands end -->

<!-- markdownlint-disable-file -->
