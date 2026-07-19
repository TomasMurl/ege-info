from itertools import product

alf = 'АКОРСТ'
# alf = sorted('СТРОКА')
words = product(alf, repeat=5)

c = 0
for w in words:
    w = "".join(w)
    c = c + 1

    if c % 2 != 0:
        continue
    if w[0] in "АСТ":
        continue
    if w.count('О') != 2:
        continue
    print(c, w)