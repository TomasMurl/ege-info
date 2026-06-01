from functools import lru_cache
# Победа, когда s1 + s2 >= 207

def moves(s):
    s1, s2 = s
    # +1, *2
    return (s1 + 1, s2), (s1, s2 + 1), (s1 * 2, s2), (s1, s2 * 2)

@lru_cache(None)
def game(s):
    if sum(s) >= 207: return 'W'
    if any( game(x) == 'W' for x in moves(s) ): return 'P1'
    if all( game(x) == 'P1' for x in moves(s) ): return 'B1'
    if any( game(x) == 'B1' for x in moves(s) ): return 'P2'
    if all( game(x) == 'P1' or game(x) == 'P2' for x in moves(s) ): return 'B2'

for s2 in range(2, 190):
    m = (17, s2)
    r = game(m)
    if r:
        print(s2, r)

# 48
# 86, 94
# 85