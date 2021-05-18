---
layout: post
title: "Transcribing phone calls with Google Live Transcribe - Table of Contents"
categories: [blog]
mathjax: false
image: /assets/2021-04-29-androidtranscribe/transcribe.jpg
---
An aid for the hard of hearing.

There was a question on the [*Electrical Engineering* StackExchange](https://electronics.stackexchange.com/) recently that I thought was worth a little time and effort.

It has taken me a couple of days to get around to it, but I found time to look at how you can use [Google "Live Transcribe"](https://play.google.com/store/apps/details?id=com.google.audio.hearing.visualization.accessibility.scribe&hl=en&gl=US) to put "closed captions" on a phone call.

It's going to take a little explaining and organizing to make a simple and robust adapter, so I've put up a table of contents along with the first post.

Note:
- This will be a sort of round about trip to find an optimal solution. I will include all of my experiments here.
- Early experiments and circuits may be non-functional or non-optimal.
- If you are following along as I make each post, remember that any given circuit may be partial or may not work well.

I'll make it clear when I have arrived at what I think is a good, workable circuit and solution.
The first part to solve is the electrical circuit.  The second part is making it easy to reproduce by hand in small numbers.  I don't think this will be a large enough product that it would make sense to have them manufactured in a factory.  Easy access to common parts and a simple mechanical construction will be needed.

0. [Transcribing phone calls with Google Live Transcribe - A first look](androidtranscribe1) - It ain't rocket science, but it ain't trivial, either.
1. [Transcribing phone calls with Google Live Transcribe - A prototype and a test](androidtranscribe2) - Electrically functional, but not quite ready for prime time.
2. [Transcribing phone calls with Google Live Transcribe - Measurements and optimization](androidtranscribe3) - Making sure that *Live Transcribe* can hear properly.
3. [Transcribing phone calls with Google Live Transcribe - An adapter made from common parts](androidtranscribe4) - Not the cheapest way but certainly a reproducible way.
4. [Transcribing phone calls with Google Live Transcribe - A properly functioning loop-back adapter](androidtranscribe5) - A CTIA four pole plug and a few spare parts.
