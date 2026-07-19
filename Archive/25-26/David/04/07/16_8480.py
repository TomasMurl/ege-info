from sys import setrecursionlimit
setrecursionlimit(250000)

# from functools import lru_cache

# @lru_cache(None)
def F(n):
    if n >= 19:
        return F(n - 4) + 3580
    if n < 19:
        return 6 * (G(n - 7) - 36)

# @lru_cache(None)
def G(n):
    if n >= 248045:
        return n // 20 + 28
    if n < 248045:
        return G(n + 9) - 4

# for n in range(248045, 0, -1):
#     G(n)

print(F(673))