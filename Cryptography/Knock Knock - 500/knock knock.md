# Knock Knock - 500
	The LG Knock Code™ (http://www.lg.com/us/mobile-phones/knockcode) is pretty convenient. It boasts an impressive 86,367 unique combinations. But just how easy is it get into a phone that is secured using this system? The flag is in the format {answer}.

[knock.7z](knock.7z)

------------------

In order to solve this problem, we first read up on how android passwords are stored (https://www.pentestpartners.com/blog/cracking-android-passwords-a-how-to/ is a really good resource for this). We see that:

	1. Inside password.key there is a SHA-1 and a MD5 hash of the password
	2. From device_policies.xml we see that the password is 7 characters
	3. From locksettings.db we see the salt is 8023748904807506340.

Since I didn't have oclHashcat, I wrote my own script to crack this. First, we copy out the MD5 hash (last 16 characters). Next, we convert the salt to lowercase hex (`6f5a151e05fb21a4`). We can then brute force the password:

(program is in python 2)
```python
import hashlib

target = '8C8476F4DE6ECF815CCF683E66F69229'
salt = '6f5a151e05fb21a4'

for i in range(10000000):
    chk = str(i).zfill(7)+salt
    if hashlib.md5(chk).hexdigest().upper() == target:
        print i
```

which soon prints out:
`1143224`.

So the flag is `{1143224}`.
