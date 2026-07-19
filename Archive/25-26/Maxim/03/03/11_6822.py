from math import *

N = 10
n = 52
i = ceil(log2(n))
pd = ceil(N * i / 8) # Байты
print(pd * 65536 / 1024)