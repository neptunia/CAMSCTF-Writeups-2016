#Numbers - 25

	"A picture is worth a thousand words."

[numbers.png](numbers.png)

-------------

We open the file first in a hex editor, and see at the bottom:

`{y0u_f0uNd_th3_1st_p4rt`.

Then we open it in an image viewer, where we see:

![numbers.png](numbers.png)

Converting int to ascii, we get:

`"99 97 78 100 95 110 48 119 95 121 48 117 95 105 48 117 110 100 95 116 104 51 95 111 116 104 51 114 125"`

Which converts to

`_aNd_n0w_y0u_f0und_th3_oth3r}`

Which, when we concatenate them, we get the flag!

Flag: `{y0u_f0uNd_th3_1st_p4rt_aNd_n0w_y0u_f0und_th3_oth3r}`
