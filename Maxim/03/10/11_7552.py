from math import *

n = 10 + 2030
i = ceil(log2(n))
for N in range(2, 1000):
    sn = ceil(N * i / 8)
    if sn * 318 > 67 * 1024:
        print(N)
        break