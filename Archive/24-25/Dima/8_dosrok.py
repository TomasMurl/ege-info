from itertools import product
alf = "ДГИАШЭ"
words = product(alf, repeat=5)
c = 0
for word in words:
    if word[0] in "ДГШ" and word[-1] in "ИАЭ":
        c += 1
print(c)