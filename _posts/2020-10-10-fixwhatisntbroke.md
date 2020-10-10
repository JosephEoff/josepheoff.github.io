---
layout: post
title: "Fixing what isn't broke"
categories: [blog]
mathjax: false
image: /assets/2020-10-10-fixwhatisntbroke/audiooutlet.jpg
---
At least, the manufacturer wouldn't see it that way.

Since I do a lot of audio stuff with the sound card from my PC, I thought it would be a good idea to install a sort of "audio outlet" on my workbench.  I get tired of crawling under the workbench to connect stuff.  I can't count how many times I've bumped my head doing that.

Rather than build one, I decided to buy one.  There are commercially available outlet kind of things intended be installed in the surface of desks.  They have extensions for line-out and microphone-in as well as a couple or three USB ports.

|Audio outlet|
|--------------------------------------------------|
|![Audio outlet](/assets/2020-10-10-fixwhatisntbroke/audiooutlet.jpg)|

That's the one I bought.  I didn't install it flat in the workbench top because first off it isn't in its permanent spot.  Secondly, if it were to lie flat in the surface like it is intended, then it would collect wire scraps and solder balls and short out sooner or later.

I intend to build a kind of rack above the workbench with a built in set of AC outlets and some shelves to hold equipment.  In place of one AC outlet will be this audio outlet.  Since the rack is a long ways off, I put the audio outlet in a little wooden base and screwed it to the bench.

Once I got it all screwed down and plugged in, I tried it out with the [impedance tester I made with GNU Radio.](gnuradio-impedancetester-2)

The results were... sad.

The audio outlet is marked "Microphone" and "Headphone." Both sockets in the outlet are stereo.  Both plugs going out the back of the outlet to the PC are stereo.

The wire in the cable for the microphone is **mono.**

The manufacturer installed a stereo jack and a stereo plug, and connected them with a mono cable.  They saved half a cent on a couple of feet of wire, and I got to spend an hour or so troubleshooting and connecting a stereo cable to the darned thing to make it work right.

I'll grant you that a microphone is a mono signal and that I'm "misusing" the audio outlet by trying to run line-in through the microphone jack of the darned outlet.

It is still a nuisance.  I bought the outlet because the photos on the Amazon page showed the stereo plug on the microphone cable.  I figured that if the manufacturer used a stereo plug then it would be wired to properly work as a mono microphone cable or a line-in cable - but I was wrong.  I now know the truth, and I now have a working line-in extension for my PC.

I cut the stupid mono cable/stereo plug off.  I'm starting a collection of "stupid stuff." The fake stereo microphone cable gets to join up with the "fake stereo line-out" cable that I removed from a pair of desktop PC speakers the other day.

I have a pair of desktop speakers that I have connected to the other PC in my workroom.  They've been kicking around the house for years, and always sounded like crap.  They were so bad, my son spent his own money to buy a better pair of speakers after I offered to let him have the ones I'm using now.

When I built the new workbench, the speakers I used to use with the regular PC were scheduled to become part of the workbench equipment.  That meant the regular PC had to use the crappy speakers.

I took them apart, and fixed the bad solder joints that caused it to hum.  I also had a closer look at the amplifier section because even without the hum the speakers sounded wrong.

There are two speakers in the set.  There is a stereo amplifier and power supply in one of them.  There's a cable with a stereo plug the goes to the PC.

The speakers sounded mono.

Right.  You guessed it.  The manufacturer saved a couple of pennies and ran a two conductor cable from a stereo plug to a stereo amplifier.  Mono sound it is.

I replaced that thing while I was at it.  The speakers sound much better, though not what you'd call good.  Cheap crap is still cheap crap.

Here's the charter members of my "stupid stuff" collection:

|Stupid stuff|
|--------------------------------------------------|
|![Stupid stuff](/assets/2020-10-10-fixwhatisntbroke/uselessplugs.jpg)|

That's two stereo plugs with molded on strain relief, both with mono cables.  The white one came from the speakers.  The red one came from the audio outlet.

------------

What stupid penny penching things have you encountered in your electronic devices?

Leave a comment below and let me know.
