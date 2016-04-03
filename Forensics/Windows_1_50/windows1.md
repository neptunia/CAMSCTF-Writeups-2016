#Windows 1 - 50

	Welcome to a series of fun Windows challenges that will bring back memories of your childhood. There are 9 parts to this challenge, all solvable on a single Virtual Machine. For reference, all flags should be submitted in {flag} format. However, they do not necessarily have braces when you find them.

	Discover the name of the "annoying" file messing up your mouse in User's account.

[Google Drive](https://drive.google.com/file/d/0B-TVTxo5SGFqa0hPbWp0bXN3NnM/view?usp=sharing) | [DropBox](https://www.dropbox.com/s/umm3d9z43sr9qu0/XP_Machine.7z?dl=0) | Password: xp_challenge_123
-----------------

First we download and extract the VM with the given password. Next, if we care about screwing up the machine, we can take a snapshot (if possible) so that we can revert back to the original version.

![image](http://i.imgur.com/fkXiXsI.png)

Now we turn it on, and log in as "User."

By the way, since we made a snapshot you're free to click those things on the desktop. It's pretty funny.

Anyways, we notice that our mouse's right and left clicks have been reversed. That's pretty annoying, what was the file that caused it? We can look through startup, since it starts up when you log in (If you noticed, a black command line thing may have popped up for a fraction of a second when you booted):

![startup](http://i.imgur.com/3sBDSoh.png)

So the flag is `rundll32_swap`. We can delete the file now. If you log out and log back in it should be fixed, or you can go into control panel and un-reverse the mouse bindings.

![reversy](http://i.imgur.com/txffci7.png)