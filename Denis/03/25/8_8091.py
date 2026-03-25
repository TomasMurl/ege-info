from itertools import product

c = 0
for w in product('ДГИАШЭ', repeat=5):
    w = ''.join(w)
    if w[0] not in 'ИАЭ' and \
        w[-1] not in 'ДГШ':
        c = c + 1
print(c)