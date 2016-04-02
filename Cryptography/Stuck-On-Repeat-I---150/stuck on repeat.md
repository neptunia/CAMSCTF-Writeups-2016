#Stuck On Repeat 1 - 150
  
  Have a bite. Repeat.
  
[repeat1.txt](repeat1.txt)

-------------

We are given this string:
`393a72301d3a2d301d1a0d101d1a0d103f`
Which seems to be hex-encoded data. Also, based on the title, we can assume that the problem refers to repeated XOR. So, we first try crib dragging with cribdrag.py (https://github.com/SpiderLabs/cribdrag). We try some random characters, and we get:
![flag](http://i.imgur.com/llzy1Qw.png)
So the key was just `B`, and the flag is `{x0r_xor_XOR_XOR}`