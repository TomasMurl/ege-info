from itertools import product

alf = "0123456"
words = product(alf, repeat=7)

c = 0
for w in words:
    w = "".join(w)
    if w[0] == "0":
        continue
    # if w[0] == "3" or w[0] == "5":
    #     continue
    if w[0] in "35":
        continue
    if "22" in w and "44" in w:
        continue
    c = c + 1
print(c)