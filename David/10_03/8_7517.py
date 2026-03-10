from itertools import product

alf = "КОСУФ"
words = product(alf, repeat=5)
c = 0
for w in words:
    w = "".join(w)
    c = c + 1

    if w.count("Ф") > 0:
        continue
    if w.count("У") != 2:
        continue
    print(c, w)