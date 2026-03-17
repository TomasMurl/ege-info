from math import *

N = 2783
for n in range(1, 10000):
    i = ceil(log2(n))
    sn = ceil(N * i / 8)
    if sn * 3845627 >= 11 * 1024 * 1024 * 1024:
        print(n)
        break