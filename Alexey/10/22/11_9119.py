from math import *

n = 10 + 120 # i <- n
i = ceil(log2(n))
for N in range(1, 1000):
    V = ceil(N * i / 8)
    if V * 12755226 <= 5 * 1024 * 1024 * 1024:
        print(N)