from math import *
for l in range(1, 1000):
    n = 10 + 26 + 26
    i = ceil(log2(n))
    ID = ceil(l * i / 8)
    if ID * 1000 <= 10 * 1024:
        print(l)