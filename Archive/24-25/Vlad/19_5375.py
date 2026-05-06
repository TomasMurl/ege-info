from functools import lru_cache

def moves(h):
    return h+1, h*2

@lru_cache(None)
def game(s):
    if s >= 165:
        return 'W'
    if any(game(x) == 'W' for x in moves(s)): return 'P1'
    if all(game(x) == 'P1' for x in moves(s)): return 'B1'
    if any(game(x) == 'B1' for x in moves(s)): return 'P2'
    if all(game(x) == 'P1' or game(x) == 'P2' for x in moves(s)): return 'B2'

for s in range(1, 165):
    if game(s) == 'B2':
        print(s, game(s))