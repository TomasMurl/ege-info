from itertools import product

c = 1
for w in product('ВДЕЛНОПШ', repeat=5):
    w = ''.join(w)
    if c % 2 != 0 and w[0] != 'Ш' and w[4] != 'Ш' and w.count('Е') >= 2:
        print(c, w)
    c = c + 1