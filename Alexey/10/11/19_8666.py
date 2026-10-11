from functools import lru_cache

def moves(cp):
    return cp + 2, cp + 4, cp * 2

@lru_cache(None)
def game(cp):
    if cp >= 125: return 'W'
    if any(game(x) == 'W' for x in moves(cp)): return 'P1'
    if all(game(x) == 'P1' for x in moves(cp)): return 'B1'
    if any(game(x) == 'B1' for x in moves(cp)): return 'P2'
    if all(game(x) == 'P1' or game(x) == 'P2' for x in moves(cp)): return 'B2'

for cp in range(1, 125):
    if game(cp) == 'B2':
        print(cp)

# 61
# 31, 57
# 55