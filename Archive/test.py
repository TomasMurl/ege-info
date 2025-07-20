from itertools import *

def f(x, c):
    A = range(c[0], c[1] + 1)
    P = range(13, 20)
    Q = range(17, 24)
    return (not ((not (x in P)) <= (x in Q))) <= ((x in A) <= ((not (x in Q)) <= (x in P)))

otrezki = combinations(range(500), 2)
min_len = 0
for o in otrezki:
    if all(f(x, o) for x in range(500)):
        min_len = max(min_len, o[1] - o[0])
print(min_len)