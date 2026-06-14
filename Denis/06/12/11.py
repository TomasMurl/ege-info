from math import *

# N - ?
n = 10 + 62
i = ceil(log2(n))
for N in range(1, 10000):
    V = ceil(N * i / 8)
    if V * 5895222 > 23 * 1024 * 1024:
        print(N)
        break