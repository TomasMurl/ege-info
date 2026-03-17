from itertools import product

alf = "МАСЛО"
words = product(alf, repeat=6)

c = 0
for w in words:
    wo = "".join(w)
    if wo.count('С') != 1:
        continue
    if wo[0] in 'АО':
        continue
    if wo[5] in 'МСЛ':
        continue
    c = c + 1
print(c)
