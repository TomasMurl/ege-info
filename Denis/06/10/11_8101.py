from math import *

N = 15
n = 12 # -> i
i = ceil(log2(n))
V = N * i
V = V + 12 * 8
V = ceil(V / 8)
print(V * 50)