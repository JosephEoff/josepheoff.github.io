---
layout: post
title: "An isolated variac for vintage radio repair"
categories: [blog]
mathjax: false
description: "A look at an isolated variac intended to be used in the repair of vintage, tube radios with with hot chassis construction."
image: /assets/2025-07-27-isolatedvariac/1.jpg
---
A little vintage safety for working with vintage equipment.

[I fixed up an old Blaupunkt Granada tube radio a few years ago.](1blaupunkt20300-toc)  It is still running strong after its latest adventure at my wife's birthday party.  I hooked up the old Granada to play music from a laptop and to be used as a speaker for announcements (it was a rather large outdoor party.)

At the party, my brother-in-law mentioned that he and his wife had bought an old tube radio and asked if I knew anyone who could help in fixing it up for use.  In actual fact, there's a young fellow who helps out at the local repair cafe who collects and restores old tube radios as a hobby.  He's been out of town for the last few weeks, though, so I offered to take a look at it.  That radio is now parked on my workbench, waiting to be cleaned, tested, adjusted and Bluetooth adapted.

When I was working on the Granada, I was very nervous what with the high voltage inside and the chances of getting zapped.  The Granada attually has an isolated transformer built in.  Many do not.  They are known as "hot chassis" radios because the metal frame inside the cabinet is at line voltage, and connected directly to the AC power line.  That kind of thing makes me nervous.

The correct solution for working on a hot chassis radio is to use [an isolated 1-to-1 transformer](https://en.wikipedia.org/wiki/Isolation_transformer) to power it.  The transformer makes it so that there's no path for current from the output side to ground.  You can't be zapped just by touching something inside the radio, and you can connect an oscilloscope or other test equipment without causing a short circuit or getting AC line voltage applied to the housing of your test equipment.

Another thing you often need while working with tube equipment is a [variac.](https://en.wikipedia.org/wiki/Autotransformer#Variable_autotransformers)  This is a transformer with a variable output voltage.  You use it to slowly apply power to an old device, allowing time for electrolytic capacitors to rebuild the insulating layer on the electrodes rather than blowing them out by applying full power straight away.

Variacs are usually autotransformers.  That is to say that there is no separate primary and secondary side.  The output is "hot," meaning that current can flow through it, through you, and to ground, shocking (and potentially killing) you along the way.  To be safe while using a variac, you also need to use an isolation transformer.

I went looking for both of those items the other day on e-Bay.  I found inexpensive variacs that I didn't like (no outlet for the power, just screw terminals for 240VAC, no thanks) and expensive isolation transformers.  I didn't much care for having to have two big, heavy devices either.

Perseverance paid off, though, when this old gadget popped up in my search:

|Variac|
|---------------|
|![Variac 1](/assets/2025-07-27-isolatedvariac/1.jpg)|
|![Variac 2](/assets/2025-07-27-isolatedvariac/2.jpg)|

At first glance, that looks like a simple variac with a couple of Euro-plug outlets on top (with an adapter in one.)  That it has outlets is already better than the other offerings.  

What made me really sit up and take notice of it, however, was this:

|Isolated variac|
|---------------|
|![Isolated variac](/assets/2025-07-27-isolatedvariac/3.jpg)|

That's a diagram of the innards of very peculiar variac.  It actually isn't a variac at all.  A variac is an autotransformer with variable output voltage.  The e-Bay advertisement had a picture of this diagram, and it is a very good thing they did.  I wouldn't have given it a second glance without it.

This thing is an isolation transformer with a variable tap on the secondary side.  It is a variable output isolation transformer.

That is exactly what I need.  One piece of equipment that does the whole job, safely.

The cherry on top is that dashed line that goes around the primary and connects to ground.  That means that the transfomer is screened to prevent capacitive leakage from the primary to the secondary. Nice.

If the screened primary was the cherry on top, the whipped cream was that it cost less than the cheap Chinese ones with the screw terminals.

Since this thing is used and intended as a safety device, I decided not to take its proper function at face value.  I don't want to find out that the isolation failed by getting myself zapped dead.

To check isolation, you need an isolation tester.  These use high voltage to measure very high resistance values, such is the insulation between two insulated conductors in a cable.

The repair cafe I help out in has one, which I borrowed for the weekend.

|Isolation tester|
|----------------|
|![Isolation tester](/assets/2025-07-27-isolatedvariac/4.jpg)|

While it's a cheap model, bought either from Amazon or Conrad Electronics, it does work.

I checked the isolation of various connections on the transformer:

|Connection|Isolation resistance|Current at 1000V|Photo|
|----------|--------------------|-----|
|Primary (line) to housing|133.5 Mohm|7.5µA|![Isolation resistance 1](/assets/2025-07-27-isolatedvariac/5.jpg)|
|Secondary (output) to housing|249 Mohm|4µA|![Isolation resistance 2](/assets/2025-07-27-isolatedvariac/6.jpg)|
|Primary to secondary|430 Mohm|2.3µA|![Isolation resistance 3](/assets/2025-07-27-isolatedvariac/7.jpg)|

That looks pretty good, considering that medical devices have an allowed maximum leakage current of 10µA.

The only part that didn't inspire confidence was the built in voltmeter.  The needle flops and wiggles considerably, making me doubt its accuracy.

The truth is that it is not accurate at all.  I did a few spot checks against my multimeter, and got some really wild results.

|Variac meter value|Multimeter value|Photo|
|------------------|----------------|-----|
|153VAC            |141VAC          |![Output voltage](/assets/2025-07-27-isolatedvariac/8.jpg)|
|200VAC            |187VAC          |![Output voltage](/assets/2025-07-27-isolatedvariac/9.jpg)|
|245VAC            |226VAC          |![Output voltage](/assets/2025-07-27-isolatedvariac/10.jpg)|

I suppose I should be thankful that it always reads too low.  If I set it for something, then I can be sure that it is below the value on the built in meter.

I'll probably default to measuring the output with my multimeter if I really need the output to be correct.

Besides the outlets and the meter, this transformer has a couple of other features:

|Features|
|--------|
|![Features 1](/assets/2025-07-27-isolatedvariac/11.jpg)|
|![Features 2](/assets/2025-07-27-isolatedvariac/12.jpg)|

The first is a lighted fuse socket.  If the fuse is blown (or removed as here,) the socket lights up to let you know that there's a problem.

The second is a switch that lets you select between maximum 240VAC (1:1 transformer ratio) or 300VAC (1:1.25 ratio.)  That's handy if you need to test how something will react to a slight over voltage.

That wraps up this look at a piece of vintage test equipment.  I'll start working on the radio itself later this week.

------

The one thing I do not know about this transformer is who made it and where it was made.  There's no manufacturer's name anywhere.  Not even a sticker that says "made in the people's republic of who knows where."  Just, nothing.  Not even the model number does me any good.  No one anywhere on Earth has ever posted anything on the internet about a B870900/C3 transformer.  Just a big old mystery, all around.


