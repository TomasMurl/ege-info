from itertools import product

for c, w in enumerate(product('АКОРСТ', repeat=5), start=1):
    w = ''.join(w)

    if c % 2 == 0 and w[0] not in 'АСТ' and w.count('О') == 2:
        print(c, w)