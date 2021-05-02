---
layout: post
title: "Transcribing phone calls with Google Live Transcribe - A prototype and a test"
categories: [blog]
mathjax: false
image: /assets/2021-05-02-androidtranscribe2/test.jpg
---
Electrically functional, but not quite ready for prime time.

<sub>[Transcribing phone calls with Google Live Transcribe - Table of Contents](androidtranscribe-toc)</sub>

I had a look at the task a couple of days ago, and made some notes on what needed to be done.  I hadn't intended the sketches to be used - they were concept sketches to show the principle behind the needed circuitry and to explain why a simple lash-up with Y-adapters wouldn't work.

This evening, I dug out some parts and hunted down some references then drew up a circuit that **will** work.

This post will go into some more of the theory then show a complete and functional (if ugly) circuit.

[Google has a recommended test circuit](https://source.android.com/devices/audio/latency/loopback) for doing audio tests on Android using a single phone.  That's called a "loopback" circuit because it takes the eaphone output and makes a loop back into the microphone input of the same phone.

Here's Google's test circuit:

|Google's loopback adapter|
|-------------------------|
|![Google's loopback adapter](/assets/2021-05-02-androidtranscribe2/google_loopback_circuit.png)|

I adapted that to be used to connect the earphone output of one phone to the microphone input of a second phone.

Here's the circuit I settled on:

|Transcription adapter circuit|
|-----------------------------|
|![Transcription adapter circuit](/assets/2021-05-02-androidtranscribe2/attenuator_complete.png)

I'm sure you can see the similarity with the [example circuit I drew in my last post.](androidtranscribe1)

The attenuation is the same in both circuits - 10 to 1.  That is, the microphone input level is about 1/10 the earphone level.  They use different values, but with the same ratio (Google used 1k to 100 ohms, I used 10k to 1k.)  For the real circuit, I went with Google's values.

Referring to my diagram, here's what the individual parts all do:

1. R1 and R2 mix the audio from the earphones. That way, you are guaranteed to get the voice from the phone call.
2. R3 together with R1 and R2 forms an attenuator. The junction of R1, R2, and R3 has the sum of "Earphone_Left" and "Earphone_Right" divided by 10.
3. C1 is a coupling capacitor.  Without it, the "transcribe" phone would "see" a button press (caused by R3,) and do something other than simply switch to the external microphone input. (See [Google's "3.5 mm Headset: Accessory Specification" for details of the audio accessory buttons.](https://source.android.com/devices/accessories/headset/plug-headset-spec))  C1 prevents the flow of DC from the microphone input while allowing the audio to pass.
4. R4 is there to signal the "transcribe" phone that an external microphone is connected.
5. R5 is presumably there to reduce short circuit current through the capacitor.

Describing it all that way reminded me that C1 and R4 form a high pass filter.  The cutoff is around 790Hz.  That's rather high and is probably removing too much of the lower frequencies from the audio. (Speech is usually considered to be between 300Hz and 3kHz.) I'd recommend using at least 330nF (cutoff around 200Hz.)  I'll change the circuit diagram when I draw up the final plans.

From that diagram, I built an adapter using a 4 pin headphone plug and an old headset.

Here's the assembly of the test adapter:

{:start="0"}
0. Plug

|Four pin headset plug|
|---------------------|
|![Four pin headset plug](/assets/2021-05-02-androidtranscribe2/CTIAplug.jpg)|
|Note the location of "Ground" and "Microphone" - make sure to connect them properly.  Old three pin headsets had the ground connected to the shell.  The four pin headsets have the microphone connected to the shell.|

{:start="1"}
1. Connect R4

|R4 - external microphone select 2k|
|-------------------------------|
|![R4 - external microphone select](/assets/2021-05-02-androidtranscribe2/1.jpg)|

{:start="2"}
1. Connect R3

|R3 - attenuator 100 ohms|
|---------------|
|![R3 - attenuator](/assets/2021-05-02-androidtranscribe2/2.jpg)|

{:start="3"}
1. Connect R5

|R5 - short circuit protection 100 ohm|
|---------------|
|![R5 - short circuit protection](/assets/2021-05-02-androidtranscribe2/3.jpg)|

{:start="4"}
1. Assemble summing circuit

|R1 and R2 - summing circuit two 1k resistors|
|---------------|
|![R1 and R2 - summing circuit two 1k resistors](/assets/2021-05-02-androidtranscribe2/4.jpg)|

{:start="5"}
1. Attach summing circuit and C1

|C1 and summing circuit - AC coupling 100nF|
|---------------|
|![C1 and summing circuit - AC coupling 100nF](/assets/2021-05-02-androidtranscribe2/5.jpg)|

{:start="6"}
1. Connect earphone left and right

I cut the earphones off of an old Android headset and connected the wires to the adapter.

|Earphone connection|
|---------------|
|![Earphone connection](/assets/2021-05-02-androidtranscribe2/6.jpg)|

{:start="7"}
1. Connect earphone ground

|Earphone ground connection|
|---------------|
|![Earphone ground connection](/assets/2021-05-02-androidtranscribe2/7.jpg)|

{:start="8"}
1. Completed assembly

Note that I connected the earphones to the adapter.  You can hear and speak using the headset while the "transcribe" phone can "hear" the voice from the call.

|Complete adapter|
|---------------|
|![Earphone ground connection](/assets/2021-05-02-androidtranscribe2/8.jpg)|

That's it electrically.

I plugged the adapter into a couple of phones ("call" is the gold phone, "transcribe" is the black phone) and called the "call" phone from a (cordless "Siemens") landline telephone.

Here's the result of that phone call:

|Successful transcription of a phone call|
|![Earphone ground connection](/assets/2021-05-02-androidtranscribe2/test.jpg)|

Google "Live Transcribe" prefers that you speak slowly and clearly.  The "transcribe" phone transcribes just as well with the adapter as it does with the normal, built in microphone.

With the electrical parts all cleared up, the question now is "What's the best way to build these?"

There's a couple of ways to build them, and I'm not sure which is easiest and cheapest.  I suspect "cheapest" will depend on what is readily available to the folks who need the adapters.  I'll have to check with the person who started this to see which way is best.

In my next post, I'll describe a couple of way that this could be built.  The problems from here on out are all mechanical, and depend on what parts are available.

<sub>[Transcribing phone calls with Google Live Transcribe - Table of Contents](androidtranscribe-toc)</sub>
