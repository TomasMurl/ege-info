from math import *

N = 640 * 256
V = 170 * 1024 * 8
i = V / N
k = 135 / 100

V_n = V * k
print(V_n)

i = V_n // N
print(i)
