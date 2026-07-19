from math import *

n = 10 + 52 * 2 + 963
i = ceil(log2(n))
for N in range(1, 1000):
    V = ceil(N * i / 8)
    if V * 2000 <= 693 * 1024:
        print(N)