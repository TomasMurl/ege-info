from itertools import product

c = 0
for w in product('ЕИЙКНОТ', repeat=7):
    w = ''.join(w)
    if 'КОТ' in w:
        c = c + 1
print(c)