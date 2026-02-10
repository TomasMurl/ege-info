from math import *

N = 1024 * 768
i = ceil(log2(4096)) # б
v = 1_310_720 # б/с
t = 300 # с

V = v * t # всего информации за 300 секунд
V_k = N * i
print(V // V_k)
