from itertools import product

c = 0
for w in product('0123456789AB', repeat=5):
    w = ''.join(w)
    if w[0] != '0' and w.count('7') == 1 and w.count('9') + w.count('A') + w.count('B') <= 3:
        c = c + 1
print(c)