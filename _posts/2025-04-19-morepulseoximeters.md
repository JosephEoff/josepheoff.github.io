---
layout: post
title: "A list of inexpensive pulse oximeters for use with OSCAR"
categories: [blog]
mathjax: false
description: "A list of inexpensive pulse oximeters for use with the OSCAR CPAP software"
image: /assets/2025-04-19-morepulseoximeters/3.jpg
---
How many can we find?

I recently mentioned that I implemented support for the Wellue/Viatom POD2W pulseoximeter for the OSCAR CPAP software.  The idea was to put support for an inexpensive pulseoximeter into the OSCAR software so that folks could check for low oxygen levels in their blood without having to spend a bundle on the more expensive oximeters out there.

It turned out that while the POD2W is available on Amazon here in Europe, it isn't available in the US or other countries.  At a guess, Wellue/Viatom makes different models to meet the regulations in different markets.

To help out folks in the US, I ordered a Wellue/Viatom OxySmart pulseoximeter from Amazon.com (US) instead of Amazon.de (Germany.)  It only cost $20, though shipping from the US to Germany was rather expensive.

I figured I'd have a look at the data format and have a go at implementing support for it in OSCAR.

It turns out there's no need to write software.  The OxySmart uses the same file format as the POD2W.  The OSCAR support for the POD2W is all you need to be able to import the OxySmart data.

I expect there are more such inexpensive pulseoximeters out there.  I'm going to use this post to collect information on pulseoximeters that can be used with OSCAR.

The list, of course, starts with the POD2W and the OxySmart.

|Manufacturer|Model|Front|Back|Notes|
|------------|-----|-----|----|-----|
|Wellue/Viatom|POD2W|![POD2W front](/assets/2025-04-19-morepulseoximeters/1.jpg)|![POD2W back](/assets/2025-04-19-morepulseoximeters/2.jpg)|Folder: /28/host/|
|Wellue/Viatom|OxySmart (KS-60FWB)|![OxySmart front](/assets/2025-04-19-morepulseoximeters/3.jpg)|![OxySmart back](/assets/2025-04-19-morepulseoximeters/4.jpg)|Folder: /27/host/|

I've asked for example files from folks on Reddit.  I'll post updates for any replies I receive.

If you have a Wellue/Viatom pulseoximeter and would like to help, I need a data file from the Android ViHealth app, the exact model number and name of the pulseoximeter, and a photo of the front and back.  You can put all of that in a comment on this post - Disqus is setup to allow guest posts without requiring that you signup to Disqus.

The data files are under Android/data/com.viatom.vihealth/files/

In that folder will be a folder with a number. Mine are 27 (OxySmart) and 28 (POD2W.) Under the numbered folder will be another folder named host. In that folder will be files with a long numerical name that ends in .dat.

As an example, a data file for the OxySmart looks like this: 

Android/data/com.viatom.vihealth/files/27/host/1745080270764.dat

The numerical file names are Unix timestamps that give the start date and time of the file. 

