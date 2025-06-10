from itertools import *

alf = sorted("ТЕОРИЯ")
words = product(alf, repeat=6)

c = 0
for word in words:
    s = ''.join(word)
    c += 1
    if c % 2 != 0 and s[0] not in 'ЕИО' and s.count('Т') == 1:
        print(c, s)