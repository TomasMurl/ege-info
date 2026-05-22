from itertools import product

c = 1
for w in product('АБДЕОП', repeat=6):
    w = ''.join(w)
    if c % 2 == 0 and w[0] == 'О' and w.count(w[0]) == 1 and w.count(w[1]) == 1 and w.count(w[2]) == 1 and w.count(w[3]) == 1 and w.count(w[4]) == 1 and w.count(w[5]) == 1:
        print(c, w)
    c += 1