# docs-content

## What Is this Repository?

This repository hosts the content for Arduino's documentation website. The content needs to be written in Markdown and will be converted to HTML automatically during the build process.

The production website is available at: <https://docs.arduino.cc>

## How Can I Contribute?

Contributing by creating content or suggestion changes to existing content can be done by making **pull requests**.
You start by forking the repository or by creating a new branch if you have write access to this repo. Create a new branch based on main and name it according to what you will create prefixed with your github username and a slash (e.g. `sebromero/wifi-tutorial`). Read in the section below how to add different types of new content.

When you're done with a draft you can create a pull request. This will give the content team the possibility to review it and leave comments or request changes. During this review process you can continue to push commits to the same branch. They will show up in the pull request automatically.
Once the pull request gests approved and merged into main, the content will be deployed to the live server.

## Fixing Bugs and Typos

If you found a mistake in the content you need to locate the corresponding file to fix it and create a pull request. Here is how to locate the content.

### Products

- If you found an issue in a hardware product-specific tutorial they are located according to the following pattern:
  `/content/hardware/[product-family]/[product-type]/[product]/tutorials/[tutorial-name]/[content-file].md`

- If you found an issue in a hardware product's datasheet they are located according to the following pattern:
  `/content/hardware/[product-family]/[product-type]/[product]/datasheet/datasheet.md`

- If you found an issue in a hardware product's description they are located according to the following pattern:
  `/content/hardware/[product-family]/[product-type]/[product]/product.md`

- If you found an issue in a hardware product's tech specs table they are located according to the following pattern:
  `/content/hardware/[product-family]/[product-type]/[product]/tech-specs.yml`

- If you found an issue in a hardware product's features they are located according to the following pattern:
  `/content/hardware/[product-family]/[product-type]/[product]/features.md`

### Software

- If you found an issue in a sofware product's tutorial they are located according to the following pattern:
  `/content/software/[product-name]/tutorials/(tutorial-subfolder)/[tutorial-name]/[content-file].md`

## Adding Content

### Referencing Content From Other Folders

The build system supports symlinks. This allows to include content in multiple places. For example, if there is a tutorial that works for different boards, it can be written once and included in different places. On Unix the `ln` command can be used for that.
For example, if we want a tutorial that lives here `content/tutorials/generic/basic-servo-control` to show up on the Nano 33 BLE product page, we can link it as follows. First open a shell and navigate to the tutorials folder of the product. e.g. `cd content/hardware/03.nano/boards/nano-33-ble/tutorials/`. Then create a symlink with a relative path to the tutorial. e.g. `ln -s ../../../../../tutorials/generic/basic-servo-control basic-servo-control`. This will create a symbolic link to that directory without duplicating it. Any change can be made in either location. They will be applied the original source file in both cases.

#### Adding Symlinks on Windows

To create symlinks using Windows OS, follow the below steps:

- Start a terminal (CMD) as admin.
- Navigate to the folder you want the symlinks. For example, to create a link for the UNO board, navigate to `docs.arduino.cc\content\hardware\02.hero\boards\uno-rev3\tutorials`.
- To create a symlink, you will need to run a command akin to:

```cmd
mklink AnalogInput "..\..\..\..\..\built-in-examples\03.analog\AnalogInput"
```

> The `..\..\` needs to match the location of the original file. Each `..\` is a step up the directory.

Note that when creating the symlink, you will not see a file in VS code, but when you commit changes it will be recognized.

On success, the following is printed:

```cmd
symbolic link created for AnalogInput <<===>> ..\..\..\..\..\built-in-examples\03.analog\AnalogInput
```

## Previewing Changes

Whenever you create a Pull Request (PR) GatsbyCloud will create a preview deployment in which you can see how your changes look when rendered on the website. The link to the preview will appear in the comments of the PR. This also works with Draft PRs, but not for PRs created from a fork.
