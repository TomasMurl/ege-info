from itertools import product

alf = 'АГИНРТ'
words = product(alf, repeat=6)

c = 0
for w in words:
    w = "".join(w)
    c = c + 1

    if c % 2 == 0:
        continue
    if w[0] in "АИГ":
        continue
    if w.count("А") != 1:
        continue
    print(c, w)
    break