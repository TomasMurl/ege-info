from functools import lru_cache

def moves(h):
    a, b = h
    return (a+1, b), (a*2, b), (a, b+1), (a, b*2)

@lru_cache(None)
def game(s):
    a, b = s
    if a + b >= 227: return 'W'
    if any(game(x) == 'W' for x in moves(s)): return 'P1'
    if all(game(x) == 'P1' for x in moves(s)): return 'B1' # если Петя делает неудачный ход, то здесь меняем на any
    if any(game(x) == 'B1' for x in moves(s)): return 'P2'
    if all(game(x) == 'P1' or game(x) == 'P2' for x in moves(s)): return 'B2'

for s in range(1, 210):
    if game((17, s)) == 'B2':
        print(s, game((17, s)))