from itertools import product

c = 1
for w in product('ЕЛОТ', repeat=5):
    w = ''.join(w) # Для перевода из tuple в str
    if 'ЕЛ' not in w and 'ЛЕ' not in w and 'ЕЕ' not in w:
        print(c, w)
        break
    c += 1