from math import *

N = 294
n = 10 + 4550
i = ceil(log2(n))
Id = ceil(N * i / 8)
print(Id * 131072 / 1024)