from math import *

k = 4
I = 192000
i = 16 # бит
V = 967 * 1024 * 1024 * 8

t = V / (k * I * i)
print(t / 60)