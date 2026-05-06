from math import *

for n in range(1000, 2, -1):
    l = 257
    i = ceil(log2(n))
    sn = ceil(l * i / 8) # Байты
    if sn * 295740 <= 33 * 1024 * 1024:
        print(n)
        break