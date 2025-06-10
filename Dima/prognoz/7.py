from math import *
N = 1920 * 1080
n = 2 ** 22
i = ceil(log2(n))
s1 = N * i # bit
N2 = 1280 * 1024
i2 = 21
s2 = N2 * i2
eco = s1 - s2 # bit
print(eco * 120 // 8 // 1024)