---
title: 'Embed & Share Sketches'
description: 'Learn about sharing your sketches and different methods to embed your sketches in a website.'
author: 'Karl Söderby, Hannes Siebeneicher'
---

The Cloud Editor is a great tool for creating and uploading programs while also collecting all of your sketches in one place. Another great feature is embedding them as iframes, such as articles, blogposts or journals.

Embedding an iframe is easy. Simply copy and paste the link from your sketch in the Cloud Editor. But we can also do a series of modifications to that iframe, and in this tutorial we will take a look at how to do that.

## Let's start

First of all, we need to navigate to the [Cloud Editor](https://app.arduino.cc/sketches). If we do not have an account, we can register one with just a few simple steps.

Then, we need to have a code. In this tutorial, we are just going to use the good old **blink** example. When we have our sketch ready, click on the **share** button next to the serial monitor tool. This will open up a new window, that will have two fields: **link** and **embed**. Copy the embed field.

![Embed in HTML code](./assets/Embed_1.png)


It should look something like this:

```markup
<iframe src="https://app.arduino.cc/sketches/examples?eid=01.Basics%2FBlink&view-mode=embed" style="height:510px;width:100%;margin:10px 0" frameborder="0"></iframe>
```

This iframe can now simply be embedded in a HTML page, and it will look like this:

<iframe src="https://app.arduino.cc/sketches/examples?eid=01.Basics%2FBlink&view-mode=embed" style="height:510px;width:100%;margin:10px 0" frameborder="0"></iframe>

But there are many ways we can modify the iframe to look different. So let's take a look the available modifications we can make!

## Creating a snippet

First up is the easiest: making a simple snippet. This removes the other information, such as sketch name and author, and simply presents a good looking snippet!

To do this, we need to change `view-mode=` from `embed` to `snippet` at the end of the URL:

```
&view-mode=snippet
```
The result is the following:

<iframe src="https://app.arduino.cc/sketches/examples?eid=01.Basics%2FBlink&view-mode=snippet" style="height:510px;width:100%;margin:10px 0" frameborder="0"></iframe>

And the full URL should look like this:

```markup
<iframe src="https://app.arduino.cc/sketches/examples?eid=01.Basics%2FBlink&view-mode=snippet" style="height:510px;width:100%;margin:10px 0" frameborder="0"></iframe>
```

## Highlighting specific lines

Next is the highlighting feature. To use this, simply add the following lines to the end of your URL:

```
&highlight=L6,7
```

The result is that line 6 and 7 are highlighted:

<iframe src="https://app.arduino.cc/sketches/examples?eid=01.Basics%2FBlink&view-mode=snippet&highlight=L6,7" style="height:510px;width:100%;margin:10px 0" frameborder="0"></iframe>

And the full URL should look like this:

```markup
<iframe src="https://app.arduino.cc/sketches/examples?eid=01.Basics%2FBlink&view-mode=snippet&highlight=L6,7" style="height:510px;width:100%;margin:10px 0" frameborder="0"></iframe>
```

You can highlight as many lines as you want, and it is easily configurable. For example, if we want to highlight line 4 and 6-9, we simply need to add the following to the URL:

```
&highlight=L4,L6-L9 
```

## Scope

It's also possible to only show specific lines by adding the `scope` parameter, like this:

```markup
&scope=L24-L37
```

The result is that only lines 24 to 37 are shown.

<iframe src="https://app.arduino.cc/sketches/examples?eid=01.Basics%2FBlink&view-mode=snippet&scope=L24-L37" style="height:510px;width:100%;margin:10px 0" frameborder="0"></iframe>

The full URL should look like this:
```markup
<iframe src="https://app.arduino.cc/sketches/examples?eid=01.Basics%2FBlink&view-mode=snippet&scope=24-28" style="height:510px;width:100%;margin:10px 0" frameborder="0"></iframe>
```

## Hide Numbers

To hide the line numbers in the embedded snippet, add the `&hide-numbers` parameter, like this:

```markup
&hide-numbers
```

The full URL should look like this:
```markup
<iframe src="https://app.arduino.cc/sketches/examples?eid=01.Basics%2FBlink&view-mode=snippet&scope=L3-L30&hide-numbers" style="height:510px;width:100%;margin:10px 0" frameborder="0"></iframe>
```

## Manually changing the size of your widget

If we want to change the size of the widget, we just need to modify the dimensions of the iframe.

The following dimensions are default:

```markup
style="height:510px;width:100%;margin:10px 0"
```

But we can change them up a bit:

```
style="height:200px;width:50%;margin:10px 0"
```

Which will look like this:

<iframe src="https://app.arduino.cc/sketches/examples?eid=01.Basics%2FBlink&view-mode=snippet" style="height:200px;width:50%;margin:10px 0" frameborder="0"></iframe>

## Automatically re-sizing your sketches

We can also choose to automatically re-size our iframes. This is simply done by first including this script in your HTML file:

```markup
<script src="https://content.arduino.cc/assets/arduinoSketchIframeResizer.js"></script>
```

And then using the class `arduino-sketch-iframe` in your `HTML element`.

## Share your Code

If you want to share you're code with others can you do so by following the same steps as above, but instead of clicking on "Embed in HTML code:" you click on "Link to share:"

![Share Code](./assets/Share_1.png)

This link will direct others to a preview of our code where they can copy it or directly add it to their sketchbook.

***Note: If you want to learn how to keep sensitive data in your code safe, read [Store Sensitive Data in Sketches](/arduino-cloud/cloud-editor/share-your-sketches/).***

### More tutorials

You can find more tutorials in the [Arduino Cloud documentation page](/arduino-cloud).