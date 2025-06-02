from math import *
N = 1920 * 1080
i = ceil(log2(2 ** 24))
V = N * i
N_2 = 1280 * 1024
i_2 = 23
V_2 = N_2 * i_2
e = V - V_2 # bit
print( e * 120 / 8 / 1024 )