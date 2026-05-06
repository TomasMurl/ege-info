from functools import lru_cache

def moves(h):
    a, b = h
    return (a + 1, b), (a * 3, b), (a, b + 1), (a, b * 3)

@lru_cache(None)
def game(s):
    a, b = s
    if a + b >= 65: return "W"
    if any(game(x) == "W" for x in moves(s)): return "P1"
    if all(game(x) == "P1" for x in moves(s)): return "B1"
    if any(game(x) == "B1" for x in moves(s)): return "P2"
    if all(game(x) == "P2" or game(x) == "P1" for x in moves(s)): return "B2"

for i in range(2, 58):
    if game((6, i)) == "B2":
        print(i)