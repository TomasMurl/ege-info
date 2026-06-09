from math import *

n = 10 + 26 + 8164 # -> i
i = ceil(log2(n))

for N in range(1, 10000):
    sn = ceil(N * i / 8) # Б
    if sn * 835 > 156 * 1024:
        print(N)
        break