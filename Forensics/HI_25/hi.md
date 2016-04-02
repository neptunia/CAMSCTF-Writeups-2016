#HI - 25

	HI!

[HI](HI)

--------------

The first thing we do is run `strings` on it.

```
$ strings HI
/lib64/ld-linux-x86-64.so.2
libc.so.6
puts
__libc_start_main
__gmon_start__
GLIBC_2.2.5
{StRinGzH
AWAVA
AUATL
[]A\A]A^A_
;*3$"
```

Wait, one of those lines looks suspiciously like a flag. We fix it up a bit to `{StRinGz}`, which indeed is the flag!

Flag: `{StRinGz}`