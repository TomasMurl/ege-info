# 1. moves() - шаги
# 2. game() - основная логика
from functools import lru_cache
def moves(h):
    a = [h - 2, h // 2]
    a = [i for i in a if i >= 0]
    return a

@lru_cache(None)
def game(s):
    if s <= 87:
        return 'W'
    if any( game(x) == 'W' for x in moves(s) ): return "P1" # 0)
    if all( game(x) == "P1" for x in moves(s)): return "B1" # 1)
    if any( game(x) == 'B1' for x in moves(s) ): return "P2" # 2)
    if all( game(x) == "P1" or game(x) == "P2" for x in moves(s)): return "B2" # 3)

for s in range(88, 200):
    if game(s) == "B1":
        print(s, "B1")

for s in range(88, 200):
    if game(s) == "P2":
        print(s, "P2")
        
for s in range(88, 200):
    if game(s) == "B2":
        print(s, "B2")