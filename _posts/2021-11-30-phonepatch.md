---
layout: post
title: "An Android phone patch adapter"
categories: [blog]
mathjax: false
description: "An adapter to connect two Android phones together.  This phone patch allows calls to be forwarded through a pair of Android phones."
image: /assets/2021-11-30-phonepatch/zoom.png
---
Connecting two Android phones for fun and profit.

I received an interesting inquiry in the comments to one of my ["Transcribing phone calls with Google *Live Transcribe*"](androidtranscribe-toc) posts.

It seems some folks would like to be able to route phone calls through a pair of Android phones.  The idea is to connect two phones together with a cable, then when one of the paired phones is called the audio for the call is routed to the second Android phone of the pair which then makes a call to a third phone.  Accepting the call and dialing the number of the third phone wasn't specified to be automatic - somebody will have to operate the phone patch.  Or, maybe not.  Android phones (at least, some of them) can be set to automatically answer a call.  Set both of the paired phones to automatically accept incoming calls and you've got an automatic phone patch.

The audio routing is trivial.  It is nearly identical to the adapter I made to allow *Live Transcribe* to listen in on a phone call.

To make a fully functional phone patch, you need two copies of the circuit that I made for *Live Transcribe.*

It is very simple - any engineer could figure it out after looking at the circuit for Google's recommended [Android audio loopback dongle.](https://source.android.com/devices/audio/latency/loopback)

I'm not an engineer - I do this kind of stuff for fun - and it was still easy as pie.  Heck, I even managed to improve Google's suggested circuit.

In answer to the inquiry, here's the circuit you need to connect two Android phones together to route a call:

|Android phone patch cable|
|-------------------------|
|![Android phone patch cable](/assets/2021-11-30-phonepatch/schematic.png)|
|<sub>Download the image for a clearer view - or open it in a new tab.</sub>|

Not much to it.  It's almost identical to the circuit I used for the [transcription adapter.](androidtranscribe4)

|Transcription adapter|
|---------------------|
|![Transcription adapter](/assets/2021-05-10-androidtranscribe4/revisedcircuit.png)|

The circuit is trivial - I give it to you.  Whoever needs it can use it.  It took me less time to draw the circuit than it took me to write about it.

-------

I'm having a difficult time imagining a legitimate use for this thing.

The most harmless thing I can think of is to prank someone - you call the paired phones and make your call look like it is coming from somewhere else.  The setup is overkill for that, though.  If you wanted to fool someone and you've got all those phones (with SIM cards) to hand, you'd just make the call with one of the phones for which your target doesn't know the number.

If the idea is to hide phone calls between two people to make illicit (illegal) deals, then I'd suggest you not go that route.  If one of the parties is suspected, the authorities can get a list of all the numbers called on that person's phone - that will lead straight to the phone patch pair.  Once the authorities find that, they can locate the phone patch and find the numbers called by the second phone in the pair.  You might slow them down, but they can still find you in the end.

The same goes for anyone who tries to use this for the legitimate goal of communicating past a repressive government.  It might work short term, but it can be found and tracked long term - and even turned against the users.

The only legitimate use I can see which will not get you in hot water would be to make calls across network or country borders in places where the networks don't mesh for whatever reason.  That'd be a mighty small set of users, though.

Whatever.  Build it, use it, try to stay out of trouble.

-----

The circuit is simple.

Building copies of it by hand is easy.

Making a commercial product (more than a few dozen) from it is **not** easy.

I wish all of you bidding on the [*Freelancer* project](https://www.freelancer.com/projects/electrical-engineering/electrical-circuit-for-cable-connect/?ngsw-bypass=&w=f#) behind this inquiry good luck - and I wish the project owner good luck.

|Freelancer project concept|
|--------------------------|
|![Freelancer project concept](/assets/2021-11-30-phonepatch/phonepatchconcept.jpg)|

For good measure, I am also including the [KiCad files](/assets/2021-11-30-phonepatch/scribble.zip) for the patch cable.  You'll need to unzip the file then use [KiCad](https://www.kicad.org/) to open the scribble.pro file.

----

For the record, it took me about 15 minutes to draw the schematic.  It has taken me the better part of an hour and a half to write this blog post.


