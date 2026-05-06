from itertools import *
alf = sorted("ПОБЕДА")
words = product(alf, repeat=6)
c = 0
for word in words:
    s = ''.join(word)
    c += 1
    if c % 2 == 0 and s[0] == 'О' and len(set(s)) == 6:
        print(c, s)