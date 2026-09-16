from itertools import product

c = 0
for w in product('МАСЛО', repeat=6):
    w = ''.join(w)
    if w[0] not in 'АО' and w[5] not in 'МСЛ' and w.count('С') == 1:
        c += 1
print(c)