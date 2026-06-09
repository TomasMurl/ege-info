from itertools import product

c = 0
for w in product('0123456789', repeat=4):
    w = ''.join(w)
    if w[0] != '0' and w.count(w[0]) == 1 and w.count(w[1]) == 1 and w.count(w[2]) == 1 and w.count(w[3]) == 1 and int(w[0]) % 2 != int(w[1]) % 2 and int(w[1]) % 2 != int(w[2]) % 2 and int(w[2]) % 2 != int(w[3]) % 2:
        c = c + 1
print(c)