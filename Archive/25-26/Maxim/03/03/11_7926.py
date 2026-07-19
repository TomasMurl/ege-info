from math import *

N = 377
for n in range(2, 10000):
    i = ceil(log2(n))
    sn = ceil(N * i / 8)
    V = sn * 23155 / 1024 # кБ
    if V > 5536:
        print(n)
        break