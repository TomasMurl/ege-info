from itertools import product

c = 1
for w in product('ЕИОРТЯ', repeat=6):
    w = ''.join(w)
    if c % 2 == 1 and w[0] not in 'ЕИО' and w.count('Т') == 1:
        print(c, w)
    c += 1