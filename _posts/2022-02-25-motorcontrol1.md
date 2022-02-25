---
layout: post
title: "A sewing machine motor speed control - Basic ideas on how not to make a motor speed control"
categories: [blog]
mathjax: false
description: "Some notes on how not to build a motor speed control.  Starting with a simple, naive resistance controller."
image: /assets/2022-02-25-motorcontrol1/1.jpg
---
Simple but not really useful.

<sub>[A sewing machine motor speed control - Table of Contents](motorcontrol-toc)</sub>

I'm going to start this series with a look at the simplest, most naive motor control there is.

The simplest conceptual motor speed controller is a variable resistor in series between the motor and the power supply.  More resistance means less current means the motor turns slower.

Such a controller would look like this:

|Simple, naive motor control|
|---------------------------|
|![Simple, naive motor control](/assets/2022-02-25-motorcontrol1/2.png)|

Nothing to it.  A power supply, a variable resistor, a motor.

That's all a typical sewing machine controller is.

|Sewing machine motor with control|
|---------------------------------|
|![Sewing machine motor with control](/assets/2022-02-25-motorcontrol1/3.jpg)|

You've got a power supply (the mains plug,) a motor (screwed to the wooden upright,) and a (somewhat) variable resistor hiding in the foot pedal.

The foot pedal actually contains some big resistors and some switches arranged so that pressing down on the pedal successivelly shorts more resistors to allow more current to reach the motor.  Since it uses just a few resistors you don't have really fine control - you've got maybe five resistance values.

There's several downsides to the controllers used on sewing machines, and only one upside.

The one advantage is that the controller is simple.  Not so much a big deal in this day and age, but back in the days when sewing machines were first electrified there wasn't really any good way to control motor speed.  Electronics meant vacuum tubes, which were expensive and sensitive to vibration.  No way was anybody going to put any kind of complicated circuitry in something that was going to be literally kicked around.

There are several downsides:
1. Such controllers are wasteful.
2. Such controllers have only a few distinct control steps.
3. They don't maintain a specific speed.

A resistor always converts current to heat.  To slow down the motor, you put more resistance in series with it.  The power the motor doesn't use is wasted as heat.

The few available control steps don't allow for fine control of the motor speed.  You step on the pedal, and the motor turns.  It speeds up, goes too fast, and then you back off to slow down - and now it's too slow, so step on it again and it's too fast.

Worst of all is that the speed control isn't a speed control.  It is actually a power control.  It works like the accelerator in a car - mashing down on the pedal feeds more power to the motor.  The speed the motor turns at is determined by the power and the load.  For the same power, the motor turns faster when it has a light load than when it has a heavy load.

For a sewing machine, that last means that the machine slows down when you cross a thicker seam and speeds up when you get back to a lighter section.

In electronics terms, a sewing machine motor control is open loop.  It changes its output according to the control input (the pedal,) but it doesn't monitor the motor to see if it matches the desired speed.

I put together a simple circuit to illustrate the load control problem.  It uses an IRF540 N-channel MOSFET to control the speed of a small motor.

|Test circuit|
|------------|
|![Test circuit](/assets/2022-02-25-motorcontrol1/1.jpg)|

I don't have a rheostat (variable resistor) that could handle the motor power requirements without burning out, so I made that circuit to do the same job.

The potentiometer controls the gate voltage on the MOSFET.  Higher voltage on the gate means more current through the drain - the MOSFET acts like a voltage controlled resistor.  Turning the potentiometer varies the gate voltage, making the motor run faster or slower.  The MOSFET can handle a fairly large amount of power - at least in comparison with what my dinky little motor draws.

<div style="padding:80% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/682059971?h=f14194ffa4&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="simplemotorcontrol"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

You can see how putting a load on the motor makes it slow down and how removing the load (letting go of the shaft) lets the motor speed up.

Sewing machines do the same thing when using the typical simple foot pedal controls.

I'll take a look at a (slightly) improved version of this controller the next time around.

<sub>[A sewing machine motor speed control - Table of Contents](motorcontrol-toc)</sub>
