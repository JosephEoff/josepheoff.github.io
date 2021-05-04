---
layout: post
title: "Transcribing phone calls with Google Live Transcribe - Measurements and optimization"
categories: [blog]
mathjax: false
image: /assets/2021-05-04-androidtranscribe3/transcribe.jpg
---
Making sure that *Live Transcribe* can hear properly.

<sub>[Transcribing phone calls with Google Live Transcribe - Table of Contents](androidtranscribe-toc)</sub>

I noted while working with the transcription adapter a couple of days ago that the circuit Google recommended isn't quite optimal.  There's a noticeable drop below about 1000Hz.

I decided to break out the fancy tools (right - sound card and free software) and see just how bad it really is.

I got out [GNU Radio](https://www.gnuradio.org/) and assembled an audio frequency spectrum analyser using the sound card of my PC.  GNU Radio was actually developed to do digital signal processing on radio frequency signals, but it is just as happy to handle audio. (I've included the GNU Radio Companion "Flowchart" for the [spectrum analyser here](/assets/2021-05-04-androidtranscribe3/Spectrumanalyser.grc) if you would like to have it. You'll also need to [install GNU Radio](https://wiki.gnuradio.org/index.php/InstallingGR) to use it.  The flowchart is trivial, so it doesn't get a github repository like most of my projects.  It doesn't even get licensed - use it, share it, call it your own.)

For reference, here's the circuit:

|Adapter using the Google recommended values|
|-------------------------------------------|
|![Adapter using the Google recommended values](/assets/2021-05-04-androidtranscribe3/attenuator_not_optimal.png)|
|This is **NOT** optimal.  Do not use this circuit.|

After constructing my spectrum anaylser, I had a look at what Google's recommended circuit does to the audio signal.  It wasn't pretty.

|Hard of hearing transcription adapter|
|-------------------------------------|
|![Hard of hearing transcription adapter](/assets/2021-05-04-androidtranscribe3/Google.png)|

The red line is the input (earphone side) of the adapter.  The blue line is what goes to the microphone input of the transcription phone.

Ideally, the two lines should have the same shape, but with the blue line 20dB (factor of 10) below the red line.

Over to the right, you can that the blue line is 20dB below the red one.  Over to the left, you can see that the blue line loses a considerable amount of sound below 1000Hz - the Google circuit makes the transcription phone some what hard of hearing.

Voice is usually defined as lying between 300Hz and 3000Hz.  This circuit loses a good bit of the lower third of that range.

I suggested in my last post that it might be advisable to use a 330nF capacitor for C1 instead of the 100nF part.  That was a guess, and it turned out to be **very** low.  The load of the microphone input of the Android phone is much higher than I expected (that is, the input impedance is lower than I expected.)

I tried out a 330nF capacitor for C1.  It was better, but still not optimal.

|C1 = 330nF|
|----------|
|![C1 = 330nF](/assets/2021-05-04-androidtranscribe3/330nF.png)|

It still droops quite a lot below about 600Hz.

I stepped up to 1 microfarad after that.

|C1 = 1µF|
|----------|
|![C1 = 1µF](/assets/2021-05-04-androidtranscribe3/1microfarad.png)|

It is still not flat down to 100Hz like the input.

|C1 = 4.7µF|
|----------|
|![C1 = 4.7µF](/assets/2021-05-04-androidtranscribe3/4.7microfarad.png)|

Flat at last!

From those experiments, it seems that the input impedance of the phone is about 2kiloohms.  With the pull down resistor for the microphone detection (R4,) that comes out to a total impedance of around 1kiloohm.

It takes a fairly large capacitor to get the lower cutoff completely below the voice range with that low input impedance.

After correcting the frequency response, I had a look at the input level.

I couldn't find anything that specified the correct microphone level for an Android phone.  Maybe it is specified somewhere that I couldn't find it.

Lacking a specification to measure against, I did the best I could.

I hooked up the adapter between two phones, and made a phone call.

On the phone being used to make the call, I turned the volume all the way up.

On the other phone, I started a simple voice recorder program.

With the two phones connected with the improved adapter, I made a recording while speaking at various loudness levels - normal voice, soft voice, loud voice.

Speaking loudly into the calling phone caused the recording to clip - but only if I spoke **really** loud into the phone.

I think the attenuation level is about right.  It reduces the signal so the microphone input can handle it, without attenuating things too much at lower levels.

This is what the voice recording looks like:

|Voice level recording|
|---------------------|
|![Voice level recording](/assets/2021-05-04-androidtranscribe3/level.png)|

The blippity looking lines across the middle represent the loudness of my voice. Louder = taller bars.

The loudest sections were with me speaking in a **really** loud voice with the volume all the way up.  The bars hit the edges of the window in those spots, but only for short moments at the loudest times.  That's clipping, but it shouldn't be a problem in normal use.  Most folks don't turn the volume all the way up, and most folks don't yell at people on the phone.

Here's the final, revised circuit:

|Final adapter circuit|
|---------------------|
|![Final adapter circuit](/assets/2021-05-04-androidtranscribe3/revisedcircuit.png)|
|This should be a good circuit to build and to use for transcription.|

Note that I changed from a non-polarized capacitor to a polarized (electrolytic) capacitor.  If you build this circuit, you will need to make sure that you install the capacitor properly.  They usually have a stripe marked down one side that shows the **negative** connection.  The negative side goes towards the eaphone, the positive side goes towards the microphone.  The microphone connection has a DC voltage on it, the earphones don't.

You could replace the electrolytic capacitor with a ceramic 4.7 microfarad part, but they are almost always surface mount parts - you can't reasonably connect them in a circuit with leaded parts without using a printed circuit board.  Large value ceramic capacitors also aren't common in small shops - they'll normally stock electrolytic capacitors, though.

I'll start looking at the best way to construct this tomorrow.  I may just summarize a few ways to do it, and see what the potential users think is simplest to build (or have built.)

|*Live Transcribe* understands electronics jargon|
|------------------------------------------------|
|![Live Transcribe understands electronics jargon](/assets/2021-05-04-androidtranscribe3/transcribe.jpg)|

-------

The peaks down around 50Hz in the spectrum plots are caused by interference from the AC power in my house.  I built the circuit without any kind of shielding, and the microphone wire runs a couple of meters down to the PC under the workbench - it picks up **far** more noise than it ought to.  I need to install a better (shielded) cable from the top of my workbench down to the PC.  That nasty spike won't be there when the adapter is used with a phone - it only exists on my workbench setup.


<sub>[Transcribing phone calls with Google Live Transcribe - Table of Contents](androidtranscribe-toc)</sub>
