from functools import lru_cache

def moves(cp):
    a, b = cp
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)

@lru_cache(None)
def game(cp):
    if sum(cp) >= 227: return 'W'
    if any(game(x) == 'W' for x in moves(cp)): return 'P1'
    if all(game(x) == 'P1' for x in moves(cp)): return 'B1'
    if any(game(x) == 'B1' for x in moves(cp)): return 'P2'
    if all(game(x) == 'P1' or game(x) == 'P2' for x in moves(cp)): return 'B2'

for S in range(1, 209):
    if game((17, S)) == 'B2':
        print(S)

# 53
# 96, 104
# 95