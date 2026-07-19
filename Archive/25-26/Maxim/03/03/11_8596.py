from math import *

n = 10 + 52 + 963
i = ceil(log2(n))

for N in range(2, 1000):
    V = ceil(N * i / 8) # Байты
    if V * 2000 / 1024 <= 693:
        print(N)