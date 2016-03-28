# Basic Decryption - 25
	This should be easy.

[basic_decryption.txt](basic_decryption.txt)

------------------

This time, we are given a string: 
`JVWVK2DCK5MXQS3LIZBE2Q3TFNLVO5BQJVVVKN3CKR3XQUSWPBIVUU3TFNSFG53KJVVWY23BNVGXQWKTJJRU6Q3TF5FW2ZCTJVCTSMKPNR2ECTL2GRTWKMTHGBGVOWRTLFMGYZTEI5TXUY3NKY4Q`

Since we see only capital letters and numbers, we can assume it is base32. Plugging it into an online base32 to ascii converter, we get:

`MmUhbWYxKkFBMCs+WWt0MkU7bTwxRVxQZSs+dSwjMklkamMxYSJcOCs/KmdSME91OltAMz4ge2g0MWZ3YXlfdGgzcmV9`

This looks like a base64 string. Decoding that, we get:

`2e!mf1*AA0+>Ykt2E;m<1E\Pe+>u,#2Idjc1a"\8+?*gR0Ou:[@3> {h41fway_th3re}`

But `{h41fway_th3re}` isn't the flag, so we have to continue. The left side of this string initially looks confusing, but based on <a href="https://en.wikipedia.org/wiki/List_of_numeral_systems">this</a> Wikipedia page it seems that it could be Ascii85. We plug it into an Ascii85 to Ascii decoder (http://www.dcode.fr/ascii-85-encoding) to get:

`7b 62 34 35 69 63 5f 66 6c 34 67 7d 0d 0a`. This is quite obviously hex, so we convert it to ascii:

`{b45ic_fl4g}` which is the flag.