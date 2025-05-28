from itertools import *

alf = "0123456789"
ch = "02468"
nech = "13579"
words = permutations(alf, 4)
c = 0
for word in words:
    s = "".join(word)
    flag = True
    if s[0] == '0':
        flag = False
    for i in range(len(s) - 1):
        if s[i] in ch and s[i+1] in ch:
            flag = False
        if s[i] in nech and s[i+1] in nech:
            flag = False
    if flag == True:
        c += 1
        print(s)
print(c)