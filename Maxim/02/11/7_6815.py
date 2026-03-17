from math import *

k = 2
I = 48000
i = 24
V = 288 * 1024 * 1024 * 8

t = V / k / I / i
print(t / 60)