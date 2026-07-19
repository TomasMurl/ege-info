from itertools import product

c = 0
for w in product('012345678', repeat=5):
    w = ''.join(w)
    if w[0] not in '01357' and \
            w[-1] not in '18' and \
            w.count('3') <= 1:
        c = c + 1
print(c)