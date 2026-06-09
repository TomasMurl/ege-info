from itertools import product

c = 0
for w in product('0123456789AB', repeat=5):
    w = ''.join(w)
    n = 0
    if int(w[0], 12) > 8:
        n = n + 1
    if int(w[1], 12) > 8:
        n = n + 1
    if int(w[2], 12) > 8:
        n = n + 1
    if int(w[3], 12) > 8:
        n = n + 1
    if int(w[4], 12) > 8:
        n = n + 1

    if w[0] != '0' and w.count('7') == 1 and n <= 3:
        c = c + 1
print(c)
