from itertools import product

for c, w in enumerate(product('КОСУФ', repeat=5), start=1):
    w = ''.join(w)

    # if w.count('Ф') == 0
    if 'Ф' not in w and w.count('У') == 2:
        print(c, w)