from itertools import product

c = 0
for w in product('0123456', repeat=5): # 01234
    w = ''.join(w)
    if w[0] != '0' and w.count('0') == 1 and w.count('1') <= 2:
        c += 1
print(c)