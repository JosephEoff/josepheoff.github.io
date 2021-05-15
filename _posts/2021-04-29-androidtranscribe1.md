---
layout: post
title: "Transcribing phone calls with Google Live Transcribe - A first look"
categories: [blog]
mathjax: false
image: /assets/2021-04-29-androidtranscribe/transcribe.jpg
---
It ain't rocket science, but it ain't trivial, either.

<sub>[Transcribing phone calls with Google Live Transcribe - Table of Contents](androidtranscribe-toc)</sub>

Someday I'm going to have to search the whole blog and see how many posts contain the phrase "somebody asked a question on the [*Electrical Engineering* StackExchange.](https://electronics.stackexchange.com/)"

However many there are, this is another.

This question in particular was about connecting the earphone output of one smart phone to the microphone input of a second smart phone.  The idea is to let [Google "Live Transcribe"](https://play.google.com/store/apps/details?id=com.google.audio.hearing.visualization.accessibility.scribe&hl=en&gl=US) "listen in" on a phone call and write text as the conversation is running.  There are folks who don't hear well who could make use of the transcription to aid their understanding of the spoken words.  *Live Transcribe* unfortunately can't transcribe directly from a call.  The way around that is to use a second phone to do the transcription.

This means that the earphone needs to still work, and that the microphone of the phone that is used as a phone also has to work.

One suggested solution was a bunch of Y-adapters and some aux-cables.

That won't work, and anyone who has the slightest knowledge of how the headphone adapters work would understand why.

For those who don't understand it, I recommend a look at the [Android 3.5mm headset specifications.](https://source.android.com/devices/accessories/headset/plug-headset-spec)

There are two important bits that go into why just plugging adapters together won't work.

1. The microphone jack of an Android phone requires a certain resistance between the microphone connection and ground so that the phone can recognize that a microphone is connected.
2. The output level on the earphone connection is far too high for the microphone input.

That first point is where the Y-adapter and aux-cable plan falls on its face - the phone that is supposed to record won't even recognize that there's a cable attached to the microphone input.  It will either record nothing, or it will use the phone's regular microphone.

If you fix the first part, then you still have to deal with the second part.

The first part is easy.  Put a 1k resistor from microphone to ground, and any Android phone out there will recognize that there's a microphone attached.

The second part is a little trickier.  The output levels of the headphone connection varies, and the user can change it with the volume control of the phone.  The microphone level isn't a fixed, known value, either.

I tried things out with my phone, and I find that the earphone level is about 600 millivolts RMS at full volume.

I also had a look at the microphone level when speaking in a normal tone of voice about 30 centimeters (1 foot) from the microphone - about like when I have the headset on.  That got me just a few millivolts RMS.

Recording the headphone output with the microphone input means that you have to reduce the level considerably.

You can do part of it using the volume control, but you really need what is known as an attenuator to reduce the level.

Electrically, an attenuator is very simple:

|Android attenuator|
|------------------|
|![Android attenuator](/assets/2021-04-29-androidtranscribe/attenuator.png)|
|**2021-05-02 Note:** This is **NOT** a complete circuit. This is a section of the needed circuit, but not all of it.|

It also solves the minumum resistance problem so that the phone will recognize that the microphone is connected.

The trick lies in connecting it, and making it simple enough that anyone can replicate it.

The person who asked about it on *Electrical Engineering* can't use a soldering iron, and is limited to what can be bought and assembled in a local shop.

What's missing is a clear set of instructions on how to build a proper adapter that meets the needs of the targeted users.

The solution needs to be inexpensive, simple, and robust.

I'm going to give this a little more thought as to the simplest, cheapest way to build the adapter.

I'll post more information as I make progress.  I'll also post an answer on the the *Electrical Engineering* StackExchange when I get done.

------

Google suprised me with how well the transcriber works.  I tried it out with a microphone I had laying here, and it went right along with me as I was cussing at the cat (she likes to get on my nerves.)

|Google *Live Transcribe*|
|------------------------|
|![Google Live Transcribe](/assets/2021-04-29-androidtranscribe/transcribe.jpg)|

<sub>[Transcribing phone calls with Google Live Transcribe - Table of Contents](androidtranscribe-toc)</sub>
