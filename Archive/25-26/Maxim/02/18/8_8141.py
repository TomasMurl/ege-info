from itertools import product

alf = sorted("ПОБЕДА")
words = product(alf, repeat=6)

c = 0
for word in words:
    w = "".join(word)
    c = c + 1
    if c % 2 == 1:
        continue
    if w[0] != "О":
        continue
    flag = True
    for s in w:
        if w.count(s) > 1:
            flag = False
    if flag:
        print(c, w)