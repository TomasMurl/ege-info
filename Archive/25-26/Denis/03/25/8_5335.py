from itertools import product

c = 0
for w in product('01234567', repeat=5):
    w = ''.join(w)
    if w.count('6') == 1 and \
        '16' not in w and \
        '61' not in w and \
        '36' not in w and \
        '63' not in w and \
        '56' not in w and \
        '65' not in w and \
        '76' not in w and \
        '67' not in w and \
        w[0] != '0':
        c = c + 1
print(c)