from itertools import *

alf = "МАСЛО"

c = 0
p = 0
words = product(alf, repeat=6)
for word in words:
    p += 1
    s = "".join(word)
    flag = True
    if s.count("С") != 1 or s[0] in 'АО' or s[-1] in 'МСЛ':
        flag = False
    if flag == True:
        c += 1
        print(s)
print(c, p)