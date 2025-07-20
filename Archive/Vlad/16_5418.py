from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10000000)
@lru_cache(None)
def F(n):
    if n < 2:
        return n
    if n >= 2 and n % 2 == 0:
        return F(n // 2) + 1
    if n >= 2 and n % 2 != 0:
        return F(3*n + 1) + 1

c = 0
for n in range(1,100001):
    if F(n) == 16:
        c = c + 1
print(c)

# F(2) = F(1) + 1 = 1 + 1 = 2
# F(1) = 1

# F(10) = F(5) + 1 = 7
# F(5) = F(16) + 1 = 6
# F(16) = F(8) + 1 = 5
# F(8) = F(4) + 1 = 4
# F(4) = F(2) + 1 = 3