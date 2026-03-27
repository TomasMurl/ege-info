from itertools import product

for c, w in enumerate(product('ЕКМОПРТЬЮ', repeat=5), start=1):
    w = ''.join(w)

    if c % 2 == 1 and w[0] != 'Ь' and w.count('К') == 2:
        print(c, w)