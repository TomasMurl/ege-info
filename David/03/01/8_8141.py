from itertools import product

alf = "АБДЕОП"
words = product(alf, repeat=6)

c = 0
for w in words:
    w = "".join(w)
    c = c + 1

    if c % 2 != 0:
        continue
    if w[0] != "О":
        continue

    flag = True
    for i in w:
        if w.count(i) > 1:
            flag = False
    if not flag:
        continue
    print(c, w)
