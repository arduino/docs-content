---
title: Guide for using LVGL with the Giga Display Shield
description: 'Learn how to use LVGL with the GIGA display shield'
author: Benjamin Dannegård
tags: [Display, LVGL]
---


## Hardware & Software Needed

- [GIGA R1 WiFi](/hardware/giga-r1).
- [GIGA Display Shield]()
- [Arduino IDE](https://www.arduino.cc/en/software)
- [Arduino_H7_Video]() library.
- [Arduino_GigaDisplayTouch]() library.

## Downloading the Library and Core

The Giga core includes a library that will help us handle the display so make sure you have the latest version of the core. This library is called **Arduino_H7_Video**.

For touch features we will be using the **Arduino_GigaDisplayTouch** library. The LVGL library is called **lvgl** which also needs to be downloaded. Go to the library manager in the Arduino IDE and make sure these library is installed.

In the sketch include the libraries like this:

```arduino
#include "Arduino_H7_Video.h"
#include "lvgl.h"

#include "Arduino_GigaDisplayTouch.h"
```

### Initializing the libraries

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

## General set up

### Screen configuration

When creating elements, information about the screen and placement needs to be provided. Lets create a pointer variable that can be used whenever the screenspace needs to be used. The pointer variable will be named `screen` and to use the current screen for the pointer use `lv_scr_act()`.

```arduino
  lv_obj_t * screen = lv_obj_create(lv_scr_act());
```

The size of the screen space needs to be set for the pointer that is declared. The size can be set to anything within the displays size paramaters. To make it easy we can use the entire size:

```arduino
  lv_obj_set_size(screen, Display.width(), Display.height());
```

### Creating a grid layout

### Update loop

### Image

```arduino
  LV_IMG_DECLARE(img_arduinologo);
  lv_obj_t * img1 = lv_img_create(obj);
  lv_img_set_src(img1, &img_arduinologo);
  lv_obj_align(img1, LV_ALIGN_CENTER, 0, 0);
  lv_obj_set_size(img1, 200, 150);
```

### Checkbox

`obj` will be a pointer that will be used to hold the information about the screenspace information for the checkbox. The `checkbox` pointer will be used for the elements in the checkbox itself.

```arduino
  lv_obj_t * obj;
  lv_obj_t * checkbox;
```

Assign the screenspace info to `obj`, that was detailed in the #Screen configuration section. To create the checkbox object use `lv_checkbox_create(obj)` and assign it to a suitable variable, here we use the `checkbox` pointer. Next set the text that will appear next to the checkbox by using `lv_checkbox_set_text(checkbox, "Example");`, here `Example` will be printed next to the checkbox.

```arduino
  obj = lv_obj_create(screen);
  checkbox = lv_checkbox_create(obj);
  lv_checkbox_set_text(checkbox, "Example");
```

The startup state of the checkbox can be set with `lv_obj_add_state()`. Where the object and state has to be specified:

```arduino
  lv_obj_add_state(checkbox, LV_STATE_CHECKED);
```


### Radio button

```arduino
  static lv_style_t style_radio;
  static lv_style_t style_radio_chk;
  lv_style_init(&style_radio);
  lv_style_set_radius(&style_radio, LV_RADIUS_CIRCLE);
  lv_style_init(&style_radio_chk);
  lv_style_set_bg_img_src(&style_radio_chk, NULL);
```

### Slider


```arduino
  lv_obj_t * slider = lv_slider_create(obj);
  lv_slider_set_value(slider, 75, LV_ANIM_OFF);
  lv_obj_center(slider);
  label = lv_label_create(obj);
  lv_label_set_text(label, "Drag me!");
  lv_obj_align_to(label, slider, LV_ALIGN_OUT_BOTTOM_MID, 0, 10);
```

### Button

A button will need two parts, the design of the button itself and the callback event function which determines what happens when the button is pressed. Lets start with designing the button.



```arduino
  lv_obj_t * btn = lv_btn_create(obj);
  lv_obj_set_size(btn, 100, 40);
  lv_obj_center(btn);
  lv_obj_add_event_cb(btn, btn_event_cb, LV_EVENT_CLICKED, NULL);

  label = lv_label_create(btn);
  lv_label_set_text(label, "Click me!");
  lv_obj_center(label);
```


```arduino
static void btn_event_callback(lv_event_t * e) {
  static uint32_t cnt = 1;
  lv_obj_t * btn = lv_event_get_target(e);
  lv_obj_t * label = lv_obj_get_child(btn, 0);
  lv_label_set_text_fmt(label, "%"LV_PRIu32, cnt);
  cnt++;
}
```

## Conclusion