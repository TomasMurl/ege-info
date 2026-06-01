from functools import lru_cache

def moves(s):
    s1, s2 = s
    return (s1 + 1, s2), (s1, s2 + 1), (s1 * 3, s2), (s1, s2 * 3) # 1

@lru_cache(None)
def game(s):
    if sum(s) >= 65: return 'W' # 2
    if any( game(x) == 'W' for x in moves(s) ): return 'P1'
    if all( game(x) == 'P1' for x in moves(s) ): return 'B1'
    if any( game(x) == 'B1' for x in moves(s) ): return 'P2'
    if all( game(x) == 'P1' or game(x) == 'P2' for x in moves(s) ): return 'B2'

for s2 in range(2, 59): # 3
    m = (6, s2) # 4
    r = game(m)
    if r:
        print(s2, r)

# 7
# 10, 19
# 18