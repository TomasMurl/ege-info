from math import *

for l in range(1, 1000):
    n = 26 + 10 + 450
    i = ceil(log2(n))
    sn = ceil(i * l / 8)
    if sn * 708 > 213 * 1024:
        print(l)
        break
