from itertools import permutations

c = 0
for w in permutations('0123456789', 4):
    w = ''.join(w)
    if w[0] != '0' and int(w[0]) % 2 != int(w[1]) % 2 and int(w[1]) % 2 != int(w[2]) % 2 and int(w[2]) % 2 != int(w[3]) % 2:
        c = c + 1
print(c)