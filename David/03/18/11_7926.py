from math import *

N = 377
for n in range(1, 1000):
    i = ceil(log2(n))
    sn = ceil(N * i / 8)
    if sn * 23155 > 5536 * 1024:
        print(n)
        break