from itertools import product

c = 0
for w in product("0123456789AB", repeat=5):
    w = ''.join(w)
    p = w.count('9') + w.count('A') + w.count('B')
    if w[0] != '0' and w.count('7') == 1 and p <= 3:
        c = c + 1
print(c)