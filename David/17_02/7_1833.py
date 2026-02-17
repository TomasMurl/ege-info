from math import *

I = 60 # кадров в секунду
n = 65536
i = ceil(log2(n))
print(i)
t = 60
V = 12 * 1024 * 1024 * 8

N = V / (i * I * t)
print()