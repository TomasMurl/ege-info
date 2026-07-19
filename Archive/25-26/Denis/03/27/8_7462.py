from itertools import product

c = 0
for w in product('012345678', repeat=5):
    w = ''.join(w)
    f = True
    for i in range(len(w) - 1):
        if w[i] == '0' and w[i+1] in '1357' or \
            w[i] in '1357' and w[i + 1] == '0':
            f = False
    if w[0] != '0' and \
        w.count('0') == 1 and \
        f == True:
        c = c + 1
print(c)