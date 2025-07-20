from math import *

for n in range(2, 1000):
    l = 377
    i = ceil(log2(n))
    sn = ceil(l * i / 8)
    if sn * 23155 > 5536 * 1024:
        print(n)
        break