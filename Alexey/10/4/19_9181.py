from functools import lru_cache

def moves(cp):
    return cp - 3, cp - 7, cp // 4

@lru_cache(None)
def game(cp):
    if cp <= 15: return 'W'
    if any(game(x) == 'W' for x in moves(cp)): return 'P1'
    if all(game(x) == 'P1' for x in moves(cp)): return 'B1'
    if any(game(x) == 'B1' for x in moves(cp)): return 'P2'
    if all(game(x) == 'P1' or game(x) == 'P2' for x in moves(cp)): return 'B2'

for sp in range(16, 90):
    if game(sp) == 'B2':
        print(sp)

# 64
# 67, 68
# 70