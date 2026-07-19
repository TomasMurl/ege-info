from math import *

for n in range(1, 10000):
    N = 36
    i = ceil(log2(n))
    V = ceil(N * i / 8)

    if V * 1_000_000 >= 52 * 1024 * 1024:
        print(n)
        break