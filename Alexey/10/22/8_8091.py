from itertools import *

c = 0
for w in product('ДГИАШЭ', repeat=5):
    w = ''.join(w)
    if w[0] not in 'АИЭ' and w[-1] not in 'ДГШ':
        c += 1
print(c)