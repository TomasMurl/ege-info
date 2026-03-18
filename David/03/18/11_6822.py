from math import *

N = 10
n = 52
i = ceil(log2(n))
p = ceil(N * i / 8)
print(p * 65536 / 1024)