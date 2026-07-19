from itertools import product

c = 0
for w in product('0123456', repeat=7):
    w = ''.join(w)
    # if w[0] not in '035' and not ('22' in w and '44' in w):
    #     c = c + 1
    if '22' in w and '44' in w:
        continue
    if w[0] not in '035':
        c = c + 1
print(c)