from math import *

for N in range(1, 10000):
    n = 10 + 26 + 34
    i = ceil(log2(n))
    V = ceil(N * i / 8)

    if V * 1142 > 305 * 1024:
        print(N)
        break