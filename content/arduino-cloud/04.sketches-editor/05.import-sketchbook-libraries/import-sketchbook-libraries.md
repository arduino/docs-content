---
title: Import Your Sketchbook and Libraries
description: Move an existing local Arduino sketchbook and custom libraries into the Cloud Editor in one step.
tags: [Arduino Cloud, Cloud Editor, Import]
author: Karl Söderby & Arduino Team
---

If your sketches and libraries currently live only on your computer (in the
offline Arduino IDE), the Cloud Editor's import tool moves them online in one
flow. After that they're available from any machine and backed up in your
cloud [sketchbook](/arduino-cloud/sketches-editor/sketchbook-and-sketches).

## What Can Be Imported

- Single sketches: `.ino`, `.pde`, or `.zip`.
- Libraries: `.zip`.
- A zipped folder containing both — keep libraries in a subfolder named
  literally `libraries`, and don't mix sketches and libraries in the same
  folder.

## Importing

1. Find your local sketchbook folder (named `Arduino` unless you renamed it) —
   typically `Documents/Arduino` on Windows and macOS, `$HOME/Arduino` on
   Linux.
2. Compress it to a `.zip` (not another archive format); you should get an
   `Arduino.zip`.
3. In the Cloud Editor, click the **Create** button in the top-right corner,
   select **Import local file**, and follow the instructions to upload your
   zip (or a single sketch).

A maximum of 100 MB is allowed per upload. Files in a `hardware` folder are
ignored, so exclude them from the zip. Sketches or custom libraries with names
that already exist online will prompt to overwrite rather than silently
replacing — proceed with caution.

### Importing a Custom Library

To import your own library, open any sketch, select **Libraries** in the left
panel, click **Custom**, and press the upload button, then choose your zipped
library. To import several at once, zip them all into a single file (with each
library in its own folder) and upload that.

## Next Steps

- [Sketchbook & Sketches](/arduino-cloud/sketches-editor/sketchbook-and-sketches)
- [Cloud Editor Overview](/arduino-cloud/sketches-editor/cloud-editor-overview)
- [Work Offline with the IDE](/arduino-cloud/sketches-editor/work-offline-ide)
