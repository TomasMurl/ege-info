from itertools import product

c = 0
for w in product('МАСЛО', repeat=6):
    w = ''.join(w)
    if w.count('С') == 1 and \
        w[0] not in 'АО' and \
        w[-1] not in 'МСЛ':
        c = c + 1
print(c)