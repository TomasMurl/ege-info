from functools import *
def moves(s):
    a, b = s
    return (a + 1, b), (a, b + 1), (a * 2, b), (a, b * 2)

@lru_cache(None)
def game(s):
    if sum(s) >= 227:
        return 'W'
    if any(game(x) == 'W' for x in moves(s)): return 'P1' # 0
    if all(game(x) == 'P1' for x in moves(s)): return 'B1' # 1
    if any(game(x) == 'B1' for x in moves(s)): return 'P2' # 2
    if all(game(x) == 'P1' or game(x) == 'P2' for x in moves(s)): return 'B2' # 3

for s in range(1, 210):
    s1 = (17, s)
    if game(s1) == 'B1':
        print(s, game(s1))

# for s in range(1, 210):
#     s1 = (17, s)
#     if game(s1) == 'P2':
#         print(s, game(s1))

# for s in range(1, 210):
#     s1 = (17, s)
#     if game(s1) == 'B2':
#         print(s, game(s1))