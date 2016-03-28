# Ocular Waves - 200

	Here's a file. Look deep within. Very deep. Then... see it.
	
[time](time)

------------------

We are given a file called time, with no extension. First things first, we run
```file time``` in terminal and it says KGB Archiver.

To open this, we need to download some software. I used [Universal Extractor](http://www.portablefreeware.com/?id=641) to extract the file. It takes a while but eventually it gives us a new file - [time.sfArk](time.sfArk).

Searching up .sfArk, we see that it is a compressed .sf2 file. To decompress it, I used the [sfArk SoundFont Compression](http://melodymachine.com/sfark.htm) tool, although there are other tools you can use.

This leaves us with [time.sf2](time.sf2). I tried searching up many tools to open sf2 files, none of which worked. Eventually, I stumbled upon [Polyphone](http://www.polyphone.fr/). I opened it and there was a huge list of samples, most of which sounded like [this](1.wav). However, a very particular sample sounded very strange- [sample 85]((85).wav). It sounds like some random beeping- almost always a good sign in forensics.

We open the file in [Audacity](http://www.audacityteam.org/). We switch the view to Spectrogram, and there's the flag!

[Picture:](flag.png)

Flag: ```{G0T_71m3_4_M33333}```