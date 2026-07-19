from math import *

N = 3840 * 2160
i = 17
V = N * i

N_2 = 1280 * 720
i_2 = 5
V_2 = N_2 * i_2

print((V - V_2) * 120 / 8 / 1024)