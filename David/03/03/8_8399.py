from itertools import product, permutations

words = []
for i in permutations("КОТЕНОК", 7):
    words.append(i)

n = 0
for w in product("АЕКНОТ", repeat=7):
    n = n + 1
    if n % 2 == 0:
        continue
    if w not in words:
        continue
    print(n, w)

# 270297