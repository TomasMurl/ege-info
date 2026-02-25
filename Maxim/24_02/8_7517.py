from itertools import product

alf = "косуф"
words = product(alf, repeat=5)

c = 0
for word in words:
    w = "".join(word)
    c = c + 1
    if w.count('ф') > 0:
        continue
    if w.count('у') != 2:
        continue
    print(c, w)