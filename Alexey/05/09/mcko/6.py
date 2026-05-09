from itertools import product

for c, w in enumerate(product('АВЕНС', repeat=4), start=1):
    w = ''.join(w)
    if w.count('Е') == 0 and 'АА' not in w:
        print(c, w)
        break