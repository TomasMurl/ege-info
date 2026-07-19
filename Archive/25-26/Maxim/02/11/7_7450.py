from math import *

k = 2
I = 48_000
i = 34
t = 42 * 60 + 20
V_z = k * I * i * t

z = 110 * 1024 * 8 * 13

V = V_z + z

v = 314572800
print(V // v)