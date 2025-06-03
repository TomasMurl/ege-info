from math import *

for n in range(2, 1000):
    l = 261
    i = ceil(log2(n))
    sn = ceil(l * i / 8)
    if 252500 * sn > 31 * 1024 * 1024:
        print(n)
        break
