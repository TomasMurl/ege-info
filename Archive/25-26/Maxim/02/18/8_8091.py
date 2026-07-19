from itertools import product

alf = "ДГИАШЭ"
words = product(alf, repeat=5)

c = 0
for word in words:
    w = "".join(word)
    if w[0] in "ИАЭ":
        continue
    if w[4] in "ДГШ":
        continue
    c = c + 1
print(c)