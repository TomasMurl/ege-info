from math import *

N = 3840 * 2160
i = 20
V = N * i

N_2 = 640 * 480

for n_2 in range(1, 10000):
    i_2 = ceil(log2(n_2))
    V_2 = N_2 * i_2
    e = V - V_2
    if e * 120 >= 2385004 * 1024 * 8:
        print(n_2)
# 512