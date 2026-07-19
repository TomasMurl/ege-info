from math import *

N = 150
for n in range(1, 100000):
    i = ceil(log2(n))
    V = ceil(N * i / 8)
    if V * 990200 <= 230 * 1024 * 1024:
        print(n)
# 4096