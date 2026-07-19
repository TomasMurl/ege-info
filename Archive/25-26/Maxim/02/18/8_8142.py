from itertools import permutations

alf = "0123456789"
words = permutations(alf, 4)

c = 0
for word in words:
    w = "".join(word)
    if w[0] == '0':
        continue
    flag = True
    for i in range(len(w) - 1):
        if int(w[i]) % 2 == int(w[i+1]) % 2:
            flag = False
    if flag:
        c = c + 1
print(c)