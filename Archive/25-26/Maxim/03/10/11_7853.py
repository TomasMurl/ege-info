from math import *

N = 30

for tn in range(1, 10000):
    n = 26 * 2 + 10 + tn
    i = ceil(log2(n))
    uk = ceil(N * i / 8)
    if uk * 5200 <= 150 * 1024:
        print(tn)