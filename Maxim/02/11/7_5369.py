from math import *

# i = ceil(log2(n))
# n - кол-во пикселей в палитре
# N - кол-во пикселей в картинке
N = 1024 * 120
V = 210 * 1024 * 8
i_p = V / N
i_pr = 7
i_c = i_p - i_pr
print(2 ** i_c)
