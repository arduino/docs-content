---
title: 'Importing files to the Cloud Editor'
description: 'Learn how to import your local sketchbook and custom libraries to the Cloud Editor.'
---

## Import Your Sketchbook and Libraries to the Cloud Editor

Are you sticking to the desktop Arduino IDE because all your work is saved locally? That’s no longer a problem! Our brand new import tool enables you to upload your entire sketchbook with just a few clicks on the [Arduino Cloud Editor](https://app.arduino.cc). It is particularly handy because it lets you **move all your sketches and libraries to the Cloud** in a single flow.

Once your sketchbook is online it will be available on any device and backed up.

What can you import to the [Cloud Editor](https://app.arduino.cc)?

* Single sketches in `.ino`, `.pde` and `.zip` format.
  
* Libraries in `.zip` format.
  
* Zipped folders containing sketches and libraries. Make sure your libraries are in a folder called `‘libraries’`. Be sure not to mix sketches and libraries in the same folder.

But let’s import your whole sketchbook in a few clicks, so you will be all set up to start using the Arduino Cloud Editor.


### 1. Find your sketchbook

On your PC find out where your sketchbook folder is (it is called `‘Arduino’`, unless you renamed it). On Windows it’s usually under `My Computer/Documents/Arduino`, on Mac `User/Documents/Arduino`, and on Linux is `$HOME/Arduino`.


### 2. Zip your sketchbook

Make a `.zip` pack of your sketchbook, you should obtain a file called *Arduino.zip*. Make sure it is `.zip` format, any other archive formats will not work.

![import_sketch_and_library_img_1](./assets/import_sketch_and_library_img_1.jpg)
![import_sketch_and_library_img_2](./assets/import_sketch_and_library_img_2.jpg)

### 3. Import your sketchbook to the Cloud

Go to [app.arduino.cc](https://app.arduino.cc). For some general information on how to get started on the Cloud Editor see [Getting Started with Arduino Cloud](https://docs.arduino.cc/arduino-cloud/guides/overview/). When you are logged in and ready, hit the "Create" button in the top right corner. Select "Import local file" and follow the instructions.

![import_sketch_and_library_img_3](./assets/import_1.png)
![import_sketch_and_library_img_4](./assets/import_2.png)

You can either upload single sketches or zip up your entire sketches folder, as described above and upload everything at once.

![import_sketch_and_library_img_4](./assets/import_3.png)

Wait for the upload process to complete.


### 4. You are done!

Once the import process is done you're all set.

If you already have sketches with the same name on the online IDE, these sketches will fail to import to avoid conflicts.

If you have libraries in your sketchbook, another report will tell you those that got successfully imported. If you have existing custom libraries with the same names, it’ll prompt you to overwrite the existing ones. Be sure to proceed with caution!


### Importing a custom library

The Arduino community has written over 700 libraries that you can include in your sketches without having to install a thing. You can browse through all of them in the Library Manager and favorite the ones you like the most.

But what if you want to use your own custom library on the Cloud Editor? To upload a custom library you need to open a sketch. Select "Libraries" on the left panel, click on "Custom" and press the upload button. Then just zip your custom library and upload it.

![Upload Custom Library](./assets/custom_library_1.png)

If you want to import multiple custom libraries at once you can do so by creating a single zip file which contains all of them and just import it.

## A few more notes on the importing process

* Maximum of 100MB is allowed, for either `.zip` or individual files, make sure your sketchbook does not exceeds this limit

* Only sketches and libraries can be imported. Files in the `‘hardware’` folder will be ignored. We suggest you exclude them from your `.zip`, especially if they’re taking a lot of space.

* Libraries must be in a folder called “`libraries`”.

* Remove backups, unrelated files and things you don’t want to import in general.

Please note that **all the libraries that you have added via the Library Manager on the desktop IDE will be already available on the Cloud Editor without having to do anything**. If you want to see their related examples or select a specific version, look for them on the online Library Manager.

### More tutorials

You can find more tutorials in the [Arduino Cloud documentation page](https://docs.arduino.cc/arduino-cloud/).