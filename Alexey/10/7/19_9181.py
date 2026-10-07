from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(1000000)

def moves(cp):
    a, b = cp
    m = []
    if a - 2 >= 0:
        m.append((a - 2, b))
    if b - 2 >= 0:
        m.append((a, b - 2))
    if a != 0:
        m.append((a // 3, b))
    if b != 0:
        m.append((a, b // 3))
    return m

@lru_cache(None)
def game(cp):
    if sum(cp) <= 47: return 'W'
    if any(game(x) == 'W' for x in moves(cp)): return 'P1'
    if all(game(x) == 'P1' for x in moves(cp)): return 'B1'
    if any(game(x) == 'B1' for x in moves(cp)): return 'P2'
    if all(game(x) == 'P2' or game(x) == 'P1' for x in moves(cp)): return 'B2'

for S in range(32, 400):
    if game((16, S)) == 'B2':
        print(S)

# 34
# 98, 293
# 100