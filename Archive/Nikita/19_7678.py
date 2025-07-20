from functools import lru_cache
#стандарт 2 кучки
def moves(h):
    a, b = h
    return (a+4, b), (a, b + 3), (a * 2, b), (a, b * 3)

@lru_cache(None)
def game(m):
    a, b = m
    if a + b >= 178: return "W"
    if any(game(x) == "W" for x in moves(m)): return "P1"
    if all(game(x) == "P1" for x in moves(m)): return "B1" # при неудачной игре Пети заменяем all на any
    if any(game(x) == "B1" for x in moves(m)): return "P2"
    if all(game(x) == "P1" or game(x) == "P2" for x in moves(m)): return "B2"
    if any(game(x) == "B1" or game(x) == "B2" for x in moves(m)): return "P3"

c = 1
for i in range(1, 157):
    s = 21, i
    if game(s) == "P3":
        c *= i
        print(i, game(s))
print(c)