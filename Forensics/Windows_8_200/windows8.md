#Windows 8 - 200

	"Find" administrator's password.

-----------------

You know what's a good tool for cracking passwords with windows? There's one called OphCrack (http://ophcrack.sourceforge.net/). We get an iso, plug it into our vm in the CD drive, and change the boot order so that we can boot from the CD.

Note: in order to boot into OphCrack, we first may need to change the bios system delay (which defaults to 0). We can change this in the .vmx file:

![bios boot delay](http://i.imgur.com/1YRMehG.png)

And then we can mash f2 to get into bios. We then navigate to boot and move "CD-ROM drive" above "Hard Drive."

![bios](http://i.imgur.com/H0Ctbdn.png)

Then we just boot into ophcrack and let it do its work.

![screenshot](http://i.imgur.com/RatQwmS.png)

We have successfully cracked the admin password! His password is `692786`.

Flag: `{692786}`
