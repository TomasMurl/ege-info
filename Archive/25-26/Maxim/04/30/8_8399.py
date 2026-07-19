from itertools import product, permutations

c = 0
p = list(permutations('КОТЕНОК', 7))
for w in product('АЕКНОТ', repeat=7):
    c = c + 1
    if c % 2 == 1 and w in p:
        print(c, w)
# 270297