from math import *

n = 10 + 1300
i = ceil(log2(n))
N = 270
iden = ceil(N * i / 8)
V = 290 * 1024
print(V // iden)