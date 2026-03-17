from math import *

N = 10
n = 52
i = ceil(log2(n))
Id = ceil(N * i / 8)
print(Id * 65536 / 1024)