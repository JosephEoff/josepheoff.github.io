---
layout: post
title: "Sea sounds by the seashore -rescuing a bad recording of wave sounds"
categories: [blog]
mathjax: false
description: "A step by step guide to recovering the sounds of ocean waves crashing from a recording that has a lot of wind sounds."
image: /assets/2025-10-31-seasoundsbytheseashore/1.png
---
Sometimes a little Audacity can make up for not having a dead cat.

I made a video of the waves crashing on the shore when I went to visit Holly Beach in Lousiana on the Gulf of Mexico with my mother and my sister a couple of weeks ago.  That video had a specific purpose that I won't be going into here.

The video was OK, but what I didn't realize at the time was that the wind had caused so much interference with the microphone that the waves couldn't be heard.  Even if I had realized it, there wasn't much I could do.  I had to use the camera's built in microphone.  Going back to someplace to buy or borrow an external microphone and a [dead cat](https://en.wikipedia.org/wiki/Microphone#Microphone_windscreens) wasn't an option - we were on a schedule that didn't include hours to drive around looking for a store to buy a microphone, then driving back to the beach.

|Bad recording|
|-------------|
|[Bad recording](/assets/2025-10-31-seasoundsbytheseashore/1.mp3)|

If had I wanted the sound of the wind on the beach, it would have been perfect, but it is pretty much useless as a recording of waves.

I loaded up the audio from the video recording in [Audacity](https://www.audacityteam.org/) and had a look at the spectrum of the recording to see if there was any hope.

|Spectrum of bad recording|
|-------------------------|
|![Spectrum of bad recording](/assets/2025-10-31-seasoundsbytheseashore/1.png)|

Up to about 5000 Hz is the wind sound.  Above that, there's actually a fair amount of wave sounds.

Audacity has some fairly steep filters, so I tried just straight up filtering out the wind sounds:

|Reduce the wind sounds|
|----------------------|
|![Reduce the wind sounds 1](/assets/2025-10-31-seasoundsbytheseashore/2.png)|
|![Reduce the wind sounds 2](/assets/2025-10-31-seasoundsbytheseashore/3.png)|

Filtering out everything below 5000 Hz lets you hear the crashing waves, but only after you normalize the filtered signal back to an audible volume.

The wave sounds are, of course, very high pitched and unnatural sounding.  That's bad.

|Filtered waves|
|--------------|
|[Filtered waves](/assets/2025-10-31-seasoundsbytheseashore/2.mp3)|

I though about it for a while, and realized that wave sounds are basically white noise.  They are amplitude modulated by the crashing of the waves, but the sounds are really just white noise.  That leaves me with a way out - just transpose the wave sounds down until they sound more natural.

|Transpose the wave sounds|
|-------------------------|
|![Transpose the wave sounds 1](/assets/2025-10-31-seasoundsbytheseashore/4.png)|
|![Transpose the wave sounds 2](/assets/2025-10-31-seasoundsbytheseashore/3.png)|

That sounds much more realistic, to the point that the folks who were there think it is the original recording.

|Filtered and transposed wave sounds|
|-----------------------------------|
|[Filtered and transposed wave sounds](/assets/2025-10-31-seasoundsbytheseashore/3.mp3)|

That's the final, full length recording of the wave sounds after restoration.  It still has some wind noise, which adds some realism to it, and the waves sound as real as they did in person.  When played back on the cheesy speaker of a digital picture frame, you'd be hard pressed to tell that it was ever manipulated.

Newer versions of Audacity have a function called "Normalize Loudness" that is actually much better for this kind of thing.  Since I'm not using Windows, I am limited in the version of Audacity I can use to the version that the software management of my Linux system offers.  That version (2.2.2) does not include the loudness normalizer, else I'd show you how to use it.

-------

I later realised that the wave sounds aren't particularly synchronised with the waves.  I was a bit back from the water, using a zoom to collapse the water and the waves and the sun to a sea of scintillating lights.  You don't really see any particular wave crashing to go along with the recorded sound.  From that point of view, I suppose I could have gotten some random recording of wave noises and put it under the video.

From my point of view, that would have been much more fake than my restored recording.  Mine is real, just as it happened on that windy day - it's just a good bit clearer than in the original.

If you use this method to restore some waves, keep in mind that it will make an absolute **mess** out of other sounds.  Sounds of birds crying or singing, people talking, boats puttering by with the motor running, etc.  will be absolutely mangled.  This trick only works on wave sounds, and only because they are essentially white noise.

