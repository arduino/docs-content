---
title: 'Customizing the Auto Formatter Feature'
difficulty: beginner
description: 'Learn how to configure the auto formatter feature'
tags:
 - Auto Formatter
 - Tools
author: 'Benjamin Dannegård, Per Tillisch'
---

Selecting **Edit > Auto Format** or pressing CTRL + T on Windows/Linux or CMD + T on MacOS when writing a sketch in the Arduino IDE 2 will automatically format the sketch. It is possible to change the behaviour of this command. In this tutorial we will go through how you can change the behaviour of this command. 

You can easily download the editor from the [Arduino Software page](https://www.arduino.cc/en/software). 

You can also follow the [downloading and installing the Arduino IDE 2](/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing) tutorial for more detailed guide on how to install the editor.

## Requirements

- Arduino IDE 2 installed. 

## Setting the Custom Configuration

It is possible to define your own custom configuration of the auto formatter feature in two different ways. The custom configuration of the auto formatter can be set on a global level to cover all sketches opened in the editor, or you can set the configuration to be specific to a sketch.

The formatter tool used by Arduino IDE 2 is ClangFormat. The documentation for the configuration options is [here](https://clang.llvm.org/docs/ClangFormatStyleOptions.html).

### Global scope
If you add a `.clang-format` configuration file to either of the following locations, the Arduino IDE 2 will always use it instead of the Arduino default configuration.

If you are using Windows place the file in:
```
C:\Users\<username>\.arduinoIDE\
```
Or
```
C:\Users\<username>\AppData\Local\Arduino15\
```

If you are using Linux place the file in:
```
~/.arduinoIDE/
```
Or
```
~/.arduino15/
```

If you are using macOS place the file in:
```
~/.arduinoIDE
```
Or
```
~/Library/Arduino15/
```

### Sketch scope
If you add a `.clang-format` configuration file to the root of a sketch, the Arduino IDE will use that configuration when formatting that sketch. This file has precedence over a global formatter configuration file.

![.clang-format file at the root of a sketch](assets/format-file-at-root.png)

## Default Formatting File

Here you can find the default formatting file used in the Arduino IDE 2. If you wish to customize how your auto formatting acts in the IDE then starting with this file is a good idea.

https://raw.githubusercontent.com/arduino/tooling-project-assets/main/other/clang-format-configuration/.clang-format

***Please note that the custom configuration file completely overrides the Arduino default configuration, rather than merging with it. Any configuration option you don't set in your custom file will be set to the ClangFormat default value.***

## Conclusion

In this tutorial we went through how to customize the behavior of the `CTRL + T` / `CMD + T` auto formatter command in the Arduino IDE 2. This tutorial also shows the different scopes that are available for the auto formatter configuration.

### More Tutorials

You can find more tutorials in the [Arduino IDE 2 documentation page](/software/ide-v2/).
