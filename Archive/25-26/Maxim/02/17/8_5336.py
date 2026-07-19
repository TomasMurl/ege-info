from itertools import product

alf = "012345678"

words = product(alf, repeat=5)
c = 0
for word in words:
    w = "".join(word)
    if w[0] == "0":
        continue
    if w[0] in "1357":
        continue
    if w[4] in "18":
        continue
    if w.count("3") > 1:
        continue
    c = c + 1
print(c)