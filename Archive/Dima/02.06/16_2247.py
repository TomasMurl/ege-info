from sys import setrecursionlimit
from functools import lru_cache
setrecursionlimit(100000000)

@lru_cache(None)
def f(n):
    if n < 3:
        return n + 1
    if n >= 3 and n % 2 == 0:
        return f(n-2) + n - 2
    # if n >= 3 and n % 2 != 0:
    #     return f(n+2) + n + 2

c = 0
# f(3) -> f(5) + n + 2 -> f(7) -> f(9) -> ...
# 1 - passed, 2 - passed, 3 - continue
for n in range(1, 100000):
    F = f(n) # None
    if F is None:
        continue
    if len(str(F)) == 5:
        c += 1
        print(F)
print(c)