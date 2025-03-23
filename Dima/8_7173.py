from itertools import permutations, product

alf = "ГЛУБИНА"

words_norepeat = permutations(alf, 7)

c = 0
for word in words_norepeat:
    G = word.index("Г")
    A = word.index("А")
    if G - A > 1:
        c += 1
print(c)