from math import *

i = ceil(log2(2 ** 24))
N = 1920 * 1080

N_2 = 1280 * 1024
i_2 = 23

econ = (i * N - N_2 * i_2) * 120
print(econ // 8 // 1024)