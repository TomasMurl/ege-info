from math import *

N = 105
n = 10 + 1500
i = ceil(log2(n))

Id = ceil(N * i / 8)
print(Id * 16384 / 1024)