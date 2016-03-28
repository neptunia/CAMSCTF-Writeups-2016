# Askey I - 50
	Ask and ye shall receive. ASCII and ye shall d13.

[askey.txt](askey.txt)

------------------

We are given a strange string, with seemingly random ASCII characters. We recognize the first four characters `"synt"` to be ROT13 of the word `"flag"`, so we know that this this seems to an ascii shift of letters by +13 (This is also hinted to in the problem, where they say "d13"). We write a quick script to solve the problem:

```python
s = '73 79 6E 74 88 82 81 73 3A 45 6E 7B 86 7C 7B 72 4C 7B 7C 4C 73 76 7B 72 8A'
for char in s.split(' '):
    print(chr(int(char,16)-13),end='')
```

Note: I used the hex data in the string because some of the characters were unprintable.

Running the program, it outputs:
`flag{utf-8anyone?no?fine}`