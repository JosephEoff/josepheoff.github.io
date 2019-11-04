---
layout: post
title: "Implementing a one-shot capture function for the D43"
categories: [blog]
mathjax: true
---
{% include lib/mathjax.html %}
A slight change in plans.

Last time around, I introduced my microwave camera.  I intended to make this post about the hardware for the camera but then changed my mind.

I decided that I'd rather describe the things more or less in the order I did them.  While I don't remember the order of everything I did a couple of years ago, the hardware was definitely not the first part.

What I actually did first was to see if there was even any point in trying to build the camera.  No point in wasting time building a steerable satellite TV dish and all the electronics if there's nothing there to be captured.

The new plan was therefore to recreate some of the first experiments I did before building anything, then post some pictures and descriptions of that.

Towards that end, I wanted to capture some images from my oscilloscope to illustrate some of the things that made me decide that the microwave camera was a workable concept.

To capture the things I wanted to, though, I needed to implement a new function in my [Digital D43](https://github.com/JosephEoff/D43) oscilloscope camera software.  I needed a single-shot capture to automatically make a snapshot of transient events.  The function itself was so trivial that I hadn't even intended to write about it - half an hour looking up numpy functions, a couple of lines of code, a new check box in the GUI, all done.

Well, no.  It wasn't that easy.

The things I wanted to implement really were that easy.  It's just that in actually trying to use the one-shot function, I discovered that there's a bug of sorts somewhere in the OpenCV2 library - or in the Python bindings, or in some library that OpenCV2 uses.

Ever since I switched to the [new camera made of a Logitech C270,](new-oscilloscope-camera) the D43 program was slow to start.  I thought nothing of it, except to be slightly aggravated by having to wait on it.

Turns out there's more to it than that.

The pause function in the D43 software stops the timer for capturing an image from the camera and also called the release() method on the VideoCapture object.  When the pause is turned off (start capturing again,) the start() method created a new instance of the VideoCapture object.  This is where everything went to pieces.  Instantiating a new VideoCapture object on the C270 device caused OpenCV2 to hang.  Stuck completely.

It took a bit to discover where in my program things were going bad, but in the end it really was the instantiating of the VideoCapture object.

I had a look at the [OpenCV2 VideoCapture API documentation](https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html) in hopes of finding that I'd done something wrong, or maybe just a hint that I needed to to something besides just calling release().

No such luck.  But, I did notice that you can separate the instantiating of a VideoCapture object from the actual opening of the camera devices.

For lack of any better idea, I reimplemented the start() function to first instatiate a VideoCapture object, and then in a second step call the open(deviceID) method on it.

That did the trick - the second open succeeded, and the camera software resumed showing images after a pause.

Almost there.  After the pause, there was still a long (twenty seconds or so) break before the camera got to work.  That's the same pause that's been driving me nuts on startup.

There's no way around that short hang, so I have to live with it.

To get a long with it better, I modified the stop() and start() methods in my software so that VideoCapture.release() is only called when selecting a new camera, and so that VideoCapture is also only instantiated when selecting a new camera.

Pause works reliably again, and I have my new one-shot function.  Whee!

If you are using OpenCV2, and it hangs when closing and reopening a camera, try splitting the instatiation from the open.

Instead of this:

~~~
import cv2

cameraindex = 1
#Bad
videocapture = cv2.VideoCapture(cameraindex)
~~~


Try this:

~~~
import cv2

cameraindex = 1
#Better
videocapture = cv2.VideoCapture()
videocapture.open(cameraindex)
~~~

Maybe I'm the only person on the planet to have this problem because it is somehow peculiar to my system - and maybe it'll save someone else a frustrating couple of hours tracking down a similar bug.

Anyway, I'm done for now.

Oh.  Here's a capture made with the one-shot:

|One shot capture|
|----------------|
|![One shot capture](/assets/oneshot.png)|

How utterly impressive.  Totally worth the four or five hours it cost me.  :)

Next time around, I **will** post pictures of my microwave camera experiments.  Promise.
