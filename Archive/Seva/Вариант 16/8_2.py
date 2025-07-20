from itertools import *

alf = "АВНРЬЯ"

words = product(alf, repeat = 5)

c = 0
for word in words:
    stroka = "".join(word)
    c += 1
    if stroka[0] != "Я" and stroka.count("Ь") <= 1 and "ЯЯ" not in stroka:
        print(c, stroka)