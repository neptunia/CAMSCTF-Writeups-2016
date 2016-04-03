#Pure Evil - 100

	What is the sum of all ten-digit positive palindromic integers that have a factor of the first five-digit power of 2?
	The flag is in the format {answer}.

-----------

First, we note that at max this will take about 10**5 iterations (10 digits/5 digits = 5 digits). For a computer, that's not much, so that means we won't have to optimize our code!

We find that the smallest 5 digit power of 2 is `16384`. We can start from the smallest 10-digit multiple of this numner (`1000013824`) and count up by 16384s, and every time we hit a palindrome we increment our total. The final code looks like [this](solver.py):

```python
factor = 2**14 # 16384
smallest = (10**9//factor+1)*factor
n = smallest # 1000013824
s = 0
while n < 10**10:
    if str(n) == str(n)[::-1]:
        s += n
    n += factor
print(s)
```

We run this, and we get `19473563648`, which is indeed correct.

Flag: `{19473563648}`
