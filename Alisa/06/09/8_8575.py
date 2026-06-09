from itertools import product

c = 1
for w in product('АКОРСТ', repeat=5):
    w = ''.join(w)
    if c % 2 == 0 and w[0] not in 'АСТ' and w.count('О') == 2:
        print(c, w)
    c = c + 1