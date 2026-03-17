from itertools import permutations

# 01234
# 6721

alf = "0123456789"
words = permutations(alf, 4)

c = 0
for w in words:
    w = "".join(w)
    if w[0] == "0":
        continue

    flag = True
    for i in range(3):
        if int(w[i]) % 2 == int(w[i+1]) % 2:
            flag = False
    if not flag:
        continue

    c = c + 1
print(c)