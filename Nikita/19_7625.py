from functools import lru_cache
# уменьшение количества камней
def moves(h):
    a = [h-2, h-5, h // 3]
    a = [x for x in a if x > 0]
    return a

@lru_cache(None)
def game(m):
    if m <= 19: return "W"
    if any(game(x) == "W" for x in moves(m)): return "P1"
    if all(game(x) == "P1" for x in moves(m)): return "B1" # при неудачной игре Пети заменяем all на any
    if any(game(x) == "B1" for x in moves(m)): return "P2"
    if all(game(x) == "P1" or game(x) == "P2" for x in moves(m)): return "B2"

for i in range(20, 100):
    if game(i) == "B2":
        print(i, game(i))