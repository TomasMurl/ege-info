from functools import lru_cache

def moves(m):
    a, b = m
    return (a+1, b), (a*3, b), (a, b+1), (a, b*3)

@lru_cache(None)
def game(m):
    a, b = m
    if a + b >= 65: return 'W'
    if any( game(x) == 'W' for x in moves(m) ): return 'P1'
    if all( game(x) == 'P1' for x in moves(m) ): return 'B1' # вопрос 1 менять вот тут all на any
    if any( game(x) == 'B1' for x in moves(m) ): return 'P2' # вопрос 2
    if all( game(x) == 'P1' or game(x) == 'P2' for x in moves(m) ): return 'B2' # вопрос 3

for i in range(2, 57):
    m = (6, i)
    print(i, game(m))
# 7, 10:19, 18