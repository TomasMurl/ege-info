from functools import lru_cache

def moves(m):
    a, b = m
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)

@lru_cache(None)
def game(m):
    a, b = m
    if a + b >= 207: return 'W'
    if any( game(x) == 'W' for x in moves(m) ): return 'P1'
    if all( game(x) == 'P1' for x in moves(m) ): return 'B1'
    if any( game(x) == 'B1' for x in moves(m) ): return 'P2'
    if all( game(x) == 'P2' or game(x) == 'P1' for x in moves(m) ): return 'B2'

for s2 in range(2, 190):
    r = game((17, s2))
    if r:
        print(s2, r)

# 1) 48
# 2) 86, 94
# 3) 85