from math import *

n = 10 + 52 + 458
i = ceil(log2(n))
for N in range(1, 1000):
    sn = ceil(N * i / 8)
    if sn * 862 <= 276 * 1024:
        print(N)