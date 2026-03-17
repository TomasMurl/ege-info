from itertools import product

alf = "01234567"
words = product(alf, repeat=5)

c = 0
for w in words:
    w = "".join(w)
    if w[0] == "0":
        continue
    if w.count("6") != 1:
        continue
    if "16" in w or "61" in w or "36" in w or "63" in w or "56" in w or "65" in w or "76" in w or "67" in w:
        continue
    c = c + 1
print(c)