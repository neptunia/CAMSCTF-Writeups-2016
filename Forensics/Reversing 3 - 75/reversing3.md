# Reversing 3 - 75

    It's easy, but easy if often hard.
[3.exe](3.exe)

------------------

Again, we can try running ```strings 3.exe``` but it's obvious it won't work anymore. 
If we try to actually run the program, it says to use a debugger. So, we open it up with [Immunity Debugger](http://www.immunityinc.com/products/debugger/).

We run through the program once, and surprisingly, it gives us the flag!

![screenshot](screenshot.png)

Flag: ```{i_can_use_a_debugger_;)}```