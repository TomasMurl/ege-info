from math import *

N = 257
n = 17 + 4080
i = ceil(log2(n))
V = ceil(N * i / 8)
print(V * 8388608 / 1024 / 1024)