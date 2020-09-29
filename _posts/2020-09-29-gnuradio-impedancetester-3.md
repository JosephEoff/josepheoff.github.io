---
layout: post
title: "Learning about GNU Radio - More functions for the impedance tester"
categories: [blog]
mathjax: true
image: /assets/2020-09-29-gnuradio-impedancetester-3/inductor.png
---
{% include lib/mathjax.html %}
More math and a little more software.

<sub>[Learning about GNU Radio - Table of Contents](1gnuradio-toc)</sub> 

The impedance tester can measure impedances for more than just speakers.  It doesn't really care what you connect to it.  It'll happily measure the impedance of a resistor - or of an inductor or capacitor.

If you've been following my blog for a while, you'll know that once you have the impedance of an [inductor](inductor) or a capacitor and the frequency you measured the impedance at, then you can calculate the inductance or capacitance of the part.

Most folks learn it the other way around - from the inductance and the frequency you can calculate the impedance.

It's just math, though, and the equations work in either direction.

The equations for the impedances of capacitors and inductors can be found on the [Wikipedia Electrical Reactance](https://en.wikipedia.org/wiki/Electrical_reactance) page:

|   |To impedance|From impedance|
|---|------------|--------------|
|Capacitance|\$Z = \frac {1}{2 \pi fC}\$|\$C = \frac {1}{2 \pi fZ}\$|
|-----------|---------------------------|---------------------------|
|Inductance|\$Z = 2 \pi fL\$| \$L = \frac {Z}{2 \pi f}\$|

Well, the impedance tester has impedances, and it has frequencies.  All it needs is a little math, and it can become an inductance and capacitance meter.

I implemented another Python block in the impedance tester to do the math, and added a selector to the GUI to choose which function to use.

Tada!  Instant LCR meter!  More or less.

Here's what it looks like:

|Impedance tester impersonating an inductance meter|
|--------------------------------------------------|
|![impersonating an inductance meter](/assets/2020-09-29-gnuradio-impedancetester-3/inductor.png)|

That's the inductance function testing the inductor I built for the [simple voltage booster.](voltagebooster)

The value agrees with the [measurement](inductor) I made back then - both come out to about 31 microhenries at 10kHz.  The impedance tester tells a more telling story, though.

That inductor is far away from being an ideal inductor.  At low frequencies, it has far more impedance than it ought to.  It has so much extra impedance at low frequencies that it acts like a much larger inductor.  As the frequency goes up, it behaves more like an ideal inductor.  Above about 20kHz, the limits of the sound card kick in and the inductance appears to rise again - that's just the hardware hitting its limits, though.

This is what it looks like with a capacitor connected:

|Impedance tester pretending to be a capacitance meter|
|--------------------------------------------------|
|![pretending to be a capacitance meter](/assets/2020-09-29-gnuradio-impedancetester-3/capacitor.png)|

That's a 0.04 µF capacitor (40nF.)  It's spot on at higher frequencies, but drops some at lower frequencies.

I've always known that inductors and capacitors were far from ideal, but I had no idea they were far enough from ideal to detect with relatively crude methods.

That's about it for today.  An LCR meter for a the price of few pieces of wire.

------------------

Don't toss your real LCR meter.

The inductance and capacitance functions of the simple impedance tester are better than nothing, but they cannot replace a real, calibrated meter.

The images above involved some twiddling of the output levels to get a clean trace without distortion.  When the output (or input) of the sound card begins to clip from a signal level that is too high, or when the input level gets too low because of attenuation in the part you are testing, then you get wonky curves that can lead you astray.  A measurement involves selecting the series resistor to approximate the impedance of the part you are testing, and then adjusting the volume of the output and the amplification of the input to find settings that give reliable values.  If you get screwy curves or strange values (negative impedances, anyone?) then it's more likely that you have the sound card levels wrong or have picked a poorly matching resistor value than that your part is really **that** bad.

It's fun to fiddle with, and it's better than nothing if you don't own a good meter - just don't trust it with anything critical.

I'll write up a clean How-To on the [simple impedance tester GuitHub page,](https://github.com/JosephEoff/Simple-impedance-tester) but that's a task for another day.

<sub>[Learning about GNU Radio - Table of Contents](1gnuradio-toc)</sub> 
