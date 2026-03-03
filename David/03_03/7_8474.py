from math import *

N = 3840 * 2160
i = 20

N_2 = 640 * 480

V_e = 2385004 * 1024 * 8
n = 120

V_e1 = V_e / 120

V_1 = N * i
V_2 = V_1 - V_e1

i_2 = V_2 / N_2
print(i_2)
i_2 = 9
print(2 ** i_2)

# 512