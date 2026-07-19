from itertools import product

alf = "МАСЛО"
words = product(alf, repeat=6)

c = 0
for word in words:
    w = "".join(word)
    if w.count("С") != 1:
        continue
    if w[0] in "АО":
        continue
    if w[5] in "МСЛ":
        continue
    c = c + 1
print(c)