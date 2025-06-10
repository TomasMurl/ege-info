from sys import setrecursionlimit
from functools import lru_cache
setrecursionlimit(1000000)

@lru_cache(None)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n ** 2 + F(n-1)

print(F(2025)-F(2022))