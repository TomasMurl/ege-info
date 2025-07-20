from functools import lru_cache
# неудачный ход Пети
def moves(h):
    return h+2, h+4, h*3

@lru_cache(None)
def game(m):
    if m >= 82: return "W"
    if any(game(x) == "W" for x in moves(m)): return "P1"
    if all(game(x) == "P1" for x in moves(m)): return "B1"
    if any(game(x) == "B1" for x in moves(m)): return "P2"
    if all(game(x) == "P1" or game(x) == "P2" for x in moves(m)): return "B2"

for i in range(1, 82):
    if game(i) == "B2":
        print(i, game(i))