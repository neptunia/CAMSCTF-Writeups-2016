#Windows 8 - 200

	"Find" administrator's password.

-----------------

You know what's a good tool for cracking passwords with windows? There's one called OphCrack (http://ophcrack.sourceforge.net/). We get an iso, plug it into our vm in the CD drive, and change the boot order so that we can boot from the CD.

![screenshot](http://i.imgur.com/RatQwmS.png)

We have successfully cracked the admin password! His password is `692786`.

Flag: `{692786}`