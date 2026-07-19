from math import *

N = 294
n = 10 + 4550
i = ceil(log2(n)) # Бит
id = ceil(N * i / 8) # Байты

print(id * 131072 / 1024)