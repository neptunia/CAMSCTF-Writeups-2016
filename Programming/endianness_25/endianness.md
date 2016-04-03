#Endianness - 25

	I got this from my friend's cool antique big endian computer and it made sense there...

[endian.txt](endian.txt)
---------------

GOOD THING I HAVE A BIG-ENDIAN COMPUTER!!!! I opened the file and got the flag.

... just kidding.

First, we take the binary data of the file:

`1101111001000010100100101110001011111010001011000111011000100110111110100011011010010110001011100010111000110110101001101111101011001100011101100010011010001100001011000111011010111110`

and reverse it:

`0111110101101110001101000011000101100100011011100011001101011111011001010110110001110100011101000110100101101100010111110110010001101110001101000101111101000111010010010100001001111011`

Then we convert this to ascii:
`}n41dn3_elttil_dn4_GIB{`
and reverse it too, to get the flag!

Flag: `{BIG_4nd_little_3nd14n}`