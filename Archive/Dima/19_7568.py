from functools import lru_cache

def moves(m):
    a, b = m
    return (a+1,b),(a*2,b),(a,b+1),(a,b*2)

@lru_cache(None)
def game(m):
    a, b = m
    if a + b >= 227: return 'W'
    if any(game(x) == 'W' for x in moves(m)): return 'P1'
    if all(game(x) == 'P1' for x in moves(m)): return 'B1' # Если первый ход Пети неудачный, то в таком случае поменять первый all на any
    if any(game(x) == 'B1' for x in moves(m)): return 'P2'
    if all(game(x) == 'P2' or game(x) == 'P1' for x in moves(a,b)): return 'B2'

for b in range(1, 210):
    m = (17, b)
    if game(m) == 'B2':
        print(m, game(m))

# 53
# 96, 104
# 95