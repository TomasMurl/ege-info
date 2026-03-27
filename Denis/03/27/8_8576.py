from itertools import product

c = 0
for w in product('АГИНРТ', repeat=6):
    w = ''.join(w)
    c = c + 1

    if c % 2 == 1 and \
        w[0] not in 'АИГ' and \
        w.count('А') == 1:
        print(c, w)
        break