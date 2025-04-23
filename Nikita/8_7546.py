from itertools import *

alf = "0123456789ABCD"
c = 0
for word in product(alf, repeat=5):
    flag = True
    if word[0] == "0":
        flag = False
    if word.count("9") != 1:
        flag = False
    summa_10 = 0
    summa_10 += word.count("B") + word.count("C") + word.count("D") 
    if summa_10 > 3:
        flag = False
    if flag:
        c += 1
print(c)