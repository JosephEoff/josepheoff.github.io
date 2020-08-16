---
layout: post
title: "Learning about GNU Radio - A GNU Radio Companion flowgraph to measure impedance"
categories: [blog]
mathjax: false
image: /assets/2020-08-16-impedancetester/plotter.png
---
A first (successful) experiment with GNU-Radio.

As with many of the things that end up on this blog, this project started from a combination of things - including the ever popular "somebody asked a question the [Electrical Engineering Stack Exchange.](https://electronics.stackexchange.com/)"  Actually, it wasn't a particular question but rather a question that comes up often:  "What's the impedance of this random speaker I found?"

You can't really measure the resistance of a speaker and get a reasonable answer - it is only by accident that the speaker impedance and the speaker resistance will be anywhere close to the same.

The other thing that went into this project was a passing reference I made to [GNU Radio](https://www.gnuradio.org/) while writing the [post on generating extreme low frequency signal.](elf)  That reminded me that I'd never actually done anything with GNU Radio at all.  I'd looked at it before, but never really put anything useful together with it.

I've long wanted to put together a simple impedance tester to give to folks who ask how to measure the impedance of a speaker.  I have at various times actually assembled such a program with [Pure Data,](https://puredata.info/) but I never got it to a state where it was useful.  Implementing the functionality is trivial in Pure Data - maybe a half an hour to assemble the whole thing.  It always fails on making the display nice and useful, though.  The available display elements (arrays) are rather primitive in Pure Data - there are no cursors to make measurements, and there aren't even any decent ways to draw a grid with a scale on an array.

I decided I'd take GNU Radio for a spin, and implement an impedance tester with it.  I've long known that it has [QT](https://www.qt.io/) based GUI elements, and that it can read and write analog signals through a PC soundcard.  That's enough of a basis to work from.  At the very least I'd learn something, and best case I'd come up with a useful program I could give to other hobbyists who need a way to measure impedances.

Good news first:

GNU Radio and its QT GUI elements (together with a bit of Python code) let me assemble a [useful impedance tester](https://github.com/JosephEoff/Simple-impedance-tester) that I feel is stable enough and useful enough to let loose in the wild.

I'll explain the software and the hardware in a later post.  Right now, I'm just going to show you what it looks like and give you a schematic that you can use to try it out.

You'll need a PC with a soundcard that has "Line In" and "Line Out" jacks.  You'll need [GNU Radio](https://www.gnuradio.org/), [Python 2](https://www.python.org/downloads/), and [SciPy](https://www.scipy.org/).

You'll need this circuit:

|Test circuit|
|------------|
|![Impedance tester circuit](/assets/2020-08-16-impedancetester/testcircuit.png)|

Finally, you will need the [impedance tester](https://github.com/JosephEoff/Simple-impedance-tester) project that I've posted on GitHub.

The software looks like this when running:

|Impedance tester|
|----------------|
|![Impedance tester circuit](/assets/2020-08-16-impedancetester/plotter.png)|

This is the plot the impedance of a nominal 8 ohm car stereo speaker.  This speaker has a woofer, a mid-range, and a tweeter in one housing with a 3-way crossover network.

|Car speaker plot|
|![Car speaker impedance](/assets/2020-08-16-impedancetester/carspeaker.png)|

All lumpy and uneven - and only nominally 8 ohms.  The impedance doesn't actually hit 8 ohms anywhere.

For comparison, I plotted the impedance of a 20 ohm resistor:

|20 ohm resistor plot|
|![20 ohm resistor plot](/assets/2020-08-16-impedancetester/20-ohm-resistor.png)|

Flat from end to end, except where the soundcard limitations kick in (low frequencies and high frequencies.)

As I said, I'll explain it all in a later post.  I've noticed a tendency for my last posts to be great long monsters, and I'd like to shorten them a bit.  When I write the long monsters all in one go, things get all mashed together and shortened.

I'll write separate posts later on how the software works, how to hookup the hardware, and how to install the software.

