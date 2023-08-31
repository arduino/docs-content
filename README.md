# docs-content

## What Is this Repository?

This repository hosts the content for Arduino's documentation website. The content needs to be written in Markdown and will be converted to HTML automatically during the build process.

The production website is available at: <https://docs.arduino.cc>

## How Can I Contribute?

Contributing by creating content or suggestion changes to existing content can be done by making **pull requests**.

You start by forking the repository or by creating a new branch if you have write access to this repo. Create a new branch based on main and name it according to what you will create prefixed with your github username and a slash (e.g. `sebromero/wifi-tutorial`). Read in the section below how to add different types of new content.

When you're done with a draft you can create a pull request. This will give the content team the possibility to review it and leave comments or request changes. During this review process you can continue to push commits to the same branch. They will show up in the pull request automatically.

Once the pull request gests approved and merged into main, the content will be deployed to the live server.

There are four different content types you can contribute with. These are **tutorial**, **article**, **how to** and **project**. Please read more on what they mean and how to write one in the [Contribution Templates folder](/contribution-templates/README.md).

|Content|Description|Example|
|-------|-----------|-------|
|Tutorial|Learn how to do something.|[Control Built-in RGB LED over Wi-Fi with Nano RP2040 Connect](https://docs.arduino.cc/tutorials/nano-rp2040-connect/rp2040-web-server-rgb)|
|Article|Learn about a specific topic.|[Multimeter Basics](https://docs.arduino.cc/learn/electronics/multimeter-basics)|
|How To|Smaller tutorial with less information and more straight to the example.|[Analog Read Serial](https://docs.arduino.cc/built-in-examples/basics/AnalogReadSerial)|
|Project|Learn how to build something.|[Plant Communicator with MKR WiFi 1010](https://projecthub.arduino.cc/Arduino_Genuino/plant-communicator-with-mkr-wifi-1010-081cf5)|

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

- If you found an issue in a software product's tutorial they are located according to the following pattern:
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

### Including Code Snippets

Code snippets can be included by using the triple backticks syntax e.g. ` ```arduino` followed by the code and three closing backticks. The following syntaxes are supported:
```
arduino, bash, markup, clike, c, cpp, css, css-extras, javascript, jsx, js-extras, coffeescript, diff, git, go, graphql, handlebars, json, less, makefile, markdown, objectivec, ocaml, python, reason, sass, scss, sql, stylus, tsx, typescript, wasm, yaml
```

### Including Code Blocks fetching Github pages

CodeBlocks are custom components that can be added directly in the Markdown on docs-content.
Using this component, the code block will be fetched directly from Github pages.

Syntax:
` <CodeBlock url=”https://github.com/example” className="{language}"/>`
 
Broken URL will show error alert. URL must be in Github domain and must be public.

## Previewing Changes

Whenever you create a Pull Request (PR) GatsbyCloud will create a preview deployment in which you can see how your changes look when rendered on the website. The link to the preview will appear in the comments of the PR. This also works with Draft PRs, but not for PRs created from a fork.

## License

![](https://i.creativecommons.org/l/by-sa/3.0/88x31.png) 

Please note that your contribution to the Arduino Documentation is licensed under a Creative Commons Attribution-Share Alike 4.0 License. see https://creativecommons.org/licenses/by-sa/4.0/

