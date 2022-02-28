---
layout: post
title: "A sewing machine motor speed control - A MOSFET source follower as a motor speed control"
categories: [blog]
mathjax: true
description: "Some notes on how not to build a motor speed control.  A MOSFET source follower as a motor speed control."
image: /assets/2022-02-28-motorcontrol2/1.jpg
---
Better, but far from good.

<sub>[A sewing machine motor speed control - Table of Contents](motorcontrol-toc)</sub>

The simple motor controller I looked at the last time around was really just an electronic equivalent to the mechanically switched resistors commonly found in sewing machine foot pedals.  It is a "stupid" circuit in that it doesn't make use of the possibilities granted by the transistor used in it.

The biggest drawback of that type of simple control is that it robs the motor of power.  Any load at all on the motor will cause it to slow down.

If you rearrange the parts slightly, you get a much improved control.

|Somewhat better motor speed control|
|-----------------------------------|
|![Somewhat better motor speed control](/assets/2022-02-28-motorcontrol2/1.jpg)|

That uses the same parts, but rather than using the MOSFET as a simple variable resistor, I've wired it as a [source follower or a common drain circuit.](https://en.wikipedia.org/wiki/Common_drain)

The nice thing about the source follower is that the voltage at the source follows the voltage on the gate.  The MOSFET actively works to maintain the source voltage at (or at least, close to) the gate voltage.

For the motor control, this means that the MOSFET will attempt to maintain the set voltage by increasing the motor current as needed.  When the mechanical load on the motor causes the motor to slow down, the MOSFET jacks up the current to make the motor run faster.

The simple circuit I demonstrated in the last post doesn't do that:

<div style="padding:80% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/682991196?h=a92d711703&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Current for the simple motorcontrol"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

As you can see, the current doesn't change to match the changing load.

The source follower circuit does a much better job:

<div style="padding:79.88% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/682991431?h=67e287f1ca&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Current for the source follower motor control"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

The source follower runs up the current when I load the motor - it is trying to maintain the motor speed.

Despite being better, the source follower is not good enough:

1. There is a maximum gate to source voltage allowed by the construction of the MOSFET - using it with the much higher voltage of the sewing machine motor would be difficult (at least, for me it would be.)
2. There is always a couple of volts of difference between the gate and the source.  This is due to the way that FETs work. The gap eats into the control range.  For the low voltage circuit I'm playing with, that means that the motor will never get close to its full speed when controlled by the source follower.
3. The FET is still being used as a variable resistor.  It gets **hot** even with the low voltage and current I'm using in my experiments.

Any of those three points would be a problem with my sewing machine control.  All together they are a "show stopper."  I won't be making a sewing machine control with a source follower, even though it does illustrate how to get feedback to maintain a set speed.

Fixing points 1. and 2. means using the MOSFET on the low side - that is, with the source connected to ground and the gate voltage limited to something below the maximum V_GS for whatever MOSFET I might use.

Fixing point 3. means a radical change.  I'll go into it in my next post.

<sub>[A sewing machine motor speed control - Table of Contents](motorcontrol-toc)</sub>
