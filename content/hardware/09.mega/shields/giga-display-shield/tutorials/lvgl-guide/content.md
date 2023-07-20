---
title: Guide for Using LVGL With the GIGA Display Shield
description: 'Learn how to use LVGL with the GIGA display shield'
author: Benjamin Dannegård
tags: [Display, LVGL]
---

## Introduction

LVGL is a very powerful graphical framework that is compatible with the Giga Display Shield. It will allow you to put components on the screen like buttons, images, loading bars, sliders, checkboxes etc. It also allows you fully customize the screenspace on the display. This guide will go through the different components in detail so you can learn how to best implement it to your project.

## Hardware & Software Needed

- [GIGA R1 WiFi](/hardware/giga-r1).
- [GIGA Display Shield](/hardware/giga-display-shield)
- [Arduino IDE](https://www.arduino.cc/en/software)
- [Arduino_H7_Video]() library.
- [Arduino_GigaDisplayTouch]() library.

## Downloading the Library and Core

The GIGA core includes a library that will help us handle the display, so make sure you have the latest version of the core. This library is called **Arduino_H7_Video**.

In this guide, we will be using three different libraries:
- **Arduino_H7_Video**, this one is bundled with the core, so make sure you have the latest version of the [Mbed core](https://github.com/arduino/ArduinoCore-mbed)
- **Arduino_GigaDisplayTouch**
- **lvgl** 

Open the library manager and install the latest version of **Arduino_GigaDisplayTouch** and **lvgl**.

In the sketch include the libraries like this:

```arduino
#include "Arduino_H7_Video.h"
#include "lvgl.h"

#include "Arduino_GigaDisplayTouch.h"
```

## General Set Up

### Display Shield Configuration

We then will also need to define the screen we are using, do this by adding this line of code after the library inclusions. This function will use the **Arduino_H7_Video** library:

```arduino
Arduino_H7_Video          Display(800, 480, GigaDisplayShield);
```` 

And if you want to use touch with your application call the following to use the **Arduino_GigaDisplayTouch** library:

```arduino
Arduino_GigaDisplayTouch  TouchDetector;
```

Then we have to start these functions by putting these lines in the `setup()` function:

```arduino
Display.begin();
TouchDetector.begin();
```

### LVGL Screen Configuration

When creating elements, information about the screen and placement needs to be provided. Lets create a pointer variable that can be used whenever the screenspace needs to be used. The pointer variable will be named `screen` and to use the current screen for the pointer use `lv_scr_act()`.

```arduino
  lv_obj_t * screen = lv_obj_create(lv_scr_act());
```

The size of the screen space needs to be set for the pointer that is declared. The size can be set to anything within the displays size parameters. To make it easy we can use the entire size:

```arduino
  lv_obj_set_size(screen, Display.width(), Display.height());
```

### Creating a Grid Layout

Creating a grid that you can then fill with elements will consist of a defined column and row. This `col_dsc[] = {370, 370, LV_GRID_TEMPLATE_LAST};` will create two columns with 370 px width. To add more columns simply add more values, like so `col_dsc[] = {100, 100, 100, 100, LV_GRID_TEMPLATE_LAST};`, this will create four columns with 100 px width. The same logic is applied to the row definition.

```arduino
  static lv_coord_t col_dsc[] = {370, 370, LV_GRID_TEMPLATE_LAST};
  static lv_coord_t row_dsc[] = {215, 215, LV_GRID_TEMPLATE_LAST};
```

Then like before a pointer for the screenspace needs to be created. Here it will be called `grid`. 

```arduino
  lv_obj_t * grid = lv_obj_create(lv_scr_act());
```

To set the grid description that we defined before use:

```arduino
  lv_obj_set_grid_dsc_array(grid, col_dsc, row_dsc);
```

Now that the columns and rows have been defined the overall screen needs to be taken into account. This is achieved by using `lv_obj_set_size(grid, Display.width(), Display.height())`, to make it easy we will allow the `grid` to use the entire screen. 

```arduino
  lv_obj_set_size(grid, Display.width(), Display.height());
```

Then if we want to center the grid on the screen, simply use:

```arduino
  lv_obj_center(grid);
```

### Update Loop

Include this in the loop of your sketch to make sure the LVGL engine is running and updating the screen.

```arduino
void loop() { 
  lv_timer_handler();
}
```

## Visual Elements

### Image

To display an image on the screen we first need to define what that image that should be. Take the desired image, convert it into the correct format and place the image in the same folder as the sketch. Now use `LV_IMG_DECLARE(filename);`. For example the image we use will be named `img_arduinologo`.

```arduino
  LV_IMG_DECLARE(img_arduinologo);
```

`obj` will be a pointer that will be used to hold the information about the screenspace information for the image. The `img1` pointer will be used for the elements of the image itself.

```arduino
  lv_obj_t * obj;
  lv_obj_t * img1;
```

Then create the image object with `obj` as a parent. Then we can link the image and image pointer together.

```arduino
  img1 = lv_img_create(obj);
  lv_img_set_src(img1, &img_arduinologo);
```

To make sure we see the image use the align function to make it centered. Then at last set the size of image with `lv_obj_set_size(img1, WIDTH, HEIGHT)`.

```arduino
  lv_obj_align(img1, LV_ALIGN_CENTER, 0, 0);
  lv_obj_set_size(img1, 200, 150);
```

![An image rendered on the display shield with LVGL](assets/image.svg)

## Functional Elements

### Checkbox

`obj` will be a pointer that will be used to hold the information about the screenspace information for the checkbox. The `checkbox` pointer will be used for the elements in the checkbox itself.

```arduino
  lv_obj_t * obj;
  lv_obj_t * checkbox;
```

Assign the screenspace info to `obj`, that was detailed in the [Screen Configuration](#lvgl-screen-configuration) section. To create the checkbox object use `lv_checkbox_create(obj)` and assign it to a suitable variable, here we use the `checkbox` pointer. Next set the text that will appear next to the checkbox by using `lv_checkbox_set_text(checkbox, "Example");`, here `Example` will be printed next to the checkbox.

```arduino
  obj = lv_obj_create(screen);
  checkbox = lv_checkbox_create(obj);
  lv_checkbox_set_text(checkbox, "Example");
```

The startup state of the checkbox can be set with `lv_obj_add_state()`. Where the object and state has to be specified:

```arduino
  lv_obj_add_state(checkbox, LV_STATE_CHECKED);
```

![Checkboxes rendered on the display shield with LVGL](assets/checkboxes.svg)

### Radio Button

A radio button is created in the same way as a checkbox, but with some additional calls to change the style of the element. Adding these two style elements will allow for them to be added to the checkbox options.

```arduino
  static lv_style_t style_radio;
  static lv_style_t style_radio_chk;
```

Now initialize the style variable that was set in the previous step:

```arduino
  lv_style_init(&style_radio);
```

The size of the radio button is set with `lv_style_set_radius`. To make the radio button checkable use `lv_style_init(&style_radio_chk);`. And the color or background of the filled radio check can be set with `lv_style_set_bg_img_src`.

```arduino
  lv_style_set_radius(&style_radio, LV_RADIUS_CIRCLE);
  lv_style_init(&style_radio_chk);
  lv_style_set_bg_img_src(&style_radio_chk, NULL);
```

![Radio buttons rendered on the display shield with LVGL](assets/radio-buttons.svg)

### Slider

`obj` will be a pointer that will be used to hold the information about the screenspace information for the slider. The `slider` pointer will be used for the elements of the slider itself. The `label` pointer will be used for the text that will attached to the slider.

```arduino
  lv_obj_t * obj;
  lv_obj_t * slider;
  lv_obj_t * label;
```

Now the slider can be created with:

```arduino
  slider = lv_slider_create(obj);
```

Now the value of the slider needs to be defined, here the max value of the slider will be `75` and the animation will be default set as off as it is only needed when it is interacted with.

```arduino
  lv_slider_set_value(slider, 75, LV_ANIM_OFF);
```

If you want a label by your slider it can be created like you would create any other label. Using `lv_obj_align_to` allows for the label to be attached to the slider element. Changing the `LV_ALIGN_OUT_BOTTOM_MID` to determine where the text will be relative to the slider. You can find all the different options for alignment [here.](https://docs.lvgl.io/master/widgets/obj.html#coordinates)

```arduino
  label = lv_label_create(obj);
  lv_label_set_text(label, "Drag me!");
  lv_obj_align_to(label, slider, LV_ALIGN_OUT_BOTTOM_MID, 0, 10);
```

![Slider rendered on the display shield with LVGL](assets/slider.svg)

### Bar

To make a bar, for example a loading bar, we need to include some animation. Lets first set up the slider itself and then move on to the animation.

`obj` will be a pointer that will be used to hold the information about the screenspace information for the bar. The `bar` pointer will be used for the elements of the bar itself.

```arduino
  lv_obj_t * obj;
  lv_obj_t * bar;
```

Now the bar can be created with:

```arduino
  bar = lv_bar_create(obj);
```

Set the desired size of the bar with `lv_obj_set_size`. The value of the bar needs to be defined, here the max value of the bar will be `70` and the animation will be default set as off.

```arduino
  lv_obj_set_size(bar, 200, 20);
  lv_bar_set_value(bar, 70, LV_ANIM_OFF);
```

Now for the animation. First create the slider variable and initialize it:

```arduino
  lv_anim_t animation;
  lv_anim_init(&animation);
```

The animation time needs to be defined. It can be set with `lv_anim_set_time` which sets the duration of the animation and `lv_anim_set_playback_time` which makes the animation play back to when the forward direction is ready. The animation variable and the time in milliseconds has to be defined.

```arduino
  lv_anim_set_time(&animation, 3000);
  lv_anim_set_playback_time(&animation, 3000);
```

To connect the animation to the bar use:

```arduino
  lv_anim_set_var(&animation, bar);
```

The start and end values of the animation has to be set, here they are `0` and `100` respectively.

```arduino
  lv_anim_set_values(&animation, 0, 100);
```

How many times the animation will repeat can also be set, with this code the animation will repeat forever. And then at last we can create the animation with `lv_anim_start`.

```arduino
  lv_anim_set_repeat_count(&animation, LV_ANIM_REPEAT_INFINITE);
  lv_anim_start(&animation);
```

When the bar animates we can set it so that a separate callback function will be called. Here that function will be named `set_bar_val`.

```arduino
  lv_anim_set_exec_cb(&animation, set_bar_val);
```

In this separate callback function the bar value will be reset and the animation will be turned on again.

```arduino
static void set_bar_val(void * bar, int32_t val) {
  lv_bar_set_value((lv_obj_t *)bar, val, LV_ANIM_ON);
}
```

![A bar rendered on the display shield with LVGL](assets/bar.gif)

### Button

A button will need two parts, the design of the button itself and the callback event function which determines what happens when the button is pressed. Lets start with designing the button.


`obj` will be a pointer that will be used to hold the information about the screenspace information for the button. The `button` pointer will be used for the elements in the button itself. The `label` pointer will be used for the text that will be put on the button.

```arduino
  lv_obj_t * obj;
  lv_obj_t * button;
  lv_obj_t * label;
```

Now the button can be created with:

```arduino
  button = lv_btn_create(obj);
```

Set the size of the button with `lv_obj_set_size(btn, WIDTH, HEIGHT)`. For example:

```arduino
  lv_obj_set_size(btn, 100, 40);
```

Lets make the label on the button a child of the button by using `label = lv_label_create(button)`. Then the label can be set to whatever text it needs to be and center the text on top of the button so that it looks correct. The button will now say `Click me!` at the center of it.

```arduino
  label = lv_label_create(button);
  lv_label_set_text(label, "Click me!");
  lv_obj_center(label);
```

When the button is clicked we need to assign it a function to execute, lets call this function `button_event_callback`. Assign it to the correct button and set it to be executed when the button is clicked with `LV_EVENT_CLICKED`.

```arduino
  lv_obj_add_event_cb(button, button_event_callback, LV_EVENT_CLICKED, NULL);
```

Now lets create the callback function that will be called when the button is clicked. By creating pointers that will point to the original elements we can change them easily in our function. This function will make it so that when the button is clicked the label text on the button will be changed to `Clicked!`.


```arduino
static void button_event_callback(lv_event_t * e) {
  lv_obj_t * button = lv_event_get_target(e);
  lv_obj_t * label = lv_obj_get_child(button, 0);
  lv_label_set_text_fmt(label, "Clicked!");
}
```

![A button rendered on the display shield with LVGL](assets/button.svg)
![Button when it has been clicked](assets/button-clicked.svg)

## Conclusion

This guide went through the building blocks of the different components that can be implemented with lvgl. To see these examples in a full running example sketch go to **File->Examples->Arduino_H7_Video->LVGLDemo**.
![Example in the IDE](assets/example-in-ide.svg)
This example sketch will show the different components in a 2x2 grid.

## Next Step
If you are interested in finding out how to use LVGL with the on-board IMU check out our [Orientation tutorial](). There are more features of the display shield to discover, for example using the camera connector. For more information on that have a look at our [Camera tutorial](). LVGL has a lot of customizability, if you are interested in playing around more with this, you can find many different examples on the official website for [LVGL](https://docs.lvgl.io/master/examples.html). These can easily be put in a sketch for the display shield just remember to use the display-specific configuration that was shown at the [start of this tutorial](#display-shield-configuration).