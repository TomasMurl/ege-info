from math import *

N = 192 * 960
for n in range(1, 1000):
    i = ceil(log2(n))
    V = N * i * 0.85 / 8 / 1024
    if V < 90:
        print(n)
