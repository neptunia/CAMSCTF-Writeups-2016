# Metropolis - 50

	Legendary hacker Lujing Cen goes by a pseudonym. He also likes video games. What's his favorite game?
	Separate the pseudonym and the game (ID) by a vertical pipe ("|").For example, if the pseudonym is 'alice' and the game is '1', the flag would be {alice|1}

------------------

We are given the name "Lujing Cen" by the problem, and we have to find his online username as well as his favorite video game. A quick google of "Lujing Cen" reveals the username "bobbyluig", which is the username. Easy enough, right?

Now that we know the username, we can attempt to find the favorite game. By searching up "bobbyluig", we find him on many websites such as Github and Soundcloud- but there doesn't seem to be any games. If we change our query to "bobbyluig game", we find somewhat more relevant results, yet for some reason none of the games work as the flag.

However, on the second page of Google search results, we find a page on [ArcadePreHacks](arcadeprehacks.com). In the text under the google link, it says "Hacked By: bobbyluig". However, when we enter the website, it isn't there. This is because the webpage is frequently updated.

To bypass this, we can go to the cached version of the website, where we find "Super City 3". Unfortunately, the flag ```{bobbyluig|Super City 3}``` doesn't work. If we reread the problem, it actually asks for the game ID, not the game name itself. Looking in the URL, we see 1285, which is the second part of our flag.

Flag: ```{bobbyluig|1285}```