from math import *

N = 440
for n in range(1, 1000):
    i = ceil(log2(n))
    V = ceil(N * i / 8)
    if V * 1892412 >= 305726 * 1024:
        print(n)
        break