from sys import setrecursionlimit
from functools import lru_cache
setrecursionlimit(100000000)

@lru_cache(None)
def F(n):
    if n >= 2025:
        return n
    if n < 2025:
        return F(n+1)-F(n+2)+7

print(F(15)-F(24))