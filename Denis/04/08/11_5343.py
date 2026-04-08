from math import *

N = 294
n = 10 + 4550
i = ceil(log2(n))
V = ceil(N * i / 8)
print(V * 131072 / 1024)