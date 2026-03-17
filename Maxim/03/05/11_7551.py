from math import *

n = 10 + 26 + 450
i = ceil(log2(n))

for N in range(2, 10000):
    sn = ceil(N * i / 8) # 324 бит -> 80,5 Байт -> 81 Байт
    if sn * 708 > 213 * 1024:
        print(N)
        break