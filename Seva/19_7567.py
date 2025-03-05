from functools import lru_cache

def moves(h):
    return h+1, h+3, h*2

@lru_cache(None)
def game(m):
    if m >= 39: return 'W'
    if any( game(x) == 'W' for x in moves(m) ): return 'P1'
    if all( game(x) == 'P1' for x in moves(m) ): return 'B1'
    if any( game(x) == 'B1' for x in moves(m) ): return 'P2'
    if all( game(x) == 'P1' or game(x) == 'P2' for x in moves(m) ): return 'B2'

for i in range(1, 39):
    print(i, game(i))