from math import *

N1 = 3840 * 2160
i1 = 17

N2 = 1280 * 720
i2 = 5

V1 = N1 * i1
V2 = N2 * i2
e = V1 - V2
print(e * 120 / 8 / 1024)