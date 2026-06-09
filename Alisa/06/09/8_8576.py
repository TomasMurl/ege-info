from itertools import product

c = 1
for w in product('АГИНРТ', repeat=6):
    w = ''.join(w)
    if c % 2 == 1 and w[0] not in 'АИГ' and w.count('А') == 1:
        print(c, w)
        break
    c = c + 1