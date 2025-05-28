from itertools import *

alf = "ДГИАШЭ"

c = 0
p = 0
words = product(alf, repeat=5)
for word in words:
    p += 1
    s = "".join(word)
    flag = True
    if s[0] in 'ИАЭ' or s[-1] in 'ДГШ':
        flag = False
    if flag == True:
        c += 1
        print(s)
print(c, p)