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

### Create a New Datasheet

- Create a new feature branch for the datasheet using a `datasheets` prefix. E.g. `datasheets/mkr-1010`
- You can collaborate with other people on the same branch. For larger changes in a multi-people collaboration setting you can create a separate branch that is based on the feature branch. e.g. `datasheets/mkr-1010-certification` based on `datasheets/mkr-1010`.
- Inside the product directory e.g. `content/hardware/01.mkr/boards/mkr-wifi-1010` create a folder named `datasheet` for the new datasheet
- In your newly created folder create the `datasheet.md` file that will contain the content of the datasheet.
- Create a subfolder called `assets` where you put all the images that are used in the datasheet.
- Images that purely consist of illustrations should be in SVG format binary images in PNG format. **Make sure to outline the text for SVG exports**. Both Figma and Illustrator provide this option in their file export settings.
- When you're done with a section of the datasheet that was worked on in a specific branch e.g. `datasheets/mkr-1010-certification` create a Pull Request to merge that branch back into the original feature branch e.g. `datasheets/mkr-1010-certification` -> `datasheets/mkr-1010`. Request a review from the responsible person for this datasheet creation task or additional people from whome you need confirmation on correctness (e.g. from the hardware/firmware team).
- When you're done with the complete datasheet and you want to merge it back into main, create a pull request e.g. `datasheets/mkr-1010` -> `main`. The build process will create a PDF from the datasheet that will be deployed automatically to the website. ⚠️ This will only work if the branch name contains `datasheet` or `datasheets` in its name, and the PR is not created from a fork.
  Request a review from the responsible person for this datasheet creation task or additional people from whome you need confirmation on correctness (e.g. from the hardware/firmware team).
- Make sure to preview the datasheet in its rendered form while you're working on it to check for visual glitches. You can do so using the datasheet generator tool.

### Linking a Datasheet to a Product

If the datasheet is created from markdown and put inside the `datasheet` folder it shows up on the product page automatically. **IMPORTANT:** In order to speed up the preview builds, the datasheets will only be generated if the branch name contains `datasheet` or when the changes are merged back to the `main` branch. You can also set a `url_datasheet` property in the frontmatter part of a product page (product.md) which points to a URL. For the datasheet button in the product page header, the URL will take precedence over the generated datasheet. In the downloads section only the generated datsheets appear.

### Adding a new Product Family

To add a new family of products, create a new folder under `/content/hardware/`. Please note that the sorting is based on the family name. Therefore, if you need a specific sorting, prepend the name with a number (e.g. 05.nicla).
Inside that folder create a file named `family.md` and fill in the following contents:

```
---
title: Family Name
description: Description of that product family
---
```

The new family will only show up if it contains at least one product.

### Adding a new Product

#### Features

To add features to a product, a `features.md` file needs to be created in the root folder of a product.
To list the features the `Feature` tag can be used. The list of features needs to be wrapped inside a `<FeatureList></FeatureList>` tag pair. E.g. `<FeatureList><Feature title="Raspberry Pi RP2040 Microcontroller" image="chip"></FeatureList>`.

Each feature can have one of the following icons:

| name               | icon                                                      |
| ------------------ | --------------------------------------------------------- |
| bluetooth          | ![](src/components/product/images/bluetooth.svg)          |
| camera             | ![](src/components/product/images/camera.svg)             |
| cellular           | ![](src/components/product/images/cellular.svg)           |
| color-sensor       | ![](src/components/product/images/color-sensor.svg)       |
| communication      | ![](src/components/product/images/communication.svg)      |
| configurability    | ![](src/components/product/images/configurability.svg)    |
| connection         | ![](src/components/product/images/connection.svg)         |
| core               | ![](src/components/product/images/core.svg)               |
| crypto-chip        | ![](src/components/product/images/crypto-chip.svg)        |
| file-icon          | ![](src/components/product/images/file-icon.svg)          |
| humidity-sensor    | ![](src/components/product/images/humidity-sensor.svg)    |
| hw-pin             | ![](src/components/product/images/hw-pin.svg)             |
| imu                | ![](src/components/product/images/imu.svg)                |
| led                | ![](src/components/product/images/led.svg)                |
| light-sensor       | ![](src/components/product/images/light-sensor.svg)       |
| location           | ![](src/components/product/images/location.svg)           |
| magnetometer       | ![](src/components/product/images/magnetometer.svg)       |
| mcu                | ![](src/components/product/images/mcu.svg)                |
| mega-form-factor   | ![](src/components/product/images/mega-form-factor.svg)   |
| microphone         | ![](src/components/product/images/microphone.svg)         |
| mkr-form-factor    | ![](src/components/product/images/mkr-form-factor.svg)    |
| nano-form-factor   | ![](src/components/product/images/nano-form-factor.svg)   |
| nicla-form-factor  | ![](src/components/product/images/nicla-form-factor.svg)  |
| power              | ![](src/components/product/images/power.svg)              |
| pressure-sensor    | ![](src/components/product/images/pressure-sensor.svg)    |
| proximity-sensor   | ![](src/components/product/images/proximity-sensor.svg)   |
| python             | ![](src/components/product/images/python.svg)             |
| sim-card           | ![](src/components/product/images/sim-card.svg)           |
| temperature-sensor | ![](src/components/product/images/temperature-sensor.svg) |
| uno-form-factgor   | ![](src/components/product/images/uno-form-factor.svg)    |
| usb                | ![](src/components/product/images/usb.svg)                |
| uv-sensor          | ![](src/components/product/images/uv-sensor.svg)          |
| wifi-bluetooth     | ![](src/components/product/images/wifi-bluetooth.svg)     |
| wifi               | ![](src/components/product/images/wifi.svg)               |
| world-map          | ![](src/components/product/images/world-map.svg)          |

### Add Certifications

The certifications for each product can be added in the frontmatter of a product in the `product.md` (e.g. `certifications: [FCC, CE, RoHS]`) and the PDF can be added to the corresponding product’s `certifications` directory. The naming should be as follows <SKU>_<CERTIFICATION>_<CATEGORY>.pdf e.g. `ABX00023_FCC_DTS.pdf`

### Including Code Snippets

Code snippets can be included by using the triple backticks syntax e.g. ` ```arduino` followed by the code and three closing backticks. The following syntaxes are supported:

arduino, bash, markup, clike, c, cpp, css, css-extras, javascript, jsx, js-extras, coffeescript, diff, git, go, graphql, handlebars, json, less, makefile, markdown, objectivec, ocaml, python, reason, sass, scss, sql, stylus, tsx, typescript, wasm, yaml

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
