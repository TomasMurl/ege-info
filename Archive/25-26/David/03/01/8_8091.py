from itertools import product

alf = "ДГИАШЭ"
words = product(alf, repeat=5)

c = 0
for w in words:
    w = "".join(w)
    # if w[0] == "И" or w[0] == "А" or w[0] == "Э":
    #     continue
    if w[0] in "ИАЭ":
        continue
    if w[4] in "ДГШ":
        continue
    c = c + 1
print(c)