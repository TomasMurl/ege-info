from itertools import product

alf = "012345678"
words = product(alf, repeat=6)

c = 0
for w in words:
    w = "".join(w)
    if w[0] == '0':
        continue
    if w[0] in '1357':
        continue
    if w[5] in '23':
        continue
    if w.count('1') < 2:
        continue
    c = c + 1
print(c)