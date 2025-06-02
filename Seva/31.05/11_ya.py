from math import *
for l in range(1, 1000):
    alph = 10 + 26 + 26
    i = ceil(log2(alph))
    ID = ceil(l * i / 8)
    if ID * 1000 <= 10 * 1024:
        print(l)