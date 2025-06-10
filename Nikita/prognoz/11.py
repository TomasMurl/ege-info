from math import *

for n in range(1, 10000):
    l = 3410
    i = ceil(log2(n))
    sn = l * i
    sn = ceil(sn / 8)
    if sn * 2984523 >= 14 * 1024 * 1024 * 1024:
        print(n)
        break