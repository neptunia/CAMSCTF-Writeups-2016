factor = 2**14 # 16384
smallest = (10**9//factor+1)*factor
n = smallest
print(n)
s = 0
while n < 10**10:
    if str(n) == str(n)[::-1]:
        s += n
    n += factor
print(s)
