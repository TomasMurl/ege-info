from sys import setrecursionlimit
from functools import lru_cache
setrecursionlimit(1000000)

@lru_cache(None)
def F(n):
    if n < 2:
        return n
    if n >= 2:
        return F(n//2) + F(n%2)


print(2 ** 30)
# c = 0
# for n in range(1, 2 ** 30):
#     if F(n) == 27:
#         c = c + 1
#         print(c)