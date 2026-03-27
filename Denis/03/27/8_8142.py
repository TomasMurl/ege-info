from itertools import permutations

c = 0
for w in permutations('0123456789', 4):
    w = ''.join(w)
    f = True
    for i in range(len(w) - 1):
        if int(w[i]) % 2 == int(w[i+1]) % 2:
            f = False
    if w[0] != '0' and \
        f == True:
        c = c + 1
print(c)