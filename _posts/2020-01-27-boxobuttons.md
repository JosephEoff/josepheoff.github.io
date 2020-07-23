---
layout: post
title: "The box o' buttons"
categories: [blog]
mathjax: false
image: /assets/2020-01-27-buttons/buttonbox.jpg
---
{% include lib/mathjax.html %}
Ten, because two is a stupid number.

I've got some plans in mind for a new program that is intended to be used when I've got my hands full and my eyes busy.  I'll post about it when it's done, but for now I'm just going to show you how I intend to operate a program without using my hands or looking at the monitor.

Meet the "Box o' Buttons"

|Box o' Buttons|
|--------------|
|![Box o' Buttons](/assets/2020-01-27-buttons/buttonbox.jpg)|

That's a pair of big push buttons in a wooden, wedge shaped box that fits comfortably under my feet.

There's an Arduino Nano in there that monitors the state of the buttons using a couple of digital IO pins.  When a button is pressed or released, the Nano sends a short message to the PC indicating which pin changed, and its current state.

The program I'm going to write will keep an eye on the serial port, and react according to the button presses.

I didn't post drawings of the box because I figure anybody that wants to build something like this will have to make one to fit their own feet - and their own buttons.  

My "buttons" are actually momentary contact light switches.  They are normally used to trigger a relay in the house breaker box to turn a light on or off from multiple locations.  If you have two places you need to operate a light from, you use a couple of SPDT switches.  If you have a bunch of places, you use a bunch of pushbuttons and a toggle relay in the breaker box.

The nice thing about those push buttons is that they are cheap and robust.  I couldn't find anything trustworthy online that's as cheap as this pair of momentary contact switches from the local hardware store.

The wooden parts didn't cost me anything - I've got loads of scraps out in the garage.

The only mildly interesting part is the software in the Nano.

That [software](https://github.com/JosephEoff/BoxOButtons) is a little bit of over overkill for just two buttons.  The "Box o' Buttons" software actually reads and debounces 10 digital IO pins simultaneously.  It was just as easy to write the program to read all the available IOs as it would have been to make it only read two digital IOs.  The logic is plain enough and easy to do.

I made the software read all 10 available digital IOs on my Nano because 2 is a stupid number.  If you do one of something in software, then you kind of have to implement it that one time.  If you have to do something more than once, the temptation is to implement it for each case.  If you are only dealing with a couple of somethings, that's fine.  My Nano has 10 pins available, and even though I only need two in this project, I went ahead and implemented all 10.  The program would be just about as long if I'd only done two, and a lot less easy to read.  It's just a loop and a couple of arrays.  Rather than do the same thing twice, I just went ahead made do it for all 10 with a simple loop.

The software also debounces all 10 inputs.  I really expected the buttons to be rather crappy and have a lot of contact bounce.  They do bounce quite a bit, but it's usually over in less than a couple of milliseconds.  That let me reduce the debounce time from the original 200 milliseconds to just 20 milliseconds (fast enough, but still accounts for outliers.)

This is what the switches really produce:

|Bounce - transition from high to low|
|--------------|
|![transition from high to low](/assets/2020-01-27-buttons/transition_down.png)|

|Bounce - transition from low to high|
|--------------|
|![transition from low to high](/assets/2020-01-27-buttons/transition_up.png)|

The low to high transistion surprised me.  I expected the bounce to be about the same in both directions.  The low to high transistion  takes less than 100 microseconds.  It was hard to catch it - at first I thought I was doing something wrong.  Even after I convinced myself that it really did switch that cleanly, it took a while to catch a transistion that actually had some bounce in it.

The high to low transition takes around 1.5 milliseconds, and has lots of bounce in it.  That was fairly easy to capture.

In either case, the Nano can handle it and send clean signals to the PC.

Need to read a bunch of hardware buttons from your PC?  Well then, whip up your own ["Box o' Buttons."](https://github.com/JosephEoff/BoxOButtons)


