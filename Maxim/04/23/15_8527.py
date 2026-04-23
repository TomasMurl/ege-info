from itertools import combinations

P = range(25, 65)
Q = range(40, 116)

def f(x, A):
    return (x in P) <= (((x in Q) and (not (x in A))) <= (not (x in P)))

m = 999999999999
for c in combinations(range(200), 2):
    A = range(c[0], c[1])
    if all( f(x, A) for x in range(200) ):
        l = c[1] - 1 - c[0]
        if l < m:
            m = l
print(m)