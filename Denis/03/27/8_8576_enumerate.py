from itertools import product

for c, w in enumerate(product('АГИНРТ', repeat=6), start=1):
    w = ''.join(w)

    if c % 2 == 1 and w[0] not in 'АИГ' and w.count('А') == 1:
        print(c, w)
        break