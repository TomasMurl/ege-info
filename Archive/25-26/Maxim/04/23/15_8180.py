from itertools import combinations

B = range(36, 76)
C = range(60, 111)

def f(x, A):
    return (not (x in A)) <= ((x in B) == (x in C))

m = 9999999999
for c in combinations(range(200), 2):
    A = range(c[0], c[1])
    if all(f(x, A) for x in range(200)):
        l = c[1] - 1 - c[0]
        if l < m:
            m = l
print(m)