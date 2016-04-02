#One-Zero-Zero - 150

	Rebel leader Brad Turk has sent a message of the first strike on the United States to Lora Sum, a sleeper agent. Before the message got to her, the NSA has intercepted the message as 16 chunks; however, it was encrypted via RSA. In unrelated news, the Navy SEALS have extracted a public key from a soldier in Turk's militia.

[one-zero-zero.zip](one-zero-zero.zip)

----------------------

We are given a RSA key in key.pub:

	-----BEGIN PUBLIC KEY-----
	MEUwDQYJKoZIhvcNAQEBBQADNAAwMQIqAsjVmvR8gas3JbRyvkF+O/erhUOa9ybt
	Pf32ZInRVdwLdxx6UO98Xlj7AgMBAAE=
	-----END PUBLIC KEY-----

Based on the `key.pub` specifications, since no public exponent is given we can assume the public exponent is `65537` (the default), and the public modulus is `MEUwDQYJKoZIhvcNAQEBBQADNAAwMQIqAsjVmvR8gas3JbRyvkF+O/erhUOa9ybtPf32ZInRVdwLdxx6UO98Xlj7AgMBAAE=` which converts to

`1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139`

in base 10. However, we do not need to factor this number. In the problem statement, we are given "One-Zero-Zero," meaning 100. On the [wikipedia page for RSA numbers] (https://en.wikipedia.org/wiki/RSA_numbers) we see that RSA-100 has already been factored:

	RSA-100 = 37975227936943673922808872755445627854565536638199
        	× 40094690950920881030683735292761468389214899724061

Using this, we can calculate the private `d` and solve the problem! See my code: [decoder](decode.py)

So the flag is `flag{it'sc4lledpriv4tefor4re4son}`.