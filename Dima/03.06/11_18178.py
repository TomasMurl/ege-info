from math import *

for l in range(1000, 1, -1):
    n = 26 + 476 + 10
    i = ceil(log2(n))
    sn = ceil(l * i / 8)
    if sn * 5000 <= 1 * 1024 * 1024:
        print(l)
        break
