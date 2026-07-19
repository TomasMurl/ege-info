from itertools import product

c = 0
for w in product("012345678", repeat=6):
    w = ''.join(w)
    if w[0] != '0' and w[0] not in '1357' and w[-1] not in '23' and w.count('1') >= 2:
        c = c + 1
print(c)
