from math import *

i = ceil(log2(2**24))
N = 3840 * 2160
SD = 16 * 1024 * 1024 * 1024 * 8 # ГБ -> б
V = N * i # б
print(V)
c = SD // V # сколько фоток вмещается на одну флешку
print(c)
print(3742 % c)
