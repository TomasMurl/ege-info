from math import *

V_t = 1 * 1024 * 1024 * 8
V_min = 2 * 1024 * 8

t = V_t / V_min * 60
k = 2
I = 48000
i = 16

V = (k * I * i * t) * 0.32

print(V / 8 / 1024 / 1024 / 50)