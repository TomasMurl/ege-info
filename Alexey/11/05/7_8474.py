from math import *

for palitra in range(1, 2048):
    x = ceil(log2(palitra))
    n = 120 * 3840 * 2160 * 20
    y = 120 * 640 * 480 * x
    c = 2385004 * 1024 * 8
    if n - y >= c:
        print(palitra)