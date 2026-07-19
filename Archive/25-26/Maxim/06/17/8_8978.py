from itertools import product

c = 1
for w in product("ИРСТУЦ", repeat=5):
    w = ''.join(w)
    if w.count('И') == 2 and 'ЦЦ' not in w:
        print(c, w)
    c = c + 1