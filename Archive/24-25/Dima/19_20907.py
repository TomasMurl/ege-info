from functools import lru_cache

def moves(h):
    a, b = h
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)

@lru_cache(None)
def game(m):
    if sum(m) >= 81: return 'W'
    if any(game(x) == 'W' for x in moves(m)): return 'P1'
    if all(game(x) == 'P1' for x in moves(m)): return 'B1'
    if any(game(x) == 'B1' for x in moves(m)): return 'P2'
    if all(game(x) == 'P1' or game(x) == 'P2' for x in moves(m)): return 'B2'

for i in range(1, 74):
    s = (7, i)
    if game(s) == "B1":
        print(i, game(s))

for i in range(1, 74):
    s = (7, i)
    if game(s) == "P2":
        print(i, game(s))

for i in range(1, 74):
    s = (7, i)
    if game(s) == "B2":
        print(i, game(s))