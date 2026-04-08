from math import *

N = 252
n = 10 + 1700
i = ceil(log2(n))
V = ceil(N * i / 8)
print(V * 4096 / 1024)